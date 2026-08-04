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
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo», «si no llueve»), la condición se **verifica con datos reales** antes de encolar y se muestra citada. Aplicada el 02/08 (domingo) y el **04/08 (martes)**.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + HTML de pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

`2026-08-01-el-taller` — **APPROVED lunes 18:00 + sábado 11:00.** El mejor resultado del canal.

- Señal: **7/7 pasos ×3 pasadas**, dwell 168s @95%, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados («el error:») ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-paso-N` dice dónde se traba; `taller-arbol-<code>` dice qué cerró de verdad y le da razón para volver a abrir la página. Replicar en todo lo que sea multi-tarea.

## 🃏 04/08 — LA TARJETA DE CAMPO: el usuario pidió el formato corto

Anoche (21:08) leyó el Taller nº2 **entero** (7/7 pasos, dwell 166s) y escribió: **«Recordame las podas así hago las podas mañana si no llueve».** No hubo 😍 ni approve. Lectura correcta: **el taller largo enseñó, pero para EJECUTAR quiere otra cosa.**

- **Descubrimiento de formato:** taller largo = aprender (víspera, sillón). **Tarjeta de campo = ejecutar** (el día, guantes puestos). Son dos productos, no dos versiones del mismo. Hoy mandé la tarjeta: 3 tarjetas grandes, 3 números por planta, un error anticipado, un tilde, barra de progreso pegajosa y bloque final que se revela al completar.
- **Condición verificada, otra vez:** él puso «si no llueve». Fui a buscar el parte hora por hora — **0 mm y 0% de 07 a 20 h**, 12-13°, viento flojo; mié 1,6 mm; **jue 19,1 mm + 48 km/h**; vie se va. Lo muestro citado con su frase y la hora. Esto ya rindió el 02/08: **verificar y mostrar que verifiqué es el gesto de credibilidad más barato que tengo.**
- **La sustancia nueva del día (lo que no estaba en ningún taller): las estacas.** Crespón y althea enraízan por estaca de **madera dura**, y la madera dura es la que va a quedar tirada en el piso. 6-8 trozos de 20-25 cm, corte recto abajo / bisel arriba, 2/3 enterrados, sombra pared sur, una regada y listo — **enraízan solas durante los 16 días de viaje**. Ataca su objetivo declarado («más flor»), cuesta 15 minutos, y convierte el viaje en tiempo productivo sin pedirle nada.
- **La hortensia entra como 3ª tarjeta con un argumento de timing real:** plantarla hoy para que **los 19 mm del jueves le asienten la tierra** — mejor que cualquier regada, y se establece sola mientras no está.
- ⚠️ **Ojo con el ángulo propagación:** quedó gastada la estaca de madera dura. `se-multiplican-solos` (sept-oct) tiene que ir por **semilla / gajo verde / división de mata**, no por estaca dura.

## 📌 MANDATO 24/07 (canal tarea — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS.** Consolidada en **«Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable, se REEDITA en su lugar). NO encolar task-dia/pendientes/top3 sueltas. NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
2. **jardin-hoy lleva siempre:** vistazo de 5s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`) + caja «🙋 Pedime lo que necesites».
3. **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.

## ✈️ CONTEXTO DOMINANTE — VIAJE **7 al 23 DE AGOSTO**

- **Antes de irse (hasta el 6/8) = 3:** crespón **B-9** + althea **B-18** (poda de flor) + **hortensia B-5a/b a tierra** (rincón sur junto a la pera B-39). Opcional: hiedra **B-15**. ✅ Cerrados: durazno B-30/35, ciruela B-38, ciruelo F-4, liquidámbar B-37.
- **Ventana real:** **martes 4 es el último día seco** (0 mm/0%); mié 1,6 mm; **jue 19,1 mm + viento 48 km/h**; vie 7 se va. Si hoy no da, todo se corre al 24 y **sale bien igual** — decirlo así, sin inventar urgencia.
- **Durante (7–23/8) = 0.** Dormancia + lluvia. **NO nagear NADA.** Caen adentro sáb 8, lun 10, sáb 15, lun 17, sáb 22.
- **A la vuelta (24–31/8) = 9:** pitósporo B-43-2, hibisco B-4, podranea F-2, cerco B-7·11·31·33, abelia F-7, gardenia acidificar B-25, 3ª de neem B-25-3, caqui B-41, huerta/lechuga. **B-41 no se nombra como urgencia hasta primavera** (identidad en duda, pedido del usuario).
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página.
- ⚠️ Los ticks del Taller (`taller-arbol-*`, `tc-hecho-*`) **NO escriben `task_states.json`** — son eventos de engagement. B-30/B-38/F-4 siguen `active` en el estado real aunque estén hechos. No contradecir al usuario con eso.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo». MUERTO.
- **checklist de viaje / «antes de irte» como deberes:** el viaje se trata como **tranquilidad o como ventaja**, nunca como lista de pendientes.
- **vos-decidis / feed-de-decisiones:** el eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín.
- **Ayudarlo a HACER > informarlo.**
- **Un formato por momento.** Taller largo = víspera/aprender. Tarjeta corta = el día/ejecutar. No mandar el largo cuando toca el corto.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. Cuando la agenda la pone él, mi trabajo es responder, no proponer.
- **Timing verificado > urgencia inventada.** Ir a buscar el dato del mundo real y mostrar que se verificó.
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla. **FOTOS REALES = need validado.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** un Taller / una tarjeta de campo es monotemático — su cast lo define la TAREA, no el elenco. El ≥70% fresco no aplica ahí.
- ⚠️ **Quemados:** los 4 carozos (B-30, B-35, F-4, B-38) hasta el **09/08**; **B-9, B-18, B-5a hasta el 11/08**; B-15 hasta el 10/08.
- ⚠️ «romero única flor de julio» ya se usó 4× — descansar hasta mediados de agosto.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas → EJECUTADO. Liquidámbar B-37 → hecho.
- **01/08:** «mándamela cuando esté lindo» → EJECUTADO 02/08 con verificación meteorológica.
- **02/08:** «¿qué más puedo podar? ¿qué hago con el neem?» → contestado 02/08 + Taller nº2 el 03/08.
- **03/08:** «recordame las podas… si no llueve» → **EJECUTADO 04/08** (tarjeta de campo, condición verificada).
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.

