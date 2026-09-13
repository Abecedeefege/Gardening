const CACHE='jardineando-v2-shell-3';
const SHELL=['./','./index.html','./app.js','./styles.css','./catalog.json','./manifest.webmanifest'];
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(c=>c.addAll(SHELL))));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('jardineando-v2-shell-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
 const url=new URL(event.request.url);
 // Cache only the public application shell. Never cache auth, API or private photos here.
 if(event.request.method!=='GET'||url.origin!==self.location.origin||!url.pathname.startsWith(new URL('./',self.location).pathname))return;
 const name=url.pathname.split('/').pop();if(!['','index.html','app.js','styles.css','catalog.json','manifest.webmanifest'].includes(name))return;
 event.respondWith(fetch(event.request).then(r=>{if(r.ok){const copy=r.clone();caches.open(CACHE).then(c=>c.put(event.request,copy));}return r;}).catch(()=>caches.match(event.request).then(r=>r||caches.match('./index.html'))));
});
