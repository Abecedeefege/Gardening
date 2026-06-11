# Learnings del agente de engagement

Memoria del agente diario (`.claude/commands/engagement.md`). Este archivo se
REESCRIBE y condensa cada día — máximo ~150 líneas. No es un log: es lo que
el agente necesita recordar para decidir el contenido de mañana.

## Estado del sistema

- **Primera corrida real: 2026-06-11.** Antes de hoy todo estaba vacío
  (sin learnings, sin eventos, sin send_log, sin proposals).
- Push subscription del device `pix9`: **active** (se suscribió hoy ~17:58
  UY, ~20 min antes de esta corrida). O sea: estas son las PRIMERAS
  notificaciones que el usuario recibe. Cuidar la primera impresión.

## Qué funcionó

(Sin datos de click-through todavía — se mide a partir de mañana.)

## Qué no funcionó

(Sin datos.)

## Horarios

- Slots default: 08:30 / 13:00 / 19:30 (America/Montevideo, UTC-3).
- ⚠️ **Esta corrida fue vespertina (18:19 UY), no a las 06:00 habituales.**
  Como la corrida normal de ~06:00 reescribe `queue.json` antes de los
  slots matinales, encolar para "mañana" se perdería. Por eso las 3 de hoy
  se comprimieron en la ventana que quedaba del dispatcher (07:00–20:30):
  **19:30 / 20:00 / 20:30**, espaciadas 30 min. No es ideal (3 pushes en
  una hora de noche); medir si genera fatiga o si la novedad lo compensa.
- Regla aprendida: si la corrida es tarde, solo sirven los slots que
  queden ANTES de las 20:30 del mismo día. Si es a la mañana, usar los
  defaults.

## Lección 2026-06-11 — VERIFICAR la horticultura antes de publicar (CRÍTICO)

- El usuario frenó las 3 notificaciones del 11/06: el contenido afirmaba
  que "junio es LA ventana de poda" tomando los `due_month=6` del catálogo
  como verdad y agregándole urgencia de marketing. **Estaba mal**: revisando
  fuentes (INIA, manuales de fruticultura), la mayoría de las podas van a
  FINES del invierno (jul-ago: carozo, caqui, crespón, althea) o pasadas
  las heladas (sep: buganvilia, lantana, cítricos, paltas — sensibles al
  frío). En junio solo van limpiezas de madera muerta y trasplantes en
  dormancia. `data_plants.py` fue corregido el 11/06 con estas fechas.
- Reglas derivadas: (1) los datos del catálogo NO son verdad revelada — si
  una notificación o proposal hace una afirmación agronómica fuerte
  (cuándo podar, urgencia, riesgo), verificarla contra fuentes antes de
  publicarla; (2) jamás agregar urgencia que el dato no tiene; (3) el costo
  de un push equivocado es altísimo: quema la confianza del canal entero.
  El usuario lo dijo explícito: "cuando me recomendás o mandás algo
  pretendo que lo tengas todo investigado".

## Contexto del jardín (junio 2026 = invierno)

- Calendario de poda CORREGIDO (11/06): en junio-julio solo limpiezas
  (guayabo F-1, liquidámbar B-37, pindós), trasplante hortensia B-5,
  pera B-39 y pitósporo B-43 (jul-ago), decisiones (fresno F-10, evónimo
  B-44). Fines jul-ago: durazno B-30/35, ciruelos F-4/B-38, caqui B-41,
  crespón B-9, althea B-18, podranea F-2, azareros. Septiembre post-helada:
  buganvilia B-1, lantana B-29, limonero B-23, mandarina B-24, paltas
  B-22/B-36. No inventar urgencias.
- Tarea de usuario activa sin responder (subida 10/06): "Esto es un
  guayabo del país" (user-1781114206236-60d0, `ai_answer` null). La procesa
  `/actualizar-tareas`, no este agente — pero anotada por si reaparece.
- Heladas tardías (jun-ago) pegan más al sur y al este al amanecer
  (ver CLAUDE.md). Buen ángulo de tip estacional.

## Proposals

- **2026-06-11-poda-invernal** (pending): "Plan de poda invernal 2026" —
  pantalla única que agrupa las 19 podas del mes por zona y prioridad.
  Hipótesis: una vista estacional consolidada hace tangible la ventana
  corta de dormancia mejor que la lista dispersa del Timeline. Promovida
  por la notificación `2026-06-11-b`. Si no junta aprobación explícita,
  se descarta mañana (regla del usuario).

## Próximos experimentos

- Medir click-through de las 3 de hoy por slot y por ángulo
  (tarea urgente / teaser proposal / tip helada).
- Si la proposal de poda engancha: promoverla a vista de temporada
  permanente (link desde la nav del sitio en `build.py`).
- Si los 3 pushes nocturnos generan fatiga (0 clicks), bajar a 1-2/día y
  volver a los slots de mañana en la próxima corrida temprana.
