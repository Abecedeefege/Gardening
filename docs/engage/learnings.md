# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🚨 LO PRIMERO DEL 02/09 — NOVENO DÍA SIN UNA SOLA SEÑAL, Y SIGUE SIN SER VEREDICTO

Último evento del canal: **24/08 22:10Z**. Nueve días en cero. En el medio salieron las **dos** push del
31/08, confirmadas **201** (`jardin-hoy` + `censo-de-primavera`), y **ninguna se abrió** (~59 h).
**Nada de esto se archiva como rechazo** — hay tres confusores encadenados:

1. **La ventana 25–30/08 fue silencio PEDIDO por él** («no me mandes más cosas hasta la semana que viene»).
   Cumplida entera: 3 de 3 slots reales caídos.
2. **El 31 era su día de vuelta al país.** Escribió «vuelvo la semana que viene» — **nunca dijo el día**.
3. **⚠️ ENTREGA TARDÍA.** `jardin-hoy` vencía 13:00Z y salió **17:23Z (+4 h 23 min)**: el slot de las
   **10:00 aterrizó 14:23 local**. El censo, +59 min. El día entero le llegó corrido.

**El `send_at` NO es la hora de entrega. Medir SIEMPRE `sent_at − send_at`.** Corregido en
`push-dispatch.yml`: cron de `*/15` → **`7,22,37,52`** (GitHub difiere los cron encolados en minutos
redondos; nuestros 3 slots estaban los tres en `:00`). **El jueves 3 es la primera medición del arreglo.**

- La hipótesis del censo queda **SIN MEDIR, no refutada**. Ventana hasta el **07/09**: si el jue 3 o el
  sáb 5 aparece señal, se re-mide. **Si el 07/09 sigue en cero, ahí sí se cierra el eje.**
- Sus **ángulos** (B-39 pera Williams como punto sur · B-32 viraró como trampa de observación · el inverso
  de la aserción del 2/08) son **reutilizables después del 07/09 sin ser refritos: él nunca los vio.**
  El **elenco**, en cambio, cuenta como quemado igual — el envío se gastó.
- **Verificado hoy:** `task_states.json` no cambia desde el **08/08** → el silencio es total, también fuera
  del canal push. No está tocando el sitio por su cuenta.

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

| Día | Tarea 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Una sola push por slot de experiencia:** original NUEVA (el experimento) + las **aprobadas** de ese slot
  agrupadas DENTRO. **Aprobación = recurrencia:** sólo vuelve lo que prendió (😍 / slot «sí» /
  `engageApprove`); pending no se borra, no recurre. **Única aprobada: `el-taller` (n°1), en los dos slots.**
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + slots (`<slug>-slot-lun18` /
  `<slug>-slot-sab11`) + caja propia (`id=engage-feedback-box`) + aprobar/rechazar + pitch de 6 modelos.
  `send_at` ≥60 min post-corrida, `expires_at` 22:00, timestamps `-03:00`.
- **Canal tarea:** UNA push consolidada en `2026-07-24-jardin-hoy.html` (URL estable, **se REEDITA en su
  lugar**). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 🚨 LAS DOS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
