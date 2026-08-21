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
- **Aprobación = recurrencia.** Solo vuelve lo que el usuario prendió (😍 / slot en «sí» / `engageApprove`). Pending sin aprobar no se borra: simplemente no recurre. **Corolario que hay que respetar el 24/08:** `florecio` y `preguntas-abiertas` NO están aprobadas → **no se re-pushean solas**; como máximo van *linkeadas* dentro de la landing del slot. La regla dura gana sobre la nota vieja que decía «re-push propia el 24/08».
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo»), la condición se **verifica con datos reales** antes de encolar y se muestra citada.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## 🚨 EL HALLAZGO DEL 18/08 — **EL «CERO SEÑAL» ERA UN BUG DE LAYOUT, NO DESINTERÉS**

`preguntas-abiertas` (17/08) dio el mejor y el peor número de la misma corrida: **abierta a los 2 min 03 s** (récord absoluto; rompe la racha de 5 pushes sin abrir) y **dwell 31 s @ 41 % de scroll**, cero taps. Su primer control estaba al **75 %**: nunca tuvo un botón a la vista.

**Arreglo ya en main (18/08):** `engage.js` inyecta una **barra flotante de señal rápida** al 25 % de scroll (o a los 25 s): 😍 / 🙂 / 🙅 + atajo «✍️ Escribir», se auto-elimina si el bloque de reacción real entra en pantalla, descartable con ✕. Emite el mismo evento `reaction` + `via: "quickbar"`. Re-verificada hoy 21/08 en Chromium: sigue viva al pie de `el-taller`.

**Regla dura:** **ninguna experiencia puede tener su primer control interactivo debajo del 35 % del scroll.**

### 📏 LA AUDITORÍA, RE-MEDIDA BIEN (21/08) — y la corrección que obliga

La tabla del 20/08 estaba hecha sobre **offsets de caracteres**, no sobre scroll renderizado. Hoy se re-midió **en Chromium a 390×780** (`playwright-core` + `/opt/pw-browsers/chromium-1194`) y **varios veredictos se dan vuelta**:

| Página | Auditoría 20/08 (chars) | **Medición real 21/08** | Qué cambia |
|---|---|---|---|
| **el-taller** | 89 % | **7,9 %** ✅ | **arreglado hoy** (ver abajo) |
| jardin-hoy · el-taller-2 · tarjeta-campo | 32 / 73 / 54 % | **0 %** ✅ | **ya eran compliant** — su ⬛/masomenos **no** es layout |
| **el-parte** | 66 % | **27,3 %** ✅ | **compliant y perdió igual** → la sustancia manda |
| el-hueco 45 % · mandarina 52 % · florecio 64,5 % · asamblea 68 % · tu-semana 43 % | 54-81 % | 43-68 % ⚠️ | zona gris, menos grave de lo que se creía |
| **preguntas-abiertas** | 83 % | **75 %** ⚠️ | **diagnóstico original EN PIE**: la peor del archivo |
| que-mas-podo | 89 % | 87 % ⚠️ | 🏆 ganó igual |

**Lo que la tabla corregida enseña:** el layout **no explica** los masomenos de `el-taller-2` ni de `tarjeta-campo` (los dos tienen el control al 0 %), y **`el-parte` perdió con layout compliant**. La regla #2 sigue vigente como **seguro contra la lectura corta**, pero queda definitivamente subordinada a la #1. El único caso donde el layout sí explicó el resultado es `preguntas-abiertas`.

**➡️ Regla de método nueva: el % de scroll se mide RENDERIZADO en Chromium 390×780, nunca por offset de caracteres.** El script quedó en el scratchpad; reproducirlo es 15 líneas de `playwright-core` con `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`.

**✅ Deuda saldada hoy:** `el-taller` (aprobada, re-push 24/08) estrenó el bloque **`#arranque`** arriba de todo — pregunta nueva y sin usar: *«¿estás con el árbol adelante?»* (`el-taller-arranque` → `campo` / `lectura`) + atajo «saltar a los pasos». Mide la hipótesis nº2 de por qué ganó el Taller («se abre con la herramienta en la mano») y baja el primer tap a **7,9 %**. Verificado sin errores de JS.

