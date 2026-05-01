"""
Estilos CSS del documento.
"""

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Cormorant+Garamond:wght@400;500;600;700&display=swap');

:root {
  --bg: #f4ede0;
  --bg-paper: #fdfaf3;
  --bg-elevated: #fff8eb;
  --bg-final: #eaf3e6;
  --ink: #2e2a23;
  --ink-soft: #6b6457;
  --leaf: #4a6b3f;
  --leaf-dark: #2d4427;
  --leaf-light: #7a9a6e;
  --terracotta: #b85c3a;
  --terracotta-dark: #8c4528;
  --gold: #c9a44a;
  --gold-soft: #e8d4a0;
  --line: #d8cdb8;
  --line-soft: #e8dec3;
  --whatsapp: #25d366;
  --shadow-sm: 0 1px 3px rgba(46, 42, 35, 0.08);
  --shadow-md: 0 4px 12px rgba(46, 42, 35, 0.12);
  --shadow-lg: 0 12px 32px rgba(46, 42, 35, 0.18);
}
* { box-sizing: border-box; }

body {
  margin: 0; padding: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: 'Cormorant Garamond', Georgia, serif;
  line-height: 1.5;
  font-size: 16px;
  background-image:
    radial-gradient(circle at 10% 20%, rgba(74, 107, 63, 0.05) 0%, transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(184, 92, 58, 0.05) 0%, transparent 40%);
  min-height: 100vh;
}
.container { max-width: 1500px; margin: 0 auto; padding: 24px 20px 80px; }

header.main-header { text-align: center; padding: 32px 0 24px; position: relative; }
header.main-header::before {
  content: ""; position: absolute; top: 0; left: 50%;
  transform: translateX(-50%); width: 60px; height: 4px;
  background: linear-gradient(90deg, var(--leaf-dark), var(--gold), var(--terracotta));
  border-radius: 2px;
}
h1.brand {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.4rem, 6vw, 4rem);
  font-weight: 700; margin: 16px 0 8px;
  color: var(--leaf-dark); letter-spacing: -0.5px; line-height: 1;
}
.brand-emoji { font-size: 0.85em; display: inline-block; transform: translateY(-3px); }
h2.subbrand {
  font-family: 'Playfair Display', serif;
  font-size: clamp(1.2rem, 3vw, 1.8rem);
  font-weight: 400; font-style: italic; color: var(--terracotta);
  margin: 0 0 8px; letter-spacing: 1px;
}
.tagline {
  color: var(--ink-soft); font-style: italic; font-size: 0.95rem;
  max-width: 600px; margin: 8px auto 0;
}

.mini-stats {
  display: flex; gap: 12px; justify-content: center;
  flex-wrap: wrap; margin: 24px auto 32px; max-width: 800px;
}
.mini-stat {
  background: var(--bg-paper); border: 1px solid var(--line);
  padding: 8px 16px; border-radius: 24px;
  font-size: 0.9rem; color: var(--ink-soft);
  box-shadow: var(--shadow-sm);
}
.mini-stat strong { color: var(--leaf-dark); font-weight: 700; }

.main-tabs {
  display: flex; justify-content: center; gap: 8px;
  margin: 16px 0 0; border-bottom: 3px solid var(--leaf-dark);
  position: sticky; top: 0; background: var(--bg);
  z-index: 50; padding: 12px 0 0; flex-wrap: wrap;
}
.tab-btn {
  background: transparent; border: 2px solid var(--line);
  border-bottom: none; padding: 14px 32px;
  font-family: inherit; font-size: 1.15rem; font-weight: 600;
  cursor: pointer; border-radius: 12px 12px 0 0;
  color: var(--ink-soft); transition: all 0.2s;
  position: relative; bottom: -3px;
}
.tab-btn:hover { background: var(--bg-paper); color: var(--leaf-dark); }
.tab-btn.active {
  background: var(--leaf-dark); color: white;
  border-color: var(--leaf-dark);
  box-shadow: 0 -4px 12px rgba(45, 68, 39, 0.3);
}

