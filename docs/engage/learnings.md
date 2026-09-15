# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🎯 LO DE HOY (mar 15/09) — DÍA SIN SLOT: 0 push. Y me encontré un error mío publicado

**Encolado: NADA** (martes = mantenimiento por cadencia). `queue.json` quedó en 0 entries. Lo único que se tocó es una
**reedición SIN push** de la URL estable `2026-07-24-jardin-hoy.html`, que es lo que él abre el jueves 10:00.

**⚠️ EL HALLAZGO DEL DÍA ES CONTRA MÍ, y es una falla nueva de proceso:** la página que publiqué ayer decía en prosa
**«el jueves amanece a 14,5°»** mientras **su propia tabla, dos bloques más abajo, decía 5,5‑7,7°**. Los tres modelos
re‑pedidos hoy dan **6,1‑9,1°**. O sea: ⭐ **me creí mi propio titular sin mirar mi propia tabla, y publiqué una página
que se contradecía a sí misma.** No fue el modelo el que se movió: el dato bueno ya estaba en la página.
⭐ **REGLA NUEVA #4 (abajo): ningún número va en prosa sin cruzarlo contra la tabla de la misma página.**

**Lo segundo caído:** el «no vuelve a bajar». Vienen **tres madrugadas de 6‑9° seguidas** (mar/mié/jue) y el salto es el
**viernes**. El escalón de nueve grados existe pero es de **máxima** (mié 9,7‑14,4 → jue 17,3‑20,9), no de madrugada.

**⭐ Y de la corrección salió un argumento MEJOR que el que se cayó** — por eso la fecha del jueves 17 no se movió:
**para un corte fresco no importa la madrugada del día que podás, importan las madrugadas que vienen DESPUÉS**, con la
herida abierta. Podando el jueves, la noche siguiente es la del viernes (**12,2‑20,7°**, la más tibia de la ventana) y
ningún modelo vuelve a bajar de 8,4°. Podando el lunes le tocaban tres madrugadas de 6‑9° con el corte abierto.
⭐ **Segunda vez en dos días que le cambio el MOTIVO a una recomendación sin cambiarle el DÍA, y la segunda que el motivo
nuevo es más fuerte que el viejo.** Eso ya es una línea, no una casualidad.

**Estado del clima (3 modelos, re‑pedidos hoy 06:05):** 0,0 mm de mañana **al domingo 20** — cinco días secos — y la
ventana **cierra el lunes 21**, pero con el **primer desacuerdo serio de toda la ventana**: ECMWF 9,6 mm/56 km/h, mixto
7,8/54, **GFS seco con 32**. Se publicó como «dos contra uno», no como acuerdo. Hoy martes es el único día feo
(35‑45 km/h) — **eso sí lo acerté de punta a punta desde el lunes**. El pitósporo B‑43 se movió al **miércoles 16**: es
el pozo de frío (máx 9,7‑14,4) pero seco y calmo, y es la única planta a la que el frío le da igual.

**Apuesta del viernes, marcador provisorio (los términos NO se tocaron):** ✅ lluvia 0,0 en los tres · ✅ ráfagas, el más
alto es **42,1 contra mi techo de 43 — gano por 0,9 km/h** (ayer la misma regla perdía por 0,7; el GFS se movió 2,9 en
un día) · 🟡 máxima 18‑24°: ECMWF 23,3 y GFS 21,3 adentro, mixto 15,4 afuera → **2 de 3**, y la discrepancia de 7° que
declaré el lunes hoy es de casi 8. **Se cobra el sábado 19 con el día cerrado, acierte o pierda.**

## ⏳ EL MARCADOR — veredicto NO ejecutado hoy, y no es que lo mueva

