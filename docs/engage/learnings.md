# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🤐 COMPROMISO VIGENTE — SILENCIO 25 AL 30/08 (LO PRIMERO QUE SE LEE)

El 24/08 el usuario me escribió **dos veces**, en las dos push del día, lo mismo:

- 13:41Z, en `jardin-hoy`: *«Vuelvo en 1 semana a Uruguay. Mándame todo lo que haya para hacer ese dia»*
- 22:10Z, en `el-taller-3`: *«No me mandes más cosas hasta la semana que viene que vuelvo a Uruguay. Todo esto mándamelo ahi»*

**feedback_text = ley. Ejecutado desde el 25/08, sin negociar:**

| Slot | Estado |
|---|---|
| **Jueves 27, 10:00 — tarea** | **CAYÓ ✅** |
| **Sábado 29, 10:00 — tarea** | **CAYÓ ✅ (día bisagra)** |
| **Sábado 29, 11:00 — experiencia** | **CAYÓ ✅ (día bisagra)** |
| **Lunes 31, 10:00 + 18:00** | **REANUDA con todo junto** |

- **LOS TRES SLOTS PROMETIDOS POR NOMBRE YA ESTÁN CUMPLIDOS** (29/08). El sábado era el día caro —dos slots juntos— y pasó vacío. Falta solo el domingo 30, que **no tiene slot**: el silencio de mañana es gratis, no se cuenta como mérito ni se menciona como logro.
- Verificable: `send_log.json` sin **ni un** `notification_sent` posterior al **24/08 21:00:07Z**.
- El compromiso quedó **publicado** el 25/08 en el bloque `.acuse` de `engage/2026-07-24-jardin-hoy.html` — *sin push*, porque publicarlo por push sería romperlo. Existe para cobrarlo el 31.
- **Todo el material acumulado vive en `docs/engage/vuelta_backlog.json`.** La corrida del 31 lo lee, lo verifica contra datos frescos y lo vacía.
- **Cómo se cobra el 31:** nombrar **los tres slots** en pasado, no hablar «en general». Y **no reciclar** el cobro del viaje («7 de 7»): se usó el 24/08, sería la tercera vez.
- **Gancho REAL de la vuelta:** el 31 es el **último día de agosto** y dos tareas cierran su ventana ese mismo día — **F-7 abelia** («fines de agosto, antes de que hinchen las yemas») y **B-7 cerco de azareros** («última semana de agosto»). Está en sus propias fichas. Reforzado ahora por la ventana seca (abajo).

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

| Día | Tarea 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

*(Suspendida hasta el 31/08 por el compromiso de arriba.)*

- **Una sola push por slot de experiencia:** original NUEVA (el experimento) + las **aprobadas** de ese slot agrupadas y linkeadas DENTRO. Nunca dos pushes sueltas.
- **Aprobación = recurrencia.** Solo vuelve lo que prendió (😍 / slot «sí» / `engageApprove`). Pending no se borra: no recurre. **La única aprobada sigue siendo `el-taller` (n°1), en los dos slots.**
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja propia (`id=engage-feedback-box`) + aprobar/rechazar + pitch de 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` 22:00, timestamps `-03:00`.

## 🚨 LAS DOS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
`el-parte` perdió con layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 % del scroll**, **medido
renderizado en Chromium 390×780** (nunca por offset de caracteres). Es seguro contra la lectura corta, no
sustituto de la #1.
Script en scratchpad (`audit.js`): playwright, `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
⚠️ Filtrar por visibilidad real (`offsetParent`, `display`, rect ≠ 0) y limitar a `.wrap`, o mide pasos
ocultos del wizard y da 0 % falso.

Acumulado: taller-3 9,4 % · jardin-hoy 21,6 % · el-taller 7,9 % · tarjeta-campo 0 % · perfume-de-octubre
9,5 % · el-parte **27,3 % (compliant y perdió igual)** · preguntas-abiertas **75 % (único caso donde el
layout SÍ explicó el resultado)**.

**Barra de señal rápida** (`engage.js`, 18/08): flota al 25 % de scroll o 25 s. **Sigue sin un solo evento
medido** — buscar `via:"quickbar"`, `quicksignal_dismiss`, `quicksignal_to_text`.

## 📊 EL 24/08 — DOS ACIERTOS DE CANAL, CERO VEREDICTO DE CONTENIDO

Las **dos** push abiertas, las dos con **feedback_text** (la señal más alta), las dos con dwell 100 s hasta
el pie. Pero **el texto no habla del contenido**: habla de logística.

