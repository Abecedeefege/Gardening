#!/usr/bin/env python3
"""Genera docs/notifications/queue.json rotando FORMATOS de experiencia distintos.

Regla del usuario (14/06): cada notificación tiene que SENTIRSE única — no
alcanza con cambiar el dato dentro del mismo molde. Una URL única ≠ una
experiencia única. POR ESO: **prohibido mandar a fichas `#especie` sueltas**
(es siempre el mismo formato). En su lugar rotamos una BIBLIOTECA de formatos,
cada uno una interacción distinta, y dentro de cada formato variamos el
contenido (rueda en otro mes, quiz con otras preguntas, etc.).

Para que se sienta variado:
  - Interleave por TIPO: dos pushes seguidos nunca son el mismo formato.
  - Cantidad moderada (default 9/día ≈ cada ~70 min). Subir SOLO cuando la
    biblioteca de formatos crezca (más formatos = más frecuencia sin repetir).

Uso:  python tools/gen_queue.py [YYYY-MM-DD] [cantidad]

Para agregar un formato nuevo: sumá instancias a build_formats() abajo.
"""
import json, sys, os, random, datetime

SITE = "https://gardening-chi.vercel.app/"
RUEDA = SITE + "engage/2026-06-13-rueda-ano.html"
QUIZ = SITE + "engage/quiz-jardin.html"
CUR = SITE + "index.html#curiosidades"

MESES = {1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",
         8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}

def build_formats():
    """Devuelve dict tipo -> lista de instancias (url, title, body), cada una distinta."""
    F = {}
    # FORMATO: rueda del año (APROBADA) — variación por mes destacado
    F["rueda"] = [
        (RUEDA + "#m=11", "\U0001F300 Tu jardín en noviembre", "Tocá la rueda del año: noviembre es tu mes pico, 32 plantas en flor a la vez."),
        (RUEDA + "#m=3",  "\U0001F300 Marzo: tu cosecha", "La rueda del año abre en marzo — mirá qué tenés con fruta para cosechar."),
        (RUEDA + "#m=10", "\U0001F300 Octubre arranca la fiesta", "La rueda del año en octubre: empieza la explosión de flores. Tocá y mirá."),
        (RUEDA + "#m=6",  "\U0001F300 Tu jardín ahora (junio)", "La rueda del año en este mes. ¿Cuánto duerme tu jardín en pleno invierno?"),
    ]
    # FORMATO: quiz interactivo (NUEVO) — variación por set de preguntas
    F["quiz"] = [
        (QUIZ + "#set=1", "\U0001F9E0 ¿Cuánto conocés tu jardín?", "5 preguntas sobre tus plantas. ¿Llegás a maestro jardinero?"),
        (QUIZ + "#set=2", "\U0001F9E0 Ronda nueva: tu jardín", "Otras 5 preguntas. La última vez, ¿cuántas acertaste?"),
        (QUIZ + "#set=3", "\U0001F9E0 Desafío jardinero", "5 preguntas nuevas sobre las plantas que tenés en casa."),
        (QUIZ + "#set=4", "\U0001F9E0 ¿Sos crack de tu jardín?", "Última ronda de preguntas. A ver ese puntaje."),
    ]
    # FORMATO: feed de curiosidades (PERMANENTE, lo que más enganchó)
    F["curio"] = [
        (CUR, "\U0001F4A1 Curiosidades de tus plantas", "El feed de historias verificadas de tus 52 plantas. Entrá y picá las que te copen."),
    ]
    return F

def build(date_str, count=9):
    F = build_formats()
    rnd = random.Random(date_str)
    for t in F:
        rnd.shuffle(F[t])
    # orden de tipos para el interleave (rotado por día)
    types = list(F.keys()); rnd.shuffle(types)
    # weave: round-robin por tipo → dos seguidos nunca del mismo formato
    picks, ti, used = [], 0, set()
    cursors = {t: 0 for t in F}
    guard = 0
    while len(picks) < count and guard < 500:
        guard += 1
        t = types[ti % len(types)]; ti += 1
        if cursors[t] < len(F[t]):
            inst = F[t][cursors[t]]; cursors[t] += 1
            if inst[0] not in used:
                used.add(inst[0]); picks.append((t, inst))
        # si ya agotamos todos los tipos, cortar
        if all(cursors[t] >= len(F[t]) for t in F):
            break

    # horarios: repartir 'count' parejo entre 10:30 y 20:00
    start = datetime.datetime.strptime(date_str + " 10:30", "%Y-%m-%d %H:%M")
    end = datetime.datetime.strptime(date_str + " 20:00", "%Y-%m-%d %H:%M")
    span = int((end - start).total_seconds() // 60)
    n = len(picks)
    times = []
    for i in range(n):
        mins = 0 if n == 1 else round(span * i / (n - 1))
        times.append((start + datetime.timedelta(minutes=mins)).strftime("%H:%M"))

    notifs = []
    for i, ((t, inst), hhmm) in enumerate(zip(picks, times)):
        url, title, body = inst
        notifs.append({
            "id": date_str + "-x" + str(i + 1).zfill(2),
            "title": title, "body": body, "url": url, "format": t,
            "send_at": date_str + "T" + hhmm + ":00-03:00",
            "expires_at": date_str + "T22:00:00-03:00",
            "status": "pending", "sent_at": None, "fail_reason": None,
            "created_by": "gen_queue " + date_str,
        })
    return {"_updated_at": datetime.datetime.now().isoformat(), "notifications": notifs}

if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    cnt = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    q = build(date, cnt)
    out = os.path.join(os.path.dirname(__file__), '..', 'docs', 'notifications', 'queue.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(q, f, ensure_ascii=False, indent=2)
    urls = [n['url'] for n in q['notifications']]
    assert len(urls) == len(set(urls)), "HAY URLs DUPLICADAS"
    # chequear que no haya dos formatos iguales seguidos
    fmts = [n['format'] for n in q['notifications']]
    adj = [i for i in range(1, len(fmts)) if fmts[i] == fmts[i-1]]
    print("queue " + date + ": " + str(len(q['notifications'])) + " slots")
    print("  formatos en orden: " + " · ".join(fmts))
    print("  ✓ URLs únicas; " + ("✓ sin formatos adyacentes repetidos" if not adj else "⚠️ adyacentes: " + str(adj)))
