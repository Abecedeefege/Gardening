"""
Estilos CSS — diseño minimalista moderno.
Inter font · paleta neutra zinc + accent verde · bordes en lugar de sombras pesadas.
"""

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  /* Surfaces */
  --bg: #fafafa;
  --bg-card: #ffffff;
  --bg-soft: #f4f4f5;
  --bg-hover: #f4f4f5;

  /* Text */
  --text: #09090b;
  --text-2: #3f3f46;
  --text-3: #71717a;
  --text-muted: #a1a1aa;

  /* Borders */
  --border: #e4e4e7;
  --border-soft: #f4f4f5;
  --border-strong: #d4d4d8;

  /* Accent (green) */
  --accent: #15803d;
  --accent-hover: #166534;
  --accent-soft: #f0fdf4;
  --accent-text: #14532d;

  /* States */
  --red: #dc2626;
  --red-soft: #fef2f2;
  --orange: #ea580c;
  --orange-soft: #fff7ed;
  --green: #16a34a;
  --green-soft: #f0fdf4;
  --blue: #2563eb;
  --blue-soft: #eff6ff;
  --whatsapp: #25d366;
  --whatsapp-hover: #1da851;

  /* Shadows — minimal */
  --shadow-xs: 0 1px 2px rgba(9, 9, 11, 0.04);
  --shadow-sm: 0 1px 3px rgba(9, 9, 11, 0.06), 0 1px 2px rgba(9, 9, 11, 0.04);
  --shadow-md: 0 4px 6px -1px rgba(9, 9, 11, 0.06), 0 2px 4px -2px rgba(9, 9, 11, 0.04);
  --shadow-lg: 0 10px 15px -3px rgba(9, 9, 11, 0.08), 0 4px 6px -4px rgba(9, 9, 11, 0.04);

  /* Radii */
  --r-sm: 6px;
  --r-md: 8px;
  --r-lg: 12px;
  --r-xl: 16px;
  --r-full: 999px;

  /* Transitions */
  --t: 150ms cubic-bezier(0.4, 0, 0.2, 1);
}

* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }

