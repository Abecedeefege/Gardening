# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE (autoridad operativa — semanal, día-consciente)

| Día | Tarea (jardin-hoy) 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (solo mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Una sola push por slot de experiencia.** Siempre lleva una **original NUEVA** (el experimento del día) + las **aprobadas** de ese slot agrupadas y linkeadas DENTRO de la misma landing. Nunca dos pushes de experiencia sueltas.
- **Aprobación = recurrencia.** Solo vuelve lo que el usuario prendió (😍 / slot en «sí» / `engageApprove`). Pending sin aprobar no se borra: simplemente no recurre. **Corolario para el 24/08:** `florecio`, `preguntas-abiertas`, `tarjeta-campo`, `el-hueco`, `mandarina` y `perfume-de-octubre` NO están aprobadas → **no se re-pushean solas**; como máximo van *linkeadas* dentro de la landing del slot.
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo»), la condición se **verifica con datos reales** antes de encolar y se muestra citada.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## 🚨 LAS DOS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín. Las 3 pushes con señal activa del archivo traían **ayuda ejecutable con la herramienta en la mano**. `el-parte` perdió con el layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ninguna experiencia puede tener su primer control interactivo debajo del **35 % del scroll**, **medido renderizado en Chromium 390×780** (nunca por offset de caracteres — la auditoría del 20/08 casi archiva tres formatos por usar el proxy equivocado). Es un **seguro contra la lectura corta**, no un sustituto de la #1.
El script vive en el scratchpad: 15 líneas de `playwright` con `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ El screenshot `fullPage` deja los `.reveal` en opacity 0 — es artefacto de captura, se verifica scrolleando y contando `.reveal.in`, no en la foto.

Auditoría re-medida (21/08) que sostiene todo esto: el-taller **7,9 %** (arreglado), jardin-hoy · el-taller-2 · tarjeta-campo **0 %** (ya eran compliant → su ⬛ no es layout), el-parte **27,3 %** (compliant y perdió igual), preguntas-abiertas **75 %** (el único caso donde el layout SÍ explicó el resultado), que-mas-podo 87 % (🏆 ganó igual).

**Barra de señal rápida** (`engage.js`, 18/08): flota al 25 % de scroll o a los 25 s con 😍/🙂/🙅 + «✍️ Escribir». Emite `reaction` con `via:"quickbar"`. **Sigue SIN medir** — buscar `via:"quickbar"`, `quicksignal_dismiss` y `quicksignal_to_text` en la próxima señal que llegue.

## ✈️ EL VIAJE (7 AL 23/08) — **COMPROMISO CUMPLIDO ENTERO**

- **Compromiso publicado el 06/08: del 7 al 23 NINGUNA push de tareas.** Caían 7 slots (sáb 8, lun 10, jue 13, sáb 15, lun 17, jue 20, **sáb 22**) → **7 de 7 cumplidos**. El sáb 22 llevó solo la experiencia de las 11:00. **Esto se cobra el lunes 24: 17 días, 7 slots, cero pushes de tarea.**
- **El compromiso era SOBRE TAREAS, no sobre experiencias.** `viaje-silencio` nunca se contestó.
- **⚠️ El viaje NO fue ventana de medición.** Ningún eje ni formato se archiva con evidencia del 07 al 23. **Todo veredicto suspendido se re-mide de cero el 24/08.** *(Matiz: la apertura en 2 min del 17/08 prueba que SÍ estaba alcanzable — lo no medible es el contenido, no la disponibilidad.)*
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b). **Excepción: la hortensia tiene reloj → 29-30/08, antes del brote.** La más apurada después es **abelia F-7 (fin de agosto)**. **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** Caqui B-41 no se nombra hasta primavera.
- ✅ Cerradas: pera B-39 y liquidámbar B-37 (en `task_states.json`) + durazno B-30/35, ciruela B-38 y ciruelo F-4 **por tick propio del usuario** (02/08). ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo las muestra `active`. **No contradecir al usuario: para él están hechas.**
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (**shape real: `{"tasks": {...}}`**), no contra la edición anterior de la página.

## 🌧️ PARTE RE-VERIFICADO 22/08 (open-meteo, MVD) — 9ª vez

| Fecha | Mín | Máx | Lluvia |
|---|---|---|---|
| **23/08 (vuelta)** | 8,0 | 10,6 | **0,0 mm** |
| 24/08 | 7,6 | 8,7 | 0,0 |
| 25/08 | **4,7** | 10,8 | 0,0 |
| 26-27/08 | 7,6 / 11,1 | 13,2 / 12,7 | 1,2 / **9,6** |
| 28-31/08 | 9,9-10,7 | 11,3-11,4 | 0,0 |

- **Lo que aguanta 9 corridas (esto SÍ se publica):** máximas clavadas en **9-11 °C**, **cero heladas en 14 días** (mínima absoluta 4,7 el 25/08) y **jardín SECO a la vuelta** — 5ª confirmación seguida.
- **Correcciones honestas de hoy:** el 22/08 pasó de 0,0 a **0,2 mm** (por eso se publicó el 23, no el 22) y el «primer calor» se movió **por 4ª vez** (26/08: 15,4 → 13,2). **Ninguna de las dos se publicó.**
- ⚠️ **Dato nuevo a >72 h, NO publicable todavía: 9,6 mm el jueves 27/08.** Re-verificarlo el 24 y el 26 — si aguanta, es material real para el canal tarea de la reentrada (ventana de poda que se cierra).
- **Regla dura:** solo se publica lo que sigue en pie el día que se encola. Lo que aguanta se REAFIRMA; lo que se movió **se corrige de frente**. A >72 h el número no es publicable — nueve corridas confirmándolo.

## 🕐 LA HORA — el contenido decide, la hora modula

| Envío real (MVD) | Push | 1ª apertura | Resultado |
|---|---|---|---|
| **Lun 17/08 18:23** | preguntas-abiertas | **+2 min** ⚡ | récord de delay — murió al 41 % |
| Sáb 01/08 12:06 · Dom 02/08 11:07 | el-taller (+ re-push) | +2 h / +4 h | 🏆 ÉXITO MÁXIMO ×2 |
| Lun 03/08 18:48 | el-taller-2 | +32 min | masomenos-alto (7/7 pasos) |
| Sáb 01/08 10:58 · Vie 31/07 18:02 | jardin-hoy · el-parte | +4 h / +1 h 41 | floja · formato muerto |
| 04/08 → 15/08 | tarjeta · jardin-hoy · el-hueco · mandarina · florecio | nunca | ⬛ ×5 — *ausencia, no computan* |

- **Lunes 18:00-18:30 = la mejor puerta de entrada medida**; sábado 11-12 h dio los dos éxitos máximos. **Ambos slots validados como HORA.**
- ⚠️ **Dispatcher lag: 11 min a 2,7 h.** Encolar en el horario exacto sigue siendo lo correcto.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios en vez de texto. La hipótesis ② se mide sola con `el-taller-arranque`.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad — y es materia prima de contenido.
- **Taller nº3 = pitósporo B-43, lunes 24/08.** Llega con la pregunta ya sembrada dos veces (la flor amarilla del 05/05 contradice la ficha + el teaser «algo pendiente para el lunes» del 22/08). **Antes del re-push hay que renovarle el texto a `el-taller` en su URL**: el hero todavía dice «0 mm / 5 días al viaje», datos del 1º de agosto.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes:** el viaje es **tranquilidad o ventaja**, nunca lista de pendientes. · **vos-decidis:** el eje AGENCIA vive, el CONTENEDOR repetido se quema. · **mi-objetivo:** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí se usó el 22/08)* · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).
- **Era gimmick (feed falso, superpoderes):** el 16/08 los abrió **por voluntad propia** y rebotó en **9 s / 28 %** en los dos. No retienen ni cuando los busca él.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando NO puede hacer (viaje), lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **🆕 El VETO con fecha de vencimiento (22/08, sin veredicto):** decirle qué **NO** hacer, con ventana de días contados, es la variante de la regla #1 que nunca se probó. Toda la industria vende tareas; nadie vende lo contrario, y la pérdida cara del jardín amateur es la poda a destiempo (se cobra 3 meses después).
- **🆕 La contradicción interna del catálogo es una mina.** Cruzando `flowering` × `prune_when` de las 52 fichas apareció un error real (B-7: «post-floración mayo-junio» pero florece oct-nov). **Correr ese cruce completo sobre las 52 fichas en la reentrada** — cada fila imposible es a la vez contenido, credibilidad y un tap que genera trabajo mío.
- **El título es el activo más medido que tengo.** «Tu jardín tiene 6 preguntas abiertas» = 2 minutos. **Sustantivo concreto + número + algo que le pertenece** (+ pérdida, desde el 22/08).
- **El dato computado sobre su propio catálogo es munición sin explotar.** 52 fichas × 20 campos + el log con hora de sus acciones. Usados: floración (08/08), fruta (10/08), acción→floración (15/08), campos «a confirmar» (17/08), **poda×floración×madera vieja (22/08)**. Sin usar: **el cruce poda×FRUTA (dic-ene)**, dependencia de un solo ejemplar (44/52), **luz real vs ficha** (solo se tocó la lavanda), calendario de perfume aplicado a PLANTAR.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1.
- **Timing verificado > urgencia inventada** — y **número re-verificado > número lindo**.
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal tarea ES contenido: la promesa cumplida se cobra el 24/08.
- **Minimalismo + REAL + VISUAL.** **FOTOS REALES = need validado.** Diagrama propio > párrafo.
- **Declarar lo que NO sé suma** (ligustro F-9 el 22/08): no inventar perfume donde la ficha no lo dice, y dejar la pregunta agendada para noviembre. Credibilidad hoy + gancho futuro.
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.
- **Antes de archivar un formato, verificar la medición que lo condena.**

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días. **Una decisión guardada en learnings NO anula el ledger: el ledger gana.**
- **Excepción:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco.
- ⚠️ **Quemados nuevos hasta el 29/08** (elenco del 22/08): B-7/B-11/B-31/B-33, B-3, B-43, B-10/B-19, B-27, B-23, F-1, B-26, B-25, B-37, B-29, F-9. También **el par «madera vieja / madera nueva»** como explicación central y el conteo «11 perfumadas».
- **Elenco LIBRE para la reentrada del 24/08:** pindó B-8, podranea F-2, pata de vaca B-42, anacahuita B-16, santa rita B-1, evónimo B-44, mandioca B-34, madreselva B-40, aguaribay F-8, palta uruguaya B-22, palta Haas B-36, vivero B-46, cinta B-12, esparraguera B-6, coronita F-5, fresno F-10, mandarina B-24, crespón B-9, althea B-18, hortensia B-5a/b, hibisco B-4, lapachillo B-14, hiedra B-15, viraró B-32, fotinia F-3, abelia F-7, I-1, I-2 + los 4 frutales podados.
- **No repetir en <14 días:** el gráfico de 12 meses de FLORACIÓN · la tira de FRUTA · «32 vs 1» · «3 → 2» · «6 → 4» · el circuito reserva→tijera→flor · las 4 candidatas (camelia/aloe/salvia leucantha/jazmín de invierno) · la bifurcación del trifoliado, la clave por olor de B-45 y «hoja converge por ambiente, flor no» (libres 31/08).
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas → EJECUTADO. Liquidámbar B-37 → hecho.
- **01-04/08:** «mándamela cuando esté lindo» (ejecutado 02/08 con verificación meteo) · «¿qué más puedo podar? ¿y el neem?» (contestado 02/08 + Taller nº2) · «recordame las podas si no llueve» (ejecutado el 04/08).
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (22/08/2026)

- Push subscription `pix9`: **active**; logging vía `/api/feedback` confiable. Threads, `uploads.json` y `user_tasks.json`: **0 pendientes** (lo último del usuario es del 30/07).
- **Cero eventos nuevos en 5 días** (el último sigue siendo el dwell del 17/08 21:25Z). Ventana ciega de viaje, esperado.
- Sin responder: `podas-previaje`, `viaje-silencio`, `horario-tareas`. Los tres son insumo de la reentrada.
- Jardín en DORMANCIA, **saliendo: los 4 frutales podados están abriendo flor**. **32 días al equinoccio (23/09).** Helada posible hasta fin de agosto (ninguna en el pronóstico a 14 días), pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado = «más flor»** (el perfume del 22/08 es su extensión natural).
- Compactación 22/08: `send_log` → el envío del 06/08 (>14 d) pasó a `daily_summary`, quedan 4 eventos. `engagement.json`: los 10 eventos son del 16-17/08, nada que compactar. Queue del 21/08 reemplazada por la del 22/08.

## Conclusiones de los push (por feedback real)

- **22/08 — perfume-de-octubre: ENVIADA, sin veredicto.** Primera prueba del **veto con fecha**. Primer control al **9,5 %** del scroll (Chromium 390×780, regla #2 con margen). 3 taps distintos antes del 50 % del documento. Se mide el 24/08: si el tap que llega es `perfume-ficha-azarero`, lo que convierte es **delegarme trabajo**; si es `perfume-podaste`, lo que convierte es **que le pregunte por lo que hizo**; si es `perfume-donde`, es **proyectar el jardín futuro**. Los tres son ángulos distintos y el que gane define la reentrada.
- **17/08 — preguntas-abiertas: MASOMENOS con el mejor dato de timing del canal.** Apertura en **2 min** (récord) y muerte al 41 %. **5º reconteo (22/08, 5 días): cero eventos nuevos.** Su causa de layout sobrevive a la re-medición (75 % renderizado): la única del archivo donde el layout sí explicó el resultado. Veredicto de contenido suspendido al 24/08.
- **15/08 — florecio-lo-que-podaste: ⬛, VEREDICTO SUSPENDIDO.** Quedó linkeada al 94 % del documento del 17: **no es rechazo, es no-exposición**. No aprobada → no se re-pushea sola.
- **16/08 — domingo sin slot: 0 push por diseño, y el usuario volvió SOLO al sitio** (src=direct, desde `ideas.html`). **El espacio vacío no lo aleja** — argumento fuerte a favor de la cadencia baja.
- **18, 19, 20 y 21/08 — días sin push cumplidos** (mantenimiento puro). **22/08 cerró el compromiso del viaje: 7 de 7 slots de tarea en silencio.**
- **10/08 mandarina · 08/08 el-hueco · 04/08 tarjeta-campo · 06/08 jardin-hoy: ⬛ SUSPENDIDOS** (ventana ciega). El tap `mandarina-parte-vuelta` NO se activó → **el parte de vuelta no es deuda comprometida**. · **03/08 el-taller-2: MASOMENOS-ALTO** (7/7 pasos, dwell 166 s, cero reacción) con el control al 0 %: el layout NO fue la causa.
- **02/08 — el-taller re-push: ÉXITO MÁXIMO** (😍 + 2º slot + 3 ticks de poda reales; verificar la condición del mundo real fue determinante). · **31/07 — el-parte: formato-diario archivado**, con layout compliant (27 %) — la derrota más limpia del canal. · **30/07 — jardin-hoy GANADORA, día tier-1** (3 feedback_text, los tres ejecutados).
- **Patrón agregado (15 pushes, 30/07 al 22/08):** las 3 con señal activa traían **ayuda técnica ejecutable con la herramienta en la mano**. Las 6 ⬛ son del período 04-15/08 = ausencia física. **La única derrota con evidencia limpia sigue siendo `el-parte`, y perdió por contenido.**

## TODO / próximos experimentos

- **LUNES 24/08 — REENTRADA (tarea 10:00 + experiencia 18:00).** ① **cobrar la promesa cumplida: 17 días, 7 de 7 slots, cero pushes de tarea** ② renovar el texto de `el-taller` en su URL ANTES de re-pushearla ③ **Taller nº3 = pitósporo B-43** (ya teaseado dos veces) ④ leer `podas-previaje` y armar la lista real de las 12 ⑤ aplicar `horario-tareas` si contestó ⑥ **leer los 3 taps del 22/08** y dejar que definan el ángulo ⑦ si tocó «corregila», **corregir `prune_when` de B-7 en `data_plants.py` + `python build.py`** ⑧ re-medir de cero todo lo suspendido ⑨ hortensia el 29-30/08, la única con reloj.
- **Cantera de auditorías computadas:** el cruce `flowering × prune_when` **sobre las 52 fichas enteras** (hoy salió una contradicción de las 12 que se miraron) · un solo ejemplar (44/52) · reparto real de luz vs lo que pide cada ficha · el bucle poda→FRUTA en diciembre-enero.
- **Medir la barra de señal rápida**: sigue sin un solo evento `via:"quickbar"`.
- **Idea del 16/08:** el usuario llega a las experiencias por `ideas.html`. En la reentrada, **ordenar ahí las buenas y retirar las de la era gimmick**.
