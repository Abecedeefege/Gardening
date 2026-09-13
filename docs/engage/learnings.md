# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🎯 LO DE HOY (dom 13/09) — DÍA SIN SLOT: 0 PUSH, PERO NO 0 TRABAJO

Domingo no entra en la cadencia → **0 notificaciones**. Pero vencía la apuesta del sábado y **una promesa se cobra el día que
vence aunque no me toque escribirle**: reedité `2026-07-24-jardin-hoy.html` en su URL estable **sin push** (no consume elenco).

**EL SALDO DEL SÁBADO, EL PEOR QUE ME TOCÓ PUBLICAR:** dije **11°** → fue **12,4°** (✅ erré 1,4, dentro del ±1,5 prometido) ·
dije ráfagas **30‑45** → fueron **49,0** (❌ 4 sobre mi techo) · dije **0,7‑1,8 mm** → cayeron **2,8** (❌ más que los dos modelos).
⭐ **LA REGLA QUE PUBLIQUÉ AYER CON LETRA GRANDE SE MURIÓ EN 24 HORAS:** ayer escribí «el viento y la lluvia los tengo mucho más
finos que el termómetro» y acerté **sólo** lo que declaré débil, fallando **las dos** que declaré finas. La había armado con **UN
día de datos**. → ⭐ **NO CONSTRUIR UNA LEY SOBRE MÍ MISMO CON UNA SOLA MUESTRA**, y cuando se caiga, publicarla caída el mismo día.
⭐ **LO QUE SÍ QUEDA (aguantarla varias semanas antes de creerle):** los dos errores fueron **para el mismo lado, hacia arriba**
(los modelos suavizan los extremos y en un día feo el extremo es lo que importa) → **al techo de ráfagas sumarle 10% antes de
decidir si sale la tijera** (45 × 1,1 = 49,5 contra 49,0 reales).
⭐ **Y EL CONSUELO QUE NO ME REGALO YO: erré para el lado seguro.** Frené por 45 y 1,8; había 49 y 2,8 → **la decisión aguantó el
error.** Ese es el punto de frenar por **tres condiciones que se suman**: tolera que falle una.
**Ajuste preventivo publicado:** mi «27‑29» del viernes 18 hoy cruza **26‑35** (ECMWF 25,6 · GFS 34,9). El viernes **sigue
ganando** como el menos ventoso de los tres días secos (mié 34‑36, jue 31‑44) y con la única madrugada tibia (7,2° contra
2,9‑5,0), pero **ya no se lo vendo como «calmo»**. Dicho antes de que lo vea él; se revisa el jueves de víspera.

**LAS DOS PUSH DEL SÁBADO** salieron **+3,6 s** (tercer día seguido → el resultado ES de contenido). Partido:
**`jardin-hoy` 10:00 ABIERTA a las 10:25** — latencia de 25 min, la mejor del mes — pero **cero señal posterior**: ni dwell, ni
uno de los 3 botones por tarjeta, ni el link del contador que estaba adentro. **Entró y se fue → «masomenos»:** el título hizo su
trabajo, la página no. **`tres-pilas` 11:00 → CERO eventos, ni un click** (cruzado contra `task_states`, `uploads.json` y
threads: no volvió en todo el finde).
⭐ **HALLAZGO DEL DÍA, Y NO ES DE CONTENIDO — ES DEL SLOT: LA SEGUNDA PUSH DEL DÍA MUERE SI LA PRIMERA CAE CERCA.** 05/09: las
dos en el **mismo minuto** → 0 y 0. 12/09: a **60 min** → convirtió la primera, la segunda ni se abrió. **El sábado 11:00 está a
una hora de la tarea; el lunes 18:00 está a ocho.** ⭐ **Por eso el objeto que se llena NO queda refutado:** falló la
**APERTURA**, no el objeto — **un formato no se refuta con una página que nadie miró.** El lunes 14 18:00 es el test limpio.

## 📊 CONCLUSIONES ACUMULADAS + EL CANAL

- **⭐ LO QUE MÁS CONVIRTIÓ EN 10 SEMANAS: la lista de SUS tareas reales, con foto, dónde está y un botón por ítem.** (05/09:
  con 2 push de mañana no hizo nada; de noche, 40 min en `puesta-al-dia` resolviendo 10 tareas.)
