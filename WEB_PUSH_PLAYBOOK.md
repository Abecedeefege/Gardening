# Web Push sin backend — Playbook replicable

Cómo montar **notificaciones push programadas** en un sitio estático (GitHub
Pages / Vercel / Netlify) **sin servidor propio**: la cola, la suscripción y el
log viven como JSON en el repo; un workflow de GitHub Actions hace de
dispatcher; el browser se suscribe y escribe la suscripción vía la GitHub API.

Está escrito para copiar-pegar y adaptar. Reemplazá los placeholders
`<...>` y ajustá las rutas a tu repo.

---

## 0. Arquitectura (3 actores, ownership de archivos disjunto)

```
┌─────────────┐   encola         ┌──────────────────────┐   manda push   ┌──────────┐
│  Fuente de  │ ───────────────▶ │  queue.json (repo)   │ ─────────────▶ │  Browser │
│  contenido  │                  └──────────────────────┘                │   (SW)   │
│ (vos/agente)│                            │  lee + escribe estados       └──────────┘
└─────────────┘                            ▼                                   ▲
                                  ┌──────────────────────┐                     │
                                  │  Dispatcher          │  lee suscripción    │
                                  │  (GitHub Actions +   │ ────────────────────┘
                                  │   send_push.js)      │
                                  └──────────────────────┘
```

- **Browser**: pide permiso, se suscribe (Web Push API), y guarda la suscripción
  en `subscription.json` del repo (vía GitHub API con un PAT). El service worker
  recibe el push y muestra la notificación **aunque la app esté cerrada**.
- **Dispatcher**: corre en CI, lee `queue.json`, manda lo vencido a la
  suscripción, y actualiza estados + `send_log.json`.
- **Fuente de contenido**: vos a mano, o un agente/cron, escribís `queue.json`.

**Regla de oro de ownership**: la fuente escribe la cola; el dispatcher escribe
los estados/log; el browser escribe la suscripción. No crucen escrituras.

---

## 1. Prerrequisitos

- Sitio servido por HTTPS (requisito de Web Push). GitHub Pages / Vercel sirven.
- Un directorio publicado (ej. `docs/` en Pages, `public/` en Vercel). Abajo lo
  llamo `<PUB>/`.
- Node en CI (lo pone `actions/setup-node`).
- `icon-192.png` y `icon-96.png` en `<PUB>/` (para la notificación).

---

## 2. Generar las claves VAPID (una sola vez)

```bash
npx web-push generate-vapid-keys
# Output:
#   Public Key:  BNc...   ← va al repo (texto plano)
#   Private Key: x1Z...   ← SECRET de Actions, NUNCA al repo
```

- Guardá la **pública** en `<PUB>/notifications/vapid_public.txt` (una línea).
- Guardá la **privada** como secret de GitHub: repo → Settings → Secrets and
  variables → Actions → New repository secret → nombre `VAPID_PRIVATE_KEY`.

---

## 3. Service worker — `<PUB>/sw.js`

```js
// sw.js — recibe el push y abre el deep-link al tocar. NO cachea nada.
const SW_VERSION = 'v1';

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));

self.addEventListener('push', (event) => {
  let data = {};
  try { data = event.data ? event.data.json() : {}; } catch (e) {}
  event.waitUntil(self.registration.showNotification(data.title || 'App', {
    body: data.body || '',
    icon: 'icon-192.png',
    badge: 'icon-96.png',
    tag: data.nid || 'app',                 // colapsa reintentos del mismo id
    data: { url: data.url || './', nid: data.nid || '' },
  }));
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const d = event.notification.data || {};
  let url;
  try { url = new URL(d.url || './', self.location.origin); }
  catch (e) { url = new URL('./', self.location.origin); }
  if (d.nid) {                               // para loguear el click al abrir
    url.searchParams.set('nid', d.nid);
    url.searchParams.set('src', 'push');
  }
  event.waitUntil(clients.openWindow(url.href));
});
```

> Si tu sitio es una PWA y querés que el HTML siempre tome el último deploy,
> agregá un `fetch` handler que haga `fetch(req, { cache: 'reload' })` solo para
> `event.request.destination === 'document'`. Es opcional.

