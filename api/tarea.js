// Vercel serverless function — backend de las landings por tarea
// (docs/tasks/<taskId>.html). Igual que api/feedback.js, escribe al repo con
// un token del lado del SERVIDOR (env var GH_FEEDBACK_TOKEN, fine-grained con
// "Contents: Read and write") — el browser NO necesita PAT.
//
//   GET  /api/tarea?task_id=X
//        → { ok, thread, state }  (lee FRESCO de GitHub: el thread de la tarea
//          + su entry en task_states.json — evita esperar el deploy de Vercel)
//
//   POST /api/tarea  { type: "message" | "photo" | "state", task_id, ... }
//        message → append a docs/sync/threads/<task_id>.json (from: "user")
//        photo   → docs/images/uploads/<plant_code>/<task_id>_<ts>.jpg
//                  + entry en docs/uploads.json (ai_status: "pending")
//                  + mensaje kind:"photo" en el thread
//        state   → merge en docs/sync/task_states.json (done/snoozed/active)
//
// El agente /responder-tareas (Routine horaria) procesa los mensajes con
// status:"pending" y contesta por push que deep-linkea a la misma landing.

const REPO = 'Abecedeefege/Gardening';
const API = 'https://api.github.com/repos/' + REPO + '/contents/';
const UA = 'jardineando-tarea-fn';

const THREADS_DIR = 'docs/sync/threads/';
const STATES_FILE = 'docs/sync/task_states.json';
const UPLOADS_INDEX = 'docs/uploads.json';
const UPLOADS_DIR = 'docs/images/uploads/';

const TASK_ID_RE = /^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$/;
const PLANT_CODE_RE = /^[A-Z]{1,2}-\d{1,3}$/;
const MAX_TEXT = 2000;
const MAX_PHOTO_B64 = 3.5 * 1024 * 1024; // ~2.6MB binario; Vercel corta el body en 4.5MB

function ghHeaders(token) {
  return {
    Authorization: 'Bearer ' + token,
    Accept: 'application/vnd.github+json',
    'User-Agent': UA,
    'Content-Type': 'application/json',
  };
}

async function ghGetJson(token, path) {
  const r = await fetch(API + path + '?ref=main&_=' + Date.now(), { headers: ghHeaders(token) });
  if (r.status === 404) return { sha: null, doc: null };
  if (!r.ok) throw new Error('GET ' + path + ': ' + r.status);
  const meta = await r.json();
  return { sha: meta.sha, doc: JSON.parse(Buffer.from(meta.content, 'base64').toString('utf8')) };
}

async function ghPutJson(token, path, doc, message, sha) {
  const body = {
    message,
    content: Buffer.from(JSON.stringify(doc, null, 2) + '\n', 'utf8').toString('base64'),
    branch: 'main',
  };
  if (sha) body.sha = sha;
  return fetch(API + path, { method: 'PUT', headers: ghHeaders(token), body: JSON.stringify(body) });
}

async function ghPutBinary(token, path, base64, message) {
  return fetch(API + path, {
    method: 'PUT',
    headers: ghHeaders(token),
    body: JSON.stringify({ message, content: base64, branch: 'main' }),
  });
}

// Update read-modify-write con retry en 409 (alguien escribió en el medio).
async function updateJson(token, path, message, mutate, init) {
  for (let attempt = 0; attempt < 3; attempt++) {
    const { sha, doc } = await ghGetJson(token, path);
    const next = mutate(doc != null ? doc : (typeof init === 'function' ? init() : init));
    const put = await ghPutJson(token, path, next, message, sha);
    if (put.ok) return next;
    if (put.status === 409 || put.status === 422) continue;
    const detail = await put.text().catch(() => '');
    throw new Error('PUT ' + path + ': ' + put.status + ' ' + detail.slice(0, 120));
  }
  throw new Error('PUT ' + path + ': conflictos repetidos');
}

function tsStamp(d) {
  const p = (n) => String(n).padStart(2, '0');
  return d.getUTCFullYear() + p(d.getUTCMonth() + 1) + p(d.getUTCDate()) +
    '-' + p(d.getUTCHours()) + p(d.getUTCMinutes()) + p(d.getUTCSeconds());
}

function newThread(taskId) {
  return { task_id: taskId, _updated_at: null, messages: [] };
}

function threadPath(taskId) {
  return THREADS_DIR + taskId + '.json';
}