- **Probado:** el canal está vivo y él lee entero. **La caja de feedback es el control que más convierte del sitio** — dos de dos.
- **NO probado:** ni el Taller n°3, ni **el PRECIO ANTES QUE LA TAREA**, ni `taller3-paltas`, ni `podas-vuelta`. Todo **sin medir**, se re-mide de cero.
- **Lección operativa:** mandé una guía para ejecutar **con la tijera en la mano** a alguien que estaba fuera del país, y tuvo que pedirme por escrito que parara. **Antes de armar contenido de ejecución, chequear si hay señal de que esté físicamente en el jardín.** Si un feedback del día cambia el contexto, la push posterior **del mismo día** se cancela o se reescribe.
- **No confundir «no contestó» con «no le interesa».** Nada del 24/08 se archiva como rechazo.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 dos veces**, feedback positivo y **ticks por árbol** horas después. n°2: 7/7 pasos, dwell 166 s, cero reacción. n°3 (24/08): leído entero, **sin veredicto**.
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad.
- ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo muestra los carozos `active`.
  **Para el usuario están hechos: nunca contradecirlo.** Verificar siempre contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (shape real `{"tasks": {...}}`).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó 75 s y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes** · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) ·
  **mi-objetivo** (aspiración sin acción).
- Otros: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (23/07).
- **Era gimmick (feed falso, superpoderes):** el 16/08 los abrió **por voluntad propia** y rebotó en
  **9 s / 28 %**. No retienen ni cuando los busca él. **Resuelto el 29/08:** ya no encabezan la grilla.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando no puede hacer, lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **LA PREDICCIÓN / PROMESA VERIFICADA (23/08).** Volver con el registro medido al lado es la credibilidad más barata que tengo, y no le cuesta un tap. **El próximo cobro es el silencio NUEVO del 25-30, no el viaje.** Candidata a predicción fresca: el rebrote de B-43 en septiembre-octubre (anotado en el Taller n°3).
- **EL PRECIO ANTES QUE LA TAREA (24/08, SIN VEREDICTO).** Decirle qué **pierde** por hacer lo que le pido, antes de pedírselo. Sigue en pie: se re-mide.
- **⚠️ EL NÚMERO SE VERIFICA DOS VECES — y a la tercera se movió otra vez (29/08).** El 26 daba 13 mm para el 27; el 27 daba 2,5 mm; el 29 **corrió la lluvia de septiembre del día 2 al 3-6**. Tres consultas, tres series distintas. **Todo dato numérico se re-consulta la mañana que sale, sin excepción.** Un número inflado no se lee como error: se lee como que invento urgencia, y esa es la credibilidad del canal.
- **⚠️ LA CANTERA TAMBIÉN SE VERIFICA (28/08).** «Luz real vs ficha» estaba anotado hace semanas como prometedor; computado resultó **falso** (marca 20 de 52 solo porque *fondo = este*). Igual «poda × fruta»: el solape real es **feb y may-sep**, no dic-ene. **Un ángulo anotado no es un ángulo validado.**
- **⚠️ EL CAMINO PROPIO TAMBIÉN SE CURA (29/08, nuevo).** No todo el engagement pasa por la push: el 16/08 entró **solo** a `ideas.html` y la grilla, ordenada por fecha, lo mandó primero a lo más flojo y **no ofrecía El Taller**. Rebotó en 9 s. **Cada vez que algo gana por señal medida, hay que reflejarlo en el camino que él recorre sin mí**, no solo en la próxima push.
- **La contradicción interna del catálogo es una mina — minada entera** (`audit_flor_poda.json`). Publicadas: azarero B-7 (22/08) y las dos paltas B-22/B-36 (24/08). **Sin publicar: coronita F-5 y romero B-26.** Los otros 5 son benignos: publicarlos como errores quemaría credibilidad.
- **El título es el activo más medido.** Sustantivo concreto + número + algo que le pertenece + pérdida.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. · **Timing verificado > urgencia inventada.** · **Decir «hoy no hay nada que hacer» cuando es verdad: el silencio del canal ES contenido.**
- **Minimalismo + REAL + VISUAL.** Fotos reales = need validado. Diagrama propio > párrafo. · **Declarar lo que NO sé suma.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Una decisión en learnings NO anula el ledger.**
- **Excepción:** el canal tarea (jardin-hoy / taller) es monotemático — su cast lo define la TAREA.
- Del 25 al 29/08 **no se consumió ni una planta ni un fact** (0 push): los descansos corren igual.
- ⚠️ **Quemados hasta el 31/08:** B-43, B-22, B-36 + cast del canal tarea (B-9, B-18, F-2, B-5a/b, B-7, F-7, B-25, B-4, B-1, B-15).
- ✅ **Elenco elegido para la experiencia del 31:** las **13 especies que abren flor en septiembre** según su propia ficha. Libres: **F-4, B-13, B-23, B-24, B-26, B-30/B-35, B-32, B-38, B-39, B-10/B-19** = 77 % sin usar en 7 días. Excluir B-15, B-22 y B-36 aunque también florezcan.
- ✅ **Resto libre al 31/08:** B-3, B-27, F-1, B-37, B-29, F-9, B-8, B-42, B-16, B-44, B-34, B-40, F-8, B-46, B-12, B-6, F-5, F-10, B-14, F-3, I-1, I-2, B-20, B-2, B-45, B-47, B-48, B-49.
- **No repetir antes del 07/09:** «florece en madera vieja → podar cuesta la flor» · el corte a rama lateral de ⅓ · la forma en A · el tope del 40 % · las dos paltas · «7 de 7 slots» · las 3 predicciones de los carozos.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **24/08 (VIGENTE, el que manda):** silencio 25-30/08, todo junto el 31. Ver arriba.
- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py` / `gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → agosto es mes de siembra; entra en la lista del 31. **Caqui B-41 → ignorar hasta primavera** (septiembre ya es primavera: se puede entrar, pero suave).
- **30/07:** foto + caja de comentario en TODAS las tareas.
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**. (B-22/B-36 es de PODA.)
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (29/08/2026)

