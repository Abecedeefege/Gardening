# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🤐 VENTANA DE SILENCIO 25-30/08 — **CERRADA Y CUMPLIDA ENTERA**

El 24/08 el usuario me escribió **dos veces**, en las dos push del día, lo mismo:

- 13:41Z, en `jardin-hoy`: *«Vuelvo en 1 semana a Uruguay. Mándame todo lo que haya para hacer ese dia»*
- 22:10Z, en `el-taller-3`: *«No me mandes más cosas hasta la semana que viene que vuelvo a Uruguay. Todo esto mándamelo ahi»*

**feedback_text = ley. Ejecutado del 25 al 30/08 sin negociar. Los TRES slots reales cayeron:**
jueves 27 10:00 · sábado 29 10:00 · sábado 29 11:00 (el sábado era el día caro: dos slots juntos).
**Verificable, y re-verificado el 30/08 DESPUÉS de compactar:** `send_log.json` no tiene **ni un**
`notification_sent` posterior al **24/08 21:00:07Z**.

- ⚠️ **El domingo 30 NO cuenta: no tiene slot por cadencia, fue gratis.** Cobrar sólo los tres slots reales,
  **nombrados en pasado**, no «en general». Y **no reciclar** el cobro del viaje («7 de 7»): se usó el 24/08.
- El compromiso quedó **publicado** el 25/08 en el bloque `.acuse` de `engage/2026-07-24-jardin-hoy.html`
  —sin push, porque anunciarlo por push sería romperlo. Existe para cobrarlo el 31.
- **Todo el material acumulado vive en `docs/engage/vuelta_backlog.json`.** La corrida del 31 lo lee,
  lo verifica contra datos frescos y lo vacía.
- **Gancho REAL de la vuelta:** el 31 es el **último día de agosto** y dos tareas cierran su ventana ese
  mismo día — **F-7 abelia** («fines de agosto, antes de que hinchen las yemas») y **B-7 cerco de azareros**
  («última semana de agosto»). Está en sus propias fichas, verificado el 30/08: las dos siguen `active`.

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

| Día | Tarea 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

*(Se reanuda el 31/08. La suspensión terminó.)*

- **Una sola push por slot de experiencia:** original NUEVA (el experimento) + las **aprobadas** de ese slot
  agrupadas y linkeadas DENTRO. Nunca dos pushes sueltas. **Aprobación = recurrencia:** sólo vuelve lo que
  prendió (😍 / slot «sí» / `engageApprove`); pending no se borra, no recurre. **La única aprobada sigue
  siendo `el-taller` (n°1), en los dos slots.**
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + slots (`<slug>-slot-lun18` /
  `<slug>-slot-sab11`) + caja propia (`id=engage-feedback-box`) + aprobar/rechazar + pitch de 6 modelos.
  `send_at` ≥60 min post-corrida, `expires_at` 22:00, timestamps `-03:00`.

