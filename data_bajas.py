"""Especies dadas de baja del catálogo, con el pedido del usuario que las dio de baja.

No entra al build. Existe para poder reponer una especie si el usuario se arrepiente.
"""

BAJAS = [
    # B-34 — Mandioca brava (tentativa, Manihot grahamii).
    # Baja pedida por el usuario desde la app el 2026-09-04T16:04:30Z
    # (user_tasks.json / uploads.json, task user-1788537870474-5847):
    #   «Esta planta la saqué.  No existe más, podés eliminarla»
    # Ejecutada por /engagement el 2026-09-05. Sus fotos siguen en docs/images/uploads/B-34/.
    {
        "id_codes": ["B-34"], "zone": "fondo",
        "common": "Mandioca brava (tentativa)",
        "charrua": "",
        "sci": "Manihot grahamii (a confirmar con flor)",
        "other_names": "Yuca brava, falsa yuca, mandioca de jardín",
        "desc": "Identificación tentativa por hojas palmadas con 7-9 lóbulos lanceolados profundamente divididos, típicas del género Manihot. M. grahamii es nativa del Cono Sur (Uruguay, Argentina, sur de Brasil) y se usa como ornamental — NO comestible (tiene glucósidos cianogénicos, distinta de la mandioca de mesa M. esculenta). Confirmación definitiva con flor en primavera.",
        "type": "perenne",
        "fun_fact": "El látex blanco del tallo (sale al cortar una rama) tiene compuestos cianogénicos — típicos del género. Por eso 'brava': no comer hojas ni raíz. La especie comestible (M. esculenta, mandioca de mesa) es pariente cercana pero detoxificada por selección humana milenaria.",
        "prune_when": "Fines de invierno (agosto). Tolera poda fuerte si se quiere reducir altura.",
        "prune_how": "Recortar tallos viejos a 30-50 cm para forzar brotación nueva en primavera. Eliminar ramas secas o cruzadas. Usar guantes — el látex irrita piel sensible.",
        "water": "Moderado. Tolera sequía una vez establecida. Riego semanal en verano si seco prolongado, en invierno casi nada.",
        "light": "Pleno sol a media sombra.",
        "tags": ["nativa", "ornamental", "perenne"],
        "loc_photo": "FondoCasa_VecinoFondo.jpg",
        "main_photo": "PXL_20260428_131001512_MP.jpg",
        "flowering": [10, 11, 12],
        "fruiting": [12, 1, 2],
        "pruning": [8],
        "urgency": {
            "priority": "baja",
            "title": "Confirmar especie con foto de flor",
            "short_desc": "Identificación tentativa: Manihot grahamii. Falta confirmar con flor (oct-dic) o cápsula trígona del fruto.",
            "detail": "Por las hojas palmadas profundamente lobuladas con 7-9 lóbulos lanceolados puntiagudos y bordes lisos, se identificó tentativamente como Manihot grahamii (mandioca brava ornamental, nativa del Cono Sur). Para descartar Manihot esculenta (mandioca de mesa, casi idéntica en hoja) y otras palmadas (Schefflera, Cnidoscolus), hace falta ver la flor: M. grahamii tiene racimos terminales con flores monoicas pequeñas, sépalos campanulados rojizos en las femeninas, blancos-amarillentos en las masculinas. Aparece en primavera-inicio verano (oct-dic en Montevideo).",
            "how_to": "1) Esperar la primavera (oct-nov 2026). 2) Cuando aparezcan inflorescencias en la punta de los tallos, sacar foto cercana de un racimo entero — incluyendo flores masculinas (más pequeñas, más numerosas) y femeninas (más grandes, en la base del racimo). 3) Foto del cáliz/sépalos de una flor — color y forma son diagnósticos. 4) Si forman fruto (cápsula globosa-trígona ~1.5 cm), foto del fruto verde y maduro. 5) Subir desde la app.",
            "tips": "Si sale látex blanco al romper una hoja o tallo, eso ya confirma género Manihot (y descarta Schefflera). Tip: sacar una hojita y tocar el corte con el dedo — debería aparecer látex blanco lechoso en segundos. Confirmar con foto del corte fresco si querés acelerar la identificación sin esperar la flor.",
            "when": "Octubre-diciembre 2026 (cuando florezca)",
            "due_month": 10,
            "due_year": 2026,
        },
    },
]
