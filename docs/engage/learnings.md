# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🥇 LO PRIMERO DEL 06/09 — LE CONTESTÉ LAS DOS ÓRDENES CON LA PÁGINA, NO CON UNA PROMESA

Anoche escribió dos veces en `puesta-al-dia`:

1. **14:35Z — «Quiero que saques todas las tareas que ya esten completadas para achicar la pagina».**
2. **21:34Z — «Volverme a enviar cuando revises con mi feedback en mente».** (después de resolver 10 tareas él mismo)

**Hecho hoy (ed. 4):** las 2 que marcó hechas (B-9 crespón, B-18 althea) y las **8 que pospuso entre 21:30 y 21:32**
(B-46 vivero ×2, B-47 palmeras, B-32 viraró, B-20 arbusto, B-13 clivia, B-23 formación, B-24 mandarina) están **fuera del
HTML, no ocultas por CSS**. De 27 cards a **17**. Y no fue sólo borrar: la lista se **reordenó por ventana climática**.
Encolada 10:30 -03:00 como **única push del domingo — excepción válida porque la pidió por escrito**.

- ⭐ **«Ocultar» no es «sacar».** La ed. 3 ya escondía lo hecho con JS y él igual pidió achicarla: **lo que mide es el
  scroll que le queda, no el DOM**. Si pide achicar, se borra del archivo.
- ⭐ **Su ACCIÓN es feedback aunque no escriba.** Posponer 8 en 90 segundos es una edición: me dijo cuáles no van ahora.
  **Tratar cada `answer: snoozed` como un «sacame esto de adelante» y ejecutarlo en la reedición siguiente.**
- **Su patrón está clarísimo: pospuso todo lo observacional** (fotos de flor, decidir el destino de las palmeras, el
  vivero) **y se quedó con el trabajo de tijera y mano.** Contenido «mirá y contame» = fondo de la cola. **Ya lo sé, no lo
  vuelvo a testear.**

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS (lo que llevo aprendido del canal)

- **⭐ LO QUE MÁS CONVIRTIÓ EN 7 SEMANAS SIGUE SIENDO LO MISMO: la lista completa de SUS tareas reales, con foto, dónde
  está y un botón por ítem.** El 05/09 lo confirmó de la forma más cara posible: **con las 2 push de la mañana (tarea +
  experiencia «el portón») no hizo nada, y de noche estuvo 40 minutos dentro de `puesta-al-dia` resolviendo 10 tareas y
  escribiéndome 2 veces.** Cero gimmick, cero narrativa. **Esa es la forma.**
- **⭐ CUANDO TIENE TRABAJO REAL PENDIENTE, LA EXPERIENCIA COMPITE Y PIERDE.** `el-portón` (sábado 11:00) se fue a 0 clicks
  el mismo día que la página de tareas tuvo 7 visitas. **No la rechazó: la desplazó.** Corolario operativo: **el truco del
  portón (una condición sin fecha convertida en fecha) hay que aplicarlo DENTRO del canal tarea, no como página aparte.**
- **La caja de feedback de texto es el control que más convierte del sitio** (2 de 2 el 24/08, 1 el 03/09, **2 el 05/09**).
  Va en todas. Pero **las 5 veces que escribió fue LOGÍSTICA, IDENTIFICACIÓN o una ORDEN DE TRABAJO, jamás una reseña de
  contenido.** Sus mensajes son órdenes. **No esperes veredicto: esperá instrucciones y ejecutalas.**
- **Dwell alto sin conversión ≠ éxito** · **«no contestó» ≠ «no le interesa»** (03/09: 10 días de silencio y estaba entero)
  · **10 envíos seguidos con `201`: el status code no mide nada, medir `sent_at − send_at`.**
- **Lección más cara de agosto:** mandé una guía de ejecución a alguien que estaba fuera del país. **Chequear que esté
  físicamente en el jardín antes.**
- **Nunca 3 push en un día sin slot** (04/09: 3 envíos, 0 clicks, estaba adentro de la app subiendo 42 fotos). **Si hubo
  actividad suya en la última hora, no encolar.**

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

| Día | Tarea 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Excepción válida y única:** una push que **él pidió por escrito** (hoy domingo). Se anota siempre en el ledger.
- **Una sola push por slot de experiencia:** original NUEVA + las **aprobadas** de ese slot agrupadas DENTRO.
  **Aprobación = recurrencia:** sólo vuelve lo que prendió (😍 / slot «sí» / `engageApprove`); pending no se borra, no
  recurre. **Única aprobada: `el-taller` (n°1), en los dos slots.**
