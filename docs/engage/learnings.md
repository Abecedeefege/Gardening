# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🚨 LO PRIMERO DEL 03/09 — DÉCIMO DÍA SIN SEÑAL, Y HOY SE MIDE EL ARREGLO

Último evento del canal: **24/08 22:10Z**. Diez días en cero. En el medio salieron las **dos** push del
31/08, confirmadas **201**, y **ninguna se abrió** (>72 h). **Sigue sin ser veredicto** — tres confusores:

1. **La ventana 25–30/08 fue silencio PEDIDO por él** («no me mandes más cosas hasta la semana que viene»).
   Cumplida entera: 3 de 3 slots caídos.
2. **El 31 era su día de vuelta al país** — escribió «vuelvo la semana que viene», **nunca dijo el día**.
3. **⚠️ ENTREGA TARDÍA.** `jardin-hoy` vencía 13:00Z y salió **17:23Z (+4 h 23 min)**: el slot de las
   10:00 aterrizó 14:23 local. El censo, +59 min. **Un 201 no es una lectura. Medir SIEMPRE
   `sent_at − send_at`.** Corregido en `push-dispatch.yml`: cron `*/15` → **`7,22,37,52`** (GitHub difiere
   los cron en minutos redondos y nuestros 3 slots estaban los tres en `:00`).

- **⏱️ TAREA #1 DE LA PRÓXIMA CORRIDA: calcular `sent_at − send_at` de `2026-09-03-jardin-hoy`
  (send_at 13:00Z) en `send_log.json`. Es la PRIMERA medición del cron corregido.** Si el lag sigue en
  horas, el problema no era el cron: mirar el workflow entero antes de tocar contenido.
- Hipótesis del censo: **SIN MEDIR, no refutada.** Ventana hasta el **07/09** (sigue linkeada desde
  jardin-hoy con la nota «no vence»). **Si el 07/09 sigue en cero, ahí sí se cierra el eje.**
- Sus **ángulos** (B-39 pera Williams punto sur · B-32 viraró trampa de observación · el inverso de la
  aserción del 2/08) son **reutilizables después del 07/09 sin ser refritos: él nunca los vio.** El
  **elenco**, en cambio, cuenta como quemado igual — el envío se gastó.
- **`task_states.json` no cambia desde el 08/08** → el silencio es total, también fuera del canal push.

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
`display`, rect ≠ 0) y limitar a `.wrap`. Todas compliant (7,9–21,8 %; **jardin-hoy ed. 03/09 = 17,9 %**)
salvo **el-parte 27,3 % (compliant y perdió igual)** y **preguntas-abiertas 75 % (único caso donde el
layout SÍ explicó el resultado)**. · **Quickbar** (18/08): **sin un evento medido** — buscar `via:"quickbar"`.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS

- **El canal funciona; el problema nunca fue la entrega… hasta que lo fue.** 5 envíos desde el 22/08, los 5
  con `201`; el 31/08 midió por primera vez el **lag real** y era de horas.
- **La caja de feedback de texto es el control que más convierte del sitio: 2 de 2 el 24/08.** Única señal
  ACTIVA de todo agosto. Va en todas, siempre.
- **Las dos veces que escribió, escribió de LOGÍSTICA, no de contenido.** Los dos pedidos se cumplieron al
  pie. **Ninguno es veredicto sobre el Taller n°3 ni sobre el censo.**
- **Lección más cara de agosto:** mandé una guía para ejecutar **con la tijera en la mano** a alguien que
  estaba fuera del país, y tuvo que pedirme por escrito que parara. **Antes de contenido de ejecución,
  chequear si hay señal de que esté físicamente en el jardín.**
- **Dwell alto sin conversión ≠ éxito.** taller-3: 100 s al pie, cero veredicto. **Leer entero es
  «masomenos», no un sí.** Y **«no contestó» ≠ «no le interesa»**.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

- n°1: **7/7 pasos ×3 pasadas**, dwell 168 s @95 %, **😍 dos veces**, feedback positivo y **ticks por árbol**
  horas después. n°2: 7/7 pasos, 166 s, cero reacción. n°3 (24/08): leído entero, sin veredicto.
- **Por qué gana (replicar esto, no la estética):** ① sustancia técnica real sobre SUS plantas ② se abre con
  la herramienta en la mano ③ una pantalla = una decisión ④ los errores anticipados ⑤ diagramas propios.