.subtab-nav {
  display: flex; gap: 6px; margin: 0 0 24px;
  background: var(--bg-paper); padding: 8px;
  border-radius: 12px; flex-wrap: wrap;
  box-shadow: var(--shadow-sm); border: 1px solid var(--line);
}
.subtab-btn {
  background: transparent; border: none;
  padding: 10px 16px; font-family: inherit;
  font-size: 0.92rem; font-weight: 500;
  cursor: pointer; border-radius: 8px;
  color: var(--ink-soft); transition: all 0.15s;
  flex: 1; min-width: 110px;
}
.subtab-btn:hover { background: var(--bg-elevated); color: var(--ink); }
.subtab-btn.active {
  background: var(--terracotta); color: white;
  font-weight: 600; box-shadow: 0 2px 6px rgba(184, 92, 58, 0.3);
}

.zone-content { display: none; }
.zone-content.active { display: block; animation: fadeIn 0.3s; }
.subtab-pane { display: none; }
.subtab-pane.active { display: block; animation: fadeIn 0.3s; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

.filter-bar {
  display: flex; gap: 16px; margin-bottom: 20px;
  flex-wrap: wrap; align-items: center;
}
.search {
  flex: 1; min-width: 240px; padding: 12px 18px;
  font-family: inherit; font-size: 1rem;
  background: var(--bg-paper); border: 1px solid var(--line);
  border-radius: 24px; color: var(--ink); box-shadow: var(--shadow-sm);
}
.search:focus { outline: 2px solid var(--gold); outline-offset: 1px; }
.filter-tags { display: flex; gap: 6px; flex-wrap: wrap; }
.ftag {
  background: var(--bg-paper); border: 1px solid var(--line);
  padding: 8px 14px; font-family: inherit; font-size: 0.85rem;
  cursor: pointer; border-radius: 16px;
  color: var(--ink-soft); transition: all 0.15s;
}
.ftag:hover { background: var(--bg-elevated); color: var(--ink); }
.ftag.active { background: var(--leaf); color: white; border-color: var(--leaf); }

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}
.cards-grid.care-grid-list { grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); }

.plant-card {
  background: var(--bg-paper); border: 1px solid var(--line);
  border-radius: 14px; overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s, box-shadow 0.2s;
  display: flex; flex-direction: column;
}
.plant-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
.card-photo-wrap {
  position: relative; width: 100%; height: 220px;
  overflow: hidden;
  background: linear-gradient(135deg, #d8cdb8, #e8dec3);
}
.card-photo { width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; transition: transform 0.3s; }
.card-photo:hover { transform: scale(1.05); }
.card-loc-overlay {
  position: absolute; bottom: 8px; right: 8px;
  width: 60px; height: 60px; border-radius: 8px;
  overflow: hidden; border: 2px solid white;
  box-shadow: var(--shadow-md); background: var(--bg-paper);
}
.card-loc-photo { width: 100%; height: 100%; object-fit: cover; cursor: zoom-in; }
.card-id-pill {
  position: absolute; top: 8px; left: 8px;
  background: rgba(45, 68, 39, 0.92); color: white;
  padding: 5px 12px; border-radius: 16px;
  font-family: "Courier New", monospace;
  font-size: 0.85rem; font-weight: 600;
  box-shadow: var(--shadow-sm);
}
.card-body { padding: 18px 20px 20px; flex: 1; display: flex; flex-direction: column; }
.card-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.4rem; font-weight: 700;
  margin: 0 0 4px; color: var(--leaf-dark); line-height: 1.2;
}
.card-sci { font-style: italic; color: var(--ink-soft); font-size: 0.9rem; margin-bottom: 8px; }
.card-charrua {
  font-size: 0.85rem; color: var(--terracotta);
  margin-bottom: 6px; background: rgba(184, 92, 58, 0.07);
  padding: 4px 10px; border-radius: 6px; display: inline-block;
}
.card-other { font-size: 0.8rem; color: var(--ink-soft); margin-bottom: 8px; }
.card-tags { display: flex; flex-wrap: wrap; gap: 4px; margin: 8px 0; }
.tag {
  font-size: 0.72rem; padding: 3px 8px;
  border-radius: 12px; color: white;
  white-space: nowrap; font-weight: 500;
}
.card-type {
  font-size: 0.85rem; color: var(--ink-soft);
  margin-bottom: 10px; padding: 4px 10px;
  background: var(--bg-elevated); border-radius: 6px; display: inline-block;
}
.card-desc { font-size: 0.92rem; line-height: 1.5; color: var(--ink); margin: 8px 0; flex: 1; }
.card-funfact {
  font-size: 0.85rem; color: var(--leaf-dark);
  background: rgba(74, 107, 63, 0.06);
  border-left: 3px solid var(--gold);
  padding: 10px 12px; margin-top: 10px;
  border-radius: 0 6px 6px 0;
}