body {
  margin: 0; padding: 0;
  background-color: var(--bg);
  background-image:
    radial-gradient(ellipse at 15% 0%, rgba(21, 128, 61, 0.06) 0%, transparent 55%),
    radial-gradient(ellipse at 85% 100%, rgba(37, 99, 235, 0.04) 0%, transparent 55%);
  background-attachment: fixed;
  color: var(--text);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
  font-size: 15px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-feature-settings: 'cv11', 'ss01', 'tnum';
  letter-spacing: -0.011em;
  min-height: 100vh;
  overflow-x: hidden;
  transition: background-color 600ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* Backgrounds pastel — uno por zona, perceptibles pero suaves */
body.zone-todo     { background-color: #f5f5f7; }   /* zinc neutral */
body.zone-frente   { background-color: #fbf3e6; }   /* crema cálido — sol */
body.zone-fondo    { background-color: #e6f0fa; }   /* celeste agua — piscina */
body.zone-interior { background-color: #efeaf5; }   /* lavanda suave — adentro */
body.zone-timeline { background-color: #eef5e8; }   /* verde menta — tareas */

button, input, textarea, select {
  font-family: inherit;
  font-size: inherit;
  letter-spacing: inherit;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 16px 16px 80px;
}
@media (min-width: 700px) {
  .container { padding: 32px 24px 96px; }
}
.container.container-top { padding-bottom: 0; }
@media (min-width: 700px) {
  .container.container-top { padding-bottom: 0; }
}

/* HEADER — compacto, ≤30% viewport en móvil */
header.main-header {
  text-align: center;
  padding: 4px 0 var(--strip-gap);
  border-bottom: none;
  margin-bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}
h1.brand {
  font-size: clamp(1.85rem, 7vw, 3.5rem);
  font-weight: 800;
  letter-spacing: -0.045em;
  line-height: 0.95;
  margin: 0;
  color: var(--text);
  background: linear-gradient(135deg, var(--text) 0%, #3f3f46 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  display: inline-flex;
  align-items: center;
  gap: 12px;
}
.brand-logo {
  width: clamp(36px, 7vw, 56px);
  height: auto;
  flex: 0 0 auto;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.08));
}
.brand-emoji { display: none; }
h2.subbrand {
  font-size: clamp(0.425rem, 1vw, 0.55rem);
  font-weight: 500;
  letter-spacing: -0.005em;
  color: var(--accent);
  margin: 0 0 2px;
  font-style: normal;
  line-height: 1.1;
}
/* ======================================================
   STRIPS UNIFICADAS — weather, stats, main-tabs, subtabs
   Todas son barras segmentadas full-width con items
   distribuidos por igual (flex: 1 1 0). Separación
   constante entre módulos (--strip-gap).
   ====================================================== */
:root { --strip-gap: 6px; }

.main-tabs,
.subtab-nav {
  display: flex;
  width: 100%;
  max-width: 100%;
  margin: 0 0 var(--strip-gap);
  padding: 3px;
  gap: 3px;
  background: rgba(255, 255, 255, 0.78);
  border: 1px solid var(--border);
  border-radius: var(--r-full);
  box-shadow: 0 1px 2px rgba(9, 9, 11, 0.03);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  flex-wrap: nowrap;
  overflow: hidden;
  box-sizing: border-box;
}

/* WEATHER — bloque informativo centrado, no a full width */
.weather-line {
  display: flex;
  width: auto;
  max-width: 380px;
  margin: 0 auto var(--strip-gap);
  padding: 6px 12px;
  background: transparent;
  border: none;
  border-radius: 0;
  box-shadow: none;
  -webkit-backdrop-filter: none;
  backdrop-filter: none;
  font-size: 0.72rem;
  color: var(--text-3);
  font-weight: 500;
  align-items: center;
  justify-content: center;
  gap: 14px;
  white-space: nowrap;
  overflow: visible;
  box-sizing: border-box;
}
.weather-cell {
  flex: 0 0 auto;
  display: inline-flex; align-items: center;
  gap: 4px;
  padding: 0;
  white-space: nowrap;
  overflow: visible; text-overflow: clip;
  line-height: 1;
}
.weather-cell + .weather-cell { border-left: none; }
.weather-cell .weather-emoji { font-size: 0.95rem; line-height: 1; flex-shrink: 0; }
.weather-cell .weather-val { font-feature-settings: 'tnum'; }
.weather-cell strong { color: var(--text); font-weight: 600; }

/* STATS TICKER — marquee continuo de derecha a izquierda (no accionable) */
.stats-ticker {
  width: 100%;
  max-width: 100%;
  margin: 0 auto var(--strip-gap);
  padding: 6px 0;
  font-size: 0.78rem;
  color: var(--text-3);
  overflow: hidden;
  position: relative;
  /* Fade en los bordes para que los items aparezcan/salgan suaves */
  -webkit-mask-image: linear-gradient(to right, transparent 0, black 28px, black calc(100% - 28px), transparent 100%);
  mask-image: linear-gradient(to right, transparent 0, black 28px, black calc(100% - 28px), transparent 100%);
}
.ticker-track {
  display: inline-flex;
  gap: 28px;
  white-space: nowrap;
  animation: ticker-slide 38s linear infinite;
  will-change: transform;
}
.ticker-track:hover { animation-play-state: paused; }
@keyframes ticker-slide {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
@media (prefers-reduced-motion: reduce) {
  .ticker-track { animation: none; }
}
.ticker-item {
  display: inline-flex; align-items: center;
  gap: 6px; flex: 0 0 auto;
  line-height: 1.2;
}
.ticker-item strong {
  color: var(--text); font-weight: 700;
  font-feature-settings: 'tnum'; font-size: 0.82rem;
}
.ticker-emoji { font-size: 0.95rem; line-height: 1; flex-shrink: 0; }
.ticker-label { color: var(--text-3); }

/* MAIN TABS — pestañas segmentadas full-width, edge-to-edge */
.main-tabs {
  position: sticky;
  top: 8px;
  z-index: 50;
  padding: 0;
  gap: 0;
  border-radius: 10px;
  border-color: var(--border-strong);
  background: rgba(255, 255, 255, 0.92);
  box-shadow:
    0 1px 2px rgba(9, 9, 11, 0.04),
    0 8px 24px rgba(9, 9, 11, 0.06);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  backdrop-filter: blur(20px) saturate(180%);
}
.tab-btn {
  flex: 1 1 0; min-width: 0;
  background: transparent;
  border: none;
  border-radius: 0;
  padding: 10px 6px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  color: var(--text-2);
  transition: color 200ms cubic-bezier(0.4, 0, 0.2, 1),
              background 200ms cubic-bezier(0.4, 0, 0.2, 1);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  white-space: nowrap;
}
.tab-btn + .tab-btn { border-left: 1px solid var(--border-soft); }
.tab-btn:hover:not(.active) {
  color: var(--text);
  background: rgba(0, 0, 0, 0.04);
}
.tab-btn:active { transform: scale(0.985); }
.tab-btn.active {
  color: white;
  background: var(--text);
  font-weight: 700;
  box-shadow: inset 0 -2px 0 rgba(255, 255, 255, 0.06);
}
.tab-emoji { font-size: 1rem; line-height: 1; flex-shrink: 0; }
.tab-label { line-height: 1; overflow: hidden; text-overflow: ellipsis; }

/* IDEAS — secciones (Espacios verdes / Plantas / Huerta) */
.ideas-section {
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid var(--border-soft);
}
.ideas-section:first-child {
  margin-top: 0;
  padding-top: 0;
  border-top: none;
}
.ideas-section-now {
  background: linear-gradient(180deg, rgba(22, 163, 74, 0.07) 0%, rgba(22, 163, 74, 0) 100%);
  margin-left: -16px;
  margin-right: -16px;
  padding: 16px 16px 8px;
  border-radius: 14px;
  border: 1px solid rgba(22, 163, 74, 0.18);
}
.ideas-section-now .ideas-intro h3 { color: #166534; }

/* Badge "óptimo plantar AHORA" en idea-card y huerta-card */
.now-badge {
  display: inline-block;
  background: #16a34a;
  color: white;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  padding: 4px 10px;
  border-radius: 999px;
  margin-bottom: 10px;
  box-shadow: 0 1px 3px rgba(22, 163, 74, 0.32);
}
.idea-card.is-now,
.huerta-card.is-now {
  border-color: #86efac;
  box-shadow: 0 0 0 2px rgba(22, 163, 74, 0.12);
}

/* Mes actual marcado en el calendario de cada huerta-card */
.hcell.current {
  outline: 2px solid #16a34a;
  outline-offset: -2px;
  z-index: 1;
  position: relative;
}

/* "Ver todas" — botón que expande el resto de cards colapsadas */
.btn-show-all {
  display: block;
  width: 100%;
  margin: 14px 0 4px;
  padding: 12px 16px;
  background: rgba(22, 163, 74, 0.08);
  color: #166534;
  border: 1px dashed rgba(22, 163, 74, 0.4);
  border-radius: var(--r-md);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}
.btn-show-all:hover {
  background: rgba(22, 163, 74, 0.14);
}
.btn-show-all[aria-expanded="true"] {
  background: rgba(22, 163, 74, 0.04);
  border-style: solid;
}
.ideas-collapsed {
  margin-top: 12px;
}

/* IMPORTANTE: el atributo HTML `hidden` lo aplica el UA stylesheet como
   display:none, pero las reglas .cards-grid { display: grid } y
   .hloc-grid { display: grid } de autor lo pisan. Hace falta forzar
   con [hidden] de mayor especificidad para que el colapso funcione. */
.cards-grid[hidden],
.hloc-grid[hidden],
.ideas-collapsed[hidden] {
  display: none !important;
}

/* TO-DO'S STRIP — botón pequeño + label "X tareas pendientes" */
.todo-strip {
  display: flex; align-items: center; gap: 10px;
  margin: 0 0 var(--strip-gap);
  padding: 2px 4px;
}
.todo-btn {
  flex: 0 0 auto;
  background: rgba(255, 255, 255, 0.78);
  color: var(--text-2);
  border: 1px solid var(--border-strong);
  border-radius: var(--r-md);
  padding: 8px 14px;
  font-size: 0.85rem; font-weight: 600;
  cursor: pointer;
  display: inline-flex; align-items: center; gap: 6px;
  transition: background var(--t), color var(--t), border-color var(--t), transform 150ms;
  white-space: nowrap;
  text-decoration: none;
}
.todo-btn:hover {
  background: rgba(255, 255, 255, 0.95);
  color: var(--text);
  border-color: var(--text-3);
}
.todo-btn:active { transform: scale(0.97); }
.todo-btn.active {
  background: var(--text);
  color: white;
  border-color: var(--text);
}
.todo-label {
  color: var(--text-3);
  font-size: 0.85rem;
  white-space: nowrap;
  overflow: hidden; text-overflow: ellipsis;
  font-feature-settings: 'tnum';
}

/* container que envuelve las zonas — sticky main-tabs + subtab-nav siguen pegados */
.container-zones {
  padding-top: 0;
}
@media (min-width: 700px) {
  .container-zones { padding-top: 8px; }
}

/* SUBTAB NAV — segmented full-width, comparte estilos arriba */
.subtab-nav {
  background: rgba(255, 255, 255, 0.7);
}
.subtab-btn {
  background: transparent; border: none;
  padding: 7px 4px;
  font-size: 0.78rem; font-weight: 500;
  cursor: pointer; border-radius: var(--r-full);
  color: var(--text-3);
  transition:
    color 200ms cubic-bezier(0.4, 0, 0.2, 1),
    background 200ms cubic-bezier(0.4, 0, 0.2, 1);
  flex: 1 1 0; min-width: 0;
  white-space: nowrap;
  overflow: hidden; text-overflow: ellipsis;
  display: inline-flex; align-items: center; justify-content: center; gap: 4px;
}
.subtab-btn:hover { background: rgba(0, 0, 0, 0.04); color: var(--text); }
.subtab-btn.active {
  background: var(--text);
  color: white;
  font-weight: 600;
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.06),
    0 2px 4px rgba(0, 0, 0, 0.06);
}

/* PANES */
.zone-content { display: none; }
.zone-content.active { display: block; animation: fadeIn 0.25s ease; }
.subtab-pane { display: none; }
.subtab-pane.active { display: block; animation: fadeIn 0.25s ease; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* FILTERS */
.filter-bar {
  display: flex; gap: 8px;
  margin-bottom: 8px;
  flex-wrap: nowrap;
  align-items: stretch;
}
.search {
  flex: 1 1 0; min-width: 0;
  padding: 10px 14px;
  font-size: 0.9rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  color: var(--text);
  transition: border-color var(--t), box-shadow var(--t);
  max-width: 100%;
}
.search::placeholder { color: var(--text-muted); }
.search:focus {
  outline: none; border-color: var(--text-2);
  box-shadow: 0 0 0 3px rgba(9, 9, 11, 0.04);
}

/* FILTER TOGGLE — botón ícono+label que abre el panel de chips */
.filter-toggle {
  flex: 0 0 auto;
  display: inline-flex; align-items: center; gap: 6px;
  padding: 9px 12px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  font-size: 0.85rem; font-weight: 600;
  color: var(--text-2);
  cursor: pointer;
  transition: border-color var(--t), background var(--t), color var(--t);
  white-space: nowrap;
}
.filter-toggle:hover { background: var(--bg-soft); border-color: var(--border-strong); color: var(--text); }
.filter-toggle .filter-svg { flex-shrink: 0; }
.filter-toggle .filter-current { font-weight: 600; max-width: 90px; overflow: hidden; text-overflow: ellipsis; }
.filter-toggle .filter-caret {
  font-size: 0.7rem; opacity: 0.7;
  transition: transform 200ms ease;
  line-height: 1;
}
.filter-toggle[aria-expanded="true"] {
  background: var(--text); color: white; border-color: var(--text);
}
.filter-toggle[aria-expanded="true"] .filter-caret { transform: rotate(180deg); }

/* FILTER PANEL — chips que se despliegan abajo del bar */
.filter-panel {
  display: flex; flex-wrap: wrap; gap: 6px;
  padding: 10px 12px;
  margin-bottom: 16px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  box-shadow: 0 4px 12px rgba(9, 9, 11, 0.05);
  max-height: 60vh;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  animation: fadeIn 0.18s ease;
}
.filter-panel[hidden] { display: none; }

.ftag {
  background: var(--bg-card);
  border: 1px solid var(--border-strong);
  padding: 7px 12px;
  font-size: 0.82rem; font-weight: 600;
  cursor: pointer; border-radius: var(--r-full);
  color: var(--text-2);
  transition: all var(--t);
  white-space: nowrap;
}
.ftag:hover { background: var(--bg-soft); border-color: var(--text-3); }
.ftag.active {
  background: var(--text); color: white; border-color: var(--text);
  box-shadow: 0 1px 3px rgba(9,9,11,0.18);
}

/* CARDS GRID */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr));
  gap: 16px;
  min-width: 0;
}
.cards-grid.care-grid-list { grid-template-columns: repeat(auto-fill, minmax(min(100%, 420px), 1fr)); }

/* PLANT INFO CARD — overlay layout (foto fill con texto encima) */
.plant-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  box-shadow:
    0 1px 2px rgba(9, 9, 11, 0.04),
    0 1px 3px rgba(9, 9, 11, 0.05);
  transition:
    border-color 200ms cubic-bezier(0.16, 1, 0.3, 1),
    transform 250ms cubic-bezier(0.16, 1, 0.3, 1),
    box-shadow 250ms cubic-bezier(0.16, 1, 0.3, 1);
}
.plant-card:hover {
  border-color: var(--border-strong);
  transform: translateY(-3px);
  box-shadow:
    0 4px 8px rgba(9, 9, 11, 0.06),
    0 16px 36px rgba(9, 9, 11, 0.08);
}
.card-photo-wrap {
  position: relative;
  width: 100%;
  height: 320px;
  overflow: hidden;
  background: var(--bg-soft);
  cursor: pointer;
}
.card-photo {
  width: 100%; height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.card-photo-wrap:hover .card-photo { transform: scale(1.03); }

.card-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 14px 16px;
  color: white;
  background:
    linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.0) 22%, rgba(0,0,0,0.0) 48%, rgba(0,0,0,0.72) 100%);
}
.card-title {
  font-size: 1.05rem; font-weight: 700;
  margin: 0;
  color: white;
  line-height: 1.25;
  letter-spacing: -0.01em;
  font-family: inherit;
  text-shadow: 0 1px 4px rgba(0,0,0,0.65);
  align-self: flex-start;
  max-width: 90%;
}
.card-overlay-bottom {
  display: flex; flex-direction: column;
  align-items: center;
  gap: 6px;
  text-align: center;
  width: 100%;
}
.card-sci {
  font-style: italic;
  color: rgba(255,255,255,0.92);
  font-size: 0.82rem;
  font-weight: 400;
  text-shadow: 0 1px 3px rgba(0,0,0,0.7);
  margin: 0;
}
.card-other {
  font-size: 0.78rem;
  color: rgba(255,255,255,0.85);
  text-shadow: 0 1px 3px rgba(0,0,0,0.7);
  margin: 0;
}
.card-chips {
  display: flex; flex-wrap: wrap;
  gap: 4px;
  justify-content: center;
  margin-top: 2px;
}
.tag {
  font-size: 0.7rem; padding: 3px 8px;
  border-radius: var(--r-sm);
  color: white; white-space: nowrap;
  font-weight: 500;
  box-shadow: 0 1px 3px rgba(0,0,0,0.35);
}
.card-type-chip {
  font-size: 0.7rem; padding: 3px 8px;
  border-radius: var(--r-sm);
  background: rgba(255,255,255,0.92);
  color: var(--text);
  white-space: nowrap;
  font-weight: 500;
  box-shadow: 0 1px 3px rgba(0,0,0,0.35);
}

/* CARE CARD */
.care-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--r-lg);
  overflow: hidden; box-shadow: none;
  display: flex; flex-direction: column;
}
.care-header {
  padding: 18px 20px 14px;
  background: var(--bg-card); color: var(--text);
  border-bottom: 1px solid var(--border);
}
.care-id {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 0.72rem; color: var(--text-3);
  margin-bottom: 4px; opacity: 1; font-weight: 500;
}
.care-title {
  font-family: inherit; margin: 0;
  font-size: 1.1rem; font-weight: 600;
  letter-spacing: -0.01em; line-height: 1.3;
}
.care-sci {
  font-style: italic; font-size: 0.82rem;
  color: var(--text-3); opacity: 1; margin-top: 2px;
}
.urgency-banner {
  background: var(--bg-soft);
  border-left: 3px solid;
  padding: 12px 16px;
  display: flex; flex-wrap: wrap;
  align-items: center; gap: 10px;
  font-size: 0.85rem;
}
.urgency-badge {
  color: white; padding: 2px 8px;
  border-radius: var(--r-sm);
  font-size: 0.7rem; font-weight: 600;
  white-space: nowrap; letter-spacing: 0.02em;
}
.urgency-when {
  margin-left: auto; color: var(--text-3);
  font-size: 0.8rem; font-weight: 500;
}
.care-grid {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 0; background: var(--border-soft); padding: 1px;
}
.care-section { background: var(--bg-card); padding: 14px 16px; }
.care-label {
  font-size: 0.7rem; text-transform: uppercase;
  letter-spacing: 0.05em; color: var(--text-3);
  font-weight: 600; margin-bottom: 6px;
}
.big-icons { font-size: 0.85rem; margin-left: 4px; }
.care-value { font-size: 0.85rem; line-height: 1.5; color: var(--text); }
.month-row { display: flex; gap: 3px; margin-top: 10px; flex-wrap: wrap; }
.month-pill {
  font-size: 0.68rem; padding: 3px 7px;
  background: var(--bg-soft); color: var(--text-3);
  border-radius: var(--r-sm); font-weight: 500;
  text-transform: lowercase;
  border: 1px solid var(--border-soft);
}
.month-pill.active {
  background: var(--text); color: white;
  font-weight: 600; border-color: var(--text);
}

