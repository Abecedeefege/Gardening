"""
Jardineando · Pacha Mama — Build script
Genera docs/index.html con el catálogo + timeline + ideas.

Ejecución:
    python build.py

Salida:
    docs/index.html (subir a GitHub Pages)
"""

import base64
import json
import html as html_mod
from io import BytesIO
from pathlib import Path
from PIL import Image

from data_plants import PLANTS
from data_ideas import (
    NEW_IDEAS_FRENTE,
    NEW_IDEAS_FONDO,
    HUERTA,
    HUERTA_LOCATION_IDEAS,
    DEFAULT_CONTACTS,
)
from styles import CSS
from scripts import JS

ROOT = Path(__file__).parent
IMAGES_DIR = ROOT / "images"
OUTPUT = ROOT / "docs" / "index.html"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)


# ============================================================
# Helpers
# ============================================================
def encode_image(path: Path, max_width: int = 800, quality: int = 78) -> str:
    img = Image.open(path).convert("RGB")
    if img.width > max_width:
        ratio = max_width / img.width
        img = img.resize((max_width, int(img.height * ratio)), Image.Resampling.LANCZOS)
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=quality, optimize=True)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode('ascii')}"


def esc(s):
    return html_mod.escape(str(s) if s is not None else "", quote=True)


MONTH_NAMES = ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
MONTH_FULL = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

TAG_STYLE = {
    "nativa": ("🇺🇾 nativa", "#4a6b3f"),
    "exotica": ("🌍 exótica", "#7a8c5c"),
    "frutal": ("🍑 frutal", "#d97706"),
    "aromatica": ("🌿 aromática", "#16a34a"),
    "ornamental": ("✨ ornamental", "#ca8a04"),
    "polinizadores": ("🐝 polinizadores", "#facc15"),
    "abejas": ("🐝 abejas", "#facc15"),
    "mariposas": ("🦋 mariposas", "#a855f7"),
    "picaflor": ("🐦 picaflor", "#ec4899"),
    "aves": ("🐦 aves", "#ec4899"),
    "trepadora": ("🌿 trepadora", "#0d9488"),
    "perfume": ("👃 perfume", "#e11d48"),
    "cerco-vivo": ("🌳 cerco-vivo", "#65a30d"),
    "comestible": ("🥬 comestible", "#16a34a"),
    "maceta": ("🪴 maceta", "#a16207"),
    "interior": ("🏠 interior", "#0284c7"),
    "purificadora": ("💨 purificadora", "#0284c7"),
    "sombra": ("🌑 sombra", "#475569"),
    "epifita": ("🌿 epífita", "#0d9488"),
    "rusticidad": ("💪 rústica", "#78716c"),
    "huerta": ("🥬 huerta", "#16a34a"),
    "fruto": ("🍅 fruto", "#dc2626"),
    "hoja": ("🥬 hoja", "#16a34a"),
    "raiz": ("🥕 raíz", "#f97316"),
    "bulbo": ("🧅 bulbo", "#a16207"),
    "verano": ("☀️ verano", "#eab308"),
    "invierno": ("❄️ invierno", "#0284c7"),
    "todo-año": ("🔄 todo el año", "#0d9488"),
    "rapida": ("⚡ rápida", "#facc15"),
    "perenne": ("♾️ perenne", "#4a6b3f"),
    "pendiente": ("⏳ pendiente", "#9333ea"),
    "fruta": ("🍓 fruta", "#dc2626"),
}

PRIORITY_STYLE = {
    "alta": ("🔴", "#dc2626", "Alta"),
    "media": ("🟡", "#ca8a04", "Media"),
    "baja": ("🟢", "#16a34a", "Baja"),
}


def render_tags(tags):
    return "".join(
        f'<span class="tag" style="background: {TAG_STYLE.get(t, ("", "#6b6457"))[1]}">{TAG_STYLE.get(t, (t,))[0]}</span>'
        for t in tags if t in TAG_STYLE
    )


