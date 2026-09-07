# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🥇 LO PRIMERO DEL 07/09 — LE COBRÉ LA APUESTA Y LE PAGUÉ LA MITAD QUE PERDÍ

El 05/09 publiqué: «del martes 8 al jueves 10 no llueve y no baja de 6°». Hoy la saldé sola, sin que la reclame:

- **Gané la lluvia, y por más de lo prometido.** Mar **0,0/0,0** · mié **0,0/0,0** · jue **0,2/0,0 mm**. El jueves era el día
  en disputa (ECMWF le ponía 1,5 mm) y **se cayó a 0,2**. Los tres días secos en los dos modelos.
- **PERDÍ las mínimas y lo publiqué arriba de todo.** ECMWF ahora da **3,1° el martes y 4,5° el miércoles** al amanecer
  (GFS, 6,0 y 7,8 — se llevan 3 grados). No lo escondí: lo **convertí en instrucción** («salí después de las 10, no al
  amanecer»), que es la única forma en que una derrota mía le sirve de algo a él.
- ⭐ **REGLA NUEVA: una promesa mía se cobra SIEMPRE y ENTERA, ganada o perdida, antes de que él la revise.** La mitad
  perdida vale más que la ganada: es la prueba de que los números no están inflados para que haga click.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS (lo que llevo aprendido del canal)

- **⭐ LO QUE MÁS CONVIRTIÓ EN 7 SEMANAS: la lista de SUS tareas reales, con foto, dónde está y un botón por ítem.**
  El 05/09 lo confirmó de la forma más cara: con las 2 push de la mañana **no hizo nada**, y de noche estuvo 40 minutos
  dentro de `puesta-al-dia` resolviendo 10 tareas y escribiéndome 2 veces. Cero gimmick, cero narrativa.
- **⭐ CUANDO TIENE TRABAJO REAL PENDIENTE, LA EXPERIENCIA COMPITE Y PIERDE.** `el-portón` (sáb 11:00) sigue en **0
  absoluto** al segundo reconteo, el mismo fin de semana que la página de tareas sumó 4 visitas más. **No la rechazó: la
  desplazó.** ⭐ **Corolario que estrené hoy: la experiencia no debe competir con la tarea, debe PARASITARLA.** «La
  bandeja» se alimenta del material que sale de las 8 podas que ya tiene agendadas → sube el valor de la push de las
  10:00 en vez de disputarle atención.
- **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO ESCRIBA**, y el tap es su idioma: 13 `answer` en una noche. **Posponer 8 en 90
  segundos es una edición.** Todo `snoozed` = «sacame esto de adelante» y se ejecuta en la reedición siguiente.
- **La caja de feedback de texto es el control que más convierte del sitio** (2 el 24/08, 1 el 03/09, 2 el 05/09). Va en
  todas. Pero **las 5 veces que escribió fue LOGÍSTICA, IDENTIFICACIÓN u ORDEN DE TRABAJO, jamás una reseña.** Sus
  mensajes son órdenes: **no esperes veredicto, esperá instrucciones y ejecutalas.**
- **«Ocultar» no es «sacar»:** lo que mide es el scroll que le queda, no el DOM. Si pide achicar, se borra del archivo.
- **Dwell alto sin conversión ≠ éxito** · **«no contestó» ≠ «no le interesa»** (03/09: 10 días de silencio y estaba
  entero) · **el status code 201 no mide nada: medir `sent_at − send_at`.**
- **Lección más cara de agosto:** mandé una guía de ejecución a alguien que estaba fuera del país. **Chequear que esté
  físicamente en el jardín antes.** · **Nunca 3 push en un día sin slot** · **si hubo actividad suya en la última hora, no encolar.**

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

| Día | Tarea 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Excepción válida y única:** una push que **él pidió por escrito** (pasó el domingo 06/09). Se anota en el ledger.
- **Una sola push por slot de experiencia:** original NUEVA + las **aprobadas** de ese slot agrupadas DENTRO.
  **Aprobación = recurrencia:** sólo vuelve lo que prendió (😍 / slot «sí» / `engageApprove`); pending no se borra, no
  recurre. **Única aprobada: `el-taller` (n°1), en los dos slots** — hoy va agrupada dentro de la bandeja.
