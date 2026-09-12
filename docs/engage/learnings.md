# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🎯 LO DE HOY (sáb 12/09) — LOS DOS SLOTS, EL PRIMERO CON CANAL SANO

Vencieron los 7 días de snooze de **las tres que pospuso el 05/09** (B‑23, B‑24, B‑46‑3) y las traje **agrupadas**, como se lo
prometí en el pie de ayer. **El clima partió la lista en dos y eso fue el contenido:** las dos podas de cítrico **NO** (llovizna
+ ráfagas 30‑45 + su ficha exige «pasado el riesgo de helada» y las madrugadas bajan a **3,5‑4,2°**); **SÍ** cosechar limones
(no hace herida, y su ficha dice que la carga sin cosechar cuesta azahar) y dar vuelta las macetas del vivero. **Las podas
quedaron fechadas el VIERNES 18**, no por una condición sino por **TRES que coinciden en un solo día de siete**: 0,0 mm en los
dos modelos + ráfagas 27‑29 (mínimo semanal, contra 45 hoy y 52 el martes) + mínima 9,3° (la única madrugada sin escarcha).
El jueves 17 hay slot de tarea: cae de víspera.

**APUESTA DEL VIERNES SALDADA:** seco ✅ (0,00 mm) · pico de ráfaga ✅ clavado (dije 30‑32, fue **32,0**) · temperatura ❌❌
(dije 16, me «corregí» a 12,7, fue **14,6**).
⭐ **REGLA NUEVA, la más incómoda hasta ahora: UNA CORRECCIÓN MÍA PUEDE QUEDAR MÁS LEJOS QUE EL ERROR QUE CORREGÍA, Y SE PUBLICA
CON LOS DOS NÚMEROS.** Error original **+1,4°**, mi corrección **−1,9°**. Conclusión útil que le di: **el viento y la lluvia los
tengo finos, el termómetro no** — mis máximas van con ±1,5°. ⭐ **Antes de «corregir» un dato mío, verificar que la corrección
sea mejor que el original:** la humildad mal calibrada también es un dato falso.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS

- **⭐ LO QUE MÁS CONVIRTIÓ EN 9 SEMANAS: la lista de SUS tareas reales, con foto, dónde está y un botón por ítem.** El 05/09
  lo confirmó caro: con las 2 push de la mañana no hizo nada, y de noche estuvo 40 min en `puesta-al-dia` resolviendo 10 tareas.
- **⭐ CUANDO TIENE TRABAJO REAL PENDIENTE, LA EXPERIENCIA COMPITE Y PIERDE** → **debe PARASITAR la tarea, no competirle.** Hoy
  al extremo: la experiencia **es el instrumento del paso 3 de la ficha de B‑46‑3.** Si esto no convierte, no es el encuadre.
- **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO ESCRIBA**, y el tap es su idioma (13 `answer` en una noche). **Una foto con una línea de
  texto es su señal más rica:** síntoma + planta + fecha en un gesto.
- **Las 7 veces que escribió fue LOGÍSTICA, IDENTIFICACIÓN, ORDEN DE TRABAJO, CONSULTA TÉCNICA o PEDIDO DE RE-ENVÍO, jamás
  una reseña:** no esperes veredicto, esperá instrucciones. La caja de feedback va igual en todas.
- **⭐ `engagement.json` SUBCUENTA SU ACTIVIDAD REAL.** El 11/09 escribió a las 08:02 pidiendo el push y ese día quedó con
  **0 eventos**; el flush del cliente llegó a atrasarse **2,5 días**. **Nunca leer «0 eventos» como «no abrió»** sin cruzarlo
  con `task_states`, `uploads.json` y los threads.
- **«Ocultar» no es «sacar»** · **dwell alto sin conversión ≠ éxito** · **el 201 no mide nada** · **nunca 3 push en un día sin
  slot** · **si hubo actividad suya en la última hora, no encolar.**

## 🏁 EL CANAL: CERRADO Y SANO — NO VOLVER A INVESTIGARLO

`send_at` → `sent_at` = **+3,6 s el 10/09 y el 11/09**, contra +263 min (31/08), +89 (03/09), +168 y +75 (07/09): el
`WAIT_CAP_MIN` por evento (`push` → 330, `schedule` → 200, `timeout-minutes: 350`) funciona. ⭐ **Desde el 10/09 las métricas de
contenido SÍ significan algo** (cinco slots que leí como fracaso de contenido eran de canal), pero **medir siempre
`sent_at − send_at` antes de declarar muerto un contenido.**

## 💬 FEEDBACK DE TEXTO — los 3 vivos, ya ejecutados

1. *«Nose cuál es el crespón y la althea»* (03/09) → **al nombrar una especie, foto + dónde está, siempre.** Sin excepción.
2. *«Sacá todas las tareas ya completadas para achicar la página»* (05/09) → hecho. **«Ocultar» no es «sacar».**
3. *«Volvémela a enviar cuando revises con mi feedback en mente»* (05/09) → hecho. **Pide re-envío, no novedad.**

