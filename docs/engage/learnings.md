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
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo», «si no llueve»), la condición se **verifica con datos reales** antes de encolar y se muestra citada.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + HTML de pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## ✈️ CONTEXTO DOMINANTE — **VIAJE 7 AL 23 DE AGOSTO** (día 3 al 09/08)

- **Compromiso publicado el 06/08, a cumplir a rajatabla: del 7 al 23 NO se manda NINGUNA push de tareas.** Adentro caen 7 slots de tarea (sáb 8 ✅ cumplido, lun 10, jue 13, sáb 15, lun 17, jue 20, sáb 22). Se lo dije con número. **Romperlo quema el activo más caro que tengo.**
- Las experiencias del viaje quedaron sujetas a `viaje-silencio` (`total` / `solo-lindo` / `todo`). **Sigue sin contestar al 09/08** → rige el default: **0 tareas + experiencia solo si es lectura placentera, cero-deber y con listón alto.** Releerlo antes de cada slot del viaje (lun 10, sáb 15, lun 17, sáb 22).
- **08/08 el listón se consideró alcanzado** y salió `el-hueco`: **cero apertura a 18 h** (ver abajo). Si en los próximos slots no hay un hallazgo de ese calibre, **no mandar nada** es la respuesta correcta.
- **⚠️ Regla nueva 09/08 — el viaje NO es ventana de medición.** 5 días sin un solo evento (04/08 00:15 → 09/08). Un ⬛ durante el viaje **no condena un formato**: mide la disponibilidad del usuario, no el contenido. **Ningún eje se archiva con evidencia recogida entre el 07 y el 23.** Todo veredicto queda suspendido hasta la reentrada del 24/08.
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b) con justificación técnica real. **Excepción: la hortensia sí tiene reloj → 29-30/08, antes del brote.**
- ✅ Cerradas: durazno B-30/35, ciruela B-38, ciruelo F-4, liquidámbar B-37, pera B-39.
- **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** B-41 caqui NO se nombra como urgencia hasta primavera (pedido del usuario).
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página.
- ⚠️ Los ticks del Taller (`taller-arbol-*`, `tc-hecho-*`) **NO escriben `task_states.json`** — son eventos de engagement. No contradecir al usuario con eso.

## 🕐 LA HORA — **hipótesis CORREGIDA el 08/08** (la anterior estaba sobreajustada)

Ordenado por **hora de envío REAL** (send_log, no la cola):

| Envío real (MVD) | Push | 1ª apertura | Resultado |
|---|---|---|---|
| Sáb 01/08 10:58 | jardin-hoy | +4 h | floja (dwell 25 s) |
| **Dom 02/08 11:07** | **el-taller re-push** | +4 h | **🏆 ÉXITO (😍 + 2º slot)** |
| **Mié 06/08 11:37** | jardin-hoy «cierre» | **nunca** | ⬛ |
| **Mar 04/08 11:38** | tarjeta-campo | **nunca** | ⬛ |
| **Sáb 08/08 11:32** | el-hueco (viaje) | **nunca (18 h)** | ⬛ — *pero es día 2 de viaje: no computa como veredicto* |
| **Sáb 01/08 12:06** | **el-taller** | +2 h 08 | **🏆 ÉXITO MÁXIMO** |
| Dom 02/08 14:46 | que-mas-podo | +3 h 57 | acción real (podó F-4) |
| Vie 31/07 18:02 | el-parte | +1 h 41 | masomenos |
| **Lun 03/08 18:48** | el-taller-2 | **+32 min** | ⚡ el mejor delay medido |

- ⚠️ **CORRECCIÓN (08/08).** Ayer escribí «09-12 h = hora muerta, 2 de 2 ⬛». **La propia tabla lo desmiente:** `el-taller` salió 11:07 y 12:06 en esa misma franja y fueron **los dos mejores resultados del canal**. Lo que separa los ⬛ de los 🏆 **no es el reloj: es el contenido.** Los dos ⬛ (jardin-hoy-cierre, tarjeta-campo) eran repetición de formato y aviso; los 🏆 eran sustancia técnica nueva.
- **Regla vigente:** la hora **modula**, el contenido **decide**. De tarde el delay de apertura es menor (32 min vs 2-4 h), pero un contenido fuerte se abre igual a la mañana. **No enterrar un formato por la hora ni salvarlo por ella.**
- ⚠️ **El dispatcher LAGUEA.** `send_at` ≠ envío real. Medido: 10:00→11:37 (06/08), 09:30→11:38 (04/08), 10:00→12:41 (03/08), 10:00→10:58 (01/08), 18:00→18:48 (03/08). Lag observado 0,5 a 2,7 h.
- ⚠️ **Los horarios son mandato del usuario, no los cambio por mi cuenta.** La pregunta ya está publicada dentro de la app (`horario-tareas`, jardin-hoy 06/08). **Leer ese answer antes de la reentrada del 24/08.**

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