/* IDEA CARD */
.idea-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: 16px;
  padding: 20px;
  box-shadow:
    0 1px 2px rgba(9, 9, 11, 0.04),
    0 1px 3px rgba(9, 9, 11, 0.05);
  transition:
    border-color 200ms cubic-bezier(0.16, 1, 0.3, 1),
    transform 250ms cubic-bezier(0.16, 1, 0.3, 1),
    box-shadow 250ms cubic-bezier(0.16, 1, 0.3, 1);
}
.idea-card:hover {
  border-color: var(--border-strong);
  border-left-color: var(--accent);
  transform: translateY(-2px);
  box-shadow:
    0 4px 8px rgba(9, 9, 11, 0.06),
    0 12px 28px rgba(9, 9, 11, 0.07);
}
.idea-title {
  font-family: inherit; font-size: 1.05rem;
  font-weight: 600; margin: 0 0 2px;
  color: var(--text); letter-spacing: -0.01em;
}
.idea-sci { font-style: italic; color: var(--text-3); font-size: 0.82rem; margin-bottom: 8px; }
.idea-type {
  font-size: 0.78rem; background: var(--bg-soft);
  border: 1px solid var(--border);
  padding: 2px 10px; border-radius: var(--r-sm);
  display: inline-block; color: var(--text-2);
  margin-bottom: 10px; font-weight: 500;
}
.idea-tags { display: flex; flex-wrap: wrap; gap: 4px; margin: 8px 0 12px; }
.idea-why, .idea-where, .idea-size, .idea-season {
  font-size: 0.85rem; margin: 8px 0;
  color: var(--text-2); line-height: 1.5;
}
.idea-why { color: var(--text); margin-bottom: 12px; }
.idea-where {
  background: var(--bg-soft);
  padding: 10px 12px;
  border-radius: var(--r-md);
  border-left: none;
  border: 1px solid var(--border-soft);
}
.idea-season {
  background: var(--accent-soft);
  padding: 10px 12px;
  border-radius: var(--r-md);
  border-left: none;
  border: 1px solid #dcfce7;
  color: var(--accent-text);
}
.ideas-intro {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--text);
  padding: 18px 22px;
  margin-bottom: 28px;
  border-radius: var(--r-md);
}
.ideas-intro h3 {
  font-family: inherit; margin: 0 0 6px;
  color: var(--text); font-size: 1.05rem;
  font-weight: 600; letter-spacing: -0.01em;
}
.ideas-intro p { margin: 0; color: var(--text-3); font-size: 0.88rem; line-height: 1.55; }

/* MAPA — vista aérea por zona */
.map-container {
  display: flex; flex-direction: column;
  gap: 18px;
  max-width: 720px;
  margin: 0 auto;
}
.map-figure {
  margin: 0;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(9, 9, 11, 0.05);
}
.map-photo {
  display: block;
  width: 100%;
  height: auto;
  cursor: zoom-in;
  background: var(--bg-soft);
}
.map-figure figcaption {
  padding: 10px 14px;
  font-size: 0.85rem;
  color: var(--text-3);
  border-top: 1px solid var(--border-soft);
  line-height: 1.4;
}
.map-empty {
  text-align: center;
  padding: 60px 24px;
  color: var(--text-3);
  font-size: 0.95rem;
}

/* HUERTA CARD */
.huerta-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-top: 3px solid var(--accent);
  border-radius: var(--r-lg);
  padding: 20px; box-shadow: none;
  transition: all var(--t);
}
.huerta-card:hover { box-shadow: var(--shadow-sm); }
.huerta-header { margin-bottom: 8px; }
.huerta-title {
  font-family: inherit; font-size: 1.05rem;
  font-weight: 600; margin: 0 0 2px;
  color: var(--text); letter-spacing: -0.01em;
}
.huerta-sci { font-style: italic; color: var(--text-3); font-size: 0.82rem; }
.huerta-type { font-size: 0.78rem; color: var(--text-3); margin-bottom: 8px; }
.huerta-tags { display: flex; gap: 4px; flex-wrap: wrap; margin: 8px 0; }
.huerta-tip {
  font-size: 0.85rem;
  background: var(--bg-soft);
  border: 1px solid var(--border-soft);
  padding: 10px 12px; border-radius: var(--r-md);
  margin: 12px 0; color: var(--text-2);
  line-height: 1.5;
}
.huerta-meta {
  display: flex; flex-wrap: wrap; gap: 16px;
  font-size: 0.8rem; color: var(--text-3);
  margin: 12px 0;
}
.hcal { margin-top: 14px; }
.hbar {
  display: grid; grid-template-columns: 100px 1fr;
  gap: 8px; margin-bottom: 4px; align-items: center;
}
.hbar-label { font-size: 0.72rem; font-weight: 500; color: var(--text-3); }
.hbar-cells { display: grid; grid-template-columns: repeat(12, 1fr); gap: 2px; }
.hcell {
  font-size: 0.62rem; text-align: center;
  padding: 4px 0; background: var(--bg-soft);
  color: var(--text-muted); border-radius: var(--r-sm);
  font-weight: 500; text-transform: lowercase;
}
.hcell.active { background: var(--c, var(--accent)); color: white; font-weight: 600; }

