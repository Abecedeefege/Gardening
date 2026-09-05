// Helpers compartidos de las funciones serverless (Vercel no expone como
// endpoint los archivos que empiezan con "_"). Todo escribe al repo con el
// token del SERVIDOR (env var GH_FEEDBACK_TOKEN): el browser nunca necesita
// un PAT propio, desde ningún dispositivo.
//
// El token conviene que sea un PAT CLÁSICO con scope "repo" y "No expiration":
// los fine-grained vencen (máx. 1 año) y cuando vencen todo el sitio deja de
// poder escribir sin avisar (pasó el 05/09/2026).

const REPO = 'Abecedeefege/Gardening';
const API = 'https://api.github.com/repos/' + REPO + '/contents/';
const UA = 'jardineando-api';

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

// Read-modify-write con reintento en 409/422 (alguien escribió en el medio).
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

// Chequeo barato de que el token sigue vivo (lo usa tools/health_check.js vía
// GET /api/sync y el propio endpoint para responder 502 con causa clara).
async function ghTokenAlive(token) {
  const r = await fetch('https://api.github.com/repos/' + REPO, {
    headers: { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github+json', 'User-Agent': UA },
  });
  return r.status;
}

function cleanBase64(raw) {
  let b64 = String(raw || '');
  const comma = b64.indexOf(',');
  if (b64.slice(0, 5) === 'data:' && comma > 0) b64 = b64.slice(comma + 1);
  return b64.replace(/\s/g, '');
}

module.exports = { REPO, API, ghGetJson, ghPutJson, ghPutBinary, updateJson, ghTokenAlive, cleanBase64 };
