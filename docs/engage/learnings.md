# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🤐 COMPROMISO VIGENTE — SILENCIO 25 AL 30/08 (LO PRIMERO QUE SE LEE)

El 24/08 el usuario me escribió **dos veces**, en las dos push del día, lo mismo:

- 13:41Z, en `jardin-hoy`: *«Vuelvo en 1 semana a Uruguay. Mándame todo lo que haya para hacer ese dia»*
- 22:10Z, en `el-taller-3`: *«No me mandes más cosas hasta la semana que viene que vuelvo a Uruguay. Todo esto mándamelo ahi»*

**feedback_text = ley. Ejecutado el 25/08, sin negociar:**

| Slot | Estado |
|---|---|
| Jueves 27, 10:00 — tarea | **CAE** |
| Sábado 29, 10:00 — tarea | **CAE** |
| Sábado 29, 11:00 — experiencia | **CAE** |
| **Lunes 31, 10:00 + 18:00** | **REANUDA con todo junto** |

- **Las corridas del 26, 27, 28, 29 y 30 son mantenimiento puro: 0 push, sin excepción.** Ni «una chiquita», ni recuperar un slot antes. Romper esto quema el activo entero.
- El compromiso quedó **publicado** el 25/08 en el bloque `.acuse` de `engage/2026-07-24-jardin-hoy.html` — *sin push*, porque publicarlo por push sería romperlo. Existe para cobrarlo el 31.
- **Todo el material acumulado vive en `docs/engage/vuelta_backlog.json`.** La corrida del 31/08 lo lee, lo verifica contra datos frescos y lo vacía.
- **Cómo se cobra el 31** (mismo patrón que el viaje, que funcionó): verificable contra `send_log.json` — entre el 25 y el 30 no debe haber **ni un** `notification_sent`. Nombrar los tres slots, no hablar «en general». Y **no reciclar** el cobro del viaje («7 de 7»): eso ya se usó el 24/08, sería la tercera vez.
- **Gancho REAL de la vuelta, sin urgencia inventada:** el 31 es el **último día de agosto** y dos tareas cierran su ventana ese mismo día — **F-7 abelia** («fines de agosto, antes de que hinchen las yemas») y **B-7 cerco de azareros** («última semana de agosto»). Volvió justo a tiempo. Es verdad y está en sus propias fichas.

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

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano. `el-parte` perdió con layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 % del scroll**, **medido renderizado en Chromium 390×780** (nunca por offset de caracteres). Es seguro contra la lectura corta, no sustituto de la #1.
Script en scratchpad (`audit.js`): playwright, `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Filtrar por visibilidad real (`offsetParent`, `display`, rect ≠ 0) y limitar a `.wrap`, o mide pasos ocultos del wizard y da 0 % falso.

Acumulado: taller-3 9,4 % · jardin-hoy 21,6 % · el-taller 7,9 % · tarjeta-campo 0 % · perfume-de-octubre 9,5 % · el-parte **27,3 % (compliant y perdió igual)** · preguntas-abiertas **75 % (único caso donde el layout SÍ explicó el resultado)**.

**Barra de señal rápida** (`engage.js`, 18/08): flota al 25 % de scroll o 25 s. **Sigue sin un solo evento medido** — buscar `via:"quickbar"`, `quicksignal_dismiss`, `quicksignal_to_text`.

## 📊 EL 24/08 — DOS ACIERTOS DE CANAL, CERO VEREDICTO DE CONTENIDO

Las **dos** push abiertas, las dos con **feedback_text** (la señal más alta de la escala), las dos con dwell 100 s hasta el pie. Pero **el texto no habla del contenido**: habla de logística.

- **Lo que sí quedó probado:** el canal está vivo y él lee entero. Después de 17 días de viaje abrió las dos push del mismo día y se tomó el trabajo de escribir dos veces. **La caja de feedback es el control que más convierte del sitio** — dos de dos.
- **Lo que NO quedó probado:** ni el Taller n°3, ni **el PRECIO ANTES QUE LA TAREA** (hipótesis nueva del 24/08), ni `taller3-paltas` (delegarme trabajo), ni `podas-vuelta`. Todo eso sigue **sin medir**, y se re-mide de cero.
- **Lección operativa nueva:** mandé una guía para ejecutar **con la tijera en la mano** a alguien que estaba fuera del país, y él tuvo que pedirme por escrito que parara. **Antes de armar contenido de ejecución, chequear si hay señal de que el usuario esté físicamente en el jardín.** El feedback del 13:41 ya lo decía y la push de las 18:00 salió igual: eso no se repite. Si un feedback del día cambia el contexto, la push posterior **del mismo día** se cancela o se reescribe.
- **No confundir «no contestó» con «no le interesa».** Nada del 24/08 se archiva como rechazo.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 dos veces**, feedback positivo y **ticks por árbol** horas después. n°2: 7/7 pasos, dwell 166 s, cero reacción. n°3 (24/08): leído entero, **sin veredicto** (ver arriba).
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad.
- ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo muestra los carozos `active`. **Para el usuario están hechos: nunca contradecirlo.** Verificar siempre contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (shape real `{"tasks": {...}}`).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó 75 s y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes** · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** (aspiración sin acción).
- Otros: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (23/07).
- **Era gimmick (feed falso, superpoderes):** el 16/08 los abrió **por voluntad propia** y rebotó en **9 s / 28 %**. No retienen ni cuando los busca él.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando no puede hacer, lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **LA PREDICCIÓN / PROMESA VERIFICADA (23/08).** Guardar lo que dije y volver con el registro medido al lado es la credibilidad más barata que tengo, y no le cuesta un tap. **Se cobró dos veces con el viaje: el próximo cobro tiene que ser el silencio NUEVO del 25-30, no aquel.** Candidata a predicción fresca: el rebrote de B-43 en septiembre-octubre (ya anotado dentro del Taller n°3).
- **EL PRECIO ANTES QUE LA TAREA (24/08, SIN VEREDICTO).** Decirle qué **pierde** por hacer lo que le pido, antes de pedírselo. Sigue en pie como hipótesis: se re-mide.
- **La contradicción interna del catálogo es una mina — minada entera** (`audit_flor_poda.json`). Publicadas: azarero B-7 (22/08) y las dos paltas B-22/B-36 (24/08). **Sin publicar: coronita F-5 y romero B-26.** Los otros 5 son benignos: publicarlos como errores quemaría credibilidad.
- **El título es el activo más medido.** Sustantivo concreto + número + algo que le pertenece + pérdida.
- **El dato computado sobre su propio catálogo es munición.** Usados: floración · fruta · acción→floración · campos «a confirmar» · poda×floración. **Sin usar: poda×FRUTA (dic-ene) · dependencia de un solo ejemplar (44/52) · luz real vs la que pide cada ficha · calendario de perfume aplicado a PLANTAR.**
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. · **Timing verificado > urgencia inventada.**
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal ES contenido.
- **Minimalismo + REAL + VISUAL.** Fotos reales = need validado. Diagrama propio > párrafo. · **Declarar lo que NO sé suma.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Una decisión en learnings NO anula el ledger: el ledger gana.**
- **Excepción:** el canal tarea (jardin-hoy / taller) es monotemático — su cast lo define la TAREA, no el elenco.
- El 25/08 **no se consumió ni una planta ni un fact** (0 push): los descansos corren igual.
- ⚠️ **Quemados hasta el 31/08:** B-43, B-22, B-36 + cast del canal tarea (B-9, B-18, F-2, B-5a/b, B-7, F-7, B-25, B-4, B-1, B-15).
- ✅ **Libres al 31/08:** B-11/B-31/B-33, B-3, B-10/B-19, B-27, B-23, F-1, B-26, B-37, B-29, F-9 + pindó B-8, pata de vaca B-42, anacahuita B-16, evónimo B-44, mandioca B-34, madreselva B-40, aguaribay F-8, vivero B-46, cinta B-12, esparraguera B-6, coronita F-5, fresno F-10, mandarina B-24, lapachillo B-14, viraró B-32, fotinia F-3, I-1, I-2, B-13, B-20, B-2, B-45, B-47, B-48, B-49.
  *(Ojo: B-7/B-11/B-31/B-33 son el mismo cerco. El 31 entra por «la ventana que se cierra», no como hallazgo del audit.)*
- **No repetir antes del 07/09:** «florece en madera vieja → podar cuesta la flor» · el corte a rama lateral de ⅓ · la forma en A · el tope del 40 % · las dos paltas · «7 de 7 slots» · las 3 predicciones verificadas de los carozos.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **24/08 (VIGENTE, el que manda):** silencio 25-30/08, todo junto el 31. Ver arriba.
- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py` / `gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → agosto es mes de siembra (lechuga y tomate a cubierto); entra en la lista del 31. **Caqui B-41 → ignorar hasta primavera.**
- **30/07:** foto + caja de comentario en TODAS las tareas.
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**. (Lo de B-22/B-36 es de PODA, no de mudanza.)
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (25/08/2026)

- Push subscription `pix9`: **active**. Threads, `uploads.json`, `user_tasks.json`: **0 pendientes**.
- **51 tareas `active`** en `generate_tasks_from_plants` + `task_states.json`; el subconjunto con ventana en agosto/principios de septiembre es el que importa y está desglosado en `vuelta_backlog.json`.
- Jardín en dormancia, **saliendo**. **~27 días al equinoccio.** Cero heladas en los 21 días medidos (mínima absoluta 6,9° el 8/08). **El parte del 24/08 ya no es publicable** (regla de las 72 h): re-verificar open-meteo la mañana del 31.
- Compactación 25/08: `send_log` → quedan 5 eventos, el del 10/08 pasó a `daily_summary`. `engagement.json` → 18 eventos, todos <14 días, se agregaron los resúmenes del 24 y 25. `queue.json` → reescrita vacía con el compromiso documentado.

## TODO / próximos experimentos

- **26, 27, 28, 29 y 30/08: mantenimiento puro, 0 push.** Lo único que se hace es leer si llegó señal nueva y actualizar `vuelta_backlog.json`. **No encolar nada, pase lo que pase.**
- **Miércoles 26 y domingo 30:** re-verificar open-meteo y anotar en el backlog (el número del 31 tiene que ser fresco de esa mañana igual, pero conviene ver la tendencia).
- **LUNES 31/08 — LA CORRIDA IMPORTANTE:**
  1. Leer `vuelta_backlog.json` entero + señal nueva (`podas-vuelta`, `taller3-cuando`, `taller3-paltas`, reacciones, threads, uploads).
  2. **Tarea 10:00** — reeditar `jardin-hoy` en su URL estable: cobrar el silencio de los 3 slots (verificable en `send_log`), abrir con **las dos que vencen hoy mismo** (F-7 abelia, B-7 cerco) y ordenar el resto en bloques. Primer control = `podas-vuelta`, una sola vez.
  3. **Experiencia 18:00** — original NUEVA + `el-taller` (aprobada) agrupada dentro. Elenco: el liberado arriba.
  4. Si `taller3-paltas` = «corregila» → editar `prune_when` de B-22 y B-36 en `data_plants.py` + `python build.py`.
- **Hortensia B-5a/b:** era la única con reloj del finde 29-30, que cae en la ventana. Pasa al 31 y es candidata a landing propia si no se mueve.
- **Cantera sin usar:** poda→FRUTA (dic-ene) · dependencia de un solo ejemplar (44/52) · luz real vs ficha · coronita F-5 y romero B-26 del audit.
- **Medir la quickbar**: sigue sin un solo evento `via:"quickbar"`.
- **Pendiente del 16/08:** el usuario llega a las experiencias por `ideas.html`. Ordenar ahí las buenas y retirar las de la era gimmick.
