# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE (autoridad operativa — semanal, día-consciente)

| Día | Tarea (jardin-hoy) 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / **Viernes** / Domingo | — | — (solo mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Una sola push por slot de experiencia.** Siempre lleva una **original NUEVA** (el experimento del día) + las **aprobadas** de ese slot agrupadas y linkeadas DENTRO de la misma landing. Nunca dos pushes de experiencia sueltas.
- **Aprobación = recurrencia.** Solo vuelve lo que el usuario prendió (😍 / slot en «sí» / `engageApprove`). Pending sin aprobar no se borra: simplemente no recurre.
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo», «si no llueve»), la condición se **verifica con datos reales** antes de encolar y se muestra citada.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + HTML de pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## ✈️ CONTEXTO DOMINANTE — **VIAJE 7 AL 23 DE AGOSTO** (hoy = día 8, 14/08)

- **Compromiso publicado el 06/08, a cumplir a rajatabla: del 7 al 23 NO se manda NINGUNA push de tareas.** Adentro caen 7 slots de tarea (sáb 8 ✅, lun 10 ✅, jue 13 ✅, **sáb 15, lun 17, jue 20, sáb 22**). Se lo dije con número. **Romperlo quema el activo más caro que tengo.** **3 de 7 cumplidos**; los 4 que faltan salen solos si la cola queda vacía esos días.
- **El compromiso es SOBRE TAREAS, no sobre experiencias.** Las experiencias del viaje quedan sujetas a `viaje-silencio` (`total` / `solo-lindo` / `todo`), **sin contestar al 14/08** → rige el default: **0 tareas + experiencia solo si es lectura placentera, cero-deber y con listón alto.** Releerlo antes de cada slot (sáb 15, lun 17, sáb 22).
- **⚠️ El viaje NO es ventana de medición (regla 09/08, re-reconfirmada hoy).** **10 días sin un solo evento** (último: 04/08 00:15). Un ⬛ durante el viaje **mide disponibilidad, no contenido**. **Ningún eje ni formato se archiva con evidencia recogida entre el 07 y el 23.** Todo veredicto suspendido hasta la reentrada del 24/08.
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b) con justificación técnica real. **Excepción: la hortensia sí tiene reloj → 29-30/08, antes del brote.**
- ✅ Cerradas: pera B-39 y liquidámbar B-37 (en `task_states.json`) + durazno B-30/35, ciruela B-38 y ciruelo F-4 **por tick propio del usuario** (02/08). ⚠️ Los ticks del Taller (`taller-arbol-*`, `podo-*`) **NO escriben `task_states.json`** — el archivo las muestra `active`. **No contradecir al usuario con eso: para él están hechas.**
- **Chequeo de vencimientos (sigue válido):** ninguna ventana abierta se cierra antes del 23. Las de «yema hinchada» (crespón, althea, hibisco B-4, podranea F-2, pitósporo B-43, madreselva B-40-3) son de las últimas en despertar; la más apurada es **abelia F-7, límite fin de agosto**. Vuelve con margen real — se lo dije así, sin inflar.
- **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** B-41 caqui NO se nombra como urgencia hasta primavera (pedido del usuario).
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (**shape real: `{"tasks": {...}}`**), no contra la edición anterior de la página.

## 🌧️ PARTE RE-VERIFICADO 14/08 (open-meteo, MVD) — ⚠️ CORRIGE el de ayer

| Fecha | Mín | Máx | Lluvia |
|---|---|---|---|
| **15/08 (slot)** | 11,1 | 15,2 | 0,7 mm |
| 16/08 | 11,5 | 14,5 | 0,2 mm |
| 17/08 | 10,0 | 11,5 | 0,2 mm |
| **18/08** | 10,6 | 12,5 | **18,4 mm** |
| 19/08 | 11,8 | 12,6 | 8,8 mm |
| **20/08** | 11,4 | 13,5 | **17,2 mm** |
| 21-24/08 | 7,0-10,0 | 8,9-12,7 | ~0,6 mm total |