- **⭐ LA EXPERIENCIA DEBE PARASITAR LA TAREA, NO COMPETIRLE** — pero el 12/09 parasitó bien y igual no se abrió: **parasitar el
  CONTENIDO no alcanza si compite por la ATENCIÓN de la misma mañana.**
- **⭐ ABRIR RÁPIDO Y NO HACER NADA ≠ NO ABRIR.** Latencia baja = el título ganó; 0 taps = el cuerpo perdió. Dos diagnósticos.
- **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO ESCRIBA** (13 `answer` en una noche); **una foto con una línea de texto es su señal más
  rica**. Las 7 veces que escribió fue logística/identificación/orden de trabajo/pedido de re-envío, **jamás una reseña**.
- **⭐ `engagement.json` SUBCUENTA** (flush atrasado hasta 2,5 días): nunca leer «0 eventos» como «no abrió» sin cruzar
  `task_states` + `uploads.json` + threads. Hoy se cruzó: **el 0 del sábado es real.**
- **«Ocultar» no es «sacar»** · **dwell alto sin conversión ≠ éxito** · **el 201 no mide nada** · **si hubo actividad suya en la
  última hora, no encolar.**
- 🏁 **CANAL CERRADO Y SANO — no volver a investigarlo:** `send_at` → `sent_at` = **+3,6 s el 10, 11 y 12/09** (contra +263 min
  el 31/08); el `WAIT_CAP_MIN` por evento (`push` → 330, `schedule` → 200, `timeout-minutes: 350`) funciona. **Desde el 10/09 las
  métricas de contenido SÍ significan algo** — pero **medir `sent_at − send_at` antes de declarar muerto un contenido.**

## 💬 FEEDBACK DE TEXTO — los 3 vivos, ya ejecutados (ninguno nuevo desde el 05/09)

1. *«Nose cuál es el crespón y la althea»* (03/09) → **al nombrar una especie, foto + dónde está, siempre.** Sin excepción.
2. *«Sacá todas las tareas ya completadas para achicar la página»* (05/09) → hecho. **«Ocultar» no es «sacar».**
3. *«Volvémela a enviar cuando revises con mi feedback en mente»* (05/09) → hecho. **Pide re-envío, no novedad.**

**Pregunta abierta que le dejé hoy** (caja de `jardin-hoy`): el satélite dice 49 km/h, **él estuvo ahí y yo no** — si el fondo
contra el muro de la cancha de pádel es más reparado que la estación, **mis frenos por viento le están sacando días de poda al
pedo**. Primera vez que le pido un dato que **sólo él** tiene y que **cambia mis reglas**. Sigue viva la de los limones («más de
veinte», contados de su foto del 04/09).

## ⚙️ ESTADO OPERATIVO (13/09/2026)

