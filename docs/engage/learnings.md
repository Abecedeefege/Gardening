# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas). No es un log: es lo que necesito recordar para
decidir el contenido de mañana.

## 🏁 11/09 — SE CERRÓ LA INVESTIGACIÓN DEL CANAL. GANÓ LA HIPÓTESIS.

**`2026-09-10-jardin-hoy`: `send_at` 13:00:00Z → `sent_at` 13:00:03.575Z = +3,6 SEGUNDOS.**
Contra **+263 min** (31/08), **+89** (03/09), **+168 y +75** (07/09). La predicción falsable que dejé anteayer se
verificó **entera y en las dos mitades**: (a) trigger `push` sobre `queue.json` → `run_started_at` +8 s y la corrida
quedó `in_progress` **durmiendo** hasta el slot; (b) el envío salió puntual. El `WAIT_CAP_MIN` por evento
(`push` → 330, `schedule` → 200, `timeout-minutes: 350`) funciona.

⭐ **CONSECUENCIA QUE VALE MÁS QUE EL FIX: recién ahora las métricas de contenido significan algo.** Cinco slots
que leí como fracaso de contenido eran fracaso de canal. **`el-portón` y `la-bandeja` siguen sin refutarse** — nunca
llegaron a horario. La hipótesis del *objeto que se llena* está VIVA.

⭐ **REGLA (confirmada, no provisoria): antes de declarar muerto un contenido, verificar que haya llegado a horario.**
Medir `sent_at − send_at`, nunca el 201.

## 📌 LO DE HOY: LA PROMESA SE COBRA SIN PUSH — Y DESPUÉS ÉL PIDIÓ LA PUSH

Viernes sin slot, **dos ediciones de `jardin-hoy` sobre la misma URL estable**:

**06:10, sin push.** Ayer le dejé por escrito *«el viernes 11 está seco, 16°, sin ráfagas: es EL día de tijera»* y esa
promesa vencía **hoy**, el día que la cadencia me prohíbe notificar. Se cobró **dentro de la página**: **seco ✅**
(0,0 mm hora por hora) · **«16°» ❌** (máxima real **12,7°** — le vendí 3 grados de más) · **sin ráfagas ✅**.

**08:10, con push — porque la pidió por escrito:** *«mandame actualizado el push de tareas»*. Excepción válida y única
(la misma del 06/09). Volví a consultar y **el viento se corrió para atrás**: ráfagas 5‑16 km/h de 8 a 10h, 21‑24 de
10 a 14h, y el pico 30‑32 **recién 15‑17h**. O sea que a las 06:10 **le acorté la ventana de más**: no cierra a las
11, le llega **hasta las 14**. Fue el titular, por la regla de la corrección a su favor.

⭐ **REGLA NUEVA: una página de URL estable que dice «mañana» para algo que es HOY está mintiendo, y se arregla el
mismo día aunque no haya slot.** Un día sin slot limita las **notificaciones**, no las **ediciones**.
⭐ **Una reedición SIN push no consume elenco; CON push sí**, aunque sea el mismo archivo. Lo que quema es la exposición.
⭐ **`expires_at` se ata a la ventana del contenido, no al 22:00 de rutina** (hoy 17:00: prometer a la noche una
ventana que cerró a las 14 quema justo el activo que la hace valer).
⭐ **7ª vez que escribe en 9 semanas, y la 1ª que pide un re-envío de tareas sin que se lo ofrezca.** El canal tarea es
el único que le genera pedidos espontáneos.

## 📊 CONCLUSIONES ACUMULADAS DE LOS PUSH ENVIADOS

- **⭐ LO QUE MÁS CONVIRTIÓ EN 9 SEMANAS: la lista de SUS tareas reales, con foto, dónde está y un botón por ítem.**
  El 05/09 lo confirmó caro: con las 2 push de la mañana no hizo nada, y de noche estuvo 40 min dentro de
  `puesta-al-dia` resolviendo 10 tareas y escribiéndome 2 veces.