- Contrato de cada experiencia (back-link primero · reacción · slots · caja propia · aprobar/rechazar · pitch de 6
  modelos · `send_at` ≥60 min · `expires_at` 22:00 · `-03:00`): `.claude/commands/engagement.md` §4.
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). Script en scratchpad (`audit.js`): playwright en
`/opt/node22/lib/node_modules`, `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
**Hoy: `la-bandeja` → 3,4 % (11.436 px) · `puesta-al-dia` ed.6 → 17,3 % (12.222 px, venía de 13.078).**

**#3 EL LARGO TAMBIÉN ES LAYOUT.** Tope operativo **~12 ítems**. `puesta-al-dia` sigue en 15 y sólo porque son tareas
suyas; hoy la achiqué borrando la sección «Lo de anoche» (2 notas ya leídas, sin botones) y subiendo la ventana de tijera
arriba de todo.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ NUEVO 07/09 — LA EXPERIENCIA TIENE QUE SER UN OBJETO QUE SE LLENA, NO UN TEXTO CON UN BOTÓN AL FINAL.** Su señal
  más fuerte de 7 semanas fue *tildar*, no leer. «La bandeja» es la primera experiencia cuyo cuerpo ES el control: 9
  casilleros que tilda con las manos sucias mientras trabaja, persistidos en `localStorage` y emitiendo
  `engageAnswer('bandeja-<code>')`. **Es el experimento a leer mañana: si tildó ≥3, el formato se serializa.**
- **Ayudarlo a HACER > informarlo.** Y **darle DÓNDE registrar lo que ya hizo** es casi igual de fuerte.
- **⭐ CUANDO NOMBRÉS UNA ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE.** (03/09 perdí una respuesta entera por nombrar sin
  mostrar: «no sé cuál es el crespón y la althea».) **Las 9 de la bandeja llevan la foto que él mismo subió el 04/09.**
  Cuando **no** tengo foto suya, decirlo en la card y pedírsela.
- **⭐ EL CLIMA COMO EDITOR.** No «hay 15 tareas»: el pronóstico **ordena y descarta**. Hoy subí un escalón: ya no es
  «esta ventana sirve» sino **un día concreto por tarea** (mar: los rústicos · mié, el mejor: los friolentos · jue: las
  paltas), justificado por lo que aguanta cada planta, no por prioridad.
- **⭐ VERIFICAR MI PROPIO DATO ANTES DE PUBLICARLO.** Iba a titular «44 de tus 51 sin repuesto»; lo conté agrupando
  `id_codes` por `sci` y son **42 de 50**. Y **2 de las 9 de la bandeja sí tienen repuesto** (lavanda B-19, jazmín B-2B/C):
  lo declaré en la propia página. **Un número que se cae solo cuesta más que el titular que gana.**
- **⭐ LA CONDICIÓN CONVERTIDA EN FECHA.** Cantera abierta: B-4/B-41 yemas, F-3 brote rojo, B-12 «cuando moleste».
- **PEDIR LA OBSERVACIÓN EN VEZ DE AFIRMARLA.** `flowering` es rango de catálogo, no dato del jardín. Declarar lo que NO sé suma.
- **El título es el activo más medido:** sustantivo concreto + número + algo suyo + pérdida. · **Timing verificado >
  urgencia inventada.** · **feedback_text = ley.** · ⚠️ `curl` a api.open-meteo.com NO sale del runner: **usar WebFetch**,
  `forecast_days=7`, **un modelo por llamada**.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero / diario / «El Parte»** · **cero-lectura / duelos binarios** · **checklist de viaje como deberes** ·
**vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app
pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística
· racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** · **era gimmick** (feed falso,
superpoderes) · **`podas-vuelta` CERRADA** · **contenido observacional suelto** («sacale foto a la flor», «decidí qué
hacer con las 56 palmeras») — pospuso las 8 de un saque: **va como pedido corto DENTRO de otra cosa, nunca como card
propia** (por eso hoy dejé UNA sola foto pedida en toda la página de tareas).

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, 168 s @95 %, **😍 dos veces** y ticks por árbol horas después. n°2: 7/7, 166 s, cero
  reacción. n°3 (24/08): leído entero, sin veredicto.
- **Por qué gana:** ① sustancia técnica real sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla =
  una decisión ④ los errores anticipados ⑤ diagramas propios. **«La bandeja» hereda las cinco** (paso 1-4 + SVG del corte
  + los 5 errores en orden de frecuencia) y agrega el objeto que se llena.
- **Sus ticks (`taller-arbol-<code>`) NO escriben `task_states.json`.** Contar siempre con
  `generate_tasks_from_plants(PLANTS)` + `task_states.json`, **descartando las 16 huérfanas**. ⚠️ `pip install Pillow`.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo define
  la TAREA.**
- **La EXPOSICIÓN MEDIDA manda sobre la contabilidad del ledger:** si `scroll_pct` prueba que no llegó a esa card, está
  **fresca para él** aunque figure «featured». Sólo con evidencia medida, nunca por corazonada.
- ⚠️ **VEDADAS HASTA EL 14/09** (bandeja): I-1, I-2, B-6, B-26, B-2, B-10, B-3, F-5, B-27. **HASTA EL 13/09** (canal
  tarea): B-7, B-5a, B-23, B-25, B-12, B-15, B-8, B-4, B-1, B-29, F-2, F-7, B-43, B-22, B-36, F-3, B-41. **HASTA EL
  12/09:** B-46, B-9, B-18, B-24, B-32, B-20, B-13, B-47.
- ✅ **LIBRES para el sábado 13/09 11:00:** B-16, B-37, F-9, B-44, B-40, F-8, F-10, B-14, B-45, B-48, B-49, B-21, B-28,
  B-11, B-31, B-33, B-39, F-1. **B-34 sale de toda cantera: ya no existe.**
- **No repetir antes del 21/09:** la propagación/esqueje entera · «lo que ibas a tirar» · el ejemplar único / sin
  repuesto · la campana de botella · el corte al ras bajo el nudo · el lado este como vivero · el reparto de la ventana
  por día · «el portón» / el termómetro de 8 días · «un corte fresco + helada de amanecer».
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html` (sus
  botones escriben `task_states.json` vía `/api/tarea`; sus fotos y comentarios van al **thread**, los procesa
  `/responder-tareas`, **NO yo**). · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA).
