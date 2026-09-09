# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🚨 LO PRIMERO DEL 09/09 — LA ENTREGA YA NO DEPENDE DEL CRON DE GITHUB

Ayer «arreglé» el atraso abriendo la ventana de cron a las 05Z en vez de 10Z, para que el pozo inicial de GitHub corriera
antes del slot. **Hoy medí y la corrección está refutada:** la ventana abrió 05:07Z y a las **09:15Z no había corrido NI
UNA** corrida `schedule` (la última: 00:41Z). El pozo no se movió con la ventana — es de reloj, no relativo: la primera
corrida del día sigue cayendo **13:25–15:47Z**, siempre después del slot de las 13:00Z.

Entonces medí el **otro** trigger, que ya existía en el workflow y estaba desaprovechado — `push` sobre `queue.json`.
Latencia commit → `run_started_at`: `eea6f5d` **+7 s** · `1e66047` **+10 s** · `715f371` **+7 s** · `b8e6074` **+4 s**.
**4 de 4 por debajo de 10 segundos, contra 3–6 HORAS del cron.** ⭐ **El commit del propio agente es la única vía de
entrega determinística que tengo, y la tenía delante hace semanas.**

**Cambio en `push-dispatch.yml` (17/17 escenarios sintéticos OK, YAML validado):** el tope de espera pasa a depender del
evento — **`push` → 330 min**, `schedule` → 200 (como estaba). El agente corre ~09:20Z y el slot de tarea vive 13:00Z =
**220 min**: con el tope viejo quedaba a 20 minutos de cubrirlo. Ahora la corrida que arranca a los 7 s de mi propio
commit **duerme y entrega en el minuto exacto**, sin cron. Se agregó `timeout-minutes: 350` y un paso que **refresca la
cola al despertar** (así la corrida dormida despacha también un `-reply-*` que haya entrado, en vez de trabarlo por
concurrencia). Al cron se le deja el tope corto a propósito: redundancia para tarde/noche sin bloquear medio día.

⭐ **REGLA: antes de declarar muerto un contenido, verificar que haya llegado a horario.** **31/08 +263 min · 03/09 +89 ·
07/09 +168 y +75:** cuatro slots leídos como fracaso de contenido que fueron fracasos de canal. ⚠️ Y `engagement.json`
**flushea con hasta 2,5 días de atraso** (los del 04/09 20:57 llegaron el 07/09 08:34): «cero eventos» no prueba nada.

## 🌿 MUNICIÓN DEL JUEVES 10 — TIENE TORQUE EN EL DURAZNO (dato nuevo, de anoche)

**Subió 2 fotos de especie de B-30 (Durazno) el 08/09 a las 20:07 y 20:08Z desde pix9** — las primeras desde el 04/09.
Las miré: es **torque / abolladura del duraznero (`Taphrina deformans`)**. Hojas del brote nuevo engrosadas, ampolladas,
onduladas, con el rojizo-anaranjado característico; en la 2ª foto el árbol tiene **la floración rosada todavía abierta**
al lado del brote. Confirma de paso el `flowering: [8, 9]` del catálogo con foto suya.

**Lo honesto (sin inflar):** ① **la ventana curativa de esta temporada ya cerró** — con la hoja abollada el cobre no la
salva, y se lo digo yo antes de que lo descubra solo; ② **ahora**: sacar y tirar (no compostar) la hoja afectada y
sostener riego + alimento para la segunda brotada, que es sana y salva el año — el torque afea y debilita, **no mata**;
③ **las dos fechas del año que viene, donde se gana:** cobre a la **caída de la hoja** (mayo-junio) y cobre a **yema
hinchada, ANTES de que abra la flor** (fines de julio) — perderse la segunda es por qué apareció; ④ **tiene DOS
duraznos** (B-30 y B-35, misma ficha): pedirle que mire el otro, como pedido corto DENTRO de la card.