/* HUERTA LOCATIONS */
.hloc-intro { margin-bottom: 24px; }
.hloc-intro h3 {
  font-family: inherit; color: var(--text);
  margin: 0 0 6px; font-size: 1.1rem;
  font-weight: 600; letter-spacing: -0.01em;
}
.hloc-intro p { color: var(--text-3); margin: 0; font-size: 0.9rem; }
.hloc-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px; margin-bottom: 40px;
}
.hloc-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-top: 3px solid var(--text);
  border-radius: var(--r-lg);
  padding: 18px 20px; box-shadow: none;
  transition: all var(--t);
}
.hloc-card:hover { box-shadow: var(--shadow-sm); }
.hloc-title {
  font-family: inherit; font-size: 1rem;
  margin: 0 0 10px; color: var(--text);
  font-weight: 600; letter-spacing: -0.01em;
}
.hloc-desc { font-size: 0.85rem; margin-bottom: 12px; color: var(--text-2); line-height: 1.55; }
.hloc-pros, .hloc-cons, .hloc-best {
  font-size: 0.8rem; margin: 6px 0;
  padding: 8px 10px; border-radius: var(--r-md);
  line-height: 1.5;
}
.hloc-pros { background: var(--green-soft); color: var(--accent-text); }
.hloc-cons { background: var(--orange-soft); color: #9a3412; }
.hloc-best { background: var(--blue-soft); color: #1e40af; }
.huerta-list-title {
  font-family: inherit; color: var(--text);
  margin: 40px 0 6px; font-size: 1.5rem;
  font-weight: 700; letter-spacing: -0.02em;
  border-top: 1px solid var(--border);
  padding-top: 32px;
}
.huerta-list-intro {
  color: var(--text-3); font-style: normal;
  margin-bottom: 24px; font-size: 0.9rem;
}
.frente-huerta-intro {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--text);
  padding: 18px 22px;
  margin-bottom: 28px;
  border-radius: var(--r-md);
}
.frente-huerta-intro h3 {
  font-family: inherit; margin: 0 0 4px;
  color: var(--text); font-size: 1.05rem; font-weight: 600;
}
.frente-huerta-intro p { margin: 0; color: var(--text-3); font-size: 0.88rem; }

/* CALENDAR */
.cal-legend {
  display: flex; gap: 16px; flex-wrap: wrap;
  font-size: 0.85rem; margin-bottom: 16px;
  color: var(--text-3);
}
.cal-wrap {
  overflow-x: auto;
  background: var(--bg-card);
  border-radius: var(--r-lg);
  padding: 16px; box-shadow: none;
  border: 1px solid var(--border);
}
.cal-table {
  width: 100%; border-collapse: separate;
  border-spacing: 2px; min-width: 800px;
}
.cal-table th {
  font-family: inherit; font-size: 0.72rem;
  font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.06em; color: var(--text-3);
  padding: 6px 4px; text-align: center;
}
.cal-name-h { text-align: left !important; min-width: 180px; }
.cal-name {
  font-size: 0.85rem; font-weight: 500;
  padding: 8px 12px; background: var(--bg-soft);
  border-radius: var(--r-sm); white-space: nowrap;
  color: var(--text);
}
.cal-codes {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 0.68rem; color: var(--text-3); font-weight: 400;
}
.cal-cell {
  background: var(--bg-soft); border-radius: var(--r-sm);
  text-align: center; height: 32px; vertical-align: middle;
  font-size: 0.85rem; position: relative;
  transition: background var(--t);
}
.cal-cell.flor { background: #fce7f3; }
.cal-cell.fruta { background: #fed7aa; }
.cal-cell.poda { background: #e0e7ff; color: var(--text); }
.cal-cell.flor.fruta { background: #fbcfe8; }
.cal-cell.flor.poda { background: #fce7f3; }
.cal-cell.fruta.poda { background: #fed7aa; }
.cal-cell.flor.fruta.poda { background: #fed7aa; }

/* LIGHTBOX */
.lightbox {
  display: none; position: fixed; inset: 0;
  background: rgba(9, 9, 11, 0.95);
  z-index: 1000; align-items: center;
  justify-content: center; cursor: zoom-out; padding: 24px;
}
.lightbox.active { display: flex; }
.lightbox img {
  max-width: 95vw; max-height: 95vh;
  object-fit: contain; border-radius: var(--r-md);
}

/* TIMELINE */
.timeline-header {
  display: flex; flex-direction: column;
  gap: 10px; margin-bottom: 12px;
}
.timeline-intro {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--text);
  padding: 12px 16px; border-radius: var(--r-md);
}
.timeline-intro h3 {
  font-family: inherit; margin: 0 0 2px;
  color: var(--text); font-size: 1.02rem;
  font-weight: 600; letter-spacing: -0.01em;
}
.timeline-intro p { margin: 0; color: var(--text-3); font-size: 0.85rem; line-height: 1.45; }
.timeline-controls {
  display: flex; justify-content: space-between;
  flex-wrap: nowrap; gap: 8px; align-items: center;
  min-width: 0;
}
/* TIMELINE FILTERS — chips horizontal scroll (queda como estaba) */
.filter-tags.timeline-filters {
  display: flex; gap: 6px;
  flex-wrap: nowrap;
  overflow-x: auto;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
  padding: 2px 0;
  scroll-snap-type: x proximity;
  flex: 1 1 auto; min-width: 0;
}
.filter-tags.timeline-filters::-webkit-scrollbar { display: none; }
.filter-tags.timeline-filters .ftag { flex: 0 0 auto; scroll-snap-align: start; }
.btn-contacts {
  background: var(--bg-card);
  border: 1px solid var(--border-strong);
  padding: 7px 12px;
  font-size: 0.82rem; font-weight: 600;
  cursor: pointer; border-radius: var(--r-full);
  color: var(--text-2); transition: all var(--t);
  white-space: nowrap;
  flex: 0 0 auto;
}
.btn-contacts:hover {
  background: var(--text); color: white; border-color: var(--text);
}
.btn-settings {
  background: var(--bg-card);
  border: 1px solid var(--border-strong);
  padding: 7px 10px;
  font-size: 1rem;
  cursor: pointer; border-radius: var(--r-full);
  color: var(--text-2); transition: all var(--t);
  flex: 0 0 auto;
  line-height: 1;
}
.btn-settings:hover {
  background: var(--text); color: white; border-color: var(--text);
}

/* TIMELINE — botón "+ Nueva tarea" arriba del feed */
.timeline-actions {
  display: flex; justify-content: flex-end;
  margin-bottom: 2px;
}
.btn-create-task {
  background: var(--text);
  color: white;
  border: 1px solid var(--text);
  padding: 9px 16px;
  font-size: 0.92rem; font-weight: 600;
  cursor: pointer; border-radius: var(--r-full);
  transition: all var(--t);
  letter-spacing: -0.005em;
  flex: 0 0 auto;
}
.btn-create-task:hover {
  filter: brightness(1.15);
  transform: translateY(-1px);
}
.btn-create-task:active {
  transform: translateY(0);
}

/* SPECIES MODAL — botones de acción "Hacer pregunta" / "Sumar foto" */
.species-actions {
  display: flex; gap: 8px;
  flex-wrap: wrap;
  margin: 8px 0;
}
.species-action-btn {
  flex: 1 1 auto;
  min-width: 140px;
  background: var(--bg-card);
  border: 1px solid var(--border-strong);
  color: var(--text);
  padding: 10px 14px;
  font-size: 0.92rem; font-weight: 600;
  border-radius: var(--r-md);
  cursor: pointer;
  transition: all var(--t);
}
.species-action-btn:hover {
  background: var(--text); color: white; border-color: var(--text);
  transform: translateY(-1px);
}
.species-action-btn:active { transform: translateY(0); }

/* TASK CARD — badges de origen + bloque de respuesta IA para preguntas */
.task-origin-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  font-size: 0.72rem;
  font-weight: 600;
  border-radius: var(--r-full);
  letter-spacing: -0.005em;
}
.task-origin-badge.user {
  background: rgba(99, 102, 241, 0.12);
  color: #4f46e5;
  border: 1px solid rgba(79, 70, 229, 0.25);
}
.task-origin-badge.question {
  background: rgba(217, 119, 6, 0.12);
  color: #b45309;
  border: 1px solid rgba(180, 83, 9, 0.25);
}
.task-answer-block {
  margin: 8px 0;
  padding: 10px 12px;
  background: rgba(34, 197, 94, 0.08);
  border-left: 3px solid #16a34a;
  border-radius: var(--r-md);
  font-size: 0.88rem;
  line-height: 1.5;
  color: var(--text);
}
.task-answer-head {
  font-weight: 600;
  font-size: 0.78rem;
  color: #15803d;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 4px;
}
.task-answer-pending {
  margin: 8px 0;
  padding: 8px 10px;
  background: var(--bg-soft);
  border-left: 3px solid var(--border-strong);
  border-radius: var(--r-md);
  font-size: 0.82rem;
  color: var(--text-2);
}
.task-answer-pending code {
  background: rgba(0, 0, 0, 0.06);
  padding: 1px 5px;
  border-radius: 3px;
  font-size: 0.78rem;
}

/* COMPOSE MODAL — sección de foto opcional */
.compose-photo-section {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--border-soft);
}
.compose-plant-row {
  margin-bottom: 14px;
}

/* SETTINGS MODAL */
.settings-intro {
  font-size: 0.85rem; color: var(--text-2);
  background: var(--bg-soft);
  border-left: 3px solid var(--border-strong);
  padding: 10px 12px;
  border-radius: var(--r-md);
  margin-bottom: 16px;
}
.settings-section {
  margin-bottom: 22px;
  padding-bottom: 18px;
  border-bottom: 1px solid var(--border-soft);
}
.settings-section:last-of-type {
  border-bottom: none;
  padding-bottom: 0;
}
.settings-label {
  display: flex; flex-direction: column; gap: 4px;
  margin-bottom: 8px;
}
.settings-label strong {
  font-size: 0.92rem;
  color: var(--text);
}
.settings-hint {
  font-size: 0.78rem; color: var(--text-3);
  font-weight: 400;
  line-height: 1.4;
}
.settings-input {
  width: 100%;
  padding: 9px 12px;
  font-size: 0.9rem;
  font-family: monospace;
  border: 1px solid var(--border-strong);
  border-radius: var(--r-md);
  background: var(--bg);
  color: var(--text);
  box-sizing: border-box;
}
.settings-input:focus {
  outline: none;
  border-color: var(--text);
}
.settings-details {
  margin-top: 8px;
  font-size: 0.8rem;
  color: var(--text-2);
}
.settings-details summary {
  cursor: pointer;
  user-select: none;
  padding: 4px 0;
  color: var(--text-3);
}
.settings-details summary:hover { color: var(--text); }
.settings-steps {
  margin: 8px 0 0 0;
  padding-left: 24px;
  line-height: 1.5;
}
.settings-steps code {
  background: var(--bg-soft);
  padding: 1px 5px;
  border-radius: 3px;
  font-size: 0.78rem;
}
.settings-steps a {
  color: var(--text);
  text-decoration: underline;
}
.settings-actions {
  display: flex; gap: 8px;
  margin-top: 10px;
  flex-wrap: wrap;
}
.settings-actions .btn-secondary {
  flex: 1 1 auto;
}
.btn-secondary.btn-danger {
  flex: 0 0 auto;
}
.settings-feedback {
  margin-top: 10px;
  padding: 8px 12px;
  font-size: 0.85rem;
  border-radius: var(--r-md);
  min-height: 1.5em;
  background: transparent;
}
.settings-feedback:empty {
  display: none;
}
.settings-feedback.ok {
  background: rgba(34, 197, 94, 0.12);
  color: #166534;
}
.settings-feedback.err {
  background: rgba(239, 68, 68, 0.12);
  color: #991b1b;
}
.settings-feedback.warn {
  background: rgba(245, 158, 11, 0.12);
  color: #92400e;
}
.settings-footer {
  display: flex; justify-content: flex-end;
  margin-top: 18px;
}

/* TRANSFER LINK SECTION */
#transfer-link-output {
  margin-top: 12px;
}
.transfer-warn {
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid rgba(245, 158, 11, 0.4);
  border-radius: var(--r-md);
  padding: 10px 12px;
  font-size: 0.82rem;
  color: #92400e;
  line-height: 1.4;
  margin-bottom: 10px;
}
.transfer-qr-wrap {
  display: flex; flex-direction: column;
  align-items: center; gap: 6px;
  padding: 14px;
  background: white;
  border-radius: var(--r-md);
  margin-bottom: 12px;
}
#transfer-qr {
  display: flex; justify-content: center;
}
#transfer-qr svg {
  width: 280px; height: 280px;
  max-width: 100%;
  display: block;
}
.transfer-qr-hint {
  font-size: 0.78rem;
  color: var(--text-3);
  margin: 0;
  text-align: center;
}
.transfer-qr-error {
  font-size: 0.85rem;
  color: #991b1b;
  background: rgba(239, 68, 68, 0.08);
  border: 1px solid rgba(239, 68, 68, 0.25);
  border-radius: var(--r-md);
  padding: 12px;
}
.transfer-or {
  text-align: center;
  font-size: 0.78rem;
  color: var(--text-3);
  margin: 8px 0 6px;
  letter-spacing: 0.04em;
}
#transfer-link-text {
  width: 100%;
  font-family: monospace;
  font-size: 0.78rem;
  padding: 9px 12px;
  border: 1px solid var(--border-strong);
  border-radius: var(--r-md);
  background: var(--bg);
  color: var(--text);
  resize: vertical;
  word-break: break-all;
  box-sizing: border-box;
  margin-bottom: 8px;
}
.transfer-actions {
  display: flex; gap: 8px;
  margin-bottom: 8px;
}
.transfer-actions .btn-secondary { flex: 1 1 auto; }
.transfer-hint {
  font-size: 0.78rem;
  color: var(--text-3);
  line-height: 1.4;
}

/* Visually hidden — para inputs file que se disparan vía <label>.
   En mobile (iOS Safari + Android Chrome), `hidden` o `display:none`
   bloquea el dispatch del click hacia el input, por eso necesita
   estar en el flujo del DOM pero invisible. */
.visually-hidden {
  position: absolute !important;
  width: 1px; height: 1px;
  padding: 0; margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
  opacity: 0;
}

/* TASK PHOTO MODAL — captura + preview + upload */
.task-photo-name {
  font-size: 0.85rem;
  color: var(--text-2);
  background: var(--bg-soft);
  padding: 8px 12px;
  border-radius: var(--r-md);
  margin: 0 0 16px;
}
.task-photo-warning {
  font-size: 0.88rem;
  color: #92400e;
  background: rgba(245, 158, 11, 0.12);
  padding: 12px 14px;
  border-radius: var(--r-md);
  margin-bottom: 14px;
  line-height: 1.4;
}
.task-photo-buttons {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
@media (max-width: 480px) {
  .task-photo-buttons { grid-template-columns: 1fr; }
}
.task-photo-btn {
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 8px;
  padding: 28px 14px;
  border: 2px dashed var(--border-strong);
  border-radius: var(--r-lg);
  background: var(--bg-soft);
  cursor: pointer;
  transition: all var(--t);
}
.task-photo-btn:hover {
  background: var(--bg-card);
  border-color: var(--text);
}
.task-photo-btn-emoji {
  font-size: 2rem;
  line-height: 1;
}
.task-photo-btn-label {
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--text);
}
.task-photo-preview-wrap {
  background: var(--bg);
  border-radius: var(--r-md);
  overflow: hidden;
  text-align: center;
  margin-bottom: 12px;
}
#task-photo-canvas {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}
.task-photo-overlay-note {
  font-size: 0.78rem;
  color: var(--text-3);
  text-align: center;
  margin: 0 0 12px;
  line-height: 1.4;
}
.task-photo-actions {
  display: flex; gap: 10px;
}
.task-photo-actions > button { flex: 1 1 auto; }
.task-photo-uploading {
  text-align: center;
  font-size: 0.95rem;
  color: var(--text-2);
  padding: 32px 16px;
}
.task-photo-success {
  background: rgba(34, 197, 94, 0.08);
  border: 1px solid rgba(34, 197, 94, 0.25);
  border-radius: var(--r-lg);
  padding: 16px;
  margin-bottom: 14px;
}
.task-photo-success-title {
  font-size: 1rem; font-weight: 700;
  color: #166534;
  margin-bottom: 6px;
}
.task-photo-success p {
  font-size: 0.88rem;
  color: var(--text-2);
  margin: 6px 0;
  line-height: 1.5;
}
.task-photo-success-hint { color: var(--text-3); }
.task-photo-success-cmd {
  display: inline-block;
  background: var(--text);
  color: white;
  padding: 4px 10px;
  border-radius: var(--r-md);
  font-family: monospace;
  font-size: 0.88rem;
  font-weight: 600;
  margin: 4px 0;
}
.task-photo-success-link a {
  color: var(--text);
  text-decoration: underline;
  font-size: 0.85rem;
}
.task-photo-error {
  background: rgba(239, 68, 68, 0.08);
  border: 1px solid rgba(239, 68, 68, 0.25);
  border-radius: var(--r-lg);
  padding: 16px;
  margin-bottom: 14px;
}
.task-photo-error-title {
  font-size: 1rem; font-weight: 700;
  color: #991b1b;
  margin-bottom: 6px;
}
.task-photo-error p {
  font-size: 0.88rem;
  color: var(--text-2);
  margin: 0;
  word-break: break-word;
}

/* Botón "📷 Subir foto" en task-actions */
.task-btn-photo {
  background: rgba(99, 102, 241, 0.1);
  border-color: rgba(99, 102, 241, 0.3);
  color: #4338ca;
}
.task-btn-photo:hover {
  background: rgba(99, 102, 241, 0.2);
  border-color: rgba(99, 102, 241, 0.5);
}
/* Botón "💬 Responder" — variante violeta clara */
.task-btn-text {
  background: rgba(168, 85, 247, 0.1);
  border-color: rgba(168, 85, 247, 0.3);
  color: #7e22ce;
}
.task-btn-text:hover {
  background: rgba(168, 85, 247, 0.2);
  border-color: rgba(168, 85, 247, 0.5);
}

/* SPECIES DETAIL MODAL — estilo "Memories" con hero a sangre */
.species-modal {
  padding: 0;
}
.species-modal-content {
  padding: 0 !important;
  max-width: 520px !important;
  border-radius: 20px;
  overflow: hidden;
}
@media (max-width: 640px) {
  .species-modal-content {
    max-width: 100% !important;
    width: 100% !important;
    height: 100vh;
    max-height: 100vh;
    border-radius: 0;
  }
}

/* Hero con foto a sangre + overlay degradado + nombre grande */
.species-hero {
  position: relative;
  background-size: cover;
  background-position: center;
  background-color: #1a1a1a;
  height: 360px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 24px 22px;
}
@media (max-width: 640px) {
  .species-hero {
    height: 52vh;
    min-height: 320px;
  }
}
.species-hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.3) 0%,
    rgba(0, 0, 0, 0.05) 38%,
    rgba(0, 0, 0, 0.6) 100%
  );
  pointer-events: none;
}
.species-hero-fallback {
  background: linear-gradient(135deg, #2d3a4f 0%, #1a1a1a 100%);
}
.species-hero-overlay {
  position: relative;
  z-index: 1;
  text-align: center;
}
.species-hero-name {
  font-family: 'Anton', 'Inter', system-ui, sans-serif;
  font-weight: 400;
  font-size: clamp(2rem, 8vw, 3.4rem);
  letter-spacing: 0.05em;
  color: white;
  text-transform: uppercase;
  margin: 0 0 8px;
  line-height: 1.05;
  text-shadow: 0 2px 14px rgba(0, 0, 0, 0.5);
  text-wrap: balance;
}
.species-hero-sci {
  font-style: italic;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.88);
  margin-bottom: 10px;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.6);
}
.species-hero-meta {
  display: flex;
  gap: 6px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 12px;
}
.species-hero-chip {
  display: inline-block;
  background: rgba(255, 255, 255, 0.18);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  color: white;
  font-size: 0.74rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 999px;
  letter-spacing: 0.04em;
}
.species-hero-location {
  font-size: 0.86rem;
  color: rgba(255, 255, 255, 0.92);
  line-height: 1.45;
  margin: 4px auto 10px;
  max-width: 90%;
  text-align: center;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.6);
  text-wrap: balance;
}
.species-hero-tags {
  display: flex;
  gap: 5px;
  justify-content: center;
  flex-wrap: wrap;
}
.species-hero-tags .species-tag-chip {
  background: rgba(255, 255, 255, 0.16);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  color: white;
  font-size: 0.7rem;
  letter-spacing: 0.02em;
}
.species-hero-close {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 2;
  background: rgba(0, 0, 0, 0.45);
  border: none;
  color: white;
  width: 36px; height: 36px;
  border-radius: 50%;
  font-size: 1.05rem;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  transition: background var(--t);
}
.species-hero-close:hover {
  background: rgba(0, 0, 0, 0.7);
}