- ⚠️ **CORRECCIÓN IMPORTANTE:** ayer el modelo daba **~90 mm** entre el 17 y el 20 (50 mm solos el 18). Hoy, a 4 días vista, da **~44,6 mm**. Sigue siendo mucha agua y sigue sirviendo el argumento («el jardín se riega solo justo en el medio del viaje»), pero **el número que se publique el sábado es ~45 mm, NO 90.** Esto es exactamente por qué la regla dice re-verificar antes de encolar: publicar 90 mm y que caigan 45 quema credibilidad, que es el activo principal.
- **Cero heladas** en toda la ventana (mínima absoluta 7,0 °C el 24/08). Eso sí se sostiene sin asterisco.
- La reentrada sigue favorecida: **suelo cargado de humedad + 21-24/08 secos y frescos** → condiciones casi ideales para el trasplante de la hortensia y las podas de madera nueva.
- **Re-verificar OTRA VEZ el sábado antes de encolar.** Un pronóstico a 4-6 días se movió 50% en 24 h; puede volver a moverse.

## 🕐 LA HORA — hipótesis corregida el 08/08 (la anterior estaba sobreajustada)

| Envío real (MVD) | Push | 1ª apertura | Resultado |
|---|---|---|---|
| **Sáb 01/08 12:06** | **el-taller** | +2 h 08 | **🏆 ÉXITO MÁXIMO** |
| **Dom 02/08 11:07** | **el-taller re-push** | +4 h | **🏆 ÉXITO (😍 + 2º slot)** |
| Dom 02/08 14:46 | que-mas-podo | +3 h 57 | acción real (podó F-4) |
| **Lun 03/08 18:48** | el-taller-2 | **+32 min** | ⚡ el mejor delay medido |
| Sáb 01/08 10:58 | jardin-hoy | +4 h | floja (dwell 25 s) |
| Vie 31/07 18:02 | el-parte | +1 h 41 | masomenos |
| Mar 04/08 11:38 | tarjeta-campo | nunca | ⬛ — *víspera del silencio* |
| Mié 06/08 11:37 | jardin-hoy «cierre» | nunca | ⬛ |
| Sáb 08/08 11:32 | el-hueco (viaje) | nunca | ⬛ — *día 2: no computa* |
| Lun 10/08 18:11 | ultima-mandarina (viaje) | nunca | ⬛ — *día 4: no computa* |

- **La hora modula, el contenido decide.** `el-taller` salió 11:07 y 12:06 — la misma franja de los ⬛ — y fue el mejor resultado del canal. Los ⬛ eran repetición de formato o ausencia física; los 🏆 eran sustancia nueva. **No enterrar un formato por la hora ni salvarlo por ella.**
- ⚠️ **El dispatcher lag mide 0,2 a 2,7 h** (el 10/08 fueron **11 min**). Encolar en el horario exacto sigue siendo lo correcto.
- ⚠️ **Los horarios son mandato del usuario.** La pregunta ya está publicada (`horario-tareas`, jardin-hoy 06/08). **Leer ese answer antes de la reentrada.**

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

`2026-08-01-el-taller` — **APPROVED lunes 18:00 + sábado 11:00.** El mejor resultado del canal.

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95%, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados («el error:») ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad.
- Durante el viaje va **linkeada y en pausa** dentro de la landing del slot, nunca pusheada suelta.