---

## 4. Suscripción desde el browser (botón "Activar notificaciones")

```js
function urlBase64ToUint8Array(b64) {
  const pad = '='.repeat((4 - (b64.length % 4)) % 4);
  const s = (b64 + pad).replace(/-/g, '+').replace(/_/g, '/');
  const raw = atob(s); const arr = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i++) arr[i] = raw.charCodeAt(i);
  return arr;
}

async function enablePush() {
  if (!('serviceWorker' in navigator) || !('PushManager' in window))
    throw new Error('Este navegador no soporta Web Push');

  const reg = await navigator.serviceWorker.register('sw.js');
  await navigator.serviceWorker.ready;

  if ((await Notification.requestPermission()) !== 'granted')
    throw new Error('Permiso denegado');

  const vapidPublic = (await (await fetch('notifications/vapid_public.txt',
    { cache: 'no-store' })).text()).trim();

  let sub = await reg.pushManager.getSubscription();
  if (!sub) {
    sub = await reg.pushManager.subscribe({
      userVisibleOnly: true,                                 // obligatorio
      applicationServerKey: urlBase64ToUint8Array(vapidPublic),
    });
  }
  await persistSubscription(sub.toJSON());                   // ver abajo
  return 'Notificaciones activadas';
}
```

### Persistir la suscripción sin backend (truco GitHub API)

El dispatcher necesita leer la suscripción. Sin servidor, la commiteás al repo
con un **PAT del usuario** (guardado SOLO en `localStorage`, nunca en el repo):