/* Sección de fotos debajo del hero — grid edge-to-edge */
.species-section-photos {
  border-bottom: 1px solid var(--border-soft);
  padding-bottom: 0;
}
.species-section-label {
  font-size: 0.74rem;
  font-weight: 700;
  color: var(--text-3);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 10px 22px 6px;
  margin: 0;
}

/* Photos grid: 3 columnas, square, sin radius (edge-to-edge), gap mínimo */
.species-photos-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2px;
  padding: 0;
}
.species-photo-cell {
  position: relative;
  aspect-ratio: 1 / 1;
  overflow: hidden;
  cursor: pointer;
  background: var(--bg-soft);
  transition: transform 0.15s ease;
}
.species-photo-cell:active {
  transform: scale(0.97);
}
.species-photo-cell img {
  width: 100%; height: 100%;
  object-fit: cover;
  display: block;
}
.species-photo-cell.add {
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 4px;
  background: var(--bg-soft);
  outline: 2px dashed var(--border-strong);
  outline-offset: -8px;
}
.species-photo-cell.add:hover {
  outline-color: var(--text);
  background: var(--bg);
}
.species-add-plus {
  font-size: 2rem;
  font-weight: 300;
  color: var(--text-3);
  line-height: 1;
}
.species-add-label {
  font-size: 0.72rem;
  color: var(--text-3);
  font-weight: 600;
}

/* Detalles collapsable */
.species-details {
  border-top: 1px solid var(--border-soft);
}
.species-details-summary {
  padding: 16px 22px;
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--text);
  cursor: pointer;
  user-select: none;
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  text-align: center;
}
.species-details-summary::-webkit-details-marker { display: none; }
.species-details-summary::before {
  content: '▸';
  display: inline-block;
  transition: transform var(--t);
  color: var(--text-3);
}
.species-details[open] .species-details-summary::before {
  transform: rotate(90deg);
}
.species-details-body {
  padding: 0 22px 22px;
}

/* Tags / charrua / desc / funfact / care / tasks (re-skin para el details) */
.species-tags {
  display: flex; flex-wrap: wrap; gap: 6px;
}
.species-tag-chip {
  font-size: 0.72rem;
  font-weight: 600;
  background: var(--bg-soft);
  color: var(--text-2);
  padding: 3px 8px;
  border-radius: 999px;
}
.species-charrua {
  font-size: 0.85rem;
  color: var(--text-2);
  margin-bottom: 8px;
}
.species-desc {
  font-size: 0.92rem;
  color: var(--text);
  line-height: 1.5;
  margin: 8px 0;
}
.species-detail-other {
  font-size: 0.82rem;
  color: var(--text-3);
  margin: 4px 0 8px;
}
.species-funfact {
  background: var(--bg-soft);
  border-left: 3px solid var(--border-strong);
  padding: 8px 12px;
  border-radius: var(--r-md);
  font-size: 0.85rem;
  color: var(--text-2);
  margin: 8px 0;
}

