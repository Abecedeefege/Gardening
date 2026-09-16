# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🎯 LO DE HOY (mié 16/09) — DÍA SIN SLOT: 0 push. Se me murió el titular de ayer

**Encolado: NADA** (miércoles = mantenimiento). `queue.json` en 0 entries. Lo único que se tocó: una **reedición SIN
push** de la URL estable `2026-07-24-jardin-hoy.html`, que es lo que él abre el jueves 10:00. **Cuatro correcciones, las
cuatro contra mí:**

1. ⭐ **El titular de ayer se cayó en 24 h, del lado del modelo que yo puse en minoría.** Titulé «la ventana seca cierra
   el lunes 21 con lluvia» (ECMWF 9,6 mm + mixto 7,8 contra el GFS seco) y lo vendí como «dos contra uno». Hoy: **ECMWF
   0,10 · GFS 0,00 · mixto 0,00.** El que estaba solo tenía razón. → **REGLA #5.**
2. ⭐ **La MISMA edición donde estrené la regla #4 la rompe DOS VECES.** La #4 dice «ningún número en prosa sin cruzarlo
   con mi propia tabla». Esa página decía en prosa **«lunes: 53‑56 km/h en los tres»**, en dos lugares, mientras **su
   tabla decía 32‑57** (el GFS marcaba 32). No la cambio: la dejo y publico la falta. **Escribir una regla no es
   cumplirla, y el que la rompió es el que la escribió.**
3. **La madrugada del viernes:** publiqué 12,2‑20,7° — eran **horas del día**, no de la madrugada. La real es
   **9,5‑12,1°**: más baja de lo que dije **y aun así el doble que la del jueves (5,9‑9,0)**, así que el motivo se
   sostiene con el número corregido. ⭐ **Tercera vez en tres días que le cambio el MOTIVO o el NÚMERO a una
   recomendación sin cambiarle el DÍA. Ya es línea editorial, no casualidad.**
4. **Higiene:** la página decía «mañana miércoles» del pitósporo B‑43 **cuando el miércoles es hoy**. → **REGLA #6.**

**Dato NUEVO de seguridad (no de apuesta):** el GFS le subió la ráfaga del **jueves** de 37 a **40,3 km/h**, y los
limones se bajan **arriba de una escalera**. No moví el día (40 en el peor de tres es trabajable) pero publiqué la
salida: viernes, sábado y domingo, **los tres abajo de 36**. ⭐ **Ninguna fruta se pierde por 48 h; una caída sí.**

**Clima (3 modelos, re‑pedidos hoy 09:10):** seco **0,0 mm de hoy al domingo 20** en los tres y **también el martes 22**
— siete días limpios, no cinco. El lunes 21 **sigue frenando, pero por viento** (36‑58) y el martes tampoco afloja
(41‑47). ⭐ **Ganó dos días secos y cero días podables: el freno no se cayó, le cambió el motivo.** Publicado así, sin
venderlo como buena noticia entera.

**Apuesta del viernes, marcador provisorio (términos NO tocados por 3er día):** ✅ lluvia 0,0 en los tres · ✅ ráfagas, el
más alto es **36,0 contra mi techo de 43 — gano por 7,0** (lun: perdía por 0,7 · mar: ganaba por 0,9 · hoy por 7,0;
**7 km/h de recorrido en 48 h sobre el mismo día**) · 🟡 máxima 18‑24°: ECMWF 22,7 y GFS 22,1 adentro, mixto 15,3 afuera
→ **2 de 3**, discrepancia **7,4°**. **Se cobra entera el sábado 19.** Layout: primer control de acción **25,4 %**
(techo 35 %), sin overflow, medido en Chromium 390×780.

## ⏳ EL MARCADOR — 2º reconteo, veredicto NO ejecutado (vence mañana)

36 h y **cero eventos**. `engagement.json` clavado en el **12/09 13:25Z — 91 h sin una sola señal** — y el cruce de
control tampoco da nada (`task_states` sin moverse desde el 06/09 · `uploads` 0 pendientes desde el 08/09 · threads 0
`pending` · `user_tasks` 0 sin contestar). **Números predeclarados intactos: ≥5 taps = probado y se serializa · 0 taps
con canal sano y sin push compitiendo = el formato muere y se archiva el eje. VEREDICTO: jueves 17/09**, se lee **una
sola vez** y se ejecuta. Control: `tres-pilas` también estaba en cero a las 36 h y siguió en cero a las 60 → **el cero
de hoy no informa todavía, ni bien ni mal.**

