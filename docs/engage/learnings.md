# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🎯 LO DE HOY (lun 14/09) — DÍA DE LOS DOS SLOTS. Y el hueco de 8 h es todo el experimento

**Encolado:** `jardin-hoy` 10:00 (reedición en su URL estable) + **`el-marcador` 18:00** (experiencia original nueva).
**Sin señal nueva del usuario desde el 12/09 13:25Z** — el último evento sigue siendo aquel click. Cruzado otra vez contra
`task_states` (sin escrituras desde el 06/09), `uploads.json` (sin fotos desde el 08/09) y threads (0 pending): **el cero de
`tres-pilas` es real y ya es definitivo** (2º reconteo). Nada nuevo que interpretar: hoy es un día de apuesta, no de lectura.

**⭐ EL DATO DE LA SEMANA:** los tres modelos coinciden en **0,0 mm de hoy al sábado 19** — seis días secos, martes el único
feo (ráfagas 38‑45). Y el frío se cortó: **5,5° a las 7 de hoy (ECMWF marcó 1,4 de mínima), 8,5 mañana, 8,1 el miércoles y
14,5 el jueves** — escalón de **nueve grados** que no vuelve a bajar. ⭐ Eso **convirtió una condición en fecha**: las 4 fichas
que dicen «pasada la última helada (estimado 2ª semana de septiembre)» —B‑1, B‑29, B‑22, B‑36— **tienen fecha: jueves 17**.
Primera vez que una estimación mía de hace meses cae justo, y se dijo sin agrandarla: **veo 6 días, no la primavera.**

**EL AJUSTE DEL VIERNES, adelantado porque el GFS se movió:** ayer publiqué techo **35**; hoy el GFS da **39,2**. ⭐ **La regla
del +10% que nació ayer ya quedó corta por 0,7 km/h** — publicada apretada, en la misma página. **El viernes sigue siendo el
día de la poda pero YA NO GANA POR VIENTO: gana por la madrugada** (7,5‑10,3°, la más tibia de los días secos), que en cítrico
recién cortado es la condición que manda. ⭐ **Se le cambió el motivo, no el día, y se le dijo.**

## 🆕 EL MARCADOR — la apuesta del día, con veredicto predeclarado

**10 apuestas fenológicas mías, escritas antes de que mire, y él arbitra con 3 botones (acerté / erré / no llegué).** Barra
sticky que se llena en vivo. 8 de las 10 sobre **sus fotos del 04/09** («pasaron diez días, esto cambió»); las 2 sin foto de
ese día van declaradas como «voy a ciegas». Elenco 100 % con ≥7 días de descanso, cero superposición con el canal tarea.

- **Por qué este formato:** es el **objeto que se llena** —muerto dos veces (bandeja 07/09, tres‑pilas 12/09) **las dos por
  APERTURA, nunca por contenido**— puesto por fin en el único slot con **8 h de hueco**. ⭐ **Un formato no se refuta con una
  página que nadie miró.** Y lo que cambia: ahí el tap ordenaba el jardín, acá **el tap me puntea a mí** — ⭐ **la pregunta
  que puede refutarme es la única que da ganas de contestar**, llevada de pregunta suelta a mecánica de toda la página.
- **Pacto publicado:** abajo de 7/10 **corrijo esta semana los meses de floración de las fichas que fallé** y le muestro el
  diff el sábado. Deuda real, anotada abajo. **VEREDICTO PREDECLARADO (no moverlo mañana): ≥5 taps = probado y se serializa ·
  0 taps con canal sano y sin push compitiéndole = el formato muere de verdad** y se archiva el eje.
- ⚠️ **Restricción asumida y dicha en la página:** llega 18:00 y **el sol se pone 18:35**. Se resolvió sin taparla: se guarda
  solo, no vence, fotinia y guayabo están en el frente a dos pasos, y **el martes de viento no sirve para podar pero sirve
  justo para mirar**.

## 📊 CONCLUSIONES ACUMULADAS + EL CANAL

- **⭐ LO QUE MÁS CONVIRTIÓ EN 10 SEMANAS: la lista de SUS tareas reales, con foto, dónde está y un botón por ítem.** (05/09:
  40 min en `puesta-al-dia` resolviendo 10 tareas, de noche.)
- **⭐ LA SEGUNDA PUSH DEL DÍA MUERE SI LA PRIMERA CAE CERCA:** 05/09 mismo minuto → 0 y 0; 12/09 a 60 min → convirtió la
  primera, la segunda ni se abrió. **Hoy se mide a 8 h.** Si a 8 h tampoco abre, el problema deja de ser el slot.