/* CURIOSIDADES — feed de fun_facts (sub-tab promovida desde proposal 12/06) */
.curio-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 340px), 1fr));
  gap: 16px;
  min-width: 0;
}
.curio-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 14px 16px 16px;
  box-shadow: 0 1px 2px rgba(9, 9, 11, 0.04), 0 1px 3px rgba(9, 9, 11, 0.05);
  transition:
    border-color 200ms cubic-bezier(0.16, 1, 0.3, 1),
    transform 250ms cubic-bezier(0.16, 1, 0.3, 1),
    box-shadow 250ms cubic-bezier(0.16, 1, 0.3, 1);
}
.curio-card:hover {
  border-color: var(--border-strong);
  transform: translateY(-3px);
  box-shadow: 0 4px 8px rgba(9, 9, 11, 0.06), 0 16px 36px rgba(9, 9, 11, 0.08);
}
.curio-head {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}
.curio-thumb {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  object-fit: cover;
  background: var(--bg-soft);
  flex: none;
}
.curio-thumb-empty {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
}
.curio-titles { min-width: 0; }
.curio-name {
  margin: 0;
  font-size: 1.02rem;
  line-height: 1.2;
  color: var(--text-1);
}
.curio-sci {
  font-style: italic;
  font-size: 0.8rem;
  color: var(--text-2);
  margin-top: 2px;
}
.curio-fact {
  margin: 12px 0 0;
  font-size: 0.9rem;
  line-height: 1.5;
  color: var(--text-2);
}
.curio-empty {
  color: var(--text-2);
  padding: 12px 4px;
}
.species-care {
  display: grid; gap: 6px;
  padding-top: 12px;
  margin-top: 12px;
  border-top: 1px solid var(--border-soft);
}
.species-care-row {
  display: grid;
  grid-template-columns: 28px 110px 1fr;
  gap: 10px;
  align-items: baseline;
  font-size: 0.84rem;
  line-height: 1.4;
}
@media (max-width: 480px) {
  .species-care-row {
    grid-template-columns: 28px 1fr;
  }
  .species-care-label { display: none; }
}
.species-care-icon { font-size: 1rem; }
.species-care-label {
  font-weight: 600;
  color: var(--text-2);
}
.species-care-val { color: var(--text); }
.species-tasks {
  padding-top: 12px;
  margin-top: 12px;
  border-top: 1px solid var(--border-soft);
}
.species-tasks h4 {
  font-size: 0.92rem;
  font-weight: 700;
  margin: 0 0 8px;
  color: var(--text);
}
.species-task-row {
  display: flex; align-items: center; gap: 8px;
  padding: 6px 0;
  font-size: 0.82rem;
  border-bottom: 1px dashed var(--border-soft);
}
.species-task-row:last-child { border-bottom: none; }
.species-task-chip {
  flex: 0 0 auto;
  font-size: 0.66rem;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 999px;
  letter-spacing: 0.02em;
}
.species-task-chip.active { background: rgba(245, 158, 11, 0.18); color: #92400e; }
.species-task-chip.done { background: rgba(34, 197, 94, 0.18); color: #166534; }
.species-task-chip.snoozed { background: rgba(99, 102, 241, 0.18); color: #4338ca; }
.species-task-title {
  flex: 1 1 auto;
  color: var(--text);
  font-weight: 500;
}
.species-task-when {
  flex: 0 0 auto;
  color: var(--text-3);
  font-size: 0.74rem;
  white-space: nowrap;
}

/* Banner de IA refresh — aparece cuando /actualizar-tareas hizo description_override */
.task-ai-banner {
  background: rgba(245, 158, 11, 0.10);
  border: 1px solid rgba(245, 158, 11, 0.35);
  border-radius: var(--r-md);
  padding: 8px 11px;
  margin: 8px 4px 0;
  text-align: left;
}
.task-ai-banner-head {
  font-size: 0.74rem;
  font-weight: 700;
  color: #92400e;
  letter-spacing: 0.02em;
  margin-bottom: 4px;
}
.task-ai-banner-body {
  font-size: 0.86rem;
  color: var(--text);
  line-height: 1.4;
}

/* Summary IA en tareas done por IA */
.task-ai-summary {
  display: flex; align-items: flex-start; gap: 8px;
  background: rgba(34, 197, 94, 0.08);
  border: 1px solid rgba(34, 197, 94, 0.25);
  border-radius: var(--r-md);
  padding: 7px 10px;
  margin: 6px 4px 0;
  font-size: 0.84rem;
  line-height: 1.4;
  text-align: left;
}
.task-ai-summary-tag {
  font-size: 0.72rem;
  font-weight: 700;
  color: #166534;
  white-space: nowrap;
  flex: 0 0 auto;
}
.task-ai-summary-text {
  color: var(--text-2);
  flex: 1 1 auto;
}

/* SYNC STATUS BAR — arriba del Timeline, abajo del header */
.sync-status-bar {
  display: flex; align-items: center; gap: 10px;
  margin: 4px auto 12px;
  max-width: 460px;
  padding: 6px 12px;
  font-size: 0.78rem;
  border-radius: var(--r-full);
  background: var(--bg-soft);
  border: 1px solid var(--border-soft);
  color: var(--text-2);
}
.sync-status-bar .sync-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  flex: 0 0 auto;
  background: var(--text-3);
}
.sync-status-bar[data-state="ok"] .sync-dot { background: #22c55e; }
.sync-status-bar[data-state="syncing"] .sync-dot {
  background: #eab308;
  animation: sync-pulse 1.2s ease-in-out infinite;
}
.sync-status-bar[data-state="pending"] .sync-dot { background: #eab308; }
.sync-status-bar[data-state="error"] .sync-dot { background: #ef4444; }
.sync-status-bar[data-state="disabled"] .sync-dot { background: var(--text-3); }
@keyframes sync-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}
.sync-status-bar .sync-label {
  flex: 1 1 auto;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.sync-retry-btn {
  flex: 0 0 auto;
  background: transparent;
  border: 1px solid var(--border-strong);
  border-radius: var(--r-full);
  padding: 2px 10px;
  font-size: 0.74rem;
  font-weight: 600;
  color: var(--text);
  cursor: pointer;
}
.sync-retry-btn:hover {
  background: var(--text);
  color: white;
  border-color: var(--text);
}

/* Timeline summary — bloque informativo flat en una sola línea (estilo weather) */
.timeline-summary {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  width: auto;
  max-width: 460px;
  margin: 0 auto 12px;
  padding: 6px 12px;
  background: transparent;
  border: none;
  border-radius: 0;
  box-shadow: none;
  font-size: 0.78rem;
  color: var(--text-3);
  gap: 14px;
  white-space: nowrap;
  overflow: visible;
}
.timeline-summary .summary-cell {
  display: inline-flex; align-items: center;
  gap: 4px;
  flex: 0 0 auto;
  line-height: 1.2;
}
.timeline-summary .summary-cell strong {
  color: var(--text);
  font-weight: 700;
  font-feature-settings: 'tnum';
  font-size: 0.92rem;
}
.timeline-feed {
  display: flex; flex-direction: column;
  gap: 12px; max-width: 720px; margin: 0 auto;
}

/* Separadores de mes dentro del feed (atrasadas / mayo 2026 / junio 2026 / ...) */
.month-header {
  display: flex; align-items: baseline; justify-content: space-between;
  gap: 10px;
  margin: 18px 4px 2px;
  padding: 10px 0 8px;
  font-size: 0.78rem; font-weight: 700;
  color: var(--text-2);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border-top: 1px solid var(--border-soft);
}
.month-header:first-child {
  margin-top: 0;
  padding-top: 0;
  border-top: none;
}
.month-header.overdue {
  color: #b91c1c;
  border-top-color: rgba(185, 28, 28, 0.25);
}
.month-header.overdue .month-count {
  background: rgba(185, 28, 28, 0.12);
  color: #b91c1c;
}
.month-header .month-label { line-height: 1; }
.month-header .month-count {
  font-size: 0.7rem;
  font-weight: 600;
  color: var(--text-3);
  background: var(--bg-soft);
  padding: 2px 8px;
  border-radius: var(--r-full);
  letter-spacing: 0;
  text-transform: none;
  font-feature-settings: 'tnum';
}

/* ---- Tareas futuras (módulo colapsable) ---- */
.future-tasks {
  margin: 24px 0 8px;
  border: 1px dashed var(--border-soft);
  border-radius: var(--r-lg);
  background: var(--bg-soft);
  overflow: hidden;
}
.future-tasks-summary {
  display: flex; align-items: center; gap: 10px;
  padding: 14px 16px;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-2);
  list-style: none;
  user-select: none;
  -webkit-user-select: none;
}
.future-tasks-summary::-webkit-details-marker { display: none; }
.future-tasks-summary::marker { content: ''; }
.future-tasks-label { flex: 1; }
.future-tasks-count {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--text-3);
  background: var(--bg-card);
  padding: 2px 9px;
  border-radius: var(--r-full);
  font-feature-settings: 'tnum';
}
.future-tasks-chevron {
  transition: transform 0.2s ease;
  color: var(--text-3);
  font-size: 1rem;
}
.future-tasks[open] .future-tasks-chevron { transform: rotate(180deg); }
.future-tasks-body {
  padding: 0 14px 12px;
  background: var(--bg-card);
  border-top: 1px solid var(--border-soft);
}
.future-tasks-body .month-header:first-child { padding-top: 12px; }

.timeline-empty {
  text-align: center; padding: 80px 24px;
  background: var(--bg-card);
  border-radius: var(--r-lg);
  margin: 24px auto; max-width: 500px;
  border: 1px solid var(--border);
}
.timeline-empty .empty-icon { font-size: 3rem; margin-bottom: 12px; opacity: 0.5; }
.timeline-empty h3 {
  font-family: inherit; color: var(--text);
  margin: 0 0 6px; font-size: 1.15rem; font-weight: 600;
}
.timeline-empty p { color: var(--text-3); margin: 0; font-size: 0.9rem; }

/* TASK CARD — vertical hero, centrado y minimalista */
.task-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  box-shadow:
    0 1px 2px rgba(9, 9, 11, 0.04),
    0 1px 3px rgba(9, 9, 11, 0.05);
  position: relative;
  transition:
    border-color 200ms cubic-bezier(0.16, 1, 0.3, 1),
    box-shadow 250ms cubic-bezier(0.16, 1, 0.3, 1),
    transform 250ms cubic-bezier(0.16, 1, 0.3, 1);
  touch-action: pan-y;
  display: block;
  max-width: 100%;
}
.task-card:hover {
  border-color: var(--border-strong);
  box-shadow:
    0 4px 8px rgba(9, 9, 11, 0.05),
    0 12px 28px rgba(9, 9, 11, 0.07);
}
.task-card.swiping { transition: none; }
.task-card.swipe-out-right {
  transform: translateX(120%) rotate(6deg);
  opacity: 0; transition: transform 0.35s, opacity 0.35s;
}
.task-card.swipe-out-left {
  transform: translateX(-120%) rotate(-6deg);
  opacity: 0; transition: transform 0.35s, opacity 0.35s;
}
.task-card.completed { opacity: 0.65; background: var(--bg-soft); }
.task-card.snoozed { opacity: 0.85; background: var(--bg); }

/* Contenido principal */
.task-content-wrap {
  display: block;
  min-width: 0;
}

/* Priority dot — reemplaza la border-left-color y la priority-pill */
.task-priority-dot {
  position: absolute;
  top: 12px; right: 12px;
  width: 12px; height: 12px;
  border-radius: 50%;
  background: var(--text-muted);
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.92);
  z-index: 2;
  pointer-events: none;
}
.task-card.priority-alta .task-priority-dot { background: var(--red); }
.task-card.priority-media .task-priority-dot { background: var(--orange); }
.task-card.priority-baja .task-priority-dot { background: var(--green); }

/* Side hints — solo visibles durante swipe */
.task-side-hint {
  position: absolute;
  top: 0; bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 0 14px;
  color: var(--text-3);
  user-select: none;
  pointer-events: none;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.15s, color 0.15s, background 0.15s;
  z-index: 1;
}
.task-side-hint.left {
  left: 0;
  background: linear-gradient(90deg, rgba(244,244,245,0.95) 0%, rgba(244,244,245,0) 100%);
}
.task-side-hint.right {
  right: 0;
  background: linear-gradient(270deg, rgba(37,211,102,0.18) 0%, rgba(37,211,102,0) 100%);
}
.task-side-hint.right .hint-icon { color: var(--whatsapp); }
.task-side-hint.right .hint-icon svg { fill: var(--whatsapp); }
.task-side-hint .hint-arrow { font-size: 1.4rem; font-weight: 600; line-height: 1; }
.task-side-hint .hint-icon {
  font-size: 1.05rem; line-height: 1;
  display: inline-flex; align-items: center; justify-content: center;
}
.task-side-hint .hint-icon svg { width: 18px; height: 18px; display: block; }

/* Side hints solo aparecen mientras el dedo arrastra la card */
.task-card[data-dx-negative="true"] .task-side-hint.left { opacity: 1; color: var(--text); }
.task-card[data-dx-positive="true"] .task-side-hint.right { opacity: 1; color: var(--whatsapp); }

/* HEADER — foto hero arriba + meta centrado */
.task-header {
  display: flex; flex-direction: column;
  padding: 0; gap: 0;
  cursor: pointer;
  user-select: none;
}
.task-photo {
  width: 100%; height: 180px;
  object-fit: cover;
  background: var(--bg-soft);
  cursor: zoom-in;
  display: block;
  border-radius: 16px 16px 0 0;
}
.task-photo-placeholder {
  width: 100%; height: 140px;
  background: var(--bg-soft);
  display: flex; align-items: center; justify-content: center;
  font-size: 2.4rem;
  border-bottom: 1px solid var(--border-soft);
  border-radius: 16px 16px 0 0;
}

/* Meta centrado */
.task-meta {
  padding: 16px 18px 12px;
  display: flex; flex-direction: column;
  align-items: center;
  gap: 6px;
  text-align: center;
  min-width: 0;
}
.task-meta-top {
  display: flex; align-items: center; gap: 6px;
  flex-wrap: nowrap; justify-content: center;
  margin: 0;
  max-width: 100%;
}
.task-priority-pill { display: none; } /* lo representa el dot */
.task-zone-pill {
  background: var(--bg-soft); color: var(--text-3);
  padding: 3px 10px; border-radius: var(--r-full);
  font-size: 0.7rem;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  border: 1px solid var(--border-soft); font-weight: 500;
  white-space: nowrap;
}
.task-id-badge {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 0.65rem;
  color: var(--text-muted);
  background: transparent;
  border: 1px dashed var(--border-soft);
  padding: 2px 6px;
  border-radius: var(--r-sm);
  white-space: nowrap;
  letter-spacing: 0.02em;
  user-select: all;
  -webkit-user-select: all;
  cursor: text;
}
.task-status-pill {
  padding: 3px 10px; border-radius: var(--r-full);
  font-size: 0.7rem; font-weight: 600;
  white-space: nowrap;
}
.task-status-pill.done {
  background: var(--green-soft); color: var(--accent-text);
  border: 1px solid #bbf7d0;
}
.task-status-pill.snoozed {
  background: var(--bg-soft); color: var(--text-3);
  border: 1px solid var(--border);
}
.task-title {
  font-family: inherit; font-size: 1.1rem;
  font-weight: 600; color: var(--text);
  margin: 2px 0 0; line-height: 1.3;
  letter-spacing: -0.015em;
  text-align: center;
}
.task-plant {
  font-size: 0.85rem; color: var(--text-3);
  font-style: italic;
  text-align: center;
  margin: 0;
}
.task-short {
  font-size: 0.88rem; color: var(--text-2);
  text-align: center;
  margin: 6px 4px 0;
  line-height: 1.35;
  max-width: 60ch;
  margin-inline: auto;
}
.task-due {
  display: inline-flex; align-items: center; gap: 4px;
  margin: 4px auto 0;
  padding: 4px 10px;
  font-size: 0.78rem; color: var(--text-2);
  font-weight: 500;
  background: var(--bg-soft);
  border-radius: var(--r-full);
  border: 1px solid var(--border-soft);
  white-space: nowrap;
}
.task-due.overdue {
  color: #b91c1c; font-weight: 600;
  background: var(--red-soft);
  border-color: #fecaca;
}
.task-snoozed-until {
  display: block; margin-top: 2px;
  font-size: 0.75rem; color: var(--text-3);
  font-style: italic;
}
.task-expand-chevron {
  display: block;
  margin: 6px auto 0;
  font-size: 0.9rem;
  color: var(--text-muted);
  transition: transform 0.25s ease, color var(--t);
  user-select: none;
  line-height: 1;
}
.task-card:hover .task-expand-chevron { color: var(--text-3); }
.task-card.expanded .task-expand-chevron {
  transform: rotate(180deg);
  color: var(--text);
}

/* DETAIL — colapsable */
.task-detail {
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.3s ease, opacity 0.25s ease;
  background: var(--bg-soft);
  text-align: left;
}
.task-card.expanded .task-detail {
  max-height: 1200px;
  opacity: 1;
}
.task-detail-section {
  padding: 12px 16px;
  border-bottom: 1px solid var(--border-soft);
  text-align: left;
}
.task-detail-section:last-child { border-bottom: none; }
.task-detail-label {
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-3);
  font-weight: 600;
  margin-bottom: 4px;
}
.task-detail-text {
  font-size: 0.86rem;
  color: var(--text-2);
  line-height: 1.6;
}
.task-detail-text.task-howto { line-height: 1.7; }
.task-detail-text.task-howto strong {
  color: var(--text); font-weight: 600;
  display: inline-block; margin-top: 2px;
}
.task-detail-text.task-howto br + strong { margin-top: 8px; }

