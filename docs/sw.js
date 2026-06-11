// Service Worker mínimo — necesario para que Chrome considere el sitio
// instalable como PWA y use el icon de la manifest en home screen.
// El SW NO cachea contenido. Solo intercepta GETs SAME-ORIGIN para
// cumplir el criterio "fetch handler responde a requests" de Chrome.
//
// IMPORTANT: NO interceptar PUTs/POSTs ni cross-origin requests —
// rompía los uploads a GitHub API (PUT con body base64 grande tiraba
// "Failed to fetch" porque event.request no se puede re-fetch con body
// confiablemente).
//
// Para HTML documents: cache: 'reload' bypassa el browser HTTP cache
// para garantizar que la PWA siempre reciba el último deploy de Vercel.
// Sin esto, el HTML quedaba pegado por días en el disk cache del browser
// (especialmente en standalone PWA mode), y los nuevos features no se
// veían hasta hard-refresh manual.

const SW_VERSION = 'v1.3.0';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
  // Solo interceptamos GETs same-origin. El resto pasa derecho al browser.
  if (event.request.method !== 'GET') return;
  let url;
  try { url = new URL(event.request.url); } catch { return; }
  if (url.origin !== self.location.origin) return;

  // HTML documents → bypass cache del browser (siempre fresh).
  // Resto de assets (imágenes, fonts) → fetch default con cache normal.
  if (event.request.destination === 'document') {
    event.respondWith(fetch(event.request, { cache: 'reload' }));
  } else {
    event.respondWith(fetch(event.request));
  }
});

// ============================================================
// Web Push — el dispatcher (GitHub Actions) manda payloads JSON:
//   { nid, title, body, url }
// El click NO se loguea acá (el SW no tiene acceso al PAT en
// localStorage) — se loguea al cargar la página vía ?nid=.
// ============================================================
self.addEventListener('push', (event) => {
  let data = {};
  try { data = event.data ? event.data.json() : {}; } catch (e) {}
  event.waitUntil(self.registration.showNotification(data.title || 'Jardineando', {
    body: data.body || '',
    icon: 'icon-192.png',
    badge: 'icon-96.png',
    // tag = nid → si el dispatcher reintenta un envío, Chrome colapsa
    // las notificaciones duplicadas en una sola.
    tag: data.nid || 'jardineando',
    data: { url: data.url || './', nid: data.nid || '' },
  }));
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const d = event.notification.data || {};
  let url;
  try { url = new URL(d.url || './', self.location.origin); } catch (e) { url = new URL('./', self.location.origin); }
  if (d.nid) {
    url.searchParams.set('nid', d.nid);
    url.searchParams.set('src', 'push');
  }
  event.waitUntil(clients.openWindow(url.href));
});