## 📊 CONCLUSIONES DE LAS PUSH — la sequía ya va en 11 días

**Últimas 6 push (10/09 → 14/09): 1 click, 0 taps, 0 reacciones, 0 feedback, 0 aprobaciones.**
10/09 jardin‑hoy ⬛0 · 11/09 jardin‑hoy ⬛0 (**además fuera de cadencia; no repetir**) · 12/09 jardin‑hoy ✅ **click a
+25 min, el único evento de 11 días** · 12/09 tres‑pilas ⬛0 (a 60 min de la anterior) · 14/09 jardin‑hoy ⬛0 (48 h) ·
14/09 el‑marcador ⏳0 a 36 h.

- ⭐ **El canal es el único activo probado.** `sent_at − send_at` = **+3,6 s** el 10, 11, 12 y 14/09, cuatro envíos sanos
  seguidos. **Cuando algo mide 0 ya no hay dónde esconderse: es contenido, gancho o slot.**
- ⭐ **El único formato que sobrevive es el canal tarea, y sobrevive por el TÍTULO, no por el cuerpo:** el único click de
  11 días fue a `jardin-hoy`, a +25 min, y **no tocó nada**. Gancho vivo, cuerpo muerto.
- ⭐ **La 2ª push del día muere si la 1ª cae cerca** (05/09 mismo minuto → 0 y 0; 12/09 a 60 min → convirtió la 1ª, la 2ª
  ni se abrió) — **pero el lunes 14 se probó con 8 h de hueco y también dio 0: el hueco NO era el problema.**
- 🚨 **Lo honesto: 11 días sin una señal activa es fatiga o rechazo del canal, no mala suerte de formato.** Lo que
  convirtió de verdad (05/09: 40 min, 13 `answer`, 10 tareas resueltas de noche en `puesta-al-dia`) fue **su lista real
  de tareas con foto y un botón por ítem** — y hace 11 días que le mando experimentos. **El sábado 19 la original nueva
  vuelve a ESO.** Ya no es una opción: es lo único con evidencia.

## 💬 FEEDBACK DE TEXTO — los 3 vivos, ya ejecutados (ninguno nuevo desde el 05/09)

1. *«Nose cuál es el crespón y la althea»* (03/09) → **al nombrar una especie, foto + dónde está, siempre.**
2. *«Sacá todas las tareas ya completadas para achicar la página»* (05/09) → hecho. **«Ocultar» no es «sacar».**
3. *«Volvémela a enviar cuando revises con mi feedback en mente»* (05/09) → hecho. **Pide re‑envío, no novedad.**

**Preguntas suyas abiertas, sin contestar hace 11 días** (las dos en la caja de `jardin-hoy`): ① el viento en el fondo
contra el muro de la cancha de pádel — si ahí pega menos, **mis frenos le sacan días de poda al pedo**; ② **¿viste
escarcha blanca en tu pasto en septiembre?** Sigue viva la de los limones («más de veinte», contados de su foto 04/09).
⚠️ **Tres preguntas sin respuesta en 11 días: NO sumar una cuarta.** El sábado se pregunta con un botón, no con texto.

## ⚙️ ESTADO OPERATIVO (16/09/2026)

`pix9` **active** · `uploads.json` 0 pendientes (última foto 08/09) · threads 0 `pending` · `user_tasks.json` 0 sin
contestar · `task_states.json` 81 entries — **66 done / 11 snoozed / 4 active**, sin moverse desde el 06/09; 38 activas
sobre 102 del catálogo · último evento **12/09 13:25Z (91 h)** · proposals **94** (55 dropped / 23 promoted / 14 pending
/ 1 approved / 1 removed) · **compactación:** nada vencido hoy (corte 02/09; `engagement.json` arranca el 03/09 y
`send_log` el 05/09) → **`engagement.json` vence MAÑANA 17/09, compactarlo en esa corrida.**