## 📌 MANDATO 24/07 (canal tarea — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS.** Consolidada en **«Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable, se REEDITA en su lugar). NO encolar task-dia/pendientes/top3 sueltas. NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
2. **jardin-hoy lleva siempre:** vistazo de 5 s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** + caja «🙋 Pedime lo que necesites».
3. **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo». MUERTO.
- **checklist de viaje / «antes de irte» como deberes:** el viaje se trata como **tranquilidad o como ventaja**, nunca como lista de pendientes.
- **vos-decidis / feed-de-decisiones:** el eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín.
- **Ayudarlo a HACER > informarlo.** Cuando NO puede hacer (viaje), lo más cercano es **hacerlo DECIDIR** con un tap que produce trabajo mío, no suyo.
- **El dato computado sobre su propio catálogo es munición sin explotar.** 52 fichas × 20 campos. Usados: floración (08/08), fruta (10/08). Sin usar: dependencia de un solo ejemplar, luz real vs ficha, especies sin identificar, calendario de perfume.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1.
- **Timing verificado > urgencia inventada** — y **número re-verificado > número lindo** (ver la corrección de los 90→45 mm de hoy).
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal tarea ES contenido: la promesa cumplida se cobra el 24/08.
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla. **FOTOS REALES = need validado.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco.
- ⚠️ **Quemados al 14/08:** solo B-24, B-36, B-23 (hasta el 17/08) · romero B-26 vedado para fun_fact hasta fines de agosto. **Liberados hoy:** B-32, B-10, F-7, B-29, B-3 — justo a tiempo para el sábado.
- **No repetir en <14 días:** el gráfico de 12 meses de FLORACIÓN (libre el 22/08), la tira de 12 meses de FRUTA (libre el 24/08), el par «32 vs 1», el «3 → 2», y las 4 candidatas (camelia / aloe arborescens / salvia leucantha / jazmín de invierno).
- **Elenco INTACTO para el 15/08 y la reentrada:** pindó B-8, mirto B-27, guayabo F-1, pitósporo B-43, podranea F-2, gardenia B-25, clivia B-13, pata de vaca B-42, anacahuita B-16, santa rita B-1, hortensia B-5b.
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

## 📈 Estado del sistema + jardín (14/08/2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable → el silencio es real, no un bug.
- **Silencio total del usuario desde el 04/08 00:15 (10 días, 0 eventos).** Explicado por víspera + viaje. **No sobre-interpretar como rechazo.** Ninguna push del viaje (el-hueco, mandarina) fue abierta.
- Threads (`docs/sync/threads/`): **0 mensajes pendientes** (13 archivos), el último del usuario es del 30/07. `user_tasks.json`: 3 entries, **1 sin `ai_answer`** pero es la entry contenedora `tasks`, no una pregunta real → nada que contestar. `uploads.json`: 0 pendientes (última foto 30/07, B-30).
- Sin responder: `podas-previaje`, `viaje-silencio`, `horario-tareas`. Los tres son insumo de la reentrada.
- Jardín en DORMANCIA, saliendo. ~40 días al equinoccio (23/09). Helada posible hasta fin de agosto (ninguna en el pronóstico a 14 días), pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado = «más flor»**.
- Compactación 14/08: engagement.json 96→79 eventos (se fue el 30/07 al `daily_summary`, **los 3 feedback_text de ese día quedaron preservados dentro del resumen**), send_log 15→11, queue vaciada. Nada perdido.

## Conclusiones de los push (por feedback real)

- **14/08 — viernes sin slot: 0 push por diseño.** No hay nada que concluir de hoy salvo que el sistema se mantiene limpio y que **un número que traía la memoria estaba viejo** (90 mm → 45 mm). Detectarlo un día antes del slot es exactamente el valor de las corridas de mantenimiento.
- **13/08 — jueves, slot de tarea VACÍO a propósito: 3º de 7 del compromiso cumplido.** No es una no-decisión: es la entrega. El valor se cobra el 24/08 pudiendo decir «17 días, cero pushes de tareas, tal cual te lo prometí».
- **10/08 — la-ultima-mandarina: ⬛ CERO APERTURA — VEREDICTO SUSPENDIDO** (0 clicks/taps/slots a 4 días). Con 10 días sin un solo evento no se distingue formato de ausencia. Se re-mide el 24/08.
- **08/08 — el-hueco: ⬛ CERO APERTURA — VEREDICTO SUSPENDIDO.** Mismo motivo. **NO se archiva el eje-objetivo ni el formato auditoría-computada.**
- **06/08 — jardin-hoy «cierre»: ⬛.** Contenido honesto pero 4º jardin-hoy en 6 días: **repetición de formato**, no mala hora.
- **04/08 — tarjeta-campo: ⬛ sin testear.** Cayó justo en la víspera del silencio. **Re-test a la vuelta, primera semana.**
- **03/08 — el-taller-2: MASOMENOS-ALTO.** 7/7 pasos + dwell 166 s + un pedido concreto, cero reacción. Abrió a los **32 min**.
- **02/08 — el-taller re-push: ÉXITO.** 😍 + prendió el 2º slot + ticks B-30/B-38. Verificar la condición del mundo real fue determinante.
- **02/08 — que-mas-podo: SIN reacción pero CON acción.** Podó F-4. **El clic no es la métrica; el tick sí.**
- **31/07 — el-parte: MASOMENOS con veredicto claro.** Formato-diario archivado.
- **30/07 — jardin-hoy GANADORA, día tier-1.** 3 feedback_text, los tres ejecutados.
- **Patrón agregado (10 pushes, 30/07 al 14/08):** las 3 que ganaron señal activa fueron las 3 que traían **ayuda técnica ejecutable sobre sus plantas con la herramienta en la mano**. Las 5 ⬛ son todas del período 04-10/08 = ausencia física, no contenido. La única derrota con evidencia limpia sigue siendo `el-parte` (formato-diario).

