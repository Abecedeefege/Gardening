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
- **Aprobación = recurrencia.** Solo vuelve lo que el usuario prendió (😍 / slot en «sí» / `engageApprove`). Pending sin aprobar no se borra: simplemente no recurre.
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo»), la condición se **verifica con datos reales** antes de encolar y se muestra citada.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## 🚨 EL HALLAZGO DEL 18/08 — **EL «CERO SEÑAL» ERA UN BUG DE LAYOUT, NO DESINTERÉS**

`preguntas-abiertas` (17/08) dio el mejor y el peor número de la misma corrida: **abierta a los 2 min 03 s** (récord absoluto; el anterior era 32 min, y rompe la racha de 5 pushes sin abrir) y **dwell 31 s @ 41 % de scroll**, cero taps. Su primer control estaba al **83 %**: nunca tuvo un botón a la vista.

**Arreglo ya en main (18/08):** `engage.js` inyecta una **barra flotante de señal rápida** — aparece al 25 % de scroll (o a los 25 s), ofrece 😍 / 🙂 / 🙅 + atajo «✍️ Escribir», se auto-elimina si el bloque de reacción real entra en pantalla, descartable con ✕, no reaparece donde ya hubo señal. Emite el **mismo** evento `reaction` + `via: "quickbar"`. Probado con Playwright a 390×780. Re-verificado hoy 20/08 (`node --check` OK, la barra sigue en el archivo servido).

**Regla dura:** **ninguna experiencia puede tener su primer control interactivo debajo del 35 % del scroll.**

### 📏 AUDITORÍA MEDIDA 20/08 — dónde cae el primer control en TODO el archivo

| Página | 1er control | Lectura real |
|---|---|---|
| **jardin-hoy** (canal tarea) | **32 %** ✅ | única compliant |
| tarjeta-campo | 54 % | ⬛ (ventana ciega) |
| el-hueco 65 % · el-parte 66 % · tu-semana 69 % · el-taller-2 73 % | 54-73 % | zona gris |
| mandarina 77 % · florecio 79 % · asamblea 81 % · **preguntas-abiertas 83 %** | ≥77 % | murió al 41 % |
| **el-taller 89 % · que-mas-podo 89 %** | 89 % | 🏆 **ganaron igual** |

**Lo que la tabla enseña (y corrige a la regla #2):** el control alto no gana — la **sustancia** gana. `el-taller` tiene el peor layout del archivo (89 %) y es la mejor push de la historia del canal, porque el usuario leyó los 168 s enteros. La regla #2 es un **seguro contra la lectura corta**, no un sustituto de la regla #1. Se aplica igual, porque el costo de equivocarse es una lectura entera perdida.

**Acción concreta que dejó la auditoría:** antes del próximo re-push de **`el-taller` (aprobada, 24/08)** hay que **subirle un control por arriba del 35 %** — hoy depende de que la lectura llegue completa.

## ✈️ CONTEXTO DOMINANTE — **VIAJE 7 AL 23 DE AGOSTO** (hoy = día 14, 20/08)

- **Compromiso publicado el 06/08: del 7 al 23 NO se manda NINGUNA push de tareas.** Adentro caen 7 slots (sáb 8, lun 10, jue 13, sáb 15, lun 17, **jue 20 ✅ = 6 de 7 cumplidos**); queda solo **sáb 22**, que no lleva tarea pero **sí lleva la experiencia de las 11:00**. **Romperlo quema el activo más caro que tengo.**
- **El compromiso es SOBRE TAREAS, no sobre experiencias.** `viaje-silencio` sigue sin contestar → rige el default: **0 tareas + experiencia solo si es lectura placentera, cero-deber y con listón alto.**
- **⚠️ El viaje NO es ventana de medición.** Ningún eje ni formato se archiva con evidencia del 07 al 23. Todo veredicto suspendido hasta la reentrada del 24/08. *(Matiz 18/08: la apertura en 2 min prueba que SÍ está alcanzable — lo no medible es el contenido, no la disponibilidad.)*
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b). **Excepción: la hortensia tiene reloj → 29-30/08, antes del brote.** Ninguna otra ventana se cierra antes del 23; la más apurada es **abelia F-7 (fin de agosto)**, vuelve con margen. **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** Caqui B-41 no se nombra como urgencia hasta primavera.
- ✅ Cerradas: pera B-39 y liquidámbar B-37 (en `task_states.json`) + durazno B-30/35, ciruela B-38 y ciruelo F-4 **por tick propio del usuario** (02/08). ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo las muestra `active`. **No contradecir al usuario: para él están hechas.**
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (**shape real: `{"tasks": {...}}`**), no contra la edición anterior de la página.