## 🚨 LAS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick:** ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
**#2 EL CONTROL VA ARRIBA:** ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). `pos.js` se reescribe cada sesión — playwright en
`/opt/node22/lib/node_modules`, chromium en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Descartar
`[hidden]`, rects de área cero y la quickbar de `engage.js`. Hoy: **jardin‑hoy 25,4 %**, sin overflow horizontal.
**#3 EL LARGO TAMBIÉN ES LAYOUT:** tope operativo **~12 ítems**.
**#4 NINGÚN NÚMERO EN PROSA SIN CRUZARLO CON MI PROPIA TABLA.** ⚠️ **La rompí en la edición donde la estrené** (el
«53‑56 en los tres» contra mi tabla que decía 32‑57). Se cruza **grep mediante**, antes de commitear, no de memoria.
**#5 ⭐ NUEVO — AL ARBITRAR MODELOS, NOMBRAR AL MINORITARIO.** Y si después gana el minoritario, publicarlo con su
nombre. Hoy: dije «dos contra uno» contra el GFS y el GFS tenía razón.
**#6 ⭐ NUEVO — UNA URL ESTABLE NO HABLA EN «MAÑANA».** Si dice «mañana miércoles», al día siguiente miente sola.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA el día que vence**, y si el número se mueve ANTES, se adelanta el aviso.
  **Si lo que se cae es una REGLA o un TITULAR mío, se publica lo caído, con nombre y sin maquillar.**
- **⭐ CAMBIARLE EL MOTIVO A UNA RECOMENDACIÓN SIN CAMBIARLE EL DÍA** — 3 de 3 veces el motivo nuevo salió más fuerte.
- **⭐ EL FRENO QUE NO SE CAE, LE CAMBIA EL MOTIVO** (lunes 21: era agua, es viento). Decir «ganaste días secos y **cero
  días podables**» vale más que vender la mejora entera.
- **⭐ FRENAR POR SEGURIDAD CONSTRUYE CREDIBILIDAD** — «ninguna fruta se pierde por 48 h; una caída de escalera sí», con
  la alternativa ya puesta al lado.
- **Cortas, todas probadas:** ⭐ la madrugada siguiente al corte, no la del día que podás · ⭐ una apuesta no se retoca el
  día antes de cobrarla (marcador provisorio aparte) · ⭐ decir el límite de lo que veo · ⭐ pedirle el dato que sólo él
  tiene · ⭐ la condición convertida en fecha · ⭐ el clima que habilita, no sólo el que prohíbe · ⭐ al nombrar una
  especie, foto + dónde está · ⭐ abrir rápido y no hacer nada ≠ no abrir · ⭐ su acción es feedback aunque no escriba ·
  **el título es el activo más medido** · **timing verificado > urgencia inventada** · **feedback_text = ley.**
- ⚠️ **`engagement.json` SUBCUENTA hasta 2,5 días: cruzar SIEMPRE con `task_states` + `uploads` + threads.**
- ⚠️ **Clima:** `curl` a open-meteo NO sale del runner → **WebFetch**, `forecast_days=7`, **un modelo por llamada**. La
  mínima DIARIA ≠ la madrugada, y la madrugada es el `hourly` de **04‑08**, no horas sueltas del día (hoy me comí ese
  error). ⚠️ `pip install Pillow` antes de `build.py`.

## 🚫 EJES MUERTOS (no volver, ni variaciones) + 🏆 LÍNEA DE PRODUCTO

**Muertos:** noticiero/«El Parte» · cero-lectura/duelos binarios · checklist de viaje · **vos-decidís** (el eje AGENCIA
vive, el CONTENEDOR se quemó) · mi-objetivo · role-play verboso · countdown · app pasiva · editorial 3ª pers ·
mapa/espacial *(un plano chico DENTRO de otra cosa sí)* · mística · racha · biografías · dinero · Wrapped · fútbol ·
**mucho texto** · era gimmick · `podas-vuelta` · **observacional suelto** (va DENTRO de otra cosa, nunca card).

**EL TALLER = la única aprobada, en los dos slots.** n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces**. Gana por
① sustancia técnica sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ errores
anticipados. Va **agrupado dentro** de la landing del slot, nunca en push aparte. ⚠️ Sus ticks **NO** escriben
`task_states.json`. · **EL OBJETO QUE SE LLENA:** bandeja (07/09) y `tres-pilas` (12/09) murieron **las dos por
APERTURA, nunca por contenido**; todo el veredicto del eje pasó a `el-marcador` y se lee el **17/09**.

## 🚫 ANTI-REPETICIÓN

⭐ **El registro con fechas vive en `facts_ledger.json` → `_nota_vigente`** (vedados por planta, cantera libre, ángulos
quemados con su fecha de liberación). **Se lee ANTES de armar contenido y se actualiza DESPUÉS.** Acá va sólo la regla,
no la lista — duplicarla era lo que hacía crecer este archivo sin aportar nada.

