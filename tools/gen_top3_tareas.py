#!/usr/bin/env python3
"""Top 3 de tareas prioritarias — experiencia recurrente cada 2 días.

Pedido directo del usuario (04/07/2026): "una experiencia que mire todas las
especies y me liste las 3 tareas prioritarias a realizar; quiero recibir esto
cada 2 días".

Qué hace:
  1. Mira TODAS las tareas de todas las especies (generate_tasks_from_plants)
     respetando el estado del usuario (docs/sync/task_states.json: done no
     cuenta, snoozed solo si venció el snooze).
  2. Rankea por (prioridad alta>media>baja, vencida > vence este mes > futuro,
     fecha, id) y se queda con las 3 primeras.
  3. Regenera docs/engage/top3-tareas.html (URL estable, contenido fresco).
  4. Con --merge, encola la notificación push del día en queue.json.

Cadencia: corre TODOS los días desde /engagement, pero solo genera en días
"pares" respecto del ancla 2026-07-04 (es decir, cada 2 días). --force ignora
la cadencia (para pruebas o para el primer envío manual).

Uso:
  python tools/gen_top3_tareas.py [YYYY-MM-DD]                    # imprime la entry del día (si toca)
  python tools/gen_top3_tareas.py [YYYY-MM-DD] --merge            # además regenera la página y mergea en queue.json
  python tools/gen_top3_tareas.py [YYYY-MM-DD] --merge --force    # ídem aunque no toque por cadencia
  python tools/gen_top3_tareas.py [YYYY-MM-DD] --merge --send-at 11:15   # hora de envío custom (default 09:00)
"""
import datetime
import html
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from data_plants import PLANTS          # noqa: E402
from build import generate_tasks_from_plants  # noqa: E402

SITE = "https://gardening-chi.vercel.app/"
QUEUE_PATH = os.path.join(ROOT, "docs", "notifications", "queue.json")
STATES_PATH = os.path.join(ROOT, "docs", "sync", "task_states.json")
PAGE_PATH = os.path.join(ROOT, "docs", "engage", "top3-tareas.html")

ANCHOR = datetime.date(2026, 7, 4)   # primer envío; después cada 2 días
DEFAULT_SEND = "09:00"

PRIO_EMOJI = {"alta": "🔴", "media": "🟡", "baja": "🟢"}
PRIO_RANK = {"alta": 0, "media": 1, "baja": 2}
ZONE_LABEL = {"frente": "Frente", "fondo": "Fondo", "interior": "Interior"}
MONTHS_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def load_task_states():
    try:
        with open(STATES_PATH, encoding="utf-8") as f:
            return json.load(f).get("tasks") or {}
    except (OSError, ValueError):
        return {}


def task_status(task_id, states, today):
    s = states.get(task_id) or {}
    status = s.get("status", "active")
    if status == "snoozed":
        su = s.get("snoozed_until") or ""
        try:
            if datetime.date.fromisoformat(su[:10]) <= today:
                return "active"
        except ValueError:
            return "active"
    return status


def active_tasks(today):
    states = load_task_states()
    return [
        t for t in generate_tasks_from_plants(PLANTS)
        if task_status(t["id"], states, today) == "active"
    ]


def is_overdue(t, today):
    y, m = t.get("due_year"), t.get("due_month")
    return bool(y and m and (y, m) < (today.year, today.month))


def is_due_this_month(t, today):
    y, m = t.get("due_year"), t.get("due_month")
    return bool(y and m and (y, m) == (today.year, today.month))


def urgency_bucket(t, today):
    if is_overdue(t, today):
        return 0
    if is_due_this_month(t, today):
        return 1
    return 2


def top3(today):
    """Las 3 prioritarias: primero por prioridad declarada (alta>media>baja),
    dentro de cada prioridad las vencidas / del mes primero, después por fecha."""
    return sorted(active_tasks(today), key=lambda t: (
        PRIO_RANK.get(t["priority"], 3),
        urgency_bucket(t, today),
        t.get("due_year") or 9999,
        t.get("due_month") or 13,
        t["id"],
    ))[:3]


def is_due_day(today):
    return (today - ANCHOR).days % 2 == 0 and today >= ANCHOR


# ---------------------------------------------------------------- página HTML

def why_line(t, today):
    if is_overdue(t, today):
        return "⚠️ Atrasada — era para " + (t.get("due_label") or "antes")
    if is_due_this_month(t, today):
        return "📅 Vence este mes — " + (t.get("due_label") or "")
    return "🗓️ " + (t.get("due_label") or "Sin fecha fija")


