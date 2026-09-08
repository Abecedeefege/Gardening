# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🚨 LO PRIMERO DEL 08/09 — NO ERA EL CONTENIDO: EL CANAL ESTABA ENTREGANDO TARDE

Las 2 push del lunes volvieron **cero eventos**. Antes de tocar contenido medí el canal, y el canal estaba roto:
ed.6 `send_at` 13:00Z → `sent_at` **15:48:11Z (+168 min**, aterrizó 12:48 local, no 10:00); la-bandeja 21:00Z →
**22:15:10Z (+75 min**, 19:15 en vez de 18:00).

Medí las **19 corridas `schedule` reales del 05 al 07/09**: declaramos hasta 10 ticks/hora y GitHub ejecuta **uno cada
95 min de media, máximo 168, mínimo 21** — y **la primera corrida de cada día nunca cayó al abrir la ventana** (con el
cron abriendo 10:00Z, la primera efectiva fue **13:25Z · 13:38Z · 15:47Z**, siempre después del slot de las 13:00Z).
El paso «esperar al slot» existía con tope de 40 min: cubría 40/95 ≈ 42 % de los casos y ~0 % para las 10:00.

**Arreglado hoy** (`push-dispatch.yml`, lógica probada con 8 escenarios sintéticos, todos OK): ① ventana de cron **05Z**
en vez de 10Z → corre el pozo inicial hasta ~10:50Z; ② tope de espera **40 → 200 min** (> el gap máximo de 168) → el
primer tick de las 3 h previas se queda y entrega en el minuto exacto; ③ guarda nueva: **si ya hay algo vencido, manda
ya**. Repo público = minutos de runner gratis: la espera no cuesta nada y compra puntualidad.

⭐ **REGLA: antes de declarar muerto un contenido, verificar que haya llegado a horario.** Los tres slots leídos como
fracaso de contenido (31/08, 03/09, 07/09) tenían atraso medido de +263, +89 y +168 min.
⚠️ **Y el dato de ayer no está cerrado:** `engagement.json` flushea tarde — los eventos del 04/09 20:57 llegaron el
**07/09 08:34** (2,5 días). «Cero eventos» no prueba que no abrió. **Veredicto de la bandeja: jueves 10.**

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS (lo que llevo aprendido del canal)

- **⭐ LO QUE MÁS CONVIRTIÓ EN 7 SEMANAS: la lista de SUS tareas reales, con foto, dónde está y un botón por ítem.**
  El 05/09 lo confirmó de la forma más cara: con las 2 push de la mañana **no hizo nada**, y de noche estuvo 40 minutos
  dentro de `puesta-al-dia` resolviendo 10 tareas y escribiéndome 2 veces. Cero gimmick, cero narrativa.
- **⭐ CUANDO TIENE TRABAJO REAL PENDIENTE, LA EXPERIENCIA COMPITE Y PIERDE.** `el-portón` sigue en **0 absoluto** el
  mismo fin de semana que la página de tareas sumó 4 visitas. **No la rechazó: la desplazó.** ⭐ **Corolario: la
  experiencia no debe competir con la tarea, debe PARASITARLA.**
- **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO ESCRIBA**, y el tap es su idioma: 13 `answer` en una noche. **Posponer 8 en 90
  segundos es una edición** — todo `snoozed` se ejecuta en la reedición siguiente.
- **La caja de feedback de texto es el control que más convierte del sitio.** Va en todas. Pero **las 5 veces que
  escribió fue LOGÍSTICA, IDENTIFICACIÓN u ORDEN DE TRABAJO, jamás una reseña:** no esperes veredicto, esperá
  instrucciones y ejecutalas.
- **«Ocultar» no es «sacar»** (si pide achicar, se borra del archivo) · **dwell alto sin conversión ≠ éxito** ·
  **«no contestó» ≠ «no le interesa»** (03/09: 10 días de silencio y estaba entero) · **el 201 no mide nada: medir
  `sent_at − send_at`** · **chequear que esté físicamente en el jardín antes** (lección más cara de agosto) ·
  **nunca 3 push en un día sin slot** · **si hubo actividad suya en la última hora, no encolar.**

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

| Día | Tarea 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Excepción válida y única:** una push que **él pidió por escrito** (pasó el domingo 06/09). Se anota en el ledger.
- **Un día sin slot no es un día sin trabajo:** hoy (martes) reedité `puesta-al-dia` en su URL estable, sin push. La
  cadencia limita las **notificaciones**, no las **ediciones**.
- **Una sola push por slot de experiencia:** original NUEVA + las **aprobadas** de ese slot agrupadas DENTRO.
  **Aprobación = recurrencia:** sólo vuelve lo que prendió (😍 / slot «sí» / `engageApprove`); pending no se borra, no
  recurre. **Única aprobada: `el-taller` (n°1), en los dos slots.**