## ✈️ CONTEXTO DOMINANTE — **VIAJE 7 AL 23 DE AGOSTO** (hoy = día 15, 21/08)

- **Compromiso publicado el 06/08: del 7 al 23 NO se manda NINGUNA push de tareas.** Adentro caían 7 slots (sáb 8, lun 10, jue 13, sáb 15, lun 17, jue 20) → **6 de 7 cumplidos**; queda solo **sáb 22**, que no lleva tarea pero **sí lleva la experiencia de las 11:00**. **Romperlo quema el activo más caro que tengo.**
- **El compromiso es SOBRE TAREAS, no sobre experiencias.** `viaje-silencio` sigue sin contestar → rige el default: **0 tareas + experiencia solo si es lectura placentera, cero-deber y con listón alto.**
- **⚠️ El viaje NO es ventana de medición.** Ningún eje ni formato se archiva con evidencia del 07 al 23. Todo veredicto suspendido hasta la reentrada del 24/08. *(Matiz 18/08: la apertura en 2 min prueba que SÍ está alcanzable — lo no medible es el contenido, no la disponibilidad.)*
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b). **Excepción: la hortensia tiene reloj → 29-30/08, antes del brote.** Ninguna otra ventana se cierra antes del 23; la más apurada es **abelia F-7 (fin de agosto)**, vuelve con margen. **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** Caqui B-41 no se nombra como urgencia hasta primavera.
- ✅ Cerradas: pera B-39 y liquidámbar B-37 (en `task_states.json`) + durazno B-30/35, ciruela B-38 y ciruelo F-4 **por tick propio del usuario** (02/08). ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo las muestra `active`. **No contradecir al usuario: para él están hechas.**
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (**shape real: `{"tasks": {...}}`**), no contra la edición anterior de la página.

## 🌧️ PARTE RE-VERIFICADO 21/08 (open-meteo, MVD) — 8ª vez

| Fecha | Mín | Máx | Lluvia | Viento |
|---|---|---|---|---|
| 21/08 | 8,5 | 9,9 | 0,6 mm | 37 km/h |
| **22/08 (el slot)** | 8,5 | 10,8 | **0,0** | 30 |
| **23/08 (vuelta)** | 8,0 | 10,6 | **0,0** | 29 |
| 24/08 | **7,0** | **8,7** | 0,0 | 20 |
| 25/08 | **5,4** | 11,0 | 0,0 | 21 |
| 26-27/08 | 7,7-10,7 | 15,4 / 11,4 | 1,2 / 1,2 | — |
| 31/08 | 12,4 | 14,9 | 0,0 | 22 |

- **Lo que aguanta 8 corridas en pie (esto SÍ se publica):** máximas clavadas en **9-11 °C** toda la ventana, **cero heladas en 14 días** (mínima absoluta 5,4 el 25/08) y **jardín SECO el 22 y el 23** — **4ª confirmación seguida**. → **vuelve a un jardín seco y frío, no a un barrial**, con flor lenta que dura.
- **Corrección honesta, 3ª vez que se mueve:** el «primer calor» saltó otra vez de día — ayer el pico era el 29/08 (14,2), hoy el **26/08 marca 15,4** (ayer 12,3) y el 29 bajó a 12,3. **Esa cifra NO se publica el sábado, en ninguna forma.**
- **Regla dura:** solo se publica lo que sigue en pie el día que se encola. Lo que aguanta se REAFIRMA; **lo que se movió se corrige de frente al pie.** A >72 h, el número no es publicable — ocho corridas seguidas confirmándolo.

## 🕐 LA HORA — el contenido decide, la hora modula

