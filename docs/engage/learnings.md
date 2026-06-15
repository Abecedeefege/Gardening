# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA + BIBLIOTECA DE FORMATOS (pedido del usuario 14/06)

**Cada notificación tiene que SENTIRSE única — otro FORMATO/interacción, no el
mismo molde con otro dato.** El usuario fue tajante (14/06): "no quiero más
notificaciones que lleven a una especie en su formato actual"; "siento que mandás
mucho de lo mismo". Una URL única NO es una experiencia única. Reglas:
- **GENERÁ LA COLA CON EL SCRIPT:** `python tools/gen_queue.py <YYYY-MM-DD>` (default 9/día).
  Rota una **biblioteca de FORMATOS** distintos (rueda animada, quiz interactivo, feed
  de curiosidades…), nunca dos del mismo formato seguidos. **PROHIBIDO fichas `#especie`
  sueltas** — son "más de lo mismo".
- **Subí la frecuencia SOLO cuando crezca la biblioteca de formatos** (más formatos =
  más frecuencia sin repetir). Con pocos formatos: pocas y únicas > muchas repetidas.
- **Construir formatos nuevos seguido** (es la prioridad). Roadmap: duelo (this/that),
  antes-después con fotos subidas, mapa navegable, scrollytelling, "número del día"
  animado, adiviná-la-planta, cuenta-regresiva de floración, memoria/pares.
  Formatos vivos hoy: 🌀 rueda-ano (aprobada), 🧠 quiz-jardin (nuevo), 💡 feed curiosidades.
- NUNCA linkear a una página efímera que vayas a borrar el mismo día (da 404 — pasó el 13/06).
- Cuando el usuario diga "menos/basta", bajá la cantidad (o a 3/día) y anotalo acá.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06).
- **Logging YA funciona** (parchado 12-13/06 con outbox en localStorage + endpoint serverless
  `/api/feedback` sin PAT). Al 14/06 `engagement.json` tiene 36 eventos reales medidos. Confiar
  en la métrica de clicks/reacciones/dwell por slot y por ángulo.

## 🎯 SEÑAL REAL MEDIDA (datos del 13/06) — la base de toda decisión

Dos ganadores claros y dos perdedores claros:
- **GANADOR #1 — Curiosidades (contenido):** TODAS las cartas reaccionadas 😍 (guayabo x2,
  durazno x2, aguaribay, caqui, hibisco) + **104 s de dwell**. Las curiosidades verificadas de
  SUS plantas son lo que más engancha. → seguir alimentando el feed. Ya es sección fija.
- **GANADOR #2 — Rueda del año (formato):** **APROBADA** (proposal_approved 21:37) + **87 s
  dwell** scroll 100%. La apuesta "volvete loco" (animación 3D + interacción) funcionó.
- **PERDEDOR — sol-jardin (mapa de luz):** rechazada con reacción "no" + **proposal_rejected x3**.
- **PERDEDOR — ano-jardin (calendario de listas):** rechazada + reacción "no".

**Lectura inequívoca:** el usuario quiere **deleite (curiosidad + animación)**, NO herramientas
utilitarias (mapas, calendarios de listas). Regla: construir experiencias animadas/inmersivas y
servir contenido de curiosidad; NO volver a pushear vistas tipo mapa/lista/dashboard estático.

## Conclusiones de los pushes enviados hasta ahora (por feedback real)

- **11/06 — 1 push** (poda corregida), 20:00, ventana 2h: inconcluyente (deshora, 1ª noche).
- **12/06 día — curiosidades @14:30 → GANADOR.** "MUY buena la notificación y la landing" (chat)
  + 😍 a la Palta Hass. Origen de la sección Curiosidades. Cartas con nombre propio caen mejor.
- **12/06 noche — barrida f01-f08 (8 pushes a la MISMA página) → SOBRE-SATURACIÓN.** "N notifs
  al mismo destino mata la novedad". De acá sale el principio "1 destino único por push".
