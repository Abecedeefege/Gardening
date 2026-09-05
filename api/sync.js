// Vercel serverless function — backend de TODO lo que el sitio principal
// escribe al repo (antes lo hacía el browser con un PAT por dispositivo).
// Con esto, celular / Mac / PC escriben igual, sin configurar nada.
//
//   GET  /api/sync            → { ok, github: <status del token> }  (health check)
//   GET  /api/sync?doc=task_states|user_tasks → { ok, doc } leído FRESCO del repo
//   POST /api/sync  { op, device, ... }
//     states_merge      { tasks }            → merge LWW en docs/sync/task_states.json, devuelve el merged
//     user_tasks_merge  { tasks }            → merge LWW en docs/sync/user_tasks.json, devuelve el merged
//     uploads_append    { bucket, entry }    → append a docs/uploads.json[bucket] (dedupe por filename/_stamp+task_id)
//     photo_put         { bucket, filename, base64 } → docs/images/uploads/<bucket>/<filename>
//     push_subscription { doc }              → docs/sync/push_subscription.json (reemplaza)
//
// Mismo token de servidor que api/feedback.js y api/tarea.js (GH_FEEDBACK_TOKEN).

const gh = require('./_gh');

const STATES_FILE = 'docs/sync/task_states.json';
const USER_TASKS_FILE = 'docs/sync/user_tasks.json';
const UPLOADS_INDEX = 'docs/uploads.json';
const UPLOADS_DIR = 'docs/images/uploads/';
const PUSH_SUB_FILE = 'docs/sync/push_subscription.json';

const BUCKET_RE = /^[A-Za-z0-9_][A-Za-z0-9_-]{0,15}$/;      // B-5a, _general, B-46
const FILENAME_RE = /^[A-Za-z0-9][A-Za-z0-9_.-]{0,80}\.jpg$/;
const MAX_PHOTO_B64 = 3.5 * 1024 * 1024;
const MAX_TASKS = 2000;

