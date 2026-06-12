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

  async function logEvents(events) {
    if (!token() || !events.length) return false;
    for (let attempt = 0; attempt < 2; attempt++) {
      try {
        const cur = await ghReadJson(ENGAGEMENT_PATH);
        const doc = cur.data || { _updated_at: null, events: [], daily_summary: {} };
        doc.events = (doc.events || []).concat(events);
        doc._updated_at = new Date().toISOString();
        await ghWriteJson(ENGAGEMENT_PATH, doc,
          'engage: ' + events.map(function (e) { return e.type; }).join(', ') + ' desde ' + device(),
          cur.sha);
        return true;
      } catch (e) {
        if (attempt === 1) { console.warn('[engage] no se pudo loguear:', e); return false; }
      }
    }
    return false;
  }

  function pageName() {
    const parts = window.location.pathname.split('/');
    return 'engage/' + (parts.pop() || 'index.html');
  }

  // --- Tracking de llegada vía notificación (?nid=) + visita ---
  function trackLanding() {
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
    if (!token()) {
      if (wrap) wrap.innerHTML = '<p class="engage-feedback">⚠️ Abrí esta página desde tu teléfono con el GitHub PAT configurado para poder votar.</p>';
      return;
    }
    if (wrap) wrap.innerHTML = '<p class="engage-feedback">⏳ Guardando…</p>';
    const ok = await logEvents([{ type: type, proposal_id: proposalId, ts: new Date().toISOString(), device: device() }]);
    if (wrap) {
      wrap.innerHTML = ok
        ? '<p class="engage-feedback">' + okMsg + '</p>'
        : '<p class="engage-feedback">❌ No se pudo guardar — probá de nuevo en un rato.</p>';
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
    if (hint) hint.textContent = '¡Gracias! Anotado: ' + value + ' 🌱';
    logEvents([{ type: 'reaction', target: targetId, value: value,
      page: pageName(), ts: new Date().toISOString(), device: device() }]);
  };

  // --- Preguntas sí/no/no-sé (ej. estado observable del jardín) ---
  // Uso: <button onclick="engageAnswer('liquidambar_pelado','no', this)">No</button>
  window.engageAnswer = function (qid, value, btn) {
    btn = btn || ((typeof event !== 'undefined' && event) ? event.target : null);
    markSelected(btn);
    var hint = btn && btn.parentElement ? btn.parentElement.querySelector('.q-hint') : null;
    if (hint) hint.textContent = '✓ Anotado';
    logEvents([{ type: 'answer', qid: qid, value: value,
      page: pageName(), ts: new Date().toISOString(), device: device() }]);
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
  });
  window.addEventListener('pagehide', flushDwell);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', trackLanding);
  } else {
    trackLanding();
  }
})();