.care-card {
  background: var(--bg-paper); border: 1px solid var(--line);
  border-radius: 14px; overflow: hidden;
  box-shadow: var(--shadow-sm);
  display: flex; flex-direction: column;
}
.care-header {
  padding: 16px 20px;
  background: linear-gradient(135deg, var(--leaf-dark), var(--leaf));
  color: white;
}
.care-id { font-family: "Courier New", monospace; font-size: 0.78rem; opacity: 0.85; margin-bottom: 4px; }
.care-title { font-family: 'Playfair Display', serif; margin: 0; font-size: 1.3rem; font-weight: 700; }
.care-sci { font-style: italic; font-size: 0.85rem; opacity: 0.85; }
.urgency-banner {
  background: var(--bg-elevated); border-left: 4px solid;
  padding: 12px 16px; display: flex; flex-wrap: wrap;
  align-items: center; gap: 10px; font-size: 0.9rem;
}
.urgency-badge { color: white; padding: 3px 10px; border-radius: 12px; font-size: 0.78rem; font-weight: 600; white-space: nowrap; }
.urgency-when { margin-left: auto; color: var(--ink-soft); font-size: 0.85rem; }
.care-grid {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 1px; background: var(--line-soft); padding: 1px;
}
.care-section { background: var(--bg-paper); padding: 14px 16px; }
.care-label {
  font-size: 0.78rem; text-transform: uppercase;
  letter-spacing: 0.5px; color: var(--ink-soft);
  font-weight: 600; margin-bottom: 6px;
}
.big-icons { font-size: 0.9rem; margin-left: 4px; }
.care-value { font-size: 0.9rem; line-height: 1.4; color: var(--ink); }
.month-row { display: flex; gap: 2px; margin-top: 8px; flex-wrap: wrap; }
.month-pill {
  font-size: 0.7rem; padding: 3px 6px;
  background: var(--bg-elevated); color: var(--ink-soft);
  border-radius: 4px; font-weight: 500;
}
.month-pill.active { background: var(--terracotta); color: white; font-weight: 600; }

.idea-card {
  background: var(--bg-paper); border: 1px solid var(--line);
  border-left: 4px solid var(--gold); border-radius: 12px;
  padding: 18px 20px; box-shadow: var(--shadow-sm);
  transition: transform 0.2s;
}
.idea-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-md); }
.idea-title { font-family: 'Playfair Display', serif; font-size: 1.2rem; margin: 0 0 4px; color: var(--leaf-dark); }
.idea-sci { font-style: italic; color: var(--ink-soft); font-size: 0.85rem; margin-bottom: 6px; }
.idea-type {
  font-size: 0.85rem; background: var(--bg-elevated);
  padding: 3px 10px; border-radius: 6px;
  display: inline-block; color: var(--ink-soft); margin-bottom: 8px;
}
.idea-tags { display: flex; flex-wrap: wrap; gap: 4px; margin: 8px 0; }
.idea-why, .idea-where, .idea-size, .idea-season { font-size: 0.88rem; margin: 6px 0; color: var(--ink); }
.idea-where {
  background: rgba(184, 92, 58, 0.06); padding: 8px 10px;
  border-radius: 6px; border-left: 2px solid var(--terracotta);
}
.idea-season {
  background: rgba(74, 107, 63, 0.06); padding: 8px 10px;
  border-radius: 6px; border-left: 2px solid var(--leaf);
}
.ideas-intro {
  background: var(--bg-paper); border-left: 4px solid var(--gold);
  padding: 16px 20px; margin-bottom: 24px;
  border-radius: 0 8px 8px 0;
}
.ideas-intro h3 { font-family: 'Playfair Display', serif; margin: 0 0 6px; color: var(--leaf-dark); }
.ideas-intro p { margin: 0; color: var(--ink-soft); font-size: 0.93rem; }