## 🚨 LAS DOS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
`el-parte` perdió con layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 % del scroll**, **medido
renderizado en Chromium 390×780** (nunca por offset de caracteres). Es seguro contra la lectura corta, no
sustituto de la #1. Script en scratchpad (`audit.js`): playwright,
`executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Filtrar por visibilidad real
(`offsetParent`, `display`, rect ≠ 0) y limitar a `.wrap`, o mide pasos ocultos del wizard y da 0 % falso.
Acumulado: taller-3 9,4 % · jardin-hoy 21,6 % · el-taller 7,9 % · tarjeta-campo 0 % · perfume-de-octubre
9,5 % · el-parte **27,3 % (compliant y perdió igual)** · preguntas-abiertas **75 % (único caso donde el
layout SÍ explicó el resultado)**. · **Quickbar** (`engage.js`, 18/08, flota al 25 % de scroll o 25 s):
**sigue sin un solo evento medido** — buscar `via:"quickbar"`, `quicksignal_dismiss`, `quicksignal_to_text`.

## 📊 EL 24/08 — DOS ACIERTOS DE CANAL, CERO VEREDICTO DE CONTENIDO

Las **dos** push abiertas, las dos con **feedback_text** (la señal más alta), dwell 100 s hasta el pie. Pero
**el texto no habla del contenido**: habla de logística.

- **Probado:** el canal está vivo y él lee entero. **La caja de feedback es el control que más convierte del sitio** — dos de dos.
- **NO probado:** ni el Taller n°3, ni **el PRECIO ANTES QUE LA TAREA**, ni `taller3-paltas`, ni `podas-vuelta`. Se re-miden de cero.
- **Lección operativa:** mandé una guía para ejecutar **con la tijera en la mano** a alguien que estaba fuera del país, y tuvo que pedirme por escrito que parara. **Antes de armar contenido de ejecución, chequear si hay señal de que esté físicamente en el jardín.** Si un feedback del día cambia el contexto, la push posterior **del mismo día** se cancela o se reescribe.
- **No confundir «no contestó» con «no le interesa».** Nada del 24/08 se archiva como rechazo.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 dos veces**, feedback positivo y **ticks por árbol** horas después. n°2: 7/7 pasos, dwell 166 s, cero reacción. n°3 (24/08): leído entero, **sin veredicto**.
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad.
- ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo muestra los carozos `active`.
  **Para el usuario están hechos: nunca contradecirlo.** Verificar siempre contra
  `generate_tasks_from_plants(PLANTS)` + `task_states.json` (shape real `{"tasks": {...}}`).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó 75 s y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes** · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) ·
  **mi-objetivo** (aspiración sin acción) · role-play verboso · countdown · app pasiva · editorial 3ª pers ·
  mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak ·
  biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (23/07).
- **Era gimmick (feed falso, superpoderes):** el 16/08 los abrió **por voluntad propia** y rebotó en
  **9 s / 28 %**. No retienen ni cuando los busca él. **Resuelto el 29/08:** ya no encabezan la grilla.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando no puede hacer, lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **LA PREDICCIÓN / PROMESA VERIFICADA (23/08).** Volver con el registro medido al lado es la credibilidad más barata que tengo, y no le cuesta un tap. **El próximo cobro es el silencio NUEVO del 25-30, no el viaje.** Candidata fresca: el rebrote de B-43 en septiembre-octubre (anotado en el Taller n°3).
- **EL PRECIO ANTES QUE LA TAREA (24/08, SIN VEREDICTO).** Decirle qué **pierde** por hacer lo que le pido, antes de pedírselo. Sigue en pie: se re-mide.
- **⚠️ EL NÚMERO SE VERIFICA SIEMPRE — CUATRO CONSULTAS, CUATRO DRIFTS (30/08).** El 26 daba 13 mm para el 27;
  el 27 daba 2,5 mm; el 29 corrió la lluvia de septiembre del día 2 al 3-6; **el 30 la volvió a traer al día 2
  y disolvió el temporal**. Esto ya no es precaución teórica: **si el lunes salía con la serie del 29 publicaba
  «tres días de tijera» cuando son DOS.** Un número inflado no se lee como error: se lee como que invento
  urgencia, y esa es la credibilidad del canal. **Todo dato numérico se re-consulta la mañana que sale.**
  *Lo único estable en las 4 series: cero heladas y mínima absoluta 4,9° del 25/08 — y es OBSERVADO.*
- **⚠️ LA CANTERA TAMBIÉN SE VERIFICA (28/08).** «Luz real vs ficha» estaba anotado como prometedor; computado resultó **falso** (marca 20 de 52 sólo porque *fondo = este*). Igual «poda × fruta»: el solape real es **feb y may-sep**, no dic-ene. **Un ángulo anotado no es un ángulo validado.**
- **⚠️ EL CAMINO PROPIO TAMBIÉN SE CURA (29/08).** No todo el engagement pasa por la push: el 16/08 entró **solo** a `ideas.html` y la grilla, ordenada por fecha, lo mandó primero a lo más flojo y **no ofrecía El Taller**. Rebotó en 9 s. **Cada vez que algo gana por señal medida, reflejarlo en el camino que él recorre sin mí**, no sólo en la próxima push.
- **La contradicción interna del catálogo es una mina — minada entera** (`audit_flor_poda.json`). Publicadas: azarero B-7 (22/08) y las dos paltas B-22/B-36 (24/08). **Sin publicar: coronita F-5 y romero B-26.** Los otros 5 son benignos: publicarlos como errores quemaría credibilidad.
- **El título es el activo más medido.** Sustantivo concreto + número + algo que le pertenece + pérdida.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. · **Timing verificado > urgencia inventada.** · **Decir «hoy no hay nada que hacer» cuando es verdad: el silencio del canal ES contenido.** · **Minimalismo + REAL + VISUAL:** fotos reales = need validado, diagrama propio > párrafo, y **declarar lo que NO sé suma**.
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Una decisión en learnings NO anula el ledger.**
- **Excepción:** el canal tarea (jardin-hoy / taller) es monotemático — su cast lo define la TAREA.
- Del 25 al 30/08 **no se consumió ni una planta ni un fact** (0 push): los descansos corrieron igual.
- ⚠️ **Quemados hasta el 31/08:** B-43, B-22, B-36 + cast del canal tarea (B-9, B-18, F-2, B-5a/b, B-7, F-7, B-25, B-4, B-1, B-15).
- ✅ **Elenco del 31 — RE-COMPUTADO Y VERIFICADO el 30/08** contra `data_plants.py` (`flowering` incluye 9):
  son **13 especies**. Excluyendo B-15 (canal tarea), B-22 y B-36 (quemadas) quedan **10 libres = 77 %**:
  **F-4, B-10/B-19, B-13, B-23, B-24, B-26, B-30/B-35, B-32, B-38, B-39.**
  **Dos hechos estructurales NUEVOS que salieron del cómputo** (los dos verificables en las fichas):
  ① **F-4 es la ÚNICA del frente; las otras 12 están todas en el fondo** — la primavera de este jardín
  arranca casi entera del lado del sol de la mañana. ② **Cinco ya vienen abriendo desde agosto**
  (F-4, B-30/B-35, B-32, B-38, B-39 = `flowering [8,9]`) y **ocho arrancan recién en septiembre** → se le
  puede pedir que **confirme cuál ve abierta** en vez de afirmarlo yo.
- ✅ **Resto libre al 31/08:** B-3, B-27, F-1, B-37, B-29, F-9, B-8, B-42, B-16, B-44, B-34, B-40, F-8, B-46, B-12, B-6, F-5, F-10, B-14, F-3, I-1, I-2, B-20, B-2, B-45, B-47, B-48, B-49.
- **No repetir antes del 07/09:** «florece en madera vieja → podar cuesta la flor» · el corte a rama lateral de ⅓ · la forma en A · el tope del 40 % · las dos paltas · «7 de 7 slots» · las 3 predicciones de los carozos.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **24/08 (CUMPLIDO 30/08):** silencio 25-30/08, todo junto el 31. La entrega es mañana.
- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py` / `gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta. · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07:** lechuga/huerta → agosto es mes de siembra; entra en la lista del 31. **Caqui B-41 → ignorar hasta primavera** (septiembre ya es primavera: se puede entrar, pero suave).
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**. (B-22/B-36 es de PODA.)
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (30/08/2026)

- Push subscription `pix9`: **active**. Threads, `uploads.json`, `user_tasks.json`: **0 pendientes**.
  `engagement.json`: **cero señal nueva desde el 24/08 22:10Z (sexto día)** — esperable, estaba de viaje.
  Proposals: 89 — 54 dropped / 23 promoted / 10 pending / **1 approved (`el-taller`)** / 1 removed. Sin
  cambios: sin exposición no hay veredicto.
- **51 tareas `active`** de 100 (re-verificado el 30/08). Las **10 del backlog de la vuelta siguen todas
  `active`**: F-7, B-7, B-5a, B-4, B-9, B-18, F-2, B-15, B-25, B-43-2. ⚠️ `active` ≠ «no lo hizo».
- **Compactación 30/08 EJECUTADA** (vencía hoy): `engagement.json` 18 → **12** eventos (los 6 del 16/08
  cumplieron 14 días, resumidos en `daily_summary`); `send_log.json` 5 → **4** (el del 15/08). La prueba del
  silencio sobrevivió: último `notification_sent` sigue siendo 24/08 21:00:07Z.
- **Clima (4ª consulta, 30/08 — cambió el gancho del lunes):** cero heladas en todo el invierno medido,
  mínima absoluta **4,9° el 25/08 (observada, estable en las 4 series)**. **La ventana de tijera de la vuelta
  son DOS días, no tres: lunes 31 (0,0 mm) y martes 1/09 (0,2 mm); el miércoles 2 llueve 5,7 mm.** Se cae el
  «temporal de ~21 mm del 3 al 6» (ahora ~5,1 mm flojos) y se cae «la semana más fría viene después» (las
  máximas del 5-6/09 subieron a 11,8° y 10,7°). ⚠️ `curl` a `api.open-meteo.com` **NO sale de este runner** —
  usar **WebFetch**.

## TODO / próximos experimentos

- **LUNES 31/08 — LA CORRIDA IMPORTANTE (se reanuda la cadencia: tarea 10:00 + experiencia 18:00):**
  1. Leer `vuelta_backlog.json` entero (`municion_preparada_28_08` + `trabajo_hecho_en_silencio` +
     `clima_ventana.drift_detectado_30_08` + `cast_septiembre_verificado_30_08`) + señal nueva
     (`podas-vuelta`, `taller3-cuando`, `taller3-paltas`, reacciones, threads, uploads).
  2. **QUINTA consulta de clima ANTES de escribir un solo número.** Se movió las 4 veces. No es opcional.
  3. **Tarea 10:00** — reeditar `jardin-hoy` en su URL estable: cobrar el silencio nombrando **los tres slots**
     (verificable en `send_log`, el domingo NO cuenta), abrir con **las dos que vencen hoy mismo** (F-7 abelia,
     B-7 cerco) ancladas en la ventana seca **de dos días** que cierra el martes, y ordenar el resto en bloques.
     Primer control = `podas-vuelta`, una sola vez.
  4. **Experiencia 18:00** — original NUEVA sobre **la floración de septiembre** (13 especies, 77 % elenco
     libre) + `el-taller` (aprobada) agrupada dentro. Gancho honesto: **F-4 es la única del frente, las otras
     12 están en el fondo**, y **5 ya vienen abriendo desde agosto**. **Nunca decir «florecerán esta semana»**:
     `flowering` es rango de catálogo, no observación — se le pide que confirme cuál ve abierta.
  5. Si `taller3-paltas` = «corregila» → editar `prune_when` de B-22/B-36 en `data_plants.py` + build.
     Y **vaciar `vuelta_backlog.json`** una vez entregado.
- **Hortensia B-5a/b:** era la única con reloj del finde 29-30. Pasa al 31, candidata a landing propia.
- **Cantera SIN USAR:** el solape **«abre flor en septiembre» × «tiene poda pendiente en septiembre»**
  (B-22, B-36, B-23, B-24) — mina real pero **bloqueada hasta el 07/09** porque «florece en madera vieja»
  está quemado · poda×fruta real = **feb y may-sep** (B-24, B-41, B-8, F-8; ⚠️ B-23 limonero NO) ·
  **44 de 52 especies sin repuesto** (para la experiencia de esquejes de septiembre, nunca como título
  alarmista) · coronita F-5 y romero B-26 del audit. **DESCARTADA:** «luz real vs ficha» (retirada el 28/08).
- **Regla viva desde el 29/08:** cuando una experiencia gane señal, sumarla a `featured_experiences` en
  `build.py` — no dejar que la grilla de `ideas.html` vuelva a ordenarse sola por fecha.