## 📈 Estado del sistema + jardín (agosto 2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable.
- Jardín en DORMANCIA, saliendo. ~50 días al equinoccio (23/09). Mínimas 8-12°C esta semana, sin heladas en el pronóstico; riesgo real hasta fin de agosto, pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, arranque con lechuga a la vuelta · hortensia B-5a/b → a tierra antes del viaje, rincón sur junto a la pera B-39 · **objetivo declarado del usuario = «más flor»**.
- **Pendientes reales al 04/08: 12** — 3 antes del viaje + 9 a la vuelta.

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37 / palto B-36 / pileta · oeste/frente = fotinias, ligustro F-9, fresno F-10 · **romero B-26 = única que florece en julio** · mandarina B-24 + pindó B-8 en fruto en invierno · viraró B-32 florece en agosto · limonero B-23 fruta 12/12 · plantines de palta contra la pared, SIN TOCAR · B-41 caqui identidad EN DUDA · B-45 sin id.
**Poda de Prunus (fichas):** durazno 40-50% vaso abierto · ciruelo F-4 25-35% · ciruela B-38 30% · ventana = yema hinchada sin abrir · gomosis = riesgo principal, alcohol 70%.
**Poda de flor (fichas):** crespón B-9 *Lagerstroemia indica* 50-70%, muñones 2-4 yemas, madera nueva, «crepe murder» es mito, corteza canela exfoliante · althea B-18 *Hibiscus syriacus* 40-50%, muñones 2-3 yemas, madera nueva, rústica ante heladas, flor de un día, flor nacional de Corea del Sur · **hortensia B-5 florece en madera VIEJA → NO podar ahora**, su poda va feb-mar; es la más sedienta del jardín, raíz enmacetada = marchitez con sustrato húmedo · ninguno de los dos arbustos de flor es Prunus → sin gomosis, sin pasta cicatrizante · no fertilizar hasta ver el primer brote.
**Propagación (04/08):** crespón y althea = estaca de madera dura en dormancia, 20-25 cm, 3-4 yemas, corte recto abajo / bisel arriba, 2/3 enterrado, sombra, riego mínimo.

## Conclusiones de los pushN (por feedback real)

- **04/08 (martes, excepción por pedido explícito) — tarjeta-campo:** primera vez que el formato lo elige ÉL. Mirar: reacción, `tc-hecho-B-9/B-18/B-5`, `tc-hecho-estacas` y los slots. **Si tilda estacas, la propagación pasa a ser línea de producto propia.**
- **03/08 — el-taller-2: MASOMENOS-ALTO.** 7/7 pasos + dwell 166s + un pedido concreto, pero **cero reacción y cero approve**. Diagnóstico: el contenido acertó, el **formato del momento** no. De ahí nació la tarjeta.
- **02/08 (domingo, excepción por pedido) — el-taller re-push: ÉXITO.** 😍 + prendió el 2º slot + 7/7 pasos + ticks B-30/B-38. Verificar la condición del mundo real fue determinante.
- **02/08 — que-mas-podo: SIN reacción pero CON acción.** Podó F-4 y entró a las tareas de B-9/B-18. **El clic no es la métrica; el tick sí.**
- **01/08 (sábado) — el-taller: ÉXITO MÁXIMO.** 😍 + slot lun18 + 7/7 ×2 + feedback positivo. El molde.
- **01/08 — jardin-hoy: floja.** Abierta 4 h tarde, dwell 25s, sin señal. Sostener el canal tarea sin subirle la intensidad.
- **31/07 — el-parte: MASOMENOS con veredicto claro.** Leyó todo, ambos slots en NO. Formato-diario archivado.
- **30/07 — jardin-hoy GANADORA, día tier-1.** 3 feedback_text, los tres ejecutados.
- **28/07 — negativo.** esto-o-esto muerto; vos-decidis v3 rechazada.
- **24/07:** jardin-hoy ganadora. Minimalismo + tareas reales + caja de pedidos.
- **21/07:** asamblea — «Está todo perfecto». Sustancia + honestidad funcionan.

## TODO / próximos experimentos

- **Hoy martes a la noche:** mirar `tc-hecho-*`. Si tildó B-9 + B-18 → la jardin-hoy del **jueves 6** es **cierre y despedida**, corta: qué quedó hecho + la confirmación explícita de que del 7 al 23 **no le mando tareas**. Respetarlo a rajatabla: es la prueba de confianza más barata que tengo.
- **Si NO tildó nada:** no repetir el recordatorio el miércoles (1,6 mm igual lo tapa). El jueves va el cierre igual, sin reproche, con las 2 podas movidas al 24.
- **7 al 23/08 (viaje):** **NO mandar tareas.** Las experiencias del slot van solo si son de lectura placentera y cero-deber; si no hay una buena, **no mandar nada**. Evaluarlo día a día.
- **Lunes 24/08 — reentrada:** las 9 tareas ordenadas por rendimiento en flor + **Taller nº3 = pitósporo B-43** (reducción) + **ver si las estacas prendieron** (si las puso, es la primera pregunta del regreso).
- **Before/after con fotos reales:** si sube foto del crespón podado, evaluarla y devolverle veredicto es el siguiente salto de valor.