def render_page(today, tasks, total_active):
    date_h = f"{today.day} de {MONTHS_ES[today.month - 1]} {today.year}"
    cards = []
    medals = ["①", "②", "③"]
    for i, t in enumerate(tasks):
        codes = ", ".join(t.get("plant_codes") or [])
        zone = ZONE_LABEL.get(t.get("plant_zone") or "", t.get("plant_zone") or "")
        cards.append(f"""
    <a class="card p-{html.escape(t['priority'])}" href="{SITE}tareas.html#task={html.escape(t['id'])}">
      <div class="rank">{medals[i]}</div>
      <div class="body">
        <div class="meta"><span class="prio">{PRIO_EMOJI.get(t['priority'], '🌿')} {html.escape(t['priority'].upper())}</span>
          <span class="plant">{html.escape(t['plant_common'])} ({html.escape(codes)}) · {html.escape(zone)}</span></div>
        <h2>{html.escape(t['title'])}</h2>
        <div class="why">{html.escape(why_line(t, today))}</div>
        <div class="cta">Abrir la tarea →</div>
      </div>
    </a>""")

    return f"""<!DOCTYPE html><html lang="es-UY"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#f5faf0">
<title>🎯 Las 3 del jardín — {date_h}</title>
<style>
  :root{{ --verde:#2d5016; --verde2:#4a7c2a; --bg:#f5faf0; --card:#ffffff;
    --ink:#22301a; --ink2:#5a6b3c; --ink3:#8a9877; --line:#dde8d2;
    --alta:#c0392b; --media:#b9770e; --baja:#2d7a3a;
    --pad:max(16px,env(safe-area-inset-left));
    --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,system-ui,sans-serif; }}
  *{{ box-sizing:border-box; margin:0; -webkit-tap-highlight-color:transparent; }}
  body{{ font-family:var(--sans); background:var(--bg); color:var(--ink); line-height:1.5;
    background-image:radial-gradient(80% 30% at 50% -4%, rgba(74,124,42,.10), transparent 70%); }}
  .back{{ display:block; color:var(--verde); text-decoration:none; font-size:13px; font-weight:700;
    padding:11px var(--pad); background:#ecf4e3; }}
  .wrap{{ max-width:560px; margin:0 auto; padding:0 var(--pad) 40px; }}
  header{{ text-align:center; padding:30px 0 8px; }}
  header .kicker{{ display:inline-block; font-size:11px; font-weight:800; letter-spacing:.14em;
    text-transform:uppercase; color:var(--verde2); background:#e6f0da; border-radius:999px;
    padding:5px 13px; margin-bottom:12px; }}
  header h1{{ font-size:30px; line-height:1.12; letter-spacing:-.02em; color:var(--verde); }}
  header .date{{ color:var(--ink3); font-size:13.5px; margin-top:6px; }}
  header p.lede{{ color:var(--ink2); font-size:15px; margin-top:10px; }}
  header p.lede b{{ color:var(--ink); }}
  .card{{ display:flex; gap:13px; background:var(--card); border:1px solid var(--line);
    border-radius:16px; padding:16px 15px; margin-top:14px; text-decoration:none; color:inherit;
    box-shadow:0 3px 14px rgba(45,80,22,.07); border-left:5px solid var(--line); }}
  .card:active{{ transform:scale(.985); }}
  .card.p-alta{{ border-left-color:var(--alta); }}
  .card.p-media{{ border-left-color:var(--media); }}
  .card.p-baja{{ border-left-color:var(--baja); }}
  .rank{{ font-size:30px; line-height:1; color:var(--verde2); font-weight:700; padding-top:2px; }}
  .body{{ flex:1; min-width:0; }}
  .meta{{ display:flex; flex-wrap:wrap; gap:6px 10px; align-items:center; margin-bottom:5px; }}
  .prio{{ font-size:10.5px; font-weight:800; letter-spacing:.08em; }}
  .card.p-alta .prio{{ color:var(--alta); }}
  .card.p-media .prio{{ color:var(--media); }}
  .card.p-baja .prio{{ color:var(--baja); }}
  .plant{{ font-size:12px; color:var(--ink3); font-weight:600; }}
  h2{{ font-size:18px; letter-spacing:-.01em; margin-bottom:5px; }}
  .why{{ font-size:13.5px; color:var(--ink2); }}
  .cta{{ font-size:13px; font-weight:800; color:var(--verde2); margin-top:9px; }}
  .todas{{ display:block; text-align:center; margin:22px auto 0; color:var(--verde);
    font-weight:700; font-size:14px; }}
  .nota{{ text-align:center; color:var(--ink3); font-size:12.5px; margin-top:22px; }}
  .react{{ text-align:center; padding:24px 0 4px; }}
  .react .rt{{ font-size:14.5px; font-weight:700; margin-bottom:10px; }}
  .react .btns{{ display:flex; justify-content:center; gap:10px; }}
  .react button{{ font-size:24px; background:var(--card); border:1px solid var(--line);
    border-radius:13px; width:52px; height:52px; cursor:pointer; }}
  .react button.sel{{ background:#e6f0da; border-color:var(--verde2); transform:scale(1.08); }}
  .react button:disabled:not(.sel){{ opacity:.4; }}
  .react .react-hint{{ font-size:12px; color:var(--verde2); margin-top:7px; min-height:14px; }}
</style>
</head><body>
<a class="back" href="{SITE}index.html">← Volver al sitio estable</a>
<div class="wrap">
  <header>
    <span class="kicker">Cada 2 días · Todas las especies</span>
    <h1>🎯 Las 3 del jardín</h1>
    <div class="date">Edición del {date_h}</div>
    <p class="lede">Miré las <b>{len(PLANTS)} especies</b> del catálogo y sus <b>{total_active} tareas pendientes</b>. Si solo vas a hacer tres cosas, que sean estas:</p>
  </header>
{''.join(cards)}
  <a class="todas" href="{SITE}tareas.html">Ver todas las tareas pendientes →</a>
  <div class="react">
    <div class="rt">¿Te sirve este top 3 cada 2 días?</div>
    <div class="btns">
      <button onclick="engageReact('top3','love', this)">😍</button>
      <button onclick="engageReact('top3','like', this)">🙂</button>
      <button onclick="engageReact('top3','meh', this)">😐</button>
      <button onclick="engageReact('top3','no', this)">🙅</button>
    </div>
    <div class="react-hint"></div>
  </div>
  <div class="nota">Experiencia pedida por vos (04/07/2026). Se regenera con datos frescos cada 2 días<br>
  respetando lo que ya marcaste como hecho o pospuesto.</div>
</div>
<script src="engage.js"></script>
</body></html>
"""


