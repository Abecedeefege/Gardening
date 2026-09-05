// Health check del backend (corre en push-dispatch.yml antes de mandar la cola).
// Pregunta a /api/sync si el token de GitHub del servidor sigue vivo. Si no,
// encola UNA push por día que avisa "el backend perdió el token" — así nunca
// más se rompe en silencio (05/09/2026: el token venció y nadie se enteró
// hasta que el usuario tocó un botón).
//
// Escribe solo en docs/notifications/queue.json (el paso "Commit queue
// updates" del workflow lo commitea junto con lo del dispatcher).

const fs = require('fs');
const path = require('path');

const SITE = process.env.HEALTH_SITE || 'https://gardening-chi.vercel.app/';
const QUEUE = process.env.HEALTH_QUEUE || path.join(__dirname, '..', 'docs', 'notifications', 'queue.json');

function mvdDate(d) {
  // YYYY-MM-DD en hora de Montevideo (-03:00, sin DST).
  return new Date(d.getTime() - 3 * 3600 * 1000).toISOString().slice(0, 10);
}

async function main() {
  let status = 0, body = null;
  try {
    const r = await fetch(SITE + 'api/sync', { cache: 'no-store' });
    status = r.status;
    body = await r.json().catch(() => null);
  } catch (e) {
    console.log('health: no se pudo consultar /api/sync:', String(e).slice(0, 120));
    return; // sin red no concluimos nada
  }
  if (status === 200 && body && body.ok) { console.log('health: backend OK'); return; }
  console.log('health: backend ROTO', status, JSON.stringify(body));

  const today = mvdDate(new Date());
  const id = today + '-backend-caido';
  const queue = JSON.parse(fs.readFileSync(QUEUE, 'utf8'));
  queue.notifications = queue.notifications || [];
  if (queue.notifications.some((n) => n.id === id)) { console.log('health: aviso de hoy ya encolado'); return; }
  const send = new Date();
  queue.notifications.push({
    id,
    title: '⚠️ El jardín no puede guardar nada',
    body: 'El token de GitHub del servidor venció. Hasta renovarlo en Vercel, hecha/foto/comentario no se guardan (quedan en tu equipo).',
    url: SITE + 'engage/puesta-al-dia.html',
    format: 'sistema',
    send_at: send.toISOString(),
    expires_at: new Date(send.getTime() + 12 * 3600 * 1000).toISOString(),
    status: 'pending',
    sent_at: null,
    fail_reason: null,
    created_by: 'health_check ' + today,
  });
  queue._updated_at = new Date().toISOString();
  fs.writeFileSync(QUEUE, JSON.stringify(queue, null, 2) + '\n');
  console.log('health: encolado aviso', id);
}

main().catch((e) => { console.log('health: error', String(e).slice(0, 160)); });
