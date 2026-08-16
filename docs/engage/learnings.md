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

## ✈️ CONTEXTO DOMINANTE — **VIAJE 7 AL 23 DE AGOSTO** (hoy = día 10, 16/08)

- **Compromiso publicado el 06/08, a cumplir a rajatabla: del 7 al 23 NO se manda NINGUNA push de tareas.** Adentro caen 7 slots (sáb 8 ✅, lun 10 ✅, jue 13 ✅, sáb 15 ✅, **faltan lun 17, jue 20, sáb 22**). **4 de 7 cumplidos**; los 3 que quedan salen solos si la cola queda vacía esos días. **Romperlo quema el activo más caro que tengo.**
- **El compromiso es SOBRE TAREAS, no sobre experiencias.** `viaje-silencio` sigue **sin contestar** → rige el default: **0 tareas + experiencia solo si es lectura placentera, cero-deber y con listón alto.** Releerlo antes de lun 17 y sáb 22.
- **⚠️ El viaje NO es ventana de medición (regla 09/08, reconfirmada cada corrida).** **12 días sin un solo evento** (último: 04/08 00:15). Un ⬛ durante el viaje **mide disponibilidad, no contenido**. **Ningún eje ni formato se archiva con evidencia recogida entre el 07 y el 23.** Todo veredicto suspendido hasta la reentrada del 24/08.
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b). **Excepción: la hortensia sí tiene reloj → 29-30/08, antes del brote.**
- ✅ Cerradas: pera B-39 y liquidámbar B-37 (en `task_states.json`) + durazno B-30/35, ciruela B-38 y ciruelo F-4 **por tick propio del usuario** (02/08). ⚠️ Los ticks del Taller (`taller-arbol-*`, `podo-*`) **NO escriben `task_states.json`** — el archivo las muestra `active`. **No contradecir al usuario: para él están hechas.**
- **Chequeo de vencimientos (sigue válido):** ninguna ventana abierta se cierra antes del 23. La más apurada es **abelia F-7, límite fin de agosto**. Vuelve con margen real.
- **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** B-41 caqui NO se nombra como urgencia hasta primavera (pedido del usuario).
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (**shape real: `{"tasks": {...}}`**), no contra la edición anterior de la página.

## 🌧️ PARTE RE-VERIFICADO 16/08 (open-meteo, MVD) — ✅ POR FIN SE SOSTIENE

| Fecha | Mín | Máx | Lluvia |
|---|---|---|---|
| 16/08 | 11,6 | 14,5 | 1,3 mm |
| 17/08 | 9,9 | 11,7 | **6,9 mm** |
| 18/08 | 9,4 | 9,8 | 1,2 mm |
| 19-21/08 | 7,8-8,9 | 10,5-12,5 | **0 mm** |
| 22-23/08 (vuelta) | 6,5-6,6 | **8,5-9,2** | 6,6 mm |
| 24-25/08 | 4,9-7,5 | 9,4-10,3 | 0 mm |

- ✅ **Primera corrida en tres sin corrección.** Lo que se PUBLICÓ ayer sigue en pie a 24 h: máximas de **8,5 a 12,5 °C del 17 al 23** (ayer decía 9,3-12,0 → si algo, más frío todavía) y **cero heladas en 10 días**, con mínima absoluta **4,9 °C el 25/08** (ayer: 4,8 el 25). **La tesis del «frío que alarga la floración» NO quedó desmentida** — hay chance real de flor abierta al volver.
- La lluvia 16→23 se movió de 9,7 a **16,0 mm** (+65%). **No importa: no se publicó.** Es justo la razón por la que se descartó — dos correcciones seguidas (90 → 45 → 9,7 → 16,0 mm) prueban que **el número de lluvia a >72 h es basura**.
- **Regla dura confirmada por tercera vez: un pronóstico a >72 h NO es dato publicable.** Solo se publica lo que sigue en pie el día que se encola. **Corolario nuevo (16/08): lo que sí se sostiene en la re-verificación se puede REAFIRMAR** — y reafirmar un número que ya diste es capital de credibilidad gratis.
- **Lunes 17: 6,9 mm y máxima 11,7.** Aunque el usuario estuviera acá, no sería día de jardín. La experiencia del lunes va **cero-deber**, sin excepción.

## 🕐 LA HORA — hipótesis corregida el 08/08

| Envío real (MVD) | Push | 1ª apertura | Resultado |
|---|---|---|---|
| **Sáb 01/08 12:06** | **el-taller** | +2 h 08 | **🏆 ÉXITO MÁXIMO** |
| **Dom 02/08 11:07** | **el-taller re-push** | +4 h | **🏆 ÉXITO (😍 + 2º slot)** |
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

## 🔁 EL BUCLE CERRADO — munición estrenada el 15/08, VIVA y sin gastar

