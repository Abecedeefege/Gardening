# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## ✅ LO PRIMERO DEL 05/09 — ME PIDIÓ BORRAR UNA ESPECIE Y LA BORRÉ EL MISMO DÍA

El jueves 04/09 a las 16:04Z, desde la ficha de B-34: **«Esta planta la saqué. No existe más, podés eliminarla».**
Quedó 17 h sin respuesta (`/responder-tareas` no procesa `user_tasks.json`: hay **7 pedidos con `ai_answer: null`, el más
viejo del 07/05**). Ejecutado hoy: **B-34 fuera de `data_plants.py`**, su tarea de octubre cancelada, ficha archivada en
`data_bajas.py` (nuevo, no entra al build) por si se arrepiente. **Catálogo 52 → 51 especies; 50 tareas activas.**

- **Es el consentimiento explícito que la regla dura exige** — escrito por él, con código de planta. Sin eso, nunca.
- Se comunica arriba de todo en `jardin-hoy`, con la cita textual. **Contestar un pedido suyo es el contenido de más alto
  rendimiento que tengo.** Va con una pregunta de una tocada (`bajas-otras`): ¿quedó otra que ya no exista? Mandar tareas de
  plantas muertas es ruido que le hace desconfiar del resto del catálogo.
- ⚠️ **PENDIENTE REAL:** los otros 6 `ai_answer: null` de `user_tasks.json` (F-1 manchas negras, B-15, B-37 «¿podo con 100%
  humedad?» ×2, y 2 de mayo). **No son míos de escribir**, pero si `/responder-tareas` sigue sin tomarlos, avisarle: le
  quedaron preguntas sin contestar hace meses.

## 📊 EL 04/09 — 3 PUSH, CERO CLICKS. LA LECCIÓN NO ES OBVIA

Las 3 salieron 201. **Ninguna generó un `notification_clicked`.** La única visita del día (15:23:11Z, 9 s @28 %) fue
`src:"direct"` y **anterior** al primer envío (15:24:40Z).

- **No fue rechazo: fue redundancia.** Ese día estuvo dentro de la app subiendo 42 fotos: **cuando ya está adentro, la push
  compite con la sesión que ya está teniendo.** Y fueron 3 en un día sin slot, lo que la cadencia prohíbe.
- **Regla nueva:** si hay actividad del usuario en la última hora (`uploads.json`, threads, `engagement.json`), **no encolar
  nada ese día**.

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

| Día | Tarea 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Una sola push por slot de experiencia:** original NUEVA (el experimento) + las **aprobadas** de ese slot agrupadas
  DENTRO. **Aprobación = recurrencia:** sólo vuelve lo que prendió (😍 / slot «sí» / `engageApprove`); pending no se borra,
  no recurre. **Única aprobada: `el-taller` (n°1), en los dos slots.**
- Contrato de cada experiencia (back-link primero · reacción · slots · caja propia · aprobar/rechazar · pitch de 6 modelos ·
  `send_at` ≥60 min · `expires_at` 22:00 · `-03:00`): está en `.claude/commands/engagement.md` §4, no lo repito.
- **Canal tarea:** UNA push consolidada en `2026-07-24-jardin-hoy.html` (URL estable, **se REEDITA en su lugar**). NO correr
  `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano. `el-parte` perdió
con layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 % del scroll**, **medido renderizado en
Chromium 390×780** (nunca por offset de caracteres). Script en scratchpad (`audit.js`): playwright en
`/opt/node22/lib/node_modules`, `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Filtrar por
visibilidad real (`offsetParent`, `display`, rect ≠ 0) y limitar a `.wrap`. **Hoy: `el-porton` 14,2 % · `jardin-hoy` 31,8 %.**

**#3 EL LARGO TAMBIÉN ES LAYOUT.** Frenó en el 63 % de 29 cards. **Tope operativo: ~12 ítems por página** — hoy 6 y 4.
· **Quickbar** (18/08): **sin un evento medido** — buscar `via:"quickbar"`.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS

- **El problema era la ENTREGA, no el canal.** 10 envíos desde el 22/08, los 10 con `201`: **medir SIEMPRE `sent_at −
  send_at`, nunca el status code.**
- **⭐ LO QUE MÁS CONVIRTIÓ EN 6 SEMANAS NO FUE UNA EXPERIENCIA MÍA: fue una LISTA COMPLETA DE SUS TAREAS REALES, con foto de
  la especie, dónde está, y un botón por ítem.** Cero gimmick, cero narrativa. **Esa es la forma.**
- **La caja de feedback de texto es el control que más convierte del sitio** (2 de 2 el 24/08, 1 más el 03/09) — va en todas.
  Pero **las 3 veces que escribió fue de LOGÍSTICA, de identificación o de un pedido concreto, nunca de contenido**: sigo sin
  veredicto escrito sobre el Taller n°3 ni sobre el censo. **Sus mensajes son órdenes de trabajo, no reseñas. Tratarlos así.**