- **Métrica más valiosa: los ticks** (`taller-arbol-<code>`). ⚠️ **NO escriben `task_states.json`** — el
  archivo muestra los carozos `active`. **Para el usuario están hechos: nunca contradecirlo.** Verificar
  contra `generate_tasks_from_plants(PLANTS)` + `task_states.json` (shape `{"tasks": {...}}`, **descartando
  las huérfanas** que ya no genera el build). ⚠️ **`pip install Pillow` primero.**

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero / diario / «El Parte»** (31/07: 75 s, NO a los dos slots, meh — enterarse no es el valor,
ayudarlo a HACER sí) · **cero-lectura / duelos binarios** (28/07: «No es mi tipo») · **checklist de viaje
como deberes** · **vos-decidís** (el eje AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play
verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial *(como formato entero; un plano chico
DENTRO de otra cosa sí sirve)* · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol ·
**mucho texto/cargado** (23/07) · **era gimmick** (feed falso, superpoderes): 16/08, **9 s / 28 %**.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Ayudarlo a HACER > informarlo.** Cuando no puede hacer, lo más cercano es **mostrarle lo que YA hizo
  dando resultado**, o **hacerlo DECIDIR con un tap que produce trabajo mío, no suyo**.
- **⭐ EL CLIMA COMO EDITOR, estrenado 03/09 (sin veredicto).** No «hay 17 tareas»: **el pronóstico ORDENA la
  lista y descarta lo que hoy sale peor**. Corolarios: **«hoy no salís» es contenido** si le doy la que SÍ
  se puede hacer (la cinta B-12 se divide adentro un día de lluvia); y **la lluvia como recurso, no como
  estorbo** (el balde bajo la bajada del techo es literalmente lo que la ficha de esa planta pide).
- **⭐ PEDIR LA OBSERVACIÓN EN VEZ DE AFIRMARLA (31/08, sin veredicto).** `flowering` es un rango de
  catálogo, no un dato del jardín. **Declarar lo que NO sé suma.**
- **LA PREDICCIÓN / PROMESA VERIFICADA.** Cobrados: el viaje (7 slots, 24/08) y el silencio de la vuelta
  (3 slots, 31/08). **Los dos ya se usaron.** Candidata fresca: el rebrote de B-43 en septiembre-octubre.
- **⚠️ EL NÚMERO SE VERIFICA SIEMPRE — OCHO CONSULTAS (03/09).** El jueves osciló 12,1 → 4,4 → **12,7 →
  12,7**: la 8ª es **la primera repetición consecutiva de la serie**. Sábado y domingo volvieron a driftear
  (6,5→2,9 · 1,7→1,0) y **por eso no se publicaron**. Lo único que aguantó las 8 es el **golpe de frío del
  domingo 6 (máx 8,3°)**. ⚠️ `curl` a api.open-meteo.com NO sale del runner: **usar WebFetch**.
  **⭐ Publicar la volatilidad como bloque de honestidad ES contenido** — estrenado 03/09, medir.
- **⚠️ UN ÁNGULO ANOTADO NO ES UN ÁNGULO VALIDADO (28/08).** «Luz real vs ficha» resultó **falso** al
  computarlo. Computar antes de creerle a la cantera.
- **⚠️ EL CAMINO PROPIO TAMBIÉN SE CURA (29/08).** El 16/08 entró **solo** a `ideas.html` y rebotó en 9 s.
  **Lo que gane señal medida va a `featured_experiences` de `build.py`**, no sólo a la próxima push.
- **La contradicción interna del catálogo es una mina — minada entera** (`audit_flor_poda.json`).
  Publicadas: B-7 (22/08) y las paltas B-22/B-36 (24/08). **Sin publicar: coronita F-5 y romero B-26.**
- **El título es el activo más medido:** sustantivo concreto + número + algo suyo + pérdida. · **Contestar un
  pedido suyo < 12 h** es la forma más pura de la regla #1. · **Timing verificado > urgencia inventada.** ·
  **Minimalismo + REAL + VISUAL.** · **feedback_text = ley:** positivo = expandir; negativo = nunca vuelve;
  pedido = ejecutar ya; abrir sin señal activa = «masomenos», no éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Una decisión en learnings NO anula el ledger.**
  **Excepción:** el canal tarea (jardin-hoy / taller) es monotemático — su cast lo define la TAREA.
- ⚠️ **QUEMADOS HASTA EL 07/09:** F-4, B-30/B-35, B-38, B-39, B-32, B-13, B-10/B-19, B-26, B-23, B-24,
  F-7, B-7, B-5a, B-9, B-18, F-2, B-43, B-25, B-15, B-4, B-1.
- ⚠️ **QUEMADOS HOY 03/09, HASTA EL 10/09:** B-12/B-17, B-46, B-47, B-29, B-20.
- ✅ **LIBRES para el sábado 5 (29):** B-3, B-27, F-1, B-37, F-9, B-8, B-42, B-16, B-44, B-34, B-40, F-8,
  B-6, F-5, F-10, B-14, F-3, I-1, I-2, B-2, B-45, B-48, B-49, B-41, B-21, B-28, B-11, B-31, B-33.
- **No repetir antes del 10/09:** «la lluvia parte la lista en dos» · el punto de trasplante 24-48 h
  post-lluvia · el balde de agua de lluvia · «arrimar la hilera para que se sostengan entre ellas» ·
  «florece en madera nueva → cortar fuerte suma flor» · el bloque de honestidad de las 8 consultas.
- **No repetir antes del 07/09:** el corte a rama lateral de ⅓ · la forma en A · el tope del 40 % · las dos
  paltas · «7 de 7 slots» y «3 de 3 slots» · las 3 predicciones de los carozos.
- ⚠️ La **aserción** «la poda del 2/08 dio flor en agosto, predicción verificada» sigue quemada hasta el
  **06/09**. Su **inverso** (publicado el 31) **no lo leyó**: sigue fresco. · Re-push de una aprobada =
  contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. · **23/07:** `tareas-pendientes.html` = página fija,
  no borrar, no pushear suelta. · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07:** lechuga/huerta → entregado el 31 como bloque de septiembre. **Caqui B-41 → ignorar hasta
  primavera** (septiembre ya es primavera: se puede entrar, suave). · **PALTA:** los plantines siguen contra
  la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA). *Reafirmado explícitamente en la ed. 03/09.*
