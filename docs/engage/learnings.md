# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🚨 LO PRIMERO DEL 10/09 — ÉL ME ESCRIBIÓ Y YO NO ME HABÍA ENTERADO

**El 08/09 20:07Z subió dos fotos a la ficha del Durazno B-30 con una pregunta en el campo `note`: *«Algunas hojas
parecen algo arrugadas, ¿está bien?»*.** Ayer registré las fotos y NO leí el `note`. Sexta vez que escribe en 8
semanas, primera **desde la ficha de especie** en vez de una página de engagement.

⭐ **REGLA NUEVA: el texto del usuario NO vive sólo en `engagement.json`.** Antes de armar nada, leer `uploads.json`
**campo por campo** (`note`, `user_context`), `sync/threads/*.json` y `user_tasks.json`. `ai_status: "n/a"` es sobre
la FOTO, **no** sobre el texto que la acompaña. Casi pierdo la mejor consulta del mes por leer el índice y no el
registro.

**Lo que era, mirado en la imagen original:** torque / abolladura del duraznero (*Taphrina deformans*) — hoja del brote
nuevo engrosada, ampollada, ondulada, borde rojizo. La 2ª foto muestra además **el pétalo rosado abierto**: confirma
con foto suya el `flowering: [8,9]` del catálogo.

## 🧨 EL HALLAZGO QUE VALE MÁS QUE EL DIAGNÓSTICO: LA CULPA ERA MÍA

**El que falló fui yo.** Él hizo su parte: marcó la limpieza de otoño con caldo bordelés **hecha el 02/05**. Pero
**el torque no se frena en otoño: se frena a yema hinchada, fines de julio** — y **esa fecha no existía en mi ficha**.
Tenía UNA de las DOS manos de cobre del año. Corregido: la nº1 pasa a **mayo 2027** y se agregó **`plant-B-30-3`
(alta, julio 2027)** con el protocolo entero y la señal de cuándo mirar la yema.

⭐ **REGLA: cuando algo sale mal en el jardín, la primera hipótesis es que MI ficha está incompleta, no que él no
hizo.** Se dice con todas las letras y se arregla el mismo día. Un sistema que se audita a sí mismo y paga el costo
por escrito es el activo que hace que valga la pena abrir la notificación.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS

- **⭐ LO QUE MÁS CONVIRTIÓ EN 8 SEMANAS: la lista de SUS tareas reales, con foto, dónde está y un botón por ítem.**
  El 05/09 lo confirmó caro: con las 2 push de la mañana no hizo nada, y de noche estuvo 40 minutos dentro de
  `puesta-al-dia` resolviendo 10 tareas y escribiéndome 2 veces.
- **⭐ CUANDO TIENE TRABAJO REAL PENDIENTE, LA EXPERIENCIA COMPITE Y PIERDE.** `el-portón` (05/09) y `la-bandeja`
  (07/09) están las dos en **CERO absoluto**. **No las rechazó: las desplazó.** ⭐ **Corolario: la experiencia no
  debe competir con la tarea, debe PARASITARLA** — hoy funcionó: la única pieza viva del portón (la condición de
  helada convertida en fecha) migró al canal tarea, que es el que sí abre.
- **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO ESCRIBA**, y el tap es su idioma (13 `answer` en una noche). **Y una foto con
  una línea de texto es la señal más rica que produce:** síntoma + planta + fecha en un solo gesto.
- **Las 6 veces que escribió fue LOGÍSTICA, IDENTIFICACIÓN, ORDEN DE TRABAJO o CONSULTA TÉCNICA, jamás una reseña:**
  no esperes veredicto, esperá instrucciones. La caja de feedback va igual en todas.
- **«Ocultar» no es «sacar»** · **dwell alto sin conversión ≠ éxito** · **«no contestó» ≠ «no le interesa»** · **el 201
  no mide nada: medir `sent_at − send_at`** · **nunca 3 push en un día sin slot** · **si hubo actividad suya en la
  última hora, no encolar.**

## ⚙️ ESTADO OPERATIVO (10/09/2026)

`pix9` **active** · `uploads.json` 0 pendientes (133 entries) · **threads 0 `pending`** · `user_tasks.json` 0 sin
contestar · `task_states.json` 81 entries (66 done, 11 snoozed, 4 active), última escritura suya **06/09 11:39Z** ·
proposals **92** (54 dropped / 23 promoted / **14 pending** / 1 approved / 1 removed) · **catálogo 51 especies y 102
tareas** (+1 hoy: `plant-B-30-3`), **37 activas** y 15 con ventana ya abierta · **vuelven el 12/09** B-46-3, B-24,
B-23; **el 19/09** B-47-3, B-46-5, B-32, B-20, B-13-2; **el 27/09** B-41; **el 15/10** B-45 · **compactación** no
vencía hoy (send_log más viejo 31/08, engagement 03/09): próximas **14/09** y **17/09**.

## 🛰️ ENTREGA — LA PREDICCIÓN QUE SE JUEGA HOY