## TODO / próximos experimentos

- **SÁBADO 15/08 (11:00) — DECISIÓN TOMADA EL 12/08, ejecutar sin re-litigar:** **SÍ se manda la experiencia.** El compromiso del viaje es sobre TAREAS, y saltear un slot que el usuario fijó sería degradar su cadencia usando evidencia que yo mismo declaré inadmisible. Reglas:
  ① **cero-deber**, lectura placentera, listón alto (default de `viaje-silencio` sin contestar);
  ② **NO quemar la munición fuerte** — la auditoría «44 de 52 especies dependen de UN solo ejemplar» y el calendario de PERFUME se reservan para la reentrada, donde sí miden;
  ③ elenco disponible (todos liberados al 14/08): B-32, B-10, F-7, B-29, B-3 + el intacto (pindó B-8, mirto B-27, pitósporo B-43, clivia B-13, pata de vaca B-42, anacahuita B-16, santa rita B-1);
  ④ **ángulo recomendado — VERIFICADO HOY contra `data_plants.py`: el viraró B-32 (Ruprechtia laxiflora, fondo/este) tiene `flowering: [8,9]` → es la ÚNICA especie del catálogo que está floreciendo AHORA mismo, mientras él no está.** Ninguna otra del elenco disponible florece en agosto. «Te lo estás perdiendo» sin culpa y sin deber. Su fun_fact real: los «frutos» rosados no son flores, son sépalos persistentes agrandados que hacen de ala para dispersión por viento;
  ⑤ **reforzarlo con el parte: ~45 mm entre el 17 y el 20 + cero heladas** → el jardín se riega solo y vuelve a suelo húmedo con días secos (21-24). ⚠️ **NO decir 90 mm** — ese número era del modelo del 13/08 y ya se corrigió a la baja;
  ⑥ **re-verificar el pronóstico OTRA VEZ antes de encolar** (se movió 50% en 24 h); ⑦ Taller aprobado linkeado y en pausa dentro de la landing, nunca suelto; ⑧ slot de TAREA del sábado 15 = VACÍO (4º de 7 del compromiso).
- **Slots de tarea que faltan cumplir del compromiso:** sáb 15, lun 17, jue 20, sáb 22 → cola VACÍA esos días, sin excepción.
- **Cantera de auditorías computadas** (para la reentrada, mismo motor, dato nuevo): un solo ejemplar (44/52) · reparto real de luz frente/fondo/interior vs lo que pide cada ficha · las 5 especies sin identificar como «causas abiertas» · el calendario de PERFUME (9 especies, concentradas oct-dic).
- **LUNES 24/08 — reentrada.** ① Leer `podas-previaje` y armar la lista real ② aplicar `horario-tareas` si contestó ③ **Taller nº3 = pitósporo B-43**, con viraró B-32 en flor de elenco ④ preguntar por las estacas ⑤ hortensia el 29-30/08, la única con reloj — y el pronóstico la favorece (suelo húmedo + 21-24/08 seco) ⑥ **si prendió `mandarina-parte-vuelta`, el parte del 23 es deuda comprometida** ⑦ si prendió `hueco-multiplicar`, la lista de compra concreta ⑧ cobrar la promesa cumplida: 17 días, 7 slots de tarea, cero pushes.
- **Before/after con fotos reales:** si sube foto del crespón podado, devolverle veredicto es el siguiente salto de valor.
