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
from data_improvements import IMPROVEMENTS
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
SITE_URL = "https://gardening-chi.vercel.app"


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


def copy_curated_image(src: Path, dst: Path, max_width: int = 800, quality: int = 78) -> None:
    """Resize una imagen curada y escribirla a dst preservando el formato del
    archivo de origen (jpg/jpeg/webp/png). Las imágenes curadas se cachean
    por el browser y se comparten entre las distintas páginas del sitio."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    ext = src.suffix.lower().lstrip(".")
    fmt_map = {"jpg": "JPEG", "jpeg": "JPEG", "webp": "WEBP", "png": "PNG"}
    fmt = fmt_map.get(ext, "JPEG")
    img = Image.open(src)
    if fmt in ("JPEG", "WEBP"):
        img = img.convert("RGB")
    if img.width > max_width:
        ratio = max_width / img.width
        img = img.resize((max_width, int(img.height * ratio)), Image.Resampling.LANCZOS)
    save_kwargs = {"format": fmt, "optimize": True}
    if fmt in ("JPEG", "WEBP"):
        save_kwargs["quality"] = quality
    img.save(dst, **save_kwargs)


def esc(s):
    return html_mod.escape(str(s) if s is not None else "", quote=True)


MONTH_NAMES = ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
MONTH_FULL = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# ============================================================
# Mes actual (hemisferio sur — Montevideo)
# ============================================================
import re

CURRENT_MONTH = date.today().month
CURRENT_MONTH_NAME = MONTH_FULL[CURRENT_MONTH]

_MONTH_NAME_TO_NUM = {n: i for i, n in enumerate(MONTH_FULL) if n}
_SEASON_TO_MONTHS = {
    "otoño": [3, 4, 5],
    "otono": [3, 4, 5],
    "invierno": [6, 7, 8],
    "primavera": [9, 10, 11],
    "verano": [12, 1, 2],
}
_MONTH_RE = "(" + "|".join(_MONTH_NAME_TO_NUM.keys()) + ")"


def parse_planting_months(text):
    """Extrae los meses de plantación posibles de un string libre tipo
    'Otoño (abril-mayo) o primavera temprana (agosto-septiembre)'.
    Devuelve un set de números de mes (1-12)."""
    if not text:
        return set()
    text = text.lower().strip()
    if "cualquier época" in text or "cualquier epoca" in text:
        return set(range(1, 13))
    months = set()
    for m in re.finditer(_MONTH_RE + r"\s*-\s*" + _MONTH_RE, text):
        a = _MONTH_NAME_TO_NUM[m.group(1)]
        b = _MONTH_NAME_TO_NUM[m.group(2)]
        if a <= b:
            months.update(range(a, b + 1))
        else:
            months.update(list(range(a, 13)) + list(range(1, b + 1)))
    for m in re.finditer(r"\b" + _MONTH_RE + r"\b", text):
        months.add(_MONTH_NAME_TO_NUM[m.group(1)])
    for season, mnths in _SEASON_TO_MONTHS.items():
        if season in text:
            months.update(mnths)
    return months


def idea_is_optimal_now(idea):
    """Bool para NEW_IDEAS — usa el campo `season_plant`."""
    return CURRENT_MONTH in parse_planting_months(idea.get("season_plant", ""))


def huerta_is_optimal_now(h):
    """Bool para HUERTA — usa los arrays `siembra` y `transplante`."""
    return CURRENT_MONTH in (h.get("siembra", []) or []) or CURRENT_MONTH in (h.get("transplante", []) or [])


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
TYPE_BADGES = {
    "caduco": "🍂 Caduco",
    "perenne": "🌲 Perenne",
    "semi-perenne": "🍃 Semi-perenne",
    "semi-caduco": "🍃 Semi-caduco",
}


def render_card_chips(p):
    """Tags coloreados + type badge — una sola línea de chips reutilizable
    por la card de zona y por el hero del modal de detalle."""
    tag_html = render_tags(p.get("tags", []))
    raw_type = p.get("type", "")
    type_label = TYPE_BADGES.get(raw_type, raw_type)
    type_html = (
        f'<span class="card-type-chip">{esc(type_label)}</span>' if type_label else ''
    )
    return tag_html + type_html


def render_plant_info_card(p, img_data):
    has_main = bool(p.get("main_photo") and img_data.get(p.get("main_photo")))
    primary_code = p["id_codes"][0]
    loc_codes = ", ".join(p["id_codes"])
    photo_html = (
        f'<img class="card-photo" data-img="{esc(p["main_photo"])}" '
        f'data-action="open-species" data-plant-code="{esc(primary_code)}" alt="">'
        if has_main else ''
    )

    other_html = (
        f'<div class="card-other">↳ {esc(p["other_names"])}</div>'
        if p.get("other_names") and p["other_names"] != "—" else ''
    )

    chips_html = render_card_chips(p)

    return f"""
<article class="plant-card" data-plant-id="{esc(loc_codes)}" data-name="{esc(p['common'].lower())}" data-tags="{esc(' '.join(p['tags']))}">
  <div class="card-photo-wrap" data-action="open-species" data-plant-code="{esc(primary_code)}">
    {photo_html}
    <div class="card-overlay">
      <h3 class="card-title">{esc(p['common'])}</h3>
      <div class="card-overlay-bottom">
        <div class="card-sci">{esc(p['sci'])}</div>
        {other_html}
        <div class="card-chips">{chips_html}</div>
      </div>
    </div>
  </div>
