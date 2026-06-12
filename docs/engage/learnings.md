# Learnings del agente de engagement

Memoria del agente diario (`.claude/commands/engagement.md`). Se REESCRIBE y
condensa cada día — máximo ~150 líneas. No es un log: es lo que el agente
necesita recordar para decidir el contenido de mañana.

## Estado del sistema

- Push subscription del device `pix9`: **active** (desde 11/06 ~17:58 UY).
- **2026-06-11** fue la primera corrida real (vespertina, 18:19 UY).
- **2026-06-12**: corrida matinal normal (~06:05 UY) — se usaron los slots
  default de mañana.

## Datos de ayer (11/06) — leídos el 12/06

- **0 señal de engagement.** `engagement.json` quedó vacío: 0 clicks,
  0 visitas, 0 aprobaciones, 0 rechazos.
- Solo se mandó **1 push**: `2026-06-11-d` ("Corregí el calendario de poda"),
  enviado 20:00 UY (status 201, aceptado por FCM). Las 3 notificaciones
  originales del 11/06 las **frenó el usuario** por contenido hortícola
  equivocado (ver lección abajo) y se reemplazaron por esa única corregida.
- ⚠️ **El dato de "0 clicks" NO es concluyente**: ese push salió 20:00 con
  ventana de 2 h, en la primera noche con push activo. Casi seguro el
  usuario ni lo vio. No leer esto como "el contenido no enganchó".

## Lección CRÍTICA (11/06) — verificar la horticultura antes de publicar

- El usuario frenó las 3 del 11/06: afirmaban que "junio es LA ventana de
  poda" tomando los `due_month=6` del catálogo como verdad + urgencia de
  marketing. Estaba MAL: la mayoría de las podas van a fines del invierno
  (jul-ago) o pasadas las heladas (sep). `data_plants.py` fue corregido.
- Reglas: (1) los datos del catálogo NO son verdad revelada — toda
  afirmación agronómica fuerte se verifica contra fuentes antes de
  publicarla; (2) jamás agregar urgencia que el dato no tiene; (3) un push
  equivocado quema la confianza del canal entero. El usuario: "cuando me
  recomendás o mandás algo pretendo que lo tengas todo investigado".

## QUÉ ENGANCHÓ (12/06 ~16:50) — primera señal positiva real

- El usuario respondió **"MUY buena la notificación y la landing"** a la de
  **curiosidades** (push e1, 14:30). Reaccionó 😍 a la carta de la **Palta Hass**
  ("todas las Hass descienden de un árbol") y siguió la conversación pidiendo
  más datos (preguntó si pasa lo mismo con la palta criolla). → **El formato
  curiosidades-verificadas-de-SUS-plantas FUNCIONA.** Es la dirección a seguir.
  Las cartas tipo "historia con nombre propio + dato contraintuitivo" son las
  que mejor caen. La buganvilia (Jeanne Baret) la marcó "meh" — menos gancho.
- Acción: fin de la cadencia acelerada, vuelta a 3/día. Las curiosidades pasan
  a ser una sección candidata fija. Se agregó carta "Palta uruguaya" (criolla =
  lo opuesto a Hass: de semilla, cada árbol único) respondiendo su pregunta.

## BUG de feedback (12/06) — engagement.json quedó en 0 pese a la reacción

- El usuario reaccionó 😍 pero `engagement.json` tenía 0 eventos. Causa probable:
  `engage.js` mostraba "Anotado" optimista y mandaba el evento con un PUT
  (GET+PUT a GitHub) sin await/persistencia — en mobile, al minimizar la app el
  write no alcanza a completar y se pierde. Fix aplicado: **outbox en
  localStorage** — cada evento se guarda sincrónico ANTES de mandarlo, con flush
  reintentable y dedup por `_id`, y se re-vacía al cargar/volver a foco. El
  monitor automático del loop dependía de engagement.json, así que esto también
  explica por qué no detectó la señal (vino por chat).

## PIVOT DE ESTRATEGIA (12/06 tarde) — engagement, no tareas fabricadas

