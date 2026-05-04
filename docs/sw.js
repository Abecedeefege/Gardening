// Service Worker mínimo — necesario para que Chrome considere el sitio
// instalable como PWA y use el icon de la manifest en home screen.
// El SW NO cachea contenido (passthrough explícito); existe solo para
// cumplir el criterio "fetch handler responde a requests" de Chrome.
// Si en el futuro querés offline support, expandir el fetch handler.

const SW_VERSION = 'v1.0.0';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
  // Passthrough explícito — respondWith con la fetch original.
  // Chrome requiere que el SW participe activamente en fetches para
  // considerar el sitio installable.
  event.respondWith(fetch(event.request));
});
