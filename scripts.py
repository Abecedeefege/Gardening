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
    pane.querySelectorAll('.plant-card, .care-card, .idea-card, .huerta-card').forEach(card => {
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
  TASKS.forEach(t => {
    const s = states[t.id] || { status: 'active', snoozed_until: null };
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
  const due = new Date(task.due_year, task.due_month - 1, 28); // último día del mes objetivo
  return due < new Date();
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

  const photoHtml = task.plant_photo && IMG[task.plant_photo]
    ? `<img class="task-photo" data-img="${task.plant_photo}" data-action="lightbox" alt="">`
    : `<div class="task-photo-placeholder">🌱</div>`;

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

  // Activas: 3 botones (Hecho / Posponer / WhatsApp). Hechas/Pospuestas: solo Reactivar.
  let actions = '';
  if (cls === 'active') {
    actions = `
      <div class="task-actions">
        <button class="task-btn task-btn-done" data-action="done" data-task-id="${task.id}">✅ Hecho</button>
        <button class="task-btn task-btn-snooze" data-action="snooze" data-task-id="${task.id}">😴 Posponer</button>
        <button class="task-btn task-btn-photo" data-action="photo" data-task-id="${task.id}">📷 Subir foto</button>
        <button class="task-btn task-btn-whatsapp" data-action="whatsapp" data-task-id="${task.id}">💬 WhatsApp</button>
      </div>`;
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
              <span class="task-zone-pill">${task.plant_codes.join(', ')}</span>
              <span class="task-id-badge" title="ID de la tarea — clickear para copiar">${task.id}</span>
              ${statusPill}
            </div>
            <h3 class="task-title">${task.title}</h3>
            <div class="task-plant">${task.plant_common}</div>
            ${task.short_desc ? `<p class="task-short">${task.short_desc}</p>` : ''}
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

function renderTimeline() {
  const feed = document.getElementById('timeline-feed');
  const empty = document.getElementById('timeline-empty');
  const summary = document.getElementById('timeline-summary');

  // Clasificar todas las tareas
  const buckets = { active: [], snoozed: [], done: [], all: [] };
  TASKS.forEach(task => {
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
    if (t.due_year < curYear || (t.due_year === curYear && t.due_month < curMonth)) {
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
function setupTaskInteractions(scope) {
  // Click handlers para botones de acción
  scope.querySelectorAll('button[data-action]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const action = btn.dataset.action;
      const taskId = btn.dataset.taskId;
      const task = TASKS.find(t => t.id === taskId);
      if (!task) return;
      if (action === 'done') markDone(task);
      else if (action === 'snooze') openSnoozeModal(task);
      else if (action === 'whatsapp') openWhatsAppModal(task);
      else if (action === 'photo') openTaskPhotoModal(task);
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
    const task = TASKS.find(t => t.id === taskId);

    if (Math.abs(dx) > 100 && task) {
      if (dx > 0) {
        // swipe derecha → abrir modal WhatsApp
        card.style.transform = '';
        card.style.setProperty('--swipe-strength', 0);
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
// SETTINGS — GitHub PAT + device name (localStorage only)
// ============================================================
const GITHUB_TOKEN_KEY = 'jardineando_github_token_v1';
const DEVICE_NAME_KEY = 'jardineando_device_name_v1';

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
  document.getElementById('settings-github-token').value = loadGitHubToken();
  document.getElementById('settings-device-name').value = loadDeviceName();
  document.getElementById('settings-github-feedback').textContent = '';
  document.getElementById('settings-github-feedback').className = 'settings-feedback';
  document.getElementById('settings-modal').classList.add('active');
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
  saveGitHubToken(token);
  saveDeviceName(deviceName);
  closeModal('settings');
});

// ============================================================
// GITHUB API CLIENT — read/write archivos en el repo
// ============================================================
const GH_REPO = 'abecedeefege/gardening';
const GH_API = `https://api.github.com/repos/${GH_REPO}/contents`;

async function ghGetFile(path) {
  const token = loadGitHubToken();
  if (!token) throw new Error('Sin GitHub PAT configurado');
  const r = await fetch(`${GH_API}/${path}?ref=main`, {
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

function openTaskPhotoModal(task) {
  pendingPhotoTask = task;
  pendingPhotoBlob = null;
  document.getElementById('task-photo-name').textContent = `📌 ${task.title} · ${task.plant_common} (${task.plant_codes.join(', ')})`;

  // Mostrar la stage correcta según si hay token configurado.
  const hasToken = !!loadGitHubToken();
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

  // Construir tira de fotos: main + loc + uploads (más recientes primero).
  const photoCells = [];
  if (plant.main_photo && IMG[plant.main_photo]) {
    photoCells.push({ kind: 'main', src_data: IMG[plant.main_photo], filename: plant.main_photo, label: 'Foto principal' });
  }
  if (plant.loc_photo && IMG[plant.loc_photo] && plant.loc_photo !== plant.main_photo) {
    photoCells.push({ kind: 'loc', src_data: IMG[plant.loc_photo], filename: plant.loc_photo, label: 'Vista aérea / ubicación' });
  }
  // Uploads ordenados por uploaded_at descendente.
  const sortedUploads = [...uploads].sort((a, b) => (b.uploaded_at || '').localeCompare(a.uploaded_at || ''));
  sortedUploads.forEach(u => {
    photoCells.push({
      kind: 'upload',
      src_url: `images/uploads/${primaryCode}/${u.filename}`,
      filename: u.filename,
      label: u.context === 'task' ? `Tarea: ${u.task_title_snapshot || u.task_id}` : (u.note || 'Foto del catálogo'),
      uploaded_at: u.uploaded_at,
      uploaded_by: u.uploaded_by,
      ai_evaluation: u.ai_evaluation,
    });
  });

  const photosHtml = photoCells.length ? photoCells.map((c, i) => {
    const src = c.src_data || c.src_url;
    const tooltip = c.uploaded_at
      ? `${c.label}\n${new Date(c.uploaded_at).toLocaleString('es-UY')}`
      : c.label;
    const tag = c.kind === 'main' ? '<span class="species-photo-tag main">Principal</span>'
              : c.kind === 'loc'  ? '<span class="species-photo-tag loc">Ubicación</span>'
              : c.kind === 'upload' ? `<span class="species-photo-tag upload">${c.uploaded_by || 'Subida'}</span>`
              : '';
    return `<div class="species-photo-cell" data-idx="${i}" title="${tooltip.replace(/"/g,'&quot;')}">
      <img src="${src}" alt="${c.label}" loading="lazy">
      ${tag}
    </div>`;
  }).join('') : '<div class="species-no-photos">Sin fotos todavía.</div>';

  // Lista de tareas próximas / activas para esta planta.
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

  // Datos curados de cuidados.
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

  document.getElementById('species-detail-body').innerHTML = `
    <div class="species-detail-head">
      <div class="species-detail-codes">${plant.id_codes.join(', ')} · ${plant.zone}</div>
      <h3 class="species-detail-title">${plant.common}</h3>
      <div class="species-detail-sci">${plant.sci || ''}</div>
      ${plant.other_names ? `<div class="species-detail-other">↳ ${plant.other_names}</div>` : ''}
    </div>

    <div class="species-photos-strip" id="species-photos-strip">
      ${photosHtml}
      <div class="species-photo-cell add" data-action="add-species-photo" title="Sumar foto al catálogo">
        <span class="species-add-plus">+</span>
        <span class="species-add-label">Sumar foto</span>
      </div>
    </div>

    <div class="species-detail-section">
      ${charruaHtml}
      <p class="species-desc">${plant.desc || ''}</p>
      ${funFactHtml}
      <div class="species-tags">${tagsHtml}</div>
    </div>

    ${careHtml}
    ${tasksHtml}
  `;

  // Bind click en thumbnails → lightbox; en "+" → upload modal.
  const strip = document.getElementById('species-photos-strip');
  strip.querySelectorAll('.species-photo-cell:not(.add)').forEach(cell => {
    cell.addEventListener('click', () => {
      const img = cell.querySelector('img');
      if (img && img.src) openLightboxWithUrl(img.src);
    });
  });
  strip.querySelector('[data-action="add-species-photo"]').addEventListener('click', () => {
    closeModal('species-detail');
    openSpeciesPhotoModal(plant);
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
    result.innerHTML = `
      <div class="task-photo-error">
        <div class="task-photo-error-title">❌ No se pudo subir</div>
        <p>${err.message}</p>
      </div>
      <div class="task-photo-actions">
        <button class="btn-secondary" onclick="setSpeciesPhotoStage('preview')">↺ Volver al preview</button>
        <button class="btn-secondary" onclick="closeModal('species-photo')">Cancelar</button>
      </div>`;
  }
}

// ============================================================
// SYNC ENGINE — read-on-load (write se agrega en Batch 6)
// ============================================================
// Estado de sync (placeholder, write debounce viene después).
let _stateDirty = false;
function markStateDirty() {
  _stateDirty = true;
  // El sync write real se conecta en Batch 6.
}

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
    result.innerHTML = `
      <div class="task-photo-error">
        <div class="task-photo-error-title">❌ No se pudo subir</div>
        <p>${err.message}</p>
      </div>
      <div class="task-photo-actions">
        <button class="btn-secondary" onclick="setTaskPhotoStage('preview')">↺ Volver al preview</button>
        <button class="btn-secondary" onclick="closeModal('task-photo')">Cancelar</button>
      </div>`;
  }
}
"""
