// Vercel serverless function — recibe el feedback de las landings de engagement
// (reacciones, respuestas, clicks, dwell) y lo guarda en docs/sync/engagement.json
// del repo, usando un token del lado del SERVIDOR. Así el browser NO necesita
// ningún PAT y el feedback se guarda solo desde cualquier dispositivo.
//
// Config (una sola vez): en Vercel → Project → Settings → Environment Variables,
// agregar GH_FEEDBACK_TOKEN = un token de GitHub (fine-grained) con permiso
// "Contents: Read and write" sobre el repo. Nada más.

const REPO = 'Abecedeefege/Gardening';
const FILE = 'docs/sync/engagement.json';
const API = 'https://api.github.com/repos/' + REPO + '/contents/' + FILE;
const UA = 'jardineando-feedback-fn';

async function ghGet(token) {
  const r = await fetch(API + '?ref=main&_=' + Date.now(), {
    headers: { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github+json', 'User-Agent': UA },
  });
  if (r.status === 404) return { sha: null, doc: { _updated_at: null, events: [], daily_summary: {} } };
  if (!r.ok) throw new Error('GET ' + r.status);
  const meta = await r.json();
  const doc = JSON.parse(Buffer.from(meta.content, 'base64').toString('utf8'));
  return { sha: meta.sha, doc: doc };
}

async function ghPut(token, doc, sha, n, device) {
  const body = {
    message: 'engage: ' + n + ' evento(s) desde ' + (device || 'web'),
    content: Buffer.from(JSON.stringify(doc, null, 2) + '\n', 'utf8').toString('base64'),
    branch: 'main',
  };
  if (sha) body.sha = sha;
  return fetch(API, {
    method: 'PUT',
    headers: {
      Authorization: 'Bearer ' + token, Accept: 'application/vnd.github+json',
      'User-Agent': UA, 'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });

  const token = process.env.GH_FEEDBACK_TOKEN;
  if (!token) return res.status(500).json({ error: 'sin_token', hint: 'Falta GH_FEEDBACK_TOKEN en las env vars de Vercel' });

  let events, device;
  try {
    const body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
    events = body.events; device = body.device;
  } catch (e) { return res.status(400).json({ error: 'body_invalido' }); }
  if (!Array.isArray(events) || !events.length) return res.status(400).json({ error: 'sin_eventos' });

  try {
    for (let attempt = 0; attempt < 3; attempt++) {
      const { sha, doc } = await ghGet(token);
      const have = {};
      (doc.events || []).forEach((e) => { if (e && e._id) have[e._id] = 1; });
      const toAdd = events.filter((e) => !e._id || !have[e._id]);
      if (!toAdd.length) return res.status(200).json({ ok: true, added: 0 });
      doc.events = (doc.events || []).concat(toAdd);
      doc._updated_at = new Date().toISOString();
      const put = await ghPut(token, doc, sha, toAdd.length, device);
      if (put.ok) return res.status(200).json({ ok: true, added: toAdd.length });
      if (put.status === 409) continue; // sha viejo (alguien escribió en el medio) → reintentar
      const detail = await put.text().catch(() => '');
      return res.status(502).json({ error: 'github_put_' + put.status, detail: detail.slice(0, 160) });
    }
    return res.status(409).json({ error: 'conflictos_repetidos' });
  } catch (e) {
    return res.status(502).json({ error: 'excepcion', detail: String(e).slice(0, 160) });
  }
};