.huerta-card {
  background: var(--bg-paper); border: 1px solid var(--line);
  border-top: 4px solid var(--leaf); border-radius: 12px;
  padding: 18px 20px; box-shadow: var(--shadow-sm);
}
.huerta-header { margin-bottom: 8px; }
.huerta-title { font-family: 'Playfair Display', serif; font-size: 1.25rem; margin: 0 0 4px; color: var(--leaf-dark); }
.huerta-sci { font-style: italic; color: var(--ink-soft); font-size: 0.85rem; }
.huerta-type { font-size: 0.82rem; color: var(--ink-soft); margin-bottom: 6px; }
.huerta-tags { display: flex; gap: 4px; flex-wrap: wrap; margin: 8px 0; }
.huerta-tip { font-size: 0.88rem; background: rgba(201, 164, 74, 0.1); padding: 10px 12px; border-radius: 6px; margin: 10px 0; }
.huerta-meta { display: flex; flex-wrap: wrap; gap: 12px; font-size: 0.82rem; color: var(--ink-soft); margin: 8px 0; }
.hcal { margin-top: 12px; }
.hbar {
  display: grid; grid-template-columns: 110px 1fr;
  gap: 8px; margin-bottom: 4px; align-items: center;
}
.hbar-label { font-size: 0.78rem; font-weight: 600; color: var(--ink-soft); }
.hbar-cells { display: grid; grid-template-columns: repeat(12, 1fr); gap: 1px; }
.hcell {
  font-size: 0.65rem; text-align: center;
  padding: 4px 0; background: var(--line-soft);
  color: var(--ink-soft); border-radius: 3px; font-weight: 500;
}
.hcell.active { background: var(--c, var(--leaf)); color: white; font-weight: 700; }

.hloc-intro { margin-bottom: 20px; }
.hloc-intro h3 { font-family: 'Playfair Display', serif; color: var(--leaf-dark); margin: 0 0 6px; }
.hloc-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px; margin-bottom: 32px;
}
.hloc-card {
  background: var(--bg-paper); border: 1px solid var(--line);
  border-top: 4px solid var(--terracotta); border-radius: 12px;
  padding: 16px 18px; box-shadow: var(--shadow-sm);
}
.hloc-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; margin: 0 0 8px; color: var(--terracotta-dark); }
.hloc-desc { font-size: 0.88rem; margin-bottom: 10px; }
.hloc-pros, .hloc-cons, .hloc-best { font-size: 0.83rem; margin: 6px 0; padding: 6px 10px; border-radius: 6px; }
.hloc-pros { background: rgba(74, 107, 63, 0.08); }
.hloc-cons { background: rgba(184, 92, 58, 0.08); }
.hloc-best { background: rgba(201, 164, 74, 0.1); }
.huerta-list-title {
  font-family: 'Playfair Display', serif; color: var(--leaf-dark);
  margin: 32px 0 8px; font-size: 1.6rem;
  border-top: 2px solid var(--line); padding-top: 24px;
}
.huerta-list-intro { color: var(--ink-soft); font-style: italic; margin-bottom: 20px; }
.frente-huerta-intro {
  background: var(--bg-paper); border-left: 4px solid var(--terracotta);
  padding: 16px 20px; margin-bottom: 24px;
  border-radius: 0 8px 8px 0;
}
.frente-huerta-intro h3 { font-family: 'Playfair Display', serif; margin: 0 0 4px; color: var(--terracotta-dark); }