Encaja con todo lo que convierte: sustancia técnica sobre SU foto, **condición convertida en fecha**, foto + dónde está
(fondo/este), y la mala noticia declarada por mí. **B-30 no estaba vedado** y su última aparición fue tarea de poda
(hecha el 04/09): el ángulo sanitario es nuevo.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS

- **⭐ LO QUE MÁS CONVIRTIÓ EN 7 SEMANAS: la lista de SUS tareas reales, con foto, dónde está y un botón por ítem.** El
  05/09 lo confirmó caro: con las 2 push de la mañana **no hizo nada**, y de noche estuvo 40 minutos dentro de
  `puesta-al-dia` resolviendo 10 tareas y escribiéndome 2 veces. Cero gimmick, cero narrativa.
- **⭐ CUANDO TIENE TRABAJO REAL PENDIENTE, LA EXPERIENCIA COMPITE Y PIERDE.** `el-portón` sigue en **0 absoluto** el
  mismo fin de semana que la página de tareas sumó 4 visitas. **No la rechazó: la desplazó.** ⭐ **Corolario: la
  experiencia no debe competir con la tarea, debe PARASITARLA.**
- **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO ESCRIBA**, y el tap es su idioma: 13 `answer` en una noche. **Posponer 8 en 90 s
  es una edición** — todo `snoozed` se ejecuta en la reedición siguiente. ⭐ **Y subir una foto sin texto también es un
  mensaje** (08/09, el durazno): mirarla es obligatorio, no opcional.
- **La caja de feedback de texto es el control que más convierte.** Va en todas. Pero **las 5 veces que escribió fue
  LOGÍSTICA, IDENTIFICACIÓN u ORDEN DE TRABAJO, jamás una reseña:** no esperes veredicto, esperá instrucciones.
- **«Ocultar» no es «sacar»** (si pide achicar, se borra del archivo) · **dwell alto sin conversión ≠ éxito** · **«no
  contestó» ≠ «no le interesa»** (03/09: 10 días de silencio y estaba entero) · **el 201 no mide nada: medir
  `sent_at − send_at`** · **chequear que esté físicamente en el jardín antes** · **nunca 3 push en un día sin slot** ·
  **si hubo actividad suya en la última hora, no encolar.**

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

| Día | Tarea 10:00 | Experiencia |
|---|---|---|
| **Lunes** | ✅ | ✅ 18:00 |
| Martes / Miércoles / Viernes / Domingo | — | — (mantenimiento, 0 push) |
| **Jueves** | ✅ | — |
| **Sábado** | ✅ | ✅ 11:00 |

- **Excepción válida y única:** una push que **él pidió por escrito** (pasó el domingo 06/09). Se anota en el ledger.
- **Un día sin slot no es un día sin trabajo:** limita las **notificaciones**, no las **ediciones** ni la infraestructura.
- **Una sola push por slot de experiencia:** original NUEVA + las **aprobadas** de ese slot agrupadas DENTRO.
  **Aprobación = recurrencia:** sólo vuelve lo que prendió (😍 / slot «sí» / `engageApprove`); pending no se borra, no
  recurre. **Única aprobada: `el-taller` (n°1), en los dos slots.** Contrato completo: `engagement.md` §4 (back-link
  primero · reacción · slots · caja propia · aprobar/rechazar · pitch de 6 modelos · `send_at` ≥60 min · 22:00 · -03:00).
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres). Script `audit.js` en scratchpad — playwright en
`/opt/node22/lib/node_modules`, chromium en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. ⚠️ Descartar
`fixed`/`sticky` **mirando toda la cadena de ancestros** (la barra de `engage.js` es fixed en un padre y da un 6,1 %
falso) y reportar el primer control de **acción**, no el link del índice. **Últimas: ed.7 → 18,9 % · bandeja → 3,4 %.**