def water_dots(water_str):
    if not water_str: return ""
    s = water_str.lower()
    if "muy bajo" in s or "tolera sequía" in s: return "💧"
    if "medio-bajo" in s: return "💧💧"
    if "medio-alto" in s: return "💧💧💧"
    if "bajo" in s: return "💧💧"
    if "alto" in s: return "💧💧💧💧"
    if "medio" in s: return "💧💧💧"
    return "💧"


def light_icon(light_str):
    if not light_str: return ""
    s = light_str.lower()
    if "pleno sol" in s or "sol pleno" in s: return "☀️☀️"
    if "sol parcial" in s or "sol o sombra" in s: return "🌤️"
    if "sombra parcial" in s: return "⛅"
    if "sombra" in s: return "🌑"
    if "sol" in s: return "☀️"
    return ""


# ============================================================
# Generación de tareas para Timeline
# ============================================================
def generate_tasks_from_plants(plants):
    """
    Genera la lista canónica de tareas desde el catálogo de plantas.
    Cada planta con `urgency` produce 1 tarea.
    Si en el futuro queremos auto-derivar tareas estacionales (por ej. 'hay que regar'),
    se hace acá.
    """
    tasks = []
    for plant in plants:
        if not plant.get("urgency"):
            continue
        urg = plant["urgency"]
        # Sugerir contacto basado en tipo de acción
        action_lower = urg["action"].lower()
        if "poda" in action_lower or "trasplant" in action_lower:
            suggested_contact = "jardinero"
        elif "foto" in action_lower or "identificar" in action_lower:
            suggested_contact = None  # tarea propia
        else:
            suggested_contact = "jornalero"

        tasks.append({
            "id": f"plant-{plant['id_codes'][0]}",
            "kind": "plant_action",
            "plant_codes": plant["id_codes"],
            "plant_common": plant["common"],
            "plant_zone": plant["zone"],
            "plant_photo": plant.get("main_photo", ""),
            "title": urg["action"],
            "description": f"{plant['common']} ({', '.join(plant['id_codes'])}) — {urg['action']}.",
            "priority": urg["priority"],
            "due_label": urg["when"],
            "due_month": urg.get("due_month"),
            "due_year": urg.get("due_year"),
            "suggested_contact": suggested_contact,
        })

    # Ordenar por prioridad y luego por fecha
    prio_order = {"alta": 0, "media": 1, "baja": 2}
    tasks.sort(key=lambda t: (
        prio_order.get(t["priority"], 3),
        t.get("due_year") or 9999,
        t.get("due_month") or 13,
    ))
    return tasks


# ============================================================
# Renderers — Plant cards (zone view)
# ============================================================
def render_plant_info_card(p, img_data):
    loc_codes = ", ".join(p["id_codes"])
    has_main = bool(p.get("main_photo") and img_data.get(p.get("main_photo")))
    has_loc = bool(p.get("loc_photo") and img_data.get(p.get("loc_photo")))

    photo_html = f'<img class="card-photo" data-img="{esc(p["main_photo"])}" data-action="lightbox" alt="">' if has_main else ''
    locs_html = f'<img class="card-loc-photo" data-img="{esc(p["loc_photo"])}" data-action="lightbox" alt="" title="Ver ubicación">' if has_loc else ''
    type_badge = {"caduco": "🍂 Caduco", "perenne": "🌲 Perenne", "semi-perenne": "🍃 Semi-perenne", "semi-caduco": "🍃 Semi-caduco"}.get(p.get("type", ""), p.get("type", ""))
    charrua_html = f'<div class="card-charrua">🪶 <strong>Originario:</strong> {esc(p["charrua"])}</div>' if p.get("charrua") else ''
    funfact_html = f'<div class="card-funfact">💡 <em>{esc(p["fun_fact"])}</em></div>' if p.get("fun_fact") and p["fun_fact"] != "—" else ''
    other_names_html = f'<div class="card-other">↳ {esc(p["other_names"])}</div>' if p.get("other_names") and p["other_names"] != "—" else ''

    return f"""
<article class="plant-card" data-plant-id="{esc(loc_codes)}" data-name="{esc(p['common'].lower())}" data-tags="{esc(' '.join(p['tags']))}">
  <div class="card-photo-wrap">
    {photo_html}
    <div class="card-loc-overlay">{locs_html}</div>
    <div class="card-id-pill">{esc(loc_codes)}</div>
  </div>
  <div class="card-body">
    <h3 class="card-title">{esc(p['common'])}</h3>
    <div class="card-sci">{esc(p['sci'])}</div>
    {charrua_html}
    {other_names_html}
    <div class="card-tags">{render_tags(p['tags'])}</div>
    <div class="card-type">{type_badge}</div>
    <p class="card-desc">{esc(p['desc'])}</p>
    {funfact_html}
  </div>
</article>"""