## ⚙️ ESTADO OPERATIVO (12/09/2026)

`pix9` **active** · `uploads.json` 0 pendientes · threads 0 `pending` · `user_tasks.json` 0 sin contestar · `task_states.json`
81 entries — **53 done / 38 active / 11 snoozed** sobre 102 tareas y 51 especies (16 huérfanas, descartarlas siempre) · última
escritura suya en `task_states` **06/09 11:39Z**, último evento de cualquier tipo **06/09 20:31Z** (6 días — ver el subcuento) ·
proposals **93** (54 dropped / 23 promoted / **14 pending** / 1 approved / 1 removed) · **compactación:** vence 14/09 (send_log)
y 17/09 (events).

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium 390×780**
(nunca por offset de caracteres). `audit.js` en scratchpad — playwright en `/opt/node22/lib/node_modules`, chromium en
`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`; descartar `fixed`/`sticky` por **toda la cadena de ancestros** y reportar
el control de **acción**, no el link del índice. Hoy: **tres‑pilas 7,0 %** (el objeto ES el tope) · **jardin‑hoy 24,0 %**.
⭐ **Y MIRAR LA CAPTURA, NO SÓLO EL NÚMERO.** Hoy el audit daba verde y la screenshot mostró dos bugs: `<span>` de etiqueta y
descripción pegados («A tierraBola de raíces») por falta de `display:block`, y un 🥪 donde iba un 🪴.

**#3 EL LARGO TAMBIÉN ES LAYOUT.** Tope operativo **~12 ítems**. Hoy: **3 tarjetas** en jardin‑hoy (las dos podas de cítrico
fueron UNA sola tarjeta: mismo rincón, misma técnica, misma tijera).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA, ganada o perdida, el día que vence, aunque ese día no me toque push.**
  ⭐ **La corrección a su favor vale doble; la que va en contra se dice igual y con el número al lado.**
- **⭐ FRENAR UNA TAREA VALE TANTO COMO PEDIRLA.** Hoy tres frenos en un día: las dos podas, las palmeras del vivero (no van
  hasta 2027) y la lantana. **Una lista de la que yo mismo saco cosas es creíble; una que sólo crece es spam.**
- **⭐ NUEVO: EL CLIMA QUE HABILITA, NO SÓLO EL QUE PROHÍBE.** La llovizna como **la ventaja** del trasplante en vez del
  obstáculo: convierte un día «malo» en el único día bueno para algo. Reverso del clima‑como‑editor, y más fuerte.
- **⭐ NUEVO: LA CONDICIÓN CONVERTIDA EN FECHA POR CONVERGENCIA.** No «el viernes porque no llueve» sino «el único de siete que
  cumple las tres a la vez», con la tabla de los 7 días al lado. Muestra el trabajo.
- **⭐ NUEVO: LA APUESTA FALSABLE SOBRE EL PROPIO OBJETO.** El contador no da puntos: resuelve si mis 23 macetas o el «30+» de
  la ficha estaba mal. Llenar la barra es refutarme.
