# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🎯 LO DE HOY (vie 18/09) — día sin slot: **0 push**, 1 reedición sin aviso, y mi propia regla me salvó de mentirle

**Encolado: 0.** Viernes no tiene slot (Mar/Mié/Vie/Dom). `queue.json` quedó **vacía**. Lo que sí se hizo: **reeditar
`2026-07-24-jardin-hoy.html` en su URL estable, sin notificación**, porque decía «Jueves 17 · hoy es el día» y hoy es
viernes — **regla #6: una URL estable no puede mentir sola.**

**⭐⭐ EL HALLAZGO DEL DÍA es de método: hoy casi publico lo contrario de la verdad.** Pedía el clima con **WebFetch**
(resume la página) y hoy me transcribió **mal los arrays**: un lunes con pico a la **01:00** y máximos diarios que no
figuraban en la tira horaria. Con eso el titular iba a ser **«te devuelvo el lunes»**. Lo agarró la **regla #4**.
⭐ **`curl` SÍ sale del runner** por el proxy del agente — learnings decía lo contrario hace semanas. **Desde hoy los
tres modelos se bajan en CRUDO y se cruzan con script:** hoy **31 claims, 1 falló** («ninguno baja de 47» cuando el
piso era **45,4**) → corregido **antes** de publicar. ⚠️ **DESMENTIDO:** el máximo diario **sí** coincide con el
horario, exacto en los **21 casos** (3 modelos × 7 días). Era artefacto del lector — **no publicarlo nunca.**

**Lo que se publicó, los tres con número verificado:** ① **pagué la deuda del lunes cuatro días antes** — la había
prometido para el domingo, pero el número se movió (53‑58 → 60‑78) y la regla dice que **si el número se mueve, se
adelanta el aviso**. **Veredicto: NO se lo puedo devolver.** El pico del lunes está **adentro de la jornada en los
tres** (ECMWF 63,0 a las 14‑15 · GFS 77,8 a las 15 · mixto 58,7 a las 11) y el máximo de los tres **no baja de 50,8 en
ninguna hora de 09 a 18**. ② **Le devolví el sábado 19**: ayer se lo saqué por 0‑0,6 mm, hoy volvió a **0,00 mm en los
tres**. ③ La columna de ráfagas de la tabla pasó a ser el **máximo 09‑18 en los 7 días**, cumpliendo la regla #7 de
ayer — **y se publicó que en el lunes da casi lo mismo que el viejo (59‑78 vs 60‑78)**: la prueba de que la regla
nueva no es un truco para darle siempre números chicos.

**La apuesta se juega HOY y llega al último día ganando por 0,5 km/h**, con un número de las **23:00** (GFS 42,5 vs
techo 43). Recorrido: lun −0,7 · mar +0,9 · mié +7,0 · jue +1,6 · **vie +0,5**. Máxima 18‑24°: 22,9 · 22,9 · **16,6** =
**2 de 3**. Lluvia 0,00 ×3, quinto día. ⭐ Quedó escrito antes del resultado: **gane o pierda, el +10 % sobre el máximo
diario está jubilado** — «no hay resultado en el que esta apuesta me deje bien».

## 📊 CONCLUSIONES DE LAS PUSH — 15 días de sequía; el canal está sano y el diagnóstico ya no es el formato

**Últimas 8 push (10/09 → 17/09): 1 click, 0 taps, 0 reacciones, 0 feedback, 0 aprobaciones.** 10/09 ⬛ · 11/09 ⬛ (fuera
de cadencia, a pedido escrito) · 12/09 jardin‑hoy ✅ **click a +25 min, el único evento en 15 días** · 12/09 tres‑pilas
⬛ (a 60 min) · 14/09 jardin‑hoy ⬛ · 14/09 el‑marcador ☠️ (8 h de hueco y murió igual) · **17/09 jardin‑hoy ⬛ a ~20 h**.

- ⭐ **Canal probado sano**: `sent_at − send_at` = **+2,8 s** ayer, sexto envío consecutivo puntual. **Cuando algo mide
  0 no hay dónde esconderse: es contenido, gancho o slot.** · ⭐ **El hueco entre pushes NO es el problema** (mismo
  minuto → 0 · 60 min → 0 · 8 h → 0). · ⭐ **El canal tarea vive por el TÍTULO:** el único click fue a `jardin-hoy`, a
  +25 min, y no tocó nada. **Gancho vivo, cuerpo muerto.**