| Envío real (MVD) | Push | 1ª apertura | Resultado |
|---|---|---|---|
| **Lun 17/08 18:23** | **preguntas-abiertas** | **+2 min** ⚡ | récord de delay — murió al 41 % |
| Sáb 01/08 12:06 · Dom 02/08 11:07 | el-taller (+ re-push) | +2 h / +4 h | 🏆 ÉXITO MÁXIMO ×2 |
| Lun 03/08 18:48 | el-taller-2 | +32 min | masomenos-alto (7/7 pasos) |
| Sáb 01/08 10:58 · Vie 31/07 18:02 | jardin-hoy · el-parte | +4 h / +1 h 41 | floja · formato muerto |
| 04/08 → 15/08 | tarjeta · jardin-hoy · el-hueco · mandarina · florecio | nunca | ⬛ ×5 — *ausencia, no computan* |

- **Lunes 18:00-18:30 = la mejor puerta de entrada medida** (32 min y 2 min); sábado 11-12 h dio los dos éxitos máximos. **Ambos slots validados como HORA.**
- ⚠️ **Dispatcher lag: 11 min a 2,7 h** (17/08: 23 min). Encolar en el horario exacto sigue siendo lo correcto.
- ⚠️ `horario-tareas` (06/08) sigue sin contestar. **Leerlo antes de la reentrada.**

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios en vez de texto. **La hipótesis ② ahora se mide sola** con `el-taller-arranque`.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad — y es materia prima de contenido.
- Durante el viaje va **linkeada y en pausa** dentro de la landing del slot, nunca pusheada suelta.
- **Taller nº3 = pitósporo B-43**, reservado para la reentrada — llega con la pregunta ya sembrada (la flor amarilla del 05/05 contradice la ficha).

## 🔁 EL BUCLE CERRADO — estrenado el 15/08, sigue sin gastar