```js
// PAT con scope "contents:write" sobre el repo. Lo ingresa el usuario una vez
// y queda en localStorage de su device. NO se sincroniza a ningún lado.
const REPO = '<OWNER>/<REPO>';
const SUB_PATH = '<PUB>/notifications/subscription.json';

async function ghPutJson(path, obj, message) {
  const token = localStorage.getItem('gh_pat');               // tu key
  const api = `https://api.github.com/repos/${REPO}/contents/${path}`;
  // sha actual (si existe) para el update
  let sha = null;
  const cur = await fetch(`${api}?ref=main&_=${Date.now()}`, {
    cache: 'no-store',
    headers: { Authorization: `Bearer ${token}`, Accept: 'application/vnd.github+json' },
  });
  if (cur.ok) sha = (await cur.json()).sha;
  const body = {
    message, branch: 'main',
    content: btoa(unescape(encodeURIComponent(JSON.stringify(obj, null, 2) + '\n'))),
  };
  if (sha) body.sha = sha;
  const r = await fetch(api, {
    method: 'PUT',
    headers: { Authorization: `Bearer ${token}`, Accept: 'application/vnd.github+json',
               'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw new Error('PUT ' + path + ': HTTP ' + r.status);
}

async function persistSubscription(subJson) {
  await ghPutJson(SUB_PATH, {
    device: localStorage.getItem('device_name') || 'sin-nombre',
    subscription: subJson,
    status: 'active',
    updated_at: new Date().toISOString(),
    invalidated_at: null, invalid_reason: null,
  }, 'push: registrar suscripción');
}
```

> **Alternativas a la GitHub API**: un endpoint serverless mínimo (Vercel/Netlify
> Function) que reciba la suscripción y la guarde, o un KV (Upstash, etc.). El
> resto del playbook no cambia: el dispatcher solo necesita poder LEER la
> suscripción y la cola.

---

## 5. La cola — `<PUB>/notifications/queue.json`

```json
{
  "_updated_at": "2026-06-12T19:00:00-03:00",
  "notifications": [
    {
      "id": "2026-06-12-a",
      "title": "Título corto, con gancho (~40 chars)",
      "body": "Cuerpo concreto (~110 chars).",
      "url": "<SITE_URL>/landing-especifica.html",
      "send_at": "2026-06-12T20:00:00-03:00",
      "expires_at": "2026-06-12T23:30:00-03:00",
      "status": "pending",
      "sent_at": null,
      "fail_reason": null
    }
  ]
}
```

- `send_at` / `expires_at`: **timestamps con offset explícito de tu zona**
  (ver Lección #11). El dispatcher manda cuando `send_at <= now < expires_at`.
- `status`: `pending` → `sent` | `failed` | `expired` | `cancelled`.

---

## 6. El dispatcher — `tools/send_push.js`

```js
#!/usr/bin/env node
// Lee la cola, manda lo vencido a la suscripción guardada, actualiza estados.
// Es deliberadamente tonto: NO decide contenido.
const fs = require('fs');
const path = require('path');
const webpush = require('web-push');

const ROOT = path.join(__dirname, '..');
const PUB = 'docs';                                   // <-- AJUSTAR (docs/public)
const QUEUE_PATH    = path.join(ROOT, PUB, 'notifications/queue.json');
const SEND_LOG_PATH = path.join(ROOT, PUB, 'notifications/send_log.json');
const SUB_PATH      = path.join(ROOT, PUB, 'notifications/subscription.json');
const VAPID_PUB     = path.join(ROOT, PUB, 'notifications/vapid_public.txt');
const VAPID_SUBJECT = 'mailto:<TU-EMAIL>';            // <-- AJUSTAR

const readJson  = (p, fb) => { try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch { return fb; } };
const writeJson = (p, d)  => fs.writeFileSync(p, JSON.stringify(d, null, 2) + '\n');

async function main() {
  const queue = readJson(QUEUE_PATH, null);
  if (!queue || !Array.isArray(queue.notifications)) { console.log('Cola vacía.'); return; }

  const now = Date.now();
  let changed = false;

  // Expirar vencidos aunque no haya suscripción (evita backlog a deshora).
  for (const n of queue.notifications) {
    if (n.status === 'pending' && n.expires_at && Date.parse(n.expires_at) < now) {
      n.status = 'expired'; changed = true;
    }
  }

  const due = queue.notifications.filter(
    (n) => n.status === 'pending' && n.send_at && Date.parse(n.send_at) <= now
  );

  const subDoc = readJson(SUB_PATH, null);
  const subscription = subDoc && subDoc.status === 'active' ? subDoc.subscription : null;

  if (due.length && subscription) {
    const priv = process.env.VAPID_PRIVATE_KEY;
    if (!priv) { console.error('Falta VAPID_PRIVATE_KEY'); process.exitCode = 1; return; }
    webpush.setVapidDetails(VAPID_SUBJECT, fs.readFileSync(VAPID_PUB, 'utf8').trim(), priv);

    const log = readJson(SEND_LOG_PATH, { events: [] });
    for (const n of due) {
      const payload = JSON.stringify({ nid: n.id, title: n.title, body: n.body, url: n.url });
      try {
        // urgency:'high' => entrega YA, salta el Doze del teléfono. SIN esto las
        // de prioridad normal quedan batcheadas y a veces se descartan aunque el
        // POST devuelva 201 (ver Lección #1). TTL 4h: si está apagado, llega al
        // prender, pero no trasnochada mañana.
        const res = await webpush.sendNotification(subscription, payload, { TTL: 14400, urgency: 'high' });
        n.status = 'sent'; n.sent_at = new Date().toISOString(); changed = true;
        log.events.push({ type: 'sent', nid: n.id, ts: n.sent_at, status_code: res.statusCode });
        console.log(`[${n.id}] enviada (HTTP ${res.statusCode})`);
      } catch (err) {
        const code = err.statusCode || 0;
        n.status = 'failed';
        n.fail_reason = (code === 404 || code === 410) ? 'subscription_gone' : `HTTP ${code}`;
        changed = true;
        log.events.push({ type: 'failed', nid: n.id, ts: new Date().toISOString(), status_code: code });
        console.error(`[${n.id}] falló: ${n.fail_reason}`);
        if (code === 404 || code === 410) {       // endpoint muerto → invalidar
          subDoc.status = 'invalid';
          subDoc.invalidated_at = new Date().toISOString();
          writeJson(SUB_PATH, subDoc);
          break;                                  // no insistir contra un endpoint muerto
        }
      }
    }
    writeJson(SEND_LOG_PATH, log);
  } else if (due.length) {
    console.log(`${due.length} vencidas pero sin suscripción activa — quedan pending.`);
  }

  if (changed) { queue._updated_at = new Date().toISOString(); writeJson(QUEUE_PATH, queue); }
}
main().catch((e) => { console.error(e); process.exitCode = 1; });
```

### `tools/package.json`

```json
{
  "name": "push-tools",
  "private": true,
  "dependencies": { "web-push": "^3.6.7" }
}
```

---

## 7. El workflow — `.github/workflows/push-dispatch.yml`

```yaml
name: push-dispatch

on:
  schedule:
    - cron: '*/30 10-23 * * *'   # RESPALDO. El cron de Actions deriva y saltea
                                 # (ver Lección #2). No dependas de él para timing.
  workflow_dispatch: {}          # disparo manual desde la UI
  push:
    branches: [main]
    paths:
      - 'docs/notifications/queue.json'   # <-- AJUSTAR ruta. Disparo INMEDIATO
                                          # al encolar: encolar == despachar.

concurrency:
  group: push-dispatch
  cancel-in-progress: false

permissions:
  contents: write

jobs:
  dispatch:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { ref: main }
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - name: Install web-push
        working-directory: tools
        run: npm install --no-audit --no-fund
      - name: Send due notifications
        run: node tools/send_push.js
        env:
          VAPID_PRIVATE_KEY: ${{ secrets.VAPID_PRIVATE_KEY }}
      - name: Commit queue/log updates
        run: |
          if [ -n "$(git status --porcelain docs/notifications)" ]; then
            git config user.name "push-dispatcher"
            git config user.email "actions@users.noreply.github.com"
            git add docs/notifications
            git commit -m "push: dispatch $(date -u +%FT%TZ)"
            for i in 1 2 3; do
              git push origin main && break || git pull --rebase origin main
            done
          else
            echo "Sin cambios."
          fi
```

> **Importante (sin loop infinito)**: el commit del dispatcher usa el
> `GITHUB_TOKEN` por defecto, y los pushes hechos con ese token **no** re-disparan
> workflows. Por eso el `on: push` a la cola no entra en bucle.

---

## 8. Probar de punta a punta

1. Suscribite desde el teléfono (botón "Activar"). Confirmá que aparece
   `subscription.json` con `status: active` en el repo.
2. Encolá una notificación de prueba con `send_at` en el pasado y `expires_at`
   esta noche, y pusheá `queue.json` (el `on: push` dispara el workflow).
   Alternativa: Actions → push-dispatch → **Run workflow**.
3. En segundos debería llegar al teléfono. Mirá `send_log.json`: `status_code`
   **201 = aceptada** (¡no necesariamente entregada! ver Lección #3).

---

## 9. Lecciones aprendidas (esto es el oro — bakealo desde el día 1)

1. **`urgency: 'high'` es obligatorio.** Sin eso, Android mete las notificaciones
   de prioridad normal en la cola de Doze cuando la pantalla está apagada y las
   **retiene o descarta**, aunque el POST devuelva 201. Síntoma clásico: "las
   primeras llegan (teléfono en uso), después no llega ninguna".

2. **El cron de GitHub Actions NO es confiable.** Deriva y saltea corridas (vimos
   ~100 min sin un solo tick). Para timing fino agregá el trigger `on: push` a la
   cola: **encolar = despachar al instante**. Dejá el cron solo como respaldo.
   Además el cron `10-23 UTC` no cubre todas las horas locales — calculá la
   ventana en UTC.

3. **HTTP 201 = aceptada por el push service, NO entregada al device.** Nunca lo
   leas como "llegó". La entrega depende del estado del teléfono (Doze, batería).

4. **404 / 410 = suscripción muerta.** Chrome rota suscripciones y el usuario
   puede revocar el permiso. Detectalo, marcá la suscripción `invalid`, y mostrá
   un banner de re-suscripción la próxima vez que entre.

5. **Verificá los datos antes de publicar.** Un push con info falsa quema la
   credibilidad del canal entero. Si afirmás algo (un dato, una urgencia, un
   estado), chequealo con una fuente primero. No amplifiques lo que "creés".

6. **No afirmes estados que no podés observar.** "Tu árbol está sin hojas" cuando
   no lo viste es un tiro en el pie. Frasealo condicional ("si ya perdió las
   hojas…") o **preguntalo** en una landing y guardá la respuesta.

7. **El copy del push debe cumplir lo que promete su destino.** Si decís "mirá X",
   el link tiene que abrir X — no el home genérico.

8. **Cada push lleva a una landing específica**, nunca a la home "a ver qué hay".
   El home no tiene nada puntual que ver; decepciona.

9. **Feedback durable con outbox en `localStorage`.** El registro de
   interacciones (reacciones, clicks) por `fetch` a una API **no completa** si el
   usuario minimiza la app en mobile. Guardá el evento sincrónico en localStorage
   ANTES de mandarlo, con flush reintentable y dedup por id, y revaciá al cargar /
   volver a foco. Sin esto, perdés casi todo el feedback (y un botón que dice
   "Guardado" miente).

10. **El service worker NO requiere la app abierta.** El push lo recibe el SW
    aunque la PWA esté cerrada. Lo que importa es **despertar** el device — y eso
    es `urgency: 'high'`, no tener la app en primer plano.

11. **Timestamps con el offset explícito de tu zona.** No le pongas `-03:00` a una
    hora UTC: calculá la hora local de verdad (`TZ=America/Montevideo date`). Un
    `_updated_at` 3 horas en el futuro es señal de este bug.

12. **TTL razonable** (ej. 4h / 14400s). Muy corto → se pierde si el device está
    en Doze un rato. Muy largo → llega trasnochada al día siguiente.

13. **`tag` = id de la notificación en el SW.** Colapsa reintentos y duplicados:
    si el dispatcher re-manda el mismo id, Chrome muestra una sola.

14. **Secrets nunca al repo.** La VAPID privada es secret de Actions; la pública
    va al repo. El PAT del usuario vive solo en su `localStorage`, nunca se
    sincroniza ni se commitea.

15. **Anti-duplicados: mandá primero, marcá `sent` después.** Si el job muere
    entre medio, el próximo reintenta una vez y el `tag` colapsa el duplicado.

16. **Ownership de archivos disjunto entre actores.** Fuente escribe la cola;
    dispatcher escribe estados/log; browser escribe la suscripción. En cada push
    del dispatcher: `git pull --rebase` + reintento (race con la fuente o el
    browser).

17. **Si una experiencia/landing necesita aprobación para volverse permanente**,
    hacelo explícito: efímera por default, y solo se integra al sitio con un OK
    explícito del usuario. Evita acumular features que nadie pidió.

---

## 10. Checklist de replicación

- [ ] `npx web-push generate-vapid-keys`
- [ ] Pública → `<PUB>/notifications/vapid_public.txt`
- [ ] Privada → secret `VAPID_PRIVATE_KEY` en Actions
- [ ] `<PUB>/sw.js` (push + notificationclick)
- [ ] `icon-192.png` / `icon-96.png` en `<PUB>/`
- [ ] Botón "Activar" + `enablePush()` + `persistSubscription()`
- [ ] `<PUB>/notifications/queue.json` (vacío: `{"notifications":[]}`)
- [ ] `<PUB>/notifications/send_log.json` (vacío: `{"events":[]}`)
- [ ] `tools/send_push.js` + `tools/package.json`
- [ ] `.github/workflows/push-dispatch.yml` (cron + `workflow_dispatch` + `on:push`)
- [ ] Ajustar rutas `<PUB>`, `REPO`, `VAPID_SUBJECT`, paths del workflow
- [ ] Test: suscribir → encolar con `send_at` pasado → push → verificar en el teléfono
- [ ] Confirmar que `urgency:'high'` está puesto (Lección #1)

---

*Generado a partir de un sistema en producción. Las lecciones de la sección 9
son las que costaron tiempo real de debug — no las saltees.*