</article>"""


def render_curiosidades_section(plants_in_view, img_data):
    """Feed de curiosidades verificadas (campo fun_fact de cada planta).
    Promovido desde la proposal 2026-06-12-curiosidades — el formato
    'historia con nombre propio + dato contraintuitivo' fue el que más
    enganchó. Cada card linkea al modal de especie (data-action=open-species),
    que también muestra el fun_fact en su ficha completa."""
    cards = []
    for p in plants_in_view:
        ff = p.get("fun_fact", "")
        if not ff or ff == "—":
            continue
        primary_code = p["id_codes"][0]
        has_main = bool(p.get("main_photo") and img_data.get(p.get("main_photo")))
        thumb = (
            f'<img class="curio-thumb" data-img="{esc(p["main_photo"])}" '
            f'data-action="open-species" data-plant-code="{esc(primary_code)}" alt="">'
            if has_main else '<div class="curio-thumb curio-thumb-empty">🌿</div>'
        )
        cards.append(f"""
<article class="curio-card" data-name="{esc(p['common'].lower())}" data-tags="{esc(' '.join(p['tags']))}">
  <div class="curio-head" data-action="open-species" data-plant-code="{esc(primary_code)}">
    {thumb}
    <div class="curio-titles">
      <h3 class="curio-name">{esc(p['common'])}</h3>
      <div class="curio-sci">{esc(p['sci'])}</div>
    </div>
  </div>
  <p class="curio-fact">💡 {esc(ff)}</p>
</article>""")
    if not cards:
        return '<p class="curio-empty">Todavía no hay curiosidades cargadas para esta zona.</p>'
    intro = (
        '<div class="ideas-intro">'
        '<h3>💡 Curiosidades de tus plantas</h3>'
        '<p>Historias verificadas de cada especie del jardín. Tocá una para ver su ficha completa.</p>'
        '</div>'
    )
    return intro + f'<div class="curio-grid">{"".join(cards)}</div>'


def render_idea_card(idea):
    season = f'<div class="idea-season">📅 <strong>Plantar:</strong> {esc(idea["season_plant"])}</div>' if "season_plant" in idea else ''
    where = f'<div class="idea-where">📍 <strong>Dónde:</strong> {esc(idea["where"])}</div>' if "where" in idea else ''
    size = f'<div class="idea-size">📐 <strong>Tamaño:</strong> {esc(idea["size"])}</div>' if "size" in idea else ''
    is_now = idea_is_optimal_now(idea)
    now_class = " is-now" if is_now else ""
    now_badge = f'<div class="now-badge">📅 Óptimo plantar AHORA ({esc(CURRENT_MONTH_NAME)})</div>' if is_now else ''

    return f"""
<article class="idea-card{now_class}" data-name="{esc(idea['common'].lower())}" data-tags="{esc(' '.join(idea.get('tags', [])))}">
  {now_badge}
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
            f'<div class="hcell {"active" if m in months else ""} {"current" if m == CURRENT_MONTH else ""}" style="--c:{color}" title="{MONTH_FULL[m]}">{MONTH_NAMES[m]}</div>'
            for m in range(1, 13)
        )
        return f'<div class="hbar"><div class="hbar-label">{label}</div><div class="hbar-cells">{bars}</div></div>'

    cal_html = ""
    if h.get("siembra"): cal_html += month_bar(h["siembra"], "#16a34a", "🌱 Siembra")
    if h.get("transplante"): cal_html += month_bar(h["transplante"], "#0d9488", "🪴 Trasplante")
    if h.get("cosecha"): cal_html += month_bar(h["cosecha"], "#d97706", "🧺 Cosecha")

    is_now = huerta_is_optimal_now(h)
    now_class = " is-now" if is_now else ""
    if CURRENT_MONTH in (h.get("siembra", []) or []):
        now_label = f"🌱 Sembrá AHORA ({esc(CURRENT_MONTH_NAME)})"
    elif CURRENT_MONTH in (h.get("transplante", []) or []):
        now_label = f"🪴 Trasplantá AHORA ({esc(CURRENT_MONTH_NAME)})"
    else:
        now_label = ""
    now_badge = f'<div class="now-badge">{now_label}</div>' if is_now else ''

    return f"""
<article class="huerta-card{now_class}" data-name="{esc(h['common'].lower())}" data-tags="{esc(' '.join(h.get('tags', [])))}">
  {now_badge}
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


TIER_META = {
    "free":       ("🆓", "Gratis",          "#16a34a", "tier-free"),
    "under_10":   ("💵", "Menos de USD 10", "#ca8a04", "tier-under10"),
    "under_100":  ("💰", "Menos de USD 100","#ea580c", "tier-under100"),
}
TIER_ORDER = ["free", "under_10", "under_100"]


def render_improvement_card(imp):
    tier_emoji, tier_label, _, tier_class = TIER_META[imp["tier"]]
    cost = imp.get("cost_usd", 0)
    cost_text = "Gratis" if cost == 0 else f"~USD {cost}"

    def block(icon, label, key):
        val = imp.get(key)
        if not val:
            return ""
        return f'<div class="improvement-line"><strong>{icon} {label}:</strong> {esc(val)}</div>'

    applies = ""
    if imp.get("applies_to"):
        chips = "".join(
            f'<button type="button" class="improvement-applies-chip" '
            f'data-action="open-species" data-plant-code="{esc(code)}">'
            f'{esc(code)}</button>'
            for code in imp["applies_to"]
        )
        applies = f'<div class="improvement-applies"><strong>🪴 Aplica a:</strong> {chips}</div>'

    return f"""