function appendMessage(taskId, msg) {
  return (doc) => {
    doc.messages = doc.messages || [];
    // Dedupe por id — reintentos del outbox del cliente no duplican.
    if (msg.id && doc.messages.some((m) => m && m.id === msg.id)) return doc;
    doc.messages.push(msg);
    doc._updated_at = new Date().toISOString();
    return doc;
  };
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(204).end();

  const token = process.env.GH_FEEDBACK_TOKEN;
  if (!token) return res.status(500).json({ error: 'sin_token', hint: 'Falta GH_FEEDBACK_TOKEN en las env vars de Vercel' });

  // ---------- GET: thread + estado, fresco desde GitHub ----------
  if (req.method === 'GET') {
    const taskId = (req.query && req.query.task_id) || '';
    if (!TASK_ID_RE.test(taskId)) return res.status(400).json({ error: 'task_id_invalido' });
    try {
      const [t, s] = await Promise.all([
        ghGetJson(token, threadPath(taskId)),
        ghGetJson(token, STATES_FILE),
      ]);
      const state = s.doc && s.doc.tasks ? (s.doc.tasks[taskId] || null) : null;
      return res.status(200).json({ ok: true, thread: t.doc || newThread(taskId), state });
    } catch (e) {
      return res.status(502).json({ error: 'github_get', detail: String(e).slice(0, 160) });
    }
  }

  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });

  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) { return res.status(400).json({ error: 'body_invalido' }); }

  const { type, task_id: taskId } = body;
  if (!TASK_ID_RE.test(taskId || '')) return res.status(400).json({ error: 'task_id_invalido' });
  const device = String(body.device || 'landing').slice(0, 40);
  const now = new Date();
  const nowIso = now.toISOString();
  const text = body.text != null ? String(body.text).slice(0, MAX_TEXT) : null;
  const msgId = body.message_id && /^[A-Za-z0-9_-]{1,40}$/.test(body.message_id)
    ? body.message_id
    : 'm-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8);

  try {
    // ---------- Mensaje de texto ----------
    if (type === 'message') {
      if (!text || !text.trim()) return res.status(400).json({ error: 'sin_texto' });
      await updateJson(
        token, threadPath(taskId),
        'tarea: mensaje en ' + taskId + ' desde ' + device,
        appendMessage(taskId, {
          id: msgId, from: 'user', kind: 'text', text: text.trim(),
          photo: null, ts: nowIso, device, status: 'pending',
        }),
        () => newThread(taskId)
      );
      return res.status(200).json({ ok: true, message_id: msgId });
    }

    // ---------- Foto (+ caption opcional) ----------
    if (type === 'photo') {
      const plantCode = body.plant_code || '';
      if (!PLANT_CODE_RE.test(plantCode)) return res.status(400).json({ error: 'plant_code_invalido' });
      let b64 = String(body.base64 || '');
      const comma = b64.indexOf(',');
      if (b64.slice(0, 5) === 'data:' && comma > 0) b64 = b64.slice(comma + 1);
      b64 = b64.replace(/\s/g, '');
      if (!b64 || b64.length > MAX_PHOTO_B64) return res.status(400).json({ error: 'foto_invalida_o_muy_grande' });

      // 1. Archivo nuevo — misma convención que los uploads de tarea del Timeline.
      const filename = taskId + '_' + tsStamp(now) + '.jpg';
      const photoRepoPath = UPLOADS_DIR + plantCode + '/' + filename;
      const photoRelPath = 'uploads/' + plantCode + '/' + filename; // relativo a docs/images/
      const putPhoto = await ghPutBinary(token, photoRepoPath, b64,
        'tarea: foto en ' + taskId + ' desde ' + device);
      if (!putPhoto.ok) {
        const detail = await putPhoto.text().catch(() => '');
        return res.status(502).json({ error: 'github_put_foto_' + putPhoto.status, detail: detail.slice(0, 160) });
      }

      // 2. Índice de uploads (mismo shape que los uploads del Timeline —
      //    /actualizar-tareas y /responder-tareas lo levantan de acá).
      await updateJson(
        token, UPLOADS_INDEX,
        'tarea: indexar foto de ' + taskId + ' desde ' + device,
        (doc) => {
          doc[plantCode] = doc[plantCode] || [];
          if (!doc[plantCode].some((u) => u && u.filename === filename)) {
            doc[plantCode].push({
              filename,
              uploaded_at: nowIso,
              uploaded_by: device,
              context: 'task',
              task_id: taskId,
              task_title_snapshot: String(body.task_title || '').slice(0, 120),
              ai_status: 'pending',
              ai_evaluation: null,
              user_context: text ? text.trim() : '',
              via: 'landing',
            });
          }
          return doc;
        },
        () => ({})
      );

      // 3. Mensaje en el thread.
      await updateJson(
        token, threadPath(taskId),
        'tarea: foto en thread ' + taskId + ' desde ' + device,
        appendMessage(taskId, {
          id: msgId, from: 'user', kind: 'photo', text: text ? text.trim() : null,
          photo: photoRelPath, ts: nowIso, device, status: 'pending',
        }),
        () => newThread(taskId)
      );
      return res.status(200).json({ ok: true, message_id: msgId, photo_path: photoRelPath });
    }

    // ---------- Cambio de estado (hecha / posponer / reactivar) ----------
    if (type === 'state') {
      const status = body.status;
      if (['done', 'snoozed', 'active'].indexOf(status) === -1) {
        return res.status(400).json({ error: 'status_invalido' });
      }
      let snoozedUntil = null;
      if (status === 'snoozed') {
        snoozedUntil = String(body.snoozed_until || '');
        if (isNaN(Date.parse(snoozedUntil))) return res.status(400).json({ error: 'snoozed_until_invalido' });
      }
      await updateJson(
        token, STATES_FILE,
        'tarea: ' + taskId + ' → ' + status + ' desde ' + device,
        (doc) => {
          doc.tasks = doc.tasks || {};
          const prev = doc.tasks[taskId] || {};
          doc.tasks[taskId] = Object.assign({}, prev, {
            status,
            snoozed_until: snoozedUntil,
            completed_at: status === 'done' ? nowIso : null,
            last_modified_at: nowIso,
            changed_via: 'landing',
          });
          doc._synced_at = nowIso;
          doc._last_writer = device;
          return doc;
        },
        () => ({ _synced_at: nowIso, _last_writer: device, tasks: {} })
      );
      return res.status(200).json({ ok: true });
    }

    return res.status(400).json({ error: 'type_invalido' });
  } catch (e) {
    return res.status(502).json({ error: 'excepcion', detail: String(e).slice(0, 160) });
  }
};