def render_plant_care_card(p):
    loc_codes = ", ".join(p["id_codes"])
    pruning_months = "".join(
        f'<span class="month-pill {"active" if m in p.get("pruning", []) else ""}">{MONTH_NAMES[m]}</span>'
        for m in range(1, 13)
    )
    urgency_html = ""
    if p.get("urgency"):
        u = p["urgency"]
        emo, color, label = PRIORITY_STYLE.get(u["priority"], ("", "#6b6457", u["priority"]))
        urgency_html = f"""
<div class="urgency-banner" style="border-left-color: {color}">
  <span class="urgency-badge" style="background: {color}">{emo} {label}</span>
  <strong>{esc(u["action"])}</strong>
  <span class="urgency-when">📅 {esc(u["when"])}</span>
</div>"""

    return f"""
<article class="care-card" data-plant-id="{esc(loc_codes)}" data-name="{esc(p['common'].lower())}">
  <div class="care-header">
    <div class="care-id">{esc(loc_codes)}</div>
    <h3 class="care-title">{esc(p['common'])}</h3>
    <div class="care-sci">{esc(p['sci'])}</div>
  </div>
  {urgency_html}
  <div class="care-grid">
    <div class="care-section">
      <div class="care-label">✂️ Cuándo podar</div>
      <div class="care-value">{esc(p['prune_when'])}</div>
      <div class="month-row">{pruning_months}</div>
    </div>
    <div class="care-section">
      <div class="care-label">📏 Cuánto podar</div>
      <div class="care-value">{esc(p['prune_how'])}</div>
    </div>
    <div class="care-section">
      <div class="care-label">💧 Riego <span class="big-icons">{water_dots(p['water'])}</span></div>
      <div class="care-value">{esc(p['water'])}</div>
    </div>
    <div class="care-section">
      <div class="care-label">{light_icon(p['light'])} Luz</div>
      <div class="care-value">{esc(p['light'])}</div>
    </div>
  </div>
</article>"""


def render_idea_card(idea):
    season = f'<div class="idea-season">📅 <strong>Plantar:</strong> {esc(idea["season_plant"])}</div>' if "season_plant" in idea else ''
    where = f'<div class="idea-where">📍 <strong>Dónde:</strong> {esc(idea["where"])}</div>' if "where" in idea else ''
    size = f'<div class="idea-size">📐 <strong>Tamaño:</strong> {esc(idea["size"])}</div>' if "size" in idea else ''

    return f"""
<article class="idea-card" data-name="{esc(idea['common'].lower())}" data-tags="{esc(' '.join(idea.get('tags', [])))}">
  <h3 class="idea-title">{esc(idea['common'])}</h3>
  <div class="idea-sci">{esc(idea.get('sci', ''))}</div>
  <div class="idea-type">{esc(idea['type'])}</div>
  <div class="idea-tags">{render_tags(idea.get('tags', []))}</div>
  <div class="idea-why"><strong>💚 Por qué:</strong> {esc(idea.get('why', ''))}</div>
  {where}
  {size}
  {season}
</article>"""