- 🚨 **4 formatos nuevos en 11 días, 1 solo click.** Lo único que convirtió (05/09: 40 min, 13 `answer`, **10 tareas
  resueltas de noche** en `puesta-al-dia`) fue **su lista real con foto y un botón por ítem**. **El sábado 19 vuelve a
  ESO, ya prometido por escrito en la página.** Dejo de inventar formatos.
- ⚠️ **Cruce de control hecho hoy, sin subconteo posible:** `task_states` sin moverse desde el **06/09 11:39Z** ·
  `uploads` 0 pendientes, última foto **08/09** · threads **0 pending** · `user_tasks` 0 sin contestar · último evento
  de `engagement.json` **12/09 13:25Z (≈140 h)**.

## 💬 FEEDBACK DE TEXTO — los 3 vivos, ya ejecutados (ninguno nuevo desde el 05/09)

1. *«Nose cuál es el crespón y la althea»* (03/09) → **al nombrar una especie, foto + dónde está, siempre.**
2. *«Sacá todas las tareas ya completadas para achicar la página»* (05/09) → hecho. **«Ocultar» no es «sacar».**
3. *«Volvémela a enviar cuando revises con mi feedback en mente»* (05/09) → hecho. **Pide re‑envío, no novedad.**

**Preguntas abiertas: sigue UNA** — el viento en el fondo, contra el muro de la cancha de pádel. ⭐ **Hoy se le puso
PRECIO con fecha**, que es lo que le faltaba: «el lunes te lo estoy frenando entero por 59‑78 km/h; si me decís que
contra ese muro pega la mitad, **el lunes deja de ser un día perdido** y te armo la jornada con las tareas bajas del
fondo». Hoy comprobé que **a la HORA le acierto** (31 claims cruzados); **el LUGAR es lo único que no puedo saber solo.**
⚠️ **El sábado se pregunta con un BOTÓN, no con texto.**

## ⚙️ ESTADO OPERATIVO (18/09/2026)

`pix9` **active** · `uploads.json` 0 pendientes · threads 0 `pending` · `user_tasks.json` 0 sin contestar ·
`task_states.json` 81 entries — **66 done / 11 snoozed / 4 active**, sin moverse desde el 06/09 · proposals **94**
(56 dropped / 23 promoted / 13 pending / 1 approved / 1 removed), **sin cambios de estado hoy: no hubo un solo evento
de decisión**. ✅ **COMPACTACIÓN EJECUTADA HOY** (vencía hoy, no ayer): `engagement.json` **57 → 44** eventos y
`send_log.json` **19 → 17**, los del 03‑04/09 resumidos en `daily_summary`; `queue.json` **1 → 0** entries.
⚠️ **El 19/09 vuelven las 5 pospuestas** (B‑46‑5, B‑47‑3, B‑13‑2, B‑20, B‑32) + B‑24 y B‑23 ya vencidas el 12/09.