- Contrato de cada experiencia (back-link primero · reacción · slots · caja propia · aprobar/rechazar · pitch de 6 modelos
  · `send_at` ≥60 min · `expires_at` 22:00 · `-03:00`): está en `.claude/commands/engagement.md` §4.
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). Script en scratchpad (`audit.js`): playwright en
`/opt/node22/lib/node_modules`, `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`; filtrar por
visibilidad real y limitar a `.wrap`. **Hoy: `puesta-al-dia` ed.4 → 12,4 %, altura 13.078 px (era ~20k).**

**#3 EL LARGO TAMBIÉN ES LAYOUT.** **Tope operativo: ~12 ítems**; hoy 17 en 4 bloques cortos con índice arriba — es el
máximo que me permito, y sólo porque son tareas suyas y cada bloque abre con el día en que se hacen.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Y **darle DÓNDE registrar lo que ya hizo** es casi igual de fuerte: **13 `answer` en
  una noche.** Cerrar lo hecho es contenido.
- **⭐ CUANDO NOMBRÉS UNA ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE.** (03/09 perdí una respuesta entera por nombrar sin
  mostrar: «no sé cuál es el crespón y la althea».) Cuando **no** tengo foto suya, **decirlo en la card y pedírsela**.
- **⭐ EL CLIMA COMO EDITOR — es la mejor herramienta de recorte que tengo.** No «hay 17 tareas»: **el pronóstico ORDENA la
  lista y descarta lo que hoy sale peor.** Hoy estrené la variante más útil: **partir la lista en «lo que NO es tijera»
  (mínima de 3,2-5,8° el lunes: un corte fresco + helada de amanecer se lleva la madera nueva) y «la ventana de tijera»
  (mar 8 a jue 10, 0 mm y mínimas ≥6°).** «Hoy no salís» es contenido si le doy la que SÍ se puede.
- **⭐ LA PROMESA VERIFICADA, COBRADA POR MÍ PRIMERO.** Hoy cobré la del 05/09 sin que me la reclame: mar 6,2/6,7 · mié
  7,6/8,1 · jue 10,3/10,1 y 0 mm mar-mié en los dos modelos → **va ganando**, y **publiqué dónde puedo perder** (jueves:
  1,5 mm ECMWF vs 0 GFS; máximas que difieren 5,7°). **Publicar el desacuerdo entre modelos es más creíble que publicar un
  número solo.** ⚠️ `curl` a api.open-meteo.com NO sale del runner: **usar WebFetch**, `forecast_days=7`, un modelo por
  llamada (con muchas variables da timeout).
- **⭐ LA CONDICIÓN CONVERTIDA EN FECHA.** Una condición sin fecha («pasada la última helada», «cuando las yemas se
  hinchen») **no se ejecuta nunca**. Cantera abierta: B-9/B-18/B-4/B-41 yemas, F-3 brote rojo, B-12 «cuando moleste».
- **PEDIR LA OBSERVACIÓN EN VEZ DE AFIRMARLA.** `flowering` es rango de catálogo, no dato del jardín. **Declarar lo que NO
  sé suma.**
- **El título es el activo más medido:** sustantivo concreto + número + algo suyo + pérdida. · **Timing verificado >
  urgencia inventada.** · **feedback_text = ley.**

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero / diario / «El Parte»** · **cero-lectura / duelos binarios** · **checklist de viaje como deberes** ·
**vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app
pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística
· racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** · **era gimmick** (feed falso,
superpoderes) · **`podas-vuelta` CERRADA** · **NUEVO 06/09: contenido observacional suelto** («sacale foto a la flor»,
«decidí qué hacer con las 56 palmeras») — **pospuso las 8 de un saque. Va como pedido corto DENTRO de otra cosa, nunca
como card propia.**

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, 168 s @95 %, **😍 dos veces** y ticks por árbol horas después. n°2: 7/7, 166 s, cero
  reacción. n°3 (24/08): leído entero, sin veredicto.
- **Por qué gana:** ① sustancia técnica real sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla =
  una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Sus ticks (`taller-arbol-<code>`) NO escriben `task_states.json`.** Contar siempre con
  `generate_tasks_from_plants(PLANTS)` + `task_states.json`, **descartando las 16 huérfanas**. ⚠️ `pip install Pillow`.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo define la
  TAREA.**
- **La EXPOSICIÓN MEDIDA manda sobre la contabilidad del ledger:** si `scroll_pct` prueba que no llegó a esa card, está
  **fresca para él** aunque figure «featured». Sólo con evidencia medida, nunca por corazonada.
