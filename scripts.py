"""
JavaScript del documento.
Incluye:
- Tabs y subtabs
- Lightbox
- Búsqueda y filtros
- Timeline (newsfeed estilo Tinder)
- Modal de snooze
- Modal de WhatsApp con contactos por perfil
- Modal de edición de contactos
- localStorage para estado de tareas y contactos
"""

JS = r"""
// ============================================================
// CONSTANTES
// ============================================================
// Logo oficial de WhatsApp (path SVG monocromo, hereda color via currentColor)
const WHATSAPP_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.247-.694.247-1.289.173-1.413z"/></svg>';

// ============================================================
// TAB SWITCHING (top-level: Todo / Frente / Fondo / Timeline)
// ============================================================
function setBodyZone(zone) {
  document.body.classList.remove('zone-todo', 'zone-frente', 'zone-fondo', 'zone-interior', 'zone-timeline');
  document.body.classList.add(`zone-${zone}`);
}

document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.todo-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.zone-content').forEach(z => z.classList.remove('active'));
    btn.classList.add('active');
    const zone = btn.dataset.zone;
    document.querySelector(`.zone-content[data-zone="${zone}"]`).classList.add('active');
    setBodyZone(zone);
    window.scrollTo({top: 0, behavior: 'smooth'});
    if (zone === 'timeline') renderTimeline();
  });
});

// To-Do's button — entra al timeline (no es una zona-tab, es un CTA aparte)
document.querySelectorAll('.todo-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.todo-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.zone-content').forEach(z => z.classList.remove('active'));
    btn.classList.add('active');
    const zone = btn.dataset.zone;
    document.querySelector(`.zone-content[data-zone="${zone}"]`).classList.add('active');
    setBodyZone(zone);
    window.scrollTo({top: 0, behavior: 'smooth'});
    renderTimeline();
  });
});

// ============================================================
// SUBTAB SWITCHING (within zone)
// ============================================================
document.querySelectorAll('.zone-content').forEach(zoneEl => {
  zoneEl.querySelectorAll('.subtab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      zoneEl.querySelectorAll('.subtab-btn').forEach(b => b.classList.remove('active'));
      zoneEl.querySelectorAll('.subtab-pane').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      const sub = btn.dataset.sub;
      zoneEl.querySelector(`.subtab-pane[data-sub="${sub}"]`).classList.add('active');
    });
  });
});

// ============================================================
// IDEAS — botón "Ver todas" para expandir cards colapsadas
// ============================================================
document.querySelectorAll('button[data-show-all]').forEach(btn => {
  btn.addEventListener('click', () => {
    const grid = btn.previousElementSibling;
    if (!grid || !grid.matches('[data-collapsed-grid]')) return;
    const isExpanded = btn.getAttribute('aria-expanded') === 'true';
    if (isExpanded) {
      grid.hidden = true;
      btn.setAttribute('aria-expanded', 'false');
      btn.textContent = btn.textContent.replace(/^▴/, '▾').replace(/Ocultar/, 'Ver');
    } else {
      grid.hidden = false;
      btn.setAttribute('aria-expanded', 'true');
      btn.textContent = btn.textContent.replace(/^▾/, '▴').replace(/Ver/, 'Ocultar');
    }
  });
});

// ============================================================
// IMAGE LAZY LOADING (data-img)
// ============================================================
function loadImg(img) {
  const k = img.getAttribute('data-img');
  if (k && IMG[k] && !img.src) img.src = IMG[k];
}
document.querySelectorAll('img[data-img]').forEach(loadImg);

// ============================================================
// LIGHTBOX
// ============================================================
function setupLightbox(scope) {
  // Imágenes con data-action="open-species" abren el modal de detalle de
  // especie en vez del lightbox — útil para que tap en la foto de una tarea
  // del Timeline lleve directo al perfil de la planta.
  scope.querySelectorAll('img[data-action="open-species"]').forEach(img => {
    if (img.dataset.speciesBound) return;
    img.dataset.speciesBound = '1';
    img.addEventListener('click', (e) => {
      e.stopPropagation();
      const code = img.getAttribute('data-plant-code');
      if (code && typeof openSpeciesDetailModal === 'function') {
        openSpeciesDetailModal(code);
      }
    });
  });

  // Chips de "Aplica a" en cards de mejoras → abren modal de detalle
  scope.querySelectorAll('button[data-action="open-species"]').forEach(btn => {
    if (btn.dataset.speciesBound) return;
    btn.dataset.speciesBound = '1';
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const code = btn.getAttribute('data-plant-code');
      if (code && typeof openSpeciesDetailModal === 'function') {
        openSpeciesDetailModal(code);
      }
    });
  });

  scope.querySelectorAll('img[data-action="lightbox"]').forEach(img => {
    if (img.dataset.lightboxBound) return;
    img.dataset.lightboxBound = '1';
    img.addEventListener('click', (e) => {
      e.stopPropagation();
      const k = img.getAttribute('data-img');
      if (k && IMG[k]) {
        document.getElementById('lightbox-img').src = IMG[k];
        document.getElementById('lightbox').classList.add('active');
      }
    });
  });
}
setupLightbox(document);
document.getElementById('lightbox').addEventListener('click', function() {
  this.classList.remove('active');
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    document.getElementById('lightbox').classList.remove('active');
    document.querySelectorAll('.modal.active').forEach(m => m.classList.remove('active'));
  }
});

// ============================================================
// SEARCH + TAG FILTERS (zone view)
// ============================================================
document.querySelectorAll('.search').forEach(input => {
  input.addEventListener('input', () => {
    const pane = input.closest('.subtab-pane');
    if (!pane) return;
    const q = input.value.toLowerCase().trim();
    pane.querySelectorAll('.plant-card, .care-card, .idea-card, .huerta-card, .improvement-card').forEach(card => {
      const name = card.dataset.name || '';
      const tags = card.dataset.tags || '';
      const visible = !q || name.includes(q) || tags.includes(q);
      card.style.display = visible ? '' : 'none';
    });
  });
});

// Filtro de especies — chips dentro del panel desplegable
document.querySelectorAll('.filter-panel').forEach(panel => {
  panel.querySelectorAll('.ftag').forEach(btn => {
    btn.addEventListener('click', () => {
      panel.querySelectorAll('.ftag').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      const pane = panel.closest('.subtab-pane');
      if (pane) {
        pane.querySelectorAll('.plant-card').forEach(card => {
          const tags = card.dataset.tags || '';
          const visible = filter === 'all' || tags.includes(filter);
          card.style.display = visible ? '' : 'none';
        });
      }
      // Actualizar label del toggle (texto sin emoji) + cerrar el panel
      const zone = panel.dataset.zone;
      const toggle = document.querySelector(`.filter-toggle[data-zone="${zone}"]`);
      if (toggle) {
        const label = btn.textContent.replace(/^[^\p{L}\p{N}]+/u, '').trim();
        toggle.querySelector('.filter-current').textContent = label || 'Todas';
        toggle.setAttribute('aria-expanded', 'false');
      }
      panel.hidden = true;
    });
  });
});

// Toggle del panel (abrir/cerrar al apretar el ícono) + cerrar al click outside
document.addEventListener('click', (e) => {
  const toggle = e.target.closest('.filter-toggle');
  if (toggle) {
    e.stopPropagation();
    const zone = toggle.dataset.zone;
    const panel = document.querySelector(`.filter-panel[data-zone="${zone}"]`);
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    // Cerrar todos los toggles+paneles abiertos
    document.querySelectorAll('.filter-toggle[aria-expanded="true"]').forEach(t => {
      t.setAttribute('aria-expanded', 'false');
      const p = document.querySelector(`.filter-panel[data-zone="${t.dataset.zone}"]`);
      if (p) p.hidden = true;
    });
    if (!isOpen && panel) {
      toggle.setAttribute('aria-expanded', 'true');
      panel.hidden = false;
    }
    return;
  }
  // Click fuera del panel → cerrar
  if (!e.target.closest('.filter-panel')) {
    document.querySelectorAll('.filter-toggle[aria-expanded="true"]').forEach(t => {
      t.setAttribute('aria-expanded', 'false');
      const p = document.querySelector(`.filter-panel[data-zone="${t.dataset.zone}"]`);
      if (p) p.hidden = true;
    });
  }
});

// ============================================================
// TIMELINE — STATE MANAGEMENT (localStorage)
// ============================================================
const STATE_KEY = 'jardineando_task_states_v2';
const CONTACTS_KEY = 'jardineando_contacts_v1';

function loadStates() {
  try { return JSON.parse(localStorage.getItem(STATE_KEY) || '{}'); }
  catch { return {}; }
}
function saveStates(states) {
  localStorage.setItem(STATE_KEY, JSON.stringify(states));
  updateTodoCount();
}

// Cuenta tareas activas (auto-reactiva snoozed vencidas) y actualiza el label del To-Do's strip
function updateTodoCount() {
  const el = document.getElementById('todo-count');
  if (!el || typeof TASKS === 'undefined') return;
  const states = loadStates();
  const now = new Date();
  let active = 0;
  const userIds = Object.keys(USER_TASKS);
  const allIds = [
    ...TASKS.map(t => t.id),
    ...userIds,
  ];
  allIds.forEach(id => {
    const s = states[id] || { status: 'active', snoozed_until: null };
    let status = s.status;
    if (status === 'snoozed' && s.snoozed_until && new Date(s.snoozed_until) <= now) {
      status = 'active';
    }
    if (status === 'active') active++;
  });
  el.textContent = `${active} ${active === 1 ? 'pendiente' : 'pendientes'}`;
}
function getTaskState(taskId) {
  const states = loadStates();
  return states[taskId] || { status: 'active', snoozed_until: null, completed_at: null };
}
function setTaskState(taskId, state) {
  const states = loadStates();
  // Stamp last_modified_at automáticamente para que el sync sepa cuál es la versión más nueva.
  states[taskId] = { ...state, last_modified_at: new Date().toISOString() };
  saveStates(states);
  // Notificar al sync engine para que pushee debounced (definido más abajo).
  if (typeof markStateDirty === 'function') markStateDirty();
}

function loadContacts() {
  try {
    const stored = localStorage.getItem(CONTACTS_KEY);
    if (stored) return JSON.parse(stored);
  } catch {}
  return JSON.parse(JSON.stringify(DEFAULT_CONTACTS));  // copia profunda
}
function saveContacts(contacts) {
  localStorage.setItem(CONTACTS_KEY, JSON.stringify(contacts));
}

// ============================================================
// TIMELINE — RENDERING
// ============================================================
let currentFilter = 'active';

// USER_TASKS — declarado acá arriba (no al final del archivo) para que esté
// inicializado antes del bloque INIT que llama renderTimeline() / updateTodoCount()
// (línea ~1026). Si se declara con `let` cerca del final, esas llamadas tempranas
// crashean con TDZ ReferenceError aunque uses `typeof` como guard (typeof tira en TDZ).
const USER_TASKS_KEY = 'jardineando_user_tasks_v1';
const USER_TASKS_PATH = 'docs/sync/user_tasks.json';
let USER_TASKS = {};   // { id: {kind, title, user_context, plant_codes, ...} }

function classifyTask(task) {
  const st = getTaskState(task.id);
  if (st.status === 'done') return 'done';
  if (st.status === 'snoozed') {
    const until = new Date(st.snoozed_until);
    if (!isNaN(until) && until > new Date()) return 'snoozed';
    // snooze expirado → vuelve a activa
    return 'active';
  }
  return 'active';
}

function dueLabel(task) {
  if (!task.due_month || !task.due_year) return task.due_label || '';
  const monthNames = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
  return `${monthNames[task.due_month - 1]} ${task.due_year}`;
}

function isOverdue(task) {
  if (!task.due_month || !task.due_year) return false;
  // Tareas del mes ACTUAL (o anterior) ya cuentan como atrasadas — el usuario
  // espera ver flagged todo lo "que se puede hacer hoy o ayer".
  // Para fechas con día específico podríamos refinar pero no hay due_day en
  // los datos, así que usamos granularidad mensual: due_month <= curMonth = atrasada.
  const today = new Date();
  const curY = today.getFullYear();
  const curM = today.getMonth() + 1;
  return task.due_year < curY || (task.due_year === curY && task.due_month <= curM);
}

function priorityInfo(p) {
  return ({
    'alta':  { emo: '🔴', color: '#dc2626', label: 'Alta' },
    'media': { emo: '🟡', color: '#ca8a04', label: 'Media' },
    'baja':  { emo: '🟢', color: '#16a34a', label: 'Baja' },
  })[p] || { emo: '⚪', color: '#6b6457', label: p };
}

function fmtDate(iso) {
  if (!iso) return '';
  const d = new Date(iso);
  return d.toLocaleDateString('es-UY', { day: 'numeric', month: 'short', year: 'numeric' });
}

function renderTaskCard(task) {
  const st = getTaskState(task.id);
  const cls = classifyTask(task);
  const prio = priorityInfo(task.priority);
  const overdue = isOverdue(task);
  const isUserCreated = !!task.is_user_created;
  const isQuestion = task.kind === 'question';

  const photoHtml = task.plant_photo && IMG[task.plant_photo]
    ? `<img class="task-photo" data-img="${task.plant_photo}" data-action="open-species" data-plant-code="${task.plant_codes[0]}" alt="">`
    : `<div class="task-photo-placeholder">${isQuestion ? '❓' : (isUserCreated ? '✏️' : '🌱')}</div>`;

  let statusPill = '';
  if (cls === 'done') {
    const aiBadge = st.completed_via_ai ? ' · 🤖 IA' : '';
    statusPill = `<span class="task-status-pill done">✅ Hecha · ${fmtDate(st.completed_at)}${aiBadge}</span>`;
  } else if (cls === 'snoozed') {
    statusPill = `<span class="task-status-pill snoozed">😴 Pospuesta hasta ${fmtDate(st.snoozed_until)}</span>`;
  }

  // Banner de IA refresh: aparece en active si el slash command actualizó la descripción.
  let aiBanner = '';
  if (cls === 'active' && st.description_override) {
    const when = st.description_override_at ? fmtDate(st.description_override_at) : '';
    aiBanner = `<div class="task-ai-banner" title="Actualización por IA tras revisar foto">
      <div class="task-ai-banner-head">🤖 IA refresh${when ? ' · ' + when : ''}</div>
      <div class="task-ai-banner-body">${(st.description_override || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}</div>
    </div>`;
  }
  // Summary del último análisis cuando la tarea quedó hecha por IA
  let aiSummaryBlock = '';
  if (cls === 'done' && st.completed_via_ai && st.ai_summary) {
    aiSummaryBlock = `<div class="task-ai-summary">
      <span class="task-ai-summary-tag">🤖 Resolución IA</span>
      <span class="task-ai-summary-text">${st.ai_summary.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}</span>
    </div>`;
  }

  // Bloque de respuesta para preguntas: si /actualizar-tareas ya respondió,
  // mostrar el resumen de la respuesta inline en la tarjeta.
  let answerBlock = '';
  if (isQuestion && task.ai_answer && task.ai_answer.summary) {
    const ans = task.ai_answer.summary.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\n/g, '<br>');
    const when = task.ai_answer.answered_at ? fmtDate(task.ai_answer.answered_at) : '';
    answerBlock = `<div class="task-answer-block">
      <div class="task-answer-head">💬 Respuesta IA${when ? ' · ' + when : ''}</div>
      <div class="task-answer-body">${ans}</div>
    </div>`;
  } else if (isQuestion && cls === 'active') {
    answerBlock = `<div class="task-answer-pending">⏳ Esperando respuesta — corré <code>/actualizar-tareas</code> en Claude Code.</div>`;
  }

  // Badges de origen — tarea propia / pregunta.
  let originBadge = '';
  if (isQuestion) originBadge = '<span class="task-origin-badge question">❓ Pregunta</span>';
  else if (isUserCreated) originBadge = '<span class="task-origin-badge user">✏️ Tarea propia</span>';

  // Activas: botones según tipo. Las preguntas con respuesta tienen "Marcar leída" en lugar de los botones de acción.
  let actions = '';
  if (cls === 'active') {
    if (isQuestion) {
      // Preguntas: solo "Marcar leída" (= done). Sumar foto/responder más contexto si querés.
      const hasAnswer = !!(task.ai_answer && task.ai_answer.summary);
      actions = `
        <div class="task-actions">
          <button class="task-btn task-btn-done" data-action="done" data-task-id="${task.id}">${hasAnswer ? '✅ Marcar leída' : '✅ Cerrar'}</button>
          <button class="task-btn task-btn-photo" data-action="photo" data-task-id="${task.id}">📷 Sumar foto</button>
          <button class="task-btn task-btn-text" data-action="text" data-task-id="${task.id}">💬 Sumar contexto</button>
        </div>`;
    } else if (isUserCreated) {
      // Tareas propias: hecho / posponer / foto / texto. Sin WhatsApp (no tiene contacto sugerido).
      actions = `
        <div class="task-actions">
          <button class="task-btn task-btn-done" data-action="done" data-task-id="${task.id}">✅ Hecho</button>
          <button class="task-btn task-btn-snooze" data-action="snooze" data-task-id="${task.id}">😴 Posponer</button>
          <button class="task-btn task-btn-photo" data-action="photo" data-task-id="${task.id}">📷 Subir foto</button>
          <button class="task-btn task-btn-text" data-action="text" data-task-id="${task.id}">💬 Responder</button>
        </div>`;
    } else {
      actions = `
        <div class="task-actions">
          <button class="task-btn task-btn-done" data-action="done" data-task-id="${task.id}">✅ Hecho</button>
          <button class="task-btn task-btn-snooze" data-action="snooze" data-task-id="${task.id}">😴 Posponer</button>
          <button class="task-btn task-btn-photo" data-action="photo" data-task-id="${task.id}">📷 Subir foto</button>
          <button class="task-btn task-btn-text" data-action="text" data-task-id="${task.id}">💬 Responder</button>
          <button class="task-btn task-btn-whatsapp" data-action="whatsapp" data-task-id="${task.id}">💬 WhatsApp</button>
        </div>`;
    }
  } else {
    actions = `
      <div class="task-actions">
        <button class="task-btn task-btn-undo" data-action="reactivate" data-task-id="${task.id}">↺ Reactivar</button>
      </div>`;
  }

  const dueClass = overdue && cls === 'active' ? 'overdue' : '';
  const dueText = task.due_label || dueLabel(task);

  // Sección expandible con detalle + por qué + cómo
  const fmtMd = (s) => (s || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n/g, '<br>');

  const detailSection = task.detail
    ? `<div class="task-detail-section">
        <div class="task-detail-label">📖 Qué es / Por qué</div>
        <div class="task-detail-text">${fmtMd(task.detail)}</div>
      </div>`
    : '';

  const howToSection = task.how_to
    ? `<div class="task-detail-section">
        <div class="task-detail-label">🛠️ Cómo hacerla bien</div>
        <div class="task-detail-text task-howto">${fmtMd(task.how_to)}</div>
      </div>`
    : '';

  const tipsSection = task.tips
    ? `<div class="task-detail-section">
        <div class="task-detail-label">💡 Tips & tricks</div>
        <div class="task-detail-text">${fmtMd(task.tips)}</div>
      </div>`
    : '';

  const detailHtml = (detailSection || howToSection || tipsSection)
    ? `<div class="task-detail">${detailSection}${howToSection}${tipsSection}</div>`
    : '';

  // Side hints — solo para tareas activas (no se pueden swipear las done/snoozed)
  const sideHintLeft = (cls === 'active') ? `
    <div class="task-side-hint left" aria-label="Deslizar a la izquierda para posponer">
      <span class="hint-arrow">‹</span>
      <span class="hint-icon">😴</span>
    </div>` : '';
  const sideHintRight = (cls === 'active') ? `
    <div class="task-side-hint right" aria-label="Deslizar a la derecha para WhatsApp">
      <span class="hint-icon">${WHATSAPP_SVG}</span>
      <span class="hint-arrow">›</span>
    </div>` : '';

  return `
    <article class="task-card priority-${task.priority} ${cls === 'done' ? 'completed' : ''} ${cls === 'snoozed' ? 'snoozed' : ''}"
             data-task-id="${task.id}" style="--swipe-strength: 0">
      <span class="task-priority-dot" aria-hidden="true"></span>
      ${sideHintLeft}
      <div class="task-content-wrap">
        <div class="task-header">
          ${photoHtml}
          <div class="task-meta">
            <div class="task-meta-top">
              <span class="task-zone-pill">${task.plant_codes.join(', ').replace(/_general/g, 'Sin planta')}</span>
              <span class="task-id-badge" title="ID de la tarea — clickear para copiar">${task.id}</span>
              ${originBadge}
              ${statusPill}
            </div>
            <h3 class="task-title">${task.title}</h3>
            <div class="task-plant">${task.plant_common}</div>
            ${task.short_desc ? `<p class="task-short">${task.short_desc}</p>` : ''}
            ${answerBlock}
            ${aiBanner}
            ${aiSummaryBlock}
            ${dueText ? `<div class="task-due ${dueClass}">📅 ${overdue && cls === 'active' ? 'Vencida — ' : ''}${dueText}</div>` : ''}
            <span class="task-expand-chevron" aria-hidden="true">▾</span>
          </div>
        </div>
        ${detailHtml}
        ${actions}
      </div>
      ${sideHintRight}
    </article>`;
}

// Convierte un user_task (questions / user-created) al shape de Task que espera renderTaskCard.
function userTaskToTaskShape(ut) {
  return {
    id: ut.id,
    kind: ut.kind || 'user_task',
    plant_codes: ut.plant_codes && ut.plant_codes.length ? ut.plant_codes : ['_general'],
    plant_common: ut.plant_common || (ut.plant_codes && ut.plant_codes.length ? '' : 'Sin planta'),
    plant_zone: ut.plant_zone || null,
    plant_photo: null,
    title: ut.title || (ut.kind === 'question' ? 'Pregunta' : 'Tarea propia'),
    short_desc: '',
    description: ut.user_context || '',
    detail: ut.user_context || '',
    how_to: '',
    tips: '',
    priority: 'media',
    due_label: '',
    due_month: null,
    due_year: null,
    suggested_contact: null,
    is_user_created: true,
    has_photo: !!ut.has_photo,
    photo_filename: ut.photo_filename || null,
    ai_answer: ut.ai_answer || null,
    created_at: ut.created_at || null,
  };
}

function renderTimeline() {
  const feed = document.getElementById('timeline-feed');
  const empty = document.getElementById('timeline-empty');
  const summary = document.getElementById('timeline-summary');

  // Combinar TASKS del catálogo + user_tasks creadas desde la app.
  const userTaskList = Object.values(USER_TASKS).map(userTaskToTaskShape);
  const allTasks = [...TASKS, ...userTaskList];

  // Clasificar todas las tareas
  const buckets = { active: [], snoozed: [], done: [], all: [] };
  allTasks.forEach(task => {
    const cls = classifyTask(task);
    buckets[cls].push(task);
    buckets.all.push(task);
  });

  // Resumen — bloque informativo plano, una sola línea (estilo weather-line)
  summary.innerHTML = `
    <span class="summary-cell"><strong>${buckets.active.length}</strong> 📌 activas</span>
    <span class="summary-cell"><strong>${buckets.done.length}</strong> ✅ hechas</span>
    <span class="summary-cell"><strong>${buckets.snoozed.length}</strong> 😴 pospuestas</span>
  `;

  // Render filtered feed agrupado por mes (atrasadas → mes actual → futuros → sin fecha)
  const tasks = buckets[currentFilter] || [];

  if (tasks.length === 0) {
    feed.innerHTML = '';
    empty.style.display = 'block';
  } else {
    empty.style.display = 'none';
    feed.innerHTML = renderTasksGroupedByMonth(tasks);
    // hidratar imágenes y bind swipe + lightbox
    feed.querySelectorAll('img[data-img]').forEach(loadImg);
    setupLightbox(feed);
    setupTaskInteractions(feed);
  }
}

// Agrupa una lista de tareas por mes y devuelve el HTML con separadores.
// Hoy → "Mayo 2026"; meses anteriores con tareas pendientes → "⚠️ Atrasadas";
// meses futuros en orden cronológico ascendente; sin fecha al final.
const MONTH_NAMES_ES = [
  'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre',
];

function renderTasksGroupedByMonth(tasks) {
  const today = new Date();
  const curYear = today.getFullYear();
  const curMonth = today.getMonth() + 1;  // 1-12

  function bucketKey(t) {
    if (!t.due_year || !t.due_month) return 'sin-fecha';
    // Mismo criterio que isOverdue: mes actual o anterior → atrasadas.
    if (t.due_year < curYear || (t.due_year === curYear && t.due_month <= curMonth)) {
      return 'atrasadas';
    }
    return `${t.due_year}-${String(t.due_month).padStart(2, '0')}`;
  }
  function bucketLabel(key) {
    if (key === 'atrasadas') return '⚠️ Atrasadas';
    if (key === 'sin-fecha') return 'Sin fecha';
    const [y, m] = key.split('-');
    return `${MONTH_NAMES_ES[parseInt(m, 10) - 1]} ${y}`;
  }

  // Agrupar
  const groups = new Map();  // preserva orden de inserción
  tasks.forEach(t => {
    const k = bucketKey(t);
    if (!groups.has(k)) groups.set(k, []);
    groups.get(k).push(t);
  });

  // Orden de los buckets: atrasadas primero, luego YYYY-MM ascendente, sin-fecha al final
  const sortedKeys = [...groups.keys()].sort((a, b) => {
    if (a === b) return 0;
    if (a === 'atrasadas') return -1;
    if (b === 'atrasadas') return 1;
    if (a === 'sin-fecha') return 1;
    if (b === 'sin-fecha') return -1;
    return a < b ? -1 : 1;  // YYYY-MM string sort = chronological
  });

  const curMonthKey = `${curYear}-${String(curMonth).padStart(2, '0')}`;
  // "Futuro" = meses estrictamente posteriores al actual (no se pueden adelantar
  // por estar atadas a estación / floración / dormancia). Van en un módulo
  // colapsable cerrado por defecto para reducir ruido.
  const isFutureKey = (k) =>
    k !== 'atrasadas' && k !== 'sin-fecha' && k > curMonthKey;

  function renderGroup(k) {
    const items = groups.get(k);
    const headerCls = k === 'atrasadas' ? 'month-header overdue' : 'month-header';
    return (
      `<div class="${headerCls}" data-key="${k}">` +
        `<span class="month-label">${bucketLabel(k)}</span>` +
        `<span class="month-count">${items.length}</span>` +
      `</div>` +
      items.map(renderTaskCard).join('')
    );
  }

  const presentKeys = sortedKeys.filter(k => !isFutureKey(k));
  const futureKeys = sortedKeys.filter(isFutureKey);

  let html = presentKeys.map(renderGroup).join('');

  if (futureKeys.length > 0) {
    const futureCount = futureKeys.reduce((n, k) => n + groups.get(k).length, 0);
    const inner = futureKeys.map(renderGroup).join('');
    html += (
      `<details class="future-tasks">` +
        `<summary class="future-tasks-summary">` +
          `<span class="future-tasks-label">🗓️ Tareas futuras (no se pueden adelantar)</span>` +
          `<span class="future-tasks-count">${futureCount}</span>` +
          `<span class="future-tasks-chevron" aria-hidden="true">▾</span>` +
        `</summary>` +
        `<div class="future-tasks-body">${inner}</div>` +
      `</details>`
    );
  }

  return html;
}

// ============================================================
// TIMELINE — TASK INTERACTIONS (clicks + swipe)
// ============================================================
// Busca una tarea por id en el catálogo + las user_tasks creadas desde la app.
function findAnyTask(taskId) {
  const fromCat = TASKS.find(t => t.id === taskId);
  if (fromCat) return fromCat;
  const ut = USER_TASKS[taskId];
  return ut ? userTaskToTaskShape(ut) : null;
}

function setupTaskInteractions(scope) {
  // Click handlers para botones de acción
  scope.querySelectorAll('button[data-action]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const action = btn.dataset.action;
      const taskId = btn.dataset.taskId;
      const task = findAnyTask(taskId);
      if (!task) return;
      if (action === 'done') markDone(task);
      else if (action === 'snooze') openSnoozeModal(task);
      else if (action === 'whatsapp') openWhatsAppModal(task);
      else if (action === 'photo') openTaskPhotoModal(task);
      else if (action === 'text') openTaskTextModal(task);
      else if (action === 'reactivate') reactivateTask(task);
    });
  });

  // Click en task-header para expandir/colapsar.
  // Se ignora si:
  //   - el target es un botón (los maneja el handler de arriba)
  //   - el target es la foto (se abre lightbox)
  //   - hubo swipe reciente (flag justSwiped seteada por setupSwipe)
  scope.querySelectorAll('.task-card').forEach(card => {
    const header = card.querySelector('.task-header');
    if (!header) return;
    header.addEventListener('click', (e) => {
      if (e.target.closest('button')) return;
      if (e.target.closest('img')) return;
      if (card.dataset.justSwiped === '1') return;
      card.classList.toggle('expanded');
    });
  });

  // Swipe en cada card
  scope.querySelectorAll('.task-card').forEach(card => {
    setupSwipe(card);
  });
}

function setupSwipe(card) {
  // Solo tareas activas se pueden swipear
  if (card.classList.contains('completed') || card.classList.contains('snoozed')) return;

  let startX = 0, startY = 0, currentX = 0;
  let isDragging = false;
  let pointerDown = false;

  function onStart(x, y) {
    pointerDown = true;
    startX = x;
    startY = y;
    currentX = x;
    isDragging = false;
  }

  function onMove(x, y) {
    if (!pointerDown) return;
    const dx = x - startX;
    const dy = y - startY;
    if (!isDragging) {
      // determinar si es swipe horizontal vs scroll vertical
      if (Math.abs(dx) > 12 && Math.abs(dx) > Math.abs(dy)) {
        isDragging = true;
        card.classList.add('swiping');
      } else if (Math.abs(dy) > 12) {
        // scroll vertical, abandonar
        pointerDown = false;
        return;
      } else {
        return;
      }
    }
    currentX = x;
    const strength = Math.min(Math.abs(dx) / 120, 1);
    card.style.transform = `translateX(${dx}px) rotate(${dx * 0.05}deg)`;
    card.style.setProperty('--swipe-strength', strength);
    card.dataset.dxPositive = dx > 0;
    card.dataset.dxNegative = dx < 0;
  }

  function onEnd() {
    if (!pointerDown) return;
    pointerDown = false;
    if (!isDragging) return;
    const dx = currentX - startX;
    card.classList.remove('swiping');

    // Marcar flag para que el click handler ignore este "click" residual
    card.dataset.justSwiped = '1';
    setTimeout(() => { delete card.dataset.justSwiped; }, 350);

    const taskId = card.dataset.taskId;
    const task = findAnyTask(taskId);

    if (Math.abs(dx) > 100 && task) {
      if (dx > 0) {
        // swipe derecha → abrir modal WhatsApp (solo catálogo — user_tasks/questions no tienen contacto)
        card.style.transform = '';
        card.style.setProperty('--swipe-strength', 0);
        if (task.is_user_created) {
          // Para user-created sólo permitimos snooze a la izquierda; swipe a derecha no aplica.
          card.style.transform = '';
          return;
        }
        openWhatsAppModal(task);
      } else {
        // swipe izquierda → modal snooze
        card.style.transform = '';
        card.style.setProperty('--swipe-strength', 0);
        openSnoozeModal(task);
      }
    } else {
      // volver a posición
      card.style.transform = '';
      card.style.setProperty('--swipe-strength', 0);
    }
    delete card.dataset.dxPositive;
    delete card.dataset.dxNegative;
  }

  // Touch
  card.addEventListener('touchstart', (e) => {
    if (e.target.closest('button')) return;
    onStart(e.touches[0].clientX, e.touches[0].clientY);
  }, { passive: true });
  card.addEventListener('touchmove', (e) => {
    onMove(e.touches[0].clientX, e.touches[0].clientY);
  }, { passive: true });
  card.addEventListener('touchend', onEnd);
  card.addEventListener('touchcancel', onEnd);

  // Mouse (para testing en desktop)
  card.addEventListener('mousedown', (e) => {
    if (e.target.closest('button')) return;
    onStart(e.clientX, e.clientY);
  });
  document.addEventListener('mousemove', (e) => {
    if (pointerDown) onMove(e.clientX, e.clientY);
  });
  document.addEventListener('mouseup', () => {
    if (pointerDown) onEnd();
  });
}

// ============================================================
// TIMELINE — TASK ACTIONS
// ============================================================
function markDone(task) {
  setTaskState(task.id, {
    status: 'done',
    snoozed_until: null,
    completed_at: new Date().toISOString(),
  });
  setTimeout(renderTimeline, 100);
}

function reactivateTask(task) {
  setTaskState(task.id, { status: 'active', snoozed_until: null, completed_at: null });
  renderTimeline();
}

function snoozeTask(task, untilDate) {
  setTaskState(task.id, {
    status: 'snoozed',
    snoozed_until: untilDate,
    completed_at: null,
  });
  renderTimeline();
}

// ============================================================
// SNOOZE MODAL
// ============================================================
let pendingSnoozeTask = null;

function openSnoozeModal(task) {
  pendingSnoozeTask = task;
  document.getElementById('snooze-task-name').textContent = `📌 ${task.title} (${task.plant_common})`;
  document.getElementById('snooze-modal').classList.add('active');
  // pre-llenar fecha custom con hoy + 7
  const d = new Date(); d.setDate(d.getDate() + 7);
  document.getElementById('snooze-custom-date').valueAsDate = d;
}

document.querySelectorAll('.snooze-opt').forEach(btn => {
  btn.addEventListener('click', () => {
    if (!pendingSnoozeTask) return;
    const days = parseInt(btn.dataset.days, 10);
    const until = new Date();
    until.setDate(until.getDate() + days);
    snoozeTask(pendingSnoozeTask, until.toISOString());
    closeModal('snooze');
  });
});

document.getElementById('btn-snooze-custom').addEventListener('click', () => {
  if (!pendingSnoozeTask) return;
  const dateStr = document.getElementById('snooze-custom-date').value;
  if (!dateStr) return;
  const d = new Date(dateStr);
  if (d <= new Date()) { alert('Elegí una fecha futura'); return; }
  snoozeTask(pendingSnoozeTask, d.toISOString());
  closeModal('snooze');
});

// ============================================================
// WHATSAPP MODAL
// ============================================================
let pendingWaTask = null;
let pendingWaContactId = null;

function openWhatsAppModal(task) {
  pendingWaTask = task;
  pendingWaContactId = task.suggested_contact || null;
  document.getElementById('whatsapp-task-name').textContent = `📌 ${task.title} (${task.plant_common})`;
  renderWhatsAppContacts();
  // pre-llenar mensaje si hay contacto sugerido
  if (pendingWaContactId) {
    fillWhatsAppMessage(pendingWaContactId, task);
  } else {
    document.getElementById('whatsapp-message').value = '';
    document.getElementById('btn-send-whatsapp').disabled = true;
  }
  document.getElementById('whatsapp-modal').classList.add('active');
}

function renderWhatsAppContacts() {
  const contacts = loadContacts();
  const container = document.getElementById('whatsapp-contacts');
  container.innerHTML = contacts.map(c => {
    const noPhone = !c.phone || c.phone.trim() === '';
    return `
      <button class="wa-contact-btn ${pendingWaContactId === c.id ? 'active' : ''}" data-cid="${c.id}">
        <span class="wa-contact-icon">${c.icon}</span>
        <span class="wa-contact-name">${c.name}</span>
        ${noPhone ? '<span class="wa-contact-noPhone">(sin teléfono)</span>' : ''}
      </button>
    `;
  }).join('');
  container.querySelectorAll('.wa-contact-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      pendingWaContactId = btn.dataset.cid;
      renderWhatsAppContacts();
      fillWhatsAppMessage(pendingWaContactId, pendingWaTask);
    });
  });
}

function fillWhatsAppMessage(contactId, task) {
  const contacts = loadContacts();
  const c = contacts.find(x => x.id === contactId);
  if (!c) return;
  const taskText = `${task.title} — ${task.plant_common} (${task.plant_codes.join(', ')})`;
  const taskLink = SITE_URL ? `${SITE_URL}/tasks/${task.id}.html` : '';

  // Preferir plantilla específica por action_type × contacto si existe;
  // si no, caer al default_template del contacto.
  let template = null;
  if (task.action_type && typeof WHATSAPP_TEMPLATES !== 'undefined') {
    const byAction = WHATSAPP_TEMPLATES[task.action_type];
    if (byAction && byAction[contactId]) {
      template = byAction[contactId];
    }
  }
  if (!template) template = c.default_template || '';

  let msg = template.replace(/\{task\}/g, taskText);
  if (msg.includes('{link}')) {
    msg = msg.replace(/\{link\}/g, taskLink || '(link no disponible)');
  } else if (taskLink) {
    // Si la plantilla no incluye {link}, lo agregamos al final automáticamente.
    msg = msg + '\n\n📎 ' + taskLink;
  }

  document.getElementById('whatsapp-message').value = msg;
  document.getElementById('btn-send-whatsapp').disabled = !c.phone || c.phone.trim() === '';
}

document.getElementById('btn-send-whatsapp').addEventListener('click', () => {
  if (!pendingWaTask || !pendingWaContactId) return;
  const contacts = loadContacts();
  const c = contacts.find(x => x.id === pendingWaContactId);
  if (!c || !c.phone) {
    alert('Este contacto no tiene teléfono. Editalo desde "📞 Mis contactos".');
    return;
  }
  const phone = c.phone.replace(/[^0-9]/g, '');
  const msg = document.getElementById('whatsapp-message').value;
  const url = `https://wa.me/${phone}?text=${encodeURIComponent(msg)}`;
  window.open(url, '_blank');
  closeModal('whatsapp');
});

// ============================================================
// CONTACTS MODAL
// ============================================================
function openContactsModal() {
  renderContactsForm();
  document.getElementById('contacts-modal').classList.add('active');
}

function renderContactsForm() {
  const contacts = loadContacts();
  const list = document.getElementById('contacts-list');
  list.innerHTML = contacts.map((c, idx) => `
    <div class="contact-row" data-cid="${c.id}">
      <div class="contact-row-header">
        <span class="contact-row-icon">${c.icon}</span>
        <span class="contact-row-name">${c.name}</span>
      </div>
      <label class="contact-input-label">Teléfono (incluí código país, ej. +598 99 123 456)</label>
      <input type="tel" class="contact-input" data-field="phone" value="${(c.phone || '').replace(/"/g, '&quot;')}" placeholder="+598 99 123 456">
      <label class="contact-input-label">Plantilla del mensaje (usá {task} para insertar la tarea)</label>
      <textarea class="contact-input template" data-field="default_template" rows="3">${(c.default_template || '').replace(/</g,'&lt;')}</textarea>
    </div>
  `).join('');
}

document.getElementById('btn-edit-contacts').addEventListener('click', openContactsModal);

document.getElementById('btn-save-contacts').addEventListener('click', () => {
  const contacts = loadContacts();
  document.querySelectorAll('#contacts-list .contact-row').forEach(row => {
    const cid = row.dataset.cid;
    const c = contacts.find(x => x.id === cid);
    if (!c) return;
    c.phone = row.querySelector('[data-field="phone"]').value.trim();
    c.default_template = row.querySelector('[data-field="default_template"]').value;
  });
  saveContacts(contacts);
  closeModal('contacts');
  // refrescar modal whatsapp si está abierto
  if (pendingWaTask) renderWhatsAppContacts();
});

document.getElementById('btn-reset-contacts').addEventListener('click', () => {
  if (!confirm('¿Restaurar los contactos por defecto? Perderás los teléfonos guardados.')) return;
  saveContacts(JSON.parse(JSON.stringify(DEFAULT_CONTACTS)));
  renderContactsForm();
});

// ============================================================
// MODAL CLOSE HANDLERS
// ============================================================
function closeModal(name) {
  document.getElementById(`${name}-modal`).classList.remove('active');
}
document.querySelectorAll('.modal-close').forEach(btn => {
  btn.addEventListener('click', () => closeModal(btn.dataset.close));
});
document.querySelectorAll('.modal').forEach(modal => {
  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('active');
  });
});

// ============================================================
// TIMELINE FILTERS
// ============================================================
document.querySelectorAll('.timeline-filters .ftag').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.timeline-filters .ftag').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentFilter = btn.dataset.filter;
    renderTimeline();
  });
});

// ============================================================
// INIT
// ============================================================
renderTimeline();
updateTodoCount();

// Si la URL trae #task=ID (viene de un share), abrir Timeline + expandir + scroll
function openTaskFromHash() {
  const m = (window.location.hash || '').match(/^#task=(.+)$/);
  if (!m) return;
  const taskId = decodeURIComponent(m[1]);
  // Switch a Timeline (ahora vive en el To-Do's strip, no en main-tabs)
  const tlBtn = document.querySelector('.todo-btn[data-zone="timeline"]');
  if (tlBtn) tlBtn.click();
  // Buscar la tarea — puede estar en filter "active" o no, así que vamos a "all"
  const task = TASKS.find(t => t.id === taskId);
  if (!task) return;
  // Cambiar al filtro "all" para asegurar que la veamos sea cual sea su estado
  const allBtn = document.querySelector('.timeline-filters .ftag[data-filter="all"]');
  if (allBtn) {
    document.querySelectorAll('.timeline-filters .ftag').forEach(b => b.classList.remove('active'));
    allBtn.classList.add('active');
    currentFilter = 'all';
    renderTimeline();
  }
  // Expandir y scroll después del render
  setTimeout(() => {
    const card = document.querySelector(`.task-card[data-task-id="${taskId}"]`);
    if (card) {
      card.classList.add('expanded');
      card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      // Highlight visual breve
      card.style.transition = 'box-shadow 0.4s ease';
      card.style.boxShadow = '0 0 0 3px rgba(21, 128, 61, 0.4)';
      setTimeout(() => { card.style.boxShadow = ''; }, 2200);
    }
  }, 200);
}
openTaskFromHash();
window.addEventListener('hashchange', openTaskFromHash);

// ============================================================
// CLIMA EN MONTEVIDEO (Open-Meteo, sin API key)
// ============================================================
function weatherCondition(code) {
  // WMO weather codes → emoji + label
  if (code === 0) return { emoji: '☀️', label: 'despejado' };
  if (code <= 2) return { emoji: '🌤️', label: 'algo nublado' };
  if (code === 3) return { emoji: '☁️', label: 'nublado' };
  if (code <= 48) return { emoji: '🌫️', label: 'niebla' };
  if (code <= 57) return { emoji: '🌦️', label: 'llovizna' };
  if (code <= 67) return { emoji: '🌧️', label: 'lluvia' };
  if (code <= 77) return { emoji: '🌨️', label: 'nieve' };
  if (code <= 82) return { emoji: '🌧️', label: 'chubascos' };
  if (code >= 95) return { emoji: '⛈️', label: 'tormenta' };
  return { emoji: '🌤️', label: '' };
}

async function loadWeather() {
  const el = document.getElementById('weather-line');
  if (!el) return;
  try {
    // Montevideo, Uruguay — coords
    const url = 'https://api.open-meteo.com/v1/forecast?latitude=-34.9011&longitude=-56.1645&current=temperature_2m,weather_code,wind_speed_10m,relative_humidity_2m&timezone=America%2FMontevideo';
    const r = await fetch(url, { cache: 'no-store' });
    if (!r.ok) throw new Error('HTTP ' + r.status);
    const data = await r.json();
    const c = data.current;
    const w = weatherCondition(c.weather_code);
    const temp = Math.round(c.temperature_2m);
    const wind = Math.round(c.wind_speed_10m);
    const hum = Math.round(c.relative_humidity_2m);
    el.innerHTML = `
      <span class="weather-cell" title="${w.label}"><span class="weather-emoji">${w.emoji}</span><span class="weather-val"><strong>${temp}°</strong></span></span>
      <span class="weather-cell" title="Viento"><span class="weather-emoji">💨</span><span class="weather-val">${wind} km/h</span></span>
      <span class="weather-cell" title="Humedad"><span class="weather-emoji">💧</span><span class="weather-val">${hum}%</span></span>
      <span class="weather-cell" title="Ubicación"><span class="weather-emoji">📍</span><span class="weather-val">Montevideo</span></span>`;
  } catch (err) {
    el.innerHTML = `
      <span class="weather-cell"><span class="weather-emoji">🌱</span><span class="weather-val">Montevideo</span></span>`;
  }
}
loadWeather();

// ============================================================
// SERVICE WORKER — registro mínimo para que Chrome/Android consideren
// el sitio "instalable" y use el icon de la manifest en home screen.
// El SW no cachea nada (passthrough); existe solo para cumplir el
// criterio de installability de PWA.
// ============================================================
// Estado del PWA — usado por el panel de diagnóstico en settings.
const _pwaState = {
  swSupported: 'serviceWorker' in navigator,
  swRegistered: false,
  swActive: false,
  swError: null,
  manifestStatus: 'checking',
  manifestError: null,
  authGatingDetected: false,
  authGatingDetail: null,
  installable: false,
  installed: false,
  isStandalone: window.matchMedia('(display-mode: standalone)').matches,
};

if (_pwaState.swSupported) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('sw.js')
      .then(reg => {
        _pwaState.swRegistered = true;
        _pwaState.swActive = !!reg.active;
        reg.addEventListener('updatefound', () => {
          const nw = reg.installing;
          if (nw) nw.addEventListener('statechange', () => {
            if (nw.state === 'activated') _pwaState.swActive = true;
            updatePwaStatusPanel();
          });
        });
        updatePwaStatusPanel();
      })
      .catch(err => {
        _pwaState.swError = err.message || String(err);
        console.warn('SW registration failed:', err);
        updatePwaStatusPanel();
      });
  });
}

// Verificar manifest fetch + parse.
fetch('manifest.webmanifest', { cache: 'no-store' })
  .then(r => {
    if (!r.ok) throw new Error('HTTP ' + r.status);
    const ct = r.headers.get('content-type') || '';
    if (!ct.includes('manifest') && !ct.includes('json')) {
      _pwaState.manifestError = 'MIME incorrecto: ' + ct;
    }
    return r.json();
  })
  .then(m => {
    _pwaState.manifestStatus = 'ok';
    _pwaState.manifestData = { name: m.name, icons: (m.icons || []).length };
    updatePwaStatusPanel();
  })
  .catch(err => {
    _pwaState.manifestStatus = 'fail';
    _pwaState.manifestError = err.message || String(err);
    updatePwaStatusPanel();
  });

// Detección de auth gating (ej: Vercel Deployment Protection). Hacemos un
// segundo fetch del manifest CON credentials='omit' — Chrome internal
// PWA installability check usa contexto similar. Si el con-cookies devuelve
// 200 pero el sin-cookies devuelve 401/redirect, la PWA NO se considera
// installable porque Chrome ve los recursos como inaccesibles.
fetch('manifest.webmanifest', { cache: 'no-store', credentials: 'omit', redirect: 'manual' })
  .then(r => {
    // r.type === 'opaqueredirect' cuando hay redirect (típico de Vercel SSO).
    // r.status === 0 también común en ese caso con redirect: 'manual'.
    if (r.type === 'opaqueredirect' || r.status === 401 || r.status === 403 ||
        (r.headers.get('content-type') || '').includes('text/html')) {
      _pwaState.authGatingDetected = true;
      _pwaState.authGatingDetail = `Vercel/auth gate: con cookies funciona, sin cookies devuelve ${r.status === 0 ? 'redirect' : 'HTTP ' + r.status}. Chrome no puede validar la PWA en estas condiciones.`;
      updatePwaStatusPanel();
    }
  })
  .catch(() => { /* network error, ignore — el otro fetch ya cubre fail */ });

// PWA install prompt — capturar el evento.
let _deferredInstallPrompt = null;
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  _deferredInstallPrompt = e;
  _pwaState.installable = true;
  showInstallBanner();
  updatePwaStatusPanel();
});

window.addEventListener('appinstalled', () => {
  _pwaState.installed = true;
  updatePwaStatusPanel();
});

function updatePwaStatusPanel() {
  const panel = document.getElementById('pwa-status-panel');
  const btn = document.getElementById('btn-trigger-install');
  if (!panel) return;
  const yes = '<span class="pwa-st-ok">✓</span>';
  const no = '<span class="pwa-st-err">✗</span>';
  const wait = '<span class="pwa-st-wait">⏳</span>';
  let html = '<div class="pwa-st-row">' + (_pwaState.swSupported ? yes : no) + ' Service Worker support en este browser</div>';
  if (_pwaState.swSupported) {
    if (_pwaState.swError) {
      html += `<div class="pwa-st-row">${no} SW registrado — error: <code>${_pwaState.swError}</code></div>`;
    } else if (_pwaState.swRegistered) {
      html += `<div class="pwa-st-row">${yes} SW registrado${_pwaState.swActive ? ' y activo' : ' (activando…)'}</div>`;
    } else {
      html += `<div class="pwa-st-row">${wait} SW registrando…</div>`;
    }
  }
  if (_pwaState.manifestStatus === 'ok') {
    html += `<div class="pwa-st-row">${yes} Manifest cargado (${_pwaState.manifestData?.icons || 0} icons)</div>`;
  } else if (_pwaState.manifestStatus === 'fail') {
    html += `<div class="pwa-st-row">${no} Manifest falla: <code>${_pwaState.manifestError}</code></div>`;
  } else {
    html += `<div class="pwa-st-row">${wait} Manifest verificando…</div>`;
  }
  if (_pwaState.authGatingDetected) {
    html += `<div class="pwa-st-row">${no} <strong>Auth gating detectado</strong> — el deployment exige login para servir los recursos. ${_pwaState.authGatingDetail || ''} <br><strong>Fix:</strong> Vercel Dashboard → Project → Settings → Deployment Protection → "None" (o usar un custom domain / cambiar a GitHub Pages).</div>`;
  }
  if (_pwaState.isStandalone || _pwaState.installed) {
    html += `<div class="pwa-st-row">${yes} App ya instalada (corriendo en standalone)</div>`;
  } else if (_pwaState.installable) {
    html += `<div class="pwa-st-row">${yes} Chrome dice que es installable — click el botón abajo</div>`;
  } else {
    html += `<div class="pwa-st-row">${wait} Chrome aún no disparó <code>beforeinstallprompt</code>. Causas: engagement insuficiente (navegá unos minutos), auth gating, o algún criterio falla.</div>`;
  }
  panel.innerHTML = html;
  if (btn) {
    btn.disabled = !_deferredInstallPrompt;
    btn.textContent = _deferredInstallPrompt ? '📲 Instalar app ahora' : 'Esperando que Chrome lo habilite…';
  }
}

// Bind del botón manual.
document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('btn-trigger-install');
  if (btn) btn.addEventListener('click', async () => {
    if (!_deferredInstallPrompt) return;
    _deferredInstallPrompt.prompt();
    await _deferredInstallPrompt.userChoice;
    _deferredInstallPrompt = null;
    updatePwaStatusPanel();
  });

  const resetBtn = document.getElementById('btn-reset-sw');
  if (resetBtn) resetBtn.addEventListener('click', async () => {
    if (!confirm('Resetear el Service Worker? Después de esto recargá la página para registrar la versión nueva.')) return;
    try {
      if ('serviceWorker' in navigator) {
        const regs = await navigator.serviceWorker.getRegistrations();
        await Promise.all(regs.map(r => r.unregister()));
      }
      if (window.caches) {
        const keys = await caches.keys();
        await Promise.all(keys.map(k => caches.delete(k)));
      }
      alert('SW reseteado y caches borrados. Recargá la página (Ctrl+Shift+R o cerrá y reabrí la pestaña).');
    } catch (e) {
      alert('Error al resetear SW: ' + (e.message || e));
    }
  });
});

function showInstallBanner() {
  if (document.getElementById('pwa-install-banner')) return;
  const banner = document.createElement('div');
  banner.id = 'pwa-install-banner';
  banner.innerHTML = `
    <span class="pwa-install-icon">📲</span>
    <span class="pwa-install-text">Instalar Jardineando como app</span>
    <button class="pwa-install-btn">Instalar</button>
    <button class="pwa-install-dismiss" aria-label="Cerrar">✕</button>
  `;
  document.body.appendChild(banner);
  banner.querySelector('.pwa-install-btn').addEventListener('click', async () => {
    if (!_deferredInstallPrompt) return;
    _deferredInstallPrompt.prompt();
    const { outcome } = await _deferredInstallPrompt.userChoice;
    _deferredInstallPrompt = null;
    banner.remove();
  });
  banner.querySelector('.pwa-install-dismiss').addEventListener('click', () => {
    banner.remove();
    localStorage.setItem('pwa_install_dismissed', '1');
  });
}

// Si ya se instaló antes, log y nada más.
window.addEventListener('appinstalled', () => {
  console.log('[PWA] instalada — banner cerrado');
  const banner = document.getElementById('pwa-install-banner');
  if (banner) banner.remove();
});

// ============================================================
// SETTINGS — GitHub PAT + device name (localStorage only)
// ============================================================
const GITHUB_TOKEN_KEY = 'jardineando_github_token_v1';
const DEVICE_NAME_KEY = 'jardineando_device_name_v1';
const CANONICAL_URL_KEY = 'jardineando_canonical_url_v1';

function loadGitHubToken() {
  return localStorage.getItem(GITHUB_TOKEN_KEY) || '';
}
function saveGitHubToken(token) {
  if (token) localStorage.setItem(GITHUB_TOKEN_KEY, token);
  else localStorage.removeItem(GITHUB_TOKEN_KEY);
}
function loadDeviceName() {
  return localStorage.getItem(DEVICE_NAME_KEY) || '';
}
function saveDeviceName(name) {
  if (name) localStorage.setItem(DEVICE_NAME_KEY, name);
  else localStorage.removeItem(DEVICE_NAME_KEY);
}
function loadCanonicalUrl() {
  return localStorage.getItem(CANONICAL_URL_KEY) || '';
}
function saveCanonicalUrl(url) {
  if (url) localStorage.setItem(CANONICAL_URL_KEY, url);
  else localStorage.removeItem(CANONICAL_URL_KEY);
}

// Detectar si la URL actual parece un Vercel preview (URLs con hash que rotan
// en cada deploy y a los días dejan de funcionar).
function isEphemeralHostname(host) {
  // Vercel preview: <project>-git-<branch>-<team>-<8hexhash>.vercel.app
  if (/-[0-9a-f]{8}\.vercel\.app$/i.test(host)) return true;
  // Vercel deployment URL: <project>-<8hexhash>-<team>.vercel.app
  if (/-[0-9a-z]{9,}\.vercel\.app$/i.test(host)) return true;
  // Netlify deploy preview
  if (/--[a-f0-9]{6,}\.netlify\.app$/i.test(host)) return true;
  return false;
}

function getEffectiveSiteUrl() {
  const canonical = loadCanonicalUrl();
  return canonical || (window.location.origin + window.location.pathname);
}

async function testGitHubToken(token) {
  if (!token) throw new Error('Falta token');
  const r = await fetch('https://api.github.com/user', {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Accept': 'application/vnd.github+json',
    },
  });
  if (!r.ok) {
    if (r.status === 401) throw new Error('Token inválido o revocado');
    if (r.status === 403) throw new Error('Token sin permisos suficientes');
    throw new Error(`HTTP ${r.status}`);
  }
  const data = await r.json();
  // Validar acceso al repo específico
  const repoR = await fetch('https://api.github.com/repos/abecedeefege/gardening', {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Accept': 'application/vnd.github+json',
    },
  });
  if (!repoR.ok) {
    throw new Error('No tiene acceso al repo abecedeefege/gardening');
  }
  return { user: data.login };
}

function openSettingsModal() {
  const token = loadGitHubToken();
  document.getElementById('settings-github-token').value = token;
  document.getElementById('settings-device-name').value = loadDeviceName();
  document.getElementById('settings-canonical-url').value = loadCanonicalUrl();
  document.getElementById('settings-github-feedback').textContent = '';
  document.getElementById('settings-github-feedback').className = 'settings-feedback';
  // Avisar si estamos en una URL ephemeral y no hay canonical configurada.
  const fb = document.getElementById('settings-canonical-feedback');
  if (!loadCanonicalUrl() && isEphemeralHostname(window.location.hostname)) {
    fb.textContent = '⚠️ Estás en una URL temporal (preview de Vercel). Configurá la URL canónica para que los links de transferencia no se rompan.';
    fb.className = 'settings-feedback warn';
  } else {
    fb.textContent = '';
    fb.className = 'settings-feedback';
  }
  // Sección de transfer solo aparece si ya hay token configurado.
  document.getElementById('settings-transfer-section').hidden = !token;
  document.getElementById('transfer-link-output').hidden = true;
  document.getElementById('settings-modal').classList.add('active');
  // Refrescar el panel de PWA status al abrir.
  if (typeof updatePwaStatusPanel === 'function') updatePwaStatusPanel();
}

document.getElementById('btn-open-settings').addEventListener('click', openSettingsModal);

document.getElementById('btn-test-github-token').addEventListener('click', async () => {
  const token = document.getElementById('settings-github-token').value.trim();
  const fb = document.getElementById('settings-github-feedback');
  if (!token) {
    fb.textContent = '⚠️ Pegá un token primero';
    fb.className = 'settings-feedback warn';
    return;
  }
  fb.textContent = '⏳ Probando…';
  fb.className = 'settings-feedback';
  try {
    const result = await testGitHubToken(token);
    fb.textContent = `✅ Conectado como ${result.user} · acceso al repo OK`;
    fb.className = 'settings-feedback ok';
  } catch (err) {
    fb.textContent = `❌ ${err.message}`;
    fb.className = 'settings-feedback err';
  }
});

document.getElementById('btn-clear-github-token').addEventListener('click', () => {
  if (!confirm('¿Borrar el token de este dispositivo? Sin token no podrás subir fotos ni sincronizar.')) return;
  saveGitHubToken('');
  document.getElementById('settings-github-token').value = '';
  const fb = document.getElementById('settings-github-feedback');
  fb.textContent = '🗑 Token eliminado';
  fb.className = 'settings-feedback';
});

document.getElementById('btn-save-settings').addEventListener('click', () => {
  const token = document.getElementById('settings-github-token').value.trim();
  const deviceName = document.getElementById('settings-device-name').value.trim();
  const canonical = document.getElementById('settings-canonical-url').value.trim();
  saveGitHubToken(token);
  saveDeviceName(deviceName);
  saveCanonicalUrl(canonical);
  closeModal('settings');
});

// ============================================================
// TRANSFER LINK — pasar el PAT a otro device sin tipear
// ============================================================
// Se genera un URL `<sitio>?import_token=<base64>` que el usuario manda a su
// otro device por canal privado (WhatsApp Web a sí mismo, AirDrop, mail).
// El token NUNCA pasa por el repo. Es una transferencia entre devices del
// mismo usuario, end-to-end (vía el canal que él elija).
function generateTransferLink() {
  const token = loadGitHubToken();
  if (!token) return null;
  const payload = JSON.stringify({ t: token, d: loadDeviceName() });
  // base64 URL-safe (sin + / =).
  const b64 = btoa(unescape(encodeURIComponent(payload)))
    .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  const baseUrl = getEffectiveSiteUrl();
  // Separador correcto según si baseUrl ya tiene query string.
  const sep = baseUrl.includes('?') ? '&' : '?';
  return `${baseUrl}${sep}import_token=${b64}`;
}

document.getElementById('btn-gen-transfer-link').addEventListener('click', () => {
  const token = loadGitHubToken();
  if (!token) {
    alert('No hay token configurado todavía. Pegá uno arriba y guardá primero.');
    return;
  }
  // Validar canonical URL antes de generar.
  if (!loadCanonicalUrl() && isEphemeralHostname(window.location.hostname)) {
    const ok = confirm(
      '⚠️ Estás en una URL temporal (preview de Vercel). El link de transferencia ' +
      'apuntará a esta URL y puede dejar de funcionar en pocos días cuando Vercel ' +
      'reasigne la preview.\n\n' +
      'Mejor cerrá esto, andá al campo "URL canónica del sitio" arriba, pegá tu URL ' +
      'estable y guardá. ¿Generar igual?'
    );
    if (!ok) return;
  }
  const link = generateTransferLink();
  document.getElementById('transfer-link-text').value = link;
  // Renderizar QR.
  try {
    const svg = qrEncodeSvg(link, { cellSize: 5, margin: 4 });
    document.getElementById('transfer-qr').innerHTML = svg;
  } catch (err) {
    document.getElementById('transfer-qr').innerHTML =
      `<div class="transfer-qr-error">⚠️ No se pudo generar el QR (${err.message}). Usá el link de abajo.</div>`;
  }
  document.getElementById('transfer-link-output').hidden = false;
});

document.getElementById('btn-copy-transfer-link').addEventListener('click', async () => {
  const ta = document.getElementById('transfer-link-text');
  const text = ta.value;
  const btn = document.getElementById('btn-copy-transfer-link');
  const orig = btn.textContent;
  try {
    await navigator.clipboard.writeText(text);
    btn.textContent = '✓ Copiado';
  } catch {
    // Fallback sin clipboard API (iOS viejo, file://, etc.).
    ta.removeAttribute('readonly');
    ta.select();
    try { document.execCommand('copy'); btn.textContent = '✓ Copiado'; }
    catch { btn.textContent = '⚠️ Seleccioná y copiá manualmente'; }
    ta.setAttribute('readonly', 'true');
  }
  setTimeout(() => { btn.textContent = orig; }, 2200);
});

// Receive-side: si la URL trae ?import_token=..., ofrecer importarlo.
function handleTransferImport() {
  const params = new URLSearchParams(window.location.search);
  const importToken = params.get('import_token');
  if (!importToken) return;

  let payload = null;
  try {
    const b64 = importToken.replace(/-/g, '+').replace(/_/g, '/');
    const padded = b64 + '==='.slice(0, (4 - b64.length % 4) % 4);
    const decoded = decodeURIComponent(escape(atob(padded)));
    payload = JSON.parse(decoded);
  } catch {
    cleanImportTokenFromUrl();
    return;
  }
  if (!payload || !payload.t) {
    cleanImportTokenFromUrl();
    return;
  }

  // Si el token en el URL ya coincide con el guardado, no preguntamos —
  // strip silente. Caso típico: bookmark / home-screen shortcut con el
  // link de transfer queda abriéndose siempre con ?import_token=.
  if (loadGitHubToken() === payload.t) {
    cleanImportTokenFromUrl();
    return;
  }

  const tokenPreview = payload.t.length > 20
    ? payload.t.slice(0, 16) + '…' + payload.t.slice(-4)
    : payload.t;
  const ok = confirm(
    'Importar GitHub PAT desde el link?\n\n' +
    `Token: ${tokenPreview}\n` +
    `Device origen: ${payload.d || '(sin nombre)'}\n\n` +
    'Se va a guardar en este navegador (localStorage). Después se elimina el token de la URL.'
  );
  if (ok) {
    saveGitHubToken(payload.t);
    if (!loadDeviceName()) {
      const suggested = (payload.d ? payload.d + '-2' : '') || 'device-' + Math.floor(Math.random() * 100);
      const chosen = prompt('Nombre para este device (recomendado: distinguilo del origen):', suggested);
      if (chosen) saveDeviceName(chosen);
    }
    alert('✅ Token importado. Probá tareas y sync.');
    updateSyncStatus();
  }
  cleanImportTokenFromUrl();
}

function cleanImportTokenFromUrl() {
  const url = new URL(window.location.href);
  url.searchParams.delete('import_token');
  history.replaceState({}, '', url.toString());
}

handleTransferImport();

// ============================================================
// QR ENCODER — byte mode, EC level L, versions 1-10
// Implementación propia basada en ISO/IEC 18004:2015. Soporta hasta
// ~270 bytes de payload, suficiente para el link de transferencia.
// Sin dependencias externas. Output: SVG string.
// ============================================================
const QR_GF_EXP = new Array(512);
const QR_GF_LOG = new Array(256);
(function initQrGf() {
  let x = 1;
  for (let i = 0; i < 255; i++) {
    QR_GF_EXP[i] = x;
    QR_GF_LOG[x] = i;
    x <<= 1;
    if (x & 0x100) x ^= 0x11D;
  }
  for (let i = 255; i < 512; i++) QR_GF_EXP[i] = QR_GF_EXP[i - 255];
})();

function qrGfMul(a, b) {
  if (a === 0 || b === 0) return 0;
  return QR_GF_EXP[QR_GF_LOG[a] + QR_GF_LOG[b]];
}

function qrRsGen(degree) {
  let g = [1];
  for (let i = 0; i < degree; i++) {
    const next = new Array(g.length + 1).fill(0);
    for (let j = 0; j < g.length; j++) {
      next[j] ^= g[j];
      next[j + 1] ^= qrGfMul(g[j], QR_GF_EXP[i]);
    }
    g = next;
  }
  return g;
}

function qrRsEcc(data, eccLen) {
  const gen = qrRsGen(eccLen);
  const buf = data.concat(new Array(eccLen).fill(0));
  for (let i = 0; i < data.length; i++) {
    const f = buf[i];
    if (f === 0) continue;
    for (let j = 0; j < gen.length; j++) {
      buf[i + j] ^= qrGfMul(gen[j], f);
    }
  }
  return buf.slice(data.length);
}

// ISO/IEC 18004 Tabla 9 — level L, versiones 1..10.
const QR_PARAMS_L = [
  null,
  { ecPerBlock: 7,  blocks: [[1, 19]] },                    // v1
  { ecPerBlock: 10, blocks: [[1, 34]] },                    // v2
  { ecPerBlock: 15, blocks: [[1, 55]] },                    // v3
  { ecPerBlock: 20, blocks: [[1, 80]] },                    // v4
  { ecPerBlock: 26, blocks: [[1, 108]] },                   // v5
  { ecPerBlock: 18, blocks: [[2, 68]] },                    // v6
  { ecPerBlock: 20, blocks: [[2, 78]] },                    // v7
  { ecPerBlock: 24, blocks: [[2, 97]] },                    // v8
  { ecPerBlock: 30, blocks: [[2, 116]] },                   // v9
  { ecPerBlock: 18, blocks: [[2, 68], [2, 69]] },           // v10
];

const QR_ALIGN_CENTERS = [
  null, [], [6, 18], [6, 22], [6, 26], [6, 30],
  [6, 34], [6, 22, 38], [6, 24, 42], [6, 26, 46], [6, 28, 50],
];

function qrTotalDataCw(p) {
  return p.blocks.reduce((s, b) => s + b[0] * b[1], 0);
}

function qrPickVersion(byteLen) {
  for (let v = 1; v <= 10; v++) {
    const dc = qrTotalDataCw(QR_PARAMS_L[v]);
    const ccBits = v <= 9 ? 8 : 16;
    const cap = Math.floor((dc * 8 - 4 - ccBits) / 8);
    if (byteLen <= cap) return v;
  }
  throw new Error('texto muy largo (>270 bytes)');
}

function qrEncodeData(text) {
  const bytes = Array.from(new TextEncoder().encode(text));
  const version = qrPickVersion(bytes.length);
  const params = QR_PARAMS_L[version];
  const dc = qrTotalDataCw(params);

  // Construir bit stream.
  const bits = [];
  function pushBits(v, n) { for (let i = n - 1; i >= 0; i--) bits.push((v >> i) & 1); }
  pushBits(0b0100, 4);                          // mode indicator: byte
  pushBits(bytes.length, version <= 9 ? 8 : 16); // char count indicator
  for (const b of bytes) pushBits(b, 8);

  const totalBits = dc * 8;
  for (let i = 0; i < 4 && bits.length < totalBits; i++) bits.push(0); // terminador
  while (bits.length % 8 !== 0) bits.push(0);                          // pad a byte
  const padBytes = [0xEC, 0x11];
  let pi = 0;
  while (bits.length < totalBits) pushBits(padBytes[pi++ & 1], 8);     // pad codewords

  // Bits → bytes.
  const data = [];
  for (let i = 0; i < bits.length; i += 8) {
    let b = 0;
    for (let j = 0; j < 8; j++) b = (b << 1) | bits[i + j];
    data.push(b);
  }

  // Split en bloques + ECC.
  const blocks = [];
  const eccBlocks = [];
  let pos = 0;
  for (const [count, dpb] of params.blocks) {
    for (let k = 0; k < count; k++) {
      const blk = data.slice(pos, pos + dpb);
      pos += dpb;
      blocks.push(blk);
      eccBlocks.push(qrRsEcc(blk, params.ecPerBlock));
    }
  }

  // Interleave: data column-major, luego ECC column-major.
  const out = [];
  const maxData = Math.max(...blocks.map(b => b.length));
  for (let i = 0; i < maxData; i++) {
    for (const blk of blocks) if (i < blk.length) out.push(blk[i]);
  }
  for (let i = 0; i < params.ecPerBlock; i++) {
    for (const blk of eccBlocks) out.push(blk[i]);
  }

  return { version, codewords: out };
}

function qrSize(version) { return 17 + version * 4; }

// Determina si un módulo está reservado y su valor (si lo está). Construye
// la matriz con finder + timing + alignment + dark module + reserva format info.
function qrPlaceFunctionPatterns(version) {
  const N = qrSize(version);
  const m = Array.from({ length: N }, () => new Array(N).fill(null));
  const reserved = Array.from({ length: N }, () => new Array(N).fill(false));

  function placeFinder(r, c) {
    for (let i = -1; i <= 7; i++) {
      for (let j = -1; j <= 7; j++) {
        const rr = r + i, cc = c + j;
        if (rr < 0 || rr >= N || cc < 0 || cc >= N) continue;
        let v;
        if (i === -1 || i === 7 || j === -1 || j === 7) v = 0;
        else if (i === 0 || i === 6 || j === 0 || j === 6) v = 1;
        else if (i >= 2 && i <= 4 && j >= 2 && j <= 4) v = 1;
        else v = 0;
        m[rr][cc] = v;
        reserved[rr][cc] = true;
      }
    }
  }
  placeFinder(0, 0);
  placeFinder(0, N - 7);
  placeFinder(N - 7, 0);

  // Timing patterns.
  for (let i = 8; i < N - 8; i++) {
    if (m[6][i] === null) { m[6][i] = (i % 2 === 0) ? 1 : 0; reserved[6][i] = true; }
    if (m[i][6] === null) { m[i][6] = (i % 2 === 0) ? 1 : 0; reserved[i][6] = true; }
  }

  // Dark module (siempre 1).
  m[N - 8][8] = 1; reserved[N - 8][8] = true;

  // Reservar área de format info (15 módulos).
  for (let i = 0; i <= 8; i++) { reserved[8][i] = true; reserved[i][8] = true; }
  for (let i = 0; i < 8; i++) { reserved[8][N - 1 - i] = true; reserved[N - 1 - i][8] = true; }

  // Reservar área de version info (versión 7+): 6x3 arriba-derecha + 3x6 abajo-izquierda.
  if (version >= 7) {
    for (let i = 0; i < 18; i++) {
      const a = Math.floor(i / 3), b = i % 3;
      reserved[a][N - 11 + b] = true;
      reserved[N - 11 + b][a] = true;
    }
  }

  // Alignment patterns (versión 2+).
  const centers = QR_ALIGN_CENTERS[version];
  for (const r of centers) {
    for (const c of centers) {
      // Saltar overlap con finders (esquinas).
      if ((r < 8 && c < 8) || (r < 8 && c > N - 9) || (r > N - 9 && c < 8)) continue;
      for (let i = -2; i <= 2; i++) {
        for (let j = -2; j <= 2; j++) {
          const rr = r + i, cc = c + j;
          if (rr < 0 || rr >= N || cc < 0 || cc >= N) continue;
          const dist = Math.max(Math.abs(i), Math.abs(j));
          const v = (dist === 1) ? 0 : 1;
          m[rr][cc] = v;
          reserved[rr][cc] = true;
        }
      }
    }
  }

  return { matrix: m, reserved, size: N };
}

// Coloca codewords en zigzag empezando por la esquina inferior derecha.
function qrPlaceData(matrix, reserved, codewords) {
  const N = matrix.length;
  const totalBits = codewords.length * 8;
  let bitIdx = 0;
  let dir = -1; // -1 = sube, +1 = baja
  let col = N - 1;
  while (col > 0) {
    if (col === 6) col--;
    let row = (dir === -1) ? N - 1 : 0;
    while (row >= 0 && row < N) {
      for (let dx = 0; dx < 2; dx++) {
        const c = col - dx;
        const r = row;
        if (!reserved[r][c]) {
          let bit = 0;
          if (bitIdx < totalBits) {
            const byte = codewords[bitIdx >> 3];
            bit = (byte >> (7 - (bitIdx & 7))) & 1;
            bitIdx++;
          }
          matrix[r][c] = bit;
        }
      }
      row += dir;
    }
    dir = -dir;
    col -= 2;
  }
}

const QR_MASK_FNS = [
  (r, c) => (r + c) % 2 === 0,
  (r, c) => r % 2 === 0,
  (r, c) => c % 3 === 0,
  (r, c) => (r + c) % 3 === 0,
  (r, c) => (Math.floor(r / 2) + Math.floor(c / 3)) % 2 === 0,
  (r, c) => ((r * c) % 2 + (r * c) % 3) === 0,
  (r, c) => ((r * c) % 2 + (r * c) % 3) % 2 === 0,
  (r, c) => ((r + c) % 2 + (r * c) % 3) % 2 === 0,
];

function qrApplyMask(matrix, reserved, mask) {
  const fn = QR_MASK_FNS[mask];
  const N = matrix.length;
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (!reserved[r][c] && matrix[r][c] !== null) {
        if (fn(r, c)) matrix[r][c] ^= 1;
      }
    }
  }
}

// Format info: BCH(15,5) + máscara 0x5412. Level L = 01.
function qrFormatBits(level, mask) {
  const data = (level << 3) | mask;
  let r = data << 10;
  for (let i = 14; i >= 10; i--) {
    if ((r >> i) & 1) r ^= 0b10100110111 << (i - 10);
  }
  return ((data << 10) | r) ^ 0b101010000010010;
}

// Version info: BCH(18,6) sobre el número de versión. Solo aplica versión 7+.
function qrVersionInfoBits(version) {
  let v = version << 12;
  for (let i = 17; i >= 12; i--) {
    if ((v >> i) & 1) v ^= 0x1F25 << (i - 12);
  }
  return (version << 12) | (v & 0xFFF);
}

function qrPlaceVersionInfo(matrix, version) {
  if (version < 7) return;
  const N = matrix.length;
  const bits = qrVersionInfoBits(version);
  for (let i = 0; i < 18; i++) {
    const bit = (bits >> i) & 1;
    const a = Math.floor(i / 3), b = i % 3;
    matrix[a][N - 11 + b] = bit;          // top-right block (6 filas × 3 cols)
    matrix[N - 11 + b][a] = bit;          // bottom-left block (3 filas × 6 cols)
  }
}

function qrPlaceFormat(matrix, formatBits) {
  const N = matrix.length;
  // Posiciones top-left (15 módulos): bit 0 → (8,0), ..., bit 14 → (0,8).
  // Saltando timing en (6,8) y (8,6).
  const tl = [
    [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 7], [8, 8],
    [7, 8], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8],
  ];
  for (let i = 0; i < 15; i++) {
    const bit = (formatBits >> i) & 1;
    matrix[tl[i][0]][tl[i][1]] = bit;
  }
  // Top-right (bits 0..7) + bottom-left (bits 8..14).
  for (let i = 0; i < 8; i++) {
    matrix[8][N - 1 - i] = (formatBits >> i) & 1;
  }
  for (let i = 0; i < 7; i++) {
    matrix[N - 7 + i][8] = (formatBits >> (8 + i)) & 1;
  }
  // Re-marcar dark module (puede haber sido pisado).
  matrix[N - 8][8] = 1;
}

// Penalty score per ISO/IEC 18004 §7.8.3 — para elegir mejor máscara.
function qrPenalty(matrix) {
  const N = matrix.length;
  let p = 0;
  // 1) Runs ≥ 5 del mismo color.
  for (let r = 0; r < N; r++) {
    let run = 1, prev = matrix[r][0];
    for (let c = 1; c < N; c++) {
      if (matrix[r][c] === prev) { run++; if (run === 5) p += 3; else if (run > 5) p += 1; }
      else { run = 1; prev = matrix[r][c]; }
    }
  }
  for (let c = 0; c < N; c++) {
    let run = 1, prev = matrix[0][c];
    for (let r = 1; r < N; r++) {
      if (matrix[r][c] === prev) { run++; if (run === 5) p += 3; else if (run > 5) p += 1; }
      else { run = 1; prev = matrix[r][c]; }
    }
  }
  // 2) Bloques 2x2 mismo color.
  for (let r = 0; r < N - 1; r++) {
    for (let c = 0; c < N - 1; c++) {
      const v = matrix[r][c];
      if (v === matrix[r][c+1] && v === matrix[r+1][c] && v === matrix[r+1][c+1]) p += 3;
    }
  }
  // 3) Patrón finder-like (1011101 con 4 light a un lado) en filas/columnas.
  function check(line) {
    const target = [1,0,1,1,1,0,1];
    let count = 0;
    for (let i = 0; i <= line.length - 11; i++) {
      let match = true;
      for (let j = 0; j < 7; j++) if (line[i + 2 + j] !== target[j]) { match = false; break; }
      if (!match) continue;
      const left = i + 2 - 4;
      const right = i + 2 + 7 + 4 - 1;
      if (left >= 0 && line.slice(left, left + 4).every(x => x === 0)) count++;
      if (right < line.length && line.slice(i + 9, i + 13).every(x => x === 0)) count++;
    }
    return count;
  }
  for (let r = 0; r < N; r++) p += 40 * check(matrix[r]);
  for (let c = 0; c < N; c++) {
    const col = matrix.map(row => row[c]);
    p += 40 * check(col);
  }
  // 4) Balance dark/light.
  let dark = 0;
  for (let r = 0; r < N; r++) for (let c = 0; c < N; c++) if (matrix[r][c]) dark++;
  const ratio = (dark * 100) / (N * N);
  p += 10 * Math.floor(Math.abs(ratio - 50) / 5);
  return p;
}

function qrEncodeSvg(text, opts = {}) {
  const cellSize = opts.cellSize || 5;
  const margin = opts.margin == null ? 4 : opts.margin;
  const { version, codewords } = qrEncodeData(text);

  // Probar las 8 máscaras y elegir la de menor penalty.
  let best = null;
  for (let mask = 0; mask < 8; mask++) {
    const { matrix, reserved } = qrPlaceFunctionPatterns(version);
    qrPlaceData(matrix, reserved, codewords);
    qrApplyMask(matrix, reserved, mask);
    qrPlaceFormat(matrix, qrFormatBits(0b01, mask)); // L = 01
    qrPlaceVersionInfo(matrix, version);
    const score = qrPenalty(matrix);
    if (!best || score < best.score) best = { matrix, score };
  }

  const N = best.matrix.length;
  const total = N + margin * 2;
  const px = total * cellSize;
  let rects = '';
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (best.matrix[r][c] === 1) {
        const x = (c + margin) * cellSize;
        const y = (r + margin) * cellSize;
        rects += `<rect x="${x}" y="${y}" width="${cellSize}" height="${cellSize}"/>`;
      }
    }
  }
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${px}" height="${px}" viewBox="0 0 ${px} ${px}" shape-rendering="crispEdges"><rect width="${px}" height="${px}" fill="#ffffff"/><g fill="#000000">${rects}</g></svg>`;
}

// ============================================================
// GITHUB API CLIENT — read/write archivos en el repo
// ============================================================
const GH_REPO = 'abecedeefege/gardening';
const GH_API = `https://api.github.com/repos/${GH_REPO}/contents`;

async function ghGetFile(path) {
  const token = loadGitHubToken();
  if (!token) throw new Error('Sin GitHub PAT configurado');
  // cache: 'no-store' + ?_=timestamp para bypass del cache HTTP del browser
  // y de cualquier CDN intermedio. NO agregar Cache-Control header — GitHub
  // no lo permite en CORS preflight (no está en access-control-allow-headers)
  // y rompe el fetch con TypeError.
  const r = await fetch(`${GH_API}/${path}?ref=main&_=${Date.now()}`, {
    cache: 'no-store',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Accept': 'application/vnd.github+json',
    },
  });
  if (r.status === 404) return null;
  if (!r.ok) throw new Error(`GET ${path}: HTTP ${r.status}`);
  return await r.json();
}

async function ghPutFile(path, base64Content, message, sha = null) {
  const token = loadGitHubToken();
  if (!token) throw new Error('Sin GitHub PAT configurado');
  const body = { message, content: base64Content, branch: 'main' };
  if (sha) body.sha = sha;
  const r = await fetch(`${GH_API}/${path}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Accept': 'application/vnd.github+json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });
  if (!r.ok) {
    const txt = await r.text();
    throw new Error(`PUT ${path}: HTTP ${r.status} — ${txt.slice(0, 200)}`);
  }
  return await r.json();
}

// JSON de docs (uploads.json, sync/*.json) — fetch + merge + put.
async function ghReadJsonFile(path) {
  const meta = await ghGetFile(path);
  if (!meta) return { sha: null, data: null };
  // GitHub devuelve content base64 con saltos de línea.
  const decoded = atob(meta.content.replace(/\n/g, ''));
  // Decodificar UTF-8 desde la cadena ISO-Latin-1 que devuelve atob.
  const utf8 = decodeURIComponent(escape(decoded));
  return { sha: meta.sha, data: JSON.parse(utf8) };
}

async function ghWriteJsonFile(path, data, message) {
  // Encode UTF-8 → ISO Latin-1 → base64.
  const utf8 = unescape(encodeURIComponent(JSON.stringify(data, null, 2) + '\n'));
  const base64 = btoa(utf8);
  let sha = null;
  try {
    const existing = await ghReadJsonFile(path);
    sha = existing.sha;
  } catch (e) { /* si falla el read, intentamos crear */ }
  return await ghPutFile(path, base64, message, sha);
}

// ============================================================
// TASK PHOTO UPLOAD MODAL
// ============================================================
let pendingPhotoTask = null;
let pendingPhotoBlob = null;

const PRIVACY_SEEN_KEY = 'jardineando_privacy_seen_v1';

function ensurePrivacyAcknowledged() {
  if (localStorage.getItem(PRIVACY_SEEN_KEY) === '1') return true;
  const ok = confirm(
    'Recordatorio:\n\n' +
    '• La foto que subas se commitea al repo público de GitHub. Cualquiera con el link al sitio puede verla.\n' +
    '• El contenido del estado de tareas (sync) también es público.\n' +
    '• Tu GitHub PAT y nombre del device viven solo en este navegador (localStorage).\n\n' +
    '¿Continuamos?'
  );
  if (ok) localStorage.setItem(PRIVACY_SEEN_KEY, '1');
  return ok;
}

function openTaskPhotoModal(task) {
  pendingPhotoTask = task;
  pendingPhotoBlob = null;
  document.getElementById('task-photo-name').textContent = `📌 ${task.title} · ${task.plant_common} (${task.plant_codes.join(', ')})`;
  const ctx = document.getElementById('task-photo-context');
  if (ctx) ctx.value = '';

  // Mostrar la stage correcta según si hay token configurado.
  const hasToken = !!loadGitHubToken();
  if (hasToken && !ensurePrivacyAcknowledged()) return;
  setTaskPhotoStage(hasToken ? 'pick' : 'setup');
  document.getElementById('task-photo-modal').classList.add('active');
}

function setTaskPhotoStage(stage) {
  document.querySelectorAll('#task-photo-modal .task-photo-stage').forEach(s => {
    s.hidden = (s.dataset.stage !== stage);
  });
}

document.getElementById('btn-photo-go-settings').addEventListener('click', () => {
  closeModal('task-photo');
  openSettingsModal();
});

['task-photo-camera-input', 'task-photo-gallery-input'].forEach(id => {
  document.getElementById(id).addEventListener('change', async (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    e.target.value = '';  // permitir reseleccionar el mismo archivo después
    await loadAndPreviewPhoto(file);
  });
});

document.getElementById('btn-photo-change').addEventListener('click', () => {
  pendingPhotoBlob = null;
  setTaskPhotoStage('pick');
});

document.getElementById('btn-photo-upload').addEventListener('click', uploadPendingPhoto);

async function loadAndPreviewPhoto(file) {
  if (!pendingPhotoTask) return;
  try {
    const blob = await resizeAndStampImage(file, pendingPhotoTask, 1024, 0.85);
    pendingPhotoBlob = blob;
    // Mostrar preview en el canvas que ya está renderizado.
    const canvas = document.getElementById('task-photo-canvas');
    const url = URL.createObjectURL(blob);
    const img = new Image();
    img.onload = () => {
      canvas.width = img.width;
      canvas.height = img.height;
      canvas.getContext('2d').drawImage(img, 0, 0);
      URL.revokeObjectURL(url);
      setTaskPhotoStage('preview');
    };
    img.src = url;
  } catch (err) {
    setTaskPhotoStage('result');
    document.getElementById('task-photo-result').innerHTML = `
      <div class="task-photo-error">❌ Error procesando la foto: ${err.message}</div>
      <button class="btn-secondary" onclick="setTaskPhotoStage('pick')">↺ Reintentar</button>`;
  }
}

// Resize la imagen a maxSide px (lado mayor) y quema overlay con metadata
// de la tarea en la esquina inferior izquierda. Devuelve un Blob JPEG.
async function resizeAndStampImage(file, task, maxSide, quality) {
  // 1. Cargar imagen.
  const img = await new Promise((resolve, reject) => {
    const i = new Image();
    i.onload = () => resolve(i);
    i.onerror = () => reject(new Error('No se pudo leer la imagen'));
    i.src = URL.createObjectURL(file);
  });

  // 2. Calcular dimensiones.
  let { width, height } = img;
  if (width > maxSide || height > maxSide) {
    if (width >= height) {
      height = Math.round(height * (maxSide / width));
      width = maxSide;
    } else {
      width = Math.round(width * (maxSide / height));
      height = maxSide;
    }
  }

  // 3. Dibujar en canvas.
  const canvas = document.createElement('canvas');
  canvas.width = width;
  canvas.height = height;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img, 0, 0, width, height);
  URL.revokeObjectURL(img.src);

  // 4. Quemar overlay.
  drawTaskOverlay(ctx, width, height, task);

  // 5. Exportar a Blob.
  return await new Promise((resolve, reject) => {
    canvas.toBlob(b => b ? resolve(b) : reject(new Error('Falló toBlob')), 'image/jpeg', quality);
  });
}

function drawTaskOverlay(ctx, width, height, task) {
  // Banda semi-transparente abajo, ~12% del alto (mínimo 56px, máximo 84px).
  const bandH = Math.max(56, Math.min(84, Math.round(height * 0.12)));
  const padX = 14;
  const padY = 10;

  // Fondo de banda.
  ctx.fillStyle = 'rgba(0, 0, 0, 0.62)';
  ctx.fillRect(0, height - bandH, width, bandH);

  // Construir las 2 líneas.
  const now = new Date();
  const monthShort = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
  const dd = String(now.getDate()).padStart(2, '0');
  const mm = monthShort[now.getMonth()];
  const yy = String(now.getFullYear()).slice(-2);
  const hh = String(now.getHours()).padStart(2, '0');
  const mi = String(now.getMinutes()).padStart(2, '0');
  const line1 = `📌 ${task.id} · ${dd} ${mm} ${yy} · ${hh}:${mi}`;
  let line2 = task.title || '';
  if (line2.length > 55) line2 = line2.slice(0, 52) + '…';

  // Texto.
  const fontSize = Math.max(14, Math.min(20, Math.round(bandH * 0.30)));
  ctx.fillStyle = 'rgba(255, 255, 255, 0.96)';
  ctx.font = `600 ${fontSize}px -apple-system, "Segoe UI", Roboto, sans-serif`;
  ctx.textBaseline = 'top';
  ctx.fillText(line1, padX, height - bandH + padY);

  ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
  ctx.font = `400 ${fontSize - 2}px -apple-system, "Segoe UI", Roboto, sans-serif`;
  ctx.fillText(line2, padX, height - bandH + padY + fontSize + 4);
}

// Convierte Blob → base64 string sin prefijo "data:image/jpeg;base64,".
function blobToBase64(blob) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      const dataUrl = reader.result;
      resolve(dataUrl.split(',')[1]);
    };
    reader.onerror = () => reject(new Error('Error leyendo blob'));
    reader.readAsDataURL(blob);
  });
}

// ============================================================
// SPECIES DETAIL MODAL — click en plant-card abre detalle con galería
// ============================================================

// Cache del índice de uploads (docs/uploads.json) — fetch perezoso.
let _uploadsIndexCache = null;
let _uploadsIndexFetchedAt = 0;
async function loadUploadsIndex(forceRefresh = false) {
  const TTL_MS = 30 * 1000;  // 30s cache
  if (!forceRefresh && _uploadsIndexCache && Date.now() - _uploadsIndexFetchedAt < TTL_MS) {
    return _uploadsIndexCache;
  }
  try {
    const url = `uploads.json?_=${Date.now()}`;
    const r = await fetch(url, { cache: 'no-store' });
    if (!r.ok) { _uploadsIndexCache = {}; }
    else _uploadsIndexCache = await r.json();
  } catch {
    _uploadsIndexCache = {};
  }
  _uploadsIndexFetchedAt = Date.now();
  return _uploadsIndexCache;
}

// Encontrá la planta en PLANTS_INFO por id_code (cualquier elemento de id_codes).
function findPlantByCode(code) {
  if (typeof PLANTS_INFO === 'undefined') return null;
  return PLANTS_INFO.find(p => p.id_codes.includes(code));
}

// Tareas del Timeline filtradas por plant_code.
function tasksForPlant(code) {
  if (typeof TASKS === 'undefined') return [];
  return TASKS.filter(t => t.plant_codes.includes(code));
}

const MONTH_SHORT_ES = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
function fmtMonths(arr) {
  if (!arr || !arr.length) return '—';
  return arr.map(m => MONTH_SHORT_ES[m - 1] || '?').join(' · ');
}

let _currentSpeciesPlant = null;

async function openSpeciesDetailModal(plantCode) {
  const plant = findPlantByCode(plantCode);
  if (!plant) return;
  _currentSpeciesPlant = plant;
  const primaryCode = plant.id_codes[0];
  const idx = await loadUploadsIndex();
  const uploads = idx[primaryCode] || [];

  // Construir set de fotos: main + loc + uploads (más recientes primero).
  const photoCells = [];
  if (plant.main_photo && IMG[plant.main_photo]) {
    photoCells.push({ kind: 'main', src_data: IMG[plant.main_photo], filename: plant.main_photo, label: 'Foto principal' });
  }
  if (plant.loc_photo && IMG[plant.loc_photo] && plant.loc_photo !== plant.main_photo) {
    photoCells.push({ kind: 'loc', src_data: IMG[plant.loc_photo], filename: plant.loc_photo, label: 'Vista de ubicación' });
  }
  const sortedUploads = [...uploads].sort((a, b) => (b.uploaded_at || '').localeCompare(a.uploaded_at || ''));
  sortedUploads.forEach(u => {
    photoCells.push({
      kind: 'upload',
      src_url: `images/uploads/${primaryCode}/${u.filename}`,
      filename: u.filename,
      label: u.context === 'task' ? `Tarea: ${u.task_title_snapshot || u.task_id}` : (u.note || 'Foto del catálogo'),
      uploaded_at: u.uploaded_at,
      uploaded_by: u.uploaded_by,
      context: u.context,
    });
  });

  // Hero photo: prioridad main_photo (close-up de especie) > species upload >
  // loc_photo (vista de ubicación) > task upload. Esto pone la especie en
  // primer plano en vez de la zona donde vive.
  let heroSrc = null;
  if (plant.main_photo && IMG[plant.main_photo]) heroSrc = IMG[plant.main_photo];
  else {
    const firstSpecies = sortedUploads.find(u => u.context === 'species');
    if (firstSpecies) heroSrc = `images/uploads/${primaryCode}/${firstSpecies.filename}`;
    else if (plant.loc_photo && IMG[plant.loc_photo]) heroSrc = IMG[plant.loc_photo];
    else {
      const firstTask = sortedUploads.find(u => u.context === 'task');
      if (firstTask) heroSrc = `images/uploads/${primaryCode}/${firstTask.filename}`;
    }
  }

  // Photos grid (todas las fotos, sin tags overlaid — limpio).
  const photosGridHtml = photoCells.length ? photoCells.map((c, i) => {
    const src = c.src_data || c.src_url;
    const tooltip = c.kind === 'main' ? 'Principal'
                  : c.kind === 'loc' ? 'Ubicación'
                  : (c.uploaded_by ? `Subida (${c.uploaded_by})` : 'Subida')
                  + (c.uploaded_at ? ` · ${new Date(c.uploaded_at).toLocaleDateString('es-UY')}` : '');
    return `<div class="species-photo-cell" data-idx="${i}" title="${tooltip.replace(/"/g,'&quot;')}">
      <img src="${src}" alt="${c.label}" loading="lazy">
    </div>`;
  }).join('') : '';

  // Tareas + cuidados — todo en el <details> de "Detalles".
  const plantTasks = tasksForPlant(primaryCode);
  const tasksHtml = plantTasks.length ? `
    <div class="species-tasks">
      <h4>📋 Tareas del Timeline</h4>
      ${plantTasks.map(t => {
        const st = getTaskState(t.id);
        const cls = classifyTask(t);
        const stChip = cls === 'done'    ? '<span class="species-task-chip done">✅ Hecha</span>'
                    : cls === 'snoozed' ? '<span class="species-task-chip snoozed">😴 Pospuesta</span>'
                    : '<span class="species-task-chip active">📌 Activa</span>';
        return `<div class="species-task-row">
          ${stChip}
          <span class="species-task-title">${t.title}</span>
          <span class="species-task-when">${t.due_label || ''}</span>
        </div>`;
      }).join('')}
    </div>` : '';

  const careRows = [];
  if (plant.water) careRows.push({ icon: '💧', label: 'Riego', val: plant.water });
  if (plant.light) careRows.push({ icon: '☀️', label: 'Luz', val: plant.light });
  if (plant.prune_when) careRows.push({ icon: '✂️', label: 'Cuándo podar', val: plant.prune_when });
  if (plant.prune_how) careRows.push({ icon: '🛠️', label: 'Cómo podar', val: plant.prune_how });
  if (plant.flowering && plant.flowering.length) careRows.push({ icon: '🌸', label: 'Florece', val: fmtMonths(plant.flowering) });
  if (plant.fruiting && plant.fruiting.length) careRows.push({ icon: '🍎', label: 'Fructifica', val: fmtMonths(plant.fruiting) });
  if (plant.pruning && plant.pruning.length) careRows.push({ icon: '🗓️', label: 'Meses de poda', val: fmtMonths(plant.pruning) });
  const careHtml = careRows.length ? `
    <div class="species-care">
      ${careRows.map(r => `<div class="species-care-row">
        <span class="species-care-icon">${r.icon}</span>
        <span class="species-care-label">${r.label}</span>
        <span class="species-care-val">${r.val}</span>
      </div>`).join('')}
    </div>` : '';

  const charruaHtml = plant.charrua ? `<div class="species-charrua">🪶 <strong>Originario:</strong> ${plant.charrua}</div>` : '';
  const funFactHtml = plant.fun_fact && plant.fun_fact !== '—' ? `<div class="species-funfact">💡 <em>${plant.fun_fact}</em></div>` : '';
  const tagsHtml = (plant.tags || []).map(t => `<span class="species-tag-chip">${t}</span>`).join('');

  // Ubicación: zone capitalizada + primera oración del desc + tags.
  const zoneLabel = (plant.zone || '').replace(/^\w/, c => c.toUpperCase());
  // Extraer 1ra oración del desc — usualmente trae info de ubicación.
  const firstSentence = (plant.desc || '').split(/(?<=\.)\s/)[0] || '';
  const locationLine = firstSentence.length > 0 && firstSentence.length < 240 ? firstSentence : '';

  const photoCount = photoCells.length;

  document.getElementById('species-detail-body').innerHTML = `
    <div class="species-hero ${heroSrc ? '' : 'species-hero-fallback'}"
         ${heroSrc ? `style="background-image:url('${heroSrc.replace(/'/g, "%27")}')"` : ''}>
      <button class="species-hero-close" data-action="close-species" aria-label="Cerrar">✕</button>
      <div class="species-hero-overlay">
        <h2 class="species-hero-name">${plant.common}</h2>
        ${plant.sci ? `<div class="species-hero-sci">${plant.sci}</div>` : ''}
        <div class="species-hero-meta">
          <span class="species-hero-chip">${plant.id_codes.join(', ')}</span>
          <span class="species-hero-chip">${zoneLabel}</span>
        </div>
        ${locationLine ? `<p class="species-hero-location">📍 ${locationLine}</p>` : ''}
        ${tagsHtml ? `<div class="species-hero-tags">${tagsHtml}</div>` : ''}
      </div>
    </div>

    <div class="species-actions">
      <button class="species-action-btn" data-action="ask-question" type="button">❓ Hacer pregunta</button>
      <button class="species-action-btn" data-action="add-task" type="button">➕ Agregar tarea</button>
    </div>

    <div class="species-section-photos">
      <div class="species-section-label">📷 Fotos${photoCount ? ` · ${photoCount}` : ''}</div>
      <div class="species-photos-grid" id="species-photos-grid">
        ${photosGridHtml}
        <div class="species-photo-cell add" data-action="add-species-photo" title="Sumar foto al catálogo">
          <span class="species-add-plus">+</span>
          <span class="species-add-label">Sumar foto</span>
        </div>
      </div>
    </div>

    <details class="species-details">
      <summary class="species-details-summary">Detalles</summary>
      <div class="species-details-body">
        ${charruaHtml}
        ${plant.desc ? `<p class="species-desc">${plant.desc}</p>` : ''}
        ${plant.other_names ? `<div class="species-detail-other">↳ ${plant.other_names}</div>` : ''}
        ${funFactHtml}
        ${careHtml}
        ${tasksHtml}
      </div>
    </details>
  `;

  // Bind clicks: close hero / thumbnails → lightbox / "+" → upload.
  const body = document.getElementById('species-detail-body');
  body.querySelector('[data-action="close-species"]')?.addEventListener('click', () => closeModal('species-detail'));
  const grid = document.getElementById('species-photos-grid');
  grid.querySelectorAll('.species-photo-cell:not(.add)').forEach(cell => {
    cell.addEventListener('click', () => {
      const img = cell.querySelector('img');
      if (img && img.src) openLightboxWithUrl(img.src);
    });
  });
  grid.querySelector('[data-action="add-species-photo"]')?.addEventListener('click', () => {
    closeModal('species-detail');
    openSpeciesPhotoModal(plant);
  });
  body.querySelector('[data-action="ask-question"]')?.addEventListener('click', () => {
    closeModal('species-detail');
    openTaskComposeModal({ mode: 'question', plantCode: plant.id_codes[0] });
  });
  body.querySelector('[data-action="add-task"]')?.addEventListener('click', () => {
    closeModal('species-detail');
    openTaskComposeModal({ mode: 'user_task', plantCode: plant.id_codes[0] });
  });

  document.getElementById('species-detail-modal').classList.add('active');
}

// Abrir lightbox con un URL (en lugar de un nombre de archivo en IMG).
function openLightboxWithUrl(url) {
  const img = document.getElementById('lightbox-img');
  const lb = document.getElementById('lightbox');
  if (!img || !lb) return;
  img.src = url;
  lb.classList.add('active');
}

// Bind click en TODAS las plant-card (todos los tabs Frente/Fondo/Interior/Todos).
document.querySelectorAll('.plant-card').forEach(card => {
  card.addEventListener('click', (e) => {
    if (e.target.closest('a, button')) return;  // dejar que links/botones internos sigan funcionando
    const code = card.dataset.plantId?.split(',')[0]?.trim();
    if (code) openSpeciesDetailModal(code);
  });
  card.style.cursor = 'pointer';
});

// ============================================================
// SPECIES PHOTO UPLOAD — sumar foto al catálogo (sin AI eval)
// ============================================================
let pendingSpeciesPhotoBlob = null;
let pendingSpeciesPhotoPlant = null;

function openSpeciesPhotoModal(plant) {
  pendingSpeciesPhotoPlant = plant;
  pendingSpeciesPhotoBlob = null;
  document.getElementById('species-photo-name').textContent = `🌿 ${plant.common} (${plant.id_codes.join(', ')})`;
  document.getElementById('species-photo-note').value = '';
  const hasToken = !!loadGitHubToken();
  if (hasToken && !ensurePrivacyAcknowledged()) return;
  setSpeciesPhotoStage(hasToken ? 'pick' : 'setup');
  document.getElementById('species-photo-modal').classList.add('active');
}

function setSpeciesPhotoStage(stage) {
  document.querySelectorAll('#species-photo-modal .task-photo-stage').forEach(s => {
    s.hidden = (s.dataset.stage !== stage);
  });
}

document.getElementById('btn-species-photo-go-settings').addEventListener('click', () => {
  closeModal('species-photo');
  openSettingsModal();
});

['species-photo-camera-input', 'species-photo-gallery-input'].forEach(id => {
  document.getElementById(id).addEventListener('change', async (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    e.target.value = '';
    await loadAndPreviewSpeciesPhoto(file);
  });
});

document.getElementById('btn-species-photo-change').addEventListener('click', () => {
  pendingSpeciesPhotoBlob = null;
  setSpeciesPhotoStage('pick');
});

document.getElementById('btn-species-photo-upload').addEventListener('click', uploadPendingSpeciesPhoto);

async function loadAndPreviewSpeciesPhoto(file) {
  if (!pendingSpeciesPhotoPlant) return;
  try {
    // Sin overlay para fotos de especie — son del catálogo.
    const blob = await resizeImageNoOverlay(file, 1024, 0.85);
    pendingSpeciesPhotoBlob = blob;
    const canvas = document.getElementById('species-photo-canvas');
    const url = URL.createObjectURL(blob);
    const img = new Image();
    img.onload = () => {
      canvas.width = img.width;
      canvas.height = img.height;
      canvas.getContext('2d').drawImage(img, 0, 0);
      URL.revokeObjectURL(url);
      setSpeciesPhotoStage('preview');
    };
    img.src = url;
  } catch (err) {
    setSpeciesPhotoStage('result');
    document.getElementById('species-photo-result').innerHTML = `
      <div class="task-photo-error">❌ Error procesando la foto: ${err.message}</div>
      <button class="btn-secondary" onclick="setSpeciesPhotoStage('pick')">↺ Reintentar</button>`;
  }
}

async function resizeImageNoOverlay(file, maxSide, quality) {
  const img = await new Promise((resolve, reject) => {
    const i = new Image();
    i.onload = () => resolve(i);
    i.onerror = () => reject(new Error('No se pudo leer la imagen'));
    i.src = URL.createObjectURL(file);
  });
  let { width, height } = img;
  if (width > maxSide || height > maxSide) {
    if (width >= height) { height = Math.round(height * (maxSide / width)); width = maxSide; }
    else { width = Math.round(width * (maxSide / height)); height = maxSide; }
  }
  const canvas = document.createElement('canvas');
  canvas.width = width; canvas.height = height;
  canvas.getContext('2d').drawImage(img, 0, 0, width, height);
  URL.revokeObjectURL(img.src);
  return await new Promise((resolve, reject) => {
    canvas.toBlob(b => b ? resolve(b) : reject(new Error('Falló toBlob')), 'image/jpeg', quality);
  });
}

async function uploadPendingSpeciesPhoto() {
  if (!pendingSpeciesPhotoBlob || !pendingSpeciesPhotoPlant) return;
  setSpeciesPhotoStage('result');
  const result = document.getElementById('species-photo-result');
  result.innerHTML = `<div class="task-photo-uploading">⏳ Subiendo foto al catálogo…</div>`;
  try {
    const plant = pendingSpeciesPhotoPlant;
    const plantId = plant.id_codes[0];
    const note = document.getElementById('species-photo-note').value.trim();
    const now = new Date();
    const stamp = now.toISOString().replace(/[-:]/g, '').replace(/\..+/, '').replace('T', '-').slice(0, 15);
    const filename = `species-${plantId}_${stamp}.jpg`;
    const path = `docs/images/uploads/${plantId}/${filename}`;
    const base64 = await blobToBase64(pendingSpeciesPhotoBlob);

    await ghPutFile(path, base64, `upload: foto al catálogo de ${plantId} (${plant.common})`);

    const uploadsPath = 'docs/uploads.json';
    const { sha, data } = await ghReadJsonFile(uploadsPath);
    const idx = data || {};
    if (!idx[plantId]) idx[plantId] = [];
    const entry = {
      filename,
      uploaded_at: now.toISOString(),
      uploaded_by: loadDeviceName() || 'desconocido',
      context: 'species',
      ai_status: 'n/a',
    };
    if (note) entry.note = note;
    idx[plantId].push(entry);
    const newJson = JSON.stringify(idx, null, 2) + '\n';
    const newBase64 = btoa(unescape(encodeURIComponent(newJson)));
    await ghPutFile(uploadsPath, newBase64, `upload: registrar ${filename} en uploads.json (especie)`, sha);

    // Invalidar cache para que el modal de detalle muestre la nueva foto al reabrir.
    _uploadsIndexCache = null;

    const fileUrl = `https://github.com/${GH_REPO}/blob/main/${path}`;
    result.innerHTML = `
      <div class="task-photo-success">
        <div class="task-photo-success-title">✅ Foto agregada al catálogo</div>
        <p>Quedó visible en la galería de <strong>${plant.common}</strong>.</p>
        <p class="task-photo-success-link">
          <a href="${fileUrl}" target="_blank" rel="noopener">Ver foto en GitHub →</a>
        </p>
      </div>
      <button class="btn-primary" onclick="closeModal('species-photo')">Listo</button>`;
  } catch (err) {
    const msg = err.message || String(err);
    const isType = err.name === 'TypeError';
    const detail = isType
      ? `<p>Probable causa: CORS preflight rechazado, network error, o Service Worker viejo. Probá "Resetear SW" en ⚙️ Configuración y recargar.</p><p style="font-size:0.78rem;color:#666">Detalle técnico: ${msg}</p>`
      : `<p>${msg}</p>`;
    result.innerHTML = `
      <div class="task-photo-error">
        <div class="task-photo-error-title">❌ No se pudo subir</div>
        ${detail}
      </div>
      <div class="task-photo-actions">
        <button class="btn-secondary" onclick="setSpeciesPhotoStage('preview')">↺ Volver al preview</button>
        <button class="btn-secondary" onclick="closeModal('species-photo')">Cancelar</button>
      </div>`;
  }
}

// ============================================================
// SYNC ENGINE — read on load + write debounced al repo
// ============================================================
let _stateDirty = false;
let _syncFlushTimer = null;
let _syncInProgress = false;
const SYNC_DEBOUNCE_MS = 5000;
const SYNC_PATH = 'docs/sync/task_states.json';

function markStateDirty() {
  _stateDirty = true;
  scheduleSyncFlush();
  updateSyncStatus();
}

function scheduleSyncFlush() {
  if (!loadGitHubToken()) return;  // sin token, no hay sync write
  if (_syncFlushTimer) clearTimeout(_syncFlushTimer);
  _syncFlushTimer = setTimeout(flushSync, SYNC_DEBOUNCE_MS);
}

async function flushSync(retries = 5) {
  if (_syncInProgress) return;
  if (!loadGitHubToken()) return;
  if (!_stateDirty) return;
  _syncInProgress = true;
  updateSyncStatus();
  try {
    // 1. Leer remoto (cache: no-store via ghGetFile).
    const { sha, data } = await ghReadJsonFile(SYNC_PATH);
    const remoteTasks = (data && data.tasks) || {};

    // 2. Mergear con local — gana el last_modified_at más reciente.
    const local = loadStates();
    const merged = { ...remoteTasks };
    Object.entries(local).forEach(([taskId, localState]) => {
      const remoteState = remoteTasks[taskId];
      const localTs = localState?.last_modified_at || '0';
      const remoteTs = remoteState?.last_modified_at || '0';
      if (localTs >= remoteTs) merged[taskId] = localState;
    });

    // 3. Construir nuevo JSON y escribir.
    const payload = {
      _synced_at: new Date().toISOString(),
      _last_writer: loadDeviceName() || 'browser',
      tasks: merged,
    };
    const json = JSON.stringify(payload, null, 2) + '\n';
    const base64 = btoa(unescape(encodeURIComponent(json)));
    await ghPutFile(SYNC_PATH, base64, `sync: actualizar task_states desde ${loadDeviceName() || 'browser'}`, sha);

    // 4. Reemplazar local con merged (ahora todos tienen last_modified_at acordado).
    saveStates(merged);
    _stateDirty = false;
    updateSyncStatus({ ok: true });
  } catch (err) {
    console.warn(`Sync flush falló (retries restantes: ${retries}):`, err);
    if (retries > 0 && /409|412|5\d\d/.test(String(err.message))) {
      // Conflict (409/412) o error transitorio del servidor (5xx) — backoff
      // exponencial y reintentar. 600ms, 1.2s, 2.4s, 4.8s, 9.6s.
      const delay = 600 * Math.pow(2, 5 - retries);
      await new Promise(r => setTimeout(r, delay));
      _syncInProgress = false;
      return flushSync(retries - 1);
    }
    updateSyncStatus({ error: err.message });
  } finally {
    _syncInProgress = false;
  }
}

function updateSyncStatus(opts = {}) {
  const bar = document.getElementById('sync-status-bar');
  const label = document.getElementById('sync-label');
  const retryBtn = document.getElementById('sync-retry-btn');
  if (!bar) return;
  const hasToken = !!loadGitHubToken();

  if (!hasToken) {
    bar.dataset.state = 'disabled';
    label.textContent = 'Sync deshabilitado · configurá tu GitHub PAT en ⚙️';
    retryBtn.hidden = true;
    bar.hidden = false;
    return;
  }
  if (_syncInProgress) {
    bar.dataset.state = 'syncing';
    label.textContent = 'Sincronizando…';
    retryBtn.hidden = true;
    bar.hidden = false;
    return;
  }
  if (opts.error) {
    bar.dataset.state = 'error';
    label.textContent = `Error de sync: ${opts.error.slice(0, 80)}`;
    retryBtn.hidden = false;
    bar.hidden = false;
    return;
  }
  if (_stateDirty) {
    bar.dataset.state = 'pending';
    label.textContent = 'Sync pendiente · se subirá en unos segundos';
    retryBtn.hidden = false;
    bar.hidden = false;
    return;
  }
  // Sin pendientes → ocultar la barra para no hacer ruido visual.
  bar.dataset.state = 'ok';
  bar.hidden = true;
}

// Flush al perder foco / cerrar pestaña.
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden' && _stateDirty) {
    flushSync();
  }
});
window.addEventListener('beforeunload', () => {
  if (_stateDirty) {
    // Best-effort — sendBeacon no sirve para PUT con auth; intentamos fetch sin await.
    flushSync();
  }
});

// Botón "Reintentar" en la status bar.
document.getElementById('sync-retry-btn')?.addEventListener('click', () => flushSync());

// Update inicial de la status bar (puede que ya haya cambios pending desde una sesión vieja).
updateSyncStatus();

// Fetch público del task_states.json del repo (no necesita auth — repo público).
async function fetchRemoteTaskStates() {
  // Se referencia con path relativo así sirve también localmente con file://, vía dev server, o GH Pages.
  // En GH Pages: docs/index.html → docs/sync/task_states.json es '../sync/task_states.json' a partir
  // de la URL, pero como el sitio es servido desde docs/ como raíz, el path es 'sync/task_states.json'.
  try {
    const url = `sync/task_states.json?_=${Date.now()}`;  // bust cache
    const r = await fetch(url, { cache: 'no-store' });
    if (!r.ok) return null;
    return await r.json();
  } catch {
    return null;
  }
}

// Merge per-task: gana el last_modified_at más reciente.
function mergeRemoteIntoLocal(remote) {
  if (!remote || !remote.tasks) return { merged: 0, skipped: 0 };
  const local = loadStates();
  let merged = 0;
  let skipped = 0;
  Object.entries(remote.tasks).forEach(([taskId, remoteState]) => {
    const localState = local[taskId];
    const localTs = localState?.last_modified_at || '0';
    const remoteTs = remoteState?.last_modified_at || '0';
    if (remoteTs > localTs) {
      local[taskId] = remoteState;
      merged++;
    } else {
      skipped++;
    }
  });
  saveStates(local);
  return { merged, skipped };
}

async function syncReadFromRepo() {
  const remote = await fetchRemoteTaskStates();
  if (!remote) return;
  const { merged } = mergeRemoteIntoLocal(remote);
  if (merged > 0 && typeof renderTimeline === 'function') {
    // Si estamos viendo el timeline, refrescar el render para que aparezcan los cambios.
    renderTimeline();
  }
}

// Disparar al cargar la página y al recuperar foco (vuelve a la pestaña).
syncReadFromRepo();
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible') syncReadFromRepo();
});

async function uploadPendingPhoto() {
  if (!pendingPhotoBlob || !pendingPhotoTask) return;
  setTaskPhotoStage('result');
  const result = document.getElementById('task-photo-result');
  result.innerHTML = `<div class="task-photo-uploading">⏳ Subiendo foto al repo…</div>`;

  try {
    const task = pendingPhotoTask;
    const plantId = task.plant_codes[0];
    const now = new Date();
    const stamp = now.toISOString().replace(/[-:]/g, '').replace(/\..+/, '').replace('T', '-').slice(0, 15);
    const filename = `${task.id}_${stamp}.jpg`;
    const path = `docs/images/uploads/${plantId}/${filename}`;
    const base64 = await blobToBase64(pendingPhotoBlob);

    // 1. Push de la imagen al repo.
    await ghPutFile(path, base64, `upload: foto para ${task.id}`);

    // 2. Append entry a docs/uploads.json.
    const uploadsPath = 'docs/uploads.json';
    const { sha, data } = await ghReadJsonFile(uploadsPath);
    const idx = data || {};
    if (!idx[plantId]) idx[plantId] = [];
    const userContext = (document.getElementById('task-photo-context')?.value || '').trim();
    const entry = {
      filename,
      uploaded_at: now.toISOString(),
      uploaded_by: loadDeviceName() || 'desconocido',
      context: 'task',
      task_id: task.id,
      task_title_snapshot: task.title,
      ai_status: 'pending',
      ai_evaluation: null,
    };
    if (userContext) entry.user_context = userContext;
    idx[plantId].push(entry);
    const newJson = JSON.stringify(idx, null, 2) + '\n';
    const newBase64 = btoa(unescape(encodeURIComponent(newJson)));
    await ghPutFile(uploadsPath, newBase64, `upload: registrar ${filename} en uploads.json`, sha);

    // 3. Mostrar éxito.
    const fileUrl = `https://github.com/${GH_REPO}/blob/main/${path}`;
    result.innerHTML = `
      <div class="task-photo-success">
        <div class="task-photo-success-title">✅ Foto subida al repo</div>
        <p>Quedó registrada como <strong>pending</strong>.</p>
        <p class="task-photo-success-hint">
          Para evaluarla y actualizar la tarea, abrí Claude Code en este repo y corré:
        </p>
        <code class="task-photo-success-cmd">/actualizar-tareas</code>
        <p class="task-photo-success-link">
          <a href="${fileUrl}" target="_blank" rel="noopener">Ver foto en GitHub →</a>
        </p>
      </div>
      <button class="btn-primary" onclick="closeModal('task-photo')">Listo</button>`;
  } catch (err) {
    const msg = err.message || String(err);
    const isType = err.name === 'TypeError';
    const detail = isType
      ? `<p>Probable causa: CORS preflight rechazado, network error, o Service Worker viejo. Probá "Resetear SW" en ⚙️ Configuración y recargar.</p><p style="font-size:0.78rem;color:#666">Detalle técnico: ${msg}</p>`
      : `<p>${msg}</p>`;
    result.innerHTML = `
      <div class="task-photo-error">
        <div class="task-photo-error-title">❌ No se pudo subir</div>
        ${detail}
      </div>
      <div class="task-photo-actions">
        <button class="btn-secondary" onclick="setTaskPhotoStage('preview')">↺ Volver al preview</button>
        <button class="btn-secondary" onclick="closeModal('task-photo')">Cancelar</button>
      </div>`;
  }
}

// ============================================================
// TASK TEXT RESPONSE MODAL — responder con texto, sin foto
// ============================================================
let pendingTextTask = null;

function openTaskTextModal(task) {
  pendingTextTask = task;
  document.getElementById('task-text-name').textContent = `📌 ${task.title} · ${task.plant_common} (${task.plant_codes.join(', ')})`;
  document.getElementById('task-text-content').value = '';
  const hasToken = !!loadGitHubToken();
  if (hasToken && !ensurePrivacyAcknowledged()) return;
  setTaskTextStage(hasToken ? 'write' : 'setup');
  document.getElementById('task-text-modal').classList.add('active');
}

function setTaskTextStage(stage) {
  document.querySelectorAll('#task-text-modal .task-photo-stage').forEach(s => {
    s.hidden = (s.dataset.stage !== stage);
  });
}

document.getElementById('btn-text-go-settings')?.addEventListener('click', () => {
  closeModal('task-text');
  openSettingsModal();
});

// "Marcar hecha con esta nota" — sin AI eval, solo guarda nota como respuesta directa
// del usuario en sync/task_states.json (campo user_note) y marca done.
document.getElementById('btn-text-mark-done')?.addEventListener('click', async () => {
  if (!pendingTextTask) return;
  const text = document.getElementById('task-text-content').value.trim();
  if (!text) {
    alert('Escribí una nota primero.');
    return;
  }
  setTaskTextStage('result');
  const result = document.getElementById('task-text-result');
  result.innerHTML = `<div class="task-photo-uploading">⏳ Marcando hecha con tu nota…</div>`;
  try {
    setTaskState(pendingTextTask.id, {
      status: 'done',
      snoozed_until: null,
      completed_at: new Date().toISOString(),
      user_note: text,
    });
    renderTimeline();
    result.innerHTML = `
      <div class="task-photo-success">
        <div class="task-photo-success-title">✅ Tarea marcada hecha</div>
        <p>Tu nota: <em>${text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}</em></p>
      </div>
      <button class="btn-primary" onclick="closeModal('task-text')">Listo</button>`;
  } catch (err) {
    result.innerHTML = `<div class="task-photo-error">❌ ${err.message}</div>
      <button class="btn-secondary" onclick="setTaskTextStage('write')">↺ Volver</button>`;
  }
});

// "Subir nota + pedir evaluación IA" — pushea entry text-only a uploads.json
// con context="task_text", ai_status="pending". /actualizar-tareas la procesa.
document.getElementById('btn-text-ask-ai')?.addEventListener('click', async () => {
  if (!pendingTextTask) return;
  const text = document.getElementById('task-text-content').value.trim();
  if (!text) {
    alert('Escribí algo primero.');
    return;
  }
  setTaskTextStage('result');
  const result = document.getElementById('task-text-result');
  result.innerHTML = `<div class="task-photo-uploading">⏳ Subiendo tu nota al repo…</div>`;
  try {
    const task = pendingTextTask;
    const plantId = task.plant_codes[0];
    const now = new Date();
    const stamp = now.toISOString().replace(/[-:]/g, '').replace(/\..+/, '').replace('T', '-').slice(0, 15);
    const entry = {
      filename: null,
      uploaded_at: now.toISOString(),
      uploaded_by: loadDeviceName() || 'desconocido',
      context: 'task_text',
      task_id: task.id,
      task_title_snapshot: task.title,
      user_context: text,
      ai_status: 'pending',
      ai_evaluation: null,
      _stamp: stamp,
    };
    const uploadsPath = 'docs/uploads.json';
    const { sha, data } = await ghReadJsonFile(uploadsPath);
    const idx = data || {};
    if (!idx[plantId]) idx[plantId] = [];
    idx[plantId].push(entry);
    const newJson = JSON.stringify(idx, null, 2) + '\n';
    const newBase64 = btoa(unescape(encodeURIComponent(newJson)));
    await ghPutFile(uploadsPath, newBase64, `text-note: respuesta de texto para ${task.id}`, sha);
    result.innerHTML = `
      <div class="task-photo-success">
        <div class="task-photo-success-title">✅ Nota subida</div>
        <p>Quedó registrada como <strong>pending</strong> de evaluación IA.</p>
        <p class="task-photo-success-hint">Para que se procese, abrí Claude Code y corré:</p>
        <code class="task-photo-success-cmd">/actualizar-tareas</code>
      </div>
      <button class="btn-primary" onclick="closeModal('task-text')">Listo</button>`;
  } catch (err) {
    result.innerHTML = `<div class="task-photo-error">❌ ${err.message}</div>
      <div class="task-photo-actions">
        <button class="btn-secondary" onclick="setTaskTextStage('write')">↺ Volver</button>
        <button class="btn-secondary" onclick="closeModal('task-text')">Cancelar</button>
      </div>`;
  }
});

// ============================================================
// USER TASKS — tareas y preguntas creadas desde la app
// Persistidas en docs/sync/user_tasks.json (sincronizado entre devices)
// y cacheadas en localStorage para render inmediato.
// (declaraciones de USER_TASKS_KEY / USER_TASKS_PATH / USER_TASKS están más
// arriba, en el bloque de state management, para evitar TDZ con renderTimeline).
// ============================================================

function loadUserTasksLocal() {
  try {
    const raw = localStorage.getItem(USER_TASKS_KEY);
    if (raw) USER_TASKS = JSON.parse(raw);
  } catch { USER_TASKS = {}; }
  return USER_TASKS;
}
function saveUserTasksLocal() {
  localStorage.setItem(USER_TASKS_KEY, JSON.stringify(USER_TASKS));
}
loadUserTasksLocal();

// Fetch público de user_tasks.json (igual que task_states.json — público).
async function fetchRemoteUserTasks() {
  try {
    const url = `sync/user_tasks.json?_=${Date.now()}`;
    const r = await fetch(url, { cache: 'no-store' });
    if (!r.ok) return null;
    return await r.json();
  } catch { return null; }
}

function mergeRemoteUserTasks(remote) {
  if (!remote || !remote.tasks) return 0;
  let changed = 0;
  Object.entries(remote.tasks).forEach(([id, ut]) => {
    const localUt = USER_TASKS[id];
    const localTs = localUt?.last_modified_at || localUt?.created_at || '0';
    const remoteTs = ut.last_modified_at || ut.created_at || '0';
    if (remoteTs > localTs) {
      USER_TASKS[id] = ut;
      changed++;
    }
  });
  // Si remote no tiene un id que sí está local, mantenemos el local (será pusheado en próxima escritura).
  if (changed > 0) saveUserTasksLocal();
  return changed;
}

async function syncReadUserTasks() {
  const remote = await fetchRemoteUserTasks();
  if (!remote) return;
  const changed = mergeRemoteUserTasks(remote);
  if (changed > 0 && typeof renderTimeline === 'function') renderTimeline();
}
syncReadUserTasks();
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible') syncReadUserTasks();
});

// Push de user_tasks.json al repo (full snapshot, last-write-wins por id).
async function flushUserTasksToRepo(retries = 3) {
  if (!loadGitHubToken()) return;
  try {
    const { sha, data } = await ghReadJsonFile(USER_TASKS_PATH);
    const remoteTasks = (data && data.tasks) || {};
    const merged = { ...remoteTasks };
    Object.entries(USER_TASKS).forEach(([id, localUt]) => {
      const remoteUt = remoteTasks[id];
      const localTs = localUt?.last_modified_at || localUt?.created_at || '0';
      const remoteTs = remoteUt?.last_modified_at || remoteUt?.created_at || '0';
      if (localTs >= remoteTs) merged[id] = localUt;
    });
    const payload = {
      _synced_at: new Date().toISOString(),
      _last_writer: loadDeviceName() || 'browser',
      tasks: merged,
    };
    const json = JSON.stringify(payload, null, 2) + '\n';
    const base64 = btoa(unescape(encodeURIComponent(json)));
    await ghPutFile(USER_TASKS_PATH, base64, `user-tasks: actualizar desde ${loadDeviceName() || 'browser'}`, sha);
    USER_TASKS = merged;
    saveUserTasksLocal();
  } catch (err) {
    if (retries > 0 && /409|412|5\d\d/.test(String(err.message))) {
      const delay = 600 * Math.pow(2, 3 - retries);
      await new Promise(r => setTimeout(r, delay));
      return flushUserTasksToRepo(retries - 1);
    }
    console.warn('user_tasks flush falló:', err);
    throw err;
  }
}

// ============================================================
// TASK-COMPOSE MODAL — crear tarea propia o hacer pregunta
// Se invoca desde el botón "+ Nueva tarea" del Timeline o desde
// los botones "❓ Hacer pregunta" / "➕ Agregar tarea" del species modal.
// ============================================================
let composeState = { mode: null, plantCode: null, blob: null };

function openTaskComposeModal({ mode, plantCode } = {}) {
  composeState = { mode: mode || 'user_task', plantCode: plantCode || null, blob: null };

  const titleEl = document.getElementById('task-compose-title');
  const ctxEl = document.getElementById('task-compose-context');
  const titleLabel = document.getElementById('compose-title-label');
  const titleInput = document.getElementById('compose-title');
  const textLabel = document.getElementById('compose-text-label');
  const textHint = document.getElementById('compose-text-hint');
  const textArea = document.getElementById('compose-text');
  const submitBtn = document.getElementById('btn-compose-submit');
  const plantRow = document.getElementById('compose-plant-row');
  const plantSelect = document.getElementById('compose-plant-select');
  const previewWrap = document.getElementById('compose-photo-preview-wrap');
  const photoPick = document.getElementById('compose-photo-pick');

  // Reset
  titleInput.value = '';
  textArea.value = '';
  if (previewWrap) previewWrap.hidden = true;
  if (photoPick) photoPick.hidden = false;

  // Buscar la planta si hay plantCode
  let plantInfo = null;
  if (plantCode && typeof PLANTS_INFO !== 'undefined') {
    plantInfo = PLANTS_INFO.find(p => (p.id_codes || []).includes(plantCode));
  }
  composeState.plantInfo = plantInfo;

  if (composeState.mode === 'question') {
    titleEl.textContent = '❓ Hacer pregunta';
    titleLabel.style.display = 'none';
    titleInput.style.display = 'none';
    textLabel.textContent = 'Tu pregunta';
    textHint.textContent = 'Sé concreto: ¿qué querés saber? Sumá foto si ayuda.';
    textArea.placeholder = 'Ej: ¿es buen momento para podar fuerte? ¿Qué tiene esta hoja?';
    submitBtn.textContent = '📤 Hacer pregunta';
  } else {
    titleEl.textContent = '＋ Nueva tarea';
    titleLabel.style.display = '';
    titleInput.style.display = '';
    textLabel.textContent = 'Detalles / contexto';
    textHint.textContent = 'Lo que querés que sepa la IA al procesar esto. Opcional.';
    textArea.placeholder = 'Ej: regué con manguera, parece que necesita drenar mejor...';
    submitBtn.textContent = '📤 Crear tarea';
  }

  // Subtítulo de contexto + selector de planta (solo modo user_task sin plantCode)
  if (plantInfo) {
    const codes = plantInfo.id_codes.join(', ');
    ctxEl.textContent = `🌱 ${plantInfo.common} (${codes})`;
    plantRow.hidden = true;
  } else if (composeState.mode === 'question') {
    ctxEl.textContent = '🌱 Sin planta — pregunta general';
    plantRow.hidden = true;
  } else {
    ctxEl.textContent = '';
    plantRow.hidden = false;
    if (plantSelect && typeof PLANTS_INFO !== 'undefined') {
      // Llenar el select solo una vez
      if (plantSelect.options.length <= 1) {
        const sorted = [...PLANTS_INFO].sort((a, b) => (a.common || '').localeCompare(b.common || ''));
        sorted.forEach(p => {
          const opt = document.createElement('option');
          opt.value = p.id_codes[0];
          opt.textContent = `${p.common} (${p.id_codes.join(', ')})`;
          plantSelect.appendChild(opt);
        });
      }
      plantSelect.value = '';
    }
  }

  const hasToken = !!loadGitHubToken();
  if (hasToken && !ensurePrivacyAcknowledged()) return;
  setComposeStage(hasToken ? 'write' : 'setup');
  document.getElementById('task-compose-modal').classList.add('active');
}

function setComposeStage(stage) {
  document.querySelectorAll('#task-compose-modal .task-photo-stage').forEach(s => {
    s.hidden = (s.dataset.stage !== stage);
  });
}

document.getElementById('btn-compose-go-settings')?.addEventListener('click', () => {
  closeModal('task-compose');
  openSettingsModal();
});

// Botón principal del Timeline.
document.getElementById('btn-create-task')?.addEventListener('click', () => {
  openTaskComposeModal({ mode: 'user_task' });
});

// File inputs (cámara / galería).
['compose-camera-input', 'compose-gallery-input'].forEach(id => {
  document.getElementById(id)?.addEventListener('change', async (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    e.target.value = '';
    await loadAndPreviewComposePhoto(file);
  });
});

document.getElementById('btn-compose-photo-remove')?.addEventListener('click', () => {
  composeState.blob = null;
  const wrap = document.getElementById('compose-photo-preview-wrap');
  const pick = document.getElementById('compose-photo-pick');
  if (wrap) wrap.hidden = true;
  if (pick) pick.hidden = false;
});

async function loadAndPreviewComposePhoto(file) {
  try {
    // Resize sin overlay (las tareas/preguntas creadas por el user no tienen task_id del catálogo).
    const blob = await resizeImagePlain(file, 1024, 0.85);
    composeState.blob = blob;
    const canvas = document.getElementById('compose-photo-canvas');
    const url = URL.createObjectURL(blob);
    const img = new Image();
    img.onload = () => {
      canvas.width = img.width;
      canvas.height = img.height;
      canvas.getContext('2d').drawImage(img, 0, 0);
      URL.revokeObjectURL(url);
      const wrap = document.getElementById('compose-photo-preview-wrap');
      const pick = document.getElementById('compose-photo-pick');
      if (wrap) wrap.hidden = false;
      if (pick) pick.hidden = true;
    };
    img.src = url;
  } catch (err) {
    alert('Error procesando la foto: ' + err.message);
  }
}

// Resize sin overlay (similar a resizeAndStampImage pero sin la metadata burnt-in).
async function resizeImagePlain(file, maxSide, quality) {
  const img = await new Promise((resolve, reject) => {
    const i = new Image();
    i.onload = () => resolve(i);
    i.onerror = () => reject(new Error('No se pudo leer la imagen'));
    i.src = URL.createObjectURL(file);
  });
  let { width, height } = img;
  if (width > maxSide || height > maxSide) {
    if (width >= height) {
      height = Math.round(height * (maxSide / width));
      width = maxSide;
    } else {
      width = Math.round(width * (maxSide / height));
      height = maxSide;
    }
  }
  const canvas = document.createElement('canvas');
  canvas.width = width;
  canvas.height = height;
  canvas.getContext('2d').drawImage(img, 0, 0, width, height);
  URL.revokeObjectURL(img.src);
  return await new Promise((resolve, reject) => {
    canvas.toBlob(b => b ? resolve(b) : reject(new Error('toBlob falló')), 'image/jpeg', quality);
  });
}

document.getElementById('btn-compose-submit')?.addEventListener('click', submitCompose);

async function submitCompose() {
  const mode = composeState.mode || 'user_task';
  const text = (document.getElementById('compose-text').value || '').trim();
  let title = (document.getElementById('compose-title').value || '').trim();

  if (mode === 'user_task' && !title) {
    alert('Escribí un título corto para la tarea.');
    return;
  }
  if (mode === 'question' && !text && !composeState.blob) {
    alert('Escribí la pregunta o sumá una foto.');
    return;
  }

  // Determinar plantCode final: el que vino en composeState o el del select
  let plantCode = composeState.plantCode;
  if (!plantCode && mode === 'user_task') {
    const sel = document.getElementById('compose-plant-select');
    if (sel && sel.value) plantCode = sel.value;
  }
  let plantInfo = composeState.plantInfo;
  if (!plantInfo && plantCode && typeof PLANTS_INFO !== 'undefined') {
    plantInfo = PLANTS_INFO.find(p => (p.id_codes || []).includes(plantCode));
  }

  // Para preguntas, si no hay título usamos el primer renglón del texto.
  if (mode === 'question') {
    title = (text.split('\n')[0] || 'Pregunta').slice(0, 80);
  }

  setComposeStage('result');
  const result = document.getElementById('task-compose-result');
  result.innerHTML = `<div class="task-photo-uploading">⏳ Subiendo al repo…</div>`;

  try {
    const now = new Date();
    const stamp = now.toISOString().replace(/[-:]/g, '').replace(/\..+/, '').replace('T', '-').slice(0, 15);
    const rand = Math.random().toString(16).slice(2, 6);
    const id = `user-${now.getTime()}-${rand}`;
    const bucketKey = plantCode || '_general';

    let filename = null;
    let photoPath = null;
    if (composeState.blob) {
      filename = `${id}_${stamp}.jpg`;
      photoPath = `docs/images/uploads/${bucketKey}/${filename}`;
      const base64 = await blobToBase64(composeState.blob);
      await ghPutFile(photoPath, base64, `compose: foto para ${id}`);
    }

    // 1. Crear el user_task entry y pushearlo a sync/user_tasks.json
    const userTask = {
      id,
      kind: mode,  // "user_task" | "question"
      title,
      user_context: text || '',
      plant_codes: plantCode ? [plantCode] : [],
      plant_common: plantInfo ? (plantInfo.common || '') : '',
      plant_zone: plantInfo ? (plantInfo.zone || '') : '',
      created_at: now.toISOString(),
      created_by: loadDeviceName() || 'browser',
      last_modified_at: now.toISOString(),
      has_photo: !!filename,
      photo_filename: filename,
      ai_answer: null,
    };
    USER_TASKS[id] = userTask;
    saveUserTasksLocal();
    await flushUserTasksToRepo();

    // 2. Append entry a docs/uploads.json para que /actualizar-tareas lo procese.
    const uploadsPath = 'docs/uploads.json';
    const { sha, data } = await ghReadJsonFile(uploadsPath);
    const idx = data || {};
    if (!idx[bucketKey]) idx[bucketKey] = [];
    const uploadEntry = {
      filename,  // null si no hay foto
      uploaded_at: now.toISOString(),
      uploaded_by: loadDeviceName() || 'desconocido',
      context: mode,  // "user_task" | "question"
      task_id: id,
      task_title_snapshot: title,
      ai_status: 'pending',
      ai_evaluation: null,
    };
    if (text) uploadEntry.user_context = text;
    if (plantCode) uploadEntry.plant_id = plantCode;
    idx[bucketKey].push(uploadEntry);
    const newJson = JSON.stringify(idx, null, 2) + '\n';
    const newBase64 = btoa(unescape(encodeURIComponent(newJson)));
    await ghPutFile(uploadsPath, newBase64, `compose: registrar ${id} en uploads.json`, sha);

    // 3. Setear estado inicial active en task_states.json (para que aparezca en feed Activas).
    setTaskState(id, { status: 'active', snoozed_until: null, completed_at: null });

    // 4. Re-render timeline.
    if (typeof renderTimeline === 'function') renderTimeline();

    const labelKind = mode === 'question' ? 'pregunta' : 'tarea';
    const photoLink = photoPath
      ? `<p class="task-photo-success-link"><a href="https://github.com/${GH_REPO}/blob/main/${photoPath}" target="_blank" rel="noopener">Ver foto en GitHub →</a></p>`
      : '';
    result.innerHTML = `
      <div class="task-photo-success">
        <div class="task-photo-success-title">✅ ${labelKind[0].toUpperCase() + labelKind.slice(1)} subida</div>
        <p>Aparece en el Timeline como <strong>activa</strong> y queda <strong>pending</strong> de evaluación IA.</p>
        <p class="task-photo-success-hint">Para procesarla, abrí Claude Code y corré:</p>
        <code class="task-photo-success-cmd">/actualizar-tareas</code>
        ${photoLink}
      </div>
      <button class="btn-primary" onclick="closeModal('task-compose')">Listo</button>`;
  } catch (err) {
    const msg = err.message || String(err);
    result.innerHTML = `
      <div class="task-photo-error">
        <div class="task-photo-error-title">❌ No se pudo subir</div>
        <p>${msg}</p>
      </div>
      <div class="task-photo-actions">
        <button class="btn-secondary" onclick="setComposeStage('write')">↺ Volver</button>
        <button class="btn-secondary" onclick="closeModal('task-compose')">Cancelar</button>
      </div>`;
  }
}
"""