- Contrato de cada experiencia (back-link primero · reacción · slots · caja propia · aprobar/rechazar · pitch de 6
  modelos · `send_at` ≥60 min · `expires_at` 22:00 · `-03:00`): `.claude/commands/engagement.md` §4.
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). Script: `audit.js` en scratchpad — playwright en
`/opt/node22/lib/node_modules`, chromium en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
⚠️ **Corrección de método 08/09:** descartar `fixed`/`sticky` **mirando toda la cadena de ancestros** (la barra de señal
rápida de `engage.js` es fixed en un padre: medía siempre ~760 px y daba un **6,1 % falso**) y reportar el primer
control de **acción**, no el link del índice. **Hoy: `puesta-al-dia` ed.7 → 18,9 % · `la-bandeja` → 3,4 %.**

**#3 EL LARGO TAMBIÉN ES LAYOUT.** Tope operativo **~12 ítems**. `puesta-al-dia` sigue en 15 y sólo porque son tareas
suyas (las hechas ya están fuera del archivo). La ed.7 creció 12.222 → 12.464 px por la apuesta saldada: aceptado,
porque lo agregado es la corrección de mi propia guía.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA, ganada o perdida, ANTES de que él la revise.** Y se cobra **el día que
  vence**, no cuando toca push: hoy martes era el día, así que la saldé en la página aunque no hubiera notificación.
  **La mitad perdida vale más que la ganada:** es la prueba de que los números no están inflados para que haga click.
- **⭐ NUEVO 08/09 — CORREGIR MI PROPIA GUÍA CON EL DATO DE HOY ES CONTENIDO DE PRIMERA.** Ayer repartí los 8 cortes por
  día; hoy la mínima se movió y **di vuelta miércoles y jueves** (friolentas al jueves, la única mañana ≥6°; paltas al
  miércoles, el día más calmo). Un plan que se corrige solo con el número a la vista vale más que uno que finge no
  haberse equivocado. **Es el experimento a leer el jueves.**
- **⭐ LA EXPERIENCIA TIENE QUE SER UN OBJETO QUE SE LLENA, NO UN TEXTO CON UN BOTÓN AL FINAL.** Su señal más fuerte de 7
  semanas fue *tildar*, no leer. «La bandeja» es la primera experiencia cuyo cuerpo ES el control. **Sin veredicto aún.**
- **Ayudarlo a HACER > informarlo**, y **darle DÓNDE registrar lo que ya hizo** es casi igual de fuerte.
- **⭐ CUANDO NOMBRÉS UNA ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE** (03/09 perdí una respuesta entera por nombrar sin
  mostrar: «no sé cuál es el crespón y la althea»). Sin foto suya, decirlo en la card y pedírsela.
- **⭐ EL CLIMA COMO EDITOR.** No «hay 15 tareas»: el pronóstico **ordena y descarta**, con un día concreto por tarea,
  justificado por lo que aguanta cada planta. Y el viento es tan editor como la lluvia: el viernes 11 lo cerré por agua
  y se cierra por **ráfagas de 68 km/h con 0,0 mm**.
- **⭐ VERIFICAR MI PROPIO DATO ANTES DE PUBLICARLO** (07/09: iba a titular «44 de tus 51 sin repuesto» y son **42 de
  50**). **Un número que se cae solo cuesta más que el titular que gana.** · **⭐ LA CONDICIÓN CONVERTIDA EN FECHA:**
  cantera abierta en B-4/B-41 yemas, F-3 brote rojo, B-12 «cuando moleste». · **PEDIR LA OBSERVACIÓN EN VEZ DE
  AFIRMARLA** (`flowering` es rango de catálogo, no dato del jardín).