`2026-08-01-el-taller` — **APPROVED lunes 18:00 + sábado 11:00.** El mejor resultado del canal.

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95%, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados («el error:») ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-paso-N` dice dónde se traba; `taller-arbol-<code>` dice qué cerró de verdad.
- **08/08 se probó el Taller SIN herramienta** (`el-hueco`): misma sustancia y mismos «el error:», pero todo se resuelve con un tap. Es la variante para cuando no puede tocar el jardín. **Medir si el molde sobrevive sin la acción física.**

## 📌 MANDATO 24/07 (canal tarea — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS.** Consolidada en **«Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable, se REEDITA en su lugar). NO encolar task-dia/pendientes/top3 sueltas. NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
2. **jardin-hoy lleva siempre:** vistazo de 5 s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`) + caja «🙋 Pedime lo que necesites».
3. **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo». MUERTO.
- **checklist de viaje / «antes de irte» como deberes:** el viaje se trata como **tranquilidad o como ventaja**, nunca como lista de pendientes.
- **vos-decidis / feed-de-decisiones:** el eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte. ⚠️ Ojo: `el-hueco` (08/08) toca su objetivo declarado pero **desde el dato duro**, no desde la aspiración. Si falla, el problema es el eje-objetivo entero, no el formato auditoría.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín.
- **Ayudarlo a HACER > informarlo.** Corolario 08/08: cuando no PUEDE hacer (viaje), lo más cercano es **hacerlo DECIDIR** — un tap que produce trabajo mío, no suyo.
- **El dato computado sobre su propio catálogo es munición sin explotar.** 52 fichas × 20 campos = hallazgos que él no tiene forma de ver solo. Primer uso: 08/08.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1.
- **Timing verificado > urgencia inventada.** Ir a buscar el dato real y mostrar que se verificó (rindió 02/08 y 04/08).
- **Decir «hoy no hay nada que hacer» cuando es verdad.** Y **el silencio del canal se respeta como contenido**: no mandar tareas durante el viaje ES la jugada; la promesa cumplida se cobra el 24/08.
- **Preguntar en vez de asumir.**
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla. **FOTOS REALES = need validado.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco.
- ⚠️ **Quemados al 08/08:** B-32, B-10, F-7, B-29, B-3 hasta el **15/08** (consumidos hoy) · B-9, B-18, B-5a, B-39 hasta el 13/08 · romero B-26 vedado para fun_fact hasta fines de agosto (hoy se usó como *problema*, no como trivia). Carozos y B-15 ya vencieron.
- **No repetir en <14 días:** el gráfico de 12 meses, el par «32 vs 1», y las 4 candidatas (camelia / aloe arborescens / salvia leucantha / jazmín de invierno).
- **Elenco INTACTO para la reentrada del 24/08:** mandarina B-24, pindó B-8, limonero B-23, mirto B-27, guayabo F-1, pitósporo B-43, podranea F-2, gardenia B-25, clivia B-13, pata de vaca B-42, anacahuita B-16, santa rita B-1.
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

## 📈 Estado del sistema + jardín (09/08/2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable → el silencio es real, no un bug de tracking.
- **Silencio total del usuario desde el 04/08 00:15** (0 eventos el 04, 05, 06, 07, 08). Cinco días. Se explica por víspera + viaje. **No sobre-interpretar como rechazo** (ver regla del 09/08 arriba).
- Threads (`docs/sync/threads/`): **0 mensajes pendientes**, el último del usuario es del 30/07. Nada que calibrar desde ese canal.
- Sin responder: `podas-previaje`, `viaje-silencio`, `horario-tareas`. Los tres son insumo de la reentrada.
- Parte verificado 06/08 (open-meteo, MVD): del 8 al 15/08 **0-2 mm, mínimas 7-9 °C, sin heladas**. El jardín aguanta solo los 17 días.
- Jardín en DORMANCIA, saliendo. ~46 días al equinoccio (23/09). Helada posible hasta fin de agosto, pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado = «más flor»** (reencuadrado el 08/08: el problema es el *mes*, no la cantidad).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco B-4 / lapachillo B-14), mejor sol de invierno → huerta acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37 / palto B-36 / pileta · oeste/frente = fotinias, ligustro F-9, fresno F-10 · **romero B-26 = única en flor en junio Y julio** · mandarina B-24 + pindó B-8 en fruto en invierno · **viraró B-32 florece agosto-setiembre, es dioica** · limonero B-23 fruta 12/12 · plantines de palta contra la pared, SIN TOCAR · B-41 caqui identidad EN DUDA · B-45 sin id.
**Curva de floración (calculada 08/08 sobre `flowering` de las 52 fichas):** Ene 16 · Feb 11 · Mar 9 · Abr 6 · May 3 · Jun 1 · Jul 1 · Ago 6 · Set 13 · Oct 26 · Nov 32 · Dic 24. **Solo 4 especies cubren mayo-julio** (abelia F-7, lavanda B-10/19, lantana B-29 en mayo; romero B-26 solo en junio y julio). **5 de las 6 de agosto son flor de frutal** (efímera, 2-3 semanas).
**Poda de Prunus (fichas):** durazno 40-50% vaso abierto · ciruelo F-4 25-35% · ciruela B-38 30% · ventana = yema hinchada sin abrir · gomosis = riesgo principal, alcohol 70%.
**Poda de flor (fichas):** crespón B-9 *Lagerstroemia indica* 50-70%, madera nueva, «crepe murder» es mito, **de los últimos en despertar (septiembre)** · althea B-18 *Hibiscus syriacus* 40-50%, madera nueva, **brota tardísimo → el mayor margen del jardín** · **hortensia B-5 florece en madera VIEJA → NO podar ahora**, su poda va feb-mar; **su trasplante SÍ tiene reloj: antes del brote** · ninguno de los dos arbustos de flor es Prunus → sin gomosis · no fertilizar hasta ver el primer brote.
**Propagación:** crespón/althea = estaca de madera dura en dormancia (gastado 04/08) · romero y lavanda = gajo semi-maduro, pendiente de desarrollar a la vuelta si prendió `hueco-multiplicar`.