<article class="improvement-card {tier_class}" data-name="{esc(imp['title'].lower())}" data-tags="{esc(' '.join(imp.get('tags', [])))}">
  <div class="improvement-header">
    <span class="tier-badge {tier_class}">{tier_emoji} {esc(tier_label)}</span>
    <span class="improvement-cost">{esc(cost_text)}</span>
  </div>
  <h3 class="improvement-title">{esc(imp['title'])}</h3>
  <div class="improvement-category">{esc(imp.get('category', ''))}</div>
  {block('🛒', 'Qué', 'what')}
  {block('💚', 'Por qué', 'why')}
  {block('🔧', 'Cómo', 'how')}
  {block('📅', 'Cuándo', 'when')}
  {block('📍', 'Dónde comprar', 'where_buy')}
  {applies}
</article>"""


def render_improvements_section(zone_name):
    if zone_name == "todo":
        # Vista global: todas las mejoras de todas las zonas
        relevant = list(IMPROVEMENTS)
    else:
        relevant = [
            imp for imp in IMPROVEMENTS
            if imp["zone"] == zone_name or imp["zone"] == "all"
        ]
    if not relevant:
        return '<div class="ideas-section"><div class="ideas-intro"><h3>💰 Mejoras</h3><p>(Sin sugerencias todavía para esta zona.)</p></div></div>'

    blocks = []
    for tier in TIER_ORDER:
        tier_items = [imp for imp in relevant if imp["tier"] == tier]
        if not tier_items:
            continue
        # ordenar por costo ascendente dentro del tier
        tier_items.sort(key=lambda x: x.get("cost_usd", 0))
        emoji, label, color, _ = TIER_META[tier]
        card_htmls = [render_improvement_card(imp) for imp in tier_items]
        grid = render_collapsible_grid(card_htmls, "improvements-grid", label="todas las mejoras")
        blocks.append(f"""
<div class="improvements-tier" style="--tier-color:{color}">
  <h4 class="improvements-tier-header">{emoji} {esc(label)} <span class="improvements-tier-count">· {len(tier_items)}</span></h4>
  {grid}
</div>""")

    title = "💰 Mejoras para el jardín" if zone_name == "todo" else "💰 Mejoras para esta zona"
    intro = f"""
<div class="ideas-intro">
  <h3>{title}</h3>
  <p>Inversiones (o trabajo gratis) para subir un escalón el jardín — agrupado por presupuesto. Empezá por lo gratis y subí si tiene sentido.</p>
</div>"""
    return f'<div class="ideas-section">{intro}{"".join(blocks)}</div>'


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
    card_htmls = [f"""
<article class="hloc-card">
  <h4 class="hloc-title">{esc(idea["title"])}</h4>
  <p class="hloc-desc">{esc(idea["desc"])}</p>
  <div class="hloc-pros"><strong>✅ Pros:</strong> {esc(idea["pros"])}</div>
  <div class="hloc-cons"><strong>⚠️ Contras:</strong> {esc(idea["cons"])}</div>
  <div class="hloc-best"><strong>👍 Mejor para:</strong> {esc(idea["best_for"])}</div>
</article>""" for idea in HUERTA_LOCATION_IDEAS]
    if len(card_htmls) <= 2:
        return f'<div class="hloc-grid">{"".join(card_htmls)}</div>'
    visible = "".join(card_htmls[:2])
    hidden = "".join(card_htmls[2:])
    n_more = len(card_htmls) - 2
    return f"""<div class="hloc-grid">{visible}</div>
<div class="hloc-grid ideas-collapsed" hidden data-collapsed-grid>{hidden}</div>
<button type="button" class="btn-show-all" data-show-all aria-expanded="false">▾ Ver todas las opciones — {n_more} más</button>"""


def render_collapsible_grid(card_htmls, grid_class, visible_count=2, label="ver más"):
    """Renderiza una grid donde los primeros `visible_count` cards quedan
    visibles y el resto colapsado bajo un botón 'Ver todas (N más)' que
    se expande con click. Si hay <= visible_count cards, no genera botón."""
    if len(card_htmls) <= visible_count:
        return f'<div class="cards-grid {grid_class}">{"".join(card_htmls)}</div>'

    visible = "".join(card_htmls[:visible_count])
    hidden = "".join(card_htmls[visible_count:])
    n_more = len(card_htmls) - visible_count
    plural = "" if n_more == 1 else "s"
    return f"""<div class="cards-grid {grid_class}">{visible}</div>
<div class="cards-grid {grid_class} ideas-collapsed" hidden data-collapsed-grid>{hidden}</div>
<button type="button" class="btn-show-all" data-show-all aria-expanded="false">▾ Ver {label} — {n_more} más</button>"""


# ============================================================
# Build de cada zona (Todo / Frente / Fondo)
# ============================================================
def build_zone(zone_name, zone_label, plants_in_view, img_data):
    """plants_in_view: lista de plantas a mostrar (frente, fondo o interior).
    Subtabs: Info + Calendario. Curiosidades vive en Ideas → Experiencias y
    Mejoras en Ideas → Mejoras (páginas separadas)."""
    info_cards = "\n".join(render_plant_info_card(p, img_data) for p in plants_in_view)
    cal_grid = render_calendar_grid(plants_in_view)

    return f"""
<section class="zone-content" data-zone="{zone_name}">
  <nav class="subtab-nav">
    <button class="subtab-btn active" data-sub="info">🪴 Info</button>
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
    <div class="timeline-actions">
      <button class="btn-create-task" id="btn-create-task">＋ Nueva tarea</button>
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
      <label class="settings-label" style="margin-top: 8px;">
        <strong>Contexto opcional</strong>
        <span class="settings-hint">Lo que querés que sepa la IA al evaluar esta foto. Ej: "ambas plantas comparten la base", "la foto se sacó al atardecer", etc.</span>
      </label>
      <textarea id="task-photo-context" class="settings-input" rows="3" maxlength="500" placeholder="Notas sobre lo que se ve en la foto, ángulo, condiciones..."></textarea>
      <div class="task-photo-actions" style="margin-top: 10px;">
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