- **Dwell alto sin conversión ≠ éxito** (taller-3). **Leer entero es «masomenos», no un sí**; y **«no contestó» ≠ «no le
  interesa»** (03/09: 10 días de «silencio» y estaba entero). · **Lección más cara de agosto:** mandé una guía de ejecución
  a alguien que estaba fuera del país — **chequear que esté físicamente en el jardín antes.**

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, 168 s @95 %, **😍 dos veces** y **ticks por árbol** horas después. n°2: 7/7, 166 s, cero
  reacción. n°3 (24/08): leído entero, sin veredicto.
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre con la herramienta
  en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Sus ticks (`taller-arbol-<code>`) NO escriben `task_states.json`** — por eso B-30/B-38/F-4 figuraron `active` un mes.
  Contar siempre con `generate_tasks_from_plants(PLANTS)` + `task_states.json`, **descartando las 16 huérfanas**.
  ⚠️ **`pip install Pillow` primero.**

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero / diario / «El Parte»** (enterarse no es el valor, ayudarlo a HACER sí) · **cero-lectura / duelos binarios**
(«No es mi tipo») · **checklist de viaje como deberes** · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) ·
**mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un
plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol ·
**mucho texto/cargado** · **era gimmick** (feed falso, superpoderes: 9 s / 28 %) · **`podas-vuelta` CERRADA** (contestado).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Y **darle DÓNDE registrar lo que ya hizo** es casi tan fuerte: las 3 conversiones del
  03/09 fueron trabajo viejo, no trabajo nuevo. **Cerrar lo hecho es contenido.**
- **⭐ CUANDO NOMBRÉS UNA ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE.** Perdí una respuesta entera por nombrar sin mostrar.
  Corolario del 05/09: **cuando NO tengo foto suya, decirlo en la card y pedírsela** (B-22 y B-36 quedaron fuera de las 42).
- **⭐ EL CLIMA COMO EDITOR (03/09, abierta 159 s @100 %).** No «hay 17 tareas»: **el pronóstico ORDENA la lista y descarta lo
  que hoy sale peor.** Corolarios: **«hoy no salís» es contenido** si le doy la que SÍ se puede hacer; **la lluvia como
  recurso, no como estorbo** (05/09: «las 4 que la lluvia MEJORA» — trasplante con cepellón entero, quelato que baja solo).
- **⭐ ESTRENADO HOY — LA CONDICIÓN CONVERTIDA EN FECHA.** 6 tareas decían «pasada la última helada» y por eso llevaban meses
  quietas. Una condición sin fecha **no se ejecuta nunca**. Barrer el catálogo buscando más condiciones sin fecha
  («cuando las yemas se hinchen», «cuando el brote rojo vire a verde», «cuando moleste») es cantera pura.
- **⭐ PEDIR LA OBSERVACIÓN EN VEZ DE AFIRMARLA (31/08).** `flowering` es un rango de catálogo, no un dato del jardín.
  **Declarar lo que NO sé suma** (hoy: «un pronóstico ve 8 días, la última helada no la confirma nadie hasta que pasó»).
- **LA PREDICCIÓN / PROMESA VERIFICADA.** Cobrados: el viaje (24/08) y el silencio de la vuelta (31/08). **VIVA HOY:
  «del martes 8 al jueves 10 no llueve y no baja de 6°» — hay que cobrarla o admitirla el martes, sin que me la reclame.**
- **⚠️ EL NÚMERO SE VERIFICA SIEMPRE.** ⚠️ `curl` a api.open-meteo.com NO sale del runner: **usar WebFetch**. Hoy: **dos
  modelos cruzados (ECMWF + GFS)**; difieren hasta 2° en mínimas y muchísimo en máximas (mié: 14,1 vs 19,2) pero coinciden
  en lo único accionable. **Publicar el desacuerdo entre modelos es más creíble que publicar un número solo.**
- **El título es el activo más medido:** sustantivo concreto + número + algo suyo + pérdida. · **Timing verificado > urgencia
  inventada.** · **feedback_text = ley.** · Catálogo minado entero en `audit_flor_poda.json`; sin publicar: la coronita F-5.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción:** el canal tarea (jardin-hoy / taller / puesta-al-dia)
  es monotemático — su cast lo define la TAREA.
- **⭐ REGLA NUEVA (05/09): la EXPOSICIÓN MEDIDA manda sobre la contabilidad del ledger.** Las cards 19-29 de la
  puesta-al-día figuran «featured» pero él frenó en la 18: **quemadas para mí, frescas para él**. Se pueden reusar, pero
  **sólo con evidencia de `scroll_pct`**, nunca por corazonada. Registrado como excepción explícita en el ledger.
- ⚠️ **VEDADAS HASTA EL 12/09** (usadas hoy): B-5a/B-5b, B-46, B-25, B-23, B-29, B-24, B-1, B-22, B-36.
  **HASTA EL 10/09:** B-12/B-17, B-47, B-20, B-41, B-42. **HASTA EL 07/09:** F-4, B-30/B-35, B-38, B-39, B-32, B-13,
  B-10/B-19, B-26, F-7, B-7, B-9, B-18, F-2, B-43, B-15, B-4, F-3/F-3-2.
