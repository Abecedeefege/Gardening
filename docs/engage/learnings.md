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
- **Única excepción a los días sin slot:** que el usuario **lo pida explícitamente**. Aplicada el 02/08 (ver abajo). Si el pedido es condicional («cuando esté lindo»), la condición se **verifica con datos reales** antes de encolar — no se asume.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + HTML de pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.

## 🏆 EL TALLER = PRIMERA EXPERIENCIA APROBADA Y RECURRENTE (01/08)

`2026-08-01-el-taller` — **APPROVED, slot LUNES 18:00.** Es el mejor resultado desde el thread del liquidámbar y define la línea de producto.

- Señal: **7/7 pasos del wizard completados… y después recorridos DE NUEVO** (`taller-paso-1..7` ×2), dwell 168s @95% + 30s @100%, reacción **😍 love**, **slot lun18 «sí»**, y feedback de texto positivo.
- **Sábado 11:00 lo dejó SIN prender.** No es rechazo del formato: es que el sábado ya tiene la push de tarea a las 10:00. Un solo slot de experiencia por semana le alcanza.
- **Por qué ganó (replicar esto, no la estética):** ① sustancia técnica real y verificable sobre SUS árboles ② se abre **con la herramienta en la mano** — acompaña el trabajo físico, no lo describe ③ una pantalla = una decisión ④ los errores anticipados («el error:») ⑤ diagramas propios en vez de texto.
- **Serie:** una edición por tarea real. El wizard es reutilizable tal cual, solo cambia el contenido. **nº2 = poda de flor (crespón B-9 / althea B-18)**, a la vuelta del viaje. Después: pitósporo B-43 (reducción), cerco B-7·11·31·33 (recorte parejo).
- **Métrica nueva y valiosa:** `taller-paso-N` me dice exactamente dónde se traba. Hasta ahora: **no se traba en ningún paso.**

## 📩 EJECUTADO 02/08 — pedido textual atendido con dato real

Feedback del 01/08: «Genial esto. Pero **hoy está lloviendo, mándamela cuando esté lindo**!»

- Verifiqué el parte real de Montevideo antes de decidir: **domingo 2 = 0 mm, 0% de probabilidad, 14°/9°, viento 18 km/h — el único día limpio que queda antes del viaje.** Lun 3 = 50% prob · Mié 5 llovizna · Jue 6 = 7,5 mm + 39 km/h · Vie 7 se va.
- Por eso encolé **1 push el domingo** (día sin slot): excepción legítima por pedido explícito + condición cumplida.
- **Misma URL, contenido RENOVADO** (regla de re-push): bloque de acuse con su frase citada y la fecha, tabla de **ventanas reales** hasta el viaje, hero/facts al día (0 mm · 5 días al viaje), **ticks persistentes por árbol** (`taller-arbol-<code>`) y biblioteca mostrando el slot ya prendido.
- **Lección a mantener:** cuando el usuario pone una condición del mundo real, **ir a buscar el dato** y mostrarle que se verificó. El acuse citando su propia frase es barato y es exactamente la prueba de que el sistema lo escucha.

