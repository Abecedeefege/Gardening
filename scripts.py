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
// TAB SWITCHING (top-level: Timeline / Frente / Fondo)
// ============================================================
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.zone-content').forEach(z => z.classList.remove('active'));
    btn.classList.add('active');
    const zone = btn.dataset.zone;
    document.querySelector(`.zone-content[data-zone="${zone}"]`).classList.add('active');
    window.scrollTo({top: 0, behavior: 'smooth'});
    if (zone === 'timeline') renderTimeline();
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

document.querySelectorAll('.filter-tags').forEach(filterBar => {
  // Skip timeline filter — handled separately
  if (filterBar.classList.contains('timeline-filters')) return;
  filterBar.querySelectorAll('.ftag').forEach(btn => {
    btn.addEventListener('click', () => {
      filterBar.querySelectorAll('.ftag').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      const pane = filterBar.closest('.subtab-pane');
      if (!pane) return;
      pane.querySelectorAll('.plant-card').forEach(card => {
        const tags = card.dataset.tags || '';
        const visible = filter === 'all' || tags.includes(filter);
        card.style.display = visible ? '' : 'none';
      });
    });
  });
});

// ============================================================
// TIMELINE — STATE MANAGEMENT (localStorage)
// ============================================================
const STATE_KEY = 'jardineando_task_states_v1';
const CONTACTS_KEY = 'jardineando_contacts_v1';

function loadStates() {
  try { return JSON.parse(localStorage.getItem(STATE_KEY) || '{}'); }
  catch { return {}; }
}
function saveStates(states) {
  localStorage.setItem(STATE_KEY, JSON.stringify(states));
}
function getTaskState(taskId) {
  const states = loadStates();
  return states[taskId] || { status: 'active', snoozed_until: null, completed_at: null };
}
function setTaskState(taskId, state) {
  const states = loadStates();
  states[taskId] = state;
  saveStates(states);
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
    statusPill = `<span class="task-status-pill done">✅ Hecha · ${fmtDate(st.completed_at)}</span>`;
  } else if (cls === 'snoozed') {
    statusPill = `<span class="task-status-pill snoozed">😴 Pospuesta hasta ${fmtDate(st.snoozed_until)}</span>`;
  }

  let actions = '';
  if (cls === 'active') {
    actions = `
      <div class="task-actions">
        <button class="task-btn task-btn-done" data-action="done" data-task-id="${task.id}">✅ Hecho</button>
        <button class="task-btn task-btn-snooze" data-action="snooze" data-task-id="${task.id}">😴 Posponer</button>
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

  return `
    <article class="task-card priority-${task.priority} ${cls === 'done' ? 'completed' : ''} ${cls === 'snoozed' ? 'snoozed' : ''}"
             data-task-id="${task.id}" style="--swipe-strength: 0">
      <div class="swipe-hint left">😴</div>
      <div class="swipe-hint right">✅</div>
      <div class="task-header">
        ${photoHtml}
        <div class="task-meta">
          <div class="task-meta-top">
            <span class="task-priority-pill" style="background: ${prio.color}">${prio.emo} ${prio.label}</span>
            <span class="task-zone-pill">${task.plant_codes.join(', ')}</span>
            ${statusPill}
          </div>
          <h3 class="task-title">${task.title}</h3>
          <div class="task-plant">${task.plant_common}</div>
          ${dueText ? `<div class="task-due ${dueClass}">📅 ${overdue && cls === 'active' ? 'Vencida — ' : ''}${dueText}</div>` : ''}
        </div>
      </div>
      <div class="task-description">${task.description}</div>
      ${actions}
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

  // Resumen
  summary.innerHTML = `
    <div class="stat-block"><div class="stat-num">${buckets.active.length}</div><div class="stat-label">📌 Activas</div></div>
    <div class="stat-block"><div class="stat-num">${buckets.done.length}</div><div class="stat-label">✅ Hechas</div></div>
    <div class="stat-block"><div class="stat-num">${buckets.snoozed.length}</div><div class="stat-label">😴 Pospuestas</div></div>
  `;

  // Render filtered feed
  const tasks = buckets[currentFilter] || [];

  if (tasks.length === 0) {
    feed.innerHTML = '';
    empty.style.display = 'block';
  } else {
    empty.style.display = 'none';
    feed.innerHTML = tasks.map(renderTaskCard).join('');
    // hidratar imágenes y bind swipe + lightbox
    feed.querySelectorAll('img[data-img]').forEach(loadImg);
    setupLightbox(feed);
    setupTaskInteractions(feed);
  }
}

// ============================================================
// TIMELINE — TASK INTERACTIONS (clicks + swipe)
// ============================================================
function setupTaskInteractions(scope) {
  // Click handlers
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
      else if (action === 'reactivate') reactivateTask(task);
    });
  });

  // Swipe (touch + mouse)
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
    const taskId = card.dataset.taskId;
    const task = TASKS.find(t => t.id === taskId);

    if (Math.abs(dx) > 100 && task) {
      if (dx > 0) {
        // swipe derecha → marcar hecho
        card.classList.add('swipe-out-right');
        setTimeout(() => markDone(task), 300);
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
  const msg = (c.default_template || '').replace('{task}', taskText);
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
"""
