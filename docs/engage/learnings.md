# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE (autoridad operativa — semanal, día-consciente)

| Día | Tarea (jardin-hoy) 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / **Domingo** | — | — (solo mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Una sola push por slot de experiencia.** Siempre lleva una **original NUEVA** (el experimento del día) + las **aprobadas** de ese slot agrupadas y linkeadas DENTRO de la misma landing. Nunca dos pushes de experiencia sueltas.
- **Aprobación = recurrencia.** Solo vuelve lo que el usuario prendió (😍 / slot en «sí» / `engageApprove`). Pending sin aprobar no se borra: simplemente no recurre.
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo», «si no llueve»), la condición se **verifica con datos reales** antes de encolar y se muestra citada.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + HTML de pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## ✈️ CONTEXTO DOMINANTE — **VIAJE 7 AL 23 DE AGOSTO** (hoy = día 11, 17/08)

- **Compromiso publicado el 06/08, a cumplir a rajatabla: del 7 al 23 NO se manda NINGUNA push de tareas.** Adentro caen 7 slots (sáb 8 ✅, lun 10 ✅, jue 13 ✅, sáb 15 ✅, **lun 17 ✅ hoy**; faltan jue 20 y sáb 22). **5 de 7 cumplidos.** Los 2 que quedan salen solos si la cola queda vacía esos días. **Romperlo quema el activo más caro que tengo.**
- **El compromiso es SOBRE TAREAS, no sobre experiencias.** `viaje-silencio` sigue **sin contestar** → rige el default: **0 tareas + experiencia solo si es lectura placentera, cero-deber y con listón alto.** Releerlo antes del sáb 22.
- **⚠️ El viaje NO es ventana de medición (regla 09/08, reconfirmada cada corrida).** **Ningún eje ni formato se archiva con evidencia recogida entre el 07 y el 23.** Todo veredicto suspendido hasta la reentrada del 24/08.
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b). **Excepción: la hortensia sí tiene reloj → 29-30/08, antes del brote.**
- ✅ Cerradas: pera B-39 y liquidámbar B-37 (en `task_states.json`) + durazno B-30/35, ciruela B-38 y ciruelo F-4 **por tick propio del usuario** (02/08). ⚠️ Los ticks del Taller (`taller-arbol-*`, `podo-*`) **NO escriben `task_states.json`** — el archivo las muestra `active`. **No contradecir al usuario: para él están hechas.**
- **Chequeo de vencimientos (sigue válido):** ninguna ventana abierta se cierra antes del 23. La más apurada es **abelia F-7, límite fin de agosto**. Vuelve con margen real.
- **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** B-41 caqui NO se nombra como urgencia hasta primavera (pedido del usuario) — hoy calificaba para los expedientes abiertos y **lo excluí a propósito**.
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (**shape real: `{"tasks": {...}}`**), no contra la edición anterior de la página.

## 🚨 LO NUEVO DEL 17/08 — **EL USUARIO ROMPIÓ EL SILENCIO SOLO, SIN PUSH**

**Dom 16/08, 15:53 UY: primeros eventos en 12 días.** `src: "direct"`, sin `nid` → **no vino de una notificación: entró al sitio por su cuenta**, desde `ideas.html` (que es lo único que linkea esas dos páginas). Abrió **dos experiencias VIEJAS**: `2026-06-29-feed-jardin` (9 s, 28 % de scroll) y `2026-06-30-superpoderes-jardin` (10 s, 29 %). Nada más: 0 taps, 0 reacción, 0 feedback.

Tres lecturas, las tres operativas:

