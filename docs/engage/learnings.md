# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🏆 LO PRIMERO DEL 04/09 — SE ROMPIÓ EL SILENCIO, Y GANÓ EL FORMATO QUE NO INVENTÉ YO

Doce días de cero se cortaron el **03/09**: abrió `jardin-hoy` (159 s @100 %) y esa misma noche la **`puesta-al-dia`**
produjo el mejor día medido desde el 02/08. **13,6 min de dwell (305 s@17 % + 514 s@63 %) — el más largo de toda la serie —
y 3 escrituras reales en `task_states.json`.**

- **Marcó las 3 primeras cards, en orden, 21 s entre una y otra** (B-30 · B-38 · F-4): **exactamente las 3 podas que ya había
  hecho el 02/08** y que vivían sólo como ticks del Taller. **Le faltaba el lugar donde escribirlo.**
- **De la card 4 en adelante no marcó ninguna, y frenó en el 63 % (card 18 de 29).** El formato ganó; **la LONGITUD perdió.**
  Lo hecho lo cerró en 42 s; lo pendiente no lo tocó a las 22 h de un jueves.
- ⚠️ **Corolario de elenco:** las cards **19-29 nunca las vio** (B-46-5, F-3/F-3-2, B-32, B-20, B-13, B-1, B-23, B-24, B-22,
  B-36, B-29). Igual que el censo: **quemadas para mí, frescas para él.**
- **Su único feedback de texto fue de identificación, no de contenido:** «no sé cuál es el crespón y la althea». Contestado
  con foto + ubicación en la puesta-al-día. **`podas-vuelta` queda CERRADA: no volver a preguntarlo.**

## ⏱️ EL LAG DE ENTREGA — MEDIDO Y ATACADO (era la tarea #1; queda cerrada)

**Serie: +263 min (31/08 10:00) · +59 (31/08 18:00) · +89 (03/09 10:00, ya con el cron desplazado) · +3,3 (`puesta-al-dia`,
disparada A MANO).** No era el minuto elegido: **GitHub difiere y descarta corridas cron bajo carga**, y 13:00Z es hora pico
(los slots de la tarde siempre llegaron mejor). **Fix puesto hoy en `push-dispatch.yml`:** ① cron cada 10 min en las horas
**previas** a los slots (12Z, 13Z, 20Z, 21Z) y ② paso **«Esperar al slot si esta inminente»** — el run que arranca hasta
**40 min** antes duerme hasta el minuto exacto en vez de mandar tarde. 7/7 casos de borde testeados. **Se mide el lunes 7.**

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

