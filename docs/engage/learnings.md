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

## Contexto del jardín (junio 2026 = invierno)

- Junio es **el** mes de poda invernal: 19 urgencias `due_month=6`
  (8 altas, 9 medias, 2 bajas). Altas: ciruelo F-4, buganvilia B-1,
  hortensia B-5, crespón B-9, althea B-18, durazno B-30/35, liquidámbar
  B-37, caqui B-41. Ese es el gancho real del mes — no inventar urgencias.
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