def render_huerta_card(h):
    def month_bar(months, color, label):
        bars = "".join(
            f'<div class="hcell {"active" if m in months else ""}" style="--c:{color}" title="{MONTH_FULL[m]}">{MONTH_NAMES[m]}</div>'
            for m in range(1, 13)
        )
        return f'<div class="hbar"><div class="hbar-label">{label}</div><div class="hbar-cells">{bars}</div></div>'

    cal_html = ""
    if h.get("siembra"): cal_html += month_bar(h["siembra"], "#16a34a", "🌱 Siembra")
    if h.get("transplante"): cal_html += month_bar(h["transplante"], "#0d9488", "🪴 Trasplante")
    if h.get("cosecha"): cal_html += month_bar(h["cosecha"], "#d97706", "🧺 Cosecha")

    return f"""
<article class="huerta-card" data-name="{esc(h['common'].lower())}" data-tags="{esc(' '.join(h.get('tags', [])))}">
  <div class="huerta-header">
    <h3 class="huerta-title">{esc(h['common'])}</h3>
    <div class="huerta-sci">{esc(h.get('sci', ''))}</div>
    <div class="huerta-type">{esc(h['type'])}</div>
  </div>
  <div class="huerta-tags">{render_tags(h.get('tags', []))}</div>
  <div class="huerta-tip"><strong>💡 Tip:</strong> {esc(h['tip'])}</div>
  <div class="huerta-meta">
    <span>{light_icon(h.get('sun', ''))} {esc(h.get('sun', ''))}</span>
    <span>{water_dots(h.get('water', ''))} {esc(h.get('water', ''))}</span>
  </div>
  <div class="hcal">{cal_html}</div>
</article>"""


def render_calendar_grid(zone, plants):
    plants_zone = [p for p in plants if p["zone"] == zone and any([p.get("flowering"), p.get("fruiting"), p.get("pruning")])]
    plants_zone.sort(key=lambda p: p["common"])

    rows = []
    for p in plants_zone:
        cells = ""
        for m in range(1, 13):
            classes = []
            if m in p.get("flowering", []): classes.append("flor")
            if m in p.get("fruiting", []): classes.append("fruta")
            if m in p.get("pruning", []): classes.append("poda")
            cls = " ".join(classes) if classes else ""
            content = ""
            if "flor" in classes: content += '<span class="cal-emo">🌸</span>'
            if "fruta" in classes: content += '<span class="cal-emo">🍑</span>'
            if "poda" in classes: content += '<span class="cal-emo">✂️</span>'
            cells += f'<td class="cal-cell {cls}" title="{MONTH_FULL[m]}">{content}</td>'
        rows.append(f'<tr><td class="cal-name">{esc(p["common"])}<br><span class="cal-codes">{esc(", ".join(p["id_codes"]))}</span></td>{cells}</tr>')

    header_cells = "".join(f'<th class="cal-month">{MONTH_NAMES[m]}</th>' for m in range(1, 13))
    return f"""
<div class="cal-legend">
  <span class="leg-flor">🌸 Floración</span>
  <span class="leg-fruta">🍑 Fruta/cosecha</span>
  <span class="leg-poda">✂️ Poda</span>
</div>
<div class="cal-wrap">
  <table class="cal-table">
    <thead><tr><th class="cal-name-h">Planta</th>{header_cells}</tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
</div>"""


def render_huerta_locations():
    cards = "".join(f"""
<article class="hloc-card">
  <h4 class="hloc-title">{esc(idea["title"])}</h4>
  <p class="hloc-desc">{esc(idea["desc"])}</p>
  <div class="hloc-pros"><strong>✅ Pros:</strong> {esc(idea["pros"])}</div>
  <div class="hloc-cons"><strong>⚠️ Contras:</strong> {esc(idea["cons"])}</div>
  <div class="hloc-best"><strong>👍 Mejor para:</strong> {esc(idea["best_for"])}</div>
</article>""" for idea in HUERTA_LOCATION_IDEAS)
    return f"""
<div class="hloc-intro">
  <h3>🤔 Aún no decidiste el espacio — acá te dejo opciones:</h3>
  <p>Ordenadas según mi recomendación (de mejor a más simple).</p>
</div>
<div class="hloc-grid">{cards}</div>
<h3 class="huerta-list-title">📋 Catálogo de cultivos para Uruguay</h3>
<p class="huerta-list-intro">Estos son los más recomendados para tu clima (Montevideo) y tu nivel de mantenimiento medio. Calendario marcado en meses.</p>
"""


