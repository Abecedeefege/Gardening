# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🎯 LO DE HOY (jue 17/09) — 1 push de tarea, y el error más caro de la semana es mío

**Encolado: 1** — `2026-09-17-jardin-hoy`, **10:00 -03:00**, `expires_at` **16:00** (el consejo del día es «hoy de 14
a 18»; una push que llega a las 19 miente). Jueves no tiene slot de experiencia.

**⭐ EL HALLAZGO: pedí por PRIMERA VEZ el pronóstico HORA POR HORA y se me cayó el aviso que más repetí.** Venía
frenando con el **máximo diario** de ráfagas: dos días seguidos le dije que el GFS le ponía **40 km/h** al jueves y
que los limones son escalera. Hora por hora, **ese 40,0 es el valor de las 03:00**; de **09 a 18 el más alto de los
tres es 25,6 km/h** y de las 15 en adelante 23,0 · 19,1 · 14,4. **Le vendí riesgo con el pico de un día que ocurre
mientras duerme.** → **REGLA #7.**

**Las otras dos, también contra mí:** ① el titular de ayer («siete días limpios hasta el martes 22») **duró 24 h** —
volvió la lluvia (sáb **0‑0,6** · dom **0,3‑4,1** · lun **0,2‑4,9**) y el 4,9 lo pone el **ECMWF**, el mismo que la
había borrado (**9,6 → 0,1 → 4,9 en tres días**): **la ventana pasó de 7 días a 2**; ② **el escape que le di ayer se
cayó** — viernes y sábado subieron a **41,4 y 40,7** en el GFS, sobre el jueves (40,0): **hoy es el más calmo de los
cuatro, por 0,7 km/h.** **Además:** madrugada real 04‑08 en **las siete filas** (ayer sólo tres) · **tira horaria** de
hoy · **retiré una pregunta abierta** (la escarcha) · B‑43 al final, su día era ayer · arreglé un bug de CSS
(`.veredicto b` hacía `display:block` a los `<b>` anidados y partía la bajada).

**Apuesta del viernes, 4º día sin tocarla, último marcador antes del cobro:** ✅ lluvia 0,00 ×3 · ✅ ráfagas **41,4 vs
techo 43 → gano por 1,6** (lun −0,7 · mar +0,9 · mié +7,0 · **jue +1,6**) · 🟡 máxima 18‑24°: ECMWF 22,5 y GFS 22,0
adentro, mixto 16,2 afuera → **2 de 3**. ⭐ **Dejé escrito ANTES del resultado que si gano, gano mal:** ese 41,4 es a
las **23:00**. **Gane o pierda, el +10 % sobre el máximo diario queda jubilado**; lo reemplaza el +10 % sobre 09‑18.

## ☠️ EL MARCADOR — veredicto leído UNA vez y ejecutado, como estaba pactado

**0 taps a las 60 h.** `engagement.json` clavado en el **12/09 13:25Z (116 h sin un evento)** y el cruce de control
descarta subconteo (`task_states` desde el 06/09 · `uploads` 0 pendientes desde el 08/09 · threads y `user_tasks` en
0). Canal **sano** (201 a +3,6 s) y **sin push compitiendo** (8 h de hueco) → se cumple exacto la condición
predeclarada de muerte → **`dropped`**. ⭐ **EL EJE «OBJETO QUE SE LLENA» QUEDA ARCHIVADO** en cualquier variante:
bandeja (07/09), `tres-pilas` (12/09), `el-marcador` (14/09) — **tres muertes, las tres por APERTURA.**
**No borré el HTML a propósito** (único registro de las 10 apuestas; `dropped` ya evita el re-envío). **La deuda
asociada no se puede cobrar sin su arbitraje:** queda muerta con el formato, y así se lo publiqué hoy.

## 📊 CONCLUSIONES DE LAS PUSH — 14 días de sequía, y el diagnóstico ya no es el formato