<!-- Modal: Responder con texto (sin foto) -->
<div class="modal" id="task-text-modal">
  <div class="modal-content modal-wide">
    <button class="modal-close" data-close="task-text">✕</button>
    <h3>💬 Responder con texto</h3>
    <p class="task-photo-name" id="task-text-name"></p>

    <div class="task-photo-stage" data-stage="setup" hidden>
      <div class="task-photo-warning">
        ⚠️ Necesitás configurar tu GitHub Personal Access Token antes de subir notas al repo.
      </div>
      <button class="btn-primary" id="btn-text-go-settings">⚙️ Ir a Configuración</button>
    </div>

    <div class="task-photo-stage" data-stage="write">
      <label class="settings-label">
        <strong>Tu respuesta o nota</strong>
        <span class="settings-hint">Describí qué hiciste, qué viste, una pregunta, etc. La IA puede leer este texto cuando corras /actualizar-tareas.</span>
      </label>
      <textarea id="task-text-content" class="settings-input" rows="6" maxlength="1500" placeholder="Ej: 'Ya regué el plantín'. O 'Sigue sin germinar después de 3 semanas, qué hago?'"></textarea>
      <div class="task-photo-actions" style="margin-top: 12px;">
        <button class="btn-secondary" id="btn-text-mark-done">✅ Marcar hecha con esta nota</button>
        <button class="btn-primary" id="btn-text-ask-ai">🤖 Subir nota + pedir evaluación IA</button>
      </div>
    </div>

    <div class="task-photo-stage" data-stage="result" hidden>
      <div class="task-photo-result" id="task-text-result"></div>
    </div>
  </div>
</div>

<!-- Modal: Compose (crear tarea propia / hacer pregunta) -->
<div class="modal" id="task-compose-modal">
  <div class="modal-content modal-wide">
    <button class="modal-close" data-close="task-compose">✕</button>
    <h3 id="task-compose-title">＋ Nueva tarea</h3>
    <p class="task-photo-name" id="task-compose-context"></p>

    <!-- Stage: setup falta PAT -->
    <div class="task-photo-stage" data-stage="setup" hidden>
      <div class="task-photo-warning">
        ⚠️ Necesitás configurar tu GitHub Personal Access Token antes de crear tareas o preguntas.
      </div>
      <button class="btn-primary" id="btn-compose-go-settings">⚙️ Ir a Configuración</button>
    </div>

    <!-- Stage: write -->
    <div class="task-photo-stage" data-stage="write">
      <div class="compose-plant-row" id="compose-plant-row" hidden>
        <label class="settings-label">
          <strong>Planta (opcional)</strong>
          <span class="settings-hint">Atá esta tarea a una planta específica para mejor contexto.</span>
        </label>
        <select id="compose-plant-select" class="settings-input">
          <option value="">— Sin planta específica —</option>
        </select>
      </div>

      <label class="settings-label" id="compose-title-label">
        <strong>Título corto</strong>
        <span class="settings-hint">Resumí en 1 línea (max 80 caracteres).</span>
      </label>
      <input type="text" id="compose-title" class="settings-input" maxlength="80" placeholder="Ej: Trasplantar el helecho del fondo">

      <label class="settings-label" style="margin-top: 10px;">
        <strong id="compose-text-label">Detalles / contexto</strong>
        <span class="settings-hint" id="compose-text-hint">Lo que querés que sepa la IA al procesar esto.</span>
      </label>
      <textarea id="compose-text" class="settings-input" rows="4" maxlength="1000" placeholder="Notas, contexto, ángulo, etc."></textarea>

      <div class="compose-photo-section">
        <label class="settings-label">
          <strong>Foto (opcional)</strong>
          <span class="settings-hint">Sumá una foto si ayuda a explicar.</span>
        </label>
        <div class="task-photo-buttons" id="compose-photo-pick">
          <label class="task-photo-btn">
            <input type="file" accept="image/*" capture="environment" id="compose-camera-input" class="visually-hidden">
            <span class="task-photo-btn-emoji">📸</span>
            <span class="task-photo-btn-label">Sacá una foto</span>
          </label>
          <label class="task-photo-btn">
            <input type="file" accept="image/*" id="compose-gallery-input" class="visually-hidden">
            <span class="task-photo-btn-emoji">🖼️</span>
            <span class="task-photo-btn-label">Subí una existente</span>
          </label>
        </div>
        <div class="task-photo-preview-wrap" id="compose-photo-preview-wrap" hidden>
          <canvas id="compose-photo-canvas"></canvas>
          <button class="btn-secondary" id="btn-compose-photo-remove" style="margin-top: 8px;">↺ Quitar foto</button>
        </div>
      </div>

      <div class="task-photo-actions" style="margin-top: 12px;">
        <button class="btn-secondary" data-close="task-compose">Cancelar</button>
        <button class="btn-primary" id="btn-compose-submit">📤 Crear</button>
      </div>
    </div>

    <!-- Stage: result -->
    <div class="task-photo-stage" data-stage="result" hidden>
      <div class="task-photo-result" id="task-compose-result"></div>
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

    <div class="settings-section">
      <label class="settings-label">
        <strong>📲 Estado de la app instalable (PWA)</strong>
        <span class="settings-hint">Diagnóstico de por qué Chrome puede o no ofrecer "Install app".</span>
      </label>
      <div id="pwa-status-panel" class="pwa-status-panel">Verificando…</div>
      <div class="settings-actions">
        <button class="btn-secondary" id="btn-trigger-install" disabled>Instalar app</button>
        <button class="btn-secondary" id="btn-reset-sw">🔄 Resetear SW</button>
      </div>
    </div>

    <div class="settings-section">
      <label class="settings-label">
        <strong>🔔 Notificaciones push</strong>
        <span class="settings-hint">Recordatorios diarios del jardín en este dispositivo. Requiere el GitHub PAT configurado. La suscripción se guarda en el repo (público): técnicamente cualquiera con el repo podría mandarte notificaciones — mismo modelo de privacidad que el sync.</span>
      </label>
      <div id="push-status-panel" class="pwa-status-panel">Verificando…</div>
      <div class="settings-actions">
        <button class="btn-secondary" id="btn-enable-push">🔔 Activar notificaciones</button>
        <button class="btn-secondary btn-danger" id="btn-disable-push" hidden>🔕 Desactivar</button>
      </div>
      <div class="settings-feedback" id="settings-push-feedback"></div>
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

    redirect_target = f"../tareas.html#task={task_id}"

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
# Helpers de página — shell HTML + nav cross-page
# ============================================================
HEAD_META = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#2d5016">