- Los tildes del usuario tienen **fecha y hora**, y cruzados semanas después contra la fenología del catálogo producen contenido que **ninguna otra fuente puede dar**: «esto que pasa hoy lo produjiste vos el 2 de agosto a las 14:25».
- Primera vez que el protagonista **no es una planta ni un dato de ficha, sino el trabajo del propio usuario**. Ataca la regla #1 desde el ángulo de máxima recompensa y **con cero-deber**.
- **Se envió el 15/08 y midió ⬛ — NO se archiva** (ventana ciega del viaje). Se re-mide de cero el 24/08.
- **Es un pozo, no una nota suelta.** Cada tick futuro habilita un cruce nuevo. **Reservar el cruce poda→FRUTA para diciembre-enero** (durazno/ciruela fructifican 12-1-2, pera 2-3): es el mismo bucle cobrando la segunda cuota.
- Requisito: el cruce tiene que ser **verificable en ambos extremos** (tick real + ventana real de ficha).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo». MUERTO.
- **checklist de viaje / «antes de irte» como deberes:** el viaje se trata como **tranquilidad o como ventaja**, nunca como lista de pendientes.
- **vos-decidis / feed-de-decisiones:** el eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín.
- **Ayudarlo a HACER > informarlo.** Cuando NO puede hacer (viaje), lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR** con un tap que produce trabajo mío, no suyo.
- **El dato computado sobre su propio catálogo es munición sin explotar.** 52 fichas × 20 campos + **el log con hora de sus propias acciones**. Usados: floración (08/08), fruta (10/08), acción→floración (15/08). Sin usar: dependencia de un solo ejemplar, luz real vs ficha, especies sin identificar, calendario de perfume.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1.
- **Timing verificado > urgencia inventada** — y **número re-verificado > número lindo**. Tres corridas seguidas re-verificando (90→45→9,7→16,0 mm) dejaron una regla y un corolario: el pronóstico se re-verifica el día que se encola **o no se publica**; y **cuando aguanta, se reafirma** (16/08).
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal tarea ES contenido: la promesa cumplida se cobra el 24/08.
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla. **FOTOS REALES = need validado.** Diagrama propio > párrafo.
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco.
- ⚠️ **Lección del 15/08 (vigente):** learnings traía escrito, como decisión tomada y «no re-litigar», hacer protagonista al viraró B-32 con el fun_fact de los sépalos rosados; el ledger mostró que ese ángulo ya se había usado 4 veces (la última hacía 7 días). **Una decisión guardada NO anula el ledger — el ledger se consulta igual y gana.**
- ⚠️ **Quemados al 16/08:** **B-30, B-35, B-38, F-4, B-39 y B-32 hasta el 22/08** (consumidos el 15/08 — NINGUNO puede protagonizar el lunes 17) · romero B-26 vedado para fun_fact hasta fines de agosto. **Liberados a partir del 17/08:** B-24, B-36, B-23. Ya libres: B-9, B-18, B-5a/b, B-10, F-7, B-29, B-3, I-1, I-2.
- **No repetir en <14 días:** el gráfico de 12 meses de FLORACIÓN (libre 22/08), la tira de 12 meses de FRUTA (libre 24/08), el par «32 vs 1», el «3 → 2», el «6 → 4» y el circuito reserva→tijera→flor (libres el 29/08), y las 4 candidatas (camelia / aloe / salvia leucantha / jazmín de invierno).
- **Elenco INTACTO para lun 17, sáb 22 y la reentrada:** pindó B-8, mirto B-27, guayabo F-1, pitósporo B-43, podranea F-2, gardenia B-25, clivia B-13, pata de vaca B-42, anacahuita B-16, santa rita B-1, hortensia B-5b, lapachillo B-14, evónimo B-44, azarero B-7.
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

## 📈 Estado del sistema + jardín (16/08/2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable → el silencio es real, no un bug.
- **Silencio total del usuario desde el 04/08 00:15 (12 días, 0 eventos).** Explicado por víspera + viaje. **No sobre-interpretar como rechazo.**
- Threads (`docs/sync/threads/`): **0 mensajes pendientes**, el último del usuario es del 30/07. `user_tasks.json`: 1 entry sin `ai_answer` pero es la contenedora `tasks`, no una pregunta → nada que contestar. `uploads.json`: **0 pendientes** (última foto 30/07, B-30).
- Sin responder: `podas-previaje`, `viaje-silencio`, `horario-tareas`. Los tres son insumo de la reentrada.
- Jardín en DORMANCIA, **saliendo: los 4 frutales podados están abriendo flor**. ~38 días al equinoccio (23/09). Helada posible hasta fin de agosto (ninguna en el pronóstico a 10 días), pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado = «más flor»**.
- Compactación 16/08: engagement.json 73→46 eventos (se fue el 01/08 al `daily_summary` **preservando su 😍, su `el-taller-slot-lun18:si`, su feedback «Genial esto…» y los dwells de 168 s@95% y 30 s@100%**), send_log 11→9, queue reescrita vacía. Nada perdido.