`pix9` **active** · `uploads.json` 0 pendientes (última foto 08/09) · threads 0 `pending` · `user_tasks.json` 0 sin contestar ·
`task_states.json` 81 entries — **53 done / 38 active / 11 snoozed** sobre 102 tareas y 51 especies (16 huérfanas, descartarlas
siempre), última escritura suya **06/09 11:39Z** · último evento **12/09 13:25Z** · proposals **93** (54 dropped / 23 promoted /
**14 pending** / 1 approved / 1 removed) · **compactación NO vencida**: eventos vencen el **17/09**, `send_log` el **14/09**.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick:** ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
**#2 EL CONTROL VA ARRIBA:** ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium 390×780**
(nunca por offset de caracteres). `audit.js` en scratchpad — playwright en `/opt/node22/lib/node_modules`, chromium en
`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ **Descartar `[hidden]` y los rects de área cero** o reporta 0 % falsos
por los composers plegados. Hoy: **jardin‑hoy 23,0 %**. ⭐ **Y MIRAR LA CAPTURA:** hoy arregló dos etiquetas del `.duo`.
**#3 EL LARGO TAMBIÉN ES LAYOUT:** tope operativo **~12 ítems**. Hoy jardin‑hoy quedó en **3 tarjetas**.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA el día que vence, aunque no me toque push.** La corrección a su favor vale
  doble; la que va en contra se dice igual, con el número al lado. ⭐ **NUEVO: si lo que se cae es una REGLA MÍA, se publica la
  regla caída, no sólo el número.**
- **⭐ NUEVO: NO HACER LEYES SOBRE MÍ MISMO CON UNA MUESTRA** (una conclusión de un día es una coincidencia con pretensiones) ·
  **⭐ EL ERROR PARA EL LADO SEGURO NO ES LO MISMO QUE EL ERROR** (un freno por tres condiciones sobrevive a que falle una) ·
  **⭐ PEDIRLE EL DATO QUE SÓLO ÉL TIENE:** no «¿te gustó?» sino «¿tu rincón es más reparado que la estación? — porque si sí, mis
  reglas están mal y las cambio». **La pregunta que puede refutarme es la única que da ganas de contestar.**
- **⭐ FRENAR UNA TAREA VALE TANTO COMO PEDIRLA** · **⭐ EL CLIMA QUE HABILITA, NO SÓLO EL QUE PROHÍBE** · **⭐ LA CONDICIÓN
  CONVERTIDA EN FECHA POR CONVERGENCIA** · **⭐ LA APUESTA FALSABLE SOBRE EL PROPIO OBJETO.**
- **Ayudarlo a HACER > informarlo** · **darle DÓNDE registrar lo ya hecho** · **⭐ AL NOMBRAR UNA ESPECIE: FOTO + DÓNDE ESTÁ** ·
  **el título es el activo más medido** · **timing verificado > urgencia inventada** · **feedback_text = ley.**
  ⚠️ `curl` a open-meteo NO sale del runner: **WebFetch**, `forecast_days=7`, **un modelo por llamada**; para apuestas,
  `past_days` + `best_match`.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero/«El Parte»** · **cero-lectura/duelos binarios** · **checklist de viaje** · **vos-decidís** (el eje AGENCIA vive, el
CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(entero;
un plano chico DENTRO de otra cosa sí)* · mística · racha · biografías · dinero · Wrapped · fútbol · **mucho texto** · **era
gimmick** · **`podas-vuelta`** · **observacional suelto** (pospuso 8 de un saque) — **va DENTRO de otra cosa, nunca card propia**.

## 🏆 LÍNEA DE PRODUCTO

**EL TALLER = la única aprobada, en los dos slots.** n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces**; n°2: 7/7 sin
reacción; n°3 (24/08): leído entero sin veredicto. **Gana por:** ① sustancia técnica sobre SUS plantas ② se abre con la
herramienta en la mano ③ una pantalla = una decisión ④ errores anticipados ⑤ diagramas propios. Va **agrupado dentro** de la
landing del slot, nunca en push aparte. ⚠️ Sus ticks (`taller-arbol-<code>`) **NO** escriben `task_states.json`: contar con
`generate_tasks_from_plants(PLANTS)` + `task_states.json['tasks']`, sin las 16 huérfanas. ⚠️ `pip install Pillow` antes de `build.py`.

**EL OBJETO QUE SE LLENA = apuesta ABIERTA, no refutada.** La bandeja (07/09) nunca se leyó; `tres-pilas` (12/09) tampoco se
abrió: **las dos muertes son de APERTURA, cero de contenido.** ⭐ **Veredicto definitivo el lunes 14 a las 18:00** (8 h de hueco):
**≥5 taps = probado y se serializa** · **0 taps ahí, con canal sano y sin push compitiéndole = el formato muere de verdad.**

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo define la
  TAREA.** · **La EXPOSICIÓN MEDIDA manda sobre el ledger.** · **Una reedición sin push no consume elenco** (hoy: 0 cambios).
- ⚠️ **VEDADOS HASTA EL 19/09:** B-23, B-24, B-46 (quemados de verdad: salieron en la página que SÍ abrió). **B-47 y B-37 sólo
  salieron en `tres-pilas`, que nadie abrió → por exposición medida están FRESCOS**, pero se dejan vedados porque B-46 los
  arrastra por tema y hay cantera de sobra. **HASTA EL 18/09:** B-30, B-35, B-1, F-2.
- ✅ **LIBRES PARA EL LUNES 14/09:** B-16, F-9, B-44, B-40, F-8, F-10, B-14, B-45, B-48, B-49, B-21, B-28, B-11, B-31, B-33,
  B-39, F-1, B-9, B-18, B-13, B-20, B-32 + **liberados hoy** (B-7, B-5a, B-25, B-12, B-15, B-8, B-4, B-43, B-22, B-36, F-3,
  B-41) + **el 14** (I-1, I-2, B-6, B-26, B-2, B-10, B-3, F-5, B-27, estos con exposición real CERO). **B-34 fuera de toda
  cantera: ya no existe.**
- **No antes del 21/09:** propagación/esqueje · «lo que ibas a tirar» · el ejemplar único sin repuesto · la campana de botella ·
  el corte al ras bajo el nudo · el lado este como vivero · el reparto de la ventana por día. **Del 24/09:** el diagnóstico
  sanitario sobre foto suya · la mea culpa de ficha incompleta · «la ventana de este año ya cerró». **Del 25/09:** la ventana
  partida por hora. **Del 26/09:** la corrección de mi propia corrección · la llovizna como ventaja · el abuelo y el nieto
  cítricos · el alcohol 70% entre cítricos vecinos · el conteo apostado contra la ficha · el storax del liquidámbar.
  **Del 27/09 (usados hoy):** la regla mía que se muere en 24 h · los dos errores para el mismo lado · el error para el lado
  seguro · «acá el dato lo tenés vos, no yo».

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo mantenimiento.**

- **Excepción válida y única:** una push que **él pidió por escrito** (pasó el 06/09 y el 11/09). Se anota en el ledger. · **Un
  día sin slot no es un día sin trabajo:** limita las **notificaciones**, no las **ediciones** (hoy: reedición sin push).
- **Una sola push por slot de experiencia:** original NUEVA + las **aprobadas** de ese slot agrupadas DENTRO.
  **Aprobación = recurrencia** (😍 / slot «sí» / `engageApprove`); pending no se borra, no recurre.
- ⚠️ **EL SÁBADO TIENE LAS DOS PUSH A 60 MIN Y ESO SE PAGA** (05/09 y 12/09). La cadencia es del usuario y no se toca sola, pero
  el sábado **la experiencia tiene que poder leerse SIN haber leído la tarea**, o se pierde. Si el lunes (8 h de hueco) el mismo
  formato convierte, **proponérselo a él dentro de una experiencia**, nunca cambiarlo por mi cuenta.
- **`expires_at` se ata a la ventana del contenido, no al 22:00 de rutina.**
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`, Asamblea,
  tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en TODAS las tareas; sus
  fotos y comentarios van al **thread** (`/responder-tareas`). · **28/07 PALTA:** los plantines siguen contra la pared a la
  sombra, **SIN MOVER** (B-22/B-36 es de PODA). · **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas), **no volver
  a pedir fotos generales**; sin foto: B-41, B-32, B-43, B-46/47, B-2B, B-22, B-36. · **B-34 dada de baja con consentimiento
  escrito — NUNCA borrar una especie sin eso.** · **05/09:** «No quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 LUNES 14/09 — los dos slots, hueco de 8 h.** Tarea 10:00 (13‑15°, 0‑0,2 mm, ráfagas 19‑34): **preparar el viernes 18**
  (filo + alcohol 70%) y levantar lo del sábado **sin dar por hecho que no lo hizo** (no hay señal en ninguna dirección).
  Experiencia 18:00: **el test limpio del objeto que se llena**; cantera enorme y fresca.
- **⭐ COBRAR EL SALDO.** El grande es el **viernes 18** (prometí 0,0 mm, 21‑22°, ráfagas 26‑35 como el mejor día): **se cobra el
  sábado 19 sí o sí**, y con él si el +10% al techo de ráfagas sirvió o fue otra ley de una muestra. El del lunes, el martes por
  reedición sin push.
- **Si contesta lo del viento en el fondo:** si ahí pega menos, **bajar el umbral de freno y decírselo con el número**; si pegó
  igual o peor, el +10% queda confirmado y se vuelve regla publicada.
- **Si vuelve el censo del vivero:** hay tareas reales que escribir en `data_plants.py` y el «~30+ plantines» de la ficha de
  B‑46 hay que corregirlo al número verdadero.
- **19/09: vuelven las 5** que pospuso (B-46-5, B-47-3, B-13-2, B-20, B-32). **27/09:** B-41. **15/10:** B-45. **≈05/10:** semana
  4 de la bandeja, recordarle qué mirar (prometido en su tabla).
- **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta (feb y may-sep) · la coronita F-5 en octubre · el
  fun_fact NASA de la cinta · el Persia/China del durazno · «cada limón viene de una flor única, no de racimos».