1. **Está alcanzable y está curioso — el ⬛ del 15/08 no es rechazo ni desconexión.** Confirma por evidencia lo que veníamos asumiendo: la ventana ciega es de *disponibilidad*, no de interés. **Refuerza el «no archivar nada durante el viaje».**
2. **El catálogo de experiencias tiene tracción propia.** Fue a buscarlas él, desde `ideas.html`, sin que nadie lo mandara. **Las experiencias no son solo un canal push: son un lugar al que vuelve.** Vale la pena que la landing de cada slot agrupe bien las anteriores (ya lo hace) y que las buenas queden linkeadas desde el sitio.
3. **Y rebotó a los 9 segundos con 28 % de scroll, en las dos.** Las dos que abrió son de la **era gimmick** (feed falso, superpoderes). Es la regla #1 otra vez, ahora medida en la dirección contraria: **fue a buscar contenido por curiosidad y lo que encontró no lo retuvo.** Un formato sin sustancia no aguanta ni la visita que el propio usuario inicia.

**Consecuencia adoptada hoy:** ninguna experiencia nueva puede depender del gancho — el primer scroll tiene que traer sustancia o se pierde a los 9 segundos.

## 🌧️ PARTE RE-VERIFICADO 17/08 (open-meteo, MVD) — la tesis del frío AGUANTA

| Fecha | Mín | Máx | Lluvia |
|---|---|---|---|
| **17/08 (hoy)** | 10,0 | 11,8 | 3,1 mm |
| 18-20/08 | 6,7-9,2 | 9,8-10,6 | 0-0,2 mm |
| 21-22/08 | 7,0-7,9 | 10,1-10,8 | 1,5-4,2 mm |
| **23/08 (vuelta)** | 7,1 | **8,7** | 4,6 mm |
| 24-25/08 | 3,8-6,5 | 7,8-10,4 | 0 mm |

- **Lo publicado el 15/08 se sostiene, con una corrección honesta al pie:** dije «máximas de 9,3 a 12,0 °C del 17 al 23»; la medición de hoy da **8,7 a 11,8**. El 23 pincha 0,6 °C por debajo del piso que publiqué. La **sustancia** (frío sostenido → flor lenta → flor que dura) queda **reforzada, no desmentida**. Mínima absoluta ahora **3,8 °C el 25** (dije 4,8) — **sigue sin tocar cero: cero heladas en 14 días.** La flor de los frutales está a salvo y hay chance real de flor abierta el 23.
- La lluvia se movió otra vez (17/08 pasó de 6,9 a 3,1 mm). **Cuarta confirmación seguida: el número de lluvia a >72 h es basura y no se publica.**
- **Regla dura, cuarta vez:** un pronóstico a >72 h NO es dato publicable. Solo se publica lo que sigue en pie el día que se encola. **Corolario:** lo que aguanta se REAFIRMA (es capital gratis), y **lo que se movió se corrige de frente en el pie de página** — corregirse uno mismo antes de que lo note el otro es la forma más barata de credibilidad.

## 🕐 LA HORA — hipótesis corregida el 08/08

| Envío real (MVD) | Push | 1ª apertura | Resultado |
|---|---|---|---|
| **Sáb 01/08 12:06** | **el-taller** | +2 h 08 | **🏆 ÉXITO MÁXIMO** |
| **Dom 02/08 11:07** | **el-taller re-push** | +4 h | **🏆 ÉXITO (😍 + 2º slot + 3 ticks)** |
| Dom 02/08 14:46 | que-mas-podo | +3 h 57 | acción real (podó F-4) |
| **Lun 03/08 18:48** | el-taller-2 | **+32 min** | ⚡ el mejor delay medido |
| Sáb 01/08 10:58 | jardin-hoy | +4 h | floja (dwell 25 s) |
| Vie 31/07 18:02 | el-parte | +1 h 41 | masomenos |
| Mar 04/08 → sáb 15/08 | tarjeta-campo · jardin-hoy · el-hueco · mandarina · florecio | nunca | ⬛ ×5 — *ausencia física, no computan* |

- **La hora modula, el contenido decide.** `el-taller` salió 11:07 y 12:06 — la misma franja de los ⬛ — y fue el mejor resultado del canal. **No enterrar un formato por la hora ni salvarlo por ella.**
- ⚠️ **El dispatcher lag mide 11 min a 2,7 h** (el 15/08 fueron **19 min**). Encolar en el horario exacto sigue siendo lo correcto.
- ⚠️ **Los horarios son mandato del usuario.** `horario-tareas` publicado el 06/08 sin contestar. **Leerlo antes de la reentrada.**

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