## Conclusiones de los push (por feedback real)

- **15/08 — florecio-lo-que-podaste: ⬛ CERO APERTURA a 24 h — VEREDICTO SUSPENDIDO.** Enviada 11:19 (lag 19 min). 0 clicks/taps/slots/feedback. **NO se archiva:** ventana ciega del viaje. Lo único medible que dejó: el pronóstico que publicó **se sostuvo a 24 h**, así que no hay deuda de credibilidad. El bucle cerrado sigue entero para el 24/08.
- **14/08 — viernes sin slot: 0 push por diseño.** Detectó que un número de la memoria estaba viejo. El 15 resultó que **seguía viejo**. El 16 resultó que **el reemplazo también se movió** (9,7→16,0 mm). Tres por tres: el valor de las corridas de mantenimiento es exactamente ese.
- **13/08 — jueves, slot de tarea VACÍO a propósito: 3º de 7 del compromiso.** El valor se cobra el 24/08.
- **10/08 — la-ultima-mandarina: ⬛ VEREDICTO SUSPENDIDO** (0 clicks/taps/slots). El tap `mandarina-parte-vuelta` NO se activó → **el parte de vuelta del 22/08 no es deuda comprometida**, se decide por contenido.
- **08/08 — el-hueco: ⬛ VEREDICTO SUSPENDIDO.** **NO se archiva el eje-objetivo ni el formato auditoría-computada.**
- **06/08 — jardin-hoy «cierre»: ⬛.** Contenido honesto pero 4º jardin-hoy en 6 días: **repetición de formato**, no mala hora.
- **04/08 — tarjeta-campo: ⬛ sin testear.** Cayó en la víspera del silencio. **Re-test a la vuelta, primera semana.**
- **03/08 — el-taller-2: MASOMENOS-ALTO.** 7/7 pasos + dwell 166 s + un pedido concreto, cero reacción. Abrió a los **32 min**.
- **02/08 — el-taller re-push: ÉXITO.** 😍 + prendió el 2º slot + ticks B-30/B-38. Verificar la condición del mundo real fue determinante.
- **02/08 — que-mas-podo: SIN reacción pero CON acción.** Podó F-4. **El clic no es la métrica; el tick sí.**
- **31/07 — el-parte: MASOMENOS con veredicto claro.** Formato-diario archivado.
- **30/07 — jardin-hoy GANADORA, día tier-1.** 3 feedback_text, los tres ejecutados.
- **Patrón agregado (12 pushes, 30/07 al 15/08):** las 3 que ganaron señal activa traían **ayuda técnica ejecutable sobre sus plantas con la herramienta en la mano**. Las 6 ⬛ son todas del período 04-15/08 = ausencia física, no contenido. La única derrota con evidencia limpia sigue siendo `el-parte` (formato-diario).

## TODO / próximos experimentos

- **LUNES 17/08 (18:00) — slot de experiencia dentro del viaje.** Slot de TAREA vacío (5º de 7). Reglas del viaje: cero-deber, listón alto, elenco intacto. **Prohibido el cast del 15/08** (B-30/35/38/F-4/B-39/B-32, quemados hasta el 22). **NO reusar** el bucle cerrado (recién estrenado). **NO quemar** la auditoría «un solo ejemplar» ni el calendario de PERFUME — se reservan para la reentrada, donde sí miden. Meteo del lunes: 6,9 mm y máxima 11,7 → nada de jardín aunque estuviera acá.
- **JUEVES 20/08 — 6º slot de tarea vacío.** Mantenimiento puro.
- **SÁBADO 22/08 (11:00) — último slot del viaje.** Vuelve el 23. Lugar natural del **parte de vuelta**, pero **sin deuda previa** (el tap del 10/08 no se activó): se gana por contenido.
- **Si prendió `florecio-foto-23`:** el 23/08 va un recordatorio de UNA línea pidiendo la foto del durazno en flor, y el 24 el veredicto de poda. Verificar el evento antes de asumirlo.
- **LUNES 24/08 — reentrada.** ① Leer `podas-previaje` y armar la lista real ② aplicar `horario-tareas` si contestó ③ **Taller nº3 = pitósporo B-43** ④ preguntar por las estacas ⑤ hortensia el 29-30/08, la única con reloj ⑥ pagar las deudas de los taps que hayan prendido ⑦ **cobrar la promesa cumplida: 17 días, 7 slots de tarea, cero pushes** ⑧ re-medir de cero todo lo suspendido (el-hueco, mandarina, tarjeta-campo, florecio).
- **Cantera de auditorías computadas** (reentrada, mismo motor, dato nuevo): un solo ejemplar (44/52) · reparto real de luz frente/fondo/interior vs lo que pide cada ficha · las 5 especies sin identificar como «causas abiertas» · el calendario de PERFUME (9 especies, oct-dic) · **el bucle cerrado poda→FRUTA en diciembre-enero**.
