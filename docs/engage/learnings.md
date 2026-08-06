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

## ✈️ CONTEXTO DOMINANTE — **VIAJE 7 AL 23 DE AGOSTO (arranca mañana)**

- **Compromiso publicado el 06/08, a cumplir a rajatabla: del 7 al 23 NO se manda NINGUNA push de tareas.** Caen adentro 7 slots de tarea (sáb 8, lun 10, jue 13, sáb 15, lun 17, jue 20, sáb 22) y 5 de experiencia (sáb 8, lun 10, sáb 15, lun 17, sáb 22) = 12 notificaciones que NO se mandan por calendario. Se lo dije con ese número. **Romperlo quema el activo más caro que tengo.**
- Las experiencias del viaje quedaron sujetas a su respuesta en `viaje-silencio` (`total` / `solo-lindo` / `todo`). **Default si no contesta: 0 tareas garantizado + experiencia solo si es lectura placentera y cero-deber.** Leer ese answer antes de encolar cualquier cosa entre el 8 y el 22.
- **Las 3 abiertas se corrieron al 24/08** (crespón B-9, althea B-18, hortensia B-5a/b) con justificación técnica real, sin reproche: el límite es la yema, no el calendario. **Excepción: la hortensia sí tiene reloj → 29-30/08, antes del brote.**
- ✅ Cerradas: durazno B-30/35, ciruela B-38, ciruelo F-4, liquidámbar B-37, pera B-39.
- **A la vuelta (24-31/08) = 9 + las 3 corridas = 12.** B-41 caqui NO se nombra como urgencia hasta primavera (identidad en duda, pedido del usuario).
- Verificar SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página.
- ⚠️ Los ticks del Taller (`taller-arbol-*`, `tc-hecho-*`) **NO escriben `task_states.json`** — son eventos de engagement. No contradecir al usuario con eso.

## 🕐 HALLAZGO MAYOR (05/08, confirmado 06/08): **la hora manda más que el formato**

| Envío (MVD) | Push | 1ª apertura | Delay |
|---|---|---|---|
| Lun 03/08 **18:48** | el-taller-2 | 19:20 | **+32 min** ⚡ |
| Vie 31/07 18:02 | el-parte | 19:43 | +1 h 41 |
| Sáb 01/08 12:06 | el-taller | 14:14 | +2 h 08 |
| Dom 02/08 14:46 | que-mas-podo | 18:43 | +3 h 57 |
| **Mar 04/08 11:38** | **tarjeta-campo** | **nunca** | **⬛** |

- Curva de actividad real (page_visits por hora): pico **14-15 h**, segundo pico **17-20 h**. La franja **09-12 h junta 11 visitas en dos semanas: hora muerta.**
- **Corolario duro:** un buen contenido a la hora muerta mide igual que un contenido malo. **No es gancho: es reloj.**
- ⚠️ **SEGUNDO HALLAZGO (06/08): el dispatcher LAGUEA.** `send_at` ≠ envío real. Medido: 10:00→12:41 (03/08), 09:30→**11:38** (04/08), 10:00→10:58 (01/08), 18:00→18:48 (03/08). Lag observado 0,5 a 2,7 h. **Encolar a las 14:30 puede caer 16:30.** Si el usuario habilita el cambio de horario, encolar ~1 h ANTES del objetivo real y verificar contra `send_log.json`, no contra la cola.
- ⚠️ **Los horarios son mandato del usuario, no los cambio por mi cuenta.** La pregunta ya está publicada DENTRO de la app (jardin-hoy 06/08, `engageAnswer('horario-tareas', …)`) con el cuadro de delays a la vista. **Leer ese answer antes de la reentrada del 24/08.**

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (aprobado en LOS DOS slots, 01-02/08)

`2026-08-01-el-taller` — **APPROVED lunes 18:00 + sábado 11:00.** El mejor resultado del canal.