`el-parte` perdió con layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 % del scroll**, **medido
renderizado en Chromium 390×780** (nunca por offset de caracteres). Script en scratchpad (`audit.js`):
playwright en `/opt/node22/lib/node_modules`, `executablePath:
/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Filtrar por visibilidad real (`offsetParent`,
`display`, rect ≠ 0) y limitar a `.wrap`, o mide pasos ocultos del wizard y da 0 % falso. Todas compliant
(7,9–21,8 %) salvo **el-parte 27,3 % (compliant y perdió igual)** y **preguntas-abiertas 75 % (único caso
donde el layout SÍ explicó el resultado)**. · **Quickbar** (18/08): **sin un solo evento medido**
— buscar `via:"quickbar"`.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS (lo que el feedback dejó probado)

- **El canal funciona; el problema nunca fue la entrega… hasta que lo fue.** 5 envíos desde el 22/08, los 5
  con `201`. Pero el 31/08 midió por primera vez el **lag real** y era de horas. **Un 201 no es una lectura.**
- **La caja de feedback de texto es el control que más convierte de todo el sitio: 2 de 2 el 24/08.** Es la
  única señal ACTIVA que este sistema consiguió en todo agosto. Va en todas, siempre.
- **Las dos veces que escribió, escribió de LOGÍSTICA, no de contenido** («vuelvo en 1 semana, mandame todo
  lo que haya para hacer ese día» / «no me mandes más hasta la semana que viene»). Los dos pedidos se
  cumplieron al pie. **Ninguno es veredicto sobre el Taller n°3 ni sobre el censo.**
- **Lección más cara de agosto:** mandé una guía para ejecutar **con la tijera en la mano** a alguien que
  estaba fuera del país, y tuvo que pedirme por escrito que parara. **Antes de armar contenido de ejecución,
  chequear si hay señal de que esté físicamente en el jardín.**
- **Dwell alto sin conversión ≠ éxito.** taller-3: 100 s al pie, cero veredicto. `el-taller-2`: 7/7 pasos,
  166 s, cero reacción. **Leer entero es «masomenos», no un sí.** Y **«no contestó» ≠ «no le interesa»**.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 dos veces**, feedback positivo y **ticks por árbol**
  horas después. n°2: 7/7 pasos, dwell 166 s, cero reacción. n°3 (24/08): leído entero, **sin veredicto**.
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre con
  la herramienta en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Métrica más valiosa: los ticks** (`taller-arbol-<code>`). ⚠️ **NO escriben `task_states.json`** — el
  archivo muestra los carozos `active`. **Para el usuario están hechos: nunca contradecirlo.** Verificar
  contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (shape `{"tasks": {...}}`, **descartando
  las 15 entries huérfanas** que ya no genera el build, o el conteo da mal).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó 75 s y puso NO a los dos slots + meh. Enterarse no es el
  valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes** · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) ·
  **mi-objetivo** (aspiración sin acción) · role-play verboso · countdown · app pasiva · editorial 3ª pers ·
  mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak
  · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (23/07) · **era gimmick**
  (feed falso, superpoderes): el 16/08 los abrió solo y rebotó en **9 s / 28 %**.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando no puede hacer, lo más cercano es **mostrarle lo que YA hizo
  dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **⭐ PEDIR LA OBSERVACIÓN EN VEZ DE AFIRMARLA (estrenado 31/08, SIN veredicto — no lo abrió).**
  `flowering` es un rango de catálogo, no un dato del jardín. **Declarar lo que NO sé suma.**
- **LA PREDICCIÓN / PROMESA VERIFICADA.** Cobrados: el viaje (7 slots, 24/08) y el silencio de la vuelta
  (3 slots, 31/08). **Los dos ya se usaron: no reciclarlos.** Candidata fresca: el rebrote de B-43 en
  septiembre-octubre (anotado en el Taller n°3).
- **EL PRECIO ANTES QUE LA TAREA (sin veredicto).** Decirle qué **pierde** por hacer lo que le pido, antes
  de pedírselo.
- **⚠️ EL NÚMERO SE VERIFICA SIEMPRE — SIETE CONSULTAS, SIETE DRIFTS (02/09).** El jueves 3 solo osciló
  **12,1 → 4,4 → 12,7 mm** en tres consultas seguidas; antes la lluvia saltó del 27 al 3-6, al día 2 y de
  vuelta al 3. **El número que publico hoy es falso mañana.** Todo dato numérico se re-consulta la mañana
  que sale, **por WebFetch** (`curl` a api.open-meteo.com NO sale de este runner). *Jugada que sale de esto:
  contarle que la serie se movió siete veces y darle sólo lo que aguantó las siete.*
- **⚠️ UN ÁNGULO ANOTADO NO ES UN ÁNGULO VALIDADO (28/08).** «Luz real vs ficha» estaba anotado como
  prometedor y computado resultó **falso**. Computar antes de creerle a la cantera.
- **⚠️ EL CAMINO PROPIO TAMBIÉN SE CURA (29/08).** El 16/08 entró **solo** a `ideas.html` y rebotó en 9 s
  porque la grilla lo mandó a lo más flojo. **Cada vez que algo gane señal medida, reflejarlo en
  `featured_experiences` de `build.py`**, no sólo en la próxima push.
- **La contradicción interna del catálogo es una mina — minada entera** (`audit_flor_poda.json`).
  Publicadas: B-7 (22/08) y las paltas B-22/B-36 (24/08). **Sin publicar: coronita F-5 y romero B-26.**
- **El título es el activo más medido:** sustantivo concreto + número + algo que le pertenece + pérdida. ·
  **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. · **Timing verificado > urgencia
  inventada.** · **«Hoy no hay nada que hacer», cuando es verdad, ES contenido.** · **Minimalismo + REAL +
  VISUAL:** fotos reales = need validado, diagrama propio > párrafo. · **feedback_text = ley:** positivo =
  expandir; negativo = nunca vuelve; pedido = ejecutar ya; abrir sin señal activa = «masomenos», no éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Una decisión en learnings NO anula el ledger.**
  **Excepción:** el canal tarea (jardin-hoy / taller) es monotemático — su cast lo define la TAREA.
- ⚠️ **QUEMADOS HASTA EL 07/09** (elenco del censo + canal tarea del 31, se haya leído o no): F-4, B-30/B-35,
  B-38, B-39, B-32, B-13, B-10/B-19, B-26, B-23, B-24 · F-7, B-7, B-5a, B-9, B-18, F-2, B-43, B-25, B-15,
  B-4, B-1.
- ✅ **LIBRES para el jueves 3 y el sábado 5:** B-3, B-27, F-1, B-37, B-29, F-9, B-8, B-42, B-16, B-44,
  B-34, B-40, F-8, B-46, B-12, B-6, F-5, F-10, B-14, F-3, I-1, I-2, B-20, B-2, B-45, B-47, B-48, B-49,
  B-41, B-21, B-28, B-11, B-31, B-33, B-17.
- **No repetir antes del 07/09:** «florece en madera vieja → podar cuesta la flor» · el corte a rama lateral
  de ⅓ · la forma en A · el tope del 40 % · las dos paltas · «7 de 7 slots» y «3 de 3 slots» ·
  las 3 predicciones de los carozos.
- ⚠️ **DISTINCIÓN FINA:** la **aserción** «la poda del 2/08 dio flor en agosto, predicción verificada»
  (usada 15/08, re-editada 23/08) sigue quemada hasta el **06/09**. Lo publicado el 31 es su **inverso**
  (no decirle cómo salió y pedirle que vaya a mirarlo) — y **no lo leyó**, así que el inverso sigue fresco.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner:
  `pip install Pillow`** antes de tocar `build.py` / `gen_*.py`. · **23/07:** `tareas-pendientes.html` =
  página fija, no borrar, no pushear suelta. · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07:** lechuga/huerta → entregado el 31 como bloque de septiembre. **Caqui B-41 → ignorar hasta
  primavera** (septiembre ya es primavera: se puede entrar, suave). · **PALTA:** los plantines siguen contra
  la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA).
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (02/09/2026)

- Push subscription `pix9`: **active**. Threads, `uploads.json`, `user_tasks.json`: **0 pendientes**.
  `engagement.json`: **8 eventos, cero señal nueva desde el 24/08 22:10Z (noveno día)**. Proposals: **90**
  — 54 dropped / 23 promoted / **11 pending** / 1 approved (`el-taller`) / 1 removed.
- **51 tareas `active`** de 100 (46 done, 3 snoozed) — **verificado hoy** contra
  `generate_tasks_from_plants`. ⚠️ `active` ≠ «no lo hizo».
- **17 activas vencen en septiembre.** En **elenco LIBRE** (usables el jueves): **vivero B-46-3 / B-46-5 /
  B-46-7** (trasplantar los listos · decidir destino de las paltas · liquidámbares a sol pleno) ·
  **palmeras B-47-3 / B-47-4** · **B-29 lantana** (poda severa) · **B-12 cinta** (dividir matas) ·
  **fotinias F-3 / F-3-2** · **B-20** (foto al brotar). ⚠️ **B-22, B-23, B-24, B-36-2, B-1, B-32, B-13-2
  también vencen en septiembre pero están QUEMADAS hasta el 07/09** — no como protagonistas.
- **Compactación: NO vence.** `engagement` 8 eventos (los del 24/08 cumplen 15 días el **08/09**),
  `send_log` 5 eventos (el del 22/08 vence el **06/09**), `queue.json` en 0 entries.
- **Clima (7ª consulta, hoy):** mié 2 0,0 mm / **máx 17,6°** · **jue 3 → 12,7 mm** (máx 15,6) · vie 4 0,0
  (máx 11,8) · **sáb 5 → 6,5 mm** (máx 12,1) · dom 6 → 1,7 (**máx 8,3°**) · lun 7 0,0 (**mín 6,1°**).
  **Lo único que aguantó las 7 consultas es el golpe de frío del 6-7**: de 17,6° hoy a 8,3° el domingo,
  sobre brote tierno recién empujado por el calor de hoy. Eso es lo publicable; los mm, no.

## TODO / próximos experimentos

- **JUE 3 (tarea 10:00):** `jardin-hoy` reeditado en su URL. **⭐ El ángulo ya está: llueve 12,7 mm ese
  mismo día, y eso PARTE la lista de septiembre en dos** — tierra mojada = la mejor condición para
  **trasplantar el vivero (B-46-3, B-47-4)** y **dividir matas (B-12)**; y la PEOR para **podar cítricos**
  (herida abierta + follaje mojado = vía de entrada). No es urgencia inventada: es la lista de siempre
  reordenada por un dato verificable. **Re-consultar el número esa mañana (van 7 de 7 drifts)** y **medir
  `sent_at − send_at`: es el test del cron corregido.**
- **SÁB 5 (tarea 10:00 + experiencia 11:00):** la original nueva sale sí o sí. Si el censo sigue sin una
  apertura, **no insistir con recorridos de observación**: volver a la forma que SÍ ganó (El Taller,
  ejecutar con la herramienta en la mano) sobre el **vivero B-46/B-47**, tarea real de septiembre y libre de
  veto. Ángulo de respaldo: el golpe de frío del 6-7 sobre brote tierno.
- **`podas-vuelta` re-preguntada por 2ª y ÚLTIMA vez.** Sin respuesta → asumir «ninguna» y cerrar el tema
  para siempre. Acumular preguntas viejas es la queja de «cargado».
- **`taller3-paltas` se reactiva en la 2ª semana de septiembre**, cuando la tarea entra por calendario.
  Si contesta «corregila» → editar `prune_when` de B-22/B-36 en `data_plants.py` + `build.py`.
- **Si el censo gana señal → sumarlo a `featured_experiences` en `build.py`** (regla viva del 29/08).
- **Cantera SIN USAR:** «abre flor en septiembre» × «poda pendiente en septiembre» (B-22, B-36, B-23, B-24),
  desbloqueado desde el 07/09 · poda×fruta = feb y may-sep (B-24, B-41, B-8, F-8; ⚠️ B-23 NO: figura con
  fruta 12 meses, es simplificación de ficha) · **44 de 52 sin repuesto** (para esquejes de septiembre,
  nunca como título alarmista) · coronita F-5 y romero B-26 del audit.
