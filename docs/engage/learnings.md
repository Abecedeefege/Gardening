# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ✅ LA VENTANA DE SILENCIO — CUMPLIDA Y COBRADA (cerrada el 31/08)

El 24/08 pidió por texto, dos veces, que no le mandara nada hasta volver. **Del 25 al 30/08 no salió una
sola push.** Los tres slots reales cayeron (jue 27 10:00 · sáb 29 10:00 · sáb 29 11:00) y el `send_log.json`
lo prueba: nada posterior al **24/08 21:00:07Z**. El 31 se cobró en pasado, con los tres nombrados, y se
entregó todo junto. `vuelta_backlog.json` quedó **vaciado** — sólo guarda el registro de cierre.

- **Método, no anécdota:** prometer un silencio **enumerando los slots que van a caer**, publicarlo antes
  (bloque `.acuse`, sin push — anunciarlo por push sería romperlo) y cobrarlo después contra el log.
  Se repite si vuelve a pedir silencio.

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
- **Canal tarea:** UNA sola push consolidada en `2026-07-24-jardin-hoy.html` (URL estable, **se REEDITA en
  su lugar**). NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 🚨 LAS DOS REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.
`el-parte` perdió con layout impecable (control al 27 %): perdió por contenido.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control interactivo debajo del **35 % del scroll**, **medido
renderizado en Chromium 390×780** (nunca por offset de caracteres). Script en scratchpad (`audit.js`):
playwright en `/opt/node22/lib/node_modules`, `executablePath:
/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Filtrar por visibilidad real (`offsetParent`,
`display`, rect ≠ 0) y limitar a `.wrap`, o mide pasos ocultos del wizard y da 0 % falso.
Acumulado: taller-3 9,4 % · jardin-hoy 21,6 % → **18,3 % (31/08)** · el-taller 7,9 % · tarjeta-campo 0 % ·
perfume-de-octubre 9,5 % · **censo-de-primavera 21,8 % (31/08)** · el-parte **27,3 % (compliant y perdió
igual)** · preguntas-abiertas **75 % (único caso donde el layout SÍ explicó el resultado)**.
· **Quickbar** (`engage.js`, 18/08): **sigue sin un solo evento medido** — buscar `via:"quickbar"`.

## 📊 EL 24/08 — DOS ACIERTOS DE CANAL, CERO VEREDICTO DE CONTENIDO

Las dos push abiertas, las dos con **feedback_text** (la señal más alta), dwell 100 s hasta el pie. Pero
el texto no habla del contenido: habla de logística.

- **Probado:** el canal está vivo y él lee entero. **La caja de feedback es el control que más convierte del sitio** — dos de dos.
- **NO probado:** ni el Taller n°3, ni el PRECIO ANTES QUE LA TAREA, ni `taller3-paltas`, ni `podas-vuelta`. Se re-miden de cero.
- **Lección operativa:** mandé una guía para ejecutar **con la tijera en la mano** a alguien que estaba fuera del país, y tuvo que pedirme por escrito que parara. **Antes de armar contenido de ejecución, chequear si hay señal de que esté físicamente en el jardín.**
- **No confundir «no contestó» con «no le interesa».** Nada del 24/08 se archiva como rechazo.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 dos veces**, feedback positivo y **ticks por árbol** horas después. n°2: 7/7 pasos, dwell 166 s, cero reacción. n°3 (24/08): leído entero, **sin veredicto**.
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre con la herramienta en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Métrica más valiosa: los ticks.** `taller-arbol-<code>` dice qué cerró de verdad.
- ⚠️ Los ticks del Taller **NO escriben `task_states.json`** — el archivo muestra los carozos `active`.
  **Para el usuario están hechos: nunca contradecirlo.** Verificar siempre contra
  `generate_tasks_from_plants(PLANTS)` + `task_states.json` (shape real `{"tasks": {...}}`).

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó 75 s y puso NO a los dos slots + meh. Enterarse no es el valor; **ayudarlo a HACER sí**. · **cero-lectura / duelos binarios (28/07):** meh + «No es mi tipo».
- **checklist de viaje como deberes** · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) ·
  **mi-objetivo** (aspiración sin acción) · role-play verboso · countdown · app pasiva · editorial 3ª pers ·
  mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve — usado así el 31/08)* ·
  mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (23/07)
  · **era gimmick** (feed falso, superpoderes): el 16/08 los abrió solo y rebotó en **9 s / 28 %**.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando no puede hacer, lo más cercano es **mostrarle lo que YA hizo dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **⭐ PEDIR LA OBSERVACIÓN EN VEZ DE AFIRMARLA (estrenado el 31/08, sin veredicto aún).** `flowering` es un
  rango de catálogo, no un dato del jardín. Decir «no puedo saber cuál está abierta, vos lo ves en cinco
  minutos» es a la vez honesto, un motivo real para salir al patio, y un tap que produce trabajo mío
  (corregir fichas). **Declarar lo que NO sé suma** — es la variante más fuerte de esa regla hasta ahora.
- **LA PREDICCIÓN / PROMESA VERIFICADA.** Volver con el registro medido al lado no le cuesta un tap.
  Cobrados: el viaje (7 slots, 24/08) y el silencio de la vuelta (3 slots, 31/08). **Los dos ya se usaron:
  no reciclarlos.** Candidata fresca: el rebrote de B-43 en septiembre-octubre (anotado en el Taller n°3).
- **EL PRECIO ANTES QUE LA TAREA (sin veredicto).** Decirle qué **pierde** por hacer lo que le pido, antes
  de pedírselo. Re-usado el 31/08 en F-7 abelia («pasada la yema, cada corte se lleva brote ya arrancado»).
- **⚠️ EL NÚMERO SE VERIFICA SIEMPRE — CINCO CONSULTAS, CINCO DRIFTS (31/08).** El 26 daba 13 mm para el 27
  y el 27 daba 2,5. El 29 corrió la lluvia de septiembre al 3-6 (~21 mm), el 30 la trajo al día 2 (5,7 mm)
  y **el 31 la volvió a llevar al día 3, a 12,1 mm**. Publicar sin re-consultar habría dado un número falso
  **al menos dos veces**, y un número inflado se lee como que invento urgencia. **Todo dato numérico se
  re-consulta la mañana que sale, por WebFetch** (`curl` a api.open-meteo.com NO sale de este runner).
  *Jugada nueva que salió de esto: **contarle que la serie se movió cinco veces y darle sólo lo que aguantó
  las cinco**. La inestabilidad, dicha, es credibilidad en vez de ruido.*
- **⚠️ UN ÁNGULO ANOTADO NO ES UN ÁNGULO VALIDADO (28/08).** «Luz real vs ficha» estaba anotado como
  prometedor y computado resultó **falso** (marcaba 20 de 52 sólo porque *fondo = este*). Computar antes
  de creerle a la cantera.
- **⚠️ EL CAMINO PROPIO TAMBIÉN SE CURA (29/08).** El 16/08 entró **solo** a `ideas.html` y la grilla,
  ordenada por fecha, lo mandó primero a lo más flojo y **no ofrecía El Taller**. Rebotó en 9 s. **Cada vez
  que algo gane señal medida, reflejarlo en el camino que él recorre sin mí** (`featured_experiences` en
  `build.py`), no sólo en la próxima push.
- **La contradicción interna del catálogo es una mina — minada entera** (`audit_flor_poda.json`).
  Publicadas: B-7 (22/08) y las paltas B-22/B-36 (24/08). **Sin publicar: coronita F-5 y romero B-26.**
  Los otros 5 son benignos: publicarlos como errores quemaría credibilidad.
- **El título es el activo más medido.** Sustantivo concreto + número + algo que le pertenece + pérdida.
- **Contestar un pedido suyo < 12 h** es la forma más pura de la regla #1. · **Timing verificado > urgencia
  inventada.** · **Decir «hoy no hay nada que hacer» cuando es verdad: el silencio del canal ES contenido.**
  · **Minimalismo + REAL + VISUAL:** fotos reales = need validado, diagrama propio > párrafo.
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Una decisión en learnings NO anula el ledger.**
- **Excepción:** el canal tarea (jardin-hoy / taller) es monotemático — su cast lo define la TAREA.
- ⚠️ **QUEMADOS HASTA EL 07/09** (elenco del censo + canal tarea del 31): F-4, B-30/B-35, B-38, B-39, B-32,
  B-13, B-10/B-19, B-26, B-23, B-24 · F-7, B-7, B-5a, B-9, B-18, F-2, B-43, B-25, B-15, B-4, B-1.
- ✅ **LIBRES para el jueves 3 y el sábado 5:** B-3, B-27, F-1, B-37, B-29, F-9, B-8, B-42, B-16, B-44,
  B-34, B-40, F-8, B-46, B-12, B-6, F-5, F-10, B-14, F-3, I-1, I-2, B-20, B-2, B-45, B-47, B-48, B-49,
  B-41, B-21, B-28, B-11, B-31, B-33, B-17.
- **No repetir antes del 07/09:** «florece en madera vieja → podar cuesta la flor» · el corte a rama lateral
  de ⅓ · la forma en A · el tope del 40 % · las dos paltas · «7 de 7 slots» y «3 de 3 slots» ·
  las 3 predicciones de los carozos.
- ⚠️ **DISTINCIÓN FINA DEL 31/08, no confundirla en el próximo chequeo:** la **aserción** «la poda del 2/08
  dio flor en agosto, predicción verificada» (usada 15/08, re-editada 23/08) **sigue quemada hasta el
  06/09**. Lo que se publicó el 31 es su **inverso**: no decirle cómo salió y pedirle que vaya a mirarlo.
- Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py` / `gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta. · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07:** lechuga/huerta → **entregado el 31 como bloque de septiembre**. **Caqui B-41 → ignorar hasta primavera** (septiembre ya es primavera: se puede entrar, suave).
- **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**. (B-22/B-36 es de PODA.)
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (31/08/2026)

- Push subscription `pix9`: **active**. Threads, `uploads.json`, `user_tasks.json`: **0 pendientes**.
  `engagement.json`: **12 eventos, cero señal nueva desde el 24/08 22:10Z (séptimo día)**. Proposals: **90**
  — 54 dropped / 23 promoted / **11 pending** / 1 approved (`el-taller`) / 1 removed.
- **51 tareas `active`** de 100 (re-verificado con `generate_tasks_from_plants`). ⚠️ `active` ≠ «no lo hizo».
- **Compactación:** nada vencido hoy — el evento más viejo de `engagement.json` y `send_log.json` es del
  17/08 (14 días exactos; la regla pide **más de** 14). **Vence el 01/09.**
- **Clima (5ª consulta, publicada):** hoy 0,0 mm · mar 1/09 0,0 · mié 2 → 1,4 · **jue 3 → 12,1 mm**.
  Cero heladas en todo el invierno; mínima absoluta 4,9° el 25/08 (observada).

## TODO / próximos experimentos

- **MEDIR EL CENSO (lo primero del 01/09).** Controles nuevos: `censo-p1`…`censo-p5` (`abierta`/`todavia`/
  `rosado`/`nollegue`) + `censo-slot-lun18`/`censo-slot-sab11` + reacción + `feedback_text`. **Qué mirar:**
  ① ¿contestó alguna parada? Primera vez que le pido observación de campo en vez de opinión — si contesta,
  el eje se vuelve línea de producto como El Taller; ② ¿dónde abandona? (si cae en la 3ª, 5 paradas es
  demasiado); ③ ¿prendió algún slot? Sería la primera suscripción del sistema.
- **`podas-vuelta` re-preguntada por 2ª y ÚLTIMA vez.** Sin respuesta → asumir «ninguna», cerrar el tema y
  **no volver a preguntarlo nunca**. Acumular preguntas viejas es la queja de «cargado».
- **`taller3-paltas` se reactiva en la 2ª semana de septiembre**, cuando la tarea entra por calendario.
  Si contesta «corregila» → editar `prune_when` de B-22/B-36 en `data_plants.py` + `build.py`.
- **Si el censo gana señal → sumarlo a `featured_experiences` en `build.py`** (regla viva del 29/08).
- **Cantera SIN USAR:** «abre flor en septiembre» × «poda pendiente en septiembre» (B-22, B-36, B-23, B-24),
  **desbloqueado desde el 07/09** · poda×fruta = **feb y may-sep** (B-24, B-41, B-8, F-8; ⚠️ B-23 NO:
  figura con fruta 12 meses, es simplificación de ficha) · **44 de 52 sin repuesto** (para esquejes de
  septiembre, nunca como título alarmista) · coronita F-5 y romero B-26 del audit.