- Señal: **7/7 pasos ×3 pasadas**, dwell 168 s @95%, **😍 las dos veces**, feedback positivo, y **ticks por árbol** horas después.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados («el error:») ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-paso-N` dice dónde se traba; `taller-arbol-<code>` dice qué cerró de verdad.
- El taller largo **de tarde/noche** es el formato que consume ENTERO, tres veces confirmado (01, 02 y 03/08).

## 📌 MANDATO 24/07 (canal tarea — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS.** Consolidada en **«Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable, se REEDITA en su lugar). NO encolar task-dia/pendientes/top3 sueltas. NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
2. **jardin-hoy lleva siempre:** vistazo de 5 s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`) + caja «🙋 Pedime lo que necesites».
3. **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo». MUERTO.
- **checklist de viaje / «antes de irte» como deberes:** el viaje se trata como **tranquilidad o como ventaja**, nunca como lista de pendientes.
- **vos-decidis / feed-de-decisiones:** el eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).
- ⚠️ **Distinguir muerto de mal-horario.** Antes de enterrar un formato, chequear a qué hora se mandó **y a qué hora se envió de verdad** (send_log, no la cola). La tarjeta de campo casi se entierra por error.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Ayuda técnica REAL sobre SU jardín.
- **Ayudarlo a HACER > informarlo.**
- **LA HORA ES PALANCA DE PRIMER ORDEN.** 14-15 h y 17-20 h convierten; 09-12 h no existe.
- **Un formato por momento.** Taller largo = víspera/aprender. Tarjeta corta = el día/ejecutar (sin testear todavía).
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. Cuando la agenda la pone él, mi trabajo es responder, no proponer.
- **Timing verificado > urgencia inventada.** Ir a buscar el dato real y mostrar que se verificó (rindió 02/08 y 04/08).
- **Decir «hoy no hay nada que hacer» cuando es verdad (nuevo, 06/08).** Con 20,8 mm y 59 km/h verificados, el contenido honesto es CERO tareas. Inventar una urgencia el último día antes de un viaje habría sido el peor uso del canal.
- **Preguntar en vez de asumir.** No hay ticks de B-9/B-18 → se lo pregunto con una sola tocada, no lo doy por hecho ni por no-hecho.
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla. **FOTOS REALES = need validado.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** el canal tarea (jardin-hoy / taller / tarjeta) es monotemático — su cast lo define la TAREA, no el elenco. El ≥70% fresco no aplica ahí.
- ⚠️ **Quemados:** carozos (B-30, B-35, F-4, B-38) hasta el **09/08**; **B-9, B-18, B-5a hasta el 13/08**; B-15 hasta el 10/08; B-39 hasta el 13/08.
- ⚠️ «romero única flor de julio» ya se usó 4× — descansar hasta mediados de agosto.
- **Elenco FRESCO reservado para la reentrada del 24/08:** **viraró B-32 (florece en agosto, nunca usado)**, mandarina B-24, pindó B-8, limonero B-23, mirto B-27, guayabo F-1 (descansa desde el 25/07), pitósporo B-43, hibisco B-4, podranea F-2, abelia F-7, gardenia B-25.
- Estaca de madera dura **gastada el 04/08** → `se-multiplican-solos` (sept-oct) va por semilla / gajo verde / división de mata.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera.
- **30/07:** foto + caja de comentario en TODAS las tareas → EJECUTADO. Liquidámbar B-37 → hecho.
- **01/08:** «mándamela cuando esté lindo» → EJECUTADO 02/08 con verificación meteorológica.
- **02/08:** «¿qué más puedo podar? ¿qué hago con el neem?» → contestado 02/08 + Taller nº2 el 03/08.
- **03/08:** «recordame las podas… si no llueve» → EJECUTADO 04/08 (tarjeta de campo; nunca la abrió — era la hora).
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.

## 📈 Estado del sistema + jardín (06/08/2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable.
- **Silencio total del usuario desde el 04/08 00:15** (último evento: dwell tras el feedback del taller nº2). 0 eventos el 04, 05 y 06. Coherente con víspera de viaje + la tarjeta mandada a la hora muerta. **No sobre-interpretar como rechazo.**
- Parte verificado 06/08 06:00 (open-meteo, MVD): **hoy 20,8 mm · 59 km/h · 100% prob · máx 15,2 °C**. Del 8 al 15/08: 0-2 mm, mínimas 7-9 °C, **sin heladas**. El jardín aguanta solo.
- Jardín en DORMANCIA, saliendo. ~48 días al equinoccio (23/09). Riesgo de helada real hasta fin de agosto, pica al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, arranque con lechuga a la vuelta · hortensia B-5a/b → a tierra, rincón sur junto a la pera B-39 · **objetivo declarado del usuario = «más flor»**.

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37 / palto B-36 / pileta · oeste/frente = fotinias, ligustro F-9, fresno F-10 · **romero B-26 = única que florece en julio** · mandarina B-24 + pindó B-8 en fruto en invierno · viraró B-32 florece en agosto · limonero B-23 fruta 12/12 · plantines de palta contra la pared, SIN TOCAR · B-41 caqui identidad EN DUDA · B-45 sin id.
**Poda de Prunus (fichas):** durazno 40-50% vaso abierto · ciruelo F-4 25-35% · ciruela B-38 30% · ventana = yema hinchada sin abrir · gomosis = riesgo principal, alcohol 70%.
**Poda de flor (fichas):** crespón B-9 *Lagerstroemia indica* 50-70%, muñones 2-4 yemas, madera nueva, «crepe murder» es mito, corteza canela exfoliante, **de los últimos en despertar (septiembre)** · althea B-18 *Hibiscus syriacus* 40-50%, muñones 2-3 yemas, madera nueva, **brota tardísimo → el mayor margen del jardín**, flor de un día, flor nacional de Corea del Sur · **hortensia B-5 florece en madera VIEJA → NO podar ahora**, su poda va feb-mar; es la más sedienta; **su trasplante SÍ tiene reloj: antes del brote** · ninguno de los dos arbustos de flor es Prunus → sin gomosis, sin pasta cicatrizante · no fertilizar hasta ver el primer brote.
**Propagación (04/08):** crespón y althea = estaca de madera dura en dormancia, 20-25 cm, 3-4 yemas, corte recto abajo / bisel arriba, 2/3 enterrado, sombra, riego mínimo.