- ⚠️ **VEDADAS HASTA EL 13/09** (canal tarea de hoy, alta exposición): B-7, B-5a, B-23, B-25, B-12, B-15, B-8, B-4, B-1,
  B-29, F-2, F-7, B-43, B-22, B-36, F-3, B-41. **HASTA EL 12/09:** B-46, B-9, B-18, B-24, B-32, B-20, B-13, B-47.
- ✅ **LIBRES para el lunes 7 (la experiencia de las 18:00 sale de acá):** B-3, B-27, B-37, F-9, B-16, B-44, B-40, F-8,
  B-6, F-5, F-10, B-14, I-1, I-2, B-2, B-45, B-48, B-49, B-21, B-28, B-11, B-31, B-33, B-10, B-26, B-39, F-1.
  **B-34 sale de toda cantera: ya no existe.**
- **No repetir antes del 13/09:** «el portón» / el termómetro de 8 días · «la lluvia MEJORA estas 4» · el cepellón entero ·
  el quelato que baja con la lluvia · «florece en madera nueva» · **«un corte fresco + helada de amanecer»** (estrenado hoy).
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html` (sus
  botones escriben `task_states.json` vía `/api/tarea`; sus fotos y comentarios van al **thread**, los procesa
  `/responder-tareas`, **NO yo**). · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA).
- **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas). **No volver a pedir fotos generales.** Sin foto:
  B-41, B-32, B-43, B-46/47, B-2B, **B-22 y B-36**.
- **04/09 (baja):** B-34 eliminada con consentimiento explícito escrito. **NUNCA borrar una especie sin eso.**
- **05/09:** «No quiero tener que cambiar tokens nunca más». `api/sync.js` + `api/_gh.js` = backend de todas las escrituras;
  `tools/health_check.js` encola 1 push/día si el token muere. **Pendiente del usuario: pegar un PAT clásico sin
  vencimiento en Vercel. Mientras `GET /api/sync` dé 502, el silencio NO es desinterés: no puede guardar nada.**
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.

## 📈 Estado del sistema + jardín (06/09/2026)

- Push subscription `pix9`: **active**. `user_tasks.json`: **0 sin contestar** (los 7 viejos los cerró `/responder-tareas`
  el 05/09 — el backlog de mayo está saldado). `uploads.json`: 0 pendientes.
- ⚠️ **Threads con 3+1 mensajes suyos `pending`, son de `/responder-tareas`, NO míos:** **B-7 azarero** («Ahí lo pode
  fuerte», «Gran poda», «Lo MEGA PODE, muchísimo») y **B-41** («está igual que siempre, 0 floración»). **Los usé como
  contenido:** la card de B-7 encabeza la ed.4 con su cita y el botón para cerrarla, y la de B-41 pide el «antes».
- Proposals: **91** — 54 dropped / 23 promoted / **12 pending** / 1 approved / 1 removed. **Ninguna cambió de estado
  ayer** (`el-porton` sigue pending con nota: 0 señal, desplazada por las tareas).
- **51 especies · 101 tareas reales · 39 `active`** (52 done, 10 snoozed tras anoche), reverificado hoy contra
  `generate_tasks_from_plants` descartando las 16 huérfanas.
- **Compactación 06/09:** `send_log` 14 → 13 eventos (cayó el del 22/08). `engagement.json`: 54 eventos, **los del 24/08
  vencen mañana 07/09**; se agregó el `daily_summary` de 05/09 (4 sent · 2 clicked · 7 visits · **13 answers** · **2
  feedback_text**). `queue.json` limpio: sólo la entry de hoy.

## TODO / próximos experimentos

- **🎯 MARTES 8 — cobrar la apuesta del jueves.** Si llueve, **decirlo yo primero**: perdí media apuesta. Si no, cobrarla
  entera. Es el activo de credibilidad más barato que tengo.
- **🎯 LUNES 7 — la experiencia de las 18:00 sale del elenco libre.** NO repetir el portón. Y la push de tarea de las
  10:00 tiene que ser la **ventana de tijera del martes**, no una lista nueva.
- **12/09 y 19/09: vuelven las 8 que pospuso.** Traerlas ese día, agrupadas, no de a una.
- **`taller3-paltas` se reactiva la 2ª semana de septiembre** (B-22/B-36 ya están en la ed.4 con pedido de foto).
- **El censo cerró sin apertura desde el 31/08** → eje «recorrido de observación» **cerrado**, coherente con que ayer
  pospuso todo lo observacional.
- **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta (feb y may-sep) · **44 de 51 sin repuesto**
  (esquejes de septiembre, nunca como título alarmista) · la coronita F-5 · el fun_fact NASA de la cinta.