`2026-08-01-el-taller` — **APPROVED lunes 18:00 + sábado 11:00.** El mejor resultado del canal.

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95%, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad — y además **es materia prima de contenido** (ver bucle cerrado).
- Durante el viaje va **linkeada y en pausa** dentro de la landing del slot, nunca pusheada suelta.
- **Taller nº3 = pitósporo B-43**, reservado para la reentrada. Bonus del 17/08: B-43 quedó instalado como expediente abierto (la flor amarilla del 05/05 contradice la ficha), así que el nº3 llega con una pregunta ya sembrada.

## 🔁 EL BUCLE CERRADO — estrenado el 15/08, sigue sin gastar

- Los tildes del usuario tienen **fecha y hora**, y cruzados semanas después contra la fenología del catálogo producen contenido que **ninguna otra fuente puede dar**.
- **Se envió el 15/08 y midió ⬛ — NO se archiva** (ventana ciega). Se re-mide de cero el 24/08. Hoy quedó **linkeado** desde la landing del 17 para darle una segunda chance sin gastar una push.
- **Es un pozo, no una nota suelta.** **Reservar el cruce poda→FRUTA para diciembre-enero** (durazno/ciruela fructifican 12-1-2, pera 2-3).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo». MUERTO.
- **checklist de viaje / «antes de irte» como deberes:** el viaje se trata como **tranquilidad o como ventaja**, nunca como lista de pendientes.
- **vos-decidis / feed-de-decisiones:** el eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).
- 🆕 **Confirmado por el rebote del 16/08:** feed falso y superpoderes (era gimmick) no retienen ni cuando el usuario los abre por voluntad propia. **9 s / 28 % de scroll.**

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín. Reconfirmada el 16/08 desde el ángulo contrario (ver arriba).
- **Ayudarlo a HACER > informarlo.** Cuando NO puede hacer (viaje), lo más cercano es **mostrarle lo que YA hizo dando resultado** (usado 15/08), o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo** (usado 17/08).
- **Reencuadrar un pendiente como una decisión bien tomada** es una jugada nueva y potente (17/08): seis fichas «a confirmar» dejan de ser desprolijidad y pasan a ser «esperaste el dato bueno en vez de anotar el fácil». **Convierte deuda en mérito sin mentir.**
- **El dato computado sobre su propio catálogo es munición sin explotar.** 52 fichas × 20 campos + el log con hora de sus acciones. Usados: floración (08/08), fruta (10/08), acción→floración (15/08), **campos «a confirmar» (17/08)**. Sin usar: dependencia de un solo ejemplar, luz real vs ficha, calendario de perfume.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1.
- **Timing verificado > urgencia inventada** — y **número re-verificado > número lindo**. Cuarta corrida seguida re-verificando. Lo que aguanta se reafirma; **lo que se movió se corrige de frente al pie**.
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal tarea ES contenido: la promesa cumplida se cobra el 24/08.
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla. **FOTOS REALES = need validado.** Diagrama propio > párrafo.
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco.
- ⚠️ **Lección del 15/08 (vigente):** una decisión guardada en learnings **NO anula el ledger** — el ledger se consulta igual y gana.
- ⚠️ **Quemados al 17/08:** **B-13, B-20, B-2/B-2B/B-2C, B-43, B-45, B-49 + B-47 y B-48 hasta el 24/08** (consumidos hoy) · **B-30, B-35, B-38, F-4, B-39, B-32 hasta el 22/08** (del 15/08) · romero B-26 vedado para fun_fact hasta fines de agosto.
- **Elenco INTACTO para sáb 22 y la reentrada (≥18 días de descanso):** pindó B-8, mirto B-27, guayabo F-1, podranea F-2, gardenia B-25, pata de vaca B-42, anacahuita B-16, santa rita B-1, evónimo B-44, azarero B-7, mandioca B-34, madreselva B-40, aguaribay F-8, palta uruguaya B-22, vivero B-46, cinta B-12, esparraguera B-6, coronita F-5, fresno F-10, ligustro F-9. Ya libres además: B-24, B-36, B-23, B-9, B-18, B-5a/b, B-10, F-7, B-29, B-3, I-1, I-2, B-4, B-14, B-15, F-3.
- **No repetir en <14 días:** el gráfico de 12 meses de FLORACIÓN (libre 22/08) · la tira de 12 meses de FRUTA (libre 24/08) · el par «32 vs 1» · el «3 → 2» · el «6 → 4» y el circuito reserva→tijera→flor (libres el 29/08) · las 4 candidatas (camelia/aloe/salvia leucantha/jazmín de invierno) · y desde hoy **la bifurcación del trifoliado, la clave por olor de B-45, la contradicción flor-amarilla del pitósporo y el bloque «hoja converge por ambiente, flor no»** (libres el 31/08).
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas → EJECUTADO. Liquidámbar B-37 → hecho.
- **01/08:** «mándamela cuando esté lindo» → EJECUTADO 02/08 con verificación meteorológica.
- **02/08:** «¿qué más puedo podar? ¿qué hago con el neem?» → contestado 02/08 + Taller nº2 el 03/08.
- **03/08:** «recordame las podas… si no llueve» → EJECUTADO 04/08.
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.