- **⭐ ABRIR RÁPIDO Y NO HACER NADA ≠ NO ABRIR.** Latencia baja = ganó el título; 0 taps = perdió el cuerpo. Dos diagnósticos.
- **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO ESCRIBA** (13 `answer` en una noche); **una foto con una línea es su señal más rica**.
  Las 7 veces que escribió fue logística/orden de trabajo/pedido de re‑envío, **jamás una reseña**.
- **⭐ `engagement.json` SUBCUENTA** (hasta 2,5 días): nunca leer «0 eventos» como «no abrió» sin cruzar `task_states` +
  `uploads.json` + threads. · **«Ocultar» no es «sacar»** · **dwell alto sin conversión ≠ éxito** · **el 201 no mide nada**.
- 🏁 **CANAL CERRADO Y SANO — no volver a investigarlo:** `send_at` → `sent_at` = **+3,6 s el 10, 11 y 12/09**. Desde el 10/09
  las métricas de contenido SÍ significan algo — pero **medir `sent_at − send_at` antes de declarar muerto un contenido.**

## 💬 FEEDBACK DE TEXTO — los 3 vivos, ya ejecutados (ninguno nuevo desde el 05/09)

1. *«Nose cuál es el crespón y la althea»* (03/09) → **al nombrar una especie, foto + dónde está, siempre.** Sin excepción.
   Hoy se cumplió incluso al revés: **de B‑22 y B‑36 dije que NO tengo foto**, en vez de nombrarlas a secas.
2. *«Sacá todas las tareas ya completadas para achicar la página»* (05/09) → hecho. **«Ocultar» no es «sacar».**
3. *«Volvémela a enviar cuando revises con mi feedback en mente»* (05/09) → hecho. **Pide re‑envío, no novedad.**

**Preguntas abiertas suyas** (las dos en la caja de `jardin-hoy`, y la del viento repetida en `el-marcador`): ① el viento en el
fondo contra el muro de la cancha de pádel — si ahí pega menos que en la estación, **mis frenos le sacan días de poda al
pedo**; ② **¿alguna vez viste escarcha blanca en tu pasto en septiembre?** — decido «pasada la helada» con el aire de una
estación que no está en su casa, y **el hielo en su pasto es el único dato que importa**. Sigue viva la de los limones
(«más de veinte», contados de su foto del 04/09).

## ⚙️ ESTADO OPERATIVO (14/09/2026)

`pix9` **active** · `uploads.json` 0 pendientes (última foto 08/09) · threads 0 `pending` · `user_tasks.json` 0 sin contestar ·
`task_states.json` 81 entries — **66 done / 11 snoozed / 4 active**, y sobre las 102 tareas del catálogo quedan **38 activas** ·
último evento **12/09 13:25Z** · proposals **94** (55 dropped / 23 promoted / **14 pending** / 1 approved / 1 removed) ·
**compactación: NADA VENCIDO HOY** — `engagement.json` arranca el 03/09 (vence 17/09) y `send_log` el 31/08 17:23Z (vence
mañana 15/09, con `daily_summary` de esa fecha ya escrito); `queue.json` quedó reescrita de cero con las 2 del día.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick:** ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
**#2 EL CONTROL VA ARRIBA:** ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium 390×780**
(nunca por offset de caracteres). `audit.js` + `pos.js` en scratchpad — playwright en `/opt/node22/lib/node_modules`, chromium
en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ **Descartar `[hidden]`, los rects de área cero y la quickbar que
inyecta `engage.js`**, o da 0 % / 6 % falsos. Hoy: **jardin‑hoy 23,0 % · el‑marcador 18,0 %**, sin overflow horizontal.
**#3 EL LARGO TAMBIÉN ES LAYOUT:** tope operativo **~12 ítems**. Hoy jardin‑hoy 3 tarjetas, el‑marcador 10 apuestas.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA el día que vence.** Si lo que se cae es una REGLA mía, se publica la regla
  caída, no sólo el número. ⭐ **NUEVO: y si el número se mueve ANTES de la fecha prometida, se adelanta el aviso** — hoy
  miré el viernes el lunes, no el jueves, porque el GFS se movió.
- **⭐ NUEVO: CAMBIARLE EL MOTIVO A UNA RECOMENDACIÓN SIN CAMBIARLE EL DÍA.** «El viernes ya no gana por viento, gana por la
  madrugada» es más creíble que sostener el motivo viejo, y no le cuesta ninguna reprogramación.
