# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3/día (bajada el 15/06 por fatiga)

**Cadencia hoy = 3 notificaciones/día, curadas a mano.** Se bajó desde la cadencia
alta (9–39/día) el 15/06 por una señal de fatiga inequívoca (ver abajo). El usuario
pidió explícitamente 3 el 15/06. Cuando la biblioteca de formatos crezca y haya señal
de hambre (clicks consistentes), se puede volver a subir — NO antes.

**Cada notificación tiene que SENTIRSE única — otro FORMATO/interacción, no el mismo
molde con otro dato.** El usuario fue tajante (14/06): "no quiero más notificaciones que
lleven a una especie en su formato actual"; "siento que mandás mucho de lo mismo". Una
URL única NO es una experiencia única. Reglas:
- Con 3/día curo a mano: **cada push a un FORMATO distinto** (rueda / quiz / curio / mazo).
  Nunca dos del mismo formato el mismo día. **PROHIBIDO fichas `#especie` sueltas.**
- Si vuelve la cadencia alta, generar con `python tools/gen_queue.py <fecha> <cant>`
  (rota formatos, assert anti-duplicados). Acepta cantidad como 2º arg.
- NUNCA linkear a una página efímera que vayas a borrar el mismo día (da 404 — pasó el 13/06).
- Formatos vivos: 🌀 rueda-ano (aprobada), 💡 feed curiosidades (promovido), 🧠 quiz-jardin,
  🃏 mazo-jardin (en re-test 15/06).

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06).
- Logging parchado 12-13/06 (outbox localStorage + endpoint serverless `/api/feedback` sin PAT).

## 🚨 SEÑAL DE FATIGA (14/06) — base de la bajada a 3/día

- El 14/06 se mandaron **39 pushes** (u01–u39, todos 201 en send_log).
- `engagement.json` NO registró **ni un solo evento** después de 2026-06-14T01:11 → 0 clicks,
  0 reacciones, 0 aprobaciones, 0 rechazos de esos 39 pushes.
- Lectura: 39/día es sobre-saturación total — el usuario tuneó el canal por completo. Confirma
  la regla "N notifs al mismo destino/exceso mata la novedad" llevada al extremo. → cadencia 3/día,
  curada, y nada de floods. La credibilidad del canal es el activo; recuperarla > volumen.
- ⚠️ El mazo v1 (proposal 14/06) quedó confounded por este flood: su único promotor (u11) cayó
  en la avalancha ignorada. Por eso se RE-LANZA hoy con test limpio (ver abajo).

## 🎯 SEÑAL REAL MEDIDA (datos del 12-13/06) — sigue siendo la base

Dos ganadores claros y dos perdedores claros:
- **GANADOR #1 — Curiosidades (contenido):** TODAS las cartas reaccionadas 😍 (guayabo x2,
  durazno x2, aguaribay, caqui, hibisco) + **104 s de dwell**. Las curiosidades verificadas de
  SUS plantas son lo que más engancha. Sección fija promovida.
- **GANADOR #2 — Rueda del año (formato):** **APROBADA** (proposal_approved 13/06 21:37) + **87 s
  dwell** scroll 100%. Animación 3D + interacción. Promovida, link fijo en la nav del inicio.
- **PERDEDOR — sol-jardin (mapa de luz):** rechazada + reacción "no" + proposal_rejected x3.
- **PERDEDOR — ano-jardin (calendario de listas):** rechazada + reacción "no".

**Lectura inequívoca:** el usuario quiere **deleite (curiosidad + animación)**, NO herramientas
utilitarias (mapas, calendarios de listas, dashboards estáticos). No volver a pushear esas vistas.

## Conclusiones de los pushes enviados hasta ahora (por feedback real)

- **11/06 — 1 push** (poda), 20:00: inconcluyente (deshora, 1ª noche).
- **12/06 día — curiosidades @14:30 → GANADOR.** "MUY buena la notificación y la landing" (chat) +
  😍 a la Palta Hass. Origen de la sección Curiosidades. Cartas con nombre propio caen mejor.
- **12/06 noche — barrida f01-f08 (8 pushes a la MISMA página) → SOBRE-SATURACIÓN.** De acá sale
  "1 destino único por push".
- **13/06 — cadencia 15min (a + s01-s13 + r01-r08).** Con destinos rotados el usuario estuvo ACTIVO:
  aprobó la rueda, rechazó las vistas utilitarias, reaccionó 😍 a curiosidades. La rotación importa.
- **14/06 — 39 pushes → FATIGA TOTAL (0 eventos).** El volumen mató todo. Es el techo a no repetir.
  El ángulo no se pudo medir porque el usuario dejó de mirar. → bajar a 3/día curadas.

## Principios vigentes (no romper)

1. **Una experiencia/destino DISTINTO por push.** Excepción: variaciones de experiencias APROBADAS.
2. **Deleite > herramientas.** Curiosidades verificadas + experiencias animadas/interactivas.
   NO mapas, NO calendarios de listas, NO dashboards utilitarios.
3. **Verificar la horticultura antes de publicar.** Jamás inventar urgencia ni estado físico no
   observable. Un push errado quema el canal entero.
4. **El destino cumple lo que promete el copy.** Hashes: `#especie=CODE`, `#curiosidades`,
   `rueda-ano.html#m=N`, `#task=ID` (tareas.html).
5. **Promotores de proposal → slot diurno (mediodía).** Primer `send_at` siempre ≥60 min post-corrida.
6. **Proposals sin aprobación explícita de un día anterior se borran hoy.**
7. **Volumen bajo y curado > flood.** El techo medido del usuario está MUY por debajo de 39/día.

## Decisiones de hoy (15/06)

- **CADENCIA → 3/día.** Bajada por la fatiga del 14/06 (39 pushes, 0 eventos) + pedido explícito.
- **DROP mazo v1** (2026-06-14, pending sin aprobación) — pero test confounded por el flood.
  **RE-LANZADO** como `2026-06-15-mazo-jardin.html` (mismo contenido, id nuevo) para medirlo limpio.
- **Cola 3 únicas:** (a) 🃏 Mazo @12:00 (slot diurno, promueve la proposal); (b) 💡 Curiosidades
  feed @15:30 (contenido ganador); (c) 🌀 Rueda del año #m=6 @19:00 (formato ganador, mes actual).
- Sin proposal extra: el re-test del mazo ES el experimento del día.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en dormancia: poco que hacer. Tareas reales casi todas `done`; las `active` son IDs
  scheduleadas para floración primavera (B-49 glicinia?, B-46-9 pinnada, B-41 caqui mayo 2027). NO
  inventar urgencia de invierno.
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno B-30/35,
  ciruelos F-4/B-38, caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept post-helada**:
  buganvilia B-1, lantana B-29, cítricos, paltas. NO inventar.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Tareas/uploads del usuario → las procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Regenerar el dataset `M` de la rueda desde data_plants.py en build-time** (hoy es snapshot estático).
- **Reconciliar arrays `pruning`** con el timing corregido antes de hacer vista de poda.
- **Si el mazo engancha en su re-test**, integrarlo como experiencia fija y generar sus cartas desde
  los `fun_fact` verificados de data_plants.py.
- Si la cadencia 3/día junta clicks consistentes varios días, evaluar subir a 4-5 (no más) con formatos rotados.