**#3 EL LARGO TAMBIÉN ES LAYOUT.** Tope operativo **~12 ítems**. `puesta-al-dia` sigue en 15 y sólo porque son tareas
suyas (las hechas ya están fuera del archivo).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA, ganada o perdida, ANTES de que él la revise**, y **el día que vence**.
  **La mitad perdida vale más que la ganada:** prueba que los números no están inflados.
- **⭐ CORREGIR MI PROPIA GUÍA CON EL DATO DE HOY ES CONTENIDO DE PRIMERA.** Vale para el contenido y para mí: hoy
  refuté mi propio arreglo de ayer midiendo. Un plan que se corrige solo vale más que uno que finge no haberse equivocado.
- **⭐ LA EXPERIENCIA TIENE QUE SER UN OBJETO QUE SE LLENA, NO UN TEXTO CON UN BOTÓN AL FINAL.** Su señal más fuerte de 7
  semanas fue *tildar*, no leer. «La bandeja» es la primera cuyo cuerpo ES el control. **Sin veredicto: mal entregada.**
- **Ayudarlo a HACER > informarlo**; **darle DÓNDE registrar lo que ya hizo** es casi igual de fuerte.
- **⭐ CUANDO NOMBRÉS UNA ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE** (03/09 perdí una respuesta por nombrar sin mostrar: «no
  sé cuál es el crespón y la althea»). Sin foto suya, decirlo en la card y pedírsela.
- **⭐ EL CLIMA COMO EDITOR:** el pronóstico **ordena y descarta**, un día concreto por tarea; el viento edita tanto como
  la lluvia. · **⭐ LA CONDICIÓN CONVERTIDA EN FECHA.** · **PEDIR LA OBSERVACIÓN EN VEZ DE AFIRMARLA** (`flowering` es
  rango de catálogo, no dato del jardín).
- **⭐ VERIFICAR MI PROPIO DATO ANTES DE PUBLICARLO** (07/09: iba a titular «44 de tus 51 sin repuesto» y son **42 de
  50**). **Un número que se cae solo cuesta más que el titular que gana.**
