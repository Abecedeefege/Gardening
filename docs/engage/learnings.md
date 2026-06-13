# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE (pedido del usuario 13/06) — REEMPLAZA el "3/día"

**El usuario pidió: una notificación cada 15 min (subida desde 30 el 13/06 tarde — "volvete loco"), ventana diurna (10:30–20:00
UY), HASTA QUE PIDA MENOS.** NO 3/día mientras esté vigente esto. Reglas:
- Llená `queue.json` con ~40 slots cada 15 min (10:30→20:00). **Cada uno a una
  experiencia/destino DISTINTO** (principio de abajo). Apoyate en destinos
  PERMANENTES y vivos: fichas `index.html#especie=CODE` (cada planta = un destino
  distinto que muestra su curiosidad), `index.html#curiosidades`, y las
  experiencias `engage/*` que existan ese día. NUNCA linkear a una página efímera
  que vayas a borrar el mismo día (da 404 — ya pasó el 13/06).
- Como el cron de Actions es poco confiable y corta 20:30, conviene un driver que
  haga push a la cola cada ~14 min en la ventana (ver tools/, o rearmar manual).
- El usuario pidió experiencias MÁS extensas/animadas/interactivas ("volvete loco"). Priorizar
  las experiencias ricas (rueda-ano animada, sol-jardin, ano-jardin) sobre fichas sueltas.
  Construir nuevas experiencias inmersivas seguido. Vivas hoy: rueda-ano, sol-jardin, ano-jardin.
- Cuando el usuario diga "menos/basta", volver a 3/día (o lo que pida) y borrar
  esta sección.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06).
- **Logging de feedback estuvo ROTO** hasta 12-13/06: el write a `engagement.json`
  era PAT-dependiente y fallaba al minimizar la app en mobile → el archivo
  quedaba en 0 eventos. Parchado con (1) outbox en localStorage (escribe sincrónico
  antes de mandar, reintenta al volver a foco) y (2) endpoint serverless
  `/api/feedback` que escribe al repo SIN PAT. **Por eso `engagement.json` sigue
  vacío al 13/06**: los datos previos a la fix no se guardaron. Regla: hasta ver
  el primer evento real entrar, NO leer "0 eventos" como "no enganchó" — el canal
  de medición recién se está estabilizando. El feedback fuerte vino por chat.

## Conclusiones de los pushes enviados hasta ahora (por feedback real)

- **11/06 — 1 push** (calendario de poda corregido), 20:00, ventana 2h. Salió 201
  pero casi seguro no se vio (primera noche, deshora). Señal: inconcluyente.
- **12/06 día — push e1 curiosidades @14:30 → GANADOR.** El usuario respondió por
  chat "MUY buena la notificación y la landing", 😍 a la carta de la Palta Hass y
  siguió pidiendo más datos. La señal positiva más fuerte que tuvo el canal. →
  formato **curiosidad verificada de SUS plantas (historia + dato contraintuitivo)**
  es la dirección. Cartas con nombre propio caen mejor; la buganvilia (Baret) = "meh".
- **12/06 noche — barrida f01-f08 (8 pushes, 20:00-22:00 UY, todas 201).** Sin
  feedback (chat ni log) y todas linkeaban a la MISMA página (curiosidades-2).
  **Conclusión: sobre-saturación.** El usuario marcó después que "N notifs a la
  MISMA experiencia mata la novedad". → de acá sale el principio del 13/06.
  No repetir barridas; los envíos nocturnos (post-20:00) con ventana corta rinden poco.

## Principios vigentes (no romper)

1. **Una experiencia DISTINTA por push.** N notifs → N experiencias diferentes,
   nunca N→1. Mezclar: (a) más de lo que enganchó, (b) variaciones, (c) experiencias
   nuevas.
2. **Contenido que engancha > tareas.** Curiosidades verificadas, vistas lindas,
   módulos nuevos. Tareas solo si son reales y oportunas, nunca como excusa de push.
3. **Verificar la horticultura antes de publicar.** Los datos del catálogo NO son
   verdad revelada. Jamás agregar urgencia que el dato no tiene. Un push errado quema
   la confianza del canal entero.