## Conclusiones de los push (por feedback real)

- **06/08 — jardin-hoy «cierre y despedida»:** encolada 10:00 (hora muerta por mandato → todo el valor en título y body: «Nada que hacer hoy (ni hasta el 24)»). Tres apuestas: ① cero tareas honesto con el parte verificado ② el compromiso numerado de las 12 push que NO se mandan ③ la pregunta del horario con SU cuadro de delays. Señales a mirar al volver: `podas-previaje`, `viaje-silencio`, `horario-tareas`.
- **04/08 — tarjeta-campo: ⬛ CERO APERTURA** (confirmado a 48 h). Único push sin una sola visita. Causa: la hora real de envío (11:38). Formato sin testear, no muerto.
- **03/08 — el-taller-2: MASOMENOS-ALTO.** 7/7 pasos + dwell 166 s + un pedido concreto, cero reacción. Abrió a los **32 min**: el envío 18:48 es oro.
- **02/08 — el-taller re-push: ÉXITO.** 😍 + prendió el 2º slot + 7/7 pasos + ticks B-30/B-38. Verificar la condición del mundo real fue determinante.
- **02/08 — que-mas-podo: SIN reacción pero CON acción.** Podó F-4 y entró a B-9/B-18. **El clic no es la métrica; el tick sí.**
- **01/08 — el-taller: ÉXITO MÁXIMO.** 😍 + slot lun18 + 7/7 ×2 + feedback positivo. El molde.
- **01/08 — jardin-hoy: floja** (sáb, abierta 4 h tarde, dwell 25 s). Releída: **era la hora, no el contenido.**
- **31/07 — el-parte: MASOMENOS con veredicto claro.** Leyó todo, ambos slots en NO. Formato-diario archivado.
- **30/07 — jardin-hoy GANADORA, día tier-1.** 3 feedback_text, los tres ejecutados.
- **24/07 — jardin-hoy ganadora.** Minimalismo + tareas reales + caja de pedidos.
- **21/07 — asamblea:** «Está todo perfecto». Sustancia + honestidad funcionan.

## TODO / próximos experimentos

- **7 al 23/08 (VIAJE): 0 push de tareas, sin excepción.** Antes de encolar cualquier experiencia en sáb 8 / lun 10 / sáb 15 / lun 17 / sáb 22, leer el answer `viaje-silencio`. `total` → no mandar nada. `solo-lindo` → una sola, lectura placentera, cero-deber, con `el-taller` (aprobada) linkeada dentro. `todo` → cadencia normal de experiencias. Sin respuesta → default `solo-lindo` con listón alto; si no hay algo genuinamente bueno, **no mandar nada**.
- **LUNES 24/08 — reentrada.** ① Leer `podas-previaje` y armar la lista real (12 o 10 tareas según qué haya podado) ② aplicar `horario-tareas` si contestó — **encolar ~1 h antes del objetivo por el lag del dispatcher** ③ **Taller nº3 = pitósporo B-43** (el trabajo más largo, primero de la vuelta) ④ preguntar por las estacas si las llegó a poner ⑤ recordar la hortensia para el 29-30/08, que es la única con reloj.
- **Re-test de la tarjeta de campo** a las 14:30 (nunca antes del mediodía) en la primera semana de vuelta: el formato corto-para-ejecutar nunca se midió.
- **Before/after con fotos reales:** si sube foto del crespón podado, evaluarla y devolverle veredicto es el siguiente salto de valor.
- **Elenco fresco de septiembre:** viraró B-32 en flor (agosto-septiembre, nunca usado) + `se-multiplican-solos` por semilla/gajo verde/división.
