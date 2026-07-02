#!/usr/bin/env python3
"""Genera docs/notifications/queue.json rotando FORMATOS de experiencia distintos.

Regla del usuario (14/06): **cada push debe explorar un FORMATO nuevo.** Los que
el usuario marca que le gustan se pueden repetir, pero SIEMPRE con contenido
original. Una URL única ≠ una experiencia única → **prohibido fichas `#especie`
sueltas** (es siempre el mismo molde).

Cómo lo logra:
  - BIBLIOTECA de formatos, cada uno una interacción distinta. Se interleavea por
    TIPO: nunca dos del mismo formato seguidos, y se cicla por todos antes de
    repetir un tipo.
  - Los formatos jugables (quiz, duelo, adiviná) y la rueda tienen contenido
    fresco en cada instancia (preguntas/duelos/rondas/mes distintos) → un repetido
    NUNCA es "lo mismo".
  - Cadencia 30 min (pedido del usuario 14/06): ventana 10:30–20:00 = ~20 slots.

Cuantos más formatos haya en build_formats(), más se acerca a "cada push, un
formato nuevo". Construir formatos nuevos es la prioridad permanente.

Uso:  python tools/gen_queue.py [YYYY-MM-DD]
"""
import json, sys, os, random, datetime

SITE = "https://gardening-chi.vercel.app/"
def E(slug): return SITE + "engage/" + slug

def build_formats():
    """tipo -> [(url, title, body)], cada instancia con contenido distinto."""
    F = {}
    # 🌀 Rueda del año: APROBADA por el usuario (proposal_approved 13/06, 87s dwell) y
    # promovida como página permanente + link en la nav del inicio. PERO sacada de la
    # rotación de push el 17/06: tras recortarla 6→3 slots el 16/06 igual juntó otro "no"
    # (van meh/meh/no el 15/06 + no el 16/06 = 4 rechazos por sobre-exposición). El feature
    # sigue vivo y accesible desde la nav; simplemente dejamos de empujarlo por push.
    # 🧠 Quiz (NUEVO) — variación por set de preguntas
    F["quiz"] = [(E("quiz-jardin.html") + "#set=" + str(s), t, b) for (s, t, b) in [
        (1, "\U0001F9E0 ¿Cuánto conocés tu jardín?", "5 preguntas sobre tus plantas. ¿Llegás a maestro jardinero?"),
        (2, "\U0001F9E0 Ronda nueva de trivia", "Otras 5 preguntas. ¿Mejorás tu puntaje?"),
        (3, "\U0001F9E0 Desafío jardinero", "5 preguntas nuevas sobre lo que tenés plantado."),
        (4, "\U0001F9E0 ¿Sos crack de tu jardín?", "Última ronda. A ver ese puntaje."),
    ]]
    # ⚔️ Duelo "¿esta o esta?" (NUEVO) — matchups aleatorios cada vez
    F["duelo"] = [(E("duelo-jardin.html") + "#set=" + str(s), t, b) for (s, t, b) in [
        (1, "⚔️ Duelo: ¿esta o esta?", "Dos de tus plantas se enfrentan. ¿Adiviná cuál gana?"),
        (2, "⚔️ Nuevo duelo de plantas", "6 enfrentamientos entre tus plantas. ¿Cuántos ganás?"),
        (3, "⚔️ Cara a cara en tu jardín", "Nativa vs exótica, frutal vs ornamental… elegí bien."),
        (4, "⚔️ Duelo relámpago", "Rondas nuevas entre tus plantas. ¿Cuánto sabés de las tuyas?"),
    ]]
    # 🔍 Adiviná la planta (NUEVO) — rondas aleatorias cada vez
    F["adivina"] = [(E("adivina-jardin.html") + "#set=" + str(s), t, b) for (s, t, b) in [
        (1, "\U0001F50D Adiviná la planta", "Te doy pistas de una de tus plantas. ¿Sabés cuál es?"),
        (2, "\U0001F50D ¿Qué planta es?", "5 rondas de pistas sobre tu jardín. Adiviná."),
        (3, "\U0001F50D Detective del jardín", "Pistas y opciones: identificá tus plantas."),
        (4, "\U0001F50D ¿Reconocés esta planta?", "Otra ronda de pistas. ¿Cuántas adivinás de tu propio jardín?"),
    ]]
    # ⚡ Verdadero o Falso: DROPPED 17/06. Proposal del 16/06 sin aprobación explícita
    # (regla de no-supervivencia) y con CERO engagement — sus 4 promotores (x04/x09/x14/x19)
    # nunca se abrieron, sepultados en el volumen de 20 pushes/día. Mismo modo de falla que
    # el mazo: nunca tuvo un test limpio. Página eliminada del repo.
    # 💡 Feed de curiosidades (sección fija, lo que más enganchó) — vive en Ideas → Experiencias
    F["curio"] = [(SITE + "ideas.html#curiosidades",
        "\U0001F4A1 Curiosidades de tus plantas", "El feed de historias verificadas de tus 52 plantas.")]
    # 🌍 La vuelta al mundo (NUEVO 15/06) — scrollytelling del origen de tus plantas
    F["mundo"] = [(E("mundo-jardin.html"),
        "\U0001F30D Tu jardín es un mapa del mundo", "Plantas de 5 continentes sin moverte de Montevideo. Hacé el viaje.")]
    # 🧩 Memoria del jardín (NUEVO 15/06) — juego de pares planta↔dato
    F["memoria"] = [(E("memoria-jardin.html") + "#set=" + str(s), t, b) for (s, t, b) in [
        (1, "\U0001F9E9 Memoria del jardín", "Encontrá los pares: cada planta con su dato. ¿En cuántas movidas?"),
        (2, "\U0001F9E9 ¿Tenés buena memoria?", "Juego de pares con tus plantas. Mejorá tu marca."),
    ]]
    return F

