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
from datetime import date
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
    WHATSAPP_TEMPLATES_BY_ACTION,
)
from styles import CSS
from scripts import JS

ROOT = Path(__file__).parent
IMAGES_DIR = ROOT / "images"
OUTPUT = ROOT / "docs" / "index.html"
TASKS_DIR = ROOT / "docs" / "tasks"
OG_DIR = ROOT / "docs" / "og"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
TASKS_DIR.mkdir(parents=True, exist_ok=True)
OG_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# CONFIGURACIÓN — editar antes del primer deploy
# ============================================================
# URL pública de tu GitHub Pages.
# Ejemplo: "https://juan.github.io/jardineando-pacha-mama"
# Si está vacío, los previews de WhatsApp no van a funcionar (links rotos).
SITE_URL = "https://gardening-git-main-andys-projects-8bfb617c.vercel.app"


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


def _select_primary_urgency(urgency_field):
    """Soporta urgency como dict (1 sola) o list (múltiples). Devuelve la más
    urgente para mostrar en banners de cards: atrasada > alta > fecha temprana.
    Devuelve None si no hay nada."""
    if not urgency_field:
        return None
    if isinstance(urgency_field, dict):
        return urgency_field
    today = date.today()
    prio = {"alta": 0, "media": 1, "baja": 2}

    def sort_key(u):
        is_overdue = bool(
            u.get("due_year") and u.get("due_month") and
            (u["due_year"] < today.year or
             (u["due_year"] == today.year and u["due_month"] < today.month))
        )
        return (
            0 if is_overdue else 1,
            prio.get(u.get("priority"), 3),
            u.get("due_year") or 9999,
            u.get("due_month") or 13,
        )

    return sorted(urgency_field, key=sort_key)[0]


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

def classify_action(action_str: str) -> str:
    """
    Clasifica un string de urgency.action en uno de 9 action_types.
    El orden importa: la primera regla que matchea gana.
    Identificar gana sobre foto (acciones tipo "Identificar — sacar foto..."
    deben caer en identificar). Poda gana sobre control_plagas para acciones
    combinadas como "Poda + control de cochinilla" — la categoría dominante
    es la poda.
    """
    a = (action_str or "").lower()
    if "identific" in a or "confirmar especie" in a or "saber qué" in a:
        return "identificar"
    if "sacar foto" in a or "fotograf" in a or " foto " in f" {a} ":
        return "foto"
    if "poda" in a or "podar" in a or "rejuven" in a or "cortar a" in a or "cortar tallo" in a:
        return "poda"
    if "trasplant" in a or "maceta más grande" in a:
        return "trasplante"
    if "fertiliz" in a or "abonar" in a:
        return "fertilizacion"
    if any(k in a for k in ("cochinilla", "pulgón", "pulgones", "plaga", "trips", "minador")):
        return "control_plagas"
    if any(k in a for k in ("limpieza", "limpiar", "ramas secas", "hojas secas", "dividir")):
        return "limpieza"
    if "riego" in a or "regar" in a:
        return "riego"
    return "mantenimiento"