**Últimas 7 push (10/09 → 17/09): 1 click, 0 taps, 0 reacciones, 0 feedback, 0 aprobaciones.** 10/09 ⬛ · 11/09 ⬛
(fuera de cadencia) · 12/09 jardin‑hoy ✅ **click a +25 min, el único evento en 14 días** · 12/09 tres‑pilas ⬛ (a 60
min) · 14/09 jardin‑hoy ⬛ · 14/09 el‑marcador ☠️ (8 h de hueco y murió igual) · 17/09 ⏳.

- ⭐ **El canal está probado sano** (`sent_at − send_at` = +3,6 s en los cinco últimos envíos): **cuando algo mide 0 no
  hay dónde esconderse — es contenido, gancho o slot.** · ⭐ **El hueco entre pushes NO era el problema** (mismo
  minuto → 0 · 60 min → 0 · 8 h → 0). · ⭐ **El canal tarea vive por el TÍTULO:** el único click fue a `jardin-hoy`, a
  +25 min, y no tocó nada. **Gancho vivo, cuerpo muerto.**
- 🚨 **4 formatos nuevos en 11 días, 1 solo click: el problema dejó de ser el formato — le mando experimentos en vez
  de su lista real de tareas.** Lo único que convirtió (05/09: 40 min, 13 `answer`, **10 tareas resueltas de noche**
  en `puesta-al-dia`) fue **su lista real con foto y un botón por ítem**. **El sábado 19 vuelve a ESO**, ya prometido.

## 💬 FEEDBACK DE TEXTO — los 3 vivos, ya ejecutados (ninguno nuevo desde el 05/09)

1. *«Nose cuál es el crespón y la althea»* (03/09) → **al nombrar una especie, foto + dónde está, siempre.**
2. *«Sacá todas las tareas ya completadas para achicar la página»* (05/09) → hecho. **«Ocultar» no es «sacar».**
3. *«Volvémela a enviar cuando revises con mi feedback en mente»* (05/09) → hecho. **Pide re‑envío, no novedad.**

**Preguntas abiertas: quedó UNA** (bajé de tres a una hoy): el viento en el fondo contra el muro de la cancha de
pádel. ⭐ **Hoy vale el doble: ya comprobé que le erraba a la HORA; si además le erro al LUGAR, el freno por viento es
casi todo ruido.** **Retiradas:** la escarcha (17/09) · los limones «más de veinte» viaja pegada al botón «hecha» de
B‑23, no suelta. ⚠️ **El sábado se pregunta con un BOTÓN, no con texto.**

## ⚙️ ESTADO OPERATIVO (17/09/2026)

`pix9` **active** · `uploads.json` 0 pendientes (última foto 08/09) · threads 0 `pending` · `user_tasks.json` 0 sin
contestar · `task_states.json` 81 entries — **66 done / 11 snoozed / 4 active**, sin moverse desde el 06/09 · último
evento **12/09 13:25Z (116 h)** · proposals **94** (56 dropped / 23 promoted / 13 pending / 1 approved / 1 removed).
**Compactación: NADA vencido hoy.** El corte de 14 días cae el **03/09** y los eventos más viejos son del 03/09
15:10Z y 14:29Z: 13 d 16 h, no 14. ⚠️ **Ayer anoté que vencía hoy; estaba corrido un día: vence el 18/09.**

