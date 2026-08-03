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
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo»), la condición se **verifica con datos reales** antes de encolar — no se asume. Aplicada el 02/08.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + HTML de pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

`2026-08-01-el-taller` — **APPROVED lunes 18:00 + sábado 11:00.** El mejor resultado del canal.

- Señal: **7/7 pasos completados ×3 pasadas** (01/08 dos veces, 02/08 una), dwell 168s @95%, **😍 love las dos veces**, feedback de texto positivo, y **ticks por árbol** (`taller-arbol-B-30`, `B-38`) horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real y verificable sobre SUS plantas ② se abre **con la herramienta en la mano** — acompaña el trabajo físico, no lo describe ③ una pantalla = una decisión ④ los errores anticipados («el error:») ⑤ diagramas propios en vez de texto.
- **Prendió lun18 el 01/08 y sáb11 el 02/08.** La suscripción crece con la confianza: **no dar por cerrada una preferencia con un solo dato.**
- **Métrica más valiosa que construí: los ticks.** `taller-paso-N` dice dónde se traba (hasta hoy: en ningún paso). `taller-arbol-<code>` dice qué cerró de verdad — y le da una razón para volver a abrir la página horas después. **Replicar en todo lo que sea multi-tarea.**
- **Serie viva:** nº1 carozos (cerrado) → **nº2 poda de flor (hoy 03/08)** → a la vuelta: pitósporo B-43 (reducción), cerco B-7·11·31·33 (recorte parejo), gardenia B-25 con el neem.

## 🌸 03/08 — TALLER Nº 2, y el usuario ya venía eligiendo el tema

El 02/08 a la noche, después de leer «empezá por el crespón» en que-mas-podo, **navegó directo a `tasks/plant-B-9` y `tasks/plant-B-18`** (22:28 y 22:31). Y a las 22:34 tildó `podo-F-4`: **podó el ciruelo del frente**. Los cuatro carozos, cerrados en un fin de semana.

- **Lección de método:** el tema del próximo Taller no lo elijo yo, lo elige él con la navegación. Mirar SIEMPRE a qué `tasks/plant-*` entró después de la última push — es el mejor predictor de intención que tengo.
- **Lección de métrica:** que-mas-podo tuvo dwell corto y ninguna reacción (= «masomenos» por la escala), pero **produjo una poda real**. El clic no es la métrica; el tick sí. No dropear un ángulo por dwell bajo si hubo acción.
- **Timing como gancho, sin inventar urgencia:** verifiqué el parte real (hoy 4,5 mm · **mar 4: 0 mm / 12%** · mié 2,7 mm · jue 14,3 mm + viento 46 km/h · vie se va). Mañana es la única tarde seca antes del viaje. En la página lo digo explícito: **«no es urgente, el 24 también salen bien»** — la apuesta es que decir la verdad sube la conversión en vez de bajarla.
- **Reencuadre del viaje:** no como deberes (ese eje murió el 29/07) sino como ventaja — «podados mañana, las tres semanas que estás afuera dejan de ser tiempo muerto».
- **La pieza de conocimiento del día:** crespón y althea florecen en **madera NUEVA** (cortar fuerte = más flor); la hortensia B-5, al lado, en **madera VIEJA** (la misma tijera le cuesta un año). Dos arbustos, dos reglas opuestas, verificado en fichas. Este tipo de contraste rinde más que cualquier fun_fact.
- **Corrección de calendario que mantengo:** los `due_label` de B-9/B-18 decían «mediados de agosto»; la ficha (`prune_when`) dice **junio-julio**. No están adelantados, **están atrasados**. Cuando `due_label` y ficha discrepan, **manda la ficha**.