## 📌 MANDATO 24/07 (canal tarea — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS.** Consolidada en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable, se REEDITA en su lugar). NO encolar task-dia/pendientes/top3 sueltas. NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
2. **jardin-hoy lleva siempre:** vistazo de 5s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`) + caja «🙋 Pedime lo que necesites».
3. **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.

## ✈️ CONTEXTO DOMINANTE — VIAJE **7 al 23 DE AGOSTO**

- Tres ventanas, con veredicto antes/después POR TAREA. Usar hasta el 24/08:
  - **Antes de irte (hasta el 6/8) = 4:** los tres carozos (durazno B-30/B-35, ciruelo F-4, ciruela amarilla B-38) — **hoy domingo 2 o el martes 4, no hay más días secos** — + hortensia B-5a/b a tierra (cualquier día).
  - **Durante (7–23/8) = 0.** Dormancia + lluvia. **NO nagear NADA.**
  - **A la vuelta (24–31/8) = 11:** crespón B-9, althea B-18, caqui B-41, pitósporo B-43-2, gardenia neem B-25-3, hibisco B-4 (la más atrasable), podranea F-2, gardenia acidificar B-25, cerco B-7·11·31·33, hiedra B-15, abelia F-7.
- La gran poda NO es «mediados de agosto» este año: la ventana real es **fin de agosto en adelante**.
- Verificar la lista SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07, DROPPED):** leyó los 75s enteros pero puso **NO a los dos slots + meh**. Lee el contenido, rechaza la recurrencia. Enterarse no es el valor; **ayudarlo a HACER sí**.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo. Revisá lo del liquidámbar». MUERTO.
- **vos-decidis / feed-de-decisiones:** ganó el 26/07 y se fatigó en 3 días. El eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- **checklist de viaje / «antes de irte» como deberes:** 29/07 sin señal. El viaje se trata como TRANQUILIDAD, no como lista de pendientes.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Lo que más pesa es la ayuda técnica REAL sobre SU jardín. Confirmada por El Taller.
- **Ayudarlo a HACER > informarlo.** Lectura combinada de el-parte (informar → no) y jardin-hoy + El Taller (hacer → oro).
- **Acompañar el momento físico.** El Taller no se lee en el sillón: se abre con el serrucho en la mano. Ése es el diferencial.
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla, glanceable. **FOTOS REALES = need validado.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** un Taller es monotemático — su cast lo define la TAREA, no el elenco. El ≥70% fresco no aplica ahí, pero **cada Taller nuevo cambia de tarea** (y por lo tanto de cast).
- ⚠️ **Los 4 carozos (B-30, B-35, F-4, B-38) quedan quemados hasta el 09/08** — usados 01/08 y 02/08. Fuera de la serie Taller, no protagonizan nada.
- ⚠️ «romero única flor de julio» ya se usó 4× — descansar hasta mediados de agosto.
- Re-push de una aprobada = contenido RENOVADO en la misma URL (hecho el 02/08).

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera (identidad en duda).
- **30/07:** foto + caja de comentario en TODAS las tareas, también las de agosto → EJECUTADO. Liquidámbar B-37 → hecho.
- **01/08:** «mándamela cuando esté lindo» → EJECUTADO el 02/08 con verificación meteorológica.
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas + **el-taller** aprobada: no borrar.

## 📈 Estado del sistema + jardín (agosto 2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable.
- Jardín en DORMANCIA, saliendo. ~52 días al equinoccio (23/09). Heladas tardías posibles hasta fin de agosto — pican al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, arranque con lechuga a la vuelta · hortensia B-5a/b → a tierra antes del viaje, rincón sur junto a la pera B-39 · liquidámbar B-37 ✅ hecho 30/07 · gardenia B-25 neem → a la vuelta · **objetivo declarado del usuario = «más flor»**.
- **Pendientes reales al 02/08: 15** (4 antes del viaje + 11 a la vuelta).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37 / palto B-36 / pileta (sol de mañana) · oeste/frente = fotinias, ligustro F-9, fresno F-10 (sol de tarde) · **romero B-26 = única que florece en julio** · mandarina B-24 + pindó B-8 en fruto en invierno · viraró B-32 (nativo) florece en agosto · limonero B-23 fruta 12/12 · plantines de palta contra la pared, SIN TOCAR · B-41 caqui identidad EN DUDA · B-45 sin id.
**Poda de Prunus (verificado en fichas):** durazno 40-50% vaso abierto · ciruelo F-4 25-35% silueta · ciruela B-38 30% + sacar madera >4 años · los tres florecen en agosto · ventana = yema hinchada sin abrir · gomosis = riesgo principal, alcohol 70% entre cortes y sellar cortes >1,5 cm.

## Conclusiones de los pushN (por feedback real)

- **01/08 (sábado) — el-taller: ÉXITO MÁXIMO.** 😍 + slot lun18 + 7/7 pasos ×2 + feedback positivo. Aprobada y recurrente. Es el molde a serializar.
- **01/08 (sábado) — jardin-hoy: floja ese día.** Abierta 14:20 (4h tarde), dwell 25s, sin señal. No es fatiga del canal: es que ese día el contenido de valor estaba en el Taller. Sostener el canal tarea, sin subirle la intensidad.
- **31/07 (viernes) — el-parte: MASOMENOS con veredicto claro.** Leyó todo (75s, 100%) pero ambos slots en NO + meh. El formato-diario, archivado. DROPPED.
- **30/07 (jueves) — jardin-hoy GANADORA, día tier-1.** 3 feedback_text (oro): liquidámbar hecho, «foto + caja de comentario en las tareas de agosto» y «viaje 7-23, recomendame antes/después». Los tres EJECUTADOS.
- **29/07 — masomenos.** Fotos solas sin sustancia ni gancho de acción no alcanzan.
- **28/07 — negativo.** esto-o-esto muerto; vos-decidis v3 rechazada.
- **26/07:** vos-decidis ganó (sub sí + like + 116s) — pico del eje agencia, después fatigado.
- **24/07:** jardin-hoy ganadora (3 feedback_text). Minimalismo + tareas reales + caja de pedidos.
- **21/07:** asamblea — «Está todo perfecto». Sustancia + honestidad funcionan.

## TODO / próximos experimentos

- **Lunes 3/08, slot 18:00:** toca original NUEVA + El Taller (aprobado) agrupado dentro. ⚠️ El usuario se va el viernes 7: la original nueva debe respetar «el viaje = tranquilidad, no deberes» (el eje checklist ya murió el 29/07).
- **Taller nº2 = poda de flor (crespón B-9 / althea B-18)** para el 24/08, a la vuelta. Cast fresco y tarea distinta.
- **Plan de reentrada del 24/08:** las 11 tareas ordenadas por prioridad y por rendimiento en flor (su objetivo declarado).
- Before/after con las fotos reales que sube el usuario (el paso «mandame una foto» del taller es la puerta de entrada).
</content>
</invoke>