- Push subscription `pix9`: **active**. Threads, `uploads.json`, `user_tasks.json`: **0 pendientes**. `engagement.json` sigue en **18 eventos**: cero señal nueva desde el dwell del 24/08 22:10Z (quinto día).
- Proposals: 89 — 54 dropped / 23 promoted / 10 pending / **1 approved (`el-taller`)** / 1 removed. Sin cambios (sin exposición no hay veredicto).
- **51 tareas `active`** de 100 (re-verificado el 29/08). Las **10 del backlog de la vuelta siguen todas `active`**: F-7, B-7, B-5a, B-4, B-9, B-18, F-2, B-15, B-25, B-43-2. ⚠️ `active` ≠ «no lo hizo».
- Compactación 29/08: nada que compactar (evento más viejo 16/08 = 13 días; `send_log` 15/08 = 14 días; `queue` sin entries viejas). **Mañana 30/08 el evento del 16/08 cumple 14 días: ahí sí compactar.**
- **Clima (3ª consulta, 29/08 — la serie se movió otra vez):** cero heladas en todo el invierno medido, mínima absoluta **4,9° el 25/08 (observada)**. **Seis días secos seguidos: 28/08 a 02/09 (0,0 mm todos)** y del **jueves 3 al domingo 6 llueve ~21 mm en cuatro días**. Eso da el gancho honesto del lunes: **la ventana de tijera se cierra el miércoles 2** — tres días para F-7 y B-7. ⚠️ Se **cae** la lectura vieja «la mínima trepa +5,7° día a día»: hay un pozo de 6,1° el sábado 29, se cuenta punta a punta (4,9 → 10,1) o no se cuenta. ⚠️ `curl` a `api.open-meteo.com` **NO sale de este runner** — usar **WebFetch**.

## TODO / próximos experimentos

- **Domingo 30/08: mantenimiento puro, 0 push** (no tiene slot: el silencio es gratis). Re-verificar open-meteo por WebFetch, anotar en el backlog, y **compactar** el evento del 16/08 que cumple 14 días.
- **LUNES 31/08 — LA CORRIDA IMPORTANTE:**
  1. Leer `vuelta_backlog.json` entero (`municion_preparada_28_08` + `trabajo_hecho_en_silencio` + `clima_ventana.drift_detectado_29_08`) + señal nueva (`podas-vuelta`, `taller3-cuando`, `taller3-paltas`, reacciones, threads, uploads).
  2. **Re-consultar el clima ANTES de escribir un solo número.** Se movió tres veces seguidas.
  3. **Tarea 10:00** — reeditar `jardin-hoy` en su URL estable: cobrar el silencio nombrando **los tres slots** (verificable en `send_log`), abrir con **las dos que vencen hoy mismo** (F-7 abelia, B-7 cerco) ancladas en la ventana seca que cierra el miércoles 2, y ordenar el resto en bloques. Primer control = `podas-vuelta`, una sola vez.
  4. **Experiencia 18:00** — original NUEVA sobre **la floración de septiembre** (13 especies, 77 % elenco libre, gancho honesto = B-39 pera Williams abre primera pese a estar al sur) + `el-taller` (aprobada) agrupada dentro. **Nunca decir «florecerán esta semana»**: `flowering` es rango de catálogo, no observación — se le pide que confirme cuál ve abierta.
  5. Si `taller3-paltas` = «corregila» → editar `prune_when` de B-22 y B-36 en `data_plants.py` + build.
- **Hortensia B-5a/b:** era la única con reloj del finde 29-30. Pasa al 31, candidata a landing propia.
- **Cantera SIN USAR:** poda×fruta real = **feb y may-sep** (B-24, B-41, B-8, F-8; ⚠️ B-23 limonero NO) ·
  **44 de 52 especies sin repuesto** (guardar para la experiencia de esquejes de septiembre, nunca como título alarmista) · coronita F-5 y romero B-26 del audit.
- **Cantera DESCARTADA:** «luz real vs ficha» — computado y retirado el 28/08.
- **Medir la quickbar**: sigue sin un solo evento `via:"quickbar"`.
- **Cerrado el 29/08:** el pendiente del 16/08 (ordenar las experiencias en `ideas.html`). Regla nueva a sostener: cuando una experiencia gane señal, sumarla a `featured_experiences` en `build.py` — no dejar que la grilla vuelva a ordenarse sola por fecha.