# ============================================================
# Build de cada zona (Frente / Fondo)
# ============================================================
def build_zone(zone_name, zone_label, plants, img_data, tasks_by_zone):
    info_cards = "\n".join(render_plant_info_card(p, img_data) for p in plants if p["zone"] == zone_name)
    care_cards = "\n".join(render_plant_care_card(p) for p in plants if p["zone"] == zone_name)
    ideas_list = NEW_IDEAS_FRENTE if zone_name == "frente" else NEW_IDEAS_FONDO
    new_ideas = "\n".join(render_idea_card(i) for i in ideas_list)
    huerta_cards = "\n".join(render_huerta_card(h) for h in HUERTA)
    huerta_intro = render_huerta_locations() if zone_name == "fondo" else """
<div class="frente-huerta-intro">
  <h3>🌿 Aromáticas para el frente</h3>
  <p>El frente no es ideal para huerta clásica (visibilidad, espacio limitado). Pero podés sumar aromáticas y comestibles ornamentales que decoran y se cosechan.</p>
</div>"""
    cal_grid = render_calendar_grid(zone_name, plants)

    return f"""
<section class="zone-content" data-zone="{zone_name}">
  <nav class="subtab-nav">
    <button class="subtab-btn active" data-sub="info">🪴 Nombres e info</button>
    <button class="subtab-btn" data-sub="care">✂️ Podas y cuidado</button>
    <button class="subtab-btn" data-sub="new">💡 Ideas nuevas</button>
    <button class="subtab-btn" data-sub="huerta">🥬 Ideas de huerta</button>
    <button class="subtab-btn" data-sub="cal">📅 Calendario</button>
  </nav>

  <div class="subtab-pane active" data-sub="info">
    <div class="filter-bar">
      <input type="text" class="search" placeholder="🔍 Buscar planta...">
      <div class="filter-tags" data-zone="{zone_name}">
        <button class="ftag active" data-filter="all">Todas</button>
        <button class="ftag" data-filter="nativa">🇺🇾 Nativas</button>
        <button class="ftag" data-filter="frutal">🍑 Frutales</button>
        <button class="ftag" data-filter="aromatica">🌿 Aromáticas</button>
        <button class="ftag" data-filter="ornamental">✨ Ornamentales</button>
        <button class="ftag" data-filter="trepadora">🌿 Trepadoras</button>
        <button class="ftag" data-filter="polinizadores">🐝 Polinizadores</button>
        <button class="ftag" data-filter="pendiente">⏳ Pendientes</button>
      </div>
    </div>
    <div class="cards-grid">{info_cards}</div>
  </div>

  <div class="subtab-pane" data-sub="care">
    <div class="filter-bar"><input type="text" class="search" placeholder="🔍 Buscar planta..."></div>
    <div class="cards-grid care-grid-list">{care_cards}</div>
  </div>

  <div class="subtab-pane" data-sub="new">
    <div class="ideas-intro">
      <h3>💡 Plantas recomendadas para sumar al {zone_label.lower()}</h3>
      <p>Basado en tu jardín actual, clima Montevideo y mantenimiento medio. Énfasis en nativas y polinizadores.</p>
    </div>
    <div class="cards-grid ideas-grid">{new_ideas}</div>
  </div>

  <div class="subtab-pane" data-sub="huerta">
    {huerta_intro}
    <div class="cards-grid huerta-grid">{huerta_cards}</div>
  </div>

  <div class="subtab-pane" data-sub="cal">
    <div class="ideas-intro">
      <h3>📅 Calendario anual de eventos del jardín</h3>
      <p>De un vistazo: cuándo florece cada planta, cuándo da fruto, y cuándo podarla.</p>
    </div>
    {cal_grid}
  </div>
</section>"""


