#!/usr/bin/env python3
"""Recordatorios push de TAREAS — planificados para todas las especies.

Las tareas ya no son una sección accesible desde la Home: se comunican por
notificación push. Este generador produce los recordatorios del día y los
mergea en docs/notifications/queue.json (la cola que manda el dispatcher de
GitHub Actions cada 30 min). Complementa a gen_queue.py / al agente de
/engagement, que manejan las notificaciones de experiencias.

Política:
  - TODOS los días (martes a domingo): 1 "tarea del día" a las 10:00 -03:00,
    con deep link a tareas.html#task=<id>. La tarea se elige rotando
    determinísticamente (día del año módulo N) sobre el pool más urgente:
    vencidas + las que vencen este mes; si no hay, rota sobre todas las
    activas. La rotación garantiza que las tareas de TODAS las especies
    pasan por el slot con los días.
  - Los LUNES: resumen semanal a las 10:00 -03:00 ("Tu semana en el jardín",
    cuántas tareas hay para el mes y cuáles encabezan) con deep link a
    tareas.html.

Respeta el estado del usuario (docs/sync/task_states.json, solo lectura):
las tareas done no se recuerdan; las snoozed solo si ya venció el snooze.
Si no hay tareas activas no genera nada — no inventamos urgencias, la
credibilidad de las notificaciones es el activo principal.

Uso:
  python tools/gen_task_reminders.py [YYYY-MM-DD]           # imprime las entries del día
  python tools/gen_task_reminders.py [YYYY-MM-DD] --merge   # además las mergea en queue.json
  python tools/gen_task_reminders.py [YYYY-MM-DD] --plan    # escribe docs/notifications/task_reminders_plan.json
                                                            # (cobertura de todas las especies + simulación 30 días)
"""
import datetime
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
PLAN_PATH = os.path.join(ROOT, "docs", "notifications", "task_reminders_plan.json")

PRIO_EMOJI = {"alta": "🔴", "media": "🟡", "baja": "🟢"}


def load_task_states():
    try:
        with open(STATES_PATH, encoding="utf-8") as f:
            return json.load(f).get("tasks") or {}
    except (OSError, ValueError):
        return {}


def task_status(task_id, states, today):
    """'active' | 'done' | 'snoozed' aplicando la misma auto-reactivación de
    snoozed vencidas que hace el cliente al renderizar."""
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


def sort_candidates(tasks, today):
    prio = {"alta": 0, "media": 1, "baja": 2}
    return sorted(tasks, key=lambda t: (
        0 if is_overdue(t, today) else (1 if is_due_this_month(t, today) else 2),
        prio.get(t["priority"], 3),
        t.get("due_year") or 9999,
        t.get("due_month") or 13,
        t["id"],
    ))


def _clip(s, n):
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


def _entry(nid, title, body, url, date_str):
    return {
        "id": nid,
        "title": _clip(title, 48),
        "body": _clip(body, 130),
        "url": url,
        "format": "tarea",
        "send_at": f"{date_str}T10:00:00-03:00",
        "expires_at": f"{date_str}T21:00:00-03:00",
        "status": "pending",
        "sent_at": None,
        "fail_reason": None,
        "created_by": f"gen_task_reminders {date_str}",
    }


def pick_daily_task(today, tasks):
    """Rotación determinística: el pool urgente (vencidas + del mes) si existe,
    si no todas las activas; índice = día del año módulo N."""
    cands = sort_candidates(tasks, today)
    urgent = [t for t in cands if is_overdue(t, today) or is_due_this_month(t, today)]
    pool = urgent or cands
    if not pool:
        return None
    return pool[today.timetuple().tm_yday % len(pool)]


def daily_entry(today, tasks):
    t = pick_daily_task(today, tasks)
    if t is None:
        return None
    date_str = today.isoformat()
    emoji = PRIO_EMOJI.get(t["priority"], "🌿")
    if is_overdue(t, today):
        title = f"⏰ Pendiente: {t['plant_common']}"
    else:
        title = f"🌿 Tarea del día: {t['plant_common']}"
    body = f"{emoji} {t['title']} · {t['due_label']}. Abrila para marcarla, mandar foto o preguntar."
    # Deep link a la LANDING de la tarea (contexto + conversación con Claude),
    # no al Timeline genérico.
    url = f"{SITE}tasks/{t['id']}.html"
    return _entry(f"{date_str}-task-dia", title, body, url, date_str)