def generate_tasks_from_plants(plants):
    """
    Genera la lista canónica de tareas desde el catálogo de plantas.
    Cada urgencia es self-contained con shape:
        {priority, title, short_desc, detail, how_to, tips, when, due_month, due_year}
    """
    tasks = []
    for plant in plants:
        urgencies = plant.get("urgency")
        if urgencies is None:
            continue
        if isinstance(urgencies, dict):
            urgencies = [urgencies]

        plant_id = plant["id_codes"][0]
        for idx, urg in enumerate(urgencies):
            title = urg["title"]
            action_type = classify_action(title)
            if action_type in ("poda", "trasplante", "fertilizacion", "control_plagas"):
                suggested_contact = "jardinero"
            elif action_type in ("identificar", "foto"):
                suggested_contact = None
            else:
                suggested_contact = "jornalero"

            task_id = f"plant-{plant_id}" if idx == 0 else f"plant-{plant_id}-{idx + 1}"

            tasks.append({
                "id": task_id,
                "kind": "plant_action",
                "plant_codes": plant["id_codes"],
                "plant_common": plant["common"],
                "plant_zone": plant["zone"],
                "plant_photo": plant.get("main_photo", ""),
                "title": title,
                "short_desc": urg.get("short_desc", ""),
                "description": f"{plant['common']} ({', '.join(plant['id_codes'])}) — {title}.",
                "detail": urg.get("detail", ""),
                "how_to": urg.get("how_to", ""),
                "tips": urg.get("tips", ""),
                "priority": urg["priority"],
                "due_label": urg["when"],
                "due_month": urg.get("due_month"),
                "due_year": urg.get("due_year"),
                "suggested_contact": suggested_contact,
                "action_type": action_type,
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

    primary_code = p["id_codes"][0]
    photo_html = f'<img class="card-photo" data-img="{esc(p["main_photo"])}" data-action="open-species" data-plant-code="{esc(primary_code)}" alt="">' if has_main else ''
    locs_html = f'<img class="card-loc-photo" data-img="{esc(p["loc_photo"])}" data-action="open-species" data-plant-code="{esc(primary_code)}" alt="" title="Ver detalles de la especie">' if has_loc else ''
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
    u = _select_primary_urgency(p.get("urgency"))
    if u:
        emo, color, label = PRIORITY_STYLE.get(u["priority"], ("", "#6b6457", u["priority"]))
        urgency_html = f"""
<div class="urgency-banner" style="border-left-color: {color}">
  <span class="urgency-badge" style="background: {color}">{emo} {label}</span>
  <strong>{esc(u.get("title") or u.get("action", ""))}</strong>
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


def render_calendar_grid(plants_in_view):
    plants_zone = [p for p in plants_in_view if any([p.get("flowering"), p.get("fruiting"), p.get("pruning")])]
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
# Build de cada zona (Todo / Frente / Fondo)
# ============================================================
def build_zone(zone_name, zone_label, plants_in_view, ideas_list, show_huerta_locations, img_data):
    """
    plants_in_view: lista de plantas a mostrar (frente, fondo, o todas).
    ideas_list: lista de ideas nuevas a mostrar (puede ser combinación frente+fondo).
    show_huerta_locations: si True, muestra el intro con opciones de espacios para huerta
        (más apropiado para "fondo" y "todo"). Si False, muestra el intro corto del frente.
    """
    info_cards = "\n".join(render_plant_info_card(p, img_data) for p in plants_in_view)
    care_cards = "\n".join(render_plant_care_card(p) for p in plants_in_view)
    new_ideas = "\n".join(render_idea_card(i) for i in ideas_list)
    huerta_cards = "\n".join(render_huerta_card(h) for h in HUERTA)
    if zone_name == "interior":
        huerta_intro = """
<div class="frente-huerta-intro">
  <h3>🪴 Comestibles en interior</h3>
  <p>Adentro no hay huerta clásica, pero podés sumar aromáticas en macetas (albahaca, perejil, ciboulette, menta) cerca de ventanas con luz indirecta brillante. También plantas comestibles tropicales (jengibre, cúrcuma) y micro-greens en bandejas.</p>
</div>"""
    elif show_huerta_locations:
        huerta_intro = render_huerta_locations()
    else:
        huerta_intro = """
<div class="frente-huerta-intro">
  <h3>🌿 Aromáticas para el frente</h3>
  <p>El frente no es ideal para huerta clásica (visibilidad, espacio limitado). Pero podés sumar aromáticas y comestibles ornamentales que decoran y se cosechan.</p>
</div>"""
    cal_grid = render_calendar_grid(plants_in_view)

    # Mapa subtab — vista aérea de la zona
    aerials_by_zone = {
        "frente": [("Aerea_Frente.png", "Vista aérea del frente — desde el techo mirando hacia la calle")],
        "fondo":  [("Aerea_Fondo.png",  "Vista aérea del fondo — desde el techo mirando hacia la pileta y el padel")],
        "todo":   [
            ("Aerea_Frente.png", "Frente — desde el techo mirando hacia la calle"),
            ("Aerea_Fondo.png",  "Fondo — desde el techo mirando hacia la pileta y el padel"),
        ],
        "interior": [],
    }
    aerial_imgs = aerials_by_zone.get(zone_name, [])
    if aerial_imgs:
        map_blocks = "\n".join(
            f'<figure class="map-figure">'
            f'<img class="map-photo" data-img="{esc(fname)}" data-action="lightbox" alt="{esc(caption)}">'
            f'<figcaption>{esc(caption)}</figcaption>'
            f'</figure>'
            for fname, caption in aerial_imgs
        )
    else:
        map_blocks = (
            '<div class="map-empty">'
            '<p>📐 Esta zona no tiene vista aérea (las plantas viven adentro).</p>'
            '</div>'
        )

    return f"""
<section class="zone-content" data-zone="{zone_name}">
  <nav class="subtab-nav">
    <button class="subtab-btn active" data-sub="info">🪴 Info</button>
    <button class="subtab-btn" data-sub="map">📐 Mapa</button>
    <button class="subtab-btn" data-sub="care">✂️ Cuidado</button>
    <button class="subtab-btn" data-sub="new">💡 Ideas</button>
    <button class="subtab-btn" data-sub="cal">📅 Calendario</button>
  </nav>

  <div class="subtab-pane active" data-sub="info">
    <div class="filter-bar">
      <input type="text" class="search" placeholder="🔍 Buscar planta...">
      <button class="filter-toggle" data-zone="{zone_name}" aria-expanded="false" aria-label="Filtrar por categoría" type="button">
        <svg class="filter-svg" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M3 5h18l-7 9v5l-4-2v-3L3 5z" fill="currentColor"/></svg>
        <span class="filter-current">Todas</span>
        <span class="filter-caret" aria-hidden="true">▾</span>
      </button>
    </div>
    <div class="filter-panel" data-zone="{zone_name}" hidden>
      <button class="ftag active" data-filter="all">Todas</button>
      <button class="ftag" data-filter="nativa">🇺🇾 Nativas</button>
      <button class="ftag" data-filter="frutal">🍑 Frutales</button>
      <button class="ftag" data-filter="aromatica">🌿 Aromáticas</button>
      <button class="ftag" data-filter="ornamental">✨ Ornamentales</button>
      <button class="ftag" data-filter="trepadora">🌿 Trepadoras</button>
      <button class="ftag" data-filter="polinizadores">🐝 Polinizadores</button>
      <button class="ftag" data-filter="pendiente">⏳ Pendientes</button>
    </div>
    <div class="cards-grid">{info_cards}</div>
  </div>

  <div class="subtab-pane" data-sub="map">
    <div class="ideas-intro">
      <h3>📐 Vista aérea</h3>
      <p>Tomada desde el techo. Click en cada foto para verla en grande.</p>
    </div>
    <div class="map-container">{map_blocks}</div>
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

    <div class="ideas-huerta-divider">
      {huerta_intro}
      <div class="cards-grid huerta-grid">{huerta_cards}</div>
    </div>
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
      <button class="btn-settings" id="btn-open-settings" aria-label="Configuración">⚙️</button>
    </div>
  </div>

  <div class="timeline-summary" id="timeline-summary"></div>
  <div class="sync-status-bar" id="sync-status-bar" data-state="disabled" hidden>
    <span class="sync-dot"></span>
    <span class="sync-label" id="sync-label">Sync deshabilitado</span>
    <button class="sync-retry-btn" id="sync-retry-btn" hidden>↻ Reintentar</button>
  </div>
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
</div>

<!-- Modal: Detalle de especie -->
<div class="modal species-modal" id="species-detail-modal">
  <div class="modal-content species-modal-content">
    <div id="species-detail-body"></div>
  </div>
</div>

<!-- Modal: Subir foto en especie -->
<div class="modal" id="species-photo-modal">
  <div class="modal-content modal-wide">
    <button class="modal-close" data-close="species-photo">✕</button>
    <h3>📷 Sumar foto al catálogo</h3>
    <p class="task-photo-name" id="species-photo-name"></p>

    <div class="task-photo-stage" data-stage="setup" hidden>
      <div class="task-photo-warning">
        ⚠️ Necesitás configurar tu GitHub Personal Access Token antes de subir fotos.
      </div>
      <button class="btn-primary" id="btn-species-photo-go-settings">⚙️ Ir a Configuración</button>
    </div>

    <div class="task-photo-stage" data-stage="pick">
      <div class="task-photo-buttons">
        <label class="task-photo-btn">
          <input type="file" accept="image/*" capture="environment" id="species-photo-camera-input" class="visually-hidden">
          <span class="task-photo-btn-emoji">📸</span>
          <span class="task-photo-btn-label">Sacá una foto</span>
        </label>
        <label class="task-photo-btn">
          <input type="file" accept="image/*" id="species-photo-gallery-input" class="visually-hidden">
          <span class="task-photo-btn-emoji">🖼️</span>
          <span class="task-photo-btn-label">Subí una existente</span>
        </label>
      </div>
    </div>

    <div class="task-photo-stage" data-stage="preview" hidden>
      <div class="task-photo-preview-wrap">
        <canvas id="species-photo-canvas"></canvas>
      </div>
      <label class="settings-label" style="margin-top: 10px;">
        <strong>Nota corta (opcional)</strong>
        <span class="settings-hint">Aparece como tooltip al pasar el mouse en la galería.</span>
      </label>
      <input type="text" id="species-photo-note" class="settings-input" maxlength="120" placeholder="Ej: floración temprana, cambio de color...">
      <div class="task-photo-actions" style="margin-top: 10px;">
        <button class="btn-secondary" id="btn-species-photo-change">↺ Cambiar foto</button>
        <button class="btn-primary" id="btn-species-photo-upload">📤 Subir al catálogo</button>
      </div>
    </div>

    <div class="task-photo-stage" data-stage="result" hidden>
      <div class="task-photo-result" id="species-photo-result"></div>
    </div>
  </div>
</div>

<!-- Modal: Subir foto en tarea -->
<div class="modal" id="task-photo-modal">
  <div class="modal-content modal-wide">
    <button class="modal-close" data-close="task-photo">✕</button>
    <h3>📷 Subir foto a la tarea</h3>
    <p class="task-photo-name" id="task-photo-name"></p>

    <!-- Pantalla 1: setup falta -->
    <div class="task-photo-stage" data-stage="setup" hidden>
      <div class="task-photo-warning">
        ⚠️ Necesitás configurar tu GitHub Personal Access Token antes de subir fotos.
      </div>
      <button class="btn-primary" id="btn-photo-go-settings">⚙️ Ir a Configuración</button>
    </div>

    <!-- Pantalla 2: elegir foto -->
    <div class="task-photo-stage" data-stage="pick">
      <div class="task-photo-buttons">
        <label class="task-photo-btn">
          <input type="file" accept="image/*" capture="environment" id="task-photo-camera-input" class="visually-hidden">
          <span class="task-photo-btn-emoji">📸</span>
          <span class="task-photo-btn-label">Sacá una foto</span>
        </label>
        <label class="task-photo-btn">
          <input type="file" accept="image/*" id="task-photo-gallery-input" class="visually-hidden">
          <span class="task-photo-btn-emoji">🖼️</span>
          <span class="task-photo-btn-label">Subí una existente</span>
        </label>
      </div>
    </div>

    <!-- Pantalla 3: preview + confirmar -->
    <div class="task-photo-stage" data-stage="preview" hidden>
      <div class="task-photo-preview-wrap">
        <canvas id="task-photo-canvas"></canvas>
      </div>
      <p class="task-photo-overlay-note">
        🏷️ La foto incluye un overlay con el ID de la tarea, fecha y título corto. Sirve para identificarla después.
      </p>
      <div class="task-photo-actions">
        <button class="btn-secondary" id="btn-photo-change">↺ Cambiar foto</button>
        <button class="btn-primary" id="btn-photo-upload">📤 Subir al repo</button>
      </div>
    </div>

    <!-- Pantalla 4: subiendo / éxito / error -->
    <div class="task-photo-stage" data-stage="result" hidden>
      <div class="task-photo-result" id="task-photo-result"></div>
    </div>
  </div>
</div>

<!-- Modal: Configuración (GitHub PAT + device name) -->
<div class="modal" id="settings-modal">
  <div class="modal-content modal-wide">
    <button class="modal-close" data-close="settings">✕</button>
    <h3>⚙️ Configuración</h3>
    <p class="settings-intro">
      Estos datos se guardan SOLO en este navegador (localStorage). Nunca se suben al repo ni se comparten entre dispositivos.
    </p>

    <div class="settings-section">
      <label class="settings-label" for="settings-github-token">
        <strong>GitHub Personal Access Token</strong>
        <span class="settings-hint">Habilita subir fotos al repo y sincronizar el estado entre dispositivos.</span>
      </label>
      <input type="password" id="settings-github-token" class="settings-input" placeholder="github_pat_...">
      <details class="settings-details">
        <summary>¿Cómo genero un PAT?</summary>
        <ol class="settings-steps">
          <li>Andá a <a href="https://github.com/settings/personal-access-tokens" target="_blank" rel="noopener">github.com/settings/personal-access-tokens</a></li>
          <li>Click "Generate new token" → "Fine-grained".</li>
          <li>Repository access: solo <code>abecedeefege/gardening</code>.</li>
          <li>Permisos: <code>Contents: Read and write</code>.</li>
          <li>Expiración: la que prefieras (90 días default).</li>
          <li>Copiá el token y pegalo acá.</li>
        </ol>
      </details>
      <div class="settings-actions">
        <button class="btn-secondary" id="btn-test-github-token">Probar conexión</button>
        <button class="btn-secondary btn-danger" id="btn-clear-github-token">🗑 Eliminar</button>
      </div>
      <div class="settings-feedback" id="settings-github-feedback"></div>
    </div>

    <div class="settings-section">
      <label class="settings-label" for="settings-device-name">
        <strong>Nombre de este dispositivo</strong>
        <span class="settings-hint">Aparece en los commits de sync para saber desde qué device se hizo cada cambio.</span>
      </label>
      <input type="text" id="settings-device-name" class="settings-input" placeholder="iPhone-Lucia / Laptop-Casa">
    </div>

    <div class="settings-section">
      <label class="settings-label" for="settings-canonical-url">
        <strong>URL canónica del sitio</strong>
        <span class="settings-hint">Para que los links de transferencia funcionen siempre, pegá la URL <em>estable</em> del sitio (no una preview de Vercel ni un dominio temporal). Ej: tu URL de GitHub Pages o tu dominio principal de Vercel.</span>
      </label>
      <input type="url" id="settings-canonical-url" class="settings-input" placeholder="https://tu-sitio.vercel.app/ o https://usuario.github.io/Gardening/">
      <div class="settings-feedback" id="settings-canonical-feedback"></div>
    </div>

    <div class="settings-section" id="settings-transfer-section" hidden>
      <label class="settings-label">
        <strong>📲 Transferir a otro device</strong>
        <span class="settings-hint">Generá un QR + link de uso único que carga el token en el otro device sin que tengas que tipearlo.</span>
      </label>
      <button class="btn-secondary" id="btn-gen-transfer-link">Generar QR + link de transferencia</button>
      <div id="transfer-link-output" hidden>
        <div class="transfer-warn">
          ⚠️ El QR y el link contienen tu PAT en claro. <strong>Mostralo solo a tu otro device</strong>. Si usás link, mandátelo solo a vos mismo y borralo del historial cuando termines.
        </div>
        <div class="transfer-qr-wrap">
          <div id="transfer-qr"></div>
          <p class="transfer-qr-hint">📷 Escaneá con la cámara del otro device.</p>
        </div>
        <div class="transfer-or">— o copiá el link —</div>
        <textarea id="transfer-link-text" readonly rows="3"></textarea>
        <div class="transfer-actions">
          <button class="btn-secondary" id="btn-copy-transfer-link">📋 Copiar al portapapeles</button>
        </div>
        <div class="transfer-hint">
          Cuando lo abras en el otro device, te pregunta si querés importar el token y lo guarda en ese navegador. El token se borra de la URL apenas se importa.
        </div>
      </div>
    </div>

    <div class="settings-footer">
      <button class="btn-primary" id="btn-save-settings">💾 Guardar</button>
    </div>
  </div>
</div>"""


# ============================================================
# OG IMAGES + TASK PAGES (para WhatsApp / Facebook previews)
# ============================================================
def build_og_image(src_path: Path, dst_path: Path):
    """
    Genera una imagen 1200x630 (estándar Open Graph) con la foto de la tarea
    centrada y recortada estilo 'cover'.
    """
    target_w, target_h = 1200, 630
    img = Image.open(src_path).convert("RGB")

    # Resize escalando para "cover" (la imagen llena todo el target)
    src_ratio = img.width / img.height
    target_ratio = target_w / target_h
    if src_ratio > target_ratio:
        # imagen más ancha — escalar por altura, recortar lados
        new_h = target_h
        new_w = int(target_h * src_ratio)
    else:
        new_w = target_w
        new_h = int(target_w / src_ratio)

    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Crop centrado
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    img = img.crop((left, top, left + target_w, top + target_h))

    img.save(dst_path, "JPEG", quality=82, optimize=True)


def build_task_page(task: dict, plant: dict | None):
    """
    Genera docs/tasks/{taskId}.html con OG meta tags específicos para esa tarea.
    Esta página al ser abierta en navegador redirige al index principal.
    Cuando se comparte el link por WhatsApp, los OG tags muestran el preview correcto.
    """
    task_id = task["id"]
    title = f"{task['title']} — {task['plant_common']}"

    # Description corta para OG (max ~200 chars).
    # Prefiere short_desc → detail → description.
    src = task.get("short_desc") or task.get("detail") or task.get("description", "")
    if len(src) > 200:
        desc = src[:197].rsplit(" ", 1)[0] + "..."
    else:
        desc = src

    # OG image absoluta
    og_img_filename = f"{task_id}.jpg"
    og_image_url = f"{SITE_URL}/og/{og_img_filename}" if SITE_URL else ""
    page_url = f"{SITE_URL}/tasks/{task_id}.html" if SITE_URL else ""

    # Si no hay foto de planta, og_image queda vacío (no agregamos meta)
    has_og_image = task.get("plant_photo") and (IMAGES_DIR / task["plant_photo"]).exists()

    og_image_meta = ""
    if has_og_image and SITE_URL:
        og_image_meta = f"""
  <meta property="og:image" content="{esc(og_image_url)}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{esc(task['plant_common'])}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{esc(og_image_url)}">"""

    page_url_meta = f'  <meta property="og:url" content="{esc(page_url)}">' if page_url else ""

    redirect_target = f"../index.html#task={task_id}"

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{esc(title)} · Jardineando · Pacha Mama</title>
<meta name="description" content="{esc(desc)}">

<meta property="og:type" content="article">
<meta property="og:site_name" content="Jardineando · Pacha Mama">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
{page_url_meta}
{og_image_meta}

<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">

<meta http-equiv="refresh" content="0; url={redirect_target}">
<link rel="canonical" href="{esc(page_url) if page_url else redirect_target}">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; padding: 40px; max-width: 600px; margin: 0 auto; text-align: center; color: #3f3f46; }}
  h1 {{ color: #15803d; font-size: 1.4rem; }}
  a {{ color: #2563eb; }}
</style>
</head>
<body>
<h1>🌿 Jardineando · Pacha Mama</h1>
<p>Redirigiendo a la tarea...</p>
<p><strong>{esc(title)}</strong></p>
<p><a href="{redirect_target}">Si no se redirige automáticamente, hacé click acá</a></p>
<script>window.location.replace("{redirect_target}");</script>
</body>
</html>"""

    out_path = TASKS_DIR / f"{task_id}.html"
    out_path.write_text(html, encoding="utf-8")
    return out_path


# ============================================================
# Main
# ============================================================
def main():
    # 1. Cargar imágenes
    unique_files = set()
    for p in PLANTS:
        if p.get("loc_photo"): unique_files.add(p["loc_photo"])
        if p.get("main_photo"): unique_files.add(p["main_photo"])
        for fname in p.get("gallery", []) or []:
            if fname: unique_files.add(fname)

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

    # 2.5 Generar páginas OG por tarea + imágenes OG (1200x630)
    if SITE_URL and "YOUR-USERNAME" not in SITE_URL:
        og_count = 0
        page_count = 0
        plant_by_first_id = {p["id_codes"][0]: p for p in PLANTS}
        for task in tasks:
            plant = plant_by_first_id.get(task["plant_codes"][0])
            # Imagen OG si hay foto disponible
            if task.get("plant_photo"):
                src = IMAGES_DIR / task["plant_photo"]
                if src.exists():
                    dst = OG_DIR / f"{task['id']}.jpg"
                    build_og_image(src, dst)
                    og_count += 1
            build_task_page(task, plant)
            page_count += 1
        print(f"🔗 Páginas OG generadas: {page_count} (con imagen: {og_count})")
    else:
        print("⚠️  SITE_URL no configurado — páginas OG no generadas.")
        print("   Editá build.py y poné tu URL de GitHub Pages para activarlas.")

    # 3. Stats
    total_plants = len(PLANTS)
    total_native = sum(1 for p in PLANTS if "nativa" in p["tags"])
    total_frutal = sum(1 for p in PLANTS if "frutal" in p["tags"])
    total_urgent = sum(1 for p in PLANTS if p.get("urgency"))

    # Stats ticker — items rotativos para el bloque informativo
    def count_tag(tag):
        return sum(1 for p in PLANTS if tag in p.get("tags", []))

    def count_type_starts(prefix):
        # "perenne (a confirmar)" cuenta como perenne; "semi-perenne" se evalúa antes que "perenne"
        if prefix == "perenne":
            return sum(1 for p in PLANTS if p.get("type", "").startswith("perenne"))
        if prefix == "semi-perenne":
            return sum(1 for p in PLANTS if p.get("type", "").startswith("semi-perenne"))
        if prefix == "caduco":
            return sum(1 for p in PLANTS if p.get("type", "").startswith("caduco"))
        return 0

    ticker_raw = [
        ("🌱", total_plants,                       "especies"),
        ("🇺🇾", count_tag("nativa"),              "nativas"),
        ("🌍", count_tag("exotica"),               "exóticas"),
        ("🍑", count_tag("frutal"),                "frutales"),
        ("🌿", count_tag("aromatica"),             "aromáticas"),
        ("✨", count_tag("ornamental"),            "ornamentales"),
        ("🌿", count_tag("trepadora"),             "trepadoras"),
        ("🐝", count_tag("polinizadores"),         "polinizadoras"),
        ("🐝", count_tag("abejas"),                "para abejas"),
        ("🦋", count_tag("mariposas"),             "para mariposas"),
        ("👃", count_tag("perfume"),               "con perfume"),
        ("🌲", count_type_starts("perenne"),       "perennes"),
        ("🍃", count_type_starts("semi-perenne"),  "semi-perennes"),
        ("🍂", count_type_starts("caduco"),        "caducas"),
    ]
    # Filtrar items con count=0 — no tiene sentido rotar a "0 mariposas"
    stats_ticker = [
        {"emoji": e, "count": c, "label": l}
        for (e, c, l) in ticker_raw if c > 0
    ]

    # 4. Build zonas
    frente_plants = [p for p in PLANTS if p["zone"] == "frente"]
    fondo_plants = [p for p in PLANTS if p["zone"] == "fondo"]
    interior_plants = [p for p in PLANTS if p["zone"] == "interior"]

    todo_html = build_zone(
        "todo", "Todo el jardín", PLANTS,
        ideas_list=NEW_IDEAS_FRENTE + NEW_IDEAS_FONDO,
        show_huerta_locations=True, img_data=img_data,
    )
    frente_html = build_zone(
        "frente", "Frente", frente_plants,
        ideas_list=NEW_IDEAS_FRENTE,
        show_huerta_locations=False, img_data=img_data,
    )
    fondo_html = build_zone(
        "fondo", "Fondo", fondo_plants,
        ideas_list=NEW_IDEAS_FONDO,
        show_huerta_locations=True, img_data=img_data,
    )
    interior_html = build_zone(
        "interior", "Interior", interior_plants,
        ideas_list=[],
        show_huerta_locations=False, img_data=img_data,
    )
    timeline_html = build_timeline_view(tasks, img_data)

    # 5. Inyectar datos como JSON para el JS
    img_js = "const IMG = " + json.dumps(img_data) + ";"
    tasks_js = "const TASKS = " + json.dumps(tasks, ensure_ascii=False) + ";"

    # PLANTS_INFO — info por planta para el modal de detalle (no incluye urgencies,
    # esas viven en TASKS y se filtran por plant_codes desde el JS).
    plants_info = []
    for p in PLANTS:
        plants_info.append({
            "id_codes": p["id_codes"],
            "zone": p["zone"],
            "common": p.get("common", ""),
            "sci": p.get("sci", ""),
            "charrua": p.get("charrua", ""),
            "other_names": p.get("other_names", ""),
            "desc": p.get("desc", ""),
            "type": p.get("type", ""),
            "fun_fact": p.get("fun_fact", ""),
            "prune_when": p.get("prune_when", ""),
            "prune_how": p.get("prune_how", ""),
            "water": p.get("water", ""),
            "light": p.get("light", ""),
            "tags": p.get("tags", []),
            "main_photo": p.get("main_photo", ""),
            "loc_photo": p.get("loc_photo", ""),
            "gallery": p.get("gallery", []),
            "flowering": p.get("flowering", []),
            "fruiting": p.get("fruiting", []),
            "pruning": p.get("pruning", []),
        })
    plants_info_js = "const PLANTS_INFO = " + json.dumps(plants_info, ensure_ascii=False) + ";"

    contacts_js = "const DEFAULT_CONTACTS = " + json.dumps(DEFAULT_CONTACTS, ensure_ascii=False) + ";"
    templates_js = "const WHATSAPP_TEMPLATES = " + json.dumps(WHATSAPP_TEMPLATES_BY_ACTION, ensure_ascii=False) + ";"
    ticker_js = "const STATS_TICKER = " + json.dumps(stats_ticker, ensure_ascii=False) + ";"

    # Marquee del ticker — render server-side de TODOS los items, duplicados
    # para que el loop de la animación CSS (translateX -50%) sea seamless.
    ticker_html_inner = "".join(
        f'<span class="ticker-item">'
        f'<span class="ticker-emoji">{esc(item["emoji"])}</span>'
        f'<strong>{item["count"]}</strong> '
        f'<span class="ticker-label">{esc(item["label"])}</span>'
        f'</span>'
        for item in stats_ticker
    )
    ticker_aria = "Catálogo: " + " · ".join(
        f'{item["count"]} {item["label"]}' for item in stats_ticker
    )
    site_url_js = "const SITE_URL = " + json.dumps(SITE_URL if SITE_URL and "YOUR-USERNAME" not in SITE_URL else "") + ";"

    # 6. HTML final
    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Jardineando · Pacha Mama</title>
<meta name="description" content="Catálogo y timeline de tareas del jardín Pacha Mama (Montevideo). 48 plantas, calendario anual, fotos.">
<meta name="theme-color" content="#2d5016">

<!-- Favicons -->
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="icon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">

<!-- PWA -->
<link rel="manifest" href="manifest.webmanifest">

<!-- Open Graph / WhatsApp / Twitter -->
<meta property="og:type" content="website">
<meta property="og:title" content="Jardineando · Pacha Mama">
<meta property="og:description" content="Catálogo y timeline de tareas del jardín Pacha Mama (Montevideo).">
<meta property="og:image" content="og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="og-image.png">

<style>{CSS}</style>
</head>
<body class="zone-todo">
<div class="container container-top">
  <header class="main-header">
    <h1 class="brand"><img class="brand-logo" src="icon-96.png" alt="" width="40" height="40"> Jardineando</h1>
    <h2 class="subbrand">Pacha Mama</h2>
  </header>

  <div class="weather-line" id="weather-line">
    <span class="weather-cell"><span class="weather-emoji">🌱</span><span class="weather-val">…</span></span>
    <span class="weather-cell"><span class="weather-emoji">💨</span><span class="weather-val">…</span></span>
    <span class="weather-cell"><span class="weather-emoji">💧</span><span class="weather-val">…</span></span>
    <span class="weather-cell"><span class="weather-emoji">📍</span><span class="weather-val">Montevideo</span></span>
  </div>

  <div class="stats-ticker" aria-label="{ticker_aria}">
    <div class="ticker-track">{ticker_html_inner}{ticker_html_inner}</div>
  </div>

  <nav class="main-tabs">
    <button class="tab-btn active" data-zone="todo"><span class="tab-emoji">🏡</span><span class="tab-label">Todo</span></button>
    <button class="tab-btn" data-zone="frente"><span class="tab-emoji">🌳</span><span class="tab-label">Frente</span></button>
    <button class="tab-btn" data-zone="fondo"><span class="tab-emoji">🏊</span><span class="tab-label">Fondo</span></button>
    <button class="tab-btn" data-zone="interior"><span class="tab-emoji">🪴</span><span class="tab-label">Interior</span></button>
  </nav>

  <div class="todo-strip">
    <button class="todo-btn" data-zone="timeline"><span aria-hidden="true">📋</span> Tareas</button>
    <span class="todo-label" id="todo-count">…</span>
  </div>
</div>

<div class="container container-zones">
  {todo_html.replace('class="zone-content"', 'class="zone-content active"', 1)}
  {frente_html}
  {fondo_html}
  {interior_html}
  <div class="zone-content" data-zone="timeline">{timeline_html.split('<section class="zone-content" data-zone="timeline">', 1)[1].split('</section>', 1)[0]}</div>
  {timeline_html.split('</section>', 1)[1]}
</div>

<div class="lightbox" id="lightbox">
  <img id="lightbox-img" alt="">
</div>

<script>
{img_js}
{tasks_js}
{plants_info_js}
{contacts_js}
{templates_js}
{ticker_js}
{site_url_js}
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