# ============================================================
# Build TIMELINE view
# ============================================================
def build_timeline_view(tasks, img_data):
    """
    Renderiza la vista Timeline. La interactividad (estado, swipe, WhatsApp)
    está en scripts.py. Acá sólo serializamos los datos a JSON para que el JS
    los consuma.
    """
    # Pasamos sólo URLs de imagen referenciadas por tasks
    return """
<section class="zone-content" data-zone="timeline">
  <div class="timeline-header">
    <div class="timeline-intro">
      <h3>📋 Timeline de tareas</h3>
      <p>Tu próxima acción aparece arriba. Marcá hecho, posponé, o pedí ayuda con un mensaje pre-armado de WhatsApp.</p>
    </div>
    <div class="timeline-controls">
      <div class="filter-tags timeline-filters">
        <button class="ftag active" data-filter="active">📌 Activas</button>
        <button class="ftag" data-filter="done">✅ Hechas</button>
        <button class="ftag" data-filter="snoozed">😴 Pospuestas</button>
        <button class="ftag" data-filter="all">📚 Todas</button>
      </div>
      <button class="btn-contacts" id="btn-edit-contacts">📞 Mis contactos</button>
    </div>
  </div>

  <div class="timeline-summary" id="timeline-summary"></div>
  <div class="timeline-feed" id="timeline-feed"></div>
  <div class="timeline-empty" id="timeline-empty" style="display:none">
    <div class="empty-icon">🌿</div>
    <h3>Todo bajo control</h3>
    <p>No hay tareas en esta vista. ¡Podés volver más tarde!</p>
  </div>
</section>

<!-- Modal: Snooze -->
<div class="modal" id="snooze-modal">
  <div class="modal-content">
    <button class="modal-close" data-close="snooze">✕</button>
    <h3>😴 Posponer tarea</h3>
    <p class="snooze-task-name" id="snooze-task-name"></p>
    <div class="snooze-options">
      <button class="snooze-opt" data-days="1">⏰ Mañana</button>
      <button class="snooze-opt" data-days="3">📆 En 3 días</button>
      <button class="snooze-opt" data-days="7">🗓️ En 1 semana</button>
      <button class="snooze-opt" data-days="14">🗓️ En 2 semanas</button>
      <button class="snooze-opt" data-days="30">📅 En 1 mes</button>
      <button class="snooze-opt" data-days="90">📅 En 3 meses</button>
    </div>
    <div class="snooze-custom">
      <label>O elegí una fecha:</label>
      <input type="date" id="snooze-custom-date">
      <button class="btn-primary" id="btn-snooze-custom">Posponer hasta esta fecha</button>
    </div>
  </div>
</div>

<!-- Modal: WhatsApp -->
<div class="modal" id="whatsapp-modal">
  <div class="modal-content modal-wide">
    <button class="modal-close" data-close="whatsapp">✕</button>
    <h3>💬 Mensaje de WhatsApp</h3>
    <p class="whatsapp-task-name" id="whatsapp-task-name"></p>

    <div class="whatsapp-section">
      <label class="whatsapp-label">¿A quién le escribo?</label>
      <div class="whatsapp-contacts" id="whatsapp-contacts"></div>
    </div>

    <div class="whatsapp-section">
      <label class="whatsapp-label">Mensaje (editable):</label>
      <textarea class="whatsapp-message" id="whatsapp-message" rows="6" placeholder="Elegí un contacto arriba para ver el mensaje..."></textarea>
    </div>

    <div class="whatsapp-actions">
      <button class="btn-primary btn-wa" id="btn-send-whatsapp" disabled>
        💬 Abrir en WhatsApp
      </button>
    </div>
  </div>
</div>

<!-- Modal: Editar contactos -->
<div class="modal" id="contacts-modal">
  <div class="modal-content modal-wide">
    <button class="modal-close" data-close="contacts">✕</button>
    <h3>📞 Mis contactos</h3>
    <p class="contacts-intro">
      Editá teléfonos y plantilla por defecto. Se guarda solo en tu navegador (no se sube a internet).
    </p>
    <div id="contacts-list"></div>
    <div class="contacts-footer">
      <button class="btn-secondary" id="btn-reset-contacts">↺ Restaurar defaults</button>
      <button class="btn-primary" id="btn-save-contacts">💾 Guardar</button>
    </div>
  </div>
</div>"""