<!-- Favicons -->
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="icon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">

<!-- Apple touch icons -->
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="apple-touch-icon" sizes="120x120" href="apple-touch-icon-120.png">
<link rel="apple-touch-icon" sizes="152x152" href="apple-touch-icon-152.png">
<link rel="apple-touch-icon" sizes="167x167" href="apple-touch-icon-167.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon-180.png">

<!-- iOS standalone web app meta -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Jardineando">

<!-- Android standalone web app meta -->
<meta name="mobile-web-app-capable" content="yes">
<meta name="application-name" content="Jardineando">

<!-- Safari pinned tab -->
<link rel="mask-icon" href="mask-icon.svg" color="#2d5016">

<!-- PWA -->
<link rel="manifest" href="manifest.webmanifest">

<!-- Open Graph / WhatsApp / Twitter (defaults; las páginas pueden overridear) -->
<meta property="og:type" content="website">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">"""


def _render_top_nav(active_page: str, ticker_html_inner: str = "", ticker_aria: str = "") -> str:
    """Renderiza el header + weather line + ticker + nav cross-page.
    active_page ∈ {"home","tareas","ideas"}.
    - "home": la Biblioteca de especies ES la home — strip cross-page + las
      tabs de zona (Frente/Fondo/Interior; cada planta se ve según ubicación).
    - "tareas"/"ideas": strip cross-page simple. Tareas no se linkea desde
      ninguna otra página (se llega por notificación push); sólo aparece como
      indicador activo estando en tareas.html.
    """
    header = """<header class="main-header">
    <h1 class="brand"><img class="brand-logo" src="icon-96.png" alt="" width="40" height="40"> Jardineando</h1>
    <h2 class="subbrand">Pacha Mama</h2>
  </header>"""

    weather = """<div class="weather-line" id="weather-line">
    <span class="weather-cell"><span class="weather-emoji">🌱</span><span class="weather-val">…</span></span>
    <span class="weather-cell"><span class="weather-emoji">💨</span><span class="weather-val">…</span></span>
    <span class="weather-cell"><span class="weather-emoji">💧</span><span class="weather-val">…</span></span>
    <span class="weather-cell"><span class="weather-emoji">📍</span><span class="weather-val">Montevideo</span></span>
  </div>"""

    ticker = f"""<div class="stats-ticker" aria-label="{esc(ticker_aria)}">
    <div class="ticker-track">{ticker_html_inner}{ticker_html_inner}</div>
  </div>""" if ticker_html_inner else ""

    home_active = " active" if active_page == "home" else ""
    ideas_active = " active" if active_page == "ideas" else ""
    tareas_link = (
        '\n    <a class="todo-btn active" href="tareas.html"><span aria-hidden="true">📋</span> Tareas '
        '<span class="todo-label" id="todo-count">…</span></a>'
        if active_page == "tareas" else ""
    )
    zone_tabs = """
  <nav class="main-tabs">
    <button class="tab-btn active" data-zone="frente"><span class="tab-emoji">🌳</span><span class="tab-label">Frente</span></button>
    <button class="tab-btn" data-zone="fondo"><span class="tab-emoji">🏊</span><span class="tab-label">Fondo</span></button>
    <button class="tab-btn" data-zone="interior"><span class="tab-emoji">🪴</span><span class="tab-label">Interior</span></button>
  </nav>""" if active_page == "home" else ""
    nav_block = f"""<div class="todo-strip cross-page-strip">
    <a class="todo-btn{home_active}" href="index.html"><span aria-hidden="true">🏡</span> Home</a>
    <a class="todo-btn{ideas_active}" href="ideas.html"><span aria-hidden="true">💡</span> Ideas</a>{tareas_link}
  </div>{zone_tabs}"""

    return f"""<div class="container container-top">
  {header}

  {weather}

  {ticker}

  {nav_block}
</div>"""


def _page_shell(*, title: str, description: str, og_image: str = "og-image.png",
                body_class: str, body_html: str, page_globals_js: str) -> str:
    """Envuelve body_html en un documento HTML completo con HEAD_META + CSS +
    JS inline. og_image puede sobrescribirse por página."""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
{HEAD_META}
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{esc(og_image)}">
<meta name="twitter:image" content="{esc(og_image)}">