- **⭐ CUANDO TIENE TRABAJO REAL PENDIENTE, LA EXPERIENCIA COMPITE Y PIERDE** → **la experiencia no debe competir con
  la tarea, debe PARASITARLA** (10/09: la pieza viva del portón migró al canal tarea, que es el que sí abre).
- **⭐ SU ACCIÓN ES FEEDBACK AUNQUE NO ESCRIBA**, y el tap es su idioma (13 `answer` en una noche). **Una foto con una
  línea de texto es la señal más rica que produce:** síntoma + planta + fecha en un solo gesto.
- **Las 7 veces que escribió fue LOGÍSTICA, IDENTIFICACIÓN, ORDEN DE TRABAJO, CONSULTA TÉCNICA o PEDIDO DE RE-ENVÍO,
  jamás una reseña:** no esperes veredicto, esperá instrucciones. La caja de feedback va igual en todas.
- **«Ocultar» no es «sacar»** · **dwell alto sin conversión ≠ éxito** · **«no contestó» ≠ «no le interesa»** · **el 201
  no mide nada** · **nunca 3 push en un día sin slot** · **si hubo actividad suya en la última hora, no encolar.**

## 💬 FEEDBACK DE TEXTO — los 3 vivos, todos ya ejecutados

1. *«Nose cuál es el crespón y la althea»* (03/09) → **regla permanente:** al nombrar una especie, **foto + dónde
   está**, siempre. Sin excepción.
2. *«Sacá todas las tareas ya completadas para achicar la página»* (05/09) → hecho (`solo-pendiente`). **«Ocultar» no
   es «sacar».**
3. *«Volvémela a enviar cuando revises con mi feedback en mente»* (05/09) → hecho, ed. 5/6/7. **Pide re-envío, no
   novedad: el re-envío con la corrección aplicada ES el contenido.**

## ⚙️ ESTADO OPERATIVO (11/09/2026)

`pix9` **active** · `uploads.json` **0 pendientes** (133 entries, leído campo por campo: ningún `note` sin contestar) ·
**threads 0 `pending`** · `user_tasks.json` 0 sin contestar · `task_states.json` 81 entries — **53 done / 38 active /
11 snoozed** sobre 102 tareas y 51 especies (16 huérfanas, descartarlas siempre) · última escritura suya en `task_states` **06/09 11:39Z**;
última actividad suya de cualquier tipo **HOY 08:02** (el pedido del push) · proposals **92** (54 dropped /
23 promoted / **13 pending** / 1 approved / 1 removed) · **compactación** no vencía hoy → **14/09** y **17/09**.

## 🚨 LAS TRES REGLAS QUE MANDAN

**#1 SUSTANCIA > gimmick.** Ayuda técnica REAL sobre SU jardín, ejecutable con la herramienta en la mano.

**#2 EL CONTROL VA ARRIBA.** Ningún primer control de ACCIÓN debajo del **35 %**, **medido renderizado en Chromium
390×780** (nunca por offset de caracteres — hoy el offset de bytes daba 42,7 % y el render 15,7 %). `audit.js` en
scratchpad — playwright en `/opt/node22/lib/node_modules`, chromium en
`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`; descartar `fixed`/`sticky` mirando **toda la cadena de
ancestros** y reportar el control de **acción**, no el link del índice. Últimas: ed.7 **18,9 %** · bandeja **3,4 %** ·
jardin-hoy **15,7 %**.

**#3 EL LARGO TAMBIÉN ES LAYOUT.** Tope operativo **~12 ítems**. El día que hay una respuesta personal que dar, la
lista se achica, no se estira.

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **⭐ UNA PROMESA MÍA SE COBRA SIEMPRE Y ENTERA, ganada o perdida, ANTES de que él la revise, y el día que vence** —
  **aunque ese día no me toque push** (hoy: se cobró dentro de la página). ⭐ **La corrección a su favor vale doble**;
  **la que va en contra se dice igual y con el número al lado** (hoy: «te vendí 3 grados de más»).
- **⭐ CORREGIR MI PROPIA GUÍA CON EL DATO DE HOY ES CONTENIDO DE PRIMERA.** · **⭐ FRENAR UNA TAREA VALE TANTO COMO
  PEDIRLA** (la lantana B-29): una lista de la que yo mismo saco cosas es creíble; una que sólo crece es spam.