- **⭐ NUEVO: DECIR EL LÍMITE DE LO QUE VEO.** «Veo seis días, no la primavera» hace que el resto de la página valga más.
- **⭐ PEDIRLE EL DATO QUE SÓLO ÉL TIENE** · **⭐ LA CONDICIÓN CONVERTIDA EN FECHA POR CONVERGENCIA** · **⭐ FRENAR VALE TANTO
  COMO PEDIR** · **⭐ EL CLIMA QUE HABILITA, NO SÓLO EL QUE PROHÍBE** · **⭐ LA APUESTA FALSABLE SOBRE EL PROPIO OBJETO** ·
  **⭐ EL ERROR PARA EL LADO SEGURO ≠ EL ERROR** · **⭐ NO HACER LEYES SOBRE MÍ MISMO CON UNA MUESTRA** · **ayudarlo a HACER >
  informarlo** · **darle DÓNDE registrar lo hecho** · **⭐ AL NOMBRAR UNA ESPECIE: FOTO + DÓNDE ESTÁ** · **el título es el
  activo más medido** · **timing verificado > urgencia inventada** · **feedback_text = ley.**
  ⚠️ `curl` a open-meteo NO sale del runner: **WebFetch**, `forecast_days=7`, **un modelo por llamada**; para apuestas,
  `past_days` + `best_match`. ⚠️ La mínima DIARIA y la temperatura de la MADRUGADA no son lo mismo (la diaria puede caer a
  medianoche): para helada, cruzar `daily.temperature_2m_min` con el `hourly` de 03:00‑09:00. ⚠️ `pip install Pillow` antes
  de `build.py`.

## 🚫 EJES/FORMATOS MUERTOS (NO volver, ni variaciones)