<style>{CSS}</style>
</head>
<body class="{body_class}">
{body_html}
<script>
{page_globals_js}
{JS}
</script>
</body>
</html>"""


def build_ideas_html(img_data, timeline_modals: str = "",
                     ticker_html_inner: str = "", ticker_aria: str = "",
                     tasks_js: str = "", plants_info_js: str = "",
                     contacts_js: str = "", templates_js: str = "",
                     ticker_js: str = "", site_url_js: str = "") -> str:
    """Página standalone con todas las ideas y la huerta. Subtabs internos
    (en 2 filas): Ornamentales / Huerta / Espacios verdes / Experiencias /
    Mejoras. Las Curiosidades del catálogo viven dentro de Experiencias, y
    como sus cards abren el modal de especie, la página necesita los modales
    (timeline_modals) + los globals reales (TASKS/PLANTS_INFO/etc.)."""
    top_nav = _render_top_nav("ideas", ticker_html_inner, ticker_aria)

    # Combinar ornamentales de las dos zonas (frente + fondo)
    all_ideas = NEW_IDEAS_FRENTE + NEW_IDEAS_FONDO
    ideas_sorted = sorted(all_ideas, key=lambda i: not idea_is_optimal_now(i))
    huerta_sorted = sorted(HUERTA, key=lambda h: not huerta_is_optimal_now(h))

    ornament_grid = render_collapsible_grid(
        [render_idea_card(i) for i in ideas_sorted],
        "ideas-grid", label="todas las plantas",
    )
    huerta_grid = render_collapsible_grid(
        [render_huerta_card(h) for h in huerta_sorted],
        "huerta-grid", label="todas las hortalizas",
    )
    locations_html = render_huerta_locations()

    # Experiencias APROBADAS — viven en docs/engage/ como páginas permanentes.
    # Regla del usuario: cada experiencia que se aprueba se suma acá (no en la
    # nav del inicio). El agente de /engagement agrega una entrada al promover.
    approved_experiences = [
        {"icon": "📱", "title": "El Feed de tu Jardín",
         "desc": "Cada planta tiene su cuenta y postea en primera persona un dato real que no sabías.",
         "page": "engage/2026-06-29-feed-jardin.html"},
        {"icon": "🍵", "title": "El Chusmerío del Cantero",
         "desc": "El tabloide del jardín: el escándalo, el robo de crédito y el secreto que esconde cada planta.",
         "page": "engage/2026-06-30-chusmerio-jardin.html"},
        {"icon": "🧪", "title": "Los Superpoderes de tu Jardín",
         "desc": "El poder secreto de cada planta: la que limpia el aire, la que es especia, la que repele mosquitos.",
         "page": "engage/2026-06-30-superpoderes-jardin.html"},
        {"icon": "🏆", "title": "Récords de tu Jardín",
         "desc": "Los superlativos de tus plantas: la más longeva, la que limpia el aire, la de Venus…",
         "page": "engage/2026-06-29-records-jardin.html"},
        {"icon": "📰", "title": "El Diario de tu Jardín",
         "desc": "Las noticias de hoy entre tus plantas, en titulares de prensa.",
         "page": "engage/2026-06-29-diario-jardin.html"},
        {"icon": "🌀", "title": "La rueda del año",
         "desc": "El pulso anual de floración y fructificación de tus 52 plantas, animado.",
         "page": "engage/2026-06-13-rueda-ano.html"},
    ]
    experiences_html = '<div class="exp-grid">' + "".join(
        f"""<a class="exp-card" href="{esc(e['page'])}">
        <span class="exp-icon" aria-hidden="true">{e['icon']}</span>
        <span class="exp-text"><span class="exp-title">{esc(e['title'])}</span>
        <span class="exp-desc">{esc(e['desc'])}</span></span>
        <span class="exp-go" aria-hidden="true">→</span>
      </a>""" for e in approved_experiences
    ) + "</div>"

    # Highlights del subtab Ornamentales: ornamentales con ventana óptima ahora.
    # (Las hortalizas óptimas aparecen primero en el pane Huerta vía huerta_sorted.)
    optimal_ideas = [i for i in all_ideas if idea_is_optimal_now(i)]
    highlights_html = ""
    if optimal_ideas:
        highlights_grid = render_collapsible_grid(
            [render_idea_card(i) for i in optimal_ideas],
            "ideas-grid", label="todas las ornamentales óptimas",
        )
        highlights_html = f"""
<div class="ideas-section ideas-section-now">
  <div class="ideas-intro">
    <h3>🎯 Para plantar ESTE MES ({esc(CURRENT_MONTH_NAME)})</h3>
    <p>Lo que tiene ventana óptima ahora. {len(optimal_ideas)} planta{'s' if len(optimal_ideas) != 1 else ''} ornamental{'es' if len(optimal_ideas) != 1 else ''}.</p>
  </div>
  {highlights_grid}
</div>"""

    # Curiosidades — feed de fun facts de todas las especies del catálogo.
    # Vive dentro del subtab Experiencias (es una experiencia más).
    curiosidades_html = render_curiosidades_section(PLANTS, img_data)
    improvements_html = render_improvements_section("todo")

    body = f"""{top_nav}