El cron de GitHub no sirve: abrir la ventana a las 05Z **no** movió el pozo inicial (primera corrida real del día
13:25–15:47Z, siempre después del slot de 13:00Z). Lo que sí funciona es el trigger **`push` sobre `queue.json`**:
latencia commit → `run_started_at` de **+7, +10, +7 y +4 s** (4 de 4 bajo 10 s, contra 3–6 HORAS). Por eso
`WAIT_CAP_MIN` depende del evento: **`push` → 330 min**, `schedule` → 200, `timeout-minutes: 350`.

**🎯 Predicción falsable, primera mitad YA VERIFICADA hoy:** commit `746b4d5` pusheado 09:19:44Z →
`run_started_at` **09:19:52Z = +8 s** (5 de 5 bajo 10 s) y la corrida **quedó `in_progress`, o sea durmiendo**
— las de los días sin cola cerraban en ~20 s, así que el paso «esperar al slot» enganchó. Faltan **220 min** hasta
13:00Z, dentro del tope de 330 del evento `push`. **Mañana falta la otra mitad: `sent_at − send_at` de
`2026-09-10-jardin-hoy`.** Si el envío igual sale corrido: sacar la entrega de GitHub Actions (cron de Vercel contra
endpoint propio; el bloqueo es que `VAPID_PRIVATE_KEY` tendría que existir en Vercel — **pedírselo dentro de una
página**, nunca por chat).

⭐ **REGLA: antes de declarar muerto un contenido, verificar que haya llegado a horario.** 31/08 +263 min · 03/09 +89 ·
07/09 +168 y +75: cinco slots leídos como fracaso de contenido que fueron fracasos de canal.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). `audit.js` en scratchpad — playwright en `/opt/node22/lib/node_modules`,
chromium en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`; descartar `fixed`/`sticky` **mirando toda la cadena
de ancestros** (la barra de `engage.js` da un 6,1 % falso) y reportar el primer control de **acción**, no el link del
índice. **Últimas: ed.7 → 18,9 % · bandeja → 3,4 % · hoy → 16,8 %.**

**#3 EL LARGO TAMBIÉN ES LAYOUT.** Tope operativo **~12 ítems**. Hoy: **2 tareas + 1 diagnóstico** — el día que hay
una respuesta personal que dar, la lista se achica, no se estira.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA, ganada o perdida, ANTES de que él la revise, y el día que vence.**
  Hoy: la apuesta del portón, **temperatura ganada 3/3** (mínimas observadas 6,4 / 7,8 / 9,8) y **lluvia PERDIDA el
  último día** (0,9 mm y lloviendo). Se cobró aunque **él nunca abrió la página donde la dejé**. ⭐ **Corolario nuevo:
  la corrección que va A SU FAVOR vale doble** — le había dado el viernes 11 por perdido (2,6 mm, ráfagas 48) y los
  dos modelos ahora lo dan seco. Devolverle un día es mejor noticia que acertar.
- **⭐ CORREGIR MI PROPIA GUÍA CON EL DATO DE HOY ES CONTENIDO DE PRIMERA** (ver la mea culpa). · **⭐ FRENAR UNA
  TAREA VALE TANTO COMO PEDIRLA:** hoy saqué la lantana B-29 de la lista con el argumento a la vista (su foto la
  muestra con hoja verde hasta abajo, no leñosa). Una lista de la que yo mismo saco cosas es creíble; una que sólo
  crece es spam.
- **⭐ LA EXPERIENCIA TIENE QUE SER UN OBJETO QUE SE LLENA, NO UN TEXTO CON UN BOTÓN AL FINAL.** Sigue sin probarse:
  la bandeja llegó +75 min tarde y con 0 visitas. La hipótesis está VIVA, no refutada.
- **Ayudarlo a HACER > informarlo**; **darle DÓNDE registrar lo que ya hizo** es casi igual de fuerte. · **⭐ CUANDO
  NOMBRÉS UNA ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE** (03/09: «no sé cuál es el crespón y la althea»). · **⭐ EL CLIMA
  COMO EDITOR** · **⭐ LA CONDICIÓN CONVERTIDA EN FECHA** — hoy en su forma más fuerte: la de B-1 («pasada la última
  helada») pasó de **pronosticada** a **VERIFICADA con mínimas observadas**.
- **⭐ VERIFICAR MI PROPIO DATO ANTES DE PUBLICARLO.** · **El título es el activo más medido.** · **Timing verificado >
  urgencia inventada.** · **feedback_text = ley.** · ⚠️ `curl` a open-meteo NO sale del runner: **WebFetch**,
  `forecast_days=7`, **un modelo por llamada**; para saldar apuestas, `past_days` con `best_match`.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero / «El Parte»** · **cero-lectura / duelos binarios** · **checklist de viaje** · **vos-decidís** (el eje
AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª
pers · mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak ·
biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** · **era gimmick** · **`podas-vuelta`
CERRADA** · **contenido observacional suelto** («sacale foto a la flor»): pospuso 8 de un saque — **va como pedido
corto DENTRO de otra cosa, nunca como card propia** (hoy: el tri-botón de B-35 adentro de la card del durazno).

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces** y ticks por árbol horas después. n°2: 7/7, cero reacción.
n°3 (24/08): leído entero, sin veredicto. **Por qué gana:** ① sustancia técnica sobre SUS plantas ② se abre con la
herramienta en la mano ③ una pantalla = una decisión ④ errores anticipados ⑤ diagramas propios.
⚠️ **Sus ticks (`taller-arbol-<code>`) NO escriben `task_states.json`:** contar con `generate_tasks_from_plants(PLANTS)`
+ `task_states.json`, **descartando las 16 huérfanas**. ⚠️ `pip install Pillow` antes de `build.py`.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo
  define la TAREA** (hoy: lo definió su propia foto). · **La EXPOSICIÓN MEDIDA manda sobre el ledger.**
- ⭐ **AHORA ES AFIRMABLE, NO PRESUNTO:** `engagement.json` no trajo **ningún** evento del 07, 08 ni 09/09 y ya pasaron
  3 días, por encima del atraso de flush máximo medido (2,5 d). O sea que **la bandeja y la ed.6 de puesta-al-día
  tienen exposición CERO medida** → su elenco (I-1, I-2, B-6, B-26, B-2, B-10, B-3, F-5, B-27) queda **fresco** y se
  libera el 14/09 sin culpa.
- ⚠️ **VEDADOS HASTA EL 17/09:** B-30, B-35, B-1, F-2. **HASTA EL 14/09:** I-1, I-2, B-6, B-26, B-2, B-10, B-3, F-5,
  B-27. **HASTA EL 13/09:** B-7, B-5a, B-23, B-25, B-12, B-15, B-8, B-4, B-43, B-22, B-36, F-3, B-41. **HASTA EL
  12/09:** B-46, B-9, B-18, B-24, B-32, B-20, B-13, B-47.
- ✅ **LIBRES para el sábado 12/09 11:00:** B-16, B-37, F-9, B-44, B-40, F-8, F-10, B-14, B-45, B-48, B-49, B-21,
  B-28, B-11, B-31, B-33, B-39, F-1. **B-34 fuera de toda cantera: ya no existe.**
- **No repetir antes del 21/09:** la propagación/esqueje entera · «lo que ibas a tirar» · el ejemplar único / sin
  repuesto · la campana de botella · el corte al ras bajo el nudo · el lado este como vivero · el reparto de la
  ventana por día. **Nuevo, no antes del 24/09:** el diagnóstico sanitario sobre foto suya · la mea culpa de ficha
  incompleta · «la ventana de este año ya cerró».

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo mantenimiento.**

- **Excepción válida y única:** una push que **él pidió por escrito** (pasó el 06/09). Se anota en el ledger. · **Un día
  sin slot no es un día sin trabajo:** limita las **notificaciones**, no las **ediciones**.
- **Una sola push por slot de experiencia:** original NUEVA + las **aprobadas** de ese slot agrupadas DENTRO.
  **Aprobación = recurrencia** (😍 / slot «sí» / `engageApprove`); pending no se borra, no recurre. **Única aprobada:
  `el-taller`, en los dos slots.** Contrato completo: `engagement.md` §4.
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`,
  Asamblea, tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en
  TODAS las tareas. · Las fotos y comentarios de esas páginas van al **thread**: los procesa `/responder-tareas`.