## 🚨 LAS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick:** ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
**#2 EL CONTROL VA ARRIBA:** ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). `pos.js` se reescribe cada sesión — playwright en
`/opt/node22/lib/node_modules`, chromium en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`; descartar
`[hidden]`, rects de área cero y la quickbar de `engage.js`. Hoy: **26,4 %**, sin overflow, altura 9964.
**#3 EL LARGO TAMBIÉN ES LAYOUT:** tope operativo **~12 ítems**. Hoy: 3 tarjetas.
**#4 NINGÚN NÚMERO EN PROSA SIN CRUZARLO CON MI PROPIA TABLA** — con código, no de memoria (hoy: `check.py`, 20
claims cruzados contra los arrays crudos antes de commitear).
**#5 AL ARBITRAR MODELOS, NOMBRAR AL MINORITARIO** — y si después gana, publicarlo con su nombre.
**#6 UNA URL ESTABLE NO HABLA EN «MAÑANA»:** si dice «mañana miércoles», al día siguiente miente sola.
**#7 ⭐ NUEVO — EL MÁXIMO DIARIO NO ES EL VIENTO DE TRABAJO:** es el peor instante de 24 h y puede caer a las 3 AM.
**Freno y habilito con el máximo de 09 a 18**; si la tarea es de ALTURA lo miro hora por hora **antes** de escribir
«riesgo». El desglose horario sólo es confiable a 1‑2 días: más allá, decirlo.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA ENTERA el día que vence**, y si el número se mueve antes, se adelanta el aviso. **Si lo
  que se cae es una REGLA, un TITULAR o un AVISO mío, se publica lo caído, con nombre y sin maquillar.**
- **⭐ NUEVO — DEVALUAR MI PROPIO PREMIO ANTES DE COBRARLO** («si gano, gano con una regla que ya jubilé») es más
  fuerte que ganar. · **⭐ NUEVO — RETIRAR UNA PREGUNTA ES CONTENIDO:** bajar de tres abiertas a una, diciendo por qué,
  hace pesar la que queda. · **⭐ NUEVO — UNA CORRECCIÓN QUE LE DEVUELVE ALGO** (hoy: la tarde libre de riesgo) vale
  más que una que sólo confiesa: buscar el ángulo donde mi error le SUMA un día, una hora o una tarea.
- **⭐ CAMBIARLE EL MOTIVO SIN CAMBIARLE EL DÍA** — 4 de 4 veces el motivo nuevo salió más fuerte. · **⭐ FRENAR POR
  SEGURIDAD construye credibilidad**, pero sólo si el número del freno es el correcto (ver #7).
- **Cortas, probadas:** la madrugada siguiente al corte, no la del día que podás · una apuesta no se retoca el día
  antes de cobrarla · decir el límite de lo que veo · pedirle el dato que sólo él tiene · la condición convertida en
  fecha · el clima que habilita, no sólo el que prohíbe · al nombrar una especie, foto + dónde está · abrir rápido y
  no hacer nada ≠ no abrir · **el título es el activo más medido** · **timing verificado > urgencia inventada** ·
  **feedback_text = ley.** · ⚠️ **`engagement.json` SUBCUENTA hasta 2,5 días: cruzar con `task_states` + `uploads` +
  threads.**
- ⚠️ **Clima:** `curl` a open-meteo NO sale del runner → **WebFetch, un modelo por llamada.** Diario:
  `forecast_days=7` + `daily=precipitation_sum,wind_gusts_10m_max,temperature_2m_max,temperature_2m_min` +
  `hourly=temperature_2m`. **Viento horario: `forecast_days=2` + `hourly=wind_gusts_10m`** (nuevo hoy, obligatorio si
  hay tarea de altura). La madrugada es el `hourly` de **04‑08**. ⚠️ `pip install Pillow` antes de `build.py`.

## 🚫 EJES MUERTOS (no volver, ni variaciones) + 🏆 LÍNEA DE PRODUCTO

**Muertos:** **el objeto que se llena** *(archivado el 17/09 tras 3 muertes)* · noticiero/«El Parte» · cero-lectura/
duelos binarios · checklist de viaje · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) · mi-objetivo ·
role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(un plano chico DENTRO de otra cosa
sí)* · mística · racha · biografías · dinero · Wrapped · fútbol · **mucho texto** · era gimmick · `podas-vuelta` ·
**observacional suelto** (va DENTRO de otra cosa, nunca card).

**EL TALLER = la única aprobada, en los dos slots.** n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces**. Gana por
① sustancia técnica sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ errores
anticipados. Va **agrupado dentro** de la landing del slot, nunca en push aparte. ⚠️ Sus ticks **NO** escriben
`task_states.json`.

## 🚫 ANTI-REPETICIÓN

⭐ **El registro con fechas vive en `facts_ledger.json` → `_nota_vigente`** (vedados, cantera libre, ángulos quemados
con su fecha de liberación). **Se lee ANTES de armar contenido y se actualiza DESPUÉS.**

- Planta featured descansa **≥7 días**; un fact no se repite en **<14 días**; cada experiencia nueva usa **≥70 % de
  elenco no featured en 7 días**. **El canal tarea es monotemático: su cast lo define la TAREA**, con excepción propia
  (hoy se usó la de jue 17: B‑1/B‑29/B‑22/B‑36 + B‑23/B‑43; queda la de vie 18: B‑23/B‑24).
- ⭐ **Una reedición sin push NO consume elenco.** · **La EXPOSICIÓN MEDIDA manda sobre el ledger:** una página que
  nunca se abrió no quemó su cast. · ⭐ **NUEVO — la lista real de tareas NO consume cantera:** una tarea pendiente
  suya no es un fun_fact que yo elijo; lo que sí debe ser fresco es el dato de color que le agregue.
- ⚠️ **B‑34 fuera de toda cantera: ya no existe** (baja con consentimiento escrito del 04/09). **NUNCA borrar una
  especie sin consentimiento explícito del usuario.**
- **Liberaciones:** 18/09 → B‑30, B‑35, F‑2 · 19/09 → B‑24, B‑46, B‑47, B‑37 · 21/09 → los 10 del marcador · 24/09 →
  los 6 del canal tarea de hoy. **Cantera libre para el sábado 19: 34 especies.**

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo
mantenimiento.** Excepción única: una push que **él pidió por escrito**. **Un día sin slot limita las NOTIFICACIONES,
no las EDICIONES.** La cadencia es del usuario: si hay que cambiarla, se le propone **dentro de una experiencia**.

- ⚠️ **El sábado tiene las dos push a 60 min y eso se paga** (05/09, 12/09) — **pero el 14/09 con 8 h de hueco también
  dio 0: el hueco NO es el problema.** · ⚠️ **El 11/09 salió una `jardin-hoy` fuera de cadencia: no repetir.**
- ⚠️ **El lunes 18:00 cae a 35 min del atardecer en septiembre** → toda experiencia de ese slot que pida salir a mirar
  **se guarda sola y dice que no vence**.
- ⭐ **`expires_at` se ata a la ventana del contenido, no al 22:00 de rutina** (hoy: 16:00, porque el consejo era «de
  14 a 18»). · **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`,
  `puesta-al-dia.html`). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

