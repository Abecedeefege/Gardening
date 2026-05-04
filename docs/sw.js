// Service Worker mínimo — solo para que Chrome considere el sitio
// instalable como PWA (necesita SW registrado + manifest + start_url).
// No cachea nada — el sitio funciona online normal. Si en el futuro
// querés offline support, expandir aquí.

self.addEventListener('install', (event) => {
  // Skip waiting para que la nueva versión active enseguida.
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  // Tomar control de todos los clients (tabs abiertas) en cuanto se activa.
  event.waitUntil(self.clients.claim());
});

// Pasthrough: dejamos que el browser maneje todos los fetches normalmente.
self.addEventListener('fetch', (event) => {
  // No interceptar — comportamiento default.
});