## 📈 Estado del sistema + jardín (17/08/2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable.
- **Silencio de push roto por navegación propia el 16/08** (ver bloque 🚨). Último evento de push-click: 04/08 00:14.
- Threads (`docs/sync/threads/`): **0 mensajes pendientes** (el último del usuario es del 30/07). `user_tasks.json`: 1 entry sin `ai_answer` pero es la contenedora `tasks`, no una pregunta. `uploads.json`: **0 pendientes** (última foto 30/07, B-30).
- Sin responder: `podas-previaje`, `viaje-silencio`, `horario-tareas`. Los tres son insumo de la reentrada.
- Jardín en DORMANCIA, **saliendo: los 4 frutales podados están abriendo flor**. **37 días al equinoccio (23/09).** Helada posible hasta fin de agosto (ninguna en el pronóstico a 14 días), pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado = «más flor»**.
- Compactación 17/08: engagement.json 52→30 eventos (02/08 al `daily_summary` **preservando el 2º 😍 del Taller, el `el-taller-slot-sab11:si`, los 7/7 pasos, los 3 ticks de poda reales y el feedback del neem**), send_log 9→7, queue reescrita con 1 sola entry. Nada perdido.

## Conclusiones de los push (por feedback real)

- **17/08 — preguntas-abiertas (hoy, 18:00): los 6 expedientes de identidad abiertos.** Primera experiencia armada sobre lo que el catálogo NO sabe. Apuesta: agencia a costo cero + sustancia botánica dura (por qué la hoja converge y la flor no) + un tap que produce trabajo MÍO. Se mide el 18.
- **15/08 — florecio-lo-que-podaste: ⬛ CERO APERTURA a 48 h — VEREDICTO SUSPENDIDO.** Y ahora sabemos algo más: el 16 el usuario entró al sitio solo y **aun así no la abrió**. Eso no la condena (fue por `ideas.html`, no por la cola de notificaciones), pero baja un poco la confianza en que el ⬛ sea 100 % ausencia. Se re-mide de cero el 24/08. El pronóstico que publicó se sostuvo a 48 h con una corrección de 0,6 °C, anotada.
- **16/08 — domingo sin slot: 0 push por diseño.** Y fue el día en que el usuario volvió solo. **Argumento fuerte a favor de la cadencia baja: el espacio vacío no lo alejó, volvió sin que lo llamaran.**
- **13/08 y 20/08 — jueves, slot de tarea VACÍO a propósito.** 3º y 6º del compromiso. El valor se cobra el 24/08.
- **10/08 — la-ultima-mandarina: ⬛ VEREDICTO SUSPENDIDO.** El tap `mandarina-parte-vuelta` NO se activó → **el parte de vuelta del 22/08 no es deuda comprometida**, se decide por contenido.
- **08/08 — el-hueco: ⬛ VEREDICTO SUSPENDIDO.** NO se archiva el eje-objetivo ni el formato auditoría-computada.
- **06/08 — jardin-hoy «cierre»: ⬛.** Contenido honesto pero 4º jardin-hoy en 6 días: **repetición de formato**, no mala hora.
- **04/08 — tarjeta-campo: ⬛ sin testear.** Cayó en la víspera del silencio. **Re-test a la vuelta, primera semana.**
- **03/08 — el-taller-2: MASOMENOS-ALTO.** 7/7 pasos + dwell 166 s + un pedido concreto, cero reacción. Abrió a los **32 min**.
- **02/08 — el-taller re-push: ÉXITO MÁXIMO.** 😍 + 2º slot + **3 ticks de poda reales**. Verificar la condición del mundo real fue determinante.
- **31/07 — el-parte: MASOMENOS con veredicto claro.** Formato-diario archivado.
- **30/07 — jardin-hoy GANADORA, día tier-1.** 3 feedback_text, los tres ejecutados.
- **Patrón agregado (13 pushes, 30/07 al 17/08):** las 3 que ganaron señal activa traían **ayuda técnica ejecutable sobre sus plantas con la herramienta en la mano**. Las 6 ⬛ son todas del período 04-15/08 = ausencia física. La única derrota con evidencia limpia sigue siendo `el-parte` (formato-diario).