El usuario fue tajante: cada vez que entra encuentra claims errados o tareas
fabricadas que NO son necesarias hoy (liquidámbar y hortensia con hojas
todavía). El objetivo NO es generar tareas — es que **interactúe / encuentre
interesante lo que ve / le guste un módulo nuevo**. Cambios de rumbo:

1. **Contenido que engancha > tareas.** Prioridad: curiosidades verificadas de
   SUS plantas, vistas lindas (jardín en números), módulos nuevos, mini-quizzes.
   Las tareas solo cuando son reales y oportunas, nunca como excusa de push.
2. **No afirmar estado no observable. Preguntarlo.** La landing
   `estado-jardin.html` pregunta (liquidámbar pelado?, hortensia?, helada?,
   cítricos con fruta?, qué preferís recibir). Esas respuestas (`answer` events)
   son ground-truth: leerlas antes de armar contenido. Si dice "liquidámbar con
   hojas" → NO hablar de podarlo hasta que esté pelado.
3. **Feedback granular.** `engage.js` ahora loguea `reaction` (love/meh/no por
   carta), `answer` (preguntas), y `dwell` (segundos + scroll_pct) pasivo.
   Antes solo había approve/reject → engagement.json quedaba vacío. Ahora hay
   señal fina de QUÉ carta/tema gustó.
4. **Cadencia acelerada hasta buen feedback (pedido explícito).** Mientras no
   haya señal positiva, mandar 1 push nuevo cada ~30 min (slots del dispatcher,
   hasta 20:30 UY), cada uno a una **landing específica** (no homepage). Apenas
   aparezca feedback bueno (reaction=love, proposal_approved, o respuestas
   útiles), **volver a 3/día**. Un loop de 30 min gestiona esto hoy.
5. **El push lleva SIEMPRE a una landing específica** que cumple lo que promete
   el copy. Nunca a index.html "a ver qué hay".