## 🚨 LAS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick:** ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
**#2 EL CONTROL VA ARRIBA:** ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). `pos.js` cada sesión — playwright en `/opt/node22/lib/node_modules`,
chromium en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`; descartar `[hidden]`, rects cero y la quickbar.
Hoy: **27,9 %**, sin overflow‑x, altura 11085.
**#3 EL LARGO TAMBIÉN ES LAYOUT:** tope operativo **~12 ítems**. Hoy: 3 tarjetas.
**#4 ⭐ REFORZADA HOY — NINGÚN NÚMERO EN PROSA SIN CRUZARLO CON MI PROPIA TABLA, con código y sobre el CRUDO.**
Hoy me salvó de publicar lo contrario de la verdad. **`curl` SÍ sale del runner** (`--cacert /root/.ccr/ca-bundle.crt`;
si da `SSL_ERROR_SYSCALL`, reintentar: sale a la 2ª). **WebFetch resume y DEFORMA arrays largos: no usarlo más para
tablas numéricas.**
**#5 AL ARBITRAR MODELOS, NOMBRAR AL MINORITARIO** — y si después gana, publicarlo con su nombre.
**#6 UNA URL ESTABLE NO HABLA EN «MAÑANA»:** si dice «hoy jueves», al día siguiente miente sola. **Un día sin slot
limita las NOTIFICACIONES, no las EDICIONES:** la página se reedita igual.
**#7 EL MÁXIMO DIARIO NO ES EL VIENTO DE TRABAJO:** freno y habilito con el **máximo de 09 a 18**. ⭐ **Validada hoy en
su contra y publicado así:** en el lunes 21 los dos números dan casi lo mismo (59‑78 vs 60‑78) porque el pico cae a las
15:00. **Una regla que nunca te quita nada es una excusa, no una regla.** El desglose horario es confiable a 1‑2 días;
a 3‑4 vale la **forma** (dónde cae el pico), no el número fino — y hay que decirlo.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA ENTERA el día que vence**, y **si el número se mueve antes, se adelanta el aviso**
  (hoy: la deuda del lunes se pagó 4 días antes). **Si lo que se cae es una REGLA, un TITULAR o un AVISO mío, se
  publica lo caído, con nombre y sin maquillar.**
- **⭐ DEVALUAR MI PREMIO ANTES DE COBRARLO** es más fuerte que ganar. · **⭐ UNA CORRECCIÓN QUE LE DEVUELVE ALGO** (hoy:
  el sábado) vale más que una que sólo confiesa. · **⭐ NUEVO — PUBLICAR EL CASO EN QUE MI REGLA NUEVA NO ME CONVIENE**
  demuestra que no la escribí para quedar bien.
- **⭐ NUEVO — A UNA PREGUNTA ABIERTA HAY QUE PONERLE PRECIO Y FECHA.** «¿Cómo pega el viento en el fondo?» estuvo
  muerta 2 días; convertida en «una línea tuya te devuelve el lunes 21» tiene algo que ganar hoy.
- **⭐ CAMBIARLE EL MOTIVO SIN CAMBIARLE EL DÍA** — 4 de 4 veces el motivo nuevo salió más fuerte. · **⭐ FRENAR POR
  SEGURIDAD construye credibilidad**, pero sólo si el número del freno es el correcto (ver #7).
- **Cortas, probadas:** la madrugada siguiente al corte · una apuesta no se retoca el día que se juega · decir el
  límite de lo que veo · pedirle el dato que sólo él tiene · la condición convertida en fecha · el clima que habilita,
  no sólo el que prohíbe · foto + dónde está al nombrar una especie · **el título es el activo más medido** · **timing
  verificado > urgencia inventada** · **feedback_text = ley** · ⚠️ **`engagement.json` SUBCUENTA hasta 2,5 días.**
- ⚠️ **Clima, receta vigente:** `curl` crudo, **un modelo por llamada** (`ecmwf_ifs025`, `gfs_seamless`, `best_match`),
  `daily=precipitation_sum,wind_gusts_10m_max,temperature_2m_max,temperature_2m_min` + `hourly=wind_gusts_10m,
  temperature_2m` + `forecast_days=7`. **Madrugada = hourly 04‑08**, nunca la mínima diaria. **Ráfaga operativa =
  máximo horario 09‑18.** ⚠️ `pip install Pillow` antes de `build.py`.

## 🚫 EJES MUERTOS (no volver, ni variaciones) + 🏆 LÍNEA DE PRODUCTO

**Muertos:** **el objeto que se llena** *(archivado 17/09, 3 muertes)* · noticiero/«El Parte» · cero-lectura/duelos
binarios · checklist de viaje · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) · mi-objetivo · role-play
verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(un plano chico DENTRO de otra cosa sí)* ·
mística · racha · biografías · dinero · Wrapped · fútbol · **mucho texto** · era gimmick · `podas-vuelta` ·
**observacional suelto** (va DENTRO de otra cosa, nunca card).

**EL TALLER = la única aprobada, en los dos slots.** n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces**. Gana por
① sustancia técnica sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ errores
anticipados. Va **agrupado dentro** de la landing del slot. ⚠️ Sus ticks **NO** escriben `task_states.json`.

## 🚫 ANTI-REPETICIÓN

⭐ **El registro con fechas vive en `facts_ledger.json` → `_nota_vigente`.** **Se lee ANTES de armar contenido y se
actualiza DESPUÉS.**

- Planta featured descansa **≥7 días**; un fact no se repite en **<14 días**; cada experiencia nueva usa **≥70 % de
  elenco no featured en 7 días**. **El canal tarea es monotemático: su cast lo define la TAREA.**
- ⭐ **Una reedición sin push NO consume elenco** (hoy se repitieron las 3 tarjetas de ayer y su veda sigue venciendo el
  24/09). · **La EXPOSICIÓN MEDIDA manda sobre el ledger.** · ⭐ **La lista real de tareas NO consume cantera;** lo que
  sí debe ser fresco es el dato de color que le agregue.
- ⚠️ **B‑34 fuera de toda cantera: ya no existe** (baja con consentimiento escrito del 04/09). **NUNCA borrar una
  especie sin consentimiento explícito del usuario.**
- **Liberados hoy 18/09:** B‑30, B‑35, F‑2. **Liberan 19/09:** B‑24, B‑46, B‑47, B‑37 · **21/09:** los 10 del marcador ·
  **24/09:** B‑1, B‑29, B‑22, B‑36, B‑23, B‑43. **Cantera libre para el sábado 19: 37 especies.**

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo
mantenimiento.** Excepción única: una push que **él pidió por escrito**. La cadencia es del usuario: si hay que
cambiarla, se le propone **dentro de una experiencia**.

- ⚠️ **El sábado tiene las dos push a 60 min y eso se paga** (05/09, 12/09) — **pero el 14/09 con 8 h de hueco también
  dio 0: el hueco NO es el problema.** · ⚠️ **El 11/09 salió una `jardin-hoy` fuera de cadencia: no repetir.** · ⚠️ **El
  lunes 18:00 cae a 35 min del atardecer** → si la experiencia pide salir a mirar, **se guarda sola y no vence**.
- ⭐ **`expires_at` se ata a la ventana del contenido, no al 22:00 de rutina.** · **Canal tarea:** URLs estables que se
  **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`). NO correr `gen_task_reminders.py` ni
  `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

**NO BORRAR ni pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`,
Asamblea, tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en TODAS
las tareas; sus fotos van al **thread**. · **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN
MOVER** (B‑22/B‑36 es de PODA). · **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas), **no volver a
pedir fotos generales**. · **05/09:** «No quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 SÁBADO 19 — DOS SLOTS, y los dos ya están prometidos por escrito en la página:** ① **10:00, jardin‑hoy:** arranca
  con el **cobro de la apuesta MEDIDO** (`past_days=1` + `best_match` sobre el viernes cerrado: 0,0 mm · ráfaga **< 43**
  · máxima **18‑24°**) y **jubilar el +10 % sobre el máximo diario gane o pierda**. El sábado es día limpio (0,00 mm ×3,
  09‑18 hasta 29,5): es el **último** antes de 4 días cerrados. ② **11:00, experiencia:** **su lista real de tareas con
  foto y un botón por ítem**, estilo `puesta-al-dia`, **NO un formato nuevo**.
- **🎯 Munición verificada para el finde:** dom 20 agua (**2,1‑5,6 mm**) · lun 21 **59‑78 km/h de 09 a 18**, pico
  15:00 · mar 22 la máxima cae a **11,3‑11,8°** (hoy 22,9: **11 grados en 4 días**) · mié 23 el ECMWF pone **4,5° a las
  05‑06**, uno contra dos (GFS 7,4 · mixto 7,3) — **no venderlo como pronóstico** · jue 24 reabre (0,00 mm ×3).
- **Si contesta lo del viento en el fondo:** bajar el umbral y **rearmar el lunes 21 con las tareas bajas**, con número.
- **27/09:** B‑41. **15/10:** B‑45. **≈05/10:** semana 4 de la bandeja (prometido en su tabla). · **Cantera SIN USAR:**
  condiciones sin fecha del catálogo · poda×fruta · la coronita F‑5 en octubre · el NASA de la cinta · el Persia/China
  del durazno · «cada limón viene de una flor única».
