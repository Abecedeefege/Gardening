// engage.js — tracking + aprobación para las páginas proposal de
// docs/engage/. Estas páginas son standalone (no cargan el bundle del
// sitio principal), así que este archivo trae copias mínimas de los
// helpers de GitHub API. Usa las MISMAS claves de localStorage que el
// sitio principal (mismo origin → mismo localStorage), así el PAT
// configurado en index.html funciona acá también.
//
// API pública para las páginas proposal:
//   engageApprove('<proposal_id>')   — botón "✅ Aprobar esta mejora"
//   engageRejected('<proposal_id>')  — botón "✕ No me interesa"
// Al cargar: si la URL tiene ?nid=, loguea notification_clicked + page_visit.

(function () {
  const GH_REPO = 'abecedeefege/gardening';
  const GH_API = 'https://api.github.com/repos/' + GH_REPO + '/contents';
  const ENGAGEMENT_PATH = 'docs/sync/engagement.json';
  const TOKEN_KEY = 'jardineando_github_token_v1';
  const DEVICE_KEY = 'jardineando_device_name_v1';
  const SEEN_NIDS_KEY = 'jardineando_seen_nids_v1';
  const OUTBOX_KEY = 'jardineando_engage_outbox_v1';

  function token() { return localStorage.getItem(TOKEN_KEY) || ''; }
  function device() { return localStorage.getItem(DEVICE_KEY) || 'sin-nombre'; }

  async function ghReadJson(path) {
    const r = await fetch(GH_API + '/' + path + '?ref=main&_=' + Date.now(), {
      cache: 'no-store',
      headers: { 'Authorization': 'Bearer ' + token(), 'Accept': 'application/vnd.github+json' },
    });
    if (r.status === 404) return { sha: null, data: null };
    if (!r.ok) throw new Error('GET ' + path + ': HTTP ' + r.status);
    const meta = await r.json();
    const utf8 = decodeURIComponent(escape(atob(meta.content.replace(/\n/g, ''))));
    return { sha: meta.sha, data: JSON.parse(utf8) };
  }

  async function ghWriteJson(path, data, message, sha) {
    const utf8 = unescape(encodeURIComponent(JSON.stringify(data, null, 2) + '\n'));
    const body = { message: message, content: btoa(utf8), branch: 'main' };
    if (sha) body.sha = sha;
    const r = await fetch(GH_API + '/' + path, {
      method: 'PUT',
      headers: {
        'Authorization': 'Bearer ' + token(),
        'Accept': 'application/vnd.github+json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });
    if (!r.ok) throw new Error('PUT ' + path + ': HTTP ' + r.status);
    return r.json();
  }

  // Outbox en localStorage: cada evento se guarda SINCRÓNICO antes de
  // intentar mandarlo. Así un click + minimizar la app no pierde el
  // feedback (la escritura a GitHub es GET+PUT y en mobile a veces no
  // alcanza a completar). El flush reintenta y deduplica por _id.
  function outboxGet() { try { return JSON.parse(localStorage.getItem(OUTBOX_KEY) || '[]'); } catch (e) { return []; } }
  function outboxSet(a) { try { localStorage.setItem(OUTBOX_KEY, JSON.stringify(a.slice(-200))); } catch (e) {} }

  // Estado de sync VISIBLE en la propia landing (diagnóstico honesto: nada de
  // "Anotado" mentiroso). El badge muestra: sin PAT / sincronizando / error / ok.
  var _flushing = false;
  var _lastSync = null; // { ok:bool, error:string|null }

  function renderSyncBadge() {
    if (!document.body) return;
    var el = document.getElementById('engage-sync-badge');
    if (!el) {
      el = document.createElement('div');
      el.id = 'engage-sync-badge';
      el.style.cssText = 'position:fixed;left:10px;bottom:10px;z-index:99999;' +
        'font:600 11.5px/1.35 -apple-system,BlinkMacSystemFont,sans-serif;padding:6px 11px;' +
        'border-radius:999px;max-width:86vw;box-shadow:0 2px 8px rgba(0,0,0,.18);cursor:pointer;';
      el.title = 'Tocar para reintentar';
      el.addEventListener('click', function () { flushOutbox(); });
      document.body.appendChild(el);
    }
    var pending = outboxGet().length;
    function show(bg, fg, txt, html) {
      el.style.background = bg; el.style.color = fg;
      if (html != null) el.innerHTML = html; else el.textContent = txt;
      el.style.display = 'block';
      if (el._t) { clearTimeout(el._t); el._t = null; }
    }
    if (_lastSync && _lastSync.error) {
      show('#fde2e2', '#9a2020', '⚠️ No se pudo guardar: ' + String(_lastSync.error).slice(0, 52) + '. Tocá para reintentar.');
    } else if (pending > 0) {
      show('#fdf3e3', '#8a5a12', '⏳ Sincronizando ' + pending + '…');
    } else if (_lastSync && _lastSync.ok) {
      show('#e6f3da', '#2d5016', '✓ Feedback sincronizado');
      el._t = setTimeout(function () { el.style.display = 'none'; }, 3000);
    } else {
      el.style.display = 'none';
    }
  }

  // Manda el outbox a la función serverless /api/feedback, que escribe al repo
  // con un token del lado del SERVIDOR. El browser NO necesita ningún PAT.
  async function flushOutbox() {
    if (_flushing) return false;
    var pending = outboxGet();
    if (!pending.length) { renderSyncBadge(); return true; }
    _flushing = true;
    var ok = false, lastErr = null;
    try {
      var r = await fetch('/api/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ events: pending, device: device() }),
      });
      if (r.ok) { outboxSet([]); ok = true; }
      else {
        var t = ''; try { t = await r.text(); } catch (e) {}
        lastErr = 'HTTP ' + r.status + (t ? ' ' + t.slice(0, 60) : '');
      }
    } catch (e) {
      lastErr = (e && e.message) ? e.message : String(e);
    } finally { _flushing = false; }
    _lastSync = { ok: ok, error: ok ? null : (lastErr || 'desconocido') };
    renderSyncBadge();
    return ok;
  }

  // Encola (durable) y dispara el flush en background. Devuelve true apenas
  // quedó guardado localmente — el sync a GitHub es best-effort con reintento.
  function logEvents(events) {
    if (!events || !events.length) return Promise.resolve(false);
    const stamped = events.map(function (e) {
      return Object.assign({ _id: Date.now().toString(36) + Math.random().toString(36).slice(2, 8) }, e);
    });
    outboxSet(outboxGet().concat(stamped));
    renderSyncBadge();
    return flushOutbox();   // resuelve true SOLO si sincronizó de verdad a GitHub
  }

  function pageName() {
    const parts = window.location.pathname.split('/');
    return 'engage/' + (parts.pop() || 'index.html');
  }

  // --- Tracking de llegada vía notificación (?nid=) + visita ---
  function trackLanding() {
    flushOutbox(); // mandar lo que haya quedado pendiente de sesiones anteriores
    let params;
    try { params = new URLSearchParams(window.location.search); } catch (e) { return; }
    const nid = params.get('nid');
    const now = new Date().toISOString();
    const events = [];
    if (nid) {
      const seen = JSON.parse(localStorage.getItem(SEEN_NIDS_KEY) || '[]');
      if (seen.indexOf(nid) === -1) {
        seen.push(nid);
        localStorage.setItem(SEEN_NIDS_KEY, JSON.stringify(seen.slice(-50)));
        events.push({ type: 'notification_clicked', nid: nid, page: pageName(), ts: now, device: device() });
      }
      params.delete('nid'); params.delete('src');
      const clean = window.location.pathname + (params.toString() ? '?' + params.toString() : '') + window.location.hash;
      history.replaceState(null, '', clean);
      events.push({ type: 'page_visit', page: pageName(), nid: nid, src: 'push', ts: now, device: device() });
    } else {
      // Visita directa — throttle 1/hora por página para no spamear con reloads.
      const throttleKey = 'jardineando_visit_throttle_' + pageName();
      const last = parseInt(localStorage.getItem(throttleKey) || '0', 10);
      if (Date.now() - last < 60 * 60 * 1000) return;
      localStorage.setItem(throttleKey, String(Date.now()));
      events.push({ type: 'page_visit', page: pageName(), nid: null, src: 'direct', ts: now, device: device() });
    }
    logEvents(events);
  }

  // --- Aprobación / rechazo de proposals ---
  function feedbackArea(btn) {
    // Reemplaza el contenedor de los botones por un mensaje de confirmación.
    if (btn && btn.closest) {
      const wrap = btn.closest('.engage-actions') || btn.parentElement;
      if (wrap) return wrap;
    }
    return document.querySelector('.engage-actions');
  }

  async function decide(proposalId, type, btn, okMsg) {
    const wrap = feedbackArea(btn);
    if (wrap) wrap.innerHTML = '<p class="engage-feedback">⏳ Guardando…</p>';
    const ok = await logEvents([{ type: type, proposal_id: proposalId, ts: new Date().toISOString(), device: device() }]);
    if (wrap) {
      wrap.innerHTML = ok
        ? '<p class="engage-feedback">' + okMsg + '</p>'
        : '<p class="engage-feedback">Guardado en este equipo — se sube en cuanto haya conexión. (Tocá el cartel de abajo para reintentar.)</p>';
    }
  }

  window.engageApprove = function (proposalId) {
    decide(proposalId, 'proposal_approved', (typeof event !== 'undefined' && event) ? event.target : null,
      '✅ ¡Listo! El agente integra esta mejora al sitio.');
  };

  window.engageRejected = function (proposalId) {
    decide(proposalId, 'proposal_rejected', (typeof event !== 'undefined' && event) ? event.target : null,
      '👍 Anotado — el agente la descarta y prueba otra cosa.');
  };

  // --- Reacciones granulares (😍/🙂/😐/🙅) ---
  // Uso en la página: <button onclick="engageReact('<page_id>','love', this)">😍</button>
  function markSelected(btn) {
    if (!btn || !btn.parentElement) return;
    Array.prototype.forEach.call(btn.parentElement.querySelectorAll('button'), function (b) {
      b.classList.remove('sel'); b.disabled = true;
    });
    btn.classList.add('sel');
  }
  window.engageReact = function (targetId, value, btn) {
    btn = btn || ((typeof event !== 'undefined' && event) ? event.target : null);
    markSelected(btn);
    var hint = btn && btn.parentElement ? btn.parentElement.querySelector('.react-hint') : null;
    if (hint) hint.textContent = 'Guardando…';
    logEvents([{ type: 'reaction', target: targetId, value: value,
      page: pageName(), ts: new Date().toISOString(), device: device() }]).then(function (ok) {
      if (hint) hint.textContent = ok ? '✓ ¡Gracias!' : 'Guardado, sincronizando…';
    });
  };

  // --- Preguntas sí/no/no-sé (ej. estado observable del jardín) ---
  // Uso: <button onclick="engageAnswer('liquidambar_pelado','no', this)">No</button>
  window.engageAnswer = function (qid, value, btn) {
    btn = btn || ((typeof event !== 'undefined' && event) ? event.target : null);
    markSelected(btn);
    var hint = btn && btn.parentElement ? btn.parentElement.querySelector('.q-hint') : null;
    if (hint) hint.textContent = 'Guardando…';
    logEvents([{ type: 'answer', qid: qid, value: value,
      page: pageName(), ts: new Date().toISOString(), device: device() }]).then(function (ok) {
      if (hint) hint.textContent = ok ? '✓' : '⏳';
    });
  };

  // --- Tracking pasivo: tiempo en página + profundidad de scroll ---
  var _t0 = Date.now();
  var _maxScroll = 0;
  function _scrollPct() {
    var h = document.documentElement;
    var denom = (h.scrollHeight - h.clientHeight);
    if (denom <= 0) return 100;
    return Math.min(100, Math.round((h.scrollTop || window.pageYOffset || 0) / denom * 100));
  }
  window.addEventListener('scroll', function () {
    var p = _scrollPct(); if (p > _maxScroll) _maxScroll = p;
  }, { passive: true });
  var _dwellSent = false;
  function flushDwell() {
    if (_dwellSent) return;
    var secs = Math.round((Date.now() - _t0) / 1000);
    if (secs < 2) return; // ignorar rebotes instantáneos
    _dwellSent = true;
    logEvents([{ type: 'dwell', seconds: secs, scroll_pct: Math.max(_maxScroll, _scrollPct()),
      page: pageName(), ts: new Date().toISOString(), device: device() }]);
  }
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden') flushDwell();
    else flushOutbox(); // al volver a foco, reintentar lo pendiente
  });
  window.addEventListener('pagehide', flushDwell);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', trackLanding);
  } else {
    trackLanding();
  }
})();