- **El título es el activo más medido:** sustantivo concreto + número + algo suyo + pérdida. · **Timing verificado >
  urgencia inventada.** · **feedback_text = ley.** · ⚠️ `curl` a api.open-meteo.com NO sale del runner: **usar WebFetch**,
  `forecast_days=7`, **un modelo por llamada**.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero / «El Parte»** · **cero-lectura / duelos binarios** · **checklist de viaje** · **vos-decidís** (el eje
AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers
· mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak ·
biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** · **era gimmick** · **`podas-vuelta` CERRADA**
· **contenido observacional suelto** («sacale foto a la flor») — pospuso las 8 de un saque: **va como pedido corto
DENTRO de otra cosa, nunca como card propia**.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, 168 s @95 %, **😍 dos veces** y ticks por árbol horas después. n°2: 7/7, 166 s, cero
  reacción. n°3 (24/08): leído entero, sin veredicto. **Por qué gana:** ① sustancia técnica real sobre SUS plantas
  ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Sus ticks (`taller-arbol-<code>`) NO escriben `task_states.json`.** Contar siempre con
  `generate_tasks_from_plants(PLANTS)` + `task_states.json`, **descartando las 16 huérfanas**. ⚠️ `pip install Pillow`.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo define
  la TAREA.**
- **La EXPOSICIÓN MEDIDA manda sobre la contabilidad del ledger:** si `scroll_pct` prueba que no llegó a esa card, está
  **fresca para él** aunque figure «featured». **Sólo con evidencia medida, nunca por corazonada** — y por eso hoy NO
  liberé el elenco de la bandeja pese a tener 0 visitas: con el flush atrasado, la evidencia no está cerrada.
- ⚠️ **VEDADAS HASTA EL 14/09** (bandeja, *a revisar el jueves 10*): I-1, I-2, B-6, B-26, B-2, B-10, B-3, F-5, B-27.
  **HASTA EL 13/09** (canal tarea): B-7, B-5a, B-23, B-25, B-12, B-15, B-8, B-4, B-1, B-29, F-2, F-7, B-43, B-22, B-36,
  F-3, B-41. **HASTA EL 12/09:** B-46, B-9, B-18, B-24, B-32, B-20, B-13, B-47.
- ✅ **LIBRES para el sábado 13/09 11:00:** B-16, B-37, F-9, B-44, B-40, F-8, F-10, B-14, B-45, B-48, B-49, B-21, B-28,
  B-11, B-31, B-33, B-39, F-1. **B-34 sale de toda cantera: ya no existe.**
- **No repetir antes del 21/09:** la propagación/esqueje entera · «lo que ibas a tirar» · el ejemplar único / sin
  repuesto · la campana de botella · el corte al ras bajo el nudo · el lado este como vivero · **el reparto de la
  ventana por día (ya usado dos veces: lunes y su corrección de hoy)**.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`
  (sus botones escriben `task_states.json` vía `/api/tarea`; sus fotos y comentarios van al **thread**, los procesa
  `/responder-tareas`, **NO yo**). Idem **Asamblea, tu-semana, vos-decidís, jardin-hoy** (promovidas) y **el-taller**
  (aprobada). · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA).
- **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas). **No volver a pedir fotos generales.** Sin foto:
  B-41, B-32, B-43, B-46/47, B-2B, B-22 y B-36. · **B-34 dada de baja con consentimiento escrito — NUNCA borrar una
  especie sin eso.**
- **05/09:** «No quiero tener que cambiar tokens nunca más». ✅ `GET /api/sync` verificado hoy: **200, `ok:true`**.
  `tools/health_check.js` sigue encolando 1 push/día si muere.

## 📈 Estado del sistema + jardín (08/09/2026)

- Push subscription `pix9` **active** · `/api/sync` **200 (`ok:true`)** · `user_tasks.json` 0 sin contestar ·
  `uploads.json` 0 pendientes · **threads 0 `pending`** · `task_states.json` **81 entries — 66 done, 11 snoozed, 4
  active**, última escritura suya **06/09 11:39Z** · proposals **92** (54 dropped / 23 promoted / 13 pending / 1
  approved / 1 removed).
- **Datos del 07/09 (lunes, los 2 slots):** 2 enviadas 201 · **0 clicks, 0 visitas, 0 ticks, 0 feedback** — con los dos
  atrasos medidos arriba y el flush pendiente. **No es un veredicto de contenido todavía.**
- **Compactación:** NO vencía hoy (evento más viejo de `engagement.json`: 03/09; de `send_log`: 31/08). Próxima: **17/09**.
- **Clima verificado hoy (ECMWF / GFS):** mar 8 **3,9/4,9°**, máx 15,3/16,2, 0,0/0,0 mm, ráfagas 30/21 · mié 9 4,8/7,0°,
  máx 18,1/18,9, 0,2/0,0 mm, **ráfagas 21/24 (el más calmo)** · jue 10 **7,8/9,2°**, 0,8/0,3 mm · vie 11 seco pero
  **ráfagas 68/41** · sáb 12 **5,8 mm** (ECMWF).

## TODO / próximos experimentos

- **🎯 JUEVES 10/09 — LA MEDICIÓN QUE MANDA: ¿entregó a horario?** Primer slot con el dispatcher corregido: comparar
  `sent_at` vs `send_at` ANTES de leer nada más. **Si sigue tarde, el problema no es el cron y hay que sacar la entrega
  de GitHub Actions** (cron de Vercel contra un endpoint propio; el bloqueo es que `VAPID_PRIVATE_KEY` tendría que
  existir como env var en Vercel — pedírselo dentro de una página).
- **🎯 JUEVES 10/09 — recién ahí, el veredicto de la bandeja** (ticks `bandeja-<code>`) y de la ed.7: con el flush de
  hasta 2,5 días hoy no alcanzaba. **≥3 tildados = el formato «objeto que se llena» se serializa.** Y **cobrar la
  corrección de hoy**: prometí que el jueves amanece 7,8-9,2°, el único día que cumple los 6°. Si falla, lo digo yo.
- **12/09 y 19/09: vuelven las 9 que pospuso.** Traerlas ese día, agrupadas, no de a una. El caqui B-41, el 27/09.
- **Semana 4 de la bandeja (≈05/10): recordarle qué mirar** — lo prometí en la tabla de la página. **Promesa con fecha.**
- **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta (feb y may-sep) · la coronita F-5 en octubre ·
  el fun_fact NASA de la cinta · el bálsamo del liquidámbar B-37.