6. **Precisión de ventanas (pedido explícito 12/06): ±1 semana o condición
   observable.** Nunca "junio-julio" ni rangos de 2 meses. Formato: o una
   condición concreta ("cuando pierda TODAS las hojas", "cuando las yemas se
   hinchen, sin abrir", "pasada la última helada") con semana estimada entre
   paréntesis, o directamente una semana ("última semana de julio"). El campo
   `when` de las urgencias en `data_plants.py` ya quedó migrado a este formato.

### Landings vivas (12/06)
- `2026-06-12-curiosidades.html` — 5 historias verificadas (Baret/buganvilia,
  árbol madre Hass, semáforo lantana, limón híbrido, NASA cinta). Reacción por
  carta + approve sección. Push e1 @14:30.
- `2026-06-12-estado-jardin.html` — 5 preguntas observables (data + engagement).
  Push e2 @15:00.
- `2026-06-12-en-numeros.html` — infografía (52 plantas, zonas, nativas/exóticas,
  frutales). Reacción. Push e3 @15:30.

## Lección CRÍTICA (12/06) — no afirmar lo que no podés observar + copy↔destino

- El push `2026-06-12-a` dijo "Sin hojas, el liquidámbar deja leer su
  estructura". El usuario miró el árbol: **todavía tenía casi todas las
  hojas** (el liquidámbar es de los ÚLTIMOS caducos en pelarse, aguanta hoja
  hasta bien entrado junio/julio). Yo afirmé un HECHO OBSERVABLE que no podía
  ver. Regla nueva: **nunca afirmar el estado físico de una planta que no
  puedo observar** ("sin hojas", "está floreciendo", "tiene plaga"). Si el
  contenido depende de un estado, frasearlo condicional ("si ya perdió las
  hojas…", "cuando esté pelado") o anclarlo en algo verificable. El catálogo
  fue corregido: liquidámbar B-37 ahora es "cuando esté pelado (≈julio)" y la
  hortensia lleva "confirmá que esté sin hojas".
- Mismo push: el copy prometía "mirá qué va hoy" (vista curada) pero
  linkeaba a `tareas.html`, que cayó en el Timeline genérico con "Tratar
  fumagina" arriba — nada que ver con el mensaje. Regla nueva: **el destino
  tiene que cumplir lo que promete el copy.** Si hablo de la vista curada de
  poda, linkeo a la página proposal; si hablo de tareas vencidas en general,
  linkeo a `tareas.html`. No prometer curado y entregar el timeline crudo.
- Un push que linkea a `index.html` o `tareas.html` "para ver X" casi siempre
  decepciona: el home no tiene nada específico que ver. Preferir deep links a
  una página/sección que muestre exactamente lo que anuncia el push.

## Lección de timing (12/06)

- Un push promotor de proposal a las 20:00 con ventana de 2 h NO le da un
  turno justo a la proposal. **Los pushes que promocionan una proposal van
  en slot diurno** (mediodía idealmente) para que el usuario tenga horas
  para abrir. Hoy el teaser de la proposal va 13:00, no de noche.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Calendario de poda CORREGIDO: en **junio-julio solo limpiezas** (guayabo
  F-1, liquidámbar B-37, pindós B-8/B-21/B-28) + **trasplantes en dormancia**
  (hortensia B-5, pera B-39, pitósporo B-43; jul-ago) + decisiones (fresno
  F-10, evónimo B-44). **Fines jul-ago**: durazno B-30/35, ciruelos F-4/B-38,
  caqui B-41, crespón B-9, althea B-18, podranea F-2, hibisco B-4, azareros.
  **Septiembre post-helada** (sensibles al frío): buganvilia B-1, lantana
  B-29, cítricos B-23/B-24, paltas B-22/B-36. **Primavera/oct**: clivia B-13,
  esparraguera B-6. NO inventar urgencias.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**
  (pera al sur, fondo al este). Buen ángulo de tip estacional.
- Tarea de usuario activa sin responder (subida 10/06): "Esto es un guayabo
  del país" (`user-1781114206236-60d0`, taggeada a B-15 Hiedra — posible
  mis-tag). La procesa `/actualizar-tareas`, no este agente. Anotada.
- 1 upload pendiente en `uploads.json` (ai_status pending) — también de
  `/actualizar-tareas`.

## Proposals

- **2026-06-11-poda-invernal**: DROPPED el 12/06 (regla de no-supervivencia
  sin aprobación). Pero el test fue confounded por timing (push 20:00, 2 h,
  0 señal). La hipótesis no quedó probada.
- **2026-06-12-poda-invernal** (pending): MISMA vista (4 ventanas: hoy /
  fines jul-ago / post-heladas / primavera), re-lanzada con push de
  mediodía. Hipótesis: con timing diurno justo, una vista estacional
  consolidada debería juntar su primer click/aprobación. Si OTRA VEZ 0
  señal con buen timing → la "vista de temporada" no le sirve a este
  usuario, pivotar de ángulo (lo que más enganchó históricamente fue el
  contenido por-planta interactivo: el "Tour educativo" de la Lantana lo
  pidió el usuario explícitamente).

## Notificaciones de hoy (12/06)

- **08:30** `-a` — tarea estacional (dormancia: trasplante hortensia +
  limpieza liquidámbar) → `tareas.html`.
- **13:00** `-b` — teaser de la proposal de poda → página proposal.
- **19:30** `-c` — tip de heladas (sur/este al amanecer) → `index.html`.

## Próximos experimentos / reglas

- Medir click-through por slot (08:30 / 13:00 / 19:30) y por ángulo
  (tarea / teaser proposal / tip). Primer dato real recién mañana 13/06.
- Si 13/06 muestra 0 clicks en los 3 con timing bueno → empezar a bajar a
  1-2 pushes/día y probar contenido por-planta en vez de listas.
- Slots default mañana: 08:30 / 13:00 / 19:30 (UTC-3). Primer `send_at`
  siempre ≥ 60 min después de la corrida (margen de deploy de Vercel).
</content>