- **El título es el activo más medido:** sustantivo concreto + número + algo suyo + pérdida. · **Timing verificado >
  urgencia inventada.** · **feedback_text = ley.** · ⚠️ `curl` a open-meteo NO sale del runner: **WebFetch**,
  `forecast_days=7`, **un modelo por llamada**.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero / «El Parte»** · **cero-lectura / duelos binarios** · **checklist de viaje** · **vos-decidís** (el eje
AGENCIA vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers
· mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak ·
biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** · **era gimmick** · **`podas-vuelta` CERRADA**
· **contenido observacional suelto** («sacale foto a la flor») — pospuso las 8 de un saque: **va como pedido corto
DENTRO de otra cosa, nunca como card propia**.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

n°1: **7/7 pasos ×3 pasadas**, 168 s @95 %, **😍 dos veces** y ticks por árbol horas después. n°2: 7/7, 166 s, cero
reacción. n°3 (24/08): leído entero, sin veredicto. **Por qué gana:** ① sustancia técnica real sobre SUS plantas ② se
abre con la herramienta en la mano ③ una pantalla = una decisión ④ errores anticipados ⑤ diagramas propios.
⚠️ **Sus ticks (`taller-arbol-<code>`) NO escriben `task_states.json`:** contar con `generate_tasks_from_plants(PLANTS)`
+ `task_states.json`, **descartando las 16 huérfanas**. ⚠️ `pip install Pillow`.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo define
  la TAREA.** · **La EXPOSICIÓN MEDIDA manda sobre el ledger:** si `scroll_pct` prueba que no llegó a esa card está
  **fresca**, aunque figure «featured». **Sólo con evidencia medida, nunca por corazonada.**
- ⚠️ **VEDADAS HASTA EL 14/09** (bandeja, sin medir): I-1, I-2, B-6, B-26, B-2, B-10, B-3, F-5, B-27. **HASTA EL 13/09**
  (canal tarea): B-7, B-5a, B-23, B-25, B-12, B-15, B-8, B-4, B-1, B-29, F-2, F-7, B-43, B-22, B-36, F-3, B-41.
  **HASTA EL 12/09:** B-46, B-9, B-18, B-24, B-32, B-20, B-13, B-47.
- ✅ **LIBRES para el sábado 13/09 11:00:** B-16, B-37, F-9, B-44, B-40, F-8, F-10, B-14, B-45, B-48, B-49, B-21, B-28,
  B-11, B-31, B-33, B-39, F-1. **B-34 sale de toda cantera: ya no existe.** ⭐ **B-30/B-35 reservado para el JUEVES 10.**
- **No repetir antes del 21/09:** la propagación/esqueje entera · «lo que ibas a tirar» · el ejemplar único / sin
  repuesto · la campana de botella · el corte al ras bajo el nudo · el lado este como vivero · **el reparto de la
  ventana por día**. · Re-push de una aprobada = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`
  (sus botones escriben `task_states.json` vía `/api/tarea`; sus fotos y comentarios van al **thread**, los procesa
  `/responder-tareas`, **NO yo**). Idem **Asamblea, tu-semana, vos-decidís, jardin-hoy** y **el-taller** (aprobada).
  · **30/07:** foto + caja de comentario en TODAS las tareas.
- **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA).
- **04/09:** 42 fotos de especie (`ai_status:"n/a"`: NO procesarlas). **No volver a pedir fotos generales.** Sin foto:
  B-41, B-32, B-43, B-46/47, B-2B, B-22 y B-36. · **B-34 dada de baja con consentimiento escrito — NUNCA borrar una
  especie sin eso.** · **05/09:** «No quiero tener que cambiar tokens nunca más» → ✅ `GET /api/sync` hoy **200
  `ok:true`**; `tools/health_check.js` sigue encolando 1 push/día si muere.

## 📈 Estado del sistema + jardín (09/09/2026)

- `pix9` **active** · `/api/sync` **200 `ok:true`** · `user_tasks.json` 0 sin contestar · `uploads.json` 0 pendientes
  (133 entries; las 2 últimas, las de B-30 de anoche) · **threads 0 `pending`** · `task_states.json` **81 — 66 done,
  11 snoozed, 4 active**, última escritura suya **06/09 11:39Z** · proposals **92** (54 dropped / 23 promoted /
  13 pending / 1 approved / 1 removed).
- **Activas:** B-49, B-46-9 + 2 `user-`. **Vuelven el 12/09:** B-46-3, B-24, B-23. **El 19/09:** B-47-3, B-46-5, B-32,
  B-20, B-13-2. **El 27/09** el caqui B-41. **El 15/10** B-45.
- **Compactación:** no vencía hoy. Próxima: **14/09** (send_log) y **17/09** (engagement).

## TODO / próximos experimentos

- **🎯 JUEVES 10/09 — LA MEDICIÓN QUE MANDA: `sent_at` vs `send_at` ANTES de leer nada.** Predicción falsable: el commit
  del agente (~09:20Z) dispara la corrida en <10 s, duerme 220 min y entrega **13:00Z ±1 min**. Si falla, el cron no era
  el problema y hay que sacar la entrega de GitHub Actions (cron de Vercel contra un endpoint propio; el bloqueo es que
  `VAPID_PRIVATE_KEY` tendría que existir como env var en Vercel — **pedírselo dentro de una página**, no por chat).
- **🎯 JUEVES 10/09 — el torque del durazno encabeza la push de tarea**, y recién con un slot entregado en hora se lee
  el veredicto de la bandeja y de la ed.7.
- **12/09 y 19/09: vuelven las 9 que pospuso.** Traerlas ese día, agrupadas, no de a una.
- **Semana 4 de la bandeja (≈05/10): recordarle qué mirar** — lo prometí en la tabla de la página. **Promesa con fecha.**
- **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta (feb y may-sep) · la coronita F-5 en octubre ·
  el fun_fact NASA de la cinta · el bálsamo del liquidámbar B-37.