`el-marcador` (14/09 18:00) lleva **12 h y cero eventos**. **Los números predeclarados quedan exactamente como estaban:
≥5 taps = probado y se serializa · 0 taps con canal sano y sin push compitiendo = el formato muere y se archiva el eje.**
Lo que NO se puede hacer es **leerlos a las 12 h**: mi propia regla dice que `engagement.json` subcuenta hasta 2,5 días.
⭐ **Declarar muerto un formato con 12 h de datos sería cometer el error que yo mismo me prohibí.**
**FECHA DE VEREDICTO: jueves 17/09** (cierra la ventana de 60 h, y es día de corrida igual). Se lee **una sola vez** y se
ejecuta lo que diga. Dato de control: `tres-pilas` también estaba en cero a las 12 h **y siguió en cero a las 60** — así
que el cero de hoy no informa todavía en ningún sentido, ni bueno ni malo.

## 📊 CONCLUSIONES DE LAS PUSH ENVIADAS — la sequía de 9 días, leída sin maquillaje

**Últimas 6 push (10/09 → 14/09): 1 solo click, 0 taps, 0 reacciones, 0 feedback, 0 aprobaciones.**

| Push | Slot | Resultado |
|---|---|---|
| 10/09 jardin-hoy (jue) | 10:00 | ⬛ 0 |
| 11/09 jardin-hoy (vie) | 12:30Z | ⬛ 0 — **y además salió fuera de cadencia; no repetir** |
| 12/09 jardin-hoy (sáb) | 10:00 | ✅ click a **+25 min** — el único evento de 9 días |
| 12/09 tres-pilas (sáb) | 11:00 | ⬛ 0 — a 60 min de la anterior |
| 14/09 jardin-hoy (lun) | 10:00 | ⬛ 0 (20 h) |
| 14/09 el-marcador (lun) | 18:00 | ⏳ 0 a 12 h — veredicto el 17 |

**Lo que SÍ se puede concluir:**
- ⭐ **El canal es el único activo que quedó probado.** `sent_at − send_at` = **+3,6 s** el 10, 11, 12 y 14/09. Cuatro
  envíos consecutivos sanos. **Cuando algo mide 0, ya no hay dónde esconderse: es contenido, gancho o slot.**
- ⭐ **El único formato que sobrevive a la sequía es el canal tarea**, y sobrevive por el **título**, no por el cuerpo:
  el único click de 9 días fue a `jardin-hoy` y a +25 min. **Abrió y no tocó nada.** Gancho vivo, cuerpo muerto.
- ⭐ **La segunda push del día muere si la primera cae cerca:** 05/09 mismo minuto → 0 y 0; 12/09 a 60 min → convirtió la
  primera, la segunda ni se abrió. **A 8 h se mide el jueves.**
- 🚨 **Lo honesto: 9 días sin una sola señal activa es fatiga o rechazo del canal, no mala suerte de formato.** Lo que
  convirtió de verdad (05/09: 40 min, 13 `answer`, 10 tareas resueltas de noche en `puesta-al-dia`) fue **su lista real
  de tareas con foto y un botón por ítem** — y hace 10 días que no le mando eso, le mando experimentos. **El sábado 19
  la original nueva debería volver a ESO**, no a un formato nuevo más.

## 💬 FEEDBACK DE TEXTO — los 3 vivos, ya ejecutados (ninguno nuevo desde el 05/09)

1. *«Nose cuál es el crespón y la althea»* (03/09) → **al nombrar una especie, foto + dónde está, siempre.**
2. *«Sacá todas las tareas ya completadas para achicar la página»* (05/09) → hecho. **«Ocultar» no es «sacar».**
3. *«Volvémela a enviar cuando revises con mi feedback en mente»* (05/09) → hecho. **Pide re‑envío, no novedad.**

**Preguntas suyas abiertas, sin contestar hace 10 días** (las dos en la caja de `jardin-hoy`): ① el viento en el fondo
contra el muro de la cancha de pádel — si ahí pega menos, **mis frenos le sacan días de poda al pedo**; ② **¿viste
escarcha blanca en tu pasto en septiembre?** Sigue viva la de los limones («más de veinte», contados de su foto 04/09).
⚠️ **Dos preguntas sin respuesta en 10 días es señal: no sumar una tercera.**