def build(date_str, cadence_min=30, max_slots=None):
    F = build_formats()
    rnd = random.Random(date_str)
    for t in F:
        rnd.shuffle(F[t])
    types = list(F.keys()); rnd.shuffle(types)

    # horarios cada 30 min en la ventana diurna
    start = datetime.datetime.strptime(date_str + " 10:30", "%Y-%m-%d %H:%M")
    end = datetime.datetime.strptime(date_str + " 20:00", "%Y-%m-%d %H:%M")
    times, t = [], start
    while t <= end:
        times.append(t.strftime("%H:%M")); t += datetime.timedelta(minutes=cadence_min)

    # interleave: en cada paso, elegir el tipo con MÁS instancias restantes que
    # sea distinto al anterior → nunca dos del mismo formato seguidos (mientras
    # exista un arreglo posible), y se reparten parejo.
    picks, cursors, used, last_ty = [], {k: 0 for k in F}, set(), None
    cap = min(len(times), max_slots) if max_slots else len(times)
    while len(picks) < cap:
        avail = [k for k in F if cursors[k] < len(F[k])]
        if not avail:
            break  # agotamos todas las instancias únicas
        cand = [k for k in avail if k != last_ty] or avail
        cand.sort(key=lambda k: len(F[k]) - cursors[k], reverse=True)
        ty = cand[0]
        inst = F[ty][cursors[ty]]; cursors[ty] += 1
        used.add(inst[0]); picks.append((ty, inst)); last_ty = ty

    notifs = []
    times = times[:len(picks)] if max_slots else times
    for i, ((ty, inst), hhmm) in enumerate(zip(picks, times)):
        url, title, body = inst
        notifs.append({
            "id": date_str + "-x" + str(i + 1).zfill(2),
            "title": title, "body": body, "url": url, "format": ty,
            "send_at": date_str + "T" + hhmm + ":00-03:00",
            "expires_at": date_str + "T22:00:00-03:00",
            "status": "pending", "sent_at": None, "fail_reason": None,
            "created_by": "gen_queue " + date_str,
        })
    return {"_updated_at": datetime.datetime.now().isoformat(), "notifications": notifs}

if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    n = int(sys.argv[2]) if len(sys.argv) > 2 else None
    q = build(date, max_slots=n)
    out = os.path.join(os.path.dirname(__file__), '..', 'docs', 'notifications', 'queue.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(q, f, ensure_ascii=False, indent=2)
    urls = [n['url'] for n in q['notifications']]
    fmts = [n['format'] for n in q['notifications']]
    adj = [i for i in range(1, len(fmts)) if fmts[i] == fmts[i - 1]]
    assert len(urls) == len(set(urls)), "HAY URLs DUPLICADAS"
    from collections import Counter
    print("queue " + date + ": " + str(len(q['notifications'])) + " slots (cada 30 min)")
    print("  mezcla de formatos: " + str(dict(Counter(fmts))))
    print("  ✓ URLs únicas; " + ("✓ sin formato adyacente repetido" if not adj else "⚠️ adyacentes:" + str(adj)))