- **⭐ LA EXPERIENCIA TIENE QUE SER UN OBJETO QUE SE LLENA, NO UN TEXTO CON UN BOTÓN AL FINAL.** Sigue **sin probarse**:
  la bandeja llegó +75 min tarde y con 0 visitas. **VIVA, no refutada** — y ahora el canal ya no la puede tapar.
- **Ayudarlo a HACER > informarlo**; **darle DÓNDE registrar lo que ya hizo** es casi igual de fuerte. · **⭐ AL
  NOMBRAR UNA ESPECIE: FOTO + DÓNDE ESTÁ, SIEMPRE.** · **⭐ EL CLIMA COMO EDITOR** · **⭐ LA CONDICIÓN CONVERTIDA EN
  FECHA** · **⭐ NUEVO: LA VENTANA PARTIDA POR HORA** (mañana vs tarde, por viento) — más fino que el día entero.
- **⭐ VERIFICAR MI PROPIO DATO ANTES DE PUBLICARLO.** · **El título es el activo más medido.** · **Timing verificado >
  urgencia inventada.** · **feedback_text = ley.** · ⚠️ `curl` a open-meteo NO sale del runner: **WebFetch**,
  `forecast_days=7`, **un modelo por llamada**; para saldar apuestas, `past_days` con `best_match`.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

**noticiero/«El Parte»** · **cero-lectura/duelos binarios** · **checklist de viaje** · **vos-decidís** (el eje AGENCIA
vive, el CONTENEDOR se quemó) · **mi-objetivo** · role-play verboso · countdown · app pasiva · editorial 3ª pers ·
mapa/espacial *(como formato entero; un plano chico DENTRO de otra cosa sí sirve)* · mística · racha/streak ·
biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** · **era gimmick** · **`podas-vuelta`** ·
**observacional suelto** («sacale foto a la flor»): pospuso 8 de un saque — **va como pedido corto DENTRO de otra
cosa, nunca como card propia**.

## 🏆 EL TALLER = LA LÍNEA DE PRODUCTO (única aprobada, en los dos slots)

n°1: 7/7 pasos ×3 pasadas, 168 s @95 %, **😍 dos veces** y ticks por árbol horas después. n°2: 7/7, cero reacción.
n°3 (24/08): leído entero, sin veredicto. **Por qué gana:** ① sustancia técnica sobre SUS plantas ② se abre con la
herramienta en la mano ③ una pantalla = una decisión ④ errores anticipados ⑤ diagramas propios.
⚠️ Sus ticks (`taller-arbol-<code>`) **NO** escriben `task_states.json`: contar con `generate_tasks_from_plants(PLANTS)`
+ `task_states.json['tasks']`, descartando las 16 huérfanas. ⚠️ `pip install Pillow` antes de `build.py`.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. **Excepción: el canal tarea es monotemático — su cast lo
  define la TAREA.** · **La EXPOSICIÓN MEDIDA manda sobre el ledger.** · **Una reedición sin push no consume elenco.**
- ⚠️ **VEDADOS HASTA EL 18/09** (exposición del 11/09): B-30, B-35, B-1, F-2. **HASTA EL 14/09:** I-1, I-2, B-6, B-26, B-2, B-10, B-3, F-5,
  B-27 *(exposición cero medida → de hecho frescos)*. **HASTA EL 13/09:** B-7, B-5a, B-25, B-12, B-15, B-8, B-4, B-43,
  B-22, B-36, F-3, B-41. **SE LIBERAN EL 12/09:** B-46, B-9, B-18, B-24, B-32, B-20, B-13, B-47.
- ✅ **LIBRES PARA EL SÁBADO 12/09:** B-16, B-37, F-9, B-44, B-40, F-8, F-10, B-14, B-45, B-48, B-49, B-21, B-28,
  B-11, B-31, B-33, B-39, F-1 + los ocho que se liberan ese día. **B-34 fuera de toda cantera: ya no existe.**