4. **No afirmar estado físico no observable** ("sin hojas", "floreciendo", "con plaga").
   Frasear condicional o preguntarlo. (El liquidámbar aguanta hoja hasta jul — me equivoqué
   afirmando que estaba pelado en junio.)
5. **El destino cumple lo que promete el copy.** Deep link preciso, nunca index.html
   "a ver qué hay". Hash routing disponible: `#especie=CODE` (abre ficha),
   `#curiosidades` (abre la sub-tab nueva), `#task=ID` (abre tarea en tareas.html).
6. **Precisión de ventanas: ±1 semana o condición observable.** Nunca rangos de 2 meses.
7. **Pushes que promocionan una proposal van en slot diurno** (mediodía), no de noche.
   Primer `send_at` siempre ≥ 60 min después de la corrida (deploy de Vercel).

## Decisiones de hoy (13/06)

- **PROMOVÍ curiosidades** → sub-tab permanente **💡 Curiosidades** en el Home (todas
  las zonas). Rinde los `fun_fact` verificados de `data_plants.py` como feed de cards
  clickeables a la ficha. Código: `render_curiosidades_section` (build.py), `.curio-*`
  (styles.py), `.curio-card` en search + `#curiosidades` hash (scripts.py). Base: el
  feedback de chat (😍) fue la aprobación real (el evento formal no llegó por el bug de
  logging). La página efímera se borró; el contenido vive en el sitio estable.
- **DROP 2026-06-12-poda-invernal** (2º turno sin tracción, ahora con timing diurno).
  Dejo de invertir en la "vista de temporada de poda" — compite con lo que SÍ engancha
  (contenido por-planta). Si vuelve a pedirse, re-medir con el logging ya arreglado.
- **ano-jardin** queda pending: recién hoy recibe su 1er push promotor (13:00) → su
  turno real de medición arranca ahora. No creo proposal nueva (hay una fresca sin testear).
- Borré las páginas efímeras del 12/06 (curiosidades, curiosidades-2, en-numeros,
  estado-jardin, poda-invernal) — ninguna aprobada; las efímeras no sobreviven el día.

## Notificaciones de hoy (13/06) — 3 experiencias distintas

- **08:30 `-a`** — curiosidad gardenia (perfume más caro del mundo) → ficha de especie
  `index.html#especie=B-25`. (más de lo que enganchó; experiencia: ficha completa)
- **13:00 `-b`** — teaser ano-jardin (flor/fruta mes a mes) → `engage/2026-06-13-ano-jardin.html`.
  (experiencia: dashboard interactivo; turno diurno de la proposal)
- **19:30 `-c`** — anuncio sección nueva Curiosidades → `index.html#curiosidades`.
  (experiencia: el feed nuevo de historias; honesto: la sección ES nueva hoy)

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Poda CORREGIDA: jun-jul **solo limpiezas** + trasplantes en dormancia (hortensia B-5,
  pera B-39, pitósporo B-43; jul-ago). **Fines jul-ago**: durazno B-30/35, ciruelos
  F-4/B-38, caqui B-41, crespón B-9, althea B-18, podranea F-2, hibisco B-4, azareros.
  **Sept post-helada** (sensibles al frío): buganvilia B-1, lantana B-29, cítricos
  B-23/24, paltas B-22/36. **Oct/primavera**: clivia B-13, esparraguera B-6. NO inventar urgencias.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer** (pera al sur,
  fondo al este). Buen ángulo de tip estacional.
- Tareas de usuario / uploads pendientes → las procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Reconciliar arrays `pruning` con el timing corregido.** Los `pruning:[6,7,8]`
  todavía marcan junio para muchas plantas, lo que contradice los `when` corregidos
  ("cuando las yemas se hinchen", "pasada la última helada"). Por eso "El año de tu
  jardín" muestra SOLO flor+fruta (exactos), sin poda. Migrar antes de hacer vista de poda anual.
- **Verificar que el logging entra.** Apenas aparezca el 1er evento real en
  `engagement.json` (vía outbox o `/api/feedback`), confirmar que reaction/answer/dwell
  se guardan, y recién ahí volver a confiar en la métrica de clicks por slot/ángulo.