/* ACTIONS — grid 3-up, ancho completo, mismo size */
.task-actions {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(96px, 1fr));
  gap: 6px;
  padding: 10px 12px 14px;
  border-top: 1px solid var(--border-soft);
}
.task-actions:has(.task-btn:only-child) {
  grid-template-columns: minmax(0, 1fr);
}
.task-btn {
  width: 100%;
  padding: 9px 8px;
  font-size: 0.82rem; font-weight: 600;
  border: 1px solid var(--border-strong);
  border-radius: var(--r-md);
  cursor: pointer; transition: all var(--t);
  display: inline-flex; align-items: center;
  justify-content: center; gap: 5px;
  background: var(--bg-card); color: var(--text-2);
  white-space: nowrap;
  min-width: 0;
}
.task-btn:hover { background: var(--bg-soft); border-color: var(--text-3); }
.task-btn:active { transform: scale(0.97); }

.task-btn-done {
  background: var(--text); color: white; border-color: var(--text);
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.08),
    0 2px 6px rgba(0, 0, 0, 0.06);
}
.task-btn-done:hover {
  background: #18181b; border-color: #18181b; color: white;
  transform: translateY(-1px);
  box-shadow:
    0 2px 4px rgba(0, 0, 0, 0.1),
    0 6px 14px rgba(0, 0, 0, 0.12);
}
.task-btn-done:active { transform: translateY(0) scale(0.97); }

.task-btn-snooze {
  background: var(--bg-card);
  border-color: var(--border-strong);
  color: var(--text-2);
}

.task-btn-whatsapp {
  background: var(--bg-card);
  border-color: var(--whatsapp);
  color: var(--whatsapp);
}
.task-btn-whatsapp:hover {
  background: var(--whatsapp);
  border-color: var(--whatsapp);
  color: white;
}

.task-btn-undo {
  background: var(--bg-card);
  border-color: var(--border-strong);
  color: var(--text-2);
}

@media (max-width: 768px) {
  .task-photo { height: 160px; }
  .task-photo-placeholder { height: 120px; }
  .task-meta { padding: 14px 14px 10px; }
  .task-actions { padding: 8px 10px 12px; }
  .task-btn { padding: 9px 4px; font-size: 0.78rem; }
}

