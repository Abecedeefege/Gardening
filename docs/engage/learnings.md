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

## 🕐 05/08 — HALLAZGO MAYOR: **la hora manda más que el formato**

Medí por primera vez el **delay entre envío y primera apertura** de todo el canal. El resultado reordena las prioridades:

| Envío (MVD) | Push | 1ª apertura | Delay |
|---|---|---|---|
| Lun 03/08 **18:48** | el-taller-2 | 19:20 | **+32 min** ⚡ |
| Vie 31/07 18:02 | el-parte | 19:43 | +1 h 41 |
| Sáb 01/08 12:06 | el-taller | 14:14 | +2 h 08 |
| Dom 02/08 14:46 | que-mas-podo | 18:43 | +3 h 57 |
| **Mar 04/08 11:38** | **tarjeta-campo** | **nunca** | **⬛** |

**Su curva de actividad real** (page_visits por hora): pico **14-15 h (29)**, segundo pico **17 h (10)**, tarde-noche 17-21 h sostenida (26). La franja **09-12 h junta 11 visitas en dos semanas: es su hora MUERTA.**

- **Corolario duro:** una push antes del mediodía llega cuando el teléfono no se mira, y para cuando lo agarra a las 14 h ya está sepultada. **No es un problema de gancho: es un problema de reloj.**
- Esto reinterpreta el histórico: la jardin-hoy de las 10-12 h viene «floja» desde siempre (01/08 abierta 4 h tarde, dwell 25 s). **Nunca fue el contenido.**
- El slot **Lun 18:00 es el mejor activo del sistema** (+32 min). El **Sáb 11:00 sobrevive porque el sábado él está en casa** (el-taller abrió a las 2 h y fue el éxito máximo) — pero es el slot frágil.
- ⚠️ **Los horarios son mandato del usuario, no los cambio por mi cuenta.** La pregunta va DENTRO de la app: en la experiencia del **sáb 08/08** (o la primera post-viaje) ofrecerle mover la push de tareas de 10:00 a ~14:30 y el slot Sáb 11:00 a 14:00, mostrándole este mismo cuadro. Es un dato suyo, medido, y pedirle permiso con evidencia es exactamente el gesto que ya rindió dos veces.

## 🃏 04/08 — LA TARJETA DE CAMPO: cero apertura (⬛)

Enviada mar 11:38 (201, subscripción `pix9` active). A las 24 h: **0 clicks, 0 visitas, 0 `tc-hecho-*`, 0 reacción, 0 slot, 0 feedback.** El primer push sin una sola apertura desde que el logging es confiable.

- **Honestidad:** no sé si podó sin la tarjeta o no hizo nada — los ticks eran el instrumento y no hay ninguno. B-9/B-18/B-5a siguen `active` en `task_states.json`. **No dar por hecho ni por no-hecho: preguntárselo.**
- Dos causas, en orden de peso: ① **la hora** (11:38, su franja muerta) ② el título vendía MI proceso («✂️ Verifiqué: hoy no llueve») en vez de un beneficio suyo.
- **El formato NO queda muerto — queda sin testear.** La hipótesis «corto para ejecutar» nunca llegó a medirse. Re-testear a las 14:30, no antes del mediodía. No recurre (sin aprobación).

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

`2026-08-01-el-taller` — **APPROVED lunes 18:00 + sábado 11:00.** El mejor resultado del canal.

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95%, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados («el error:») ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-paso-N` dice dónde se traba; `taller-arbol-<code>` dice qué cerró de verdad. Replicar en todo lo que sea multi-tarea.
- El taller largo **de tarde/noche** es el formato que consume ENTERO, tres veces confirmado (01, 02 y 03/08).

## 📌 MANDATO 24/07 (canal tarea — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS.** Consolidada en **«Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable, se REEDITA en su lugar). NO encolar task-dia/pendientes/top3 sueltas. NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
2. **jardin-hoy lleva siempre:** vistazo de 5 s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`) + caja «🙋 Pedime lo que necesites».
3. **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.

## ✈️ CONTEXTO DOMINANTE — VIAJE **7 al 23 DE AGOSTO**