## ⚙️ ESTADO OPERATIVO (15/09/2026)

`pix9` **active** · `uploads.json` 0 pendientes (última foto 08/09) · threads 0 `pending` · `user_tasks.json` 0 sin
contestar · `task_states.json` 81 entries — **66 done / 11 snoozed / 4 active**; 38 activas sobre 102 del catálogo ·
último evento **12/09 13:25Z (67 h)** · proposals **94** (55 dropped / 23 promoted / **14 pending** / 1 approved /
1 removed) · **compactado hoy:** `send_log` −2 eventos del 31/08 (`daily_summary` intacto, `sent: 2`), `queue.json`
vaciada de las 2 del 14/09. `engagement.json` arranca el 03/09 → **vence el 17/09**, compactarlo en esa corrida.

## 🚨 LAS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick:** ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
**#2 EL CONTROL VA ARRIBA:** ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). `pos.js` en scratchpad — playwright en `/opt/node22/lib/node_modules`,
chromium en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Descartar `[hidden]`, rects de área cero y la
quickbar de `engage.js`. Hoy: **jardin‑hoy 24,0 %**, sin overflow horizontal.
**#3 EL LARGO TAMBIÉN ES LAYOUT:** tope operativo **~12 ítems**.
**#4 ⭐ NUEVO — NINGÚN NÚMERO EN PROSA SIN CRUZARLO CON MI PROPIA TABLA.** Ayer publiqué una página que se contradecía a
sí misma. El error no vino de afuera: el dato bueno estaba doce líneas más abajo, escrito por mí.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA el día que vence**, y si el número se mueve ANTES, se adelanta el aviso.
  **Si lo que se cae es una REGLA mía, se publica la regla caída.** ⭐ **Y si el error es mío y no del modelo, se dice
  que fue mío** — hoy: «me creí mi propio titular sin mirar mi propia tabla».
- **⭐ CAMBIARLE EL MOTIVO A UNA RECOMENDACIÓN SIN CAMBIARLE EL DÍA** (2 de 2 veces el motivo nuevo salió más fuerte).
- **⭐ NUEVO: LO QUE IMPORTA ES LA MADRUGADA SIGUIENTE AL CORTE, NO LA DEL DÍA QUE PODÁS.** Sirve para toda poda.
- **⭐ NUEVO: UNA APUESTA NO SE RETOCA EL DÍA ANTES DE COBRARLA** — se publica el marcador provisorio al lado, aparte.
- **⭐ DECIR EL LÍMITE DE LO QUE VEO** · **⭐ PEDIRLE EL DATO QUE SÓLO ÉL TIENE** · **⭐ LA CONDICIÓN CONVERTIDA EN FECHA**
  · **⭐ FRENAR VALE TANTO COMO PEDIR** · **⭐ EL CLIMA QUE HABILITA, NO SÓLO EL QUE PROHÍBE** · **⭐ AL NOMBRAR UNA
  ESPECIE: FOTO + DÓNDE ESTÁ** · **⭐ ABRIR RÁPIDO Y NO HACER NADA ≠ NO ABRIR** · **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO
  ESCRIBA** · **⭐ `engagement.json` SUBCUENTA hasta 2,5 días: cruzar SIEMPRE con `task_states` + `uploads` + threads** ·
  **el título es el activo más medido** · **timing verificado > urgencia inventada** · **feedback_text = ley.**
  ⚠️ `curl` a open-meteo NO sale del runner: **WebFetch**, `forecast_days=7`, **un modelo por llamada**. ⚠️ La mínima
  DIARIA ≠ la madrugada: para helada cruzar `daily.temperature_2m_min` con el `hourly` de 03:00‑09:00. ⚠️ `pip install
  Pillow` antes de `build.py`.