- ✅ **LIBRES para el lunes 7 (25):** B-3, B-27, F-1, B-37, F-9, B-8, B-16, B-44, B-40, F-8, B-6, F-5, F-10, B-14, I-1, I-2,
  B-2, B-45, B-48, B-49, B-21, B-28, B-11, B-31, B-33. **B-34 sale de toda cantera: ya no existe.**
- **No repetir antes del 12/09:** «el portón» / el termómetro de 8 días · «la lluvia MEJORA estas 4» · el cepellón entero con
  tierra mojada · el quelato que baja con la lluvia · el patrón del injerto que se come al árbol · «la fruta se hace donde
  entra el sol». **Antes del 10/09:** «la lluvia parte la lista en dos» · el balde de agua de lluvia · el bloque de honestidad
  de las 8 consultas · «florece en madera nueva» *(usado hoy en B-29 y B-1)*.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html` (04/07), `tareas-pendientes.html` (23/07),
  `puesta-al-dia.html` (03/09 — sus botones escriben `task_states.json` vía `/api/tarea`; sus fotos y comentarios van al
  **thread**, los procesa `/responder-tareas`, NO yo). · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07:** **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA).
- **04/09:** subió **42 fotos de especie** (`species-*_20260904-*.jpg`, `ai_status:"n/a"`: NO procesarlas como pendientes).
  **No volver a pedir fotos generales.** Sin foto: B-41, B-32, B-43, B-46/47, B-2B, **B-22 y B-36**. Datos duros: crespón B-9
  EN MACETA al borde del deck; althea B-18 en el césped al lado; hortensias brotadas; bignonia F-2 e hibisco B-4 sin podar;
  fotinias con el rojo recién asomando; lavanda en flor; limonero cargado.
- **04/09 (baja):** B-34 eliminada con consentimiento explícito. **NUNCA borrar una especie sin eso.**
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.

## 📈 Estado del sistema + jardín (05/09/2026)

- Push subscription `pix9`: **active**. Threads y `uploads.json`: **0 pendientes** (la única `pending` era la baja de B-34,
  resuelta hoy). `user_tasks.json`: **7 sin contestar** (ver arriba). Proposals: **91** — 54 dropped / 23 promoted /
  **12 pending** / 1 approved (`el-taller`) / 1 removed. **Ninguna cambió de estado** (sin `proposal_approved` ni `_rejected`).
- **51 especies · 50 tareas `active`** de 102 reales (50 done, 2 snoozed), reverificado contra `generate_tasks_from_plants`.
  ⚠️ 16 estados huérfanos: descartarlos siempre al contar. **16 activas vencen en septiembre.**
- **Compactación:** `send_log` NO vencía todavía (el evento del 22/08 es de las 14:18Z: cumple 14 días **mañana 06/09**);
  se agregaron los `daily_summary` de 03, 04 y 05/09 y se limpió `queue.json`. `engagement.json`: 23 eventos, los del
  24/08 **vencen el 07/09**.

## TODO / próximos experimentos

- **⏱️ HOY YA HAY DOS SLOTS PARA MEDIR EL FIX DE LAG** (13:00Z y 14:00Z): no esperar al lunes. Si `sent_at − send_at` sigue
  en decenas de minutos no es el scheduling — mirar el tiempo de job (checkout + `npm install` corren ANTES de mandar).
- **🎯 LUNES 7 — TRES COSAS QUE SE COBRAN SOLAS:** ① si contestó **sí** a `porton-aviso-mar8`, **encolar la push del martes 8
  a las 08:00** (excepción válida: la pidió él); ② **verificar la apuesta** (mar-jue sin lluvia, mínimas ≥6°) y decirlo yo
  primero, gane o pierda; ③ la experiencia del lunes 18:00 sale del elenco libre — **NO repetir el portón**.
- **El censo cierra el 07/09**: sigue sin apertura desde el 31/08 → cerrar el eje «recorrido de observación», no insistir.
- **`taller3-paltas` se reactiva la 2ª semana de septiembre.** Si contesta «corregila» → editar `prune_when` de B-22/B-36.
- **Cantera SIN USAR:** **condiciones sin fecha del catálogo** («cuando las yemas se hinchen» B-9/B-18/B-4/B-41, «cuando el
  brote rojo vire a verde» F-3, «cuando moleste» B-12) — el mismo truco del portón, aplicado a otro grupo · poda×fruta =
  feb y may-sep (B-24, B-41, B-8, F-8; ⚠️ B-23 NO: fruta 12 meses es simplificación de ficha) · **44 de 51 sin repuesto**
  (esquejes de septiembre, nunca como título alarmista) · coronita F-5 · **el fun_fact NASA de la cinta.**
