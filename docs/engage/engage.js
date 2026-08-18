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
    // Ids capturados en ESTE flush: al confirmar, se remueven SOLO estos del
    // outbox — un evento encolado mientras el fetch estaba en vuelo (ej. tap
    // en reacción + enviar feedback de texto seguidos) queda para el próximo
    // flush en vez de borrarse sin haberse mandado.
    var sentIds = {};
    pending.forEach(function (e) { if (e._id) sentIds[e._id] = 1; });
    try {
      var r = await fetch('/api/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ events: pending, device: device() }),
      });
      if (r.ok) {
        outboxSet(outboxGet().filter(function (e) { return !e._id || !sentIds[e._id]; }));
        ok = true;
      }
      else {
        var t = ''; try { t = await r.text(); } catch (e) {}
        lastErr = 'HTTP ' + r.status + (t ? ' ' + t.slice(0, 60) : '');
      }
    } catch (e) {
      lastErr = (e && e.message) ? e.message : String(e);
    } finally { _flushing = false; }
    _lastSync = { ok: ok, error: ok ? null : (lastErr || 'desconocido') };
    renderSyncBadge();
    // Si durante el vuelo entró algo nuevo al outbox, mandarlo ya.
    if (ok && outboxGet().length) flushOutbox();
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

  // --- Desuscribirse de las notificaciones push DESDE la experiencia ---
  // (1) desuscribe el endpoint del browser; (2) si hay PAT, marca
  // docs/sync/push_subscription.json como "disabled" para que el dispatcher
  // deje de mandar. Mismo efecto que el botón "Desactivar" de Ajustes en el
  // inicio, pero accesible desde cualquier página de experiencia.
  var PUSH_SUB_PATH = 'docs/sync/push_subscription.json';
  window.engageUnsubscribe = async function (btn) {
    btn = btn || ((typeof event !== 'undefined' && event) ? event.target : null);
    var wrap = btn && btn.parentElement ? btn.parentElement : null;
    var hint = wrap ? wrap.querySelector('.unsub-hint') : null;
    function say(m) { if (hint) hint.textContent = m; }
    if (btn) btn.disabled = true;
    say('Desactivando…');
    var didLocal = false, didRepo = false;
    try {
      if ('serviceWorker' in navigator && 'PushManager' in window) {
        var reg = await navigator.serviceWorker.ready;
        var sub = await reg.pushManager.getSubscription();
        if (sub) { await sub.unsubscribe(); didLocal = true; }
      }
    } catch (e) { /* seguimos al paso del repo igual */ }
    try {
      if (token()) {
        var cur = await ghReadJson(PUSH_SUB_PATH);
        await ghWriteJson(PUSH_SUB_PATH, {
          device: (cur.data && cur.data.device) || device(),
          subscription: null,
          status: 'disabled',
          updated_at: new Date().toISOString(),
          invalidated_at: null,
          invalid_reason: 'desactivado por el usuario desde una experiencia',
        }, 'push: desactivar notificaciones (desde experiencia)', cur.sha);
        didRepo = true;
      }
    } catch (e) { /* el rebote del endpoint lo invalida igual */ }
    logEvents([{ type: 'push_unsubscribe', page: pageName(), local: didLocal, repo: didRepo,
      ts: new Date().toISOString(), device: device() }]);
    if (didRepo) say('🔕 Listo: no te llegan más notificaciones. Podés reactivarlas desde Ajustes en el inicio.');
    else if (didLocal) say('🔕 Desactivadas en este equipo. (Sin PAT no se avisó al repo, pero el envío se corta solo cuando rebote.)');
    else say('No había una suscripción activa en este equipo — ya estás sin notificaciones.');
  };

  // Inyecta un control discreto de "desuscribirme" al pie de cada experiencia.
  function injectUnsubControl() {
    if (!document.body || document.getElementById('engage-unsub')) return;
    var box = document.createElement('div');
    box.id = 'engage-unsub';
    box.style.cssText = 'max-width:560px;margin:14px auto 30px;text-align:center;' +
      'font:500 12.5px/1.45 -apple-system,BlinkMacSystemFont,sans-serif;';
    box.innerHTML =
      '<button type="button" onclick="engageUnsubscribe(this)" ' +
      'style="background:none;border:none;color:#9a7b12;text-decoration:underline;' +
      'cursor:pointer;font:inherit;padding:8px;">🔕 Desuscribirme de las notificaciones</button>' +
      '<div class="unsub-hint" style="color:#5a6b3c;margin-top:2px;"></div>';
    document.body.appendChild(box);
  }

  // --- Feedback libre en texto (pedido del usuario 18/07) ---
  // El texto que escriba acá lo lee el agente en su próxima pasada y es la
  // señal de MAYOR peso: feedback positivo = repetir el ángulo; negativo =
  // no volver a mandarlo; sin feedback = contenido "masomenos".
  // Uso en página (opcional, con estilo propio): un contenedor con
  // id="engage-feedback-box" que tenga un <textarea> y un botón que llame
  // engageFeedback('<slug>', this). Si la página NO trae el suyo, este
  // archivo inyecta uno estándar al pie automáticamente.
  window.engageFeedback = function (targetId, btn) {
    btn = btn || ((typeof event !== 'undefined' && event) ? event.target : null);
    var box = btn && btn.closest ? (btn.closest('#engage-feedback-box') || btn.closest('section') || btn.parentElement) : document.getElementById('engage-feedback-box');
    var ta = box ? box.querySelector('textarea') : null;
    var hint = box ? box.querySelector('.fb-hint') : null;
    var text = ta ? ta.value.trim() : '';
    if (!text) { if (hint) hint.textContent = 'Escribí algo primero — aunque sea una palabra.'; if (ta) ta.focus(); return; }
    if (btn) btn.disabled = true;
    if (ta) ta.disabled = true;
    if (hint) hint.textContent = 'Guardando…';
    logEvents([{ type: 'feedback_text', target: targetId || pageName(), text: text.slice(0, 2000),
      page: pageName(), ts: new Date().toISOString(), device: device() }]).then(function (ok) {
      if (hint) hint.textContent = ok
        ? '✓ Recibido. Lo leo en la próxima pasada y ajusto el rumbo con esto.'
        : '✓ Guardado en este equipo — se sube en cuanto haya conexión.';
    });
  };

  // Caja de feedback estándar: se inyecta en TODA experiencia que no traiga
  // la suya propia (id engage-feedback-box). Estilo autocontenido (tarjeta
  // oscura sólida) para funcionar sobre cualquier paleta.
  function injectFeedbackControl() {
    if (!document.body || document.getElementById('engage-feedback-box')) return;
    var slug = pageName().replace(/^engage\//, '').replace(/\.html$/, '');
    var box = document.createElement('section');
    box.id = 'engage-feedback-box';
    box.style.cssText = 'max-width:560px;margin:20px auto 6px;padding:18px 16px;border-radius:16px;' +
      'background:#14231a;border:1px solid rgba(255,255,255,.15);color:#eef4ec;text-align:center;' +
      'font:400 14px/1.5 -apple-system,BlinkMacSystemFont,sans-serif;box-shadow:0 4px 14px rgba(0,0,0,.25);';
    box.innerHTML =
      '<div style="font-weight:900;font-size:16.5px;margin-bottom:4px;">💬 Decime qué te pareció</div>' +
      '<div style="color:#b7c6bb;font-size:13.5px;max-width:42ch;margin:0 auto 12px;">Esto lo leo yo, el agente del jardín, antes de armar la próxima. Qué te gustó, qué te aburrió, qué querés ver — tu texto pesa más que cualquier botón.</div>' +
      '<textarea rows="3" placeholder="Escribime lo que quieras…" style="width:100%;box-sizing:border-box;' +
      'background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.2);border-radius:11px;color:#eef4ec;' +
      'padding:11px 12px;font:inherit;resize:vertical;"></textarea>' +
      '<button type="button" onclick="engageFeedback(\'' + slug.replace(/'/g, '') + '\', this)" ' +
      'style="margin-top:10px;background:#2f7d4f;color:#fff;border:none;border-radius:12px;padding:12px 20px;' +
      'font:800 14.5px -apple-system,BlinkMacSystemFont,sans-serif;cursor:pointer;">Enviar feedback</button>' +
      '<span class="fb-hint" style="display:block;margin-top:9px;font-size:12.5px;font-weight:700;color:#8fd06a;min-height:1.2em;"></span>';
    var unsub = document.getElementById('engage-unsub');
    if (unsub && unsub.parentElement) unsub.parentElement.insertBefore(box, unsub);
    else document.body.appendChild(box);
  }

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

  // --- Barra de señal rápida (18/08) ---------------------------------------
  // Diagnóstico que la motiva: el 17/08 el usuario abrió la experiencia a los
  // 2 min (récord del canal) pero se fue al 41 % de scroll. TODOS los controles
  // (1er tap 83 %, reacción 87 %, slots 90 %, caja de feedback 96 %) vivían
  // debajo de ese punto: el "cero señal activa" no fue desinterés, fue que
  // nunca tuvo un botón a mano. Esta barra flota apenas pasa el 25 % de scroll
  // (o a los 25 s) y le da 😍/🙂/🙅 + atajo al texto SIN scrollear hasta el pie.
  // Se auto-oculta al llegar al bloque de reacción real, es descartable, y no
  // vuelve a aparecer en una página donde ya dio señal.
  var QS_KEY = 'jardineando_quicksignal_done_v1';
  function qsDone() { try { return JSON.parse(localStorage.getItem(QS_KEY) || '{}'); } catch (e) { return {}; } }
  function qsMark(page) {
    try { var m = qsDone(); m[page] = 1; localStorage.setItem(QS_KEY, JSON.stringify(m)); } catch (e) {}
  }

  function installQuickSignal() {
    if (!document.body || document.getElementById('engage-quick-signal')) return;
    var page = pageName();
    if (qsDone()[page]) return;                       // ya dio señal acá
    var slug = page.replace(/^engage\//, '').replace(/\.html$/, '');

    var bar = document.createElement('div');
    bar.id = 'engage-quick-signal';
    bar.style.cssText = 'position:fixed;left:50%;transform:translateX(-50%) translateY(140%);' +
      'bottom:52px;z-index:99998;width:min(94vw,520px);box-sizing:border-box;padding:9px 10px;' +
      'border-radius:15px;background:#14231a;border:1px solid rgba(255,255,255,.16);' +
      'box-shadow:0 6px 22px rgba(0,0,0,.32);display:flex;align-items:center;gap:7px;' +
      'font:400 13px/1.3 -apple-system,BlinkMacSystemFont,sans-serif;color:#eef4ec;' +
      'transition:transform .32s cubic-bezier(.2,.8,.25,1);';
    var bs = 'background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);' +
      'border-radius:11px;cursor:pointer;padding:7px 9px;font-size:19px;line-height:1;';
    bar.innerHTML =
      '<span style="font-weight:800;font-size:12.5px;color:#b7c6bb;white-space:nowrap;">¿Va bien?</span>' +
      '<button type="button" data-v="love"  aria-label="Me encanta" style="' + bs + '">😍</button>' +
      '<button type="button" data-v="ok"    aria-label="Está bien"  style="' + bs + '">🙂</button>' +
      '<button type="button" data-v="no"    aria-label="No me sirve" style="' + bs + '">🙅</button>' +
      '<button type="button" data-v="text"  style="' + bs + 'font-size:12.5px;font-weight:800;padding:9px 10px;white-space:nowrap;">✍️ Escribir</button>' +
      '<button type="button" data-v="close" aria-label="Cerrar" style="background:none;border:none;color:#7d8f81;' +
      'cursor:pointer;font-size:16px;line-height:1;padding:6px 2px 6px 4px;margin-left:auto;">✕</button>';
    document.body.appendChild(bar);

    var shown = false, killed = false;
    function show() {
      if (shown || killed) return;
      shown = true; bar.style.transform = 'translateX(-50%) translateY(0)';
    }
    function hide(permanent) {
      if (killed) return;
      bar.style.transform = 'translateX(-50%) translateY(140%)';
      if (permanent) { killed = true; setTimeout(function () { if (bar.parentElement) bar.remove(); }, 400); }
    }

    bar.addEventListener('click', function (ev) {
      var b = ev.target.closest ? ev.target.closest('button') : null;
      if (!b) return;
      var v = b.getAttribute('data-v');
      if (v === 'close') {
        logEvents([{ type: 'quicksignal_dismiss', page: page, ts: new Date().toISOString(), device: device() }]);
        hide(true); return;
      }
      if (v === 'text') {
        var box = document.getElementById('engage-feedback-box');
        if (box) {
          box.scrollIntoView({ behavior: 'smooth', block: 'center' });
          var ta = box.querySelector('textarea');
          if (ta) setTimeout(function () { ta.focus(); }, 480);
        }
        logEvents([{ type: 'quicksignal_to_text', page: page, ts: new Date().toISOString(), device: device() }]);
        hide(true); return;
      }
      // Reacción: MISMO evento/target que el bloque de abajo (así el análisis
      // histórico no se parte), + via:"quickbar" para poder atribuirle el mérito.
      qsMark(page);
      logEvents([{ type: 'reaction', target: slug, value: v, via: 'quickbar',
        page: page, ts: new Date().toISOString(), device: device() }]);
      bar.innerHTML = '<span style="font-weight:800;font-size:13px;color:#8fd06a;padding:4px 6px;">' +
        '✓ Anotado. Con eso ajusto la próxima.</span>';
      setTimeout(function () { hide(true); }, 1900);
    });

    // Gatillos de aparición: 25 % de scroll o 25 s en página.
    function onScroll() { if (_scrollPct() >= 25) show(); }
    window.addEventListener('scroll', onScroll, { passive: true });
    setTimeout(function () { if (!killed) show(); }, 25000);

    // Si el bloque de reacción REAL entra en pantalla, la barra sobra: se va.
    try {
      var anchors = Array.prototype.filter.call(
        document.querySelectorAll('[onclick]'),
        function (el) { return /engageReact|engageFeedback|engageApprove/.test(el.getAttribute('onclick') || ''); });
      if (anchors.length && 'IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entries) {
          for (var i = 0; i < entries.length; i++) {
            if (entries[i].isIntersecting) { hide(true); io.disconnect(); return; }
          }
        }, { threshold: 0.35 });
        io.observe(anchors[0]);
      }
    } catch (e) {}
  }

  function init() { trackLanding(); injectUnsubControl(); injectFeedbackControl(); installQuickSignal(); }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