## 🚫 EJES/FORMATOS MUERTOS (NO volver, ni variaciones)

**noticiero/«El Parte»** · **cero-lectura/duelos binarios** · **checklist de viaje** · **vos-decidís** (el eje AGENCIA
vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers ·
mapa/espacial *(un plano chico DENTRO de otra cosa sí)* · mística · racha · biografías · dinero · Wrapped · fútbol ·
**mucho texto** · **era gimmick** · **`podas-vuelta`** · **observacional suelto** (va DENTRO de otra cosa, nunca card).

## 🏆 LÍNEA DE PRODUCTO

**EL TALLER = la única aprobada, en los dos slots.** n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces**. Gana por:
① sustancia técnica sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ errores
anticipados. Va **agrupado dentro** de la landing del slot, nunca en push aparte. ⚠️ Sus ticks **NO** escriben
`task_states.json`.
**EL OBJETO QUE SE LLENA:** bandeja (07/09) y `tres-pilas` (12/09) murieron **las dos por APERTURA, nunca por
contenido** — `tres-pilas` cerrado el 15/09 como no‑exposición definitiva, su hipótesis **sin refutar**. Todo el
veredicto del eje pasó a `el-marcador` y se lee el **17/09**.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **El canal tarea es monotemático: su cast lo define la TAREA.**
  · **La EXPOSICIÓN MEDIDA manda sobre el ledger.** · ⭐ **Una reedición sin push NO consume elenco** (hoy: no se movió
  ningún veto).
- ⚠️ **VEDADOS HASTA EL 21/09:** B‑13, B‑15, B‑38, B‑39, F‑3, B‑26, F‑1, B‑20, B‑32, B‑41 + B‑23, B‑43, B‑1, B‑29,
  B‑22, B‑36. **HASTA EL 19/09:** B‑24, B‑46, B‑47, B‑37. **Se liberan el 18/09:** B‑30, B‑35, F‑2.
- ✅ **CANTERA LIBRE PARA EL SÁBADO 19 (34):** B‑16, F‑9, B‑44, B‑40, F‑8, F‑10, B‑14, B‑45, B‑48, B‑49, B‑21, B‑28,
  B‑11, B‑31, B‑33, B‑9, B‑18, B‑4, B‑42, B‑6, B‑10, B‑3, B‑2, F‑5, B‑27, B‑7, B‑5a, B‑25, B‑12, B‑8, F‑7, F‑4, I‑1,
  I‑2. **B‑34 fuera de toda cantera: ya no existe** (baja con consentimiento escrito — NUNCA borrar una especie sin eso).
- **Excepción del canal tarea:** el **jueves 17** vuelven por derecho propio B‑1/B‑29/B‑22/B‑36 (es su víspera) y el
  **viernes 18** B‑23/B‑24 (cítricos), aunque figuren vedados.
- **Ángulos quemados, no antes del 28/09:** la apuesta arbitrada por el usuario · «tus fotos del 04/09, diez días
  después» · la hiedra con dos clases de hoja · el cuajado como bolita verde · el sur que atrasa y por eso protege · el
  rojo de la fotinia como cronómetro · la anti‑apuesta de los sépalos y el dioico · el pétalo comestible · «el piso pasó
  hace tres horas» · «seis días secos en los tres modelos» · la regla del +10% apretada · «¿viste escarcha?».
  **Del 29/09 (quemados hoy):** «la madrugada siguiente al corte, no la del día que podás» · «la ventana seca tiene
  fecha de cierre» · «el día raro que sólo le sirve al pitósporo» · «me creí mi propio titular sin mirar mi tabla».
- **Siguen vedados — del 21/09:** propagación/esqueje · «lo que ibas a tirar» · el ejemplar único sin repuesto · la
  campana de botella · el corte al ras bajo el nudo · el lado este como vivero · el reparto de la ventana por día.
  **Del 24/09:** el diagnóstico sanitario sobre foto suya · la mea culpa de ficha incompleta · «la ventana ya cerró».
  **Del 25/09:** la ventana partida por hora. **Del 26/09:** la corrección de mi corrección · la llovizna como ventaja ·
  el abuelo y el nieto cítricos · el alcohol 70% · el conteo apostado contra la ficha · el storax del liquidámbar.
  **Del 27/09:** la regla que se muere en 24 h · los dos errores para el mismo lado · el error para el lado seguro.

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo mantenimiento.**

- **Excepción única:** una push que **él pidió por escrito**. · **Un día sin slot no es un día sin trabajo:** limita las
  **notificaciones**, no las **ediciones** — hoy se reeditó `jardin-hoy` sin push. · **Una sola push por slot de
  experiencia:** original NUEVA + las **aprobadas** de ese slot DENTRO. **Aprobación = recurrencia.**
- ⚠️ **EL SÁBADO TIENE LAS DOS PUSH A 60 MIN Y ESO SE PAGA** (05/09 y 12/09). La cadencia es del usuario y **no se toca
  sola**: si el lunes con 8 h convierte, **proponérselo dentro de una experiencia**, nunca cambiarlo por mi cuenta.
- ⚠️ **El slot del lunes 18:00 cae a 35 min del atardecer en septiembre.** Toda experiencia de ese slot que pida salir a
  mirar **tiene que guardarse sola y decir que no vence**.
- ⚠️ **El 11/09 (viernes) salió una `jardin-hoy` fuera de cadencia.** No volver a encolar en días sin slot.
- **`expires_at` se ata a la ventana del contenido, no al 22:00 de rutina.**
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`,
  Asamblea, tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en TODAS
  las tareas; sus fotos van al **thread**. · **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN
  MOVER** (B‑22/B‑36 es de PODA). · **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas), **no volver a
  pedir fotos generales**. · **05/09:** «No quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 JUEVES 17 — tres cosas en una corrida:** ① **leer el veredicto de `el-marcador`** (60 h cumplidas) y ejecutarlo
  sin reinterpretar; ② **compactar `engagement.json`** (vence ese día); ③ push de tarea 10:00: es la **víspera doble**
  (las cuatro de la helada ese mismo día, los cítricos al otro) — ahí va el filo y el orden de trabajo.
- **🎯 DEUDA COMPROMETIDA POR ESCRITO — se paga el sábado 19, esté como esté el marcador:** ① si terminó abajo de
  **7/10**, corregir en `data_plants.py` los meses de floración de las fichas que fallé y mostrarle el diff; ② cobrar la
  **apuesta del viernes 18** (0,0 mm · ráfaga **< 43** · máxima **18‑24°**) con el día cerrado, `past_days` +
  `best_match`. **Si sopla más de 43, la regla del +10% se murió y se publica muerta.**
- **🎯 SÁBADO 19 — la original nueva debería volver a lo que probadamente convierte** (su lista real de tareas con foto
  y un botón por ítem, estilo `puesta-al-dia`), NO a un formato nuevo. 9 días de sequía lo piden.
- **Si contesta lo de la escarcha:** si en su pasto hiela más tarde que el aire de la estación, **mover el jueves sin
  discutir** y decírselo con el número. Si contesta lo del viento en el fondo: bajar el umbral de freno y publicarlo.
- **19/09: vuelven las 5** que pospuso (B‑46‑5, B‑47‑3, B‑13‑2, B‑20, B‑32). **27/09:** B‑41. **15/10:** B‑45.
  **≈05/10:** semana 4 de la bandeja (prometido en su tabla). · **Cantera SIN USAR:** condiciones sin fecha del catálogo
  · poda×fruta · la coronita F‑5 en octubre · el NASA de la cinta · el Persia/China del durazno · «cada limón viene de
  una flor única».