<div class="container container-zones">
  <section class="zone-content active" data-zone="ideas">
    <nav class="subtab-nav subtab-nav-2rows">
      <button class="subtab-btn active" data-sub="ornament">🌸 Ornamentales</button>
      <button class="subtab-btn" data-sub="huerta">🥬 Huerta</button>
      <button class="subtab-btn" data-sub="espacios">🏡 Espacios</button>
      <button class="subtab-btn" data-sub="experiencias">✨ Experiencias</button>
      <button class="subtab-btn" data-sub="improvements">💰 Mejoras</button>
    </nav>

    <div class="subtab-pane active" data-sub="ornament">
      {highlights_html}
      <div class="filter-bar"><input type="text" class="search" placeholder="🔍 Buscar planta..."></div>
      <div class="ideas-section">
        <div class="ideas-intro">
          <h3>🌳 Plantas para plantar</h3>
          <p>Especies ornamentales sugeridas para sumar — nativas, polinizadoras, frutales. Las óptimas para plantar este mes aparecen primero.</p>
        </div>
        {ornament_grid}
      </div>
    </div>

    <div class="subtab-pane" data-sub="huerta">
      <div class="filter-bar"><input type="text" class="search" placeholder="🔍 Buscar hortaliza..."></div>
      <div class="ideas-section">
        <div class="ideas-intro">
          <h3>🥬 Frutas y verduras de huerta</h3>
          <p>Catálogo de cultivos para Montevideo, calendario marcado en meses. Las que se siembran/trasplantan este mes aparecen primero.</p>
        </div>
        {huerta_grid}
      </div>
    </div>

    <div class="subtab-pane" data-sub="espacios">
      <div class="ideas-section">
        <div class="ideas-intro">
          <h3>🏡 Qué hacer con tus espacios verdes</h3>
          <p>Opciones estructurales para sumar canteros, camas elevadas, macetones o aromáticas integradas. Ordenadas de mejor a más simple.</p>
        </div>
        {locations_html}
      </div>
    </div>

    <div class="subtab-pane" data-sub="experiencias">
      <div class="ideas-section">
        <div class="ideas-intro">
          <h3>✨ Experiencias de tu jardín</h3>
          <p>Las experiencias que aprobaste quedan acá, siempre a mano. Cada vez que aprobás una nueva, se suma a esta lista.</p>
        </div>
        {experiences_html}
      </div>
      <div class="ideas-section" id="curiosidades-section">
        <div class="filter-bar"><input type="text" class="search" placeholder="🔍 Buscar curiosidad..."></div>
        {curiosidades_html}
      </div>
    </div>

    <div class="subtab-pane" data-sub="improvements">
      <div class="filter-bar"><input type="text" class="search" placeholder="🔍 Buscar mejora..."></div>
      {improvements_html}
    </div>
  </section>
</div>

<div class="lightbox" id="lightbox">
  <img id="lightbox-img" alt="">
</div>

{timeline_modals}"""

    page_globals = "\n".join([
        tasks_js or "const TASKS = [];",
        plants_info_js or "const PLANTS_INFO = [];",
        contacts_js or "const DEFAULT_CONTACTS = [];",
        templates_js or "const WHATSAPP_TEMPLATES = {};",
        ticker_js or "const STATS_TICKER = [];",
        site_url_js or 'const SITE_URL = "";',
    ])

    return _page_shell(
        title="Ideas · Jardineando",
        description="Ideas de plantas nuevas, huerta y espacios verdes para el jardín Pacha Mama (Montevideo).",
        og_image="og-image.png",
        body_class="zone-ideas",
        body_html=body,
        page_globals_js=page_globals,
    )


def build_tareas_html(tasks, img_data, ticker_html_inner: str = "", ticker_aria: str = "",
                      tasks_js: str = "", plants_info_js: str = "",
                      contacts_js: str = "", templates_js: str = "",
                      ticker_js: str = "", site_url_js: str = "") -> str:
    """Página standalone con el Timeline + todos los modales asociados.
    Recibe los JS-globals ya serializados desde main() para no duplicar
    la lógica de serialización."""
    top_nav = _render_top_nav("tareas", ticker_html_inner, ticker_aria)

    timeline_html = build_timeline_view(tasks, img_data)
    # El section sale con class="zone-content"; en esta página standalone
    # tiene que estar activa por defecto.
    timeline_active = timeline_html.replace(
        '<section class="zone-content" data-zone="timeline">',
        '<section class="zone-content active" data-zone="timeline">',
        1,
    )

    body = f"""{top_nav}

<div class="container container-zones">
  {timeline_active}
</div>

<div class="lightbox" id="lightbox">
  <img id="lightbox-img" alt="">
</div>"""

    page_globals = "\n".join([
        tasks_js or "const TASKS = [];",
        plants_info_js or "const PLANTS_INFO = [];",
        contacts_js or "const DEFAULT_CONTACTS = [];",
        templates_js or "const WHATSAPP_TEMPLATES = {};",
        ticker_js or "const STATS_TICKER = [];",
        site_url_js or 'const SITE_URL = "";',
    ])

    return _page_shell(
        title="Tareas · Jardineando",
        description="Timeline de tareas del jardín Pacha Mama: poda, riego, fertilización, control de plagas.",
        og_image="og-image.png",
        body_class="zone-tareas",
        body_html=body,
        page_globals_js=page_globals,
    )


def build_biblioteca_redirect() -> str:
    """Stub de redirect: la Biblioteca ES la home (index.html). Este archivo
    existe sólo para que no se rompan links viejos a biblioteca.html (JS
    cacheado, notificaciones ya enviadas). Preserva el hash."""
    return """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Biblioteca · Jardineando</title>