# ============================================================
# Main
# ============================================================
def main():
    # 1. Cargar imágenes
    unique_files = set()
    for p in PLANTS:
        if p.get("loc_photo"): unique_files.add(p["loc_photo"])
        if p.get("main_photo"): unique_files.add(p["main_photo"])

    print(f"📷 Procesando {len(unique_files)} imágenes...")
    img_data = {}
    for fname in sorted(unique_files):
        path = IMAGES_DIR / fname
        if path.exists():
            img_data[fname] = encode_image(path)
        else:
            img_data[fname] = ""
            print(f"  ⚠ Faltante: {fname}")
    print(f"   ✅ {sum(1 for v in img_data.values() if v)} embebidas")

    # 2. Generar tareas
    tasks = generate_tasks_from_plants(PLANTS)
    print(f"📋 Tareas generadas: {len(tasks)}")

    # 3. Stats
    total_plants = len(PLANTS)
    total_native = sum(1 for p in PLANTS if "nativa" in p["tags"])
    total_frutal = sum(1 for p in PLANTS if "frutal" in p["tags"])
    total_urgent = sum(1 for p in PLANTS if p.get("urgency"))

    # 4. Build zonas
    frente_html = build_zone("frente", "Frente", PLANTS, img_data, None)
    fondo_html = build_zone("fondo", "Fondo", PLANTS, img_data, None)
    timeline_html = build_timeline_view(tasks, img_data)

    # 5. Inyectar datos como JSON para el JS
    img_js = "const IMG = " + json.dumps(img_data) + ";"
    tasks_js = "const TASKS = " + json.dumps(tasks, ensure_ascii=False) + ";"
    contacts_js = "const DEFAULT_CONTACTS = " + json.dumps(DEFAULT_CONTACTS, ensure_ascii=False) + ";"

    # 6. HTML final
    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Jardineando · Pacha Mama</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
  <header class="main-header">
    <h1 class="brand"><span class="brand-emoji">🌿</span> Jardineando</h1>
    <h2 class="subbrand">Pacha Mama</h2>
    <p class="tagline">Catálogo vivo del jardín · {total_plants} especies · {total_native} nativas · {total_frutal} frutales · clima Montevideo</p>
  </header>

  <div class="mini-stats">
    <span class="mini-stat">🌱 <strong>{total_plants}</strong> especies catalogadas</span>
    <span class="mini-stat">🇺🇾 <strong>{total_native}</strong> nativas uruguayas</span>
    <span class="mini-stat">🍑 <strong>{total_frutal}</strong> frutales</span>
    <span class="mini-stat">🚨 <strong>{total_urgent}</strong> con acción pendiente</span>
  </div>

  <nav class="main-tabs">
    <button class="tab-btn active" data-zone="timeline">📋 Timeline</button>
    <button class="tab-btn" data-zone="frente">🏡 Frente</button>
    <button class="tab-btn" data-zone="fondo">🌳 Fondo</button>
  </nav>

  <div class="zone-content active" data-zone="timeline">{timeline_html.split('<section class="zone-content" data-zone="timeline">', 1)[1].split('</section>', 1)[0]}</div>
  {frente_html}
  {fondo_html}
  {timeline_html.split('</section>', 1)[1]}
</div>

<div class="lightbox" id="lightbox">
  <img id="lightbox-img" alt="">
</div>

<script>
{img_js}
{tasks_js}
{contacts_js}
{JS}
</script>
</body>
</html>"""

    OUTPUT.write_text(html_doc, encoding="utf-8")
    size_mb = OUTPUT.stat().st_size / 1024 / 1024
    print(f"\n✅ Generado: {OUTPUT}")
    print(f"   {size_mb:.1f} MB · {total_plants} plantas · {len(tasks)} tareas")
    print(f"\n👉 Para subir a GitHub Pages:")
    print(f"   git add docs/index.html && git commit -m 'rebuild' && git push")


if __name__ == "__main__":
    main()