def weekly_entry(today, tasks):
    if not tasks:
        return None
    date_str = today.isoformat()
    cands = sort_candidates(tasks, today)
    month_pool = [t for t in cands if is_overdue(t, today) or is_due_this_month(t, today)]
    n = len(month_pool) or len(cands)
    top = []
    for t in (month_pool or cands):
        if t["plant_common"] not in top:
            top.append(t["plant_common"])
        if len(top) == 3:
            break
    scope = "para este mes" if month_pool else "activas"
    body = f"{n} tareas {scope}: {', '.join(top)}… Mirá el plan y elegí por dónde arrancar."
    return _entry(f"{date_str}-task-semana", "📋 Tu semana en el jardín", body,
                  f"{SITE}tareas.html", date_str)


def build_day(today):
    """Las entries de recordatorio de tareas para una fecha: resumen semanal
    los lunes, tarea del día el resto de los días."""
    tasks = active_tasks(today)
    entry = weekly_entry(today, tasks) if today.weekday() == 0 else daily_entry(today, tasks)
    return [entry] if entry else []


def merge_into_queue(entries):
    try:
        with open(QUEUE_PATH, encoding="utf-8") as f:
            queue = json.load(f)
    except (OSError, ValueError):
        queue = {"notifications": []}
    new_ids = {e["id"] for e in entries}
    kept = [n for n in queue.get("notifications", []) if n["id"] not in new_ids]
    queue["notifications"] = entries + kept
    queue["_updated_at"] = datetime.datetime.now().isoformat()
    with open(QUEUE_PATH, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return queue


def write_plan(today):
    """Escribe el plan completo: política, cobertura por especie (las 52) y
    una simulación de 30 días que muestra la rotación."""
    states = load_task_states()
    all_tasks = generate_tasks_from_plants(PLANTS)
    tasks_out = [{
        "id": t["id"],
        "plant": t["plant_common"],
        "codes": t["plant_codes"],
        "zone": t["plant_zone"],
        "priority": t["priority"],
        "title": t["title"],
        "due_label": t["due_label"],
        "status": task_status(t["id"], states, today),
    } for t in all_tasks]

    schedule = []
    for i in range(30):
        d = today + datetime.timedelta(days=i)
        for e in build_day(d):
            schedule.append({"date": d.isoformat(), "id": e["id"], "title": e["title"], "body": e["body"]})

    species_with_tasks = {t["plant_codes"][0] for t in all_tasks}
    plan = {
        "generated": today.isoformat(),
        "policy": {
            "daily": "Martes a domingo 10:00 -03:00: 1 'tarea del día' (rotación determinística "
                     "sobre vencidas + del mes; cubre todas las especies con los días) → tareas.html#task=<id>",
            "weekly": "Lunes 10:00 -03:00: resumen semanal con conteo y tareas que encabezan → tareas.html",
            "state": "Respeta docs/sync/task_states.json: done no se recuerda, snoozed solo si venció.",
            "dispatch": "Las entries se mergean en docs/notifications/queue.json (corrida diaria de /engagement "
                        "con --merge); el dispatcher de GitHub Actions las manda.",
        },
        "species_total": len(PLANTS),
        "species_with_tasks": len(species_with_tasks),
        "tasks_total": len(all_tasks),
        "tasks_active": sum(1 for t in tasks_out if t["status"] == "active"),
        "schedule_next_30_days": schedule,
        "tasks": tasks_out,
    }
    with open(PLAN_PATH, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return plan


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    flags = {a for a in args if a.startswith("--")}
    dates = [a for a in args if not a.startswith("--")]
    today = datetime.date.fromisoformat(dates[0]) if dates else datetime.date.today()

    entries = build_day(today)
    print(json.dumps(entries, ensure_ascii=False, indent=2))

    if "--merge" in flags:
        q = merge_into_queue(entries)
        ids = [n["id"] for n in q["notifications"]]
        assert len(ids) == len(set(ids)), "HAY IDs DUPLICADOS EN LA COLA"
        print(f"→ mergeadas {len(entries)} en queue.json ({len(ids)} entries totales)")

    if "--plan" in flags:
        plan = write_plan(today)
        print(f"→ plan escrito en {os.path.relpath(PLAN_PATH, ROOT)}: "
              f"{plan['species_with_tasks']}/{plan['species_total']} especies con tareas, "
              f"{plan['tasks_active']}/{plan['tasks_total']} activas, "
              f"{len(plan['schedule_next_30_days'])} recordatorios simulados en 30 días")