- **Antes de irse (jue 6 = último día) = 3:** crespón **B-9** + althea **B-18** (poda de flor) + **hortensia B-5a/b a tierra** (rincón sur junto a la pera B-39). Opcional: hiedra **B-15**. ✅ Cerrados: durazno B-30/35, ciruela B-38, ciruelo F-4, liquidámbar B-37.
- **La ventana seca ya pasó** (mar 4 fue el último día 0 mm; mié 1,6 mm; **jue 19,1 mm + 48 km/h**). Realidad al 05/08: **las 3 podas se corren al 24/08 y salen bien igual** — decirlo así, sin reproche y sin inventar urgencia.
- **Durante (7–23/8) = 0. NO nagear NADA.** Caen adentro sáb 8, lun 10, sáb 15, lun 17, sáb 22.
- **A la vuelta (24–31/8) = 9 + las 3 corridas:** pitósporo B-43-2, hibisco B-4, podranea F-2, cerco B-7·11·31·33, abelia F-7, gardenia acidificar B-25, 3ª de neem B-25-3, caqui B-41, huerta/lechuga. **B-41 no se nombra como urgencia hasta primavera** (identidad en duda, pedido del usuario).
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página.
- ⚠️ Los ticks del Taller (`taller-arbol-*`, `tc-hecho-*`) **NO escriben `task_states.json`** — son eventos de engagement. B-30/B-38/F-4 siguen `active` aunque estén hechos. No contradecir al usuario con eso.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo». MUERTO.
- **checklist de viaje / «antes de irte» como deberes:** el viaje se trata como **tranquilidad o como ventaja**, nunca como lista de pendientes.
- **vos-decidis / feed-de-decisiones:** el eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).
- ⚠️ **Distinguir muerto de mal-horario.** Antes de enterrar un formato, chequear a qué hora se mandó. La tarjeta de campo casi se entierra por error.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín.
- **Ayudarlo a HACER > informarlo.**
- **LA HORA ES UNA PALANCA DE PRIMER ORDEN (nueva, 05/08).** 14-15 h y 17-20 h convierten; 09-12 h no existe. Un buen contenido a la hora muerta mide igual que un contenido malo.
- **Un formato por momento.** Taller largo = víspera/aprender. Tarjeta corta = el día/ejecutar (sin testear todavía).
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. Cuando la agenda la pone él, mi trabajo es responder, no proponer.
- **Timing verificado > urgencia inventada.** Ir a buscar el dato del mundo real y mostrar que se verificó (rindió 02/08 y 04/08).
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla. **FOTOS REALES = need validado.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** un Taller / una tarjeta de campo es monotemático — su cast lo define la TAREA, no el elenco. El ≥70% fresco no aplica ahí.
- ⚠️ **Quemados:** carozos (B-30, B-35, F-4, B-38) hasta el **09/08**; **B-9, B-18, B-5a hasta el 11/08**; B-15 hasta el 10/08.
- ⚠️ «romero única flor de julio» ya se usó 4× — descansar hasta mediados de agosto.
- **Elenco FRESCO para la reentrada:** pitósporo B-43, hibisco B-4, podranea F-2, abelia F-7, gardenia B-25, **viraró B-32 (florece en agosto, sin usar)**, mandarina B-24, pindó B-8, limonero B-23.
- Estaca de madera dura **gastada el 04/08** → `se-multiplican-solos` (sept-oct) va por semilla / gajo verde / división de mata.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas → EJECUTADO. Liquidámbar B-37 → hecho.
- **01/08:** «mándamela cuando esté lindo» → EJECUTADO 02/08 con verificación meteorológica.
- **02/08:** «¿qué más puedo podar? ¿qué hago con el neem?» → contestado 02/08 + Taller nº2 el 03/08.
- **03/08:** «recordame las podas… si no llueve» → EJECUTADO 04/08 (tarjeta de campo; nunca la abrió, ver arriba).
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.