- **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas). **No volver a pedir fotos generales.** Sin foto:
  B-41, B-32, B-43, B-46/47, B-2B, B-22 y B-36.
- **04/09 (baja):** B-34 eliminada con consentimiento explícito escrito. **NUNCA borrar una especie sin eso.**
- **05/09:** «No quiero tener que cambiar tokens nunca más». ✅ **RESUELTO: hoy `GET /api/sync` devuelve 200** (venía
  502 desde el 05/09). Ya puede volver a guardar todo. `tools/health_check.js` sigue encolando 1 push/día si muere.
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.

## 📈 Estado del sistema + jardín (07/09/2026)

- Push subscription `pix9`: **active**. `/api/sync`: **200 (sano)**. `user_tasks.json`: 0 sin contestar.
  `uploads.json`: 0 pendientes. **Threads: 0 mensajes `pending`** (`/responder-tareas` cerró B-7 y B-41 el 06/09).
- `task_states.json`: **81 entries — 66 done, 11 snoozed, 4 active.** 51 especies.
- **Datos del 06/09 (domingo, 1 push a pedido suyo):** 1 enviada (ed.5, 08:05) · **3 visitas** a `puesta-al-dia` +
  1 a `tasks/plant-B-7.html` · **0 clicks logueados, 0 answers, 0 feedback.** Lectura honesta: **abrió tres veces y no
  tocó nada = «masomenos»**. Es coherente con la ed.5, que era una página de *cierre* (le contaba lo ya resuelto) y no
  le daba nada nuevo para hacer. **Por eso la ed.6 vuelve a ser accionable: 8 cortes con día asignado.**
- Proposals: **92** — 54 dropped / 23 promoted / **13 pending** / 1 approved / 1 removed. `el-porton` cerrada como
  *desplazada, no rechazada*.
- **Compactación 07/09:** `engagement.json` 61 → **53 eventos** (los 8 del 24/08 al `daily_summary`, incluidos los 2
  feedback de logística del viaje, ya resueltos). `send_log` 14 → **12**. `queue.json` limpio: sólo las 2 entries de hoy.

## TODO / próximos experimentos

- **🎯 MAÑANA 08/09 — leer los taps de la bandeja.** `engageAnswer` con qid `bandeja-<code>`. **≥3 tildados = el formato
  «objeto que se llena» se serializa y pasa a ser la línea de producto junto con El Taller. 0 tildados con página
  abierta = el canal experiencia está muerto mientras haya tareas abiertas, y hay que fusionarlo con el canal tarea.**
- **🎯 MAÑANA 08/09 — cobrar la segunda mitad de la apuesta:** si el martes amaneció por encima de 6°, ganó GFS y lo digo;
  si amaneció en 3-4°, ganó ECMWF y **yo perdí**, y también lo digo. Ya está publicado por adelantado.
- **12/09 y 19/09: vuelven las 9 que pospuso.** Traerlas ese día, agrupadas, no de a una. El caqui B-41, el 27/09.
- **Semana 4 de la bandeja (≈05/10): recordarle qué mirar** — lo prometí en la tabla de la página. **Es una promesa con
  fecha: si no la cumplo, quemo el activo que construí hoy.**
- **`taller3-paltas` se reactiva el jueves 10** (B-22/B-36 ya tienen día asignado en la ed.6).
- **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta (feb y may-sep) · la coronita F-5 en octubre
  (cierra su ID pendiente, ya se la pedí) · el fun_fact NASA de la cinta · el bálsamo del liquidámbar B-37.