## TODO / próximos experimentos

- **JUEVES 20/08 — 6º slot de tarea vacío.** Mantenimiento puro, 0 push. Re-verificar el parte.
- **SÁBADO 22/08 (11:00) — último slot del viaje.** Vuelve el 23. Lugar natural del **parte de vuelta**, pero **sin deuda previa** (el tap del 10/08 no se activó): se gana por contenido. **Cast disponible: el elenco intacto de arriba** — B-13/B-20/B-2/B-43/B-45/B-49 quedan quemados hasta el 24.
- **Si prendió `abiertas-agenda`:** armar la agenda de las 6 ventanas (clivia ~1ª semana de setiembre · B-20 al brotar, set-oct · jazmín B-2, B-43, B-45 en octubre · B-49 oct-nov) y mandar **una línea** la semana justa de cada una. **Verificar el evento antes de asumirlo.**
- **Si prendió `abiertas-fotos-hoja`:** el 24/08 va un recordatorio único pidiendo foto de UNA hoja de B-47 y de B-48 con escala. Cierra dos expedientes el mismo día.
- **Si prendió `florecio-foto-23`:** el 23/08 va un recordatorio de UNA línea pidiendo la foto del durazno en flor, y el 24 el veredicto de poda.
- **LUNES 24/08 — reentrada.** ① Leer `podas-previaje` y armar la lista real ② aplicar `horario-tareas` si contestó ③ **Taller nº3 = pitósporo B-43** (que ya quedó sembrado como expediente abierto) ④ preguntar por las estacas ⑤ hortensia el 29-30/08, la única con reloj ⑥ pagar las deudas de los taps que hayan prendido ⑦ **cobrar la promesa cumplida: 17 días, 7 slots de tarea, cero pushes** ⑧ re-medir de cero todo lo suspendido (el-hueco, mandarina, tarjeta-campo, florecio, preguntas-abiertas).
- **Cantera de auditorías computadas** (reentrada, mismo motor, dato nuevo): un solo ejemplar (44/52) · reparto real de luz frente/fondo/interior vs lo que pide cada ficha · el calendario de PERFUME (9 especies, oct-dic) · **el bucle cerrado poda→FRUTA en diciembre-enero**.
- **Idea nueva del 16/08:** el usuario llega a las experiencias por `ideas.html`. Evaluar en la reentrada si conviene **ordenar ahí las experiencias buenas y retirar las de la era gimmick** — fue a buscar y encontró lo peor del archivo. (No tocar durante el viaje.)