## 🚨 LAS DOS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano. `el-parte` perdió
con layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 % del scroll**, **medido renderizado en
Chromium 390×780** (nunca por offset de caracteres). Script en scratchpad (`audit.js`): playwright en
`/opt/node22/lib/node_modules`, `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Filtrar por
visibilidad real (`offsetParent`, `display`, rect ≠ 0) y limitar a `.wrap`. Todas compliant (7,9–21,8 %) salvo **el-parte
27,3 % (compliant y perdió igual)** y **preguntas-abiertas 75 % (único caso donde el layout SÍ explicó el resultado)**.
**⭐ REGLA HERMANA, ESTRENADA ANOCHE: el LARGO también es layout.** Frenó en el 63 % de 29 cards. **Tope operativo: ~12
ítems por página de lista.** · **Quickbar** (18/08): **sin un evento medido** — buscar `via:"quickbar"`.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS

- **El problema era la ENTREGA, no el canal.** 7 envíos desde el 22/08, los 7 con `201`: **medir SIEMPRE `sent_at −
  send_at`, nunca el status code.**
- **La caja de feedback de texto es el control que más convierte del sitio** (2 de 2 el 24/08, 1 más el 03/09) — va en todas.
  Pero **las 3 veces que escribió fue de LOGÍSTICA o de identificación, nunca de contenido**: sigo sin veredicto escrito
  sobre el Taller n°3 ni sobre el censo.
- **⭐ LO QUE MÁS CONVIRTIÓ EN 5 SEMANAS NO FUE UNA EXPERIENCIA MÍA: fue una LISTA COMPLETA DE SUS TAREAS REALES, con foto de
  la especie, dónde está, y un botón por ítem.** Cero gimmick, cero narrativa. **Esa es la forma.**
- **Lección más cara de agosto:** mandé una guía para ejecutar con la tijera en la mano a alguien que estaba fuera del país.
  **Antes de contenido de ejecución, chequear si hay señal de que esté físicamente en el jardín.**
- **Dwell alto sin conversión ≠ éxito** (taller-3). **Leer entero es «masomenos», no un sí**; y **«no contestó» ≠ «no le
  interesa»** — anoche lo probó: 10 días de «silencio» y estaba entero.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 dos veces**, feedback positivo y **ticks por árbol** horas después.
  n°2: 7/7 pasos, 166 s, cero reacción. n°3 (24/08): leído entero, sin veredicto.
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre con la herramienta
  en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Los ticks del Taller (`taller-arbol-<code>`) NO escriben `task_states.json`** — por eso B-30/B-38/F-4 figuraron `active`
  un mes entero, hasta que anoche él mismo los cerró. Contar siempre con `generate_tasks_from_plants(PLANTS)` +
  `task_states.json` (`{"tasks": {...}}`, **descartando las 15 huérfanas**). ⚠️ **`pip install Pillow` primero.**

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero / diario / «El Parte»** (31/07: 75 s, NO a los dos slots, meh — enterarse no es el valor, ayudarlo a HACER sí) ·
**cero-lectura / duelos binarios** (28/07: «No es mi tipo») · **checklist de viaje como deberes** · **vos-decidís** (el eje
AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers ·
mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak · biografías ·
dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (23/07) · **era gimmick** (feed falso, superpoderes): 16/08,
**9 s / 28 %**.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Y **darle DÓNDE registrar lo que ya hizo** es casi tan fuerte: las 3 conversiones de
  anoche fueron trabajo viejo, no trabajo nuevo. **Cerrar lo hecho es contenido.**
- **⭐ CUANDO NOMBRÉS UNA ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE.** Perdí una respuesta entera («no sé cuál es el crespón y la
  althea») por nombrar sin mostrar. Regla dura desde el 03/09.
- **⭐ EL CLIMA COMO EDITOR (03/09, abierta 159 s @100 %).** No «hay 17 tareas»: **el pronóstico ORDENA la lista y descarta lo
  que hoy sale peor.** Corolarios: **«hoy no salís» es contenido** si le doy la que SÍ se puede hacer; y **la lluvia como
  recurso, no como estorbo**.
- **⭐ PEDIR LA OBSERVACIÓN EN VEZ DE AFIRMARLA (31/08).** `flowering` es un rango de catálogo, no un dato del jardín.
  **Declarar lo que NO sé suma.**
- **LA PREDICCIÓN / PROMESA VERIFICADA.** Cobrados: el viaje (24/08) y el silencio de la vuelta (31/08) — **los dos ya se
  usaron.** Candidata fresca: el rebrote de B-43 en septiembre-octubre.
- **⚠️ EL NÚMERO SE VERIFICA SIEMPRE — 8 consultas al clima el 03/09** (el jueves osciló 12,1 → 4,4 → 12,7 y salió **12,7 mm
  reales**). ⚠️ `curl` a api.open-meteo.com NO sale del runner: **usar WebFetch**. **Publicar la volatilidad como bloque de
  honestidad ES contenido.** · **⚠️ ANOTADO ≠ VALIDADO:** computar antes de creerle a la cantera («luz real vs ficha» era
  falso). · Lo que gane señal medida va a `featured_experiences` de `build.py`.
- **La contradicción interna del catálogo es una mina — minada entera** (`audit_flor_poda.json`). **Sin publicar: sólo queda
  la coronita F-5.**
- **El título es el activo más medido:** sustantivo concreto + número + algo suyo + pérdida. · **Contestar un pedido suyo <
  12 h** es la forma más pura de la regla #1. · **Timing verificado > urgencia inventada.** · **feedback_text = ley.**

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Una decisión en learnings NO anula el ledger.** **Excepción:** el
  canal tarea (jardin-hoy / taller / puesta-al-dia) es monotemático — su cast lo define la TAREA.
- ⚠️ **VEDADOS HASTA EL 07/09:** F-4, B-30/B-35, B-38, B-39, B-32, B-13, B-10/B-19, B-26, B-23, B-24, F-7, B-7, B-5a, B-9,
  B-18, F-2, B-43, B-25, B-15, B-4, B-1, F-3/F-3-2. **HASTA EL 10/09:** B-12/B-17, B-46, B-47, B-29, B-20.
  **⚠️ NUEVOS HOY: B-41 y B-42** (los vio anoche en la card 6).
- ✅ **LIBRES para el sábado 5 (27):** B-3, B-27, F-1, B-37, F-9, B-8, B-16, B-44, B-34, B-40, F-8, B-6, F-5, F-10, B-14,
  I-1, I-2, B-2, B-45, B-48, B-49, B-21, B-28, B-11, B-31, B-33, B-5b.
- **No repetir antes del 10/09:** «la lluvia parte la lista en dos» · el punto de trasplante 24-48 h post-lluvia · el balde
  de agua de lluvia · «arrimar la hilera para que se sostengan entre ellas» · «florece en madera nueva → cortar fuerte suma
  flor» · el bloque de honestidad de las 8 consultas. **Antes del 07/09:** el corte a rama lateral de ⅓ · la forma en A · el
  tope del 40 % · las dos paltas · «7 de 7 slots» y «3 de 3 slots» · las 3 predicciones de los carozos.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. · **23/07:** `tareas-pendientes.html` = página fija, no borrar, no
  pushear suelta. · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07:** lechuga/huerta → entregado el 31 como bloque de septiembre. **Caqui B-41 → ignorar hasta primavera**
  (septiembre ya es primavera: se puede entrar, suave). · **PALTA:** los plantines siguen contra la pared a la sombra, **SIN
  MOVER** (B-22/B-36 es de PODA).
- **03/09:** pidió todo lo atrasado del viaje + la primera semana de septiembre, con especie/lugar visible y feedback
  individual. Entregado: **`puesta-al-dia.html` (página FIJA, no borrar, no re-pushear suelta)**. Sus botones escriben
  `task_states.json` vía `/api/tarea`; sus fotos/comentarios van al **thread** → los procesa `/responder-tareas`, NO yo.
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (04/09/2026)

- Push subscription `pix9`: **active**. Threads, `uploads.json`, `user_tasks.json`: **0 pendientes**. Proposals: **90** —
  54 dropped / 23 promoted / **11 pending** / 1 approved (`el-taller`) / 1 removed. **Ninguna cambió de estado hoy** (sin
  `proposal_approved` ni `proposal_rejected`).
- **48 tareas `active`** de 100 reales (49 done, 3 snoozed), reverificado contra `generate_tasks_from_plants` — **bajó de 51
  a 48 por las 3 que cerró anoche.** ⚠️ 15 estados huérfanos: descartarlos siempre al contar. **15 activas vencen en
  septiembre.**
- **Compactación: NO vence hoy.** `engagement` 21 eventos (los del 24/08 cumplen 14 días el **07/09**), `send_log` 7 eventos
  (el del 22/08 vence el **05/09** — mañana). `queue.json` limpiada: las 2 entries del 03/09 ya están en send_log.

## TODO / próximos experimentos

- **⏱️ LUNES 7: medir `sent_at − send_at` del slot de tarea.** Es la prueba del fix de hoy. Si sigue en decenas de minutos,
  el problema no es el scheduling: mirar el tiempo de job (checkout + `npm install` corren ANTES de mandar).
- **SÁB 5 (tarea 10:00 + experiencia 11:00):** la original nueva sale sí o sí. **La forma que ganó anoche es la que hay que
  copiar: lista de tareas reales, foto + ubicación por ítem, un botón por ítem — pero ~12 ítems, no 29.** ⚠️ No repetir
  vivero/palmeras ni las 18 cards que leyó anoche. Ángulo de respaldo: **el después del golpe de frío** (domingo 6 máx 8,3°,
  lunes 7 el único día limpio) → un Taller n°4 armado para ese lunes tiene timing verificado.
- **SÁB 5: compactar `send_log`** (vence el evento del 22/08).
- **`taller3-paltas` se reactiva la 2ª semana de septiembre**, cuando la tarea entra por calendario. Si contesta
  «corregila» → editar `prune_when` de B-22/B-36 en `data_plants.py` + `build.py`.
- **El censo cierra el 07/09**: si sigue sin apertura, se cierra el eje «recorrido de observación» y no se insiste.
- **Cantera SIN USAR:** «abre flor en septiembre» × «poda pendiente en septiembre» (B-22, B-36, B-23, B-24), desde el 07/09
  · poda×fruta = feb y may-sep (B-24, B-41, B-8, F-8; ⚠️ B-23 NO: fruta 12 meses es simplificación de ficha) · **44 de 52
  sin repuesto** (esquejes de septiembre, nunca como título alarmista) · coronita F-5 · **el fun_fact NASA de la cinta.**