# ---------------------------------------------------------------- queue entry

def _clip(s, n):
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


def build_entry(today, tasks, send_at):
    date_str = today.isoformat()
    plants = []
    for t in tasks:
        if t["plant_common"] not in plants:
            plants.append(t["plant_common"])
    body = "Tus 3 prioritarias de hoy: " + " · ".join(plants) + ". Una pantalla, tres cosas, listo."
    return {
        "id": f"{date_str}-top3",
        "title": _clip("🎯 Las 3 del jardín (edición fresca)", 48),
        "body": _clip(body, 130),
        "url": f"{SITE}engage/top3-tareas.html?d={date_str}",
        "format": "tarea",
        "send_at": f"{date_str}T{send_at}:00-03:00",
        "expires_at": f"{date_str}T21:30:00-03:00",
        "status": "pending",
        "sent_at": None,
        "fail_reason": None,
        "created_by": f"gen_top3_tareas {date_str}",
    }


def merge_into_queue(entry):
    try:
        with open(QUEUE_PATH, encoding="utf-8") as f:
            queue = json.load(f)
    except (OSError, ValueError):
        queue = {"notifications": []}
    kept = [n for n in queue.get("notifications", []) if n["id"] != entry["id"]]
    queue["notifications"] = kept + [entry]
    queue["_updated_at"] = datetime.datetime.now().isoformat()
    with open(QUEUE_PATH, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return queue


if __name__ == "__main__":
    args = sys.argv[1:]
    flags = {a for a in args if a.startswith("--") and "=" not in a}
    send_at = DEFAULT_SEND
    if "--send-at" in args:
        send_at = args[args.index("--send-at") + 1]
    dates = [a for a in args if not a.startswith("--") and a != send_at]
    today = datetime.date.fromisoformat(dates[0]) if dates else datetime.date.today()

    if not is_due_day(today) and "--force" not in flags:
        print(f"{today}: no toca por cadencia (cada 2 días desde {ANCHOR}). Próxima: "
              f"{today + datetime.timedelta(days=(2 - (today - ANCHOR).days % 2) % 2 or 2)}. "
              "Usá --force para generar igual.")
        sys.exit(0)

    tasks = top3(today)
    if len(tasks) < 1:
        print(f"{today}: no hay tareas activas — no se genera nada (no inventamos urgencias).")
        sys.exit(0)
    total = len(active_tasks(today))
    entry = build_entry(today, tasks, send_at)
    print(json.dumps(entry, ensure_ascii=False, indent=2))
    for i, t in enumerate(tasks, 1):
        print(f"  {i}. [{t['priority']}] {t['plant_common']} — {t['title']} ({t['due_label']})")

    if "--merge" in flags:
        with open(PAGE_PATH, "w", encoding="utf-8") as f:
            f.write(render_page(today, tasks, total))
        print(f"→ página regenerada: {os.path.relpath(PAGE_PATH, ROOT)}")
        q = merge_into_queue(entry)
        ids = [n["id"] for n in q["notifications"]]
        assert len(ids) == len(set(ids)), "HAY IDs DUPLICADOS EN LA COLA"
        print(f"→ mergeada en queue.json ({len(ids)} entries totales)")