.cal-legend { display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.88rem; margin-bottom: 16px; }
.cal-wrap {
  overflow-x: auto; background: var(--bg-paper);
  border-radius: 12px; padding: 12px;
  box-shadow: var(--shadow-sm); border: 1px solid var(--line);
}
.cal-table { width: 100%; border-collapse: separate; border-spacing: 2px; min-width: 800px; }
.cal-table th {
  font-family: 'Playfair Display', serif;
  font-size: 0.85rem; font-weight: 600;
  color: var(--leaf-dark); padding: 8px 4px; text-align: center;
}
.cal-name-h { text-align: left !important; min-width: 180px; }
.cal-name {
  font-size: 0.88rem; font-weight: 600;
  padding: 8px 12px; background: var(--bg-elevated);
  border-radius: 4px; white-space: nowrap;
}
.cal-codes { font-family: "Courier New", monospace; font-size: 0.72rem; color: var(--ink-soft); font-weight: 400; }
.cal-cell {
  background: var(--bg-elevated); border-radius: 4px;
  text-align: center; height: 36px; vertical-align: middle;
  font-size: 0.95rem; position: relative;
  transition: background 0.15s;
}
.cal-cell.flor { background: linear-gradient(135deg, #fbcfe8 0%, #f9a8d4 100%); }
.cal-cell.fruta { background: linear-gradient(135deg, #fed7aa 0%, #fdba74 100%); }
.cal-cell.poda { background: linear-gradient(135deg, #c9a44a 0%, #b8923a 100%); color: white; }
.cal-cell.flor.fruta { background: linear-gradient(135deg, #fbcfe8 0%, #fdba74 100%); }
.cal-cell.flor.poda { background: linear-gradient(135deg, #fbcfe8 0%, #c9a44a 100%); }
.cal-cell.fruta.poda { background: linear-gradient(135deg, #fdba74 0%, #c9a44a 100%); }
.cal-cell.flor.fruta.poda { background: linear-gradient(135deg, #fbcfe8 0%, #fdba74 50%, #c9a44a 100%); }

.lightbox {
  display: none; position: fixed; inset: 0;
  background: rgba(0, 0, 0, 0.92);
  z-index: 1000; align-items: center; justify-content: center;
  cursor: zoom-out; padding: 20px;
}
.lightbox.active { display: flex; }
.lightbox img { max-width: 95vw; max-height: 95vh; object-fit: contain; border-radius: 4px; }

/* ============================================================
   TIMELINE VIEW
   ============================================================ */
.timeline-header {
  display: flex; flex-direction: column; gap: 16px;
  margin-bottom: 24px;
}
.timeline-intro {
  background: var(--bg-paper); border-left: 4px solid var(--gold);
  padding: 16px 20px; border-radius: 0 8px 8px 0;
}
.timeline-intro h3 { font-family: 'Playfair Display', serif; margin: 0 0 6px; color: var(--leaf-dark); }
.timeline-intro p { margin: 0; color: var(--ink-soft); font-size: 0.93rem; }
.timeline-controls {
  display: flex; justify-content: space-between;
  flex-wrap: wrap; gap: 12px; align-items: center;
}
.btn-contacts {
  background: var(--bg-paper); border: 1px solid var(--line);
  padding: 10px 16px; font-family: inherit;
  font-size: 0.9rem; cursor: pointer;
  border-radius: 24px; color: var(--ink);
  transition: all 0.15s;
}
.btn-contacts:hover {
  background: var(--terracotta); color: white;
  border-color: var(--terracotta);
}
.timeline-summary {
  background: var(--bg-paper); border-radius: 12px;
  padding: 16px 20px; margin-bottom: 20px;
  box-shadow: var(--shadow-sm);
  display: flex; gap: 24px; flex-wrap: wrap;
  border: 1px solid var(--line);
}
.timeline-summary .stat-block {
  display: flex; flex-direction: column; align-items: flex-start;
}
.timeline-summary .stat-num {
  font-size: 1.5rem; font-weight: 700;
  font-family: 'Playfair Display', serif;
  color: var(--leaf-dark); line-height: 1;
}
.timeline-summary .stat-label { font-size: 0.85rem; color: var(--ink-soft); }

.timeline-feed {
  display: flex; flex-direction: column; gap: 16px;
  max-width: 720px; margin: 0 auto;
}
.timeline-empty {
  text-align: center; padding: 60px 20px;
  background: var(--bg-paper); border-radius: 12px;
  margin: 20px auto; max-width: 500px;
}
.timeline-empty .empty-icon { font-size: 4rem; margin-bottom: 10px; }
.timeline-empty h3 { font-family: 'Playfair Display', serif; color: var(--leaf-dark); margin: 0 0 8px; }
.timeline-empty p { color: var(--ink-soft); margin: 0; }

.task-card {
  background: var(--bg-paper); border: 1px solid var(--line);
  border-left: 6px solid var(--leaf);
  border-radius: 14px; overflow: hidden;
  box-shadow: var(--shadow-md);
  position: relative;
  transition: transform 0.2s, box-shadow 0.2s;
  touch-action: pan-y;
}
.task-card.swiping { transition: none; }
.task-card.swipe-out-right { transform: translateX(120%) rotate(8deg); opacity: 0; transition: transform 0.4s, opacity 0.4s; }
.task-card.swipe-out-left { transform: translateX(-120%) rotate(-8deg); opacity: 0; transition: transform 0.4s, opacity 0.4s; }
.task-card.priority-alta { border-left-color: #dc2626; }
.task-card.priority-media { border-left-color: #ca8a04; }
.task-card.priority-baja { border-left-color: #16a34a; }
.task-card.completed { opacity: 0.65; background: var(--bg-final); }
.task-card.snoozed { opacity: 0.85; background: var(--bg-elevated); }

.task-header {
  display: flex; gap: 14px; padding: 16px 18px;
  align-items: flex-start;
}
.task-photo {
  width: 88px; height: 88px;
  object-fit: cover; border-radius: 10px;
  flex-shrink: 0; background: var(--bg-elevated);
  cursor: zoom-in;
}
.task-photo-placeholder {
  width: 88px; height: 88px;
  background: var(--bg-elevated);
  border-radius: 10px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-size: 2rem;
}
.task-meta { flex: 1; min-width: 0; }
.task-meta-top {
  display: flex; align-items: center; gap: 8px;
  flex-wrap: wrap; margin-bottom: 6px;
}
.task-priority-pill {
  color: white; padding: 3px 10px;
  border-radius: 12px; font-size: 0.75rem; font-weight: 700;
  white-space: nowrap;
}
.task-zone-pill {
  background: var(--bg-elevated); color: var(--ink-soft);
  padding: 3px 10px; border-radius: 12px; font-size: 0.75rem;
  font-family: "Courier New", monospace;
}
.task-status-pill {
  padding: 3px 10px; border-radius: 12px;
  font-size: 0.75rem; font-weight: 600;
}
.task-status-pill.done { background: var(--leaf); color: white; }
.task-status-pill.snoozed { background: #94a3b8; color: white; }

.task-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem; font-weight: 700;
  color: var(--leaf-dark); margin: 0 0 4px; line-height: 1.2;
}
.task-plant {
  font-size: 0.88rem; color: var(--ink-soft);
  font-style: italic;
}
.task-due {
  display: inline-block; margin-top: 6px;
  font-size: 0.85rem; color: var(--terracotta);
  font-weight: 600;
}
.task-due.overdue { color: #dc2626; }
.task-snoozed-until {
  display: block; margin-top: 4px;
  font-size: 0.82rem; color: var(--ink-soft);
  font-style: italic;
}
.task-description {
  padding: 0 18px 14px; font-size: 0.92rem;
  color: var(--ink); line-height: 1.5;
}

.task-actions {
  display: flex; gap: 8px;
  padding: 12px 18px 16px;
  border-top: 1px dashed var(--line);
  flex-wrap: wrap;
}
.task-btn {
  flex: 1; min-width: 90px;
  padding: 10px 12px; font-family: inherit;
  font-size: 0.9rem; font-weight: 600;
  border: none; border-radius: 8px;
  cursor: pointer; transition: all 0.15s;
  display: inline-flex; align-items: center; justify-content: center;
  gap: 6px;
}
.task-btn-done { background: var(--leaf); color: white; }
.task-btn-done:hover { background: var(--leaf-dark); }
.task-btn-snooze { background: var(--bg-elevated); color: var(--ink); border: 1px solid var(--line); }
.task-btn-snooze:hover { background: var(--gold-soft); }
.task-btn-whatsapp { background: var(--whatsapp); color: white; }
.task-btn-whatsapp:hover { background: #1ca152; }
.task-btn-undo { background: var(--bg-elevated); color: var(--ink); border: 1px solid var(--line); }
.task-btn-undo:hover { background: var(--gold-soft); }

.swipe-hint {
  position: absolute; top: 50%; transform: translateY(-50%);
  font-size: 2rem; opacity: 0;
  pointer-events: none; transition: opacity 0.15s;
  font-weight: 700;
  text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
.swipe-hint.left { left: 16px; color: var(--leaf); }
.swipe-hint.right { right: 16px; color: var(--terracotta); }
.task-card[data-dx-positive="true"] .swipe-hint.right { opacity: var(--swipe-strength, 0); }
.task-card[data-dx-negative="true"] .swipe-hint.left { opacity: var(--swipe-strength, 0); }

/* ============================================================
   MODALS
   ============================================================ */
.modal {
  display: none; position: fixed; inset: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 2000; align-items: center; justify-content: center;
  padding: 20px;
}
.modal.active { display: flex; animation: fadeIn 0.2s; }
.modal-content {
  background: var(--bg-paper); border-radius: 16px;
  padding: 28px 32px; max-width: 460px;
  width: 100%; max-height: 90vh; overflow-y: auto;
  box-shadow: var(--shadow-lg);
  position: relative;
}
.modal-content.modal-wide { max-width: 600px; }
.modal-close {
  position: absolute; top: 12px; right: 12px;
  background: var(--bg-elevated); border: none;
  width: 36px; height: 36px; border-radius: 50%;
  cursor: pointer; font-size: 1rem;
  color: var(--ink-soft);
  transition: all 0.15s;
}
.modal-close:hover { background: var(--terracotta); color: white; }
.modal h3 {
  font-family: 'Playfair Display', serif;
  margin: 0 0 12px; color: var(--leaf-dark);
  font-size: 1.4rem;
}
.snooze-task-name, .whatsapp-task-name {
  background: var(--bg-elevated);
  padding: 10px 14px; border-radius: 8px;
  font-size: 0.9rem; color: var(--ink);
  margin-bottom: 18px; font-style: italic;
}
.snooze-options {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px; margin-bottom: 18px;
}
.snooze-opt {
  padding: 12px 14px; font-family: inherit;
  font-size: 0.92rem; cursor: pointer;
  border: 1px solid var(--line); background: var(--bg-paper);
  border-radius: 8px; transition: all 0.15s;
  color: var(--ink);
}
.snooze-opt:hover { background: var(--gold-soft); border-color: var(--gold); }
.snooze-custom {
  border-top: 1px dashed var(--line);
  padding-top: 16px;
  display: flex; flex-direction: column; gap: 8px;
}
.snooze-custom label { font-size: 0.85rem; color: var(--ink-soft); font-weight: 600; }
.snooze-custom input[type="date"] {
  padding: 10px 14px; font-family: inherit;
  font-size: 0.95rem; border: 1px solid var(--line);
  border-radius: 8px; background: white;
}
.btn-primary {
  background: var(--leaf); color: white; border: none;
  padding: 10px 16px; font-family: inherit;
  font-size: 0.95rem; font-weight: 600;
  border-radius: 8px; cursor: pointer; transition: all 0.15s;
}
.btn-primary:hover { background: var(--leaf-dark); }
.btn-primary:disabled { opacity: 0.4; cursor: not-allowed; }
.btn-primary.btn-wa { background: var(--whatsapp); }
.btn-primary.btn-wa:hover { background: #1ca152; }
.btn-secondary {
  background: var(--bg-elevated); color: var(--ink);
  border: 1px solid var(--line);
  padding: 10px 16px; font-family: inherit;
  font-size: 0.95rem; border-radius: 8px;
  cursor: pointer; transition: all 0.15s;
}
.btn-secondary:hover { background: var(--gold-soft); }

.whatsapp-section { margin-bottom: 16px; }
.whatsapp-label {
  display: block; font-size: 0.85rem;
  color: var(--ink-soft); font-weight: 600;
  margin-bottom: 8px;
}
.whatsapp-contacts {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 8px;
}
.wa-contact-btn {
  padding: 12px 8px; background: var(--bg-elevated);
  border: 1px solid var(--line); border-radius: 10px;
  cursor: pointer; transition: all 0.15s;
  font-family: inherit; font-size: 0.85rem;
  color: var(--ink); text-align: center;
}
.wa-contact-btn:hover { background: var(--gold-soft); }
.wa-contact-btn.active { background: var(--whatsapp); color: white; border-color: var(--whatsapp); }
.wa-contact-icon { font-size: 1.4rem; display: block; margin-bottom: 4px; }
.wa-contact-name { font-size: 0.78rem; line-height: 1.2; }
.wa-contact-noPhone { color: var(--terracotta); font-size: 0.7rem; display: block; margin-top: 2px; }
.whatsapp-message {
  width: 100%; padding: 12px 14px;
  font-family: inherit; font-size: 0.95rem;
  border: 1px solid var(--line); border-radius: 8px;
  resize: vertical; line-height: 1.5;
  background: white;
}
.whatsapp-actions { display: flex; justify-content: flex-end; }

.contacts-intro { font-size: 0.88rem; color: var(--ink-soft); margin-bottom: 16px; }
.contact-row {
  background: var(--bg-elevated); border-radius: 10px;
  padding: 12px 14px; margin-bottom: 10px;
}
.contact-row-header { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.contact-row-icon { font-size: 1.4rem; }
.contact-row-name { font-weight: 600; color: var(--leaf-dark); flex: 1; }
.contact-input {
  width: 100%; padding: 8px 12px;
  font-family: inherit; font-size: 0.9rem;
  border: 1px solid var(--line); border-radius: 6px;
  background: white; margin-bottom: 6px;
}
.contact-input-label { font-size: 0.78rem; color: var(--ink-soft); font-weight: 600; margin-top: 4px; display: block; }
.contact-input.template { resize: vertical; min-height: 50px; }
.contacts-footer {
  display: flex; justify-content: space-between;
  gap: 12px; margin-top: 16px;
  padding-top: 16px; border-top: 1px dashed var(--line);
}

@media (max-width: 768px) {
  .container { padding: 12px 12px 60px; }
  .tab-btn { padding: 10px 18px; font-size: 1rem; }
  .subtab-btn { padding: 8px 12px; font-size: 0.85rem; min-width: 100px; }
  .care-grid { grid-template-columns: 1fr; }
  .hbar { grid-template-columns: 90px 1fr; }
  .filter-bar { flex-direction: column; align-items: stretch; }
  .timeline-controls { flex-direction: column; align-items: stretch; }
  .task-photo, .task-photo-placeholder { width: 64px; height: 64px; }
  .task-actions { flex-direction: column; }
  .task-btn { min-width: 0; }
  .modal-content { padding: 20px 22px; }
  .snooze-options { grid-template-columns: 1fr 1fr; }
}
"""