<meta http-equiv="refresh" content="0; url=index.html">
<link rel="canonical" href="index.html">
</head>
<body>
<p>La Biblioteca ahora es la página principal. <a href="index.html">Ir a la Biblioteca</a></p>
<script>window.location.replace('index.html' + window.location.hash);</script>
</body>
</html>"""


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
    docs_images_dir = ROOT / "docs" / "images"
    img_data = {}
    for fname in sorted(unique_files):
        path = IMAGES_DIR / fname
        if path.exists():
            copy_curated_image(path, docs_images_dir / fname)
            img_data[fname] = fname  # truthy marker para checks de existencia
        else:
            img_data[fname] = ""
            print(f"  ⚠ Faltante: {fname}")
    print(f"   ✅ {sum(1 for v in img_data.values() if v)} copiadas a docs/images/")

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

    # 4. Build zonas — cada planta se ve según su ubicación (sin vista "Todo")
    frente_plants = [p for p in PLANTS if p["zone"] == "frente"]
    fondo_plants = [p for p in PLANTS if p["zone"] == "fondo"]
    interior_plants = [p for p in PLANTS if p["zone"] == "interior"]

    frente_html = build_zone("frente", "Frente", frente_plants, img_data=img_data)
    fondo_html = build_zone("fondo", "Fondo", fondo_plants, img_data=img_data)
    interior_html = build_zone("interior", "Interior", interior_plants, img_data=img_data)

    # 5. Inyectar datos como JSON para el JS
    # Las imágenes viven en docs/images/ y se referencian por path via imgUrl()
    # en scripts.py; no se inyecta dict global.
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
            "chips_html": render_card_chips(p),
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

    # 6. HTML final — la home ES la Biblioteca de especies: tabs de zona
    # (Frente/Fondo/Interior) + subtabs Info/Calendario. Las tareas se
    # comunican por push (tareas.html se llega por deep link). Necesita los
    # modales que vienen como cola de build_timeline_view (species-detail,
    # species-photo, settings, etc.) para el modal de planta. Extraemos sólo eso.
    full_timeline_html = build_timeline_view(tasks, img_data)
    timeline_modals = full_timeline_html.split('</section>', 1)[1]
    top_nav = _render_top_nav("home", ticker_html_inner, ticker_aria)
    home_body = f"""{top_nav}

<div class="container container-zones">
  {frente_html.replace('class="zone-content"', 'class="zone-content active"', 1)}
  {fondo_html}
  {interior_html}
</div>

<div class="lightbox" id="lightbox">
  <img id="lightbox-img" alt="">
</div>

{timeline_modals}"""

    page_globals = "\n".join([tasks_js, plants_info_js, contacts_js, templates_js, ticker_js, site_url_js])

    html_doc = _page_shell(
        title="Jardineando · Pacha Mama",
        description=f"Biblioteca de especies del jardín Pacha Mama (Montevideo): {total_plants} plantas por ubicación, fichas y calendario anual.",
        og_image="og-image.png",
        body_class="zone-frente",
        body_html=home_body,
        page_globals_js=page_globals,
    )

    OUTPUT.write_text(html_doc, encoding="utf-8")
    size_mb = OUTPUT.stat().st_size / 1024 / 1024
    print(f"\n✅ Generado: {OUTPUT}")
    print(f"   {size_mb:.1f} MB · {total_plants} plantas · {len(tasks)} tareas")

    # 6.5 biblioteca.html — redirect stub a index.html (links viejos)
    biblioteca_out = ROOT / "docs" / "biblioteca.html"
    biblioteca_out.write_text(build_biblioteca_redirect(), encoding="utf-8")
    print(f"✅ Generado: {biblioteca_out} (redirect a index.html)")

    # 7. Generar docs/ideas.html
    ideas_html_doc = build_ideas_html(
        img_data,
        timeline_modals=timeline_modals,
        ticker_html_inner=ticker_html_inner,
        ticker_aria=ticker_aria,
        tasks_js=tasks_js,
        plants_info_js=plants_info_js,
        contacts_js=contacts_js,
        templates_js=templates_js,
        ticker_js=ticker_js,
        site_url_js=site_url_js,
    )
    ideas_out = ROOT / "docs" / "ideas.html"
    ideas_out.write_text(ideas_html_doc, encoding="utf-8")
    ideas_size_kb = ideas_out.stat().st_size / 1024
    print(f"✅ Generado: {ideas_out}")
    print(f"   {ideas_size_kb:.0f} KB")

    # 8. Generar docs/tareas.html
    tareas_html_doc = build_tareas_html(
        tasks, img_data,
        ticker_html_inner=ticker_html_inner,
        ticker_aria=ticker_aria,
        tasks_js=tasks_js,
        plants_info_js=plants_info_js,
        contacts_js=contacts_js,
        templates_js=templates_js,
        ticker_js=ticker_js,
        site_url_js=site_url_js,
    )
    tareas_out = ROOT / "docs" / "tareas.html"
    tareas_out.write_text(tareas_html_doc, encoding="utf-8")
    tareas_size_kb = tareas_out.stat().st_size / 1024
    print(f"✅ Generado: {tareas_out}")
    print(f"   {tareas_size_kb:.0f} KB")

    # Resumen final
    images_bytes = sum(
        p.stat().st_size for p in docs_images_dir.rglob("*")
        if p.is_file() and "uploads" not in p.parts
    )
    print(f"\n📦 Resumen:")
    print(f"   docs/index.html      → {OUTPUT.stat().st_size/1024:>6.0f} KB")
    print(f"   docs/biblioteca.html → {biblioteca_out.stat().st_size/1024:>6.0f} KB")
    print(f"   docs/tareas.html     → {tareas_out.stat().st_size/1024:>6.0f} KB")
    print(f"   docs/ideas.html      → {ideas_out.stat().st_size/1024:>6.0f} KB")
    print(f"   docs/images/      → {images_bytes/1024/1024:>6.1f} MB (cacheado por browser)")
    print(f"\n👉 Para subir a GitHub Pages:")
    print(f"   git add docs/index.html && git commit -m 'rebuild' && git push")


if __name__ == "__main__":
    main()