function lww(remote, local, tsOf) {
  // Last-write-wins por id — misma regla que usaba el cliente.
  const merged = Object.assign({}, remote || {});
  Object.keys(local || {}).forEach((id) => {
    if (!/^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$/.test(id)) return;
    const l = local[id];
    if (!l || typeof l !== 'object') return;
    const r = merged[id];
    if (!r || String(tsOf(l)) >= String(tsOf(r))) merged[id] = l;
  });
  return merged;
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(204).end();

  const token = process.env.GH_FEEDBACK_TOKEN;
  if (!token) return res.status(500).json({ error: 'sin_token', hint: 'Falta GH_FEEDBACK_TOKEN en las env vars de Vercel' });

  if (req.method === 'GET') {
    const doc = (req.query && req.query.doc) || '';
    if (doc) {
      // Lectura FRESCA de un doc de sync (evita esperar el deploy estático de Vercel).
      const files = { task_states: STATES_FILE, user_tasks: USER_TASKS_FILE };
      if (!files[doc]) return res.status(400).json({ error: 'doc_invalido' });
      try {
        const got = await gh.ghGetJson(token, files[doc]);
        res.setHeader('Cache-Control', 'no-store');
        return res.status(200).json({ ok: true, doc: got.doc || { tasks: {} } });
      } catch (e) {
        const msg = String(e && e.message || e);
        return res.status(502).json({ error: /: 401\b/.test(msg) ? 'token_vencido' : 'github_get', detail: msg.slice(0, 160) });
      }
    }
    try {
      const status = await gh.ghTokenAlive(token);
      const ok = status === 200;
      return res.status(ok ? 200 : 502).json({ ok, github: status,
        hint: ok ? null : 'El token de GitHub del servidor no sirve (venció o fue revocado): renovar GH_FEEDBACK_TOKEN en Vercel' });
    } catch (e) {
      return res.status(502).json({ ok: false, error: 'github_unreachable', detail: String(e).slice(0, 160) });
    }
  }
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });

  let body;
  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
  } catch (e) { return res.status(400).json({ error: 'body_invalido' }); }

  const op = body.op;
  const device = String(body.device || 'browser').slice(0, 40);
  const nowIso = new Date().toISOString();

  try {
    if (op === 'states_merge') {
      const local = body.tasks;
      if (!local || typeof local !== 'object' || Object.keys(local).length > MAX_TASKS) return res.status(400).json({ error: 'tasks_invalido' });
      const next = await gh.updateJson(
        token, STATES_FILE, 'sync: actualizar task_states desde ' + device,
        (doc) => {
          doc = doc || {};
          doc.tasks = lww(doc.tasks, local, (s) => s.last_modified_at || '0');
          doc._synced_at = nowIso;
          doc._last_writer = device;
          return doc;
        },
        () => ({ _synced_at: nowIso, _last_writer: device, tasks: {} })
      );
      return res.status(200).json({ ok: true, tasks: next.tasks });
    }

    if (op === 'user_tasks_merge') {
      const local = body.tasks;
      if (!local || typeof local !== 'object' || Object.keys(local).length > MAX_TASKS) return res.status(400).json({ error: 'tasks_invalido' });
      const next = await gh.updateJson(
        token, USER_TASKS_FILE, 'user-tasks: actualizar desde ' + device,
        (doc) => {
          doc = doc || {};
          doc.tasks = lww(doc.tasks, local, (u) => u.last_modified_at || u.created_at || '0');
          doc._synced_at = nowIso;
          doc._last_writer = device;
          return doc;
        },
        () => ({ _synced_at: nowIso, _last_writer: device, tasks: {} })
      );
      return res.status(200).json({ ok: true, tasks: next.tasks });
    }

    if (op === 'uploads_append') {
      const bucket = String(body.bucket || '');
      const entry = body.entry;
      if (!BUCKET_RE.test(bucket)) return res.status(400).json({ error: 'bucket_invalido' });
      if (!entry || typeof entry !== 'object') return res.status(400).json({ error: 'entry_invalida' });
      if (entry.filename != null && !FILENAME_RE.test(String(entry.filename))) return res.status(400).json({ error: 'filename_invalido' });
      const safe = JSON.parse(JSON.stringify(entry));
      safe.uploaded_by = String(safe.uploaded_by || device).slice(0, 40);
      safe.via = 'api';
      await gh.updateJson(
        token, UPLOADS_INDEX, 'upload: registrar ' + (safe.filename || safe.task_id || 'entry') + ' en uploads.json desde ' + device,
        (doc) => {
          doc = doc || {};
          doc[bucket] = doc[bucket] || [];
          const dup = doc[bucket].some((u) => u && (
            (safe.filename && u.filename === safe.filename) ||
            (safe._stamp && u._stamp === safe._stamp && u.task_id === safe.task_id)
          ));
          if (!dup) doc[bucket].push(safe);
          return doc;
        },
        () => ({})
      );
      return res.status(200).json({ ok: true });
    }

    if (op === 'photo_put') {
      const bucket = String(body.bucket || '');
      const filename = String(body.filename || '');
      if (!BUCKET_RE.test(bucket)) return res.status(400).json({ error: 'bucket_invalido' });
      if (!FILENAME_RE.test(filename)) return res.status(400).json({ error: 'filename_invalido' });
      const b64 = gh.cleanBase64(body.base64);
      if (!b64 || b64.length > MAX_PHOTO_B64) return res.status(400).json({ error: 'foto_invalida_o_muy_grande' });
      const repoPath = UPLOADS_DIR + bucket + '/' + filename;
      const put = await gh.ghPutBinary(token, repoPath, b64, 'upload: ' + filename + ' desde ' + device);
      if (!put.ok) {
        const detail = await put.text().catch(() => '');
        return res.status(502).json({ error: 'github_put_foto_' + put.status, detail: detail.slice(0, 160) });
      }
      return res.status(200).json({ ok: true, repo_path: repoPath, photo_path: 'uploads/' + bucket + '/' + filename });
    }

    if (op === 'push_subscription') {
      const doc = body.doc;
      if (!doc || typeof doc !== 'object' || !doc.subscription) return res.status(400).json({ error: 'doc_invalido' });
      await gh.updateJson(
        token, PUSH_SUB_FILE, 'push: registrar suscripción desde ' + device,
        () => doc, () => doc
      );
      return res.status(200).json({ ok: true });
    }

    return res.status(400).json({ error: 'op_invalida' });
  } catch (e) {
    const msg = String(e && e.message || e);
    const tokenDead = /: 401\b/.test(msg);
    return res.status(502).json({
      error: tokenDead ? 'token_vencido' : 'excepcion',
      detail: msg.slice(0, 160),
      hint: tokenDead ? 'Renovar GH_FEEDBACK_TOKEN en Vercel (token clásico sin vencimiento)' : null,
    });
  }
};
