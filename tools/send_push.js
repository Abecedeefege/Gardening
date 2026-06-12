#!/usr/bin/env node
// Dispatcher de web push — corre en GitHub Actions cada 30 min (ver
// .github/workflows/push-dispatch.yml). Es deliberadamente tonto: NO
// decide contenido. Lee la cola que el agente diario escribió en
// docs/notifications/queue.json, manda lo que esté vencido (send_at <= now,
// expires_at > now) a la suscripción de docs/sync/push_subscription.json,
// y actualiza statuses. El workflow commitea los cambios.
//
// Política anti-duplicados: enviar primero, marcar "sent" después. Si el
// job muere entre medio, el próximo run re-manda UNA vez y Chrome colapsa
// el duplicado vía el tag (= nid) de la notificación.
//
// Env: VAPID_PRIVATE_KEY (secret del repo). Exit code 0 siempre que no
// haya error de programación — una suscripción caída NO es un fallo del job.

const fs = require('fs');
const path = require('path');
const webpush = require('web-push');

const ROOT = path.join(__dirname, '..');
const QUEUE_PATH = path.join(ROOT, 'docs/notifications/queue.json');
const SEND_LOG_PATH = path.join(ROOT, 'docs/notifications/send_log.json');
const SUB_PATH = path.join(ROOT, 'docs/sync/push_subscription.json');
const VAPID_PUBLIC_PATH = path.join(ROOT, 'docs/notifications/vapid_public.txt');
const VAPID_SUBJECT = 'mailto:andresbazzurro@gmail.com';

function readJson(p, fallback) {
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch (e) { return fallback; }
}
function writeJson(p, data) {
  fs.writeFileSync(p, JSON.stringify(data, null, 2) + '\n');
}

async function main() {
  const queue = readJson(QUEUE_PATH, null);
  if (!queue || !Array.isArray(queue.notifications) || queue.notifications.length === 0) {
    console.log('Cola vacía — nada para mandar.');
    return;
  }

  const now = Date.now();
  let queueChanged = false;

  // Expirar pendientes vencidos aunque no haya suscripción — evita que un
  // backlog viejo dispare notificaciones a deshora cuando todo vuelva.
  for (const n of queue.notifications) {
    if (n.status === 'pending' && n.expires_at && Date.parse(n.expires_at) < now) {
      n.status = 'expired';
      queueChanged = true;
      console.log(`[${n.id}] expirada sin enviar (expires_at ${n.expires_at})`);
    }
  }

  const due = queue.notifications.filter(
    (n) => n.status === 'pending' && n.send_at && Date.parse(n.send_at) <= now
  );

  const subDoc = readJson(SUB_PATH, null);
  const subscription = subDoc && subDoc.status === 'active' ? subDoc.subscription : null;

  if (due.length && !subscription) {
    console.log(`${due.length} notificaciones vencidas pero sin suscripción activa — quedan pending.`);
  }

  if (due.length && subscription) {
    const privateKey = process.env.VAPID_PRIVATE_KEY;
    if (!privateKey) {
      console.error('Falta VAPID_PRIVATE_KEY en el environment — abortando sin tocar la cola.');
      process.exitCode = 1;
      return;
    }
    const publicKey = fs.readFileSync(VAPID_PUBLIC_PATH, 'utf8').trim();
    webpush.setVapidDetails(VAPID_SUBJECT, publicKey, privateKey);

    const sendLog = readJson(SEND_LOG_PATH, { events: [] });

    for (const n of due) {
      const payload = JSON.stringify({ nid: n.id, title: n.title, body: n.body, url: n.url });
      try {
        // urgency:'high' → el push service entrega ya, sin esperar a que el
        // teléfono salga de Doze (normal/low quedan batcheadas y a veces se
        // descartan aunque el POST devuelva 201). TTL 4h: si el device está
        // apagado, se entrega al prender, pero no llega trasnochada mañana.
        const res = await webpush.sendNotification(subscription, payload, { TTL: 14400, urgency: 'high' });
        n.status = 'sent';
        n.sent_at = new Date().toISOString();
        queueChanged = true;
        sendLog.events.push({ type: 'notification_sent', nid: n.id, ts: n.sent_at, status_code: res.statusCode });
        console.log(`[${n.id}] enviada (HTTP ${res.statusCode})`);
      } catch (err) {
        const code = err.statusCode || 0;
        n.status = 'failed';
        n.fail_reason = code === 404 || code === 410 ? 'subscription_gone' : `HTTP ${code}: ${err.message || err}`.slice(0, 200);
        queueChanged = true;
        sendLog.events.push({ type: 'notification_failed', nid: n.id, ts: new Date().toISOString(), status_code: code, reason: n.fail_reason });
        console.error(`[${n.id}] falló: ${n.fail_reason}`);
        if (code === 404 || code === 410) {
          // El endpoint murió (usuario revocó permiso / Chrome rotó la
          // suscripción). Marcar el archivo para que el sitio muestre el
          // banner de re-suscripción la próxima vez que el usuario entre.
          subDoc.status = 'invalid';
          subDoc.invalidated_at = new Date().toISOString();
          subDoc.invalid_reason = `HTTP ${code}`;
          writeJson(SUB_PATH, subDoc);
          break; // no insistir con el resto contra un endpoint muerto
        }
      }
    }
    writeJson(SEND_LOG_PATH, sendLog);
  }

  if (queueChanged) {
    queue._updated_at = new Date().toISOString();
    writeJson(QUEUE_PATH, queue);
  } else {
    console.log('Sin cambios en la cola.');
  }
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