## Conclusiones de los push (por feedback real)

- **08/08 — el-hueco (experiencia del viaje): ⬛ CERO APERTURA a 18 h — VEREDICTO SUSPENDIDO.** Enviada 11:32, 0 clicks, 0 taps `hueco-*`, 0 slots, 0 reacción, 0 feedback. **NO se archiva el eje-objetivo ni el formato auditoría-computada:** el usuario no abrió NADA en 5 días (día 2 de viaje). Un ⬛ sin ninguna apertura en la ventana no distingue «mal contenido» de «usuario ausente». Queda `pending`, la página se conserva, y **se re-mide a la reentrada (24/08) antes de cualquier decisión.** Si al volver tampoco engancha, ahí sí se cierra.
- **06/08 — jardin-hoy «cierre»: ⬛ CERO APERTURA.** Contenido honesto pero era el 4º jardin-hoy en 6 días: **repetición de formato**, no mala hora (ver corrección arriba).
- **04/08 — tarjeta-campo: ⬛ CERO APERTURA.** Formato sin testear, no muerto. **Re-test a la vuelta, primera semana.**
- **03/08 — el-taller-2: MASOMENOS-ALTO.** 7/7 pasos + dwell 166 s + un pedido concreto, cero reacción. Abrió a los **32 min**.
- **02/08 — el-taller re-push: ÉXITO.** 😍 + prendió el 2º slot + 7/7 + ticks B-30/B-38. Verificar la condición del mundo real fue determinante.
- **02/08 — que-mas-podo: SIN reacción pero CON acción.** Podó F-4. **El clic no es la métrica; el tick sí.**
- **01/08 — el-taller: ÉXITO MÁXIMO.** 😍 + slot lun18 + 7/7 ×2 + feedback positivo. El molde.
- **31/07 — el-parte: MASOMENOS con veredicto claro.** Formato-diario archivado.
- **30/07 — jardin-hoy GANADORA, día tier-1.** 3 feedback_text, los tres ejecutados.
- **21/07 — asamblea:** «Está todo perfecto». Sustancia + honestidad funcionan.

## TODO / próximos experimentos

- **LUNES 10/08 — próximo slot (experiencia 18:00). Slot de tarea 10:00: VACÍO, sin excepción.** Decisión ya tomada el 09/08: con 5-6 días de silencio total, **el default es NO mandar**. Solo va si el hallazgo supera a `el-hueco` — y si va, tiene que ser **más corto que el-hueco, un solo hallazgo, un solo tap**: la hipótesis a testear es que en viaje lo único que sobrevive es lo brevísimo. Cantera abajo.
- **Slots del viaje (lun 10, sáb 15, lun 17, sáb 22): 0 tareas SIEMPRE.** Experiencia solo si hay un hallazgo del calibre de `el-hueco`. **Sin hallazgo → no mandar nada.** Releer `viaje-silencio` cada vez.
- **09/08 (domingo, día 3): mantenimiento puro, 0 push** — correcto por cadencia. Compactados engagement (15 eventos → daily_summary) y send_log (4). Queue vaciada.
- **Cantera de auditorías computadas** (mismo molde, dato nuevo, para cuando haga falta): curva de FRUTA mes a mes · cuántas especies dependen de un solo ejemplar (riesgo de perder algo irreemplazable) · reparto real de luz frente/fondo/interior vs lo que cada ficha pide · las 5 especies sin identificar como «causas abiertas».
- **LUNES 24/08 — reentrada.** ① Leer `podas-previaje` y armar la lista real ② aplicar `horario-tareas` si contestó ③ **Taller nº3 = pitósporo B-43**, con viraró B-32 en flor de elenco ④ preguntar por las estacas ⑤ hortensia el 29-30/08, la única con reloj ⑥ **si prendió candidatas en `el-hueco`, la lista de compra concreta es la primera entrega de la vuelta.**
- **Before/after con fotos reales:** si sube foto del crespón podado, devolverle veredicto es el siguiente salto de valor.