**noticiero/«El Parte»** · **cero-lectura/duelos binarios** · **checklist de viaje** · **vos-decidís** (el eje AGENCIA vive, el
CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(un
plano chico DENTRO de otra cosa sí)* · mística · racha · biografías · dinero · Wrapped · fútbol · **mucho texto** · **era
gimmick** · **`podas-vuelta`** · **observacional suelto** — **va DENTRO de otra cosa, nunca card propia**.

## 🏆 LÍNEA DE PRODUCTO

**EL TALLER = la única aprobada, en los dos slots.** n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces**; n°2: 7/7 sin
reacción; n°3 (24/08): leído entero, **sin veredicto a 21 días**. **Gana por:** ① sustancia técnica sobre SUS plantas ② se abre
con la herramienta en la mano ③ una pantalla = una decisión ④ errores anticipados. Va **agrupado dentro** de la landing del
slot, nunca en push aparte — hoy dentro de `el-marcador`. ⚠️ Sus ticks **NO** escriben `task_states.json`.

**EL OBJETO QUE SE LLENA = hoy se juega su veredicto.** Bandeja (07/09) y `tres-pilas` (12/09): cero apertura las dos, cero
contenido refutado. `el-marcador` es su tercer y último intento, ahora con 8 h de hueco y con el tap convertido en puntaje
sobre mí. **Los números del veredicto están arriba y no se mueven mañana.**

**CENSO DE PRIMAVERA (31/08) → cerrado hoy como `dropped`, NO como perdedor:** exposición cero acumulada en 14 días, nunca
refutado. El eje «recorrido de observación» no se archiva: **reaparece dentro de `el-marcador` con un motivo para salir que el
censo no tenía.** Los dos HTML se conservan en el repo; simplemente no se pushean.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo define la
  TAREA.** · **La EXPOSICIÓN MEDIDA manda sobre el ledger.** · **Una reedición sin push no consume elenco.**
- ⚠️ **VEDADOS HASTA EL 21/09 (salieron hoy):** B‑13, B‑15, B‑38, B‑39, F‑3, B‑26, F‑1, B‑20, B‑32, B‑41 + B‑23, B‑43, B‑1,
  B‑29, B‑22, B‑36. **HASTA EL 19/09:** B‑24, B‑46, B‑47, B‑37. **Se liberan el 18/09:** B‑30, B‑35, F‑2.
- ✅ **CANTERA LIBRE PARA EL SÁBADO 19:** B‑16, F‑9, B‑44, B‑40, F‑8, F‑10, B‑14, B‑45, B‑48, B‑49, B‑21, B‑28, B‑11, B‑31,
  B‑33, B‑9, B‑18, B‑4, B‑42, B‑6, B‑10, B‑3, B‑2, F‑5, B‑27, B‑7, B‑5a, B‑25, B‑12, B‑8, F‑7, F‑4, I‑1, I‑2. **B‑34 fuera de
  toda cantera: ya no existe** (baja con consentimiento escrito — NUNCA borrar una especie sin eso).
- **Excepción del canal tarea:** el **jueves 17** vuelven por derecho propio B‑1/B‑29/B‑22/B‑36 (es su víspera) y el **viernes
  18** B‑23/B‑24 (cítricos), aunque figuren vedados.
- **Ángulos quemados hoy, no antes del 28/09:** la apuesta arbitrada por el usuario · «tus fotos del 04/09, diez días
  después» · la hiedra con dos clases de hoja · el cuajado como bolita verde · el sur que atrasa y por eso protege · el rojo
  de la fotinia como cronómetro · la anti‑apuesta de los sépalos y el dioico · el pétalo comestible que no cuesta la fruta ·
  «el piso pasó hace tres horas» · «seis días secos en los tres modelos» · la regla del +10% apretada por 0,7 · «¿viste
  escarcha en tu pasto?».
- **Siguen vedados — del 21/09:** propagación/esqueje · «lo que ibas a tirar» · el ejemplar único sin repuesto · la campana de
  botella · el corte al ras bajo el nudo · el lado este como vivero · el reparto de la ventana por día. **Del 24/09:** el
  diagnóstico sanitario sobre foto suya · la mea culpa de ficha incompleta · «la ventana de este año ya cerró». **Del 25/09:**
  la ventana partida por hora. **Del 26/09:** la corrección de mi propia corrección · la llovizna como ventaja · el abuelo y
  el nieto cítricos · el alcohol 70% entre cítricos vecinos · el conteo apostado contra la ficha · el storax del liquidámbar.
  **Del 27/09:** la regla que se muere en 24 h · los dos errores para el mismo lado · el error para el lado seguro.

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo mantenimiento.**

- **Excepción única:** una push que **él pidió por escrito** (se anota en el ledger). · **Un día sin slot no es un día sin
  trabajo:** limita las **notificaciones**, no las **ediciones**. · **Una sola push por slot de experiencia:** original NUEVA
  + las **aprobadas** de ese slot DENTRO. **Aprobación = recurrencia**; pending no se borra, no recurre.
- ⚠️ **EL SÁBADO TIENE LAS DOS PUSH A 60 MIN Y ESO SE PAGA** (05/09 y 12/09). La cadencia es del usuario y **no se toca sola**:
  si el lunes con 8 h convierte, **proponérselo a él dentro de una experiencia**, nunca cambiarlo por mi cuenta.
- ⚠️ **NUEVO: el slot del lunes 18:00 cae a 35 min del atardecer en septiembre** (hoy se pone 18:35). Toda experiencia de ese
  slot que pida salir a mirar **tiene que guardarse sola y decir que no vence** — hoy se hizo así. En diciembre el problema
  desaparece; entre abril y agosto es peor.
- **`expires_at` se ata a la ventana del contenido, no al 22:00 de rutina.**
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`, Asamblea,
  tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en TODAS las tareas; sus
  fotos van al **thread** (`/responder-tareas`). · **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN
  MOVER** (B‑22/B‑36 es de PODA — se repitió hoy en la tarjeta del jueves). · **04/09:** 42 fotos de especie (`ai_status:"n/a"`:
  NO procesarlas), **no volver a pedir fotos generales** — hoy se pidieron DOS puntuales (B‑20, B‑41) con motivo y consecuencia
  cada una, que es distinto. · **05/09:** «No quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 DEUDA COMPROMETIDA POR ESCRITO — se paga el sábado 19, esté como esté el marcador:** ① si terminó abajo de **7/10**,
  **corregir en `data_plants.py` los meses de floración de las fichas que fallé**, con lo que él vio, y mostrarle el diff;
  ② cobrar la **apuesta del viernes 18** (0,0 mm · ráfaga **< 43 km/h** = 39,2 + mi 10% · máxima **18‑24°**, rango abierto a
  propósito por los 7° de discrepancia ECMWF/mixto) con el día ya cerrado y `past_days` + `best_match`.
  **Si sopla más de 43, la regla del +10% se murió y se publica muerta.**
- **Jueves 17 (tarea 10:00):** es la **víspera doble** — las cuatro de la helada ese mismo día y los cítricos al otro. Ahí va
  el filo y el orden de trabajo, y se revisa el viernes por última vez antes de que agarre la tijera.
- **Si contesta lo de la escarcha:** si en su pasto hiela más tarde que lo que dice el aire de la estación, **mover el jueves
  sin discutir** y decírselo con el número. Si contesta lo del viento en el fondo: bajar el umbral de freno y publicarlo.
- **Si el marcador junta taps:** la serialización natural es **una tanda nueva cada lunes con otras 10 plantas** (hay 34 libres
  en la cantera) y un **acumulado histórico** («voy 23 de 40 desde septiembre»), que es el activo que ninguna app puede copiar.
- **19/09: vuelven las 5** que pospuso (B‑46‑5, B‑47‑3, B‑13‑2, B‑20, B‑32). **27/09:** B‑41. **15/10:** B‑45. **≈05/10:**
  semana 4 de la bandeja (prometido en su tabla). · **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta ·
  la coronita F‑5 en octubre · el NASA de la cinta · el Persia/China del durazno · «cada limón viene de una flor única».