**NO BORRAR ni pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`,
Asamblea, tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en TODAS
las tareas; sus fotos van al **thread**. · **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN
MOVER** (B‑22/B‑36 es de PODA). · **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas), **no volver a
pedir fotos generales**. · **05/09:** «No quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 SÁBADO 19, prometido por escrito en la página:** ① la original nueva es **su lista real de tareas con foto y un
  botón por ítem** (estilo `puesta-al-dia`), NO un formato nuevo; ② **cobrar la apuesta del viernes 18** (0,0 mm ·
  ráfaga **< 43** · máxima **18‑24°**) con el día cerrado, `past_days` + `best_match`, y **jubilar la regla del +10 %
  sobre el máximo diario gane o pierda**; ③ la push de tarea de las 10:00 arranca con ese resultado.
- **🎯 DOMINGO 20 — deuda anunciada:** mirar el **lunes 21 hora por hora**. Si el 52,6‑58,0 también es nocturno,
  **le devuelvo el lunes** y lo digo. · **🎯 18/09 — compactar** `engagement.json` y `send_log.json`.
- **Si contesta lo del viento en el fondo:** bajar el umbral de freno esta semana y publicarlo con el número.
- **19/09: vuelven las 5** que pospuso (B‑46‑5, B‑47‑3, B‑13‑2, B‑20, B‑32). **27/09:** B‑41. **15/10:** B‑45.
  **≈05/10:** semana 4 de la bandeja (prometido en su tabla). · **Cantera SIN USAR:** condiciones sin fecha del
  catálogo · poda×fruta · la coronita F‑5 en octubre · el NASA de la cinta · el Persia/China del durazno · «cada
  limón viene de una flor única».