- **Asamblea, tu-semana, vos-decidís, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.
- **NUNCA borrar una especie del sitio sin consentimiento explícito.**

## 📈 Estado del sistema + jardín (03/09/2026)

- Push subscription `pix9`: **active**. Threads, `uploads.json`, `user_tasks.json`: **0 pendientes**.
  `engagement.json`: **8 eventos, cero señal nueva desde el 24/08 22:10Z (décimo día)**. Proposals: **90**
  — 54 dropped / 23 promoted / **11 pending** / 1 approved (`el-taller`) / 1 removed.
- **51 tareas `active`** de 100 (46 done, 3 snoozed), reverificado hoy. ⚠️ `active` ≠ «no lo hizo».
- **17 activas vencen en septiembre.** Las de elenco libre se gastaron hoy (vivero, palmeras, lantana, cinta,
  B-20). **Para el sábado quedan:** F-3/F-3-2 fotinias del cerco (⚠️ vedadas hasta el 07/09 por el canal
  tarea del 31 — chequear antes de usarlas de protagonistas) y la cantera del `audit_flor_poda`.
- **Compactación: NO vence.** `engagement` 8 eventos (los del 24/08 cumplen 14 días el **07/09**),
  `send_log` 5 eventos (el del 22/08 vence el **05/09**), `queue.json` con 1 entry del día.
- **Clima (8ª consulta, hoy):** jue 3 **12,7 mm** (máx 13,7 · viento 27) · vie 4 0,6 (máx 11,7 · **viento
  16,7 = el día calmo**) · sáb 5 2,9 (**viento 38,1**) · dom 6 1,0 (**máx 8,3** · viento 37,2) · lun 7 0,0
  (máx 10,9 · **viento 10,6 = el día limpio**). Publicados sólo los 12,7 y los 8,3.

## TODO / próximos experimentos

- **⏱️ PRIMERO: `sent_at − send_at` de `2026-09-03-jardin-hoy`.** Manda sobre todo lo demás.
- **SÁB 5 (tarea 10:00 + experiencia 11:00):** la original nueva sale sí o sí. ⚠️ **No repetir vivero ni
  palmeras.** Si el censo sigue sin apertura, **no insistir con recorridos de observación**: volver a la
  forma que SÍ ganó (El Taller, con la herramienta en la mano). Ángulo de respaldo: **el después del golpe
  de frío** — el domingo cae a 8,3° sobre brote tierno y el lunes 7 es el único día limpio; un Taller n°4
  armado para ese lunes tiene timing verificado. ⚠️ El viento de 38 km/h del sábado condiciona qué le puedo
  pedir ese mismo día.
- **`podas-vuelta` re-preguntada por 2ª y ÚLTIMA vez el 03/09**, con promesa explícita de cerrar el tema.
  Sin respuesta → **asumir «ninguna», sacarlo del catálogo de preguntas y no volver a nombrarlo.**
- **`taller3-paltas` se reactiva la 2ª semana de septiembre**, cuando la tarea entra por calendario. Si
  contesta «corregila» → editar `prune_when` de B-22/B-36 en `data_plants.py` + `build.py`.
- **Si el censo gana señal → sumarlo a `featured_experiences` en `build.py`** (regla viva del 29/08).
- **Cantera SIN USAR:** «abre flor en septiembre» × «poda pendiente en septiembre» (B-22, B-36, B-23, B-24),
  desbloqueado desde el 07/09 · poda×fruta = feb y may-sep (B-24, B-41, B-8, F-8; ⚠️ B-23 NO: fruta 12 meses
  es simplificación de ficha) · **44 de 52 sin repuesto** (esquejes de septiembre, nunca como título
  alarmista) · coronita F-5 y romero B-26 del audit · **el fun_fact NASA de la cinta (purifica aire
  interior) quedó SIN usar hoy a propósito — sigue fresco.**
