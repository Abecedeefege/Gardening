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
- **Aprobación = recurrencia.** Solo vuelve lo que el usuario prendió (😍 / slot en «sí» / `engageApprove`). Pending sin aprobar no se borra: simplemente no recurre. **La única aprobada sigue siendo `el-taller` (n°1), prendida en los DOS slots.** Todas las del viaje (`tarjeta-campo`, `el-hueco`, `mandarina`, `florecio`, `preguntas-abiertas`, `perfume-de-octubre`) quedaron cerradas el 24/08 como **no-exposición** y no recurren solas.
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Si el pedido es condicional («cuando esté lindo»), la condición se **verifica con datos reales** antes de encolar y se muestra citada.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## 🚨 LAS DOS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín. Las 3 pushes con señal activa del archivo traían **ayuda ejecutable con la herramienta en la mano**. `el-parte` perdió con el layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ninguna experiencia puede tener su primer control interactivo debajo del **35 % del scroll**, **medido renderizado en Chromium 390×780** (nunca por offset de caracteres). Es un **seguro contra la lectura corta**, no un sustituto de la #1.
Script en el scratchpad (`audit.js`): playwright con `executablePath: /opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ **Filtrar por visibilidad real** (`offsetParent`, `display`, rect ≠ 0) y **limitar a `.wrap`** — si no, mide los pasos ocultos del wizard, las cajas `.tfb` colapsadas y la quickbar inyectada, y da 0 % falso.

Auditoría acumulada: **taller-3 9,4 % · jardin-hoy 21,6 %** (medidos hoy) · el-taller 7,9 % · el-taller-2 · tarjeta-campo 0 % · perfume-de-octubre 9,5 % · el-parte **27,3 % (compliant y perdió igual)** · preguntas-abiertas **75 % (único caso donde el layout SÍ explicó el resultado)**.

**Barra de señal rápida** (`engage.js`, 18/08): flota al 25 % de scroll o a los 25 s. **Sigue SIN un solo evento medido** — buscar `via:"quickbar"`, `quicksignal_dismiss` y `quicksignal_to_text` en la próxima señal que llegue.

## ✈️ EL VIAJE (7 AL 23/08) — CERRADO Y COBRADO

- **Compromiso publicado el 06/08: del 7 al 23 ninguna push de tareas. 7 de 7 slots cumplidos** (sáb 8, lun 10, jue 13, sáb 15, lun 17, jue 20, sáb 22). **Cobrado hoy 24/08 en el hero de jardin-hoy**, con el dato verificable: las 4 push de esa ventana fueron experiencias, ninguna tarea.
- **El viaje NO fue ventana de medición.** Ningún eje se archiva con evidencia del 07 al 23. Las 6 proposals de esa ventana quedaron con `result_notes` de cierre y **no recurren**; sus ejes se re-miden de cero cuando les toque turno.
- **Sin responder desde antes del viaje:** `podas-previaje` (¿podó B-9 y B-18?), `viaje-silencio`, `horario-tareas`. La primera se **volvió a preguntar hoy** como `podas-vuelta` (primer control de jardin-hoy, 21,6 %) porque define la lista entera. Las otras dos **no se re-preguntan**: acumular preguntas viejas es exactamente la queja de «muy cargado».
- ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo muestra los carozos `active`. **Para el usuario están hechos: nunca contradecirlo.** Verificar siempre contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (shape real `{"tasks": {...}}`).

## 🌧️ PARTE — 11ª verificación (24/08, open-meteo MVD)

| Fecha | Mín | Máx | Lluvia |
|---|---|---|---|
| **24/08 (hoy)** | 7,9 | 9,0 | **0,0** |
| 25/08 | **4,5** | 10,9 | 0,0 |
| 26/08 | 7,4 | **15,1** | 0,1 |
| **27/08** | 11,2 | 13,2 | **8,2 mm** |
| 28-31/08 | 8,8-11,3 | 11,2-12,5 | 0 / 0 / 0 / 0,6 |

- **Publicado hoy:** tres días secos (lun-mar-mié) → **jueves 27, único día con lluvia de los próximos diez**. Es la **3ª verificación seguida del DÍA**; el milímetro se movió (9,6 → 10,0 → 8,2) y **eso se publicó tal cual**, porque decir que el número se mueve es lo que hace creíble que el día no.
- **Cero heladas** en los 10 de pronóstico y en los 21 medidos (mínima absoluta 6,9° el 8/08). Mínima de la semana 4,5° el martes.
- El «primer calor» del 26/08 **repitió 15,1 por primera vez** tras moverse 5 veces. Sigue sin publicarse: una repetición no es una serie.
- **Regla dura:** solo se publica lo que sigue en pie el día que se encola. A >72 h el número no es publicable.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- Señal del n°1: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 dos veces**, feedback positivo y **ticks por árbol** horas después. El n°2: 7/7 pasos, dwell 166 s, cero reacción (masomenos-alto).
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre **con la herramienta en la mano** ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios en vez de texto.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad.
- 🆕 **Taller n°3 (24/08, pitósporo B-43) — entregado, con una variable nueva a propósito:** la primera pantalla ya no es «cómo se hace» sino **«cuánto te cuesta»**. B-43 florece en madera vieja → bajarlo ahora sacrifica el azahar de octubre, y su propia ficha ofrece dos ventanas legítimas. **Qué mirar mañana:** si se activa `taller3-cuando`, el PRECIO antes que la tarea pasa a ser la apertura estándar del canal. Y `taller3-paltas` mide por fin si **delegarme trabajo** convierte (quedó sin medir el 22/08 por el viaje).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75 s enteros y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes** · **vos-decidis** (el eje AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** (aspiración sin acción).
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).
- **Era gimmick (feed falso, superpoderes):** el 16/08 los abrió **por voluntad propia** y rebotó en **9 s / 28 %** en los dos. No retienen ni cuando los busca él.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando no puede hacer, lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **LA PREDICCIÓN VERIFICADA (23/08).** Guardar lo que dije y volver con el **registro medido** al lado es la credibilidad más barata que tengo, y no le cuesta un tap. **Toda ventana que le marque queda anotada para volver a mostrarla cumplida (o no).** Ya se cobró dos veces; **la tercera vez sería repetición** — el próximo cobro necesita una predicción NUEVA (candidata: el rebrote de B-43 en septiembre-octubre, ya anotado dentro del Taller n°3).
- **🆕 EL PRECIO ANTES QUE LA TAREA (24/08, sin veredicto).** Decirle qué **pierde** por hacer lo que le pido, antes de pedírselo. Es el veto del 22/08 dado vuelta y con la decisión en su mano.
- **La contradicción interna del catálogo es una mina — minada entera** (`audit_flor_poda.json`). Publicadas: azarero B-7 (22/08) y **las dos paltas B-22/B-36 (hoy)**. **Queda sin publicar: coronita F-5 y romero B-26** (solapes reales, menores). Los otros 5 son benignos: publicarlos como errores quemaría credibilidad.
- **El título es el activo más medido.** **Sustantivo concreto + número + algo que le pertenece + pérdida.**
- **El dato computado sobre su propio catálogo es munición.** Usados: floración · fruta · acción→floración · campos «a confirmar» · poda×floración (completo). **Sin usar: el cruce poda×FRUTA (dic-ene) · dependencia de un solo ejemplar (44/52) · luz real vs la que pide cada ficha · calendario de perfume aplicado a PLANTAR.**
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. · **Timing verificado > urgencia inventada.**
- **Decir «hoy no hay nada que hacer» cuando es verdad.** El silencio del canal tarea ES contenido: se cobró hoy.
- **Minimalismo + REAL + VISUAL.** Fotos reales = need validado. Diagrama propio > párrafo. · **Declarar lo que NO sé suma.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.
- **Antes de archivar un formato, verificar la medición que lo condena.**

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Una decisión guardada en learnings NO anula el ledger: el ledger gana.**
- **Excepción:** el canal tarea (jardin-hoy / taller) es monotemático — su cast lo define la TAREA, no el elenco.
- ⚠️ **Quemados hasta el 31/08** (corrida de hoy): **B-43, B-22, B-36** + el cast del canal tarea (B-9, B-18, F-2, B-5a/b, B-7, F-7, B-25, B-4, B-1, B-15).
- ✅ **Se liberaron hoy** (venció el elenco del 22/08, usables desde el 30/08): B-11/B-31/B-33, B-3, B-10/B-19, B-27, B-23, F-1, B-26, B-37, B-29, F-9.
- **Elenco LIBRE para el sábado 30/08:** pindó B-8, pata de vaca B-42, anacahuita B-16, evónimo B-44, mandioca B-34, madreselva B-40, aguaribay F-8, vivero B-46, cinta B-12, esparraguera B-6, coronita F-5, fresno F-10, mandarina B-24, lapachillo B-14, viraró B-32, fotinia F-3, hibisco… (no: B-4 quemado), I-1, I-2, B-13, B-20, B-2, B-45, B-47, B-48, B-49.
- **No repetir antes del 07/09:** «florece en madera vieja → podar cuesta la flor» · el corte a rama lateral de ⅓ · la forma en A · el tope del 40 % · las dos paltas · «7 de 7 slots en silencio» · las 3 predicciones verificadas de los carozos.
- Re-push de una aprobada = contenido RENOVADO en la misma URL. ✅ `el-taller` el 23/08 · ✅ `jardin-hoy` hoy.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py` / `gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → **fin de agosto = AHORA, ya está en la lista de hoy** (agosto es mes de siembra de lechuga y de tomate a cubierto). **Caqui B-41 → ignorar hasta primavera: no se nombró hoy.**
- **30/07:** foto + caja de comentario en TODAS las tareas → mantenido en la reedición de hoy.
- **01-04/08:** «mándamela cuando esté lindo» · «¿qué más puedo podar? ¿y el neem?» · «recordame las podas si no llueve» — los tres ejecutados en su momento.
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**. *(El hallazgo de hoy sobre B-22/B-36 es de PODA, no de mudanza — y así se aclaró en la página.)*
- **MANDATO 24/07 (canal tarea):** UNA SOLA push de tareas, consolidada en `2026-07-24-jardin-hoy.html` (URL estable, se REEDITA en su lugar). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (24/08/2026)

- Push subscription `pix9`: **active**. Threads, `uploads.json` y `user_tasks.json`: **0 pendientes** (lo último del usuario sigue siendo del 30/07).
- **Cero eventos nuevos en 7 días** — el último sigue siendo el dwell del 17/08 21:25Z. **Hoy es el primer día con exposición real desde la vuelta: la medición arranca de cero.**
- **12 tareas abiertas reales** (verificadas contra `generate_tasks_from_plants` + `task_states.json`), ordenadas hoy en 3 bloques: esta semana (B-43, B-9, B-18, F-2) · finde 29-30 (hortensia con reloj, cerco, abelia, gardenia, huerta) · septiembre (B-4, B-1, B-15).
- Jardín en dormancia, **saliendo**. **30 días al equinoccio.** Helada posible hasta fin de agosto (ninguna a la vista).
- Compactación 24/08: `engagement.json` → se cerró el registro del viaje (05-23/08) en `daily_summary`; los 10 eventos del 16-17/08 siguen vivos (<14 días). `send_log` → 4 eventos, ninguno vencido. `queue.json` → reescrita con las 2 del día.

## TODO / próximos experimentos

- **MARTES 25 A VIERNES 28:** martes/miércoles/viernes son **mantenimiento puro, 0 push**. **Jueves 27: slot de tarea 10:00** — y es el día de lluvia, así que el contenido honesto es «hoy no se poda» + lo que sí se puede hacer bajo techo; **re-verificar los 8,2 mm el 26**.
- **LEER PRIMERO mañana:** `taller3-cuando` (¿ahora / febrero / mitad?), `taller3-paltas` (¿me delega la corrección?), `podas-vuelta` y `salida-vuelta`. **Los cuatro cambian el contenido del jueves.**
  - Si `taller3-paltas` = «corregila» → **editar `prune_when` de B-22 y B-36 en `data_plants.py` + `python build.py`** (y recién ahí queda saldado el pendiente equivalente de B-7 del 22/08).
  - Si `salida-vuelta` = un día concreto → el jueves se arma **solo** con lo que entra en esa salida.
- **SÁBADO 30/08:** tarea 10:00 + experiencia 11:00. La original nueva **debe agrupar `el-taller` (aprobada) y, si el n°3 se aprueba, también el n°3**. Elenco: el liberado arriba.
- **Hortensia B-5a/b: 29-30/08, la única con reloj.** Si el finde pasa sin señal, es la primera candidata a landing propia.
- **Cantera sin usar:** el bucle poda→FRUTA (dic-ene) · dependencia de un solo ejemplar (44/52) · luz real vs ficha · coronita F-5 y romero B-26 del audit.
- **Medir la quickbar**: sigue sin un solo evento `via:"quickbar"`.
- **Idea del 16/08 pendiente:** el usuario llega a las experiencias por `ideas.html`. Ordenar ahí las buenas y retirar las de la era gimmick.
