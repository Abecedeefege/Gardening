#!/usr/bin/env python3
"""Genera docs/notifications/queue.json con slots ÚNICOS por destino.

Regla del usuario (13/06): cada notificación debe ir a un destino DISTINTO,
salvo que sea una VARIACIÓN de una experiencia APROBADA. Este generador lo
garantiza por construcción:
  - Backbone: las fichas de las 52 plantas (`index.html#especie=CODE`),
    cada una un destino único. Rotación distinta por día (seed = fecha).
  - Variaciones aprobadas: la rueda del año con un MES distinto cada vez
    (`...rueda-ano.html#m=N`) y el feed de curiosidades. 1 de cada 5 slots.
  - Verifica al final que NO haya URLs repetidas (assert).

Uso:  python tools/gen_queue.py [YYYY-MM-DD] [cadencia_min]
El agente diario debe correr ESTO en vez de escribir la cola a mano.
"""
import json, sys, os, random, datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data_plants import PLANTS

SITE = "https://gardening-chi.vercel.app/"
def esp(code): return SITE + "index.html#especie=" + code
RUEDA = SITE + "engage/2026-06-13-rueda-ano.html"
CUR = SITE + "index.html#curiosidades"

# Hooks con dato VERIFICADO (fact fuerte). El resto usa hook neutral: invita a
# la ficha (contenido ya existente del sitio) sin afirmar un dato nuevo sin
# verificar. A medida que se verifiquen más fun_facts, mové su code acá.
VERIF = {
 "F-8": ("\U0001F336️ Tenés pimienta rosa gourmet", "Los granos de tu aguaribay son la pimienta rosa del delicatessen — y es falsa pimienta."),
 "B-41": ("\U0001F7E0 'Fruta de los dioses'", "Así llamaron los griegos al caqui (Diospyros). En Japón hay caquis de 600 años."),
 "B-36": ("\U0001F951 Todas las Hass vienen de 1 árbol", "Tu palto Hass desciende de un único árbol de 1926. Abrí su ficha."),
 "B-22": ("\U0001F951 Tu palta criolla es irrepetible", "Al revés de la Hass: de semilla, única en el mundo."),
 "B-26": ("\U0001F9E0 El romero mejora la memoria", "Hay un estudio. 'Rocío del mar' en latín. Tocá su ficha."),
 "B-4": ("\U0001F33A Tu hibisco es flor nacional", "De Malasia desde 1960. Cada flor dura un solo día."),
 "F-1": ("\U0001F36C Las flores del guayabo se comen", "Saben a algodón de azúcar; los chicos las comían como golosina."),
 "B-29": ("\U0001F6A6 La lantana es un semáforo", "Cambia de amarillo a rojo para avisar a los insectos qué flor ya polinizó."),
 "B-23": ("\U0001F34B El limón no existe en la naturaleza", "Es un híbrido que inventamos hace 2500 años."),
 "B-30": ("\U0001F351 El durazno miente su origen", "Se llama 'persica' (de Persia) pero es de China, 8000 años."),
 "B-12": ("\U0001F331 Tu cinta hace 40 hijos sola", "La planta más fácil de multiplicar que tenés."),
 "B-18": ("\U0001F1F0\U0001F1F7 La flor que nunca se marchita", "Tu althea es la flor nacional de Corea del Sur."),
 "B-1": ("⛵ La descubrió la 1ª mujer en circunnavegar", "Tu buganvilia, recolectada por Jeanne Baret en 1767, disfrazada de hombre."),
}

def neutral(name, code):
    return ("\U0001F33F Conocé tu " + name,
            "Una historia de " + name + " (" + code + ") que quizás no sabías. Tocá su ficha.")

# Experiencias APROBADAS, como variaciones distintas entre sí:
def approved_variations():
    out = []
    for m in [11, 10, 3, 9, 4, 12]:  # meses de interés (nov = 32 en flor, etc.)
        out.append((RUEDA + "#m=" + str(m),
                    "\U0001F300 La rueda del año",
                    "Tocá la rueda y mirá tu jardín en flor mes a mes."))
    out.append((CUR, "\U0001F4A1 Curiosidades de tus plantas",
                "El feed de historias verificadas de tus 52 plantas."))
    return out

def build(date_str, cadence=15):
    plants = [(p['id_codes'][0], p['common']) for p in PLANTS]
    random.Random(date_str).shuffle(plants)   # rotación distinta por día
    approved = approved_variations()

    start = datetime.datetime.strptime(date_str + " 10:30", "%Y-%m-%d %H:%M")
    end = datetime.datetime.strptime(date_str + " 20:00", "%Y-%m-%d %H:%M")
    times, t = [], start
    while t <= end:
        times.append(t.strftime("%H:%M"))
        t += datetime.timedelta(minutes=cadence)

    notifs, used, pi, ai = [], set(), 0, 0
    for i, hhmm in enumerate(times):
        url = title = body = None
        if i % 5 == 4 and ai < len(approved):        # 1 de cada 5: variación aprobada
            url, title, body = approved[ai]; ai += 1
        if url is None or url in used:                # ficha única
            while pi < len(plants) and esp(plants[pi][0]) in used:
                pi += 1
            if pi >= len(plants):
                break                                 # se acabaron las fichas únicas
            code, name = plants[pi]; pi += 1
            url = esp(code)
            title, body = VERIF.get(code, neutral(name, code))
        used.add(url)
        notifs.append({
            "id": date_str + "-u" + str(i + 1).zfill(2),
            "title": title, "body": body, "url": url,
            "send_at": date_str + "T" + hhmm + ":00-03:00",
            "expires_at": date_str + "T22:00:00-03:00",
            "status": "pending", "sent_at": None, "fail_reason": None,
            "created_by": "gen_queue " + date_str,
        })
    return {"_updated_at": datetime.datetime.now().isoformat(), "notifications": notifs}

if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    cad = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    q = build(date, cad)
    out = os.path.join(os.path.dirname(__file__), '..', 'docs', 'notifications', 'queue.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(q, f, ensure_ascii=False, indent=2)
    urls = [n['url'] for n in q['notifications']]
    assert len(urls) == len(set(urls)), "HAY URLs DUPLICADAS"
    print("queue " + date + ": " + str(len(q['notifications'])) + " slots, cadencia " + str(cad) + "min")
    print("✓ todas las URLs únicas")