/* MODALS */
.modal {
  display: none; position: fixed; inset: 0;
  background: rgba(9, 9, 11, 0.55);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 2000; align-items: center;
  justify-content: center; padding: 20px;
}
.modal.active { display: flex; animation: fadeIn 0.2s ease; }
.modal-content {
  background: var(--bg-card);
  border-radius: 20px;
  padding: 28px;
  max-width: 460px; width: 100%;
  max-height: 90vh; overflow-y: auto;
  box-shadow:
    0 4px 16px rgba(0, 0, 0, 0.12),
    0 24px 64px rgba(0, 0, 0, 0.18);
  position: relative;
  border: 1px solid var(--border);
  animation: modalIn 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes modalIn {
  from {
    opacity: 0;
    transform: scale(0.96) translateY(8px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}
.modal-content.modal-wide { max-width: 600px; }
.modal-close {
  position: absolute; top: 14px; right: 14px;
  background: transparent;
  border: 1px solid var(--border);
  width: 32px; height: 32px;
  border-radius: var(--r-md);
  cursor: pointer; font-size: 0.9rem;
  color: var(--text-3);
  transition: all var(--t);
  display: inline-flex; align-items: center; justify-content: center;
}
.modal-close:hover {
  background: var(--text); color: white; border-color: var(--text);
}
.modal h3 {
  font-family: inherit; margin: 0 0 14px;
  color: var(--text); font-size: 1.2rem;
  font-weight: 700; letter-spacing: -0.02em;
}
.snooze-task-name, .whatsapp-task-name {
  background: var(--bg-soft);
  border: 1px solid var(--border-soft);
  padding: 10px 14px; border-radius: var(--r-md);
  font-size: 0.85rem; color: var(--text-2);
  margin-bottom: 18px; font-style: normal; font-weight: 500;
}
.snooze-options {
  display: grid; grid-template-columns: repeat(2, 1fr);
  gap: 8px; margin-bottom: 18px;
}
.snooze-opt {
  padding: 11px 12px; font-size: 0.88rem;
  cursor: pointer;
  border: 1px solid var(--border);
  background: var(--bg-card);
  border-radius: var(--r-md);
  transition: all var(--t);
  color: var(--text-2); font-weight: 500;
  text-align: center;
}
.snooze-opt:hover {
  background: var(--bg-soft); border-color: var(--text); color: var(--text);
}
.snooze-custom {
  border-top: 1px solid var(--border-soft);
  padding-top: 16px;
  display: flex; flex-direction: column; gap: 8px;
}
.snooze-custom label {
  font-size: 0.78rem; color: var(--text-3);
  font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.05em;
}
.snooze-custom input[type="date"] {
  padding: 10px 14px; font-size: 0.9rem;
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  background: var(--bg-card); color: var(--text);
  transition: border-color var(--t);
}
.snooze-custom input[type="date"]:focus {
  outline: none; border-color: var(--text);
}
.btn-primary {
  background: var(--text); color: white;
  border: 1px solid var(--text);
  padding: 10px 16px;
  font-size: 0.88rem; font-weight: 600;
  border-radius: var(--r-md);
  cursor: pointer; transition: all var(--t);
}
.btn-primary:hover { background: #18181b; border-color: #18181b; }
.btn-primary:disabled {
  opacity: 0.4; cursor: not-allowed;
  background: var(--text-muted); border-color: var(--text-muted);
}
.btn-primary.btn-wa { background: var(--whatsapp); border-color: var(--whatsapp); }
.btn-primary.btn-wa:hover { background: var(--whatsapp-hover); border-color: var(--whatsapp-hover); }
.btn-secondary {
  background: var(--bg-card); color: var(--text-2);
  border: 1px solid var(--border);
  padding: 10px 16px;
  font-size: 0.88rem; font-weight: 500;
  border-radius: var(--r-md);
  cursor: pointer; transition: all var(--t);
}
.btn-secondary:hover { background: var(--bg-soft); border-color: var(--border-strong); }
.btn-secondary.btn-danger {
  color: #991b1b;
  border-color: rgba(185, 28, 28, 0.25);
}
.btn-secondary.btn-danger:hover {
  background: rgba(185, 28, 28, 0.06);
  border-color: rgba(185, 28, 28, 0.5);
}
.whatsapp-section { margin-bottom: 18px; }
.whatsapp-label {
  display: block; font-size: 0.78rem;
  color: var(--text-3); font-weight: 600;
  margin-bottom: 8px;
  text-transform: uppercase; letter-spacing: 0.05em;
}
.whatsapp-contacts {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
  gap: 8px;
}
.wa-contact-btn {
  padding: 12px 8px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  cursor: pointer; transition: all var(--t);
  font-size: 0.82rem; color: var(--text-2);
  text-align: center;
}
.wa-contact-btn:hover { background: var(--bg-soft); border-color: var(--border-strong); }
.wa-contact-btn.active {
  background: var(--whatsapp); color: white;
  border-color: var(--whatsapp);
}
.wa-contact-icon { font-size: 1.3rem; display: block; margin-bottom: 4px; }
.wa-contact-name { font-size: 0.76rem; line-height: 1.3; font-weight: 500; }
.wa-contact-noPhone {
  color: var(--red); font-size: 0.66rem;
  display: block; margin-top: 2px; font-weight: 500;
}
.whatsapp-message {
  width: 100%; padding: 12px 14px;
  font-size: 0.9rem;
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  resize: vertical; line-height: 1.5;
  background: var(--bg-card); color: var(--text);
  transition: border-color var(--t);
  font-family: inherit;
}
.whatsapp-message:focus { outline: none; border-color: var(--text); }
.whatsapp-actions { display: flex; justify-content: flex-end; }
.contacts-intro {
  font-size: 0.85rem; color: var(--text-3);
  margin-bottom: 16px; line-height: 1.55;
}
.contact-row {
  background: var(--bg-soft);
  border: 1px solid var(--border-soft);
  border-radius: var(--r-md);
  padding: 14px; margin-bottom: 10px;
}
.contact-row-header {
  display: flex; align-items: center;
  gap: 8px; margin-bottom: 10px;
}
.contact-row-icon { font-size: 1.3rem; }
.contact-row-name {
  font-weight: 600; color: var(--text);
  flex: 1; font-size: 0.95rem;
}
.contact-input {
  width: 100%; padding: 8px 12px;
  font-size: 0.86rem;
  border: 1px solid var(--border);
  border-radius: var(--r-sm);
  background: var(--bg-card);
  margin-bottom: 6px; color: var(--text);
  transition: border-color var(--t);
  font-family: inherit;
}
.contact-input:focus { outline: none; border-color: var(--text); }
.contact-input-label {
  font-size: 0.72rem; color: var(--text-3);
  font-weight: 600; margin-top: 6px; display: block;
  text-transform: uppercase; letter-spacing: 0.04em;
}
.contact-input.template { resize: vertical; min-height: 60px; line-height: 1.5; }
.contacts-footer {
  display: flex; justify-content: space-between;
  gap: 12px; margin-top: 18px;
  padding-top: 18px; border-top: 1px solid var(--border-soft);
}

/* RESPONSIVE */
@media (max-width: 768px) {
  .container { padding: 20px 16px 60px; }
  .container-zones { padding-top: 20px; }
  h1.brand { font-size: 2.5rem; }
  .tab-btn { padding: 11px 6px; font-size: 0.82rem; gap: 4px; }
  .tab-emoji { font-size: 0.95rem; }
  .subtab-btn { padding: 7px 10px; font-size: 0.78rem; }
  .care-grid { grid-template-columns: 1fr; }
  .hbar { grid-template-columns: 80px 1fr; }
  .task-detail-section { padding: 10px 14px; }
  .modal-content { padding: 20px; border-radius: var(--r-lg); }
  .snooze-options { grid-template-columns: 1fr 1fr; }
  .mini-stats { gap: 16px; }
}
@media (max-width: 480px) {
  h1.brand { font-size: 2rem; }
  .cards-grid { gap: 12px; }
  .card-photo-wrap { height: 280px; }
  .tab-emoji { font-size: 1.05rem; }
  .tab-label { font-size: 0.82rem; }
  .tab-btn { padding: 10px 8px; gap: 5px; }
}

/* PWA status panel en settings — diagnóstico autónomo */
.pwa-status-panel {
  background: var(--bg-soft);
  border-radius: var(--r-md);
  padding: 10px 12px;
  font-size: 0.82rem;
  line-height: 1.5;
  margin-bottom: 8px;
}
.pwa-st-row { padding: 3px 0; }
.pwa-st-row code {
  background: rgba(0, 0, 0, 0.06);
  padding: 1px 5px;
  border-radius: 4px;
  font-size: 0.75rem;
  word-break: break-all;
}
.pwa-st-ok { color: #166534; font-weight: 700; margin-right: 4px; }
.pwa-st-err { color: #991b1b; font-weight: 700; margin-right: 4px; }
.pwa-st-wait { color: #92400e; font-weight: 700; margin-right: 4px; }

/* PWA install banner — aparece SI Chrome dispara beforeinstallprompt.
   Su sola aparición confirma que el sitio cumple criterio installable.
   #push-resub-banner (reactivar notificaciones) comparte el mismo look. */
#pwa-install-banner,
#push-resub-banner {
  position: fixed;
  bottom: 16px; left: 50%;
  transform: translateX(-50%);
  z-index: 5000;
  display: flex;
  align-items: center;
  gap: 10px;
  background: #2d5016;
  color: white;
  padding: 12px 16px;
  border-radius: 999px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
  font-size: 0.88rem;
  font-weight: 600;
  max-width: calc(100vw - 24px);
  animation: slideUpFade 0.4s ease;
}
@keyframes slideUpFade {
  from { transform: translate(-50%, 30px); opacity: 0; }
  to { transform: translate(-50%, 0); opacity: 1; }
}
#pwa-install-banner .pwa-install-icon,
#push-resub-banner .pwa-install-icon { font-size: 1.2rem; }
#pwa-install-banner .pwa-install-btn,
#push-resub-banner .pwa-install-btn {
  background: white;
  color: #2d5016;
  border: none;
  padding: 6px 14px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 0.82rem;
  cursor: pointer;
}
#pwa-install-banner .pwa-install-btn:hover,
#push-resub-banner .pwa-install-btn:hover { background: rgba(255, 255, 255, 0.85); }
#pwa-install-banner .pwa-install-dismiss,
#push-resub-banner .pwa-install-dismiss {
  background: transparent;
  color: rgba(255, 255, 255, 0.7);
  border: none;
  width: 24px; height: 24px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 0.95rem;
  display: flex; align-items: center; justify-content: center;
}
#pwa-install-banner .pwa-install-dismiss:hover,
#push-resub-banner .pwa-install-dismiss:hover {
  background: rgba(255, 255, 255, 0.15);
  color: white;
}

/* IMPROVEMENTS — Mejoras pagas/gratis por zona */
.improvements-tier {
  margin-top: 22px;
}
.improvements-tier:first-of-type { margin-top: 12px; }
.improvements-tier-header {
  font-family: inherit;
  font-size: 0.98rem;
  font-weight: 700;
  margin: 0 0 12px;
  color: var(--text);
  letter-spacing: -0.005em;
  padding-left: 10px;
  border-left: 4px solid var(--tier-color, #16a34a);
}
.improvements-tier-count {
  color: var(--text-3);
  font-weight: 500;
  font-size: 0.85rem;
}
.improvements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 14px;
}
.improvement-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: 16px;
  padding: 18px;
  box-shadow:
    0 1px 2px rgba(9, 9, 11, 0.04),
    0 1px 3px rgba(9, 9, 11, 0.05);
  transition:
    border-color 200ms cubic-bezier(0.16, 1, 0.3, 1),
    transform 250ms cubic-bezier(0.16, 1, 0.3, 1),
    box-shadow 250ms cubic-bezier(0.16, 1, 0.3, 1);
}
.improvement-card:hover {
  border-color: var(--border-strong);
  transform: translateY(-2px);
  box-shadow:
    0 4px 8px rgba(9, 9, 11, 0.06),
    0 12px 28px rgba(9, 9, 11, 0.07);
}
.improvement-card.tier-free       { border-left-color: #16a34a; }
.improvement-card.tier-under10    { border-left-color: #ca8a04; }
.improvement-card.tier-under100   { border-left-color: #ea580c; }

.improvement-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}
.tier-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  padding: 3px 9px;
  border-radius: 999px;
  color: white;
}
.tier-badge.tier-free      { background: #16a34a; }
.tier-badge.tier-under10   { background: #ca8a04; }
.tier-badge.tier-under100  { background: #ea580c; }
.improvement-cost {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--text-2);
}
.improvement-title {
  font-family: inherit;
  font-size: 1rem;
  font-weight: 600;
  margin: 0 0 4px;
  color: var(--text);
  letter-spacing: -0.01em;
}
.improvement-category {
  font-size: 0.75rem;
  background: var(--bg-soft);
  border: 1px solid var(--border);
  padding: 2px 9px;
  border-radius: var(--r-sm);
  display: inline-block;
  color: var(--text-2);
  margin-bottom: 10px;
  font-weight: 500;
  text-transform: capitalize;
}
.improvement-line {
  font-size: 0.85rem;
  margin: 7px 0;
  color: var(--text-2);
  line-height: 1.5;
}
.improvement-line strong { color: var(--text); font-weight: 600; }
.improvement-applies {
  font-size: 0.85rem;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px dashed var(--border-soft);
  color: var(--text-2);
}
.improvement-applies strong { color: var(--text); font-weight: 600; margin-right: 4px; }
.improvement-applies-chip {
  display: inline-block;
  background: var(--bg-soft);
  border: 1px solid var(--border);
  color: var(--text);
  font-size: 0.78rem;
  font-weight: 600;
  padding: 3px 9px;
  border-radius: 999px;
  margin: 2px 4px 2px 0;
  cursor: pointer;
  font-family: inherit;
  transition: background 150ms, border-color 150ms, transform 150ms;
}
.improvement-applies-chip:hover {
  background: var(--accent, #16a34a);
  border-color: var(--accent, #16a34a);
  color: white;
  transform: translateY(-1px);
}
"""