## 📌 MANDATO 24/07 (canal tarea — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS.** Consolidada en **«Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable, se REEDITA en su lugar). NO encolar task-dia/pendientes/top3 sueltas. NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
2. **jardin-hoy lleva siempre:** vistazo de 5s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`) + caja «🙋 Pedime lo que necesites».
3. **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.

## ✈️ CONTEXTO DOMINANTE — VIAJE **7 al 23 DE AGOSTO**

Recontado el 03/08 contra `task_states.json` + los ticks del Taller. Usar hasta el 24/08:

- **Antes de irte (hasta el 6/8) = 3.** Crespón **B-9** y althea **B-18** (poda de flor, Taller nº2, ventana real = martes 4) + **hortensia B-5a/b a tierra** (rincón sur junto a la pera B-39). Opcional cuarta: **hiedra B-15**. ✅ Ya cerrados: durazno B-30/35, ciruela B-38, ciruelo F-4, liquidámbar B-37.
- **Durante (7–23/8) = 0.** Dormancia + lluvia. **NO nagear NADA.**
- **A la vuelta (24–31/8) = 9:** pitósporo B-43-2, hibisco B-4 (la más atrasable), podranea F-2, cerco B-7·11·31·33, abelia F-7, gardenia acidificar B-25, 3ª aplicación de neem B-25-3, caqui B-41, huerta/lechuga. **B-41 no se nombra como urgencia hasta primavera** (identidad en duda, pedido del usuario).
- La gran poda NO es «mediados de agosto» este año: la ventana real es **fin de agosto en adelante**.
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página. El 02/08 casi recomiendo podar pera B-39, pindó B-8 y esparraguera B-6-2: las tres estaban `done` desde el 23/07.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07, DROPPED):** leyó los 75s enteros pero puso **NO a los dos slots + meh**. Lee el contenido, rechaza la recurrencia. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo». MUERTO.
- **checklist de viaje / «antes de irte» como deberes:** 29/07 sin señal. El viaje se trata como **tranquilidad o como ventaja**, nunca como lista de pendientes. (`aguantan-solos` dropeada el 03/08 sin pushear por lo mismo: el mensaje de tranquilidad funciona como DATO dentro de jardin-hoy — la franja «7→23/8: 0 tareas» — no como página propia.)
- **vos-decidis / feed-de-decisiones:** ganó el 26/07 y se fatigó en 3 días. El eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Lo que más pesa es la ayuda técnica REAL sobre SU jardín.
- **Ayudarlo a HACER > informarlo.** el-parte (informar → no) vs jardin-hoy + El Taller (hacer → oro).
- **Acompañar el momento físico.** El Taller no se lee en el sillón: se abre con el serrucho en la mano.
- **Contestar una pregunta suya < 2 h** es la forma más pura de la meta-regla #1. Cuando la agenda la pone él, mi trabajo es responder, no proponer.
- **Timing verificado > urgencia inventada.** Ir a buscar el dato del mundo real (pronóstico) y mostrar que se verificó. La credibilidad es el activo principal.
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla. **FOTOS REALES = need validado.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** un Taller es monotemático — su cast lo define la TAREA, no el elenco. El ≥70% fresco no aplica ahí, pero **cada Taller nuevo cambia de tarea** (y por lo tanto de cast). Aplicada hoy con B-9/B-18.
- ⚠️ **Quemados:** los 4 carozos (B-30, B-35, F-4, B-38) hasta el **09/08**; B-9, B-18, B-15 hasta el **10/08** (fuera de la serie Taller).
- ⚠️ «romero única flor de julio» ya se usó 4× — descansar hasta mediados de agosto.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas, también las de agosto → EJECUTADO. Liquidámbar B-37 → hecho.
- **01/08:** «mándamela cuando esté lindo» → EJECUTADO 02/08 con verificación meteorológica.
- **02/08:** «¿qué más puedo podar? ¿qué hago con el neem?» → contestado 02/08 (que-mas-podo) y **continuado hoy** con el Taller nº2.
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.

## 📈 Estado del sistema + jardín (agosto 2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable.
- Jardín en DORMANCIA, saliendo. ~51 días al equinoccio (23/09). Sin heladas en el horizonte del pronóstico (mínimas 8,5-12,4°C toda la semana); riesgo real hasta fin de agosto, pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, arranque con lechuga a la vuelta · hortensia B-5a/b → a tierra antes del viaje, rincón sur junto a la pera B-39 · **objetivo declarado del usuario = «más flor»** (por eso el Taller nº2 va sobre los dos únicos arbustos donde la poda multiplica flor).
- **Pendientes reales al 03/08: 12** — 3 antes del viaje + 9 a la vuelta.

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37 / palto B-36 / pileta (sol de mañana) · oeste/frente = fotinias, ligustro F-9, fresno F-10 (sol de tarde) · **romero B-26 = única que florece en julio** · mandarina B-24 + pindó B-8 en fruto en invierno · viraró B-32 (nativo) florece en agosto · limonero B-23 fruta 12/12 · plantines de palta contra la pared, SIN TOCAR · B-41 caqui identidad EN DUDA · B-45 sin id.
**Poda de Prunus (fichas):** durazno 40-50% vaso abierto · ciruelo F-4 25-35% · ciruela B-38 30% + sacar madera >4 años · ventana = yema hinchada sin abrir · gomosis = riesgo principal, alcohol 70% y sellar cortes >1,5 cm.
**Poda de flor (fichas, verificado 03/08):** crespón B-9 *Lagerstroemia indica* 50-70%, muñones de 2-4 yemas, florece en madera nueva, «crepe murder» es mito, corteza canela exfoliante, brota tarde · althea B-18 *Hibiscus syriacus* 40-50%, muñones 2-3 yemas, madera nueva, rústica ante heladas, cada flor dura un día · **hortensia B-5 florece en madera VIEJA → NO podar ahora**, su poda va feb-mar · ninguno de los dos es Prunus → sin gomosis, sin pasta cicatrizante · no fertilizar hasta ver el primer brote.

## Conclusiones de los pushN (por feedback real)

- **02/08 (domingo, excepción por pedido) — el-taller re-push: ÉXITO.** 😍 + **prendió el 2º slot** + 7/7 pasos otra vez + ticks B-30/B-38. Verificar la condición del mundo real («cuando esté lindo») y mostrarlo citado fue determinante.
- **02/08 — que-mas-podo: SIN reacción pero CON acción.** Dwell corto, ninguna señal de la escala… y sin embargo podó F-4 y entró a las tareas de B-9/B-18. Una respuesta directa a su pregunta convierte en conducta aunque no gane emoji.
- **01/08 (sábado) — el-taller: ÉXITO MÁXIMO.** 😍 + slot lun18 + 7/7 pasos ×2 + feedback positivo. El molde a serializar.
- **01/08 — jardin-hoy: floja ese día.** Abierta 4 h tarde, dwell 25s, sin señal. No es fatiga del canal: ese día el valor estaba en el Taller. Sostener el canal tarea sin subirle la intensidad.
- **31/07 (viernes) — el-parte: MASOMENOS con veredicto claro.** Leyó todo (75s, 100%) pero ambos slots en NO + meh. Formato-diario archivado.
- **30/07 (jueves) — jardin-hoy GANADORA, día tier-1.** 3 feedback_text (oro): liquidámbar hecho, «foto + caja de comentario en las tareas de agosto» y «viaje 7-23, recomendame antes/después». Los tres EJECUTADOS.
- **29/07 — masomenos.** Fotos solas sin sustancia ni gancho de acción no alcanzan.
- **28/07 — negativo.** esto-o-esto muerto; vos-decidis v3 rechazada.
- **24/07:** jardin-hoy ganadora (3 feedback_text). Minimalismo + tareas reales + caja de pedidos.
- **21/07:** asamblea — «Está todo perfecto». Sustancia + honestidad funcionan.

## TODO / próximos experimentos

- **Martes 4 al jueves 6 (días sin slot):** solo mantenimiento. Mirar si aparecen `t2-arbusto-B-9` / `t2-arbusto-B-18` y en qué paso se traba (`t2-paso-N`). Si el martes a la noche tildó los dos → la jardin-hoy del jueves debería ser **cierre y despedida**, no una lista nueva.
- **Jueves 6, slot tarea 10:00:** es la última push antes del viaje. Corta y de cierre: qué quedó hecho + la confirmación explícita de que del 7 al 23 **no le voy a mandar tareas**. Respetarlo a rajatabla — es la prueba de confianza más barata que tengo.
- **7 al 23/08 (viaje):** caen adentro sáb 8, lun 10, sáb 15, lun 17, sáb 22. **NO mandar tareas.** Las experiencias del slot van solo si son de lectura placentera y cero-deber; si no hay una buena, no mandar nada. Evaluarlo día a día.
- **Lunes 24/08 — reentrada:** plan de las 9 tareas ordenadas por rendimiento en flor (su objetivo declarado) + **Taller nº3 = pitósporo B-43** (reducción, el trabajo más largo de la lista).
- **Before/after con fotos reales:** el paso «mandame una foto» del Taller es la puerta de entrada. Si sube foto del crespón podado, evaluarla y devolverle veredicto es el siguiente salto de valor.
- `se-multiplican-solos` (propagación gratis) sigue en el pool para **septiembre-octubre**, con la savia en movimiento.