- Los tildes del usuario tienen **fecha y hora**; cruzados semanas después contra la fenología del catálogo dan contenido que **ninguna otra fuente puede dar**.
- Se envió el 15/08 y midió ⬛ — **NO se archiva** (ventana ciega). Re-medición de cero el 24/08.
- **Es un pozo, no una nota suelta. Reservar el cruce poda→FRUTA para diciembre-enero** (durazno/ciruela 12-1-2, pera 2-3).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. *(21/08: y su layout era compliant al 27 % — murió por contenido, no por botones.)* · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes:** el viaje es **tranquilidad o ventaja**, nunca lista de pendientes. · **vos-decidis:** el eje AGENCIA vive, el CONTENEDOR repetido se quema. · **mi-objetivo:** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).
- **Era gimmick (feed falso, superpoderes):** el 16/08 los abrió **por voluntad propia** desde `ideas.html` y rebotó en **9 s / 28 %** en los dos. No retienen ni cuando los busca él.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín. *Reforzada por la re-medición del 21/08: `el-parte` perdió con el control al 27 % y `el-taller` ganó con el control al 89 %.*
- **EL CONTROL VA ARRIBA (regla #2, 18/08).** Primer tap antes del 35 % **medido en Chromium 390×780**. Es un **seguro contra la lectura corta**, no un sustituto de la #1.
- **Ayudarlo a HACER > informarlo.** Cuando NO puede hacer (viaje), lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **El título es el activo más medido que tengo.** «Tu jardín tiene 6 preguntas abiertas» = 2 minutos. Sustantivo concreto + número + algo que le pertenece.
- **Reencuadrar un pendiente como una decisión bien tomada** (17/08): convierte deuda en mérito sin mentir. Sin veredicto todavía.
- **El dato computado sobre su propio catálogo es munición sin explotar.** 52 fichas × 20 campos + el log con hora de sus acciones. Usados: floración (08/08), fruta (10/08), acción→floración (15/08), campos «a confirmar» (17/08). Sin usar: dependencia de un solo ejemplar, luz real vs ficha, calendario de perfume.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1.
- **Timing verificado > urgencia inventada** — y **número re-verificado > número lindo**.
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal tarea ES contenido: la promesa cumplida se cobra el 24/08.
- **Minimalismo + REAL + VISUAL.** **FOTOS REALES = need validado.** Diagrama propio > párrafo.
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.
- **Y una del 21/08: antes de archivar un formato, verificar la medición que lo condena.** Una auditoría hecha con el proxy equivocado casi archiva tres formatos por un problema que no tenían.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días. **Una decisión guardada en learnings NO anula el ledger: el ledger gana.**
- **Excepción:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco.
- ⚠️ **Quemados:** **B-13, B-20, B-2/B-2B/B-2C, B-43, B-45, B-49, B-47, B-48 hasta el 24/08** · **B-30, B-35, B-38, F-4, B-39, B-32 se liberan el 22/08** (pero no hace falta tocarlos: recién cumplen) · romero B-26 vedado para fun_fact hasta fines de agosto.
- **Elenco INTACTO para sáb 22 y la reentrada (≥20 días de descanso, 3 corridas sin consumir):** pindó B-8, mirto B-27, guayabo F-1, podranea F-2, gardenia B-25, pata de vaca B-42, anacahuita B-16, santa rita B-1, evónimo B-44, azarero B-7, mandioca B-34, madreselva B-40, aguaribay F-8, palta uruguaya B-22, vivero B-46, cinta B-12, esparraguera B-6, coronita F-5, fresno F-10, ligustro F-9. Libres además: B-24, B-36, B-23, B-9, B-18, B-5a/b, B-10, F-7, B-29, B-3, I-1, I-2, B-4, B-14, B-15, F-3.
- **No repetir en <14 días:** el gráfico de 12 meses de FLORACIÓN (libre 22/08) · la tira de FRUTA (24/08) · «32 vs 1» · «3 → 2» · «6 → 4» y el circuito reserva→tijera→flor (29/08) · las 4 candidatas (camelia/aloe/salvia leucantha/jazmín de invierno) · la bifurcación del trifoliado, la clave por olor de B-45, la contradicción flor-amarilla del pitósporo y «hoja converge por ambiente, flor no» (31/08).
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas → EJECUTADO. Liquidámbar B-37 → hecho.
- **01-04/08:** «mándamela cuando esté lindo» (ejecutado 02/08 con verificación meteo) · «¿qué más puedo podar? ¿y el neem?» (contestado 02/08 + Taller nº2) · «recordame las podas si no llueve» (ejecutado el mismo 04/08; la cita quedó en el `daily_summary` del 04/08).
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.

## 📈 Estado del sistema + jardín (21/08/2026)

- Push subscription `pix9`: **active**; logging vía `/api/feedback` confiable. Threads, `uploads.json` y `user_tasks.json`: **0 pendientes** (lo último del usuario es del 30/07).
- **Cero eventos nuevos en 96 h** (el último sigue siendo el dwell del 17/08 21:25Z). Ventana ciega de viaje, esperado.
- Sin responder: `podas-previaje`, `viaje-silencio`, `horario-tareas`. Los tres son insumo de la reentrada.
- Jardín en DORMANCIA, **saliendo: los 4 frutales podados están abriendo flor**. **33 días al equinoccio (23/09).** Helada posible hasta fin de agosto (ninguna en el pronóstico a 14 días), pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado = «más flor»**.
- Compactación 21/08: nada que compactar — los 10 eventos de `engagement.json` (más viejo: 16/08) y los 5 de `send_log.json` (más viejo: 06/08) están dentro de los 14 días. Queue del 20/08 reemplazada por la nota del 21/08.

## Conclusiones de los push (por feedback real)

- **17/08 — preguntas-abiertas: MASOMENOS con el mejor dato de timing del canal.** Apertura en **2 min** (récord; rompe 5 ⬛) y muerte al 41 %. **4º reconteo hoy (96 h): cero eventos nuevos — el 41 % fue el techo real.** Su causa de layout **sobrevive a la re-medición** (75 % renderizado): es la única del archivo donde el layout sí explica el resultado. Veredicto de contenido suspendido al 24/08.
- **15/08 — florecio-lo-que-podaste: ⬛ a 144 h, VEREDICTO SUSPENDIDO.** Quedó linkeada al 94 % del documento del 17: **no es rechazo, es no-exposición**. **No está aprobada → NO se re-pushea sola el 24/08**; va linkeada dentro de la landing del slot.
- **16/08 — domingo sin slot: 0 push por diseño, y el usuario volvió SOLO al sitio** (src=direct, desde `ideas.html`). **El espacio vacío no lo aleja** — argumento fuerte a favor de la cadencia baja. Pero abrió las dos peores del archivo y rebotó en 9 s.
- **13, 18, 19, 20 y 21/08 — días sin push cumplidos.** El 20/08 fue el **6º de 7 slots de tarea del viaje cumplido en silencio**; queda solo el sáb 22 (sin tarea).
- **10/08 mandarina · 08/08 el-hueco · 04/08 tarjeta-campo · 06/08 jardin-hoy: ⬛ SUSPENDIDOS** (ventana ciega). El tap `mandarina-parte-vuelta` NO se activó → **el parte de vuelta del 22/08 no es deuda comprometida**. · **03/08 el-taller-2: MASOMENOS-ALTO** (7/7 pasos, dwell 166 s, cero reacción) — **y hoy se comprobó que su control estaba al 0 %: el layout NO fue la causa.**
- **02/08 — el-taller re-push: ÉXITO MÁXIMO** (😍 + 2º slot + 3 ticks de poda reales; verificar la condición del mundo real fue determinante). · **31/07 — el-parte: formato-diario archivado, y con layout compliant** (27 %) — la derrota más limpia del canal. · **30/07 — jardin-hoy GANADORA, día tier-1** (3 feedback_text, los tres ejecutados).
- **Patrón agregado (14 pushes, 30/07 al 17/08):** las 3 con señal activa traían **ayuda técnica ejecutable con la herramienta en la mano**. Las 6 ⬛ son del período 04-15/08 = ausencia física. **La única derrota con evidencia limpia sigue siendo `el-parte` — y ahora se sabe que perdió por contenido, no por botones.**

## TODO / próximos experimentos

- **SÁBADO 22/08 (11:00) — último slot del viaje y única push de la semana.** Materia prima verificada **8 veces**: vuelve a un jardín **seco** (0,0 mm el 22 y el 23, **4ª confirmación**) y **frío parejo, 9-11 °C, cero heladas en 14 días**. ⚠️ **NO usar el número del «primer calor»: se movió por 3ª vez** (26/08 saltó a 15,4). El ángulo «arranca la temporada» va **sin cifra**. Cast: ≥70 % del elenco intacto (≥20 días de descanso). **Primer control <35 % verificado en Chromium antes de commitear.**
- **Medir la barra de señal rápida** el 22/08: buscar `via:"quickbar"` en las reacciones y los eventos `quicksignal_dismiss` / `quicksignal_to_text`. Si la señal llega por la barra, la regla #2 queda probada.
- **LUNES 24/08 — reentrada.** ① **Renovar el contenido de `el-taller` en su URL antes de re-pushearla** — el hero todavía dice «hoy no llueve / 0 mm / 5 días al viaje», datos del 1º de agosto (la estructura ya está lista, falta el texto) ② leer `podas-previaje` y armar la lista real ③ aplicar `horario-tareas` si contestó ④ **Taller nº3 = pitósporo B-43** ⑤ preguntar por las estacas ⑥ hortensia el 29-30/08, la única con reloj ⑦ **cobrar la promesa cumplida: 17 días, 7 slots de tarea, cero pushes** ⑧ re-medir de cero todo lo suspendido ⑨ **leer `el-taller-arranque`**: si contestó «campo», el formato del Taller se optimiza para el patio (pasos más cortos, letra más grande, cero scroll entre cortes).
- **Cantera de auditorías computadas** (reentrada): un solo ejemplar (44/52) · reparto real de luz vs lo que pide cada ficha · el calendario de PERFUME (9 especies, oct-dic) · el bucle poda→FRUTA en diciembre-enero.
- **Idea del 16/08:** el usuario llega a las experiencias por `ideas.html`. En la reentrada, **ordenar ahí las buenas y retirar las de la era gimmick**. (No tocar durante el viaje.)