- **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA). · **04/09:**
  42 fotos de especie (`ai_status:"n/a"`: NO procesarlas), **no volver a pedir fotos generales**; sin foto: B-41,
  B-32, B-43, B-46/47, B-2B, B-22, B-36. · **B-34 dada de baja con consentimiento escrito — NUNCA borrar una especie
  sin eso.** · **05/09:** «No quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 MAÑANA VIERNES, LO PRIMERO: `sent_at − send_at` de `2026-09-10-jardin-hoy`.** Es el veredicto del trigger
  `push`. Recién con eso se puede leer si la bandeja y el portón fallaron por contenido o por canal.
- **🎯 SÁBADO 12/09 (2 slots): la experiencia se juega el todo por el todo.** Con exposición cero en las dos últimas,
  la apuesta es la hipótesis viva del **objeto que se llena**, pero **parasitando la tarea**: que la landing del slot
  11:00 sea el mismo objeto donde registra lo que hizo el viernes con B-1 y F-2, no una pieza aparte que compita.
- **Cobrar la promesa del viernes:** hoy afirmé que el viernes 11 está seco y que es EL día de tijera. Se verifica el
  sábado con `past_days`, gane o pierda.
- **12/09 y 19/09: vuelven las 9 que pospuso.** Traerlas ese día, agrupadas, no de a una.
- **Semana 4 de la bandeja (≈05/10): recordarle qué mirar** — lo prometí en la tabla de la página.
- **Si contesta el tri-botón de B-35:** si dice «igual de mal», la tarea de cobre de julio pasa a nombrar los dos
  ejemplares en el título; si dice «ese está sano», hay un dato de foco que vale una card entera.
- **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta (feb y may-sep) · la coronita F-5 en octubre ·
  el fun_fact NASA de la cinta · el bálsamo del liquidámbar B-37 · el fun_fact Persia/China del durazno (intacto).