- **Ayudarlo a HACER > informarlo**; **darle DÓNDE registrar lo que ya hizo** es casi igual de fuerte. · **⭐ AL NOMBRAR UNA
  ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE.** · **El título es el activo más medido.** · **Timing verificado > urgencia inventada.** ·
  **⭐ VERIFICAR MI PROPIO DATO ANTES DE PUBLICARLO** (y también mis correcciones). · **feedback_text = ley.**
  ⚠️ `curl` a open-meteo NO sale del runner: **WebFetch**, `forecast_days=7`, **un modelo por llamada**; para saldar apuestas,
  `past_days` con `best_match`.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero/«El Parte»** · **cero-lectura/duelos binarios** · **checklist de viaje** · **vos-decidís** (el eje AGENCIA vive, el
CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(como
formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak · biografías · dinero/tasación · Wrapped
· fútbol · **mucho texto/cargado** · **era gimmick** · **`podas-vuelta`** · **observacional suelto** («sacale foto a la flor»:
pospuso 8 de un saque) — **va como pedido corto DENTRO de otra cosa, nunca como card propia**.

## 🏆 LÍNEA DE PRODUCTO

**EL TALLER = la única aprobada, en los dos slots.** n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces** y ticks horas
después. n°2: 7/7, cero reacción. n°3 (24/08): leído entero, sin veredicto. **Por qué gana:** ① sustancia técnica sobre SUS
plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ errores anticipados ⑤ diagramas propios. Va
**agrupado dentro** de la landing del slot, nunca en push aparte.
⚠️ Sus ticks (`taller-arbol-<code>`) **NO** escriben `task_states.json`: contar con `generate_tasks_from_plants(PLANTS)` +
`task_states.json['tasks']`, descartando las 16 huérfanas. ⚠️ `pip install Pillow` antes de `build.py`.

**EL OBJETO QUE SE LLENA = la apuesta abierta.** La bandeja (07/09) nunca llegó a leerse. Hoy va el reintento corregido
(`tres-pilas`): el objeto arriba (7,0 %), le pido **CONTAR lo que ya tiene** en vez de **CREAR** contenido nuevo, y la apuesta
falsable va adentro. **≥5 taps = formato probado y se serializa; 0 taps con canal sano y sin competencia de tarea = el formato
muere de verdad y no se reintenta.**

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo define la
  TAREA.** · **La EXPOSICIÓN MEDIDA manda sobre el ledger.** · **Una reedición sin push no consume elenco; con push sí.**
- ⚠️ **VEDADOS HASTA EL 19/09** (exposición del 12/09): B-23, B-24, B-46, B-47, B-37. **HASTA EL 18/09:** B-30, B-35, B-1, F-2.
  **SE LIBERAN EL 13/09:** B-7, B-5a, B-25, B-12, B-15, B-8, B-4, B-43, B-22, B-36, F-3, B-41. **EL 14/09:** I-1, I-2, B-6,
  B-26, B-2, B-10, B-3, F-5, B-27.
- ✅ **LIBRES PARA EL LUNES 14/09:** B-16, F-9, B-44, B-40, F-8, F-10, B-14, B-45, B-48, B-49, B-21, B-28, B-11, B-31, B-33,
  B-39, F-1, B-9, B-18, B-13, B-20, B-32 + los doce del 13. **B-34 fuera de toda cantera: ya no existe.**
- **No antes del 21/09:** propagación/esqueje · «lo que ibas a tirar» · el ejemplar único sin repuesto · la campana de botella ·
  el corte al ras bajo el nudo · el lado este como vivero · el reparto de la ventana por día. **Del 24/09:** el diagnóstico
  sanitario sobre foto suya · la mea culpa de ficha incompleta · «la ventana de este año ya cerró». **Del 25/09:** la ventana
  partida por hora. **Del 26/09:** la corrección de mi propia corrección con los dos errores numerados · la llovizna como
  ventaja · el abuelo y el nieto cítricos a dos metros · el alcohol 70% entre cítricos vecinos · el conteo apostado contra la
  ficha · el storax del liquidámbar.

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo mantenimiento.**

- **Excepción válida y única:** una push que **él pidió por escrito** (pasó el 06/09 y el 11/09). Se anota en el ledger. · **Un
  día sin slot no es un día sin trabajo:** limita las **notificaciones**, no las **ediciones**.
- **Una sola push por slot de experiencia:** original NUEVA + las **aprobadas** de ese slot agrupadas DENTRO.
  **Aprobación = recurrencia** (😍 / slot «sí» / `engageApprove`); pending no se borra, no recurre.
- **`expires_at` se ata a la ventana del contenido, no al 22:00 de rutina.** Hoy: tarea 18:00 (trabajo a la luz del día),
  experiencia 20:00 (el contador se llena incluso adentro).
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`, Asamblea,
  tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en TODAS las tareas; sus
  fotos y comentarios van al **thread**, los procesa `/responder-tareas`.
- **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA). · **04/09:** 42 fotos
  de especie (`ai_status:"n/a"`: NO procesarlas), **no volver a pedir fotos generales**; sin foto: B-41, B-32, B-43, B-46/47,
  B-2B, B-22, B-36. · **B-34 dada de baja con consentimiento escrito — NUNCA borrar una especie sin eso.** · **05/09:** «No
  quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 LUNES 14/09 — los dos slots.** Tarea 10:00: primer día seco‑ish (0,2 mm, 13°); el contenido natural es **preparar el
  viernes 18** (filo + alcohol) y levantar lo que quedó del sábado. Experiencia 18:00: **depende de si tocó el contador** —
  ≥5 taps → serializar el objeto (el vivero se re-revisa en octubre, ya se lo prometí); 0 taps con canal sano → el formato
  objeto muere y va sustancia técnica pura estilo taller.
- **⭐ COBRAR EL SALDO** con `past_days` + `best_match`: hoy afirmé 11° de máxima, llovizna de mañana y ráfagas 30‑45 (se cobra
  el lunes). **El saldo grande es el viernes 18** — prometí 0,0 mm, 22° y ráfagas 27‑29 como el mejor día de la semana: se cobra
  el sábado 19 sí o sí.
- **Si vuelve el censo del vivero:** hay tareas reales que escribir en `data_plants.py` y el «~30+ plantines» de la ficha de
  B‑46 hay que corregirlo al número verdadero.
- **19/09: vuelven las 5** que pospuso (B-46-5, B-47-3, B-13-2, B-20, B-32). **27/09:** B-41. **15/10:** B-45. · **≈05/10:**
  semana 4 de la bandeja, recordarle qué mirar (prometido en su tabla).
- **Si contesta el tri-botón de B-35:** «igual de mal» → la tarea de cobre de julio nombra los dos ejemplares en el título;
  «ese está sano» → hay un dato de foco que vale una card entera.
- **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta (feb y may-sep) · la coronita F-5 en octubre · el
  fun_fact NASA de la cinta · el Persia/China del durazno · «cada limón viene de una flor única, no de racimos».
