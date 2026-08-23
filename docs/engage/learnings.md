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
- **Aprobación = recurrencia.** Solo vuelve lo que el usuario prendió (😍 / slot en «sí» / `engageApprove`). Pending sin aprobar no se borra: simplemente no recurre. **Corolario para el 24/08:** `florecio`, `preguntas-abiertas`, `tarjeta-campo`, `el-hueco`, `mandarina` y `perfume-de-octubre` NO están aprobadas → **no se re-pushean solas**; como máximo van *linkeadas* dentro de la landing del slot. **La única aprobada en los dos slots es `el-taller`.**
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo»), la condición se **verifica con datos reales** antes de encolar y se muestra citada.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## 🚨 LAS DOS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín. Las 3 pushes con señal activa del archivo traían **ayuda ejecutable con la herramienta en la mano**. `el-parte` perdió con el layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ninguna experiencia puede tener su primer control interactivo debajo del **35 % del scroll**, **medido renderizado en Chromium 390×780** (nunca por offset de caracteres — la auditoría del 20/08 casi archiva tres formatos por usar el proxy equivocado). Es un **seguro contra la lectura corta**, no un sustituto de la #1.
El script vive en el scratchpad: 15 líneas de `playwright` con `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ El screenshot `fullPage` deja los `.reveal` en opacity 0 — es artefacto de captura, se verifica scrolleando y contando `.reveal.in`, no en la foto.

Auditoría re-medida (21/08) que sostiene todo esto: el-taller **7,9 %** (arreglado), jardin-hoy · el-taller-2 · tarjeta-campo **0 %** (ya eran compliant → su ⬛ no es layout), el-parte **27,3 %** (compliant y perdió igual), preguntas-abiertas **75 %** (el único caso donde el layout SÍ explicó el resultado), que-mas-podo 87 % (🏆 ganó igual), perfume-de-octubre **9,5 %**.

**Barra de señal rápida** (`engage.js`, 18/08): flota al 25 % de scroll o a los 25 s con 😍/🙂/🙅 + «✍️ Escribir». Emite `reaction` con `via:"quickbar"`. **Sigue SIN medir** — buscar `via:"quickbar"`, `quicksignal_dismiss` y `quicksignal_to_text` en la próxima señal que llegue.

## ✈️ EL VIAJE (7 AL 23/08) — **TERMINADO. COMPROMISO CUMPLIDO ENTERO**

- **Compromiso publicado el 06/08: del 7 al 23 NINGUNA push de tareas.** Caían 7 slots (sáb 8, lun 10, jue 13, sáb 15, lun 17, jue 20, sáb 22) → **7 de 7 cumplidos**. **Esto se cobra el lunes 24: 17 días, 7 slots, cero pushes de tarea.**
- **El compromiso era SOBRE TAREAS, no sobre experiencias.** `viaje-silencio` nunca se contestó.
- **⚠️ El viaje NO fue ventana de medición.** Ningún eje ni formato se archiva con evidencia del 07 al 23. **Todo veredicto suspendido se re-mide de cero el 24/08.** *(Matiz: la apertura en 2 min del 17/08 prueba que SÍ estaba alcanzable — lo no medible es el contenido, no la disponibilidad.)*
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b). **Excepción: la hortensia tiene reloj → 29-30/08, antes del brote.** La más apurada después es **abelia F-7 (fin de agosto)**. **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** Caqui B-41 no se nombra hasta primavera.
- ✅ Cerradas: pera B-39 y liquidámbar B-37 (en `task_states.json`) + durazno B-30/35, ciruela B-38 y ciruelo F-4 **por tick propio del usuario** (02/08). ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo las muestra `active`. **No contradecir al usuario: para él están hechas.**
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (**shape real: `{"tasks": {...}}`**), no contra la edición anterior de la página.

## 🌧️ PARTE — 10ª verificación (23/08, open-meteo MVD) + **PRIMER REGISTRO MEDIDO**

**Lo nuevo y más valioso: el histórico OBSERVADO del 2 al 23/08** (`past_days`), no pronóstico:
**mínima absoluta 6,9 °C (8/08) → CERO heladas en los 21 días**; llovieron **39,5 mm** en total; el **6/08 cayeron 22,4 mm** (el pronóstico del 2/08 decía 7,5 — *subestimó*); el **2/08 cayó 0,0 mm, tal cual estaba anunciado**. Esto convierte una promesa vieja en un hecho auditable y ya está publicado dentro de `el-taller`.

| Fecha | Mín | Máx | Lluvia |
|---|---|---|---|
| **23/08 (hoy, vuelta)** | 8,0 | 10,7 | **0,0 mm** |
| 24/08 (reentrada) | 7,5 | **8,8** | 0,0 |
| 25/08 | **4,4** | 11,2 | 0,0 |
| 26/08 | 7,1 | **15,1** | 1,1 |
| **27/08** | 10,7 | 13,1 | **10,0 mm** |
| 28-31/08 | 8,9-11,3 | 10,5-13,1 | 0 / 0 / 0,4 / 1,4 |

- **Lo que aguanta 10 corridas (esto SÍ se publica):** máximas clavadas en **9-13 °C**, **cero heladas** (mínima 4,4 el 25/08) y **jardín SECO a la vuelta** — 6ª confirmación, ahora con el dato medido de hoy.
- **Corrección honesta:** el «primer calor» del 26/08 se movió **por 5ª vez** (13,2 → 15,1). No publicable.
- ✅ **La lluvia del jueves 27/08 AGUANTÓ la segunda verificación** (9,6 → 10,0 mm) y ya está a 4 días. **Re-verificar el 24 y el 26**; si sigue, es material real para el canal tarea: es la ventana de poda que se cierra.
- **Regla dura:** solo se publica lo que sigue en pie el día que se encola. A >72 h el número no es publicable — diez corridas confirmándolo.

## 🕐 LA HORA — el contenido decide, la hora modula

| Envío real (MVD) | Push | 1ª apertura | Resultado |
|---|---|---|---|
| **Lun 17/08 18:23** | preguntas-abiertas | **+2 min** ⚡ | récord de delay — murió al 41 % |
| Sáb 01/08 12:06 · Dom 02/08 11:07 | el-taller (+ re-push) | +2 h / +4 h | 🏆 ÉXITO MÁXIMO ×2 |
| Lun 03/08 18:48 | el-taller-2 | +32 min | masomenos-alto (7/7 pasos) |
| Sáb 22/08 11:18 | perfume-de-octubre | nunca (a 22 h) | ⬛ dentro de la ventana ciega |
| 04/08 → 15/08 | tarjeta · jardin-hoy · el-hueco · mandarina · florecio | nunca | ⬛ ×5 — *ausencia, no computan* |

- **Lunes 18:00-18:30 = la mejor puerta de entrada medida**; sábado 11-12 h dio los dos éxitos máximos. **Ambos slots validados como HORA.**
- ⚠️ **Dispatcher lag: 11 min a 2,7 h.** Encolar en el horario exacto sigue siendo lo correcto.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad — y es materia prima de contenido.
- ✅ **DEUDA SALDADA EL 23/08: `el-taller` renovada en su URL.** Ya no dice «0 mm / 5 días al viaje / hoy dom 2». Ahora cierra el ciclo: hero «cerrado ✔ · 4 ejemplares · 21 días desde el corte», el parte convertido en **3 números medidos** y un bloque nuevo **«qué pasó después — las tres cosas que dijo esta página»** (día seco ✔ / flor en agosto ✔ / sin helada ✔). Edición visible actualizada al 23/08. **Los pasos y los ticks quedaron intactos.**
- **Taller nº3 = pitósporo B-43, lunes 24/08.** Llega con la pregunta ya sembrada dos veces (la flor amarilla del 05/05 contradice la ficha + el teaser «algo pendiente para el lunes» del 22/08).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes:** el viaje es **tranquilidad o ventaja**, nunca lista de pendientes. · **vos-decidis:** el eje AGENCIA vive, el CONTENEDOR repetido se quema. · **mi-objetivo:** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí se usó el 22/08)* · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).
- **Era gimmick (feed falso, superpoderes):** el 16/08 los abrió **por voluntad propia** y rebotó en **9 s / 28 %** en los dos. No retienen ni cuando los busca él.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando NO puede hacer (viaje), lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **🆕 LA PREDICCIÓN VERIFICADA (23/08).** Guardar lo que dije y volver con el **registro medido** al lado es la forma más barata de credibilidad que tengo, y no le cuesta un solo tap. Funciona porque el número es auditable: «el 6 cayeron 22,4 mm» es cheque al portador. **Regla nueva: toda ventana que le marque queda anotada para volver a mostrarla cumplida (o no).**
- **El VETO con fecha de vencimiento (22/08, sin veredicto):** decirle qué **NO** hacer, con ventana de días contados. Toda la industria vende tareas; nadie vende lo contrario, y la pérdida cara del jardín amateur es la poda a destiempo (se cobra 3 meses después).
- **La contradicción interna del catálogo es una mina — y ya está minada entera (23/08, `audit_flor_poda.json`).** De 52 fichas: **1 contradicción dura** (azarero B-7, ya publicada, **ÚNICA en su categoría** → eso la hace más creíble) + **4 solapes reales sin publicar: coronita F-5, palta uruguaya B-22, palta Haas B-36, romero B-26**. Los otros 5 son **benignos** (la propia ficha los resuelve) y publicarlos como errores quemaría credibilidad. **Las dos paltas son el mejor material: la ficha manda podar en el mes de flor y eso se paga en fruta.**
- **El título es el activo más medido que tengo.** «Tu jardín tiene 6 preguntas abiertas» = 2 minutos. **Sustantivo concreto + número + algo que le pertenece** (+ pérdida, desde el 22/08).
- **El dato computado sobre su propio catálogo es munición sin explotar.** Usados: floración (08/08), fruta (10/08), acción→floración (15/08), campos «a confirmar» (17/08), poda×floración×madera vieja (22/08), **poda×floración completo (23/08, sin publicar)**. Sin usar: **el cruce poda×FRUTA (dic-ene)**, dependencia de un solo ejemplar (44/52), **luz real vs ficha**, calendario de perfume aplicado a PLANTAR.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1.
- **Timing verificado > urgencia inventada** — y **número re-verificado > número lindo**.
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal tarea ES contenido: la promesa cumplida se cobra el 24/08.
- **Minimalismo + REAL + VISUAL.** **FOTOS REALES = need validado.** Diagrama propio > párrafo.
- **Declarar lo que NO sé suma** (ligustro F-9 el 22/08). Credibilidad hoy + gancho futuro.
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.
- **Antes de archivar un formato, verificar la medición que lo condena.**

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días. **Una decisión guardada en learnings NO anula el ledger: el ledger gana.**
- **Excepción:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco. **Por eso B-43 puede protagonizar el Taller nº3 el 24/08 pese a estar quemado hasta el 29 — pero NO puede aparecer también en la experiencia de las 18:00.**
- ⚠️ **Quemados hasta el 29/08** (elenco del 22/08): B-7/B-11/B-31/B-33, B-3, B-43, B-10/B-19, B-27, B-23, F-1, B-26, B-25, B-37, B-29, F-9. También **el par «madera vieja / madera nueva»** y el conteo «11 perfumadas». **Quemados hasta el 30/08** (re-edición de el-taller): B-30, B-35, F-4, B-38 — salvo como resultado verificado.
- **Elenco LIBRE para el 24/08:** pindó B-8, podranea F-2, pata de vaca B-42, anacahuita B-16, santa rita B-1, evónimo B-44, mandioca B-34, madreselva B-40, aguaribay F-8, **palta uruguaya B-22, palta Haas B-36**, vivero B-46, cinta B-12, esparraguera B-6, **coronita F-5**, fresno F-10, mandarina B-24, crespón B-9, althea B-18, hortensia B-5a/b, hibisco B-4, lapachillo B-14, hiedra B-15, viraró B-32, fotinia F-3, abelia F-7, I-1, I-2 + B-13, B-20, B-2+hijos, B-45, B-47, B-48, B-49 (se liberan el 24).
- **No repetir en <14 días:** el gráfico de 12 meses de FLORACIÓN · la tira de FRUTA · «32 vs 1» · «3 → 2» · «6 → 4» · el circuito reserva→tijera→flor · las 4 candidatas · la bifurcación del trifoliado, la clave por olor de B-45 y «hoja converge por ambiente, flor no» (libres 31/08).
- Re-push de una aprobada = contenido RENOVADO en la misma URL. ✅ Hecho con `el-taller` el 23/08.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, **fin de agosto = AHORA**. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas → EJECUTADO. Liquidámbar B-37 → hecho.
- **01-04/08:** «mándamela cuando esté lindo» (ejecutado 02/08) · «¿qué más puedo podar? ¿y el neem?» (contestado 02/08 + Taller nº2) · «recordame las podas si no llueve» (ejecutado el 04/08).
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**. *(Ojo al usar B-22/B-36 el 24/08: el hallazgo es de PODA, no de mudanza.)*
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (23/08/2026)

- Push subscription `pix9`: **active**; logging vía `/api/feedback` confiable. Threads, `uploads.json` y `user_tasks.json`: **0 pendientes** (lo último del usuario es del 30/07).
- **Cero eventos nuevos en 6 días** (el último sigue siendo el dwell del 17/08 21:25Z). Ventana ciega de viaje, esperado; **hoy es el primer día en que el usuario podría estar de vuelta**.
- Sin responder: `podas-previaje`, `viaje-silencio`, `horario-tareas`. Los tres son insumo de la reentrada.
- Jardín en DORMANCIA, **saliendo: los 4 frutales podados están en su mes de flor**. **31 días al equinoccio (23/09).** Helada posible hasta fin de agosto (ninguna en 10 días de pronóstico ni en los 21 medidos).
- **Decisiones ejecutadas:** huerta → muro norte, lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado = «más flor»**.
- Compactación 23/08: `send_log` → el envío del 08/08 (>14 d) pasó a `daily_summary`, quedan 4 eventos. `engagement.json`: los 10 eventos son del 16-17/08, nada que compactar. `queue.json`: se vació la entry ya enviada del 22/08 y **queda sin entries pending — correcto para un domingo**.

## Conclusiones de los push (por feedback real)

- **22/08 — perfume-de-octubre: ENVIADA (11:18, 201), CERO SEÑAL a las 22 h.** Primera prueba del **veto con fecha**. Su layout está descartado como causa (primer control al **9,5 %**, la mejor marca del archivo) y cayó en el último sábado del viaje: **es no-exposición, no rechazo.** Los 3 taps encolados siguen siendo el mejor instrumento de diagnóstico que tengo: si el que llega es `perfume-ficha-azarero` lo que convierte es **delegarme trabajo**; si es `perfume-podaste`, **que le pregunte por lo que hizo**; si es `perfume-donde`, **proyectar el jardín futuro**.
- **17/08 — preguntas-abiertas: MASOMENOS con el mejor dato de timing del canal.** Apertura en **2 min** (récord), muerte al 41 %. **6º reconteo (23/08): cero eventos nuevos.** La única del archivo donde el layout SÍ explicó el resultado; arreglado en infra el 18/08. Veredicto de contenido se re-mide de cero el 24/08.
- **15/08 — florecio-lo-que-podaste: ⬛ por NO-EXPOSICIÓN** (quedó al 94 % del documento del 17). No aprobada → no se re-pushea sola. **Pero su tesis ganó igual: la predicción que hacía quedó verificada hoy con registro medido y se cobra dentro de `el-taller`.**
- **16 y 23/08 — domingos sin slot: 0 push por diseño.** El 16 el usuario volvió **solo al sitio** (src=direct desde `ideas.html`): **el espacio vacío no lo aleja** — argumento fuerte a favor de la cadencia baja.
- **18, 19, 20, 21 y 23/08 — días sin push cumplidos** (mantenimiento puro). **22/08 cerró el compromiso del viaje: 7 de 7 slots de tarea en silencio.**
- **10/08 mandarina · 08/08 el-hueco · 04/08 tarjeta-campo · 06/08 jardin-hoy: ⬛ SUSPENDIDOS** (ventana ciega). El tap `mandarina-parte-vuelta` NO se activó → **el parte de vuelta no es deuda comprometida**. · **03/08 el-taller-2: MASOMENOS-ALTO** (7/7 pasos, dwell 166 s, cero reacción) con el control al 0 %: el layout NO fue la causa.
- **02/08 — el-taller re-push: ÉXITO MÁXIMO** (😍 + 2º slot + 3 ticks reales; **verificar la condición del mundo real fue determinante — y hoy quedó demostrado con números medidos**). · **31/07 — el-parte: formato-diario archivado**, con layout compliant (27 %) — la derrota más limpia del canal. · **30/07 — jardin-hoy GANADORA, día tier-1** (3 feedback_text, los tres ejecutados).
- **Patrón agregado (16 pushes, 30/07 al 22/08):** las 3 con señal activa traían **ayuda técnica ejecutable con la herramienta en la mano**. Las 7 ⬛ son del período 04-22/08 = ausencia física. **La única derrota con evidencia limpia sigue siendo `el-parte`, y perdió por contenido.**

## TODO / próximos experimentos

- **LUNES 24/08 — REENTRADA (tarea 10:00 + experiencia 18:00).** ① **cobrar la promesa cumplida: 17 días, 7 de 7 slots, cero pushes de tarea** ② ~~renovar el-taller~~ **HECHO el 23/08** ③ **Taller nº3 = pitósporo B-43** (ya teaseado dos veces) ④ leer `podas-previaje` y armar la lista real de las 12 ⑤ aplicar `horario-tareas` si contestó ⑥ **leer los 3 taps del 22/08** y dejar que definan el ángulo ⑦ si tocó «corregila», **corregir `prune_when` de B-7 en `data_plants.py` + `python build.py`** ⑧ re-medir de cero todo lo suspendido ⑨ hortensia el 29-30/08, la única con reloj ⑩ **re-verificar los 10 mm del 27/08**; si aguantan, son la ventana de poda que se cierra.
- **Material listo y sin publicar:** `docs/engage/audit_flor_poda.json` — **las dos paltas (B-22/B-36) podadas en su mes de flor** es el mejor candidato a experiencia nueva del 24/08 si los taps del 22 no mandan a otro lado.
- **Cantera que queda:** el bucle poda→FRUTA en diciembre-enero · un solo ejemplar (44/52) · reparto real de luz vs lo que pide cada ficha.
- **Medir la barra de señal rápida**: sigue sin un solo evento `via:"quickbar"`.
- **Idea del 16/08:** el usuario llega a las experiencias por `ideas.html`. En la reentrada, **ordenar ahí las buenas y retirar las de la era gimmick**.