## 🌧️ PARTE RE-VERIFICADO 20/08 (open-meteo, MVD) — 7ª vez, con una corrección grande

| Fecha | Mín | Máx | Lluvia | Viento |
|---|---|---|---|---|
| 20/08 | 10,3 | 12,8 | 0,1 mm | **39 km/h** |
| 21/08 | 8,4 | 10,2 | 0,7 mm | 39 km/h |
| 22/08 | 8,3 | 10,9 | **0,0** | 29 |
| **23/08 (vuelta)** | 8,0 | 10,5 | **0,0** | 28 |
| 24/08 | **6,4** | **8,8** | 0,0 | 19 |
| 26-28/08 | 9,1-10,8 | 12,3-12,8 | **2,2 / 6,2 / 0** | — |
| 29/08 | 9,5 | **14,2** | 0 | — |

- **Corrección honesta vs ayer:** el «**primer calor 26-28/08**» **se cayó** (era 13,2 / 14,3 / 15,1 → hoy **12,8 / 12,4 / 12,3**) y encima **apareció lluvia** (2,2 + 6,2 mm). El pico de calor se corrió al **29/08 (14,2)**. **Ese dato NO se publica el sábado como número** — séptima confirmación de que a >72 h el número no es publicable.
- **Lo que aguanta 7 corridas en pie:** máximas clavadas en **10-13 °C** toda la ventana, **cero heladas en 12 días** (mínima absoluta 5,3 el 25/08) y **jardín SECO el día de la vuelta** (3ª confirmación seguida de 0,0 mm el 23). → flor lenta, flor que dura, chance real de flor abierta el 23. **Vuelve a un jardín seco y frío, no a un barrial.**
- Novedad menor pero real: **viento de 39 km/h hoy y mañana** — lo más movido de la ventana.
- **Regla dura:** solo se publica lo que sigue en pie el día que se encola. Lo que aguanta se REAFIRMA; **lo que se movió se corrige de frente al pie.**

## 🕐 LA HORA — el contenido decide, la hora modula

| Envío real (MVD) | Push | 1ª apertura | Resultado |
|---|---|---|---|
| **Lun 17/08 18:23** | **preguntas-abiertas** | **+2 min** ⚡ | récord de delay — murió al 41 % |
| Sáb 01/08 12:06 · Dom 02/08 11:07 | el-taller (+ re-push) | +2 h / +4 h | 🏆 ÉXITO MÁXIMO ×2 |
| Lun 03/08 18:48 | el-taller-2 | +32 min | masomenos-alto (7/7 pasos) |
| Sáb 01/08 10:58 · Vie 31/07 18:02 | jardin-hoy · el-parte | +4 h / +1 h 41 | floja · formato muerto |
| 04/08 → 15/08 | tarjeta · jardin-hoy · el-hueco · mandarina · florecio | nunca | ⬛ ×5 — *ausencia, no computan* |

- **La franja 18:00-18:30 del lunes es la mejor puerta de entrada medida** (32 min y 2 min). El sábado 11-12 h dio los dos éxitos máximos. **Ambos slots validados como HORA.**
- ⚠️ **Dispatcher lag: 11 min a 2,7 h** (17/08: 23 min). Encolar en el horario exacto sigue siendo lo correcto.
- ⚠️ `horario-tareas` (06/08) sigue sin contestar. **Leerlo antes de la reentrada.**

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad — y es materia prima de contenido.
- Durante el viaje va **linkeada y en pausa** dentro de la landing del slot, nunca pusheada suelta.
- **Taller nº3 = pitósporo B-43**, reservado para la reentrada — llega con la pregunta ya sembrada (la flor amarilla del 05/05 contradice la ficha).

## 🔁 EL BUCLE CERRADO — estrenado el 15/08, sigue sin gastar