- Planta featured descansa **≥7 días**; un fact no se repite en **<14 días**; cada experiencia nueva usa **≥70 % de
  elenco no featured en 7 días**. **El canal tarea es monotemático: su cast lo define la TAREA**, y tiene excepción
  propia (jue 17: B‑1/B‑29/B‑22/B‑36; vie 18: B‑23/B‑24).
- ⭐ **Una reedición sin push NO consume elenco** (ayer y hoy: ningún veto se movió). · **La EXPOSICIÓN MEDIDA manda
  sobre el ledger:** una página que nunca se abrió no quemó su cast.
- ⚠️ **B‑34 fuera de toda cantera: ya no existe** (baja con consentimiento escrito del 04/09). **NUNCA borrar una
  especie sin consentimiento explícito del usuario.**
- **Próximas liberaciones:** 18/09 → B‑30, B‑35, F‑2. 19/09 → B‑24, B‑46, B‑47, B‑37. 21/09 → los 16 del marcador y del
  canal tarea. **Cantera libre hoy para el sábado 19: 34 especies.**

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo mantenimiento.**
Excepción única: una push que **él pidió por escrito**. **Un día sin slot limita las NOTIFICACIONES, no las EDICIONES**
— ayer y hoy se reeditó `jardin-hoy` sin push.

- ⚠️ **EL SÁBADO TIENE LAS DOS PUSH A 60 MIN Y ESO SE PAGA** (05/09 y 12/09) — **pero el lunes 14 se probó con 8 h de
  hueco y también dio 0: el hueco NO era el problema.** La cadencia es del usuario: si hay que cambiarla, se le propone
  **dentro de una experiencia**, nunca por mi cuenta.
- ⚠️ **El lunes 18:00 cae a 35 min del atardecer en septiembre** → toda experiencia de ese slot que pida salir a mirar
  **se guarda sola y dice que no vence**. ⚠️ **El 11/09 salió una `jardin-hoy` fuera de cadencia: no repetir.**
- **`expires_at` se ata a la ventana del contenido, no al 22:00 de rutina.** · **Canal tarea:** URLs estables que se
  **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`). NO correr `gen_task_reminders.py` ni
  `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`,
  Asamblea, tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en TODAS
  las tareas; sus fotos van al **thread**. · **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN
  MOVER** (B‑22/B‑36 es de PODA). · **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas), **no volver a
  pedir fotos generales**. · **05/09:** «No quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 JUEVES 17 — tres cosas en una corrida:** ① **leer el veredicto de `el-marcador`** (60 h cumplidas) y ejecutarlo
  sin reinterpretar; ② **compactar `engagement.json`** (vence ese día); ③ push de tarea 10:00: es la **víspera doble**
  (las cuatro de la helada ese mismo día, los cítricos al otro) — ahí va el filo y el orden de trabajo. **Y el aviso de
  la escalera: el GFS le pone 40,3 km/h al jueves.**
- **🎯 DEUDA COMPROMETIDA POR ESCRITO — se paga el sábado 19, esté como esté el marcador:** ① si terminó abajo de
  **7/10**, corregir en `data_plants.py` los meses de floración de las fichas que fallé y mostrarle el diff; ② cobrar la
  **apuesta del viernes 18** (0,0 mm · ráfaga **< 43** · máxima **18‑24°**) con el día cerrado, `past_days` +
  `best_match`. **Si sopla más de 43, la regla del +10% se murió y se publica muerta.** Hoy va ganando por 7,0 km/h.
- **🎯 SÁBADO 19 — la original nueva vuelve a lo que probadamente convierte** (su lista real de tareas con foto y un
  botón por ítem, estilo `puesta-al-dia`), NO a un formato nuevo. 11 días de sequía ya no dejan alternativa.
- **Si contesta lo de la escarcha:** si en su pasto hiela más tarde que el aire de la estación, **mover el jueves sin
  discutir** y decírselo con el número. Si contesta lo del viento en el fondo: bajar el umbral de freno y publicarlo.
- **19/09: vuelven las 5** que pospuso (B‑46‑5, B‑47‑3, B‑13‑2, B‑20, B‑32). **27/09:** B‑41. **15/10:** B‑45.
  **≈05/10:** semana 4 de la bandeja (prometido en su tabla). · **Cantera SIN USAR:** condiciones sin fecha del catálogo
  · poda×fruta · la coronita F‑5 en octubre · el NASA de la cinta · el Persia/China del durazno · «cada limón viene de
  una flor única».