- **13/06 — cadencia 15min (a + s01-s13 + r01-r08, todas 201).** Con la cadencia alta el usuario
  estuvo ACTIVO: aprobó, rechazó y reaccionó (no fatiga). La cadencia 15min funciona MIENTRAS el
  contenido rote a destinos distintos y haya deleite. Los slots utilitarios (sol-jardin) cobraron
  los "no"; los de curiosidad/animación cobraron los 😍/aprobación.

## Principios vigentes (no romper)

1. **Una experiencia/destino DISTINTO por push.** Única excepción: variaciones de experiencias
   APROBADAS (rueda con mes distinto). Lo garantiza `tools/gen_queue.py` — usalo siempre.
2. **Deleite > herramientas.** Curiosidades verificadas + experiencias animadas/interactivas.
   NO mapas, NO calendarios de listas, NO dashboards utilitarios (los rechazó explícitamente).
3. **Verificar la horticultura antes de publicar.** El catálogo NO es verdad revelada. Jamás
   inventar urgencia ni afirmar estado físico no observable. Un push errado quema el canal entero.
4. **El destino cumple lo que promete el copy.** Deep link preciso. Hashes: `#especie=CODE`,
   `#curiosidades`, `rueda-ano.html#m=N`, `#task=ID` (tareas.html).
5. **Promotores de proposal → slot diurno (mediodía).** Primer `send_at` siempre ≥60 min después
   de la corrida (deploy de Vercel).
6. **Proposals sin aprobación explícita de un día anterior se borran hoy** (`git rm`).

## Decisiones de hoy (14/06)

- **PROMOVÍ la rueda del año** (status `approved`→`promoted`). Página queda permanente en su path
  (la cola la deep-linkea con `#m=N`); agregué link fijo «🌀 Rueda del año» en la nav del inicio
  (todo-strip, build.py). Footer de la página: saqué el CTA aprobar/rechazar, dejé link a inicio.
- **DROP sol-jardin** (rechazada x3, no estaba registrada → agregué su record de cierre) y borré
  su HTML. **DROP ano-jardin** ya estaba dropped → borré el HTML que seguía en el repo.
- **PROPOSAL NUEVA: 🃏 El mazo de tu jardín** (`2026-06-14-mazo-jardin.html`). Hipótesis: fusionar
  los dos ganadores medidos — contenido de curiosidad (#1) + formato animado/interactivo (#2) —
  en un mazo de flip-cards 3D, 1 curiosidad verificada por planta (13 cartas del dict VERIF).
  Debería batir al feed plano y a la rueda por separado porque suma el gesto de descubrir.
  Promocionada por u11 (13:00). Si no junta aprobación explícita, se borra mañana.
- **Cola de hoy:** `gen_queue.py 2026-06-14 15` → 39 slots únicos 10:30–20:00, + swap de u11 al
  mazo. Mezcla: fichas con dato verificado (caqui, palta criolla, limón, althea, romero, cinta),
  fichas neutrales, variaciones de la rueda (#m=11/10/3/9/4/12), feed de curiosidades, y el mazo.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia (hortensia B-5, pera B-39, pitósporo
  B-43). **Fines jul-ago**: durazno B-30/35, ciruelos F-4/B-38, caqui B-41, crespón B-9, althea
  B-18, podranea F-2, hibisco B-4, azareros. **Sept post-helada** (sensibles): buganvilia B-1,
  lantana B-29, cítricos B-23/24, paltas B-22/36. **Oct**: clivia B-13, esparraguera B-6. NO inventar.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer** (pera al sur, fondo al este).
- Tareas de usuario / uploads → las procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Regenerar el dataset `M` de la rueda desde data_plants.py en build-time.** Hoy es un snapshot
  estático inlineado; al estar promovida conviene que no se desincronice del catálogo.
- **Reconciliar arrays `pruning` con el timing corregido** (varios marcan junio y contradicen los
  `when`). Por eso la rueda muestra solo flor+fruta, sin poda. Migrar antes de hacer vista de poda.
- **Si el mazo engancha**, integrarlo como experiencia fija (sección o entrada en Curiosidades) y
  considerar generar sus cartas desde los `fun_fact` verificados de data_plants.py.
