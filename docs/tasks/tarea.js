// tarea.js — JS compartido de las landings por tarea (docs/tasks/<taskId>.html).
// Las landings son standalone (no cargan el bundle del sitio). Este archivo:
//   1. Carga y renderiza el thread de conversación de la tarea
//      (GET /api/tarea?task_id=… lee fresco del repo vía token del servidor;
//       fallback: ../sync/threads/<id>.json estático del último deploy).
//   2. Composer: manda texto y fotos a /api/tarea (serverless — el browser
//      NO necesita PAT). Echo local optimista: lo enviado se ve al instante
//      aunque el deploy de Vercel tarde un minuto.
//   3. Acciones de estado (hecha / posponer / reactivar) → task_states.json.
//   4. Tracking de llegada por push (?nid=) → /api/feedback (mismos eventos
//      que engage.js, page "tasks/<archivo>").
// El agente /responder-tareas procesa los mensajes pendientes cada hora y
// contesta con un push que deep-linkea de vuelta a esta misma landing.

(function () {
  'use strict';
  var T = window.TAREA || {};
  if (!T.id) return;

  var API = '/api/tarea';
  var FEEDBACK_API = '/api/feedback';
  var DEVICE_KEY = 'jardineando_device_name_v1';
  var SEEN_NIDS_KEY = 'jardineando_seen_nids_v1';   // compartida con engage.js
  var ECHO_KEY = 'jardineando_thread_echo_v1';      // {taskId: [mensajes enviados]}
  var OUTBOX_KEY = 'jardineando_tarea_outbox_v1';   // payloads texto/estado con reintento

  function device() { return localStorage.getItem(DEVICE_KEY) || 'landing'; }
  function nowIso() { return new Date().toISOString(); }
  function msgId() { return 'm-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8); }
  function jget(key, fallback) {
    try { return JSON.parse(localStorage.getItem(key)) || fallback; } catch (e) { return fallback; }
  }
  function jset(key, v) { try { localStorage.setItem(key, JSON.stringify(v)); } catch (e) {} }

  // ============================================================
  // Estado en memoria
  // ============================================================
  var serverThread = { messages: [] };
  var taskState = null;      // {status, snoozed_until, completed_at} | null
  var pendingPhoto = null;   // dataURL listo para mandar
  var _sending = false;
  var _lastSync = null;      // {ok, error}

  // ============================================================
  // Echo local — mensajes ya enviados que quizás todavía no aparecen
  // en el thread fetcheado (deploy en camino). Merge por id.
  // ============================================================
  function echoes() { return (jget(ECHO_KEY, {})[T.id]) || []; }
  function saveEcho(msg) {
    var all = jget(ECHO_KEY, {});
    all[T.id] = (all[T.id] || []).concat([msg]).slice(-30);
    jset(ECHO_KEY, all);
  }
  function pruneEchoes() {
    var all = jget(ECHO_KEY, {});
    var mine = all[T.id] || [];
    if (!mine.length) return;
    var seen = {};
    (serverThread.messages || []).forEach(function (m) { seen[m.id] = 1; });
    var week = Date.now() - 7 * 24 * 3600 * 1000;
    all[T.id] = mine.filter(function (m) {
      return !seen[m.id] && new Date(m.ts).getTime() > week;
    });
    jset(ECHO_KEY, all);
  }

  // ============================================================
  // Outbox durable (solo texto/estado — las fotos se reintentan a mano)
  // ============================================================
  function outbox() { return jget(OUTBOX_KEY, []); }
  function outboxSet(a) { jset(OUTBOX_KEY, a.slice(-50)); }
  var _flushing = false;
  async function flushOutbox() {
    if (_flushing) return;
    var items = outbox();
    if (!items.length) { renderBadge(); return; }
    _flushing = true;
    var remaining = [];
    for (var i = 0; i < items.length; i++) {
      var ok = false;
      try {
        var r = await fetch(API, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(items[i]),
        });
        ok = r.ok;
        if (!ok && r.status >= 400 && r.status < 500 && r.status !== 429) ok = true; // payload inválido: no reintentar para siempre
      } catch (e) {}
      if (!ok) { remaining = remaining.concat(items.slice(i)); break; }
    }
    outboxSet(remaining);
    _flushing = false;
    _lastSync = { ok: !remaining.length, error: remaining.length ? 'sin conexión con el servidor' : null };
    renderBadge();
  }

  function renderBadge() {
    var el = document.getElementById('sync-badge');
    if (!el) return;
    var pending = outbox().length;
    if (el._t) { clearTimeout(el._t); el._t = null; }
    if (pending > 0) {
      el.style.display = 'block';
      el.style.background = '#fdf3e3'; el.style.color = '#8a5a12';
      el.textContent = '⏳ ' + pending + ' por sincronizar — tocá para reintentar';
    } else if (_lastSync && _lastSync.ok) {
      el.style.display = 'block';
      el.style.background = '#e6f3da'; el.style.color = '#2d5016';
      el.textContent = '✓ Sincronizado';
      el._t = setTimeout(function () { el.style.display = 'none'; }, 2500);
    } else {
      el.style.display = 'none';
    }
  }

  // ============================================================
  // Carga del thread + estado
  // ============================================================
  async function loadThread() {
    // 1) Serverless: lee del repo en fresco (ve mensajes de hace segundos).
    try {
      var r = await fetch(API + '?task_id=' + encodeURIComponent(T.id), { cache: 'no-store' });
      if (r.ok) {
        var data = await r.json();
        serverThread = data.thread || { messages: [] };
        taskState = data.state || null;
        return;
      }
    } catch (e) {}
    // 2) Fallback: estáticos del último deploy.
    try {
      var rt = await fetch('../sync/threads/' + T.id + '.json?_=' + Date.now(), { cache: 'no-store' });
      if (rt.ok) serverThread = await rt.json();
    } catch (e) {}
    try {
      var rs = await fetch('../sync/task_states.json?_=' + Date.now(), { cache: 'no-store' });
      if (rs.ok) {
        var st = await rs.json();
        taskState = (st.tasks || {})[T.id] || null;
      }
    } catch (e) {}
  }

  // ============================================================
  // Render
  // ============================================================
  function escHtml(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function fmtTs(ts) {
    try {
      return new Date(ts).toLocaleDateString('es-UY', { day: 'numeric', month: 'short' }) +
        ' ' + new Date(ts).toLocaleTimeString('es-UY', { hour: '2-digit', minute: '2-digit' });
    } catch (e) { return ''; }
  }

  function renderFeed(scrollToEnd) {
    var feed = document.getElementById('thread-feed');
    if (!feed) return;
    pruneEchoes();
    var seen = {};
    var msgs = (serverThread.messages || []).concat(echoes()).filter(function (m) {
      if (!m || !m.id || seen[m.id]) return false;
      seen[m.id] = 1;
      return true;
    });
    msgs.sort(function (a, b) { return String(a.ts).localeCompare(String(b.ts)); });
    if (!msgs.length) {
      feed.innerHTML = '<p class="thread-empty">Todavía no hay mensajes sobre esta tarea.' +
        ' Escribí abajo — soy todo hojas. 🌿</p>';
      return;
    }
    var html = '';
    var lastPendingUser = null;
    msgs.forEach(function (m) {
      var who = m.from === 'claude' ? 'claude' : 'user';
      var cls = 'msg ' + who + (m._sending ? ' sending' : '');
      var inner = '';
      if (m.kind === 'photo' && (m.photo || m._localSrc)) {
        var src = m._localSrc || ('../images/' + m.photo);
        inner += '<img src="' + escHtml(src) + '" loading="lazy" alt="Foto enviada" ' +
          'onerror="this.style.display=\'none\'">';
      }
      if (m.text) inner += escHtml(m.text);
      var who_label = who === 'claude' ? '🌿 Claude' : '';
      inner += '<span class="msg-meta">' + who_label + (who_label ? ' · ' : '') + escHtml(fmtTs(m.ts)) +
        (m._sending ? ' · enviando…' : '') + '</span>';
      html += '<div class="' + cls + '">' + inner + '</div>';
      if (who === 'user' && m.status === 'pending' && !m._sending) lastPendingUser = m;
    });
    if (lastPendingUser) {
      html += '<div class="msg-pending-hint">⏳ Recibido — lo reviso en mi próxima pasada y te aviso por notificación.</div>';
    }
    feed.innerHTML = html;
    if (scrollToEnd && feed.lastElementChild) {
      feed.lastElementChild.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }
  }

  function renderStateBanner() {
    var el = document.getElementById('state-banner');
    var actions = document.getElementById('task-actions');
    if (!el) return;
    var st = taskState || {};
    var status = st.status || 'active';
    if (status === 'snoozed' && st.snoozed_until && new Date(st.snoozed_until) <= new Date()) {
      status = 'active'; // misma auto-reactivación que el Timeline
    }
    if (status === 'done') {
      el.className = 'state-banner';
      el.innerHTML = '✅ Marcada como hecha' +
        (st.completed_at ? ' el ' + new Date(st.completed_at).toLocaleDateString('es-UY') : '') +
        ' <button type="button" id="btn-reactivate">Reactivar</button>';
      el.hidden = false;
      if (actions) actions.style.display = 'none';
    } else if (status === 'snoozed') {
      el.className = 'state-banner snoozed';
      el.innerHTML = '💤 Pospuesta hasta el ' +
        (st.snoozed_until ? new Date(st.snoozed_until).toLocaleDateString('es-UY') : '—') +
        ' <button type="button" id="btn-reactivate">Reactivar</button>';
      el.hidden = false;
      if (actions) actions.style.display = 'none';
    } else {
      el.hidden = true;
      if (actions) actions.style.display = '';
    }
    var re = document.getElementById('btn-reactivate');
    if (re) re.addEventListener('click', function () { sendState('active', null); });
  }

  // ============================================================
  // Envío de mensajes
  // ============================================================
  async function postApi(payload) {
    var r = await fetch(API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!r.ok) {
      var t = ''; try { t = await r.text(); } catch (e) {}
      throw new Error('HTTP ' + r.status + (t ? ' ' + t.slice(0, 80) : ''));
    }
    return r.json();
  }

  async function sendMessage() {
    if (_sending) return;
    var ta = document.getElementById('composer-text');
    var text = (ta.value || '').trim().slice(0, 2000);
    if (!text && !pendingPhoto) return;
    _sending = true;
    var btn = document.getElementById('btn-send');
    btn.disabled = true; btn.textContent = 'Enviando…';

    var msg = {
      id: msgId(),
      from: 'user',
      kind: pendingPhoto ? 'photo' : 'text',
      text: text || null,
      photo: null,
      ts: nowIso(),
      device: device(),
      status: 'pending',
      _sending: true,
    };
    if (pendingPhoto) msg._localSrc = pendingPhoto;

    // Echo optimista en el feed.
    serverThread.messages = (serverThread.messages || []);
    var echoMsg = msg;
    saveEchoTemp(echoMsg);
    renderFeed();

    var payload = {
      type: pendingPhoto ? 'photo' : 'message',
      task_id: T.id,
      plant_code: T.plant_code,
      task_title: T.title,
      message_id: msg.id,
      text: text || null,
      device: device(),
    };
    if (pendingPhoto) payload.base64 = pendingPhoto;

    try {
      var out = await postApi(payload);
      echoMsg._sending = false;
      removeEchoTemp(echoMsg.id);
      if (out && out.photo_path) echoMsg.photo = out.photo_path;
      saveEcho(stripLocal(echoMsg));
      ta.value = '';
      clearPhoto();
      _lastSync = { ok: true, error: null };
    } catch (e) {
      // Texto: al outbox durable. Foto: queda en el composer para reintentar.
      removeEchoTemp(echoMsg.id);
      if (!pendingPhoto) {
        outboxSet(outbox().concat([payload]));
        saveEcho(stripLocal(Object.assign({}, echoMsg, { _sending: false })));
        ta.value = '';
        _lastSync = { ok: false, error: String(e.message || e) };
      } else {
        alert('No se pudo mandar la foto (' + String(e.message || e) + '). Quedó acá — probá de nuevo.');
        _lastSync = { ok: false, error: String(e.message || e) };
      }
    } finally {
      _sending = false;
      btn.disabled = false; btn.textContent = 'Enviar ➤';
      renderFeed(true);
      renderBadge();
    }
  }

  // Echos temporales mientras viaja el POST (no persistidos).
  var _tempEchoes = [];
  function saveEchoTemp(m) { _tempEchoes.push(m); }
  function removeEchoTemp(id) { _tempEchoes = _tempEchoes.filter(function (m) { return m.id !== id; }); }
  function stripLocal(m) {
    var c = {}; Object.keys(m).forEach(function (k) { if (k[0] !== '_') c[k] = m[k]; });
    return c;
  }
  // echoes() para render incluye los temporales.
  var _echoesPersisted = echoes;
  echoes = function () { return _echoesPersisted().concat(_tempEchoes); };

  // ============================================================
  // Foto: elegir + resize (max 1024px, JPEG 0.85) → dataURL
  // ============================================================
  function clearPhoto() {
    pendingPhoto = null;
    var pv = document.getElementById('photo-preview');
    if (pv) pv.hidden = true;
    var inp = document.getElementById('photo-input');
    if (inp) inp.value = '';
  }

  function handlePhotoFile(file) {
    if (!file || !file.type || file.type.indexOf('image/') !== 0) return;
    var url = URL.createObjectURL(file);
    var img = new Image();
    img.onload = function () {
      var maxSide = 1024;
      var w = img.naturalWidth, h = img.naturalHeight;
      var scale = Math.min(1, maxSide / Math.max(w, h));
      var canvas = document.createElement('canvas');
      canvas.width = Math.round(w * scale);
      canvas.height = Math.round(h * scale);
      canvas.getContext('2d').drawImage(img, 0, 0, canvas.width, canvas.height);
      URL.revokeObjectURL(url);
      pendingPhoto = canvas.toDataURL('image/jpeg', 0.85);
      var pv = document.getElementById('photo-preview');
      var pvi = document.getElementById('photo-preview-img');
      if (pv && pvi) { pvi.src = pendingPhoto; pv.hidden = false; }
    };
    img.onerror = function () { URL.revokeObjectURL(url); alert('No pude leer esa imagen.'); };
    img.src = url;
  }

  // ============================================================
  // Estado hecha / posponer / reactivar
  // ============================================================
  async function sendState(status, snoozedUntil) {
    var payload = {
      type: 'state',
      task_id: T.id,
      status: status,
      snoozed_until: snoozedUntil,
      device: device(),
    };
    // Optimista: reflejar ya en el banner.
    taskState = {
      status: status,
      snoozed_until: snoozedUntil,
      completed_at: status === 'done' ? nowIso() : null,
    };
    renderStateBanner();
    document.getElementById('snooze-opts').classList.remove('open');
    try {
      await postApi(payload);
      _lastSync = { ok: true, error: null };
    } catch (e) {
      outboxSet(outbox().concat([payload]));
      _lastSync = { ok: false, error: String(e.message || e) };
    }
    renderBadge();
  }

  // ============================================================
  // Tracking de llegada (?nid=) → /api/feedback
  // ============================================================
  function pageName() {
    var parts = window.location.pathname.split('/');
    return 'tasks/' + (parts.pop() || 'index.html');
  }
  function trackLanding() {
    var params;
    try { params = new URLSearchParams(window.location.search); } catch (e) { return; }
    var nid = params.get('nid');
    var events = [];
    var now = nowIso();
    if (nid) {
      var seen = jget(SEEN_NIDS_KEY, []);
      if (seen.indexOf(nid) === -1) {
        seen.push(nid);
        jset(SEEN_NIDS_KEY, seen.slice(-50));
        events.push({ type: 'notification_clicked', nid: nid, page: pageName(), ts: now, device: device() });
      }
      params.delete('nid'); params.delete('src');
      var clean = window.location.pathname + (params.toString() ? '?' + params.toString() : '') + window.location.hash;
      history.replaceState(null, '', clean);
      events.push({ type: 'page_visit', page: pageName(), nid: nid, src: 'push', ts: now, device: device() });
    } else {
      var throttleKey = 'jardineando_visit_throttle_' + pageName();
      var last = parseInt(localStorage.getItem(throttleKey) || '0', 10);
      if (Date.now() - last < 60 * 60 * 1000) return;
      localStorage.setItem(throttleKey, String(Date.now()));
      events.push({ type: 'page_visit', page: pageName(), nid: null, src: 'direct', ts: now, device: device() });
    }
    if (!events.length) return;
    var stamped = events.map(function (e) {
      return Object.assign({ _id: Date.now().toString(36) + Math.random().toString(36).slice(2, 8) }, e);
    });
    try {
      fetch(FEEDBACK_API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ events: stamped, device: device() }),
      });
    } catch (e) {}
  }

  // ============================================================
  // Wiring
  // ============================================================
  function wire() {
    document.getElementById('btn-send').addEventListener('click', sendMessage);
    document.getElementById('btn-photo').addEventListener('click', function () {
      document.getElementById('photo-input').click();
    });
    document.getElementById('photo-input').addEventListener('change', function (ev) {
      handlePhotoFile(ev.target.files && ev.target.files[0]);
    });
    document.getElementById('photo-remove').addEventListener('click', clearPhoto);
    document.getElementById('btn-done').addEventListener('click', function () { sendState('done', null); });
    document.getElementById('btn-snooze').addEventListener('click', function () {
      document.getElementById('snooze-opts').classList.toggle('open');
    });
    Array.prototype.forEach.call(document.querySelectorAll('#snooze-opts button'), function (b) {
      b.addEventListener('click', function () {
        var d = new Date(Date.now() + parseInt(b.dataset.days, 10) * 24 * 3600 * 1000);
        sendState('snoozed', d.toISOString());
      });
    });
    document.getElementById('sync-badge').addEventListener('click', flushOutbox);
    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState === 'visible') { refresh(); flushOutbox(); }
    });
  }

  async function refresh() {
    await loadThread();
    renderFeed();
    renderStateBanner();
  }

  async function init() {
    wire();
    trackLanding();
    flushOutbox();
    renderFeed(); // echoes al toque, mientras carga el fetch
    await refresh();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