## 📈 Estado del sistema + jardín (agosto 2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable. Sin feedback de texto nuevo desde el 04/08 00:08.
- Jardín en DORMANCIA, saliendo. ~49 días al equinoccio (23/09). Mínimas 8-12 °C, sin heladas en el pronóstico; riesgo real hasta fin de agosto, pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, arranque con lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado del usuario = «más flor»**.
- **Pendientes reales al 05/08: 12** (3 que se corren al 24 + 9 de la vuelta).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37 / palto B-36 / pileta · oeste/frente = fotinias, ligustro F-9, fresno F-10 · **romero B-26 = única que florece en julio** · mandarina B-24 + pindó B-8 en fruto en invierno · viraró B-32 florece en agosto · limonero B-23 fruta 12/12 · plantines de palta contra la pared, SIN TOCAR · B-41 caqui identidad EN DUDA · B-45 sin id.
**Poda de Prunus (fichas):** durazno 40-50% vaso abierto · ciruelo F-4 25-35% · ciruela B-38 30% · ventana = yema hinchada sin abrir · gomosis = riesgo principal, alcohol 70%.
**Poda de flor (fichas):** crespón B-9 *Lagerstroemia indica* 50-70%, muñones 2-4 yemas, madera nueva, «crepe murder» es mito, corteza canela exfoliante · althea B-18 *Hibiscus syriacus* 40-50%, muñones 2-3 yemas, madera nueva, rústica ante heladas, flor de un día, flor nacional de Corea del Sur · **hortensia B-5 florece en madera VIEJA → NO podar ahora**, su poda va feb-mar; es la más sedienta del jardín · ninguno de los dos arbustos de flor es Prunus → sin gomosis, sin pasta cicatrizante · no fertilizar hasta ver el primer brote.
**Propagación (04/08):** crespón y althea = estaca de madera dura en dormancia, 20-25 cm, 3-4 yemas, corte recto abajo / bisel arriba, 2/3 enterrado, sombra, riego mínimo.

## Conclusiones de los push (por feedback real)

- **04/08 — tarjeta-campo: ⬛ CERO APERTURA.** Único push sin una sola visita. Causa principal: la hora (11:38). Formato sin testear, no muerto.
- **03/08 — el-taller-2: MASOMENOS-ALTO.** 7/7 pasos + dwell 166 s + un pedido concreto, cero reacción. Abrió a los **32 min** (mejor delay del canal): el envío 18:48 es oro.
- **02/08 — el-taller re-push: ÉXITO.** 😍 + prendió el 2º slot + 7/7 pasos + ticks B-30/B-38. Verificar la condición del mundo real fue determinante.
- **02/08 — que-mas-podo: SIN reacción pero CON acción.** Podó F-4 y entró a B-9/B-18. **El clic no es la métrica; el tick sí.**
- **01/08 — el-taller: ÉXITO MÁXIMO.** 😍 + slot lun18 + 7/7 ×2 + feedback positivo. El molde.
- **01/08 — jardin-hoy: floja** (sáb 10:58, abierta 4 h tarde, dwell 25 s). Releída al 05/08: **era la hora, no el contenido.**
- **31/07 — el-parte: MASOMENOS con veredicto claro.** Leyó todo, ambos slots en NO. Formato-diario archivado.
- **30/07 — jardin-hoy GANADORA, día tier-1.** 3 feedback_text, los tres ejecutados.
- **28/07 — negativo.** esto-o-esto muerto; vos-decidis v3 rechazada.
- **24/07 — jardin-hoy ganadora.** Minimalismo + tareas reales + caja de pedidos.
- **21/07 — asamblea:** «Está todo perfecto». Sustancia + honestidad funcionan.

## TODO / próximos experimentos

- **JUEVES 6/08 (último día antes del viaje) — jardin-hoy = CIERRE Y DESPEDIDA.** Corta. Tres cosas y nada más: ① **preguntarle sin dar nada por hecho** si llegó a podar B-9/B-18 (no hay ticks ni estado; ofrecerle un tilde de una sola tocada) ② decirle que las 3 pendientes **se corren al 24/08 y salen igual de bien** — el jueves llueve 19 mm, no hay drama ③ **el compromiso explícito: del 7 al 23 NO le llega ninguna tarea.** Respetarlo a rajatabla es la prueba de confianza más barata que tengo. **Encolar a las 10:00 por mandato, pero es su hora muerta: meter todo el valor en el título y el body.**
- **SÁBADO 8/08 (ya de viaje) — experiencia 11:00:** solo si es de lectura placentera y cero-deber. Ahí va la **pregunta del horario** (cuadro de delays + oferta de mover a 14:30). Agrupa `el-taller` (aprobada en ese slot) con contenido RENOVADO.
- **7 al 23/08 (viaje): NO mandar tareas.** Evaluar día a día; si no hay una buena experiencia, **no mandar nada**.
- **LUNES 24/08 — reentrada:** las 12 tareas ordenadas por rendimiento en flor + **Taller nº3 = pitósporo B-43** + **preguntar por las estacas** si las llegó a poner.
- **Before/after con fotos reales:** si sube foto del crespón podado, evaluarla y devolverle veredicto es el siguiente salto de valor.