- Los tildes del usuario tienen **fecha y hora**; cruzados semanas después contra la fenología del catálogo dan contenido que **ninguna otra fuente puede dar**.
- Se envió el 15/08 y midió ⬛ — **NO se archiva** (ventana ciega). Re-medición de cero el 24/08.
- **Es un pozo, no una nota suelta. Reservar el cruce poda→FRUTA para diciembre-enero** (durazno/ciruela 12-1-2, pera 2-3).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes:** el viaje es **tranquilidad o ventaja**, nunca lista de pendientes. · **vos-decidis:** el eje AGENCIA vive, el CONTENEDOR repetido se quema. · **mi-objetivo:** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).
- **Era gimmick (feed falso, superpoderes):** el 16/08 los abrió **por voluntad propia** desde `ideas.html` y rebotó en **9 s / 28 %** en los dos. No retienen ni cuando los busca él.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín. *Confirmada por la auditoría del 20/08: las dos ganadoras tienen el PEOR layout del archivo.*
- **EL CONTROL VA ARRIBA (regla #2, 18/08).** Primer tap antes del 35 % de scroll. Es un **seguro contra la lectura corta**, no un sustituto de la #1.
- **Ayudarlo a HACER > informarlo.** Cuando NO puede hacer (viaje), lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **El título es el activo más medido que tengo.** «Tu jardín tiene 6 preguntas abiertas» = 2 minutos. Sustantivo concreto + número + algo que le pertenece.
- **Reencuadrar un pendiente como una decisión bien tomada** (17/08): convierte deuda en mérito sin mentir. Sin veredicto todavía.
- **El dato computado sobre su propio catálogo es munición sin explotar.** 52 fichas × 20 campos + el log con hora de sus acciones. Usados: floración (08/08), fruta (10/08), acción→floración (15/08), campos «a confirmar» (17/08). Sin usar: dependencia de un solo ejemplar, luz real vs ficha, calendario de perfume.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1.
- **Timing verificado > urgencia inventada** — y **número re-verificado > número lindo**.
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal tarea ES contenido: la promesa cumplida se cobra el 24/08.
- **Minimalismo + REAL + VISUAL.** **FOTOS REALES = need validado.** Diagrama propio > párrafo.
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días. **Una decisión guardada en learnings NO anula el ledger: el ledger gana.**
- **Excepción:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco.
- ⚠️ **Quemados:** **B-13, B-20, B-2/B-2B/B-2C, B-43, B-45, B-49, B-47, B-48 hasta el 24/08** · **B-30, B-35, B-38, F-4, B-39, B-32 hasta el 22/08** · romero B-26 vedado para fun_fact hasta fines de agosto.
- **Elenco INTACTO para sáb 22 y la reentrada (≥19 días de descanso):** pindó B-8, mirto B-27, guayabo F-1, podranea F-2, gardenia B-25, pata de vaca B-42, anacahuita B-16, santa rita B-1, evónimo B-44, azarero B-7, mandioca B-34, madreselva B-40, aguaribay F-8, palta uruguaya B-22, vivero B-46, cinta B-12, esparraguera B-6, coronita F-5, fresno F-10, ligustro F-9. Libres además: B-24, B-36, B-23, B-9, B-18, B-5a/b, B-10, F-7, B-29, B-3, I-1, I-2, B-4, B-14, B-15, F-3.
- **No repetir en <14 días:** el gráfico de 12 meses de FLORACIÓN (libre 22/08) · la tira de FRUTA (24/08) · «32 vs 1» · «3 → 2» · «6 → 4» y el circuito reserva→tijera→flor (29/08) · las 4 candidatas (camelia/aloe/salvia leucantha/jazmín de invierno) · la bifurcación del trifoliado, la clave por olor de B-45, la contradicción flor-amarilla del pitósporo y «hoja converge por ambiente, flor no» (31/08).
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas → EJECUTADO. Liquidámbar B-37 → hecho.
- **01-03/08:** «mándamela cuando esté lindo» (ejecutado 02/08 con verificación meteo) · «¿qué más puedo podar? ¿y el neem?» (contestado 02/08 + Taller nº2) · **04/08: «recordame las podas si no llueve» (ejecutado el mismo día; la cita quedó guardada en el `daily_summary` del 04/08 al compactar).**
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.

## 📈 Estado del sistema + jardín (20/08/2026)

- Push subscription `pix9`: **active**; logging vía `/api/feedback` confiable. Threads, `uploads.json` y `user_tasks.json`: **0 pendientes** (lo último del usuario es del 30/07).
- **Cero eventos nuevos en 72 h** (el último es el dwell del 17/08 21:25Z). Ventana ciega de viaje, esperado.
- Sin responder: `podas-previaje`, `viaje-silencio`, `horario-tareas`. Los tres son insumo de la reentrada.
- Jardín en DORMANCIA, **saliendo: los 4 frutales podados están abriendo flor**. **34 días al equinoccio (23/09).** Helada posible hasta fin de agosto (ninguna en el pronóstico a 12 días), pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado = «más flor»**.
- Compactación 20/08: nada que compactar — todos los eventos de `engagement.json` (10) y `send_log.json` (5) están dentro de los 14 días. Queue del 19/08 reemplazada por la nota del 20/08. Nada perdido.

## Conclusiones de los push (por feedback real)

- **17/08 — preguntas-abiertas: MASOMENOS con el mejor dato de timing del canal.** Apertura en **2 min** (récord; rompe 5 ⬛) y muerte al 41 %. Causa medida: **controles al 83 %**. **Tercer reconteo 20/08 (72 h): cero eventos nuevos — el 41 % fue el techo real.** Veredicto de contenido suspendido al 24/08.
- **15/08 — florecio-lo-que-podaste: ⬛ a 120 h, VEREDICTO SUSPENDIDO.** Quedó linkeada al 94 % del documento del 17: **no es rechazo, es no-exposición**. Re-push propia el 24/08.
- **16/08 — domingo sin slot: 0 push por diseño, y el usuario volvió SOLO al sitio** (src=direct, desde `ideas.html`). **El espacio vacío no lo aleja** — argumento fuerte a favor de la cadencia baja. Pero abrió las dos peores del archivo y rebotó en 9 s.
- **13, 18, 19 y 20/08 — días sin push cumplidos.** El 20/08 es el **6º de 7 slots de tarea del viaje cumplido en silencio**; queda solo el sáb 22 (sin tarea).
- **10/08 mandarina · 08/08 el-hueco · 04/08 tarjeta-campo · 06/08 jardin-hoy: ⬛ SUSPENDIDOS** (ventana ciega). El tap `mandarina-parte-vuelta` NO se activó → **el parte de vuelta del 22/08 no es deuda comprometida**. · **03/08 el-taller-2: MASOMENOS-ALTO** (7/7 pasos, dwell 166 s, cero reacción).
- **02/08 — el-taller re-push: ÉXITO MÁXIMO** (😍 + 2º slot + 3 ticks de poda reales; verificar la condición del mundo real fue determinante). · **31/07 — el-parte: formato-diario archivado.** · **30/07 — jardin-hoy GANADORA, día tier-1** (3 feedback_text, los tres ejecutados).
- **Patrón agregado (14 pushes, 30/07 al 17/08):** las 3 con señal activa traían **ayuda técnica ejecutable con la herramienta en la mano**. Las 6 ⬛ son del período 04-15/08 = ausencia física. La única derrota con evidencia limpia sigue siendo `el-parte`. **Y al menos un «masomenos» era artefacto de layout** — sospechar de los otros antes de archivarlos.

## TODO / próximos experimentos

- **SÁBADO 22/08 (11:00) — último slot del viaje y única push de la semana.** **Estrena la regla #2: primer tap antes del 35 %.** Materia prima verificada 7 veces: vuelve a un jardín **seco** (0,0 mm el 22 y el 23, tercera confirmación) y **frío parejo, 10-13 °C, cero heladas**. ⚠️ **NO usar el número del «primer calor 26-28»: se cayó hoy** (12,3-12,8 y con lluvia); si se quiere el ángulo «arranca la temporada», va sin cifra o con el 29/08 (14,2) marcado como provisorio. Cast: ≥70 % del elenco intacto del ledger. Sin deuda previa: se gana por contenido.
- **Medir la barra de señal rápida** el 22/08: buscar `via:"quickbar"` en las reacciones y los eventos `quicksignal_dismiss` / `quicksignal_to_text`. Si la señal llega por la barra, la regla #2 queda probada.
- **Deuda técnica concreta (auditoría 20/08):** subirle a **`el-taller`** un control por encima del 35 % **antes** de su re-push del 24/08 (hoy está al 89 %).
- **Si prendió `abiertas-agenda`:** armar la agenda de las 6 ventanas (clivia ~1ª semana de setiembre · B-20 al brotar, set-oct · jazmín B-2, B-43, B-45 en octubre · B-49 oct-nov) y mandar **una línea** la semana justa de cada una. **Verificar el evento antes de asumirlo.**
- **LUNES 24/08 — reentrada.** ① Leer `podas-previaje` y armar la lista real ② aplicar `horario-tareas` si contestó ③ **Taller nº3 = pitósporo B-43** ④ preguntar por las estacas ⑤ hortensia el 29-30/08, la única con reloj ⑥ pagar las deudas de los taps que hayan prendido ⑦ **cobrar la promesa cumplida: 17 días, 7 slots de tarea, cero pushes** ⑧ re-medir de cero todo lo suspendido.
- **Cantera de auditorías computadas** (reentrada): un solo ejemplar (44/52) · reparto real de luz vs lo que pide cada ficha · el calendario de PERFUME (9 especies, oct-dic) · el bucle poda→FRUTA en diciembre-enero.
- **Idea del 16/08:** el usuario llega a las experiencias por `ideas.html`. En la reentrada, **ordenar ahí las buenas y retirar las de la era gimmick**. (No tocar durante el viaje.)