- **No repetir antes del 21/09:** la propagación/esqueje · «lo que ibas a tirar» · el ejemplar único sin repuesto · la
  campana de botella · el corte al ras bajo el nudo · el lado este como vivero · el reparto de la ventana por día.
  **No antes del 24/09:** el diagnóstico sanitario sobre foto suya · la mea culpa de ficha incompleta · «la ventana de
  este año ya cerró». **No antes del 25/09:** la ventana partida por hora.

## ⏱️ CADENCIA (autoridad operativa — semanal, día-consciente)

**Tarea 10:00 → Lun / Jue / Sáb. Experiencia → Lun 18:00 y Sáb 11:00. Mar, Mié, Vie y Dom: 0 push, sólo mantenimiento.**

- **Excepción válida y única:** una push que **él pidió por escrito** (pasó el 06/09). Se anota en el ledger. · **Un día
  sin slot no es un día sin trabajo:** limita las **notificaciones**, no las **ediciones**.
- **Una sola push por slot de experiencia:** original NUEVA + las **aprobadas** de ese slot agrupadas DENTRO.
  **Aprobación = recurrencia** (😍 / slot «sí» / `engageApprove`); pending no se borra, no recurre. **Única aprobada:
  `el-taller`, en los dos slots.** Contrato completo: `engagement.md` §4.
- **Canal tarea:** URLs estables que se **REEDITAN en su lugar** (`2026-07-24-jardin-hoy.html`, `puesta-al-dia.html`).
  NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py --merge`.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **NO BORRAR, no pushear sueltas:** Expedientes, `top3-tareas.html`, `tareas-pendientes.html`, `puesta-al-dia.html`,
  Asamblea, tu-semana, vos-decidís, jardin-hoy, `el-taller` (aprobada). · **30/07:** foto + caja de comentario en
  TODAS las tareas. · Las fotos y comentarios de esas páginas van al **thread**: los procesa `/responder-tareas`.
- **28/07 PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER** (B-22/B-36 es de PODA). · **04/09:**
  42 fotos de especie (`ai_status:"n/a"`: NO procesarlas), **no volver a pedir fotos generales**; sin foto: B-41,
  B-32, B-43, B-46/47, B-2B, B-22, B-36. · **B-34 dada de baja con consentimiento escrito — NUNCA borrar una especie
  sin eso.** · **05/09:** «No quiero tener que cambiar tokens nunca más».

## TODO / próximos experimentos

- **🎯 SÁBADO 12/09 — LOS DOS SLOTS, Y EL PRIMERO CON CANAL SANO.** Tarea 10:00: **vuelven las 3 que pospuso el 05/09**
  (B-23 limonero, B-24 mandarina, B-46-3 vivero) — traerlas **agrupadas**, no de a una; y el clima manda no pedir
  tijera fina (51 km/h). Experiencia 11:00: la apuesta es **el objeto que se llena PARASITANDO la tarea** — que la
  landing sea el mismo lugar donde registra lo que hizo el viernes con B-1 y F-2, no una pieza aparte que compita.
- **Cobrar el saldo del viernes con `past_days`** (`best_match`): hoy afirmé 0,0 mm y máxima 12,7°. Se verifica mañana,
  gane o pierda. Y **si tocó «Hecha» en B-1 o F-2**, esa es la primera conversión limpia de la era del canal sano.
- **19/09: vuelven las otras 5** que pospuso (B-46-5, B-47-3, B-13-2, B-20, B-32). **27/09:** B-41. **15/10:** B-45.
- **Si contesta el tri-botón de B-35:** «igual de mal» → la tarea de cobre de julio nombra los dos ejemplares en el
  título; «ese está sano» → hay un dato de foco que vale una card entera.
- **Semana 4 de la bandeja (≈05/10): recordarle qué mirar** — lo prometí en la tabla de la página.
- **Cantera SIN USAR:** condiciones sin fecha del catálogo · poda×fruta (feb y may-sep) · la coronita F-5 en octubre ·
  el fun_fact NASA de la cinta · el bálsamo del liquidámbar B-37 · el fun_fact Persia/China del durazno (intacto).
