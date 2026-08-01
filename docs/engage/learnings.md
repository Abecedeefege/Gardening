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
- **Aprobación = recurrencia.** Solo vuelve lo que el usuario prendió (`engageApprove` / slot en «sí»). Pending sin aprobar no se borra: simplemente no recurre.
- Cada experiencia: back-link «← Volver al sitio estable» primero + reacción + selector de slots (`<slug>-slot-lun18` / `<slug>-slot-sab11`) + caja de feedback propia (`id=engage-feedback-box`) + aprobar/rechazar + HTML de pitch con 6 modelos. `send_at` ≥60 min post-corrida, `expires_at` mismo día 22:00, timestamps `-03:00`.
- ⚠️ El mandato del 31/07 de «2 instancias en paralelo, push también los viernes» **quedó sin efecto**: el prompt del 01/08 restituye la cadencia semanal pura (Mar/Mié/Vie/Dom = 0 push). El resultado del viernes 31/07 respalda la vuelta atrás (meh + ambos slots en NO).

## 📌 MANDATO 24/07 (canal tarea — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS.** Consolidada en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable, se REEDITA en su lugar). NO encolar task-dia/pendientes/top3 sueltas. NO correr `gen_task_reminders.py` ni `gen_top3_tareas.py` con `--merge`.
2. **jardin-hoy lleva siempre:** vistazo de 5s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`) + caja «🙋 Pedime lo que necesites».
3. **PALTA:** los plantines siguen contra la pared a la sombra, **SIN MOVER**.

## ✈️ CONTEXTO DOMINANTE — VIAJE **7 al 23 DE AGOSTO**

- Tres ventanas, con veredicto antes/después POR TAREA. Usar hasta el 24/08:
  - **Antes de irte (hasta el 6/8) = 4:** los tres carozos (durazno B-30/B-35, ciruelo F-4, ciruela amarilla B-38) **el domingo 2** + hortensia B-5a/b a tierra (cualquier día).
  - **Durante (7–23/8) = 0.** Dormancia + lluvia. **NO nagear NADA.**
  - **A la vuelta (24–31/8) = 11:** crespón B-9, althea B-18, caqui B-41, pitósporo B-43-2, gardenia neem B-25-3, hibisco B-4 (la más atrasable), podranea F-2, gardenia acidificar B-25, cerco B-7·11·31·33, hiedra B-15, abelia F-7.
- La gran poda NO es «mediados de agosto» este año: la ventana real es **fin de agosto en adelante**.
- Verificar la lista SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **noticiero / diario / «El Parte» (31/07):** leyó los 75s enteros pero puso **NO a los dos slots + meh**. Lee el contenido, rechaza la recurrencia. Enterarse no es el valor; **ayudarlo a HACER sí**. Archivado.
- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + «No es mi tipo. Revisá lo del liquidámbar». MUERTO.
- **vos-decidis / feed-de-decisiones:** ganó el 26/07 y se fatigó en 3 días. El eje AGENCIA vive; el CONTENEDOR repetido se quema.
- **mi-objetivo (goal→plan):** aspiración abstracta sin acción NO convierte.
- **checklist de viaje / «antes de irte» como deberes:** 29/07 sin señal. El viaje se trata como TRANQUILIDAD, no como lista de pendientes.
- Otros muertos: role-play verboso · countdown · app pasiva · editorial 3ª pers · mapa/espacial · mística · racha/streak · biografías · dinero/tasación · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Lo que más pesa es la ayuda técnica REAL sobre SU jardín. El thread del liquidámbar (poda de reducción paso a paso) sigue siendo el pico histórico y el usuario lo usa como vara.
- **Ayudarlo a HACER > informarlo.** Es la lectura combinada de el-parte (informar → no) y jardin-hoy (hacer → oro). El contenido tiene que servir con las manos sucias.
- **Minimalismo + REAL + VISUAL.** Poco texto por pantalla, glanceable. **FOTOS REALES = need validado.**
- **feedback_text = ley.** Positivo = expandir. Negativo = nunca vuelve. Pedido = ejecutar ya. Abrir sin señal activa = «masomenos», NO es éxito.

## 🆕 EXPERIENCIA DEL DÍA — 01/08 (sábado, slot 11:00)

**`2026-08-01-el-taller` — 🪚 «El Taller nº 1: poda de carozos».** Primer intento de productizar el eje ganador (el thread del liquidámbar) como **formato repetible**: un walkthrough guiado que se abre **con el serrucho en la mano** y avanza al ritmo del trabajo físico.

- Formato nunca probado: **wizard de 7 pasos** (uno por pantalla, con barra de progreso), **diagramas SVG propios** (vaso abierto vs centro cerrado; los tres cortes), **checklist de herramientas** que persiste en el device, 3 dudas resueltas de antemano, ficha comparada de los tres árboles.
- Cada paso completado loguea `taller-paso-N` → **sé exactamente dónde se traba**. Esa es la métrica nueva más valiosa que tengo.
- Timing insoslayable: mañana domingo 2 es el día seco, es la semana exacta de poda de Prunus (yema hinchada sin abrir) y quedan 6 días para el viaje.
- **WATCH:** ¿cuántos pasos completa? ¿reacción 😍? ¿prende slot? Si gana → serializar «El Taller» con una tarea real distinta por edición (crespón B-9 / althea B-18 → poda de flor; pitósporo B-43 → reducción; cerco B-7).
- Pool sin pushear (candidatas débiles): `2026-07-30-se-multiplican-solos`, `2026-07-30-aguantan-solos`.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizarlo DESPUÉS. Planta featured descansa ≥7 días; fun_fact no se repite en <14 días.
- **Excepción documentada:** un Taller es monotemático por definición — su cast lo define la TAREA, no el elenco. La regla del ≥70% fresco no aplica ahí, pero **cada Taller nuevo debe cambiar de tarea** (y por lo tanto de cast).
- ⚠️ «romero única flor de julio» ya se usó 4× — descansar hasta mediados de agosto.
- Re-push de una promovida = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS — NO PISAR

- **04/07:** Expedientes + `top3-tareas.html` NO borrar. ⚠️ **Pillow no viene en el runner: `pip install Pillow`** antes de tocar `build.py`/`gen_*.py`.
- **23/07:** `tareas-pendientes.html` = página fija, no borrar, no pushear suelta.
- **28/07:** lechuga/huerta → a la vuelta, fin de agosto. Caqui B-41 → ignorar hasta primavera (identidad en duda).
- **30/07:** foto + caja de comentario en TODAS las tareas, también las de agosto → EJECUTADO. Liquidámbar B-37 → hecho.
- **Asamblea, tu-semana, vos-decidis, jardin-hoy** promovidas: no borrar.

## 📈 Estado del sistema + jardín (agosto 2026)

- Push subscription device `pix9`: **active**. Logging vía `/api/feedback` confiable.
- Jardín en DORMANCIA, saliendo. ~53 días al equinoccio (23/09). Heladas tardías posibles hasta fin de agosto — pican al SUR y al ESTE al amanecer.
- **Decisiones ejecutadas:** huerta → muro norte, arranque con lechuga a la vuelta · hortensia B-5a/b → a tierra antes del viaje, rincón sur junto a la pera B-39 · liquidámbar B-37 ✅ hecho 30/07 · gardenia B-25 neem → a la vuelta · **objetivo declarado del usuario = «más flor»**.
- **Pendientes reales al 01/08: 15** (4 antes del viaje + 11 a la vuelta).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37 / palto B-36 / pileta (sol de mañana) · oeste/frente = fotinias, ligustro F-9, fresno F-10 (sol de tarde) · **romero B-26 = única que florece en julio** · mandarina B-24 + pindó B-8 en fruto en invierno · viraró B-32 (nativo) florece en agosto · limonero B-23 fruta 12/12 · plantines de palta contra la pared, SIN TOCAR · B-41 caqui identidad EN DUDA · B-45 sin id.
**Poda de Prunus (verificado en fichas):** durazno 40-50% vaso abierto · ciruelo F-4 25-35% silueta · ciruela B-38 30% + sacar madera >4 años · los tres florecen en agosto · ventana = yema hinchada sin abrir · gomosis = riesgo principal, alcohol 70% entre cortes y sellar cortes >1,5 cm.

## Conclusiones de los pushN (por feedback real)

- **31/07 (viernes, canal paralelo) — el-parte: MASOMENOS con veredicto claro.** Abierta 22:43, dwell 75s, scroll 100% → leyó todo. Pero **ambos slots en NO y reacción meh**, sin feedback de texto. Lectura dura: el usuario consume información pero **no quiere suscribirse a que le cuenten cosas**. El formato-diario está archivado; lo que sobrevive es que el contenido debe habilitar una ACCIÓN.
- **30/07 (jueves) — jardin-hoy GANADORA, día tier-1.** Dwell 199s / 45s / 37s, scroll 100%, **3 feedback_text (oro)**: liquidámbar hecho, «foto + caja de comentario en las tareas de agosto» y «viaje 7-23, recomendame antes/después». Los tres EJECUTADOS. La ayuda REAL por tarea, con foto y caja de comentario, es EL activo del producto.
- **29/07 — masomenos.** los-que-no-duermen + antes-de-irte: abiertas de noche, 14-30s, sin señal. Las fotos solas no alcanzan sin sustancia ni gancho de acción.
- **28/07 — negativo.** esto-o-esto (cero-lectura) muerto; vos-decidis v3 rechazada (molde fatigado). jardin-hoy siguió dando feedback rico.
- **26/07:** vos-decidis ganó (sub sí + like + 116s) — pico del eje agencia, después fatigado.
- **24/07:** jardin-hoy ganadora (3 feedback_text). Minimalismo + tareas reales + caja de pedidos.
- **21/07:** asamblea — «Está todo perfecto». Sustancia + honestidad funcionan.

## TODO / próximos experimentos

- **Si El Taller gana** → serializarlo: una edición por tarea real (crespón/althea = poda de flor a la vuelta; pitósporo = reducción; cerco = recorte parejo). El wizard es reutilizable tal cual.
- **Si El Taller no gana** pero completa muchos pasos → el problema es el envoltorio, no el eje: probar el mismo contenido embebido DENTRO de la landing de la tarea (`docs/tasks/<id>.html`) en vez de como página aparte.
- Before/after con las fotos reales que sube el usuario (el paso «mandame una foto» del taller es la puerta de entrada).
- **Plan de reentrada del 24/08:** cuando vuelva, las 11 tareas ordenadas por prioridad y por rendimiento en flor (su objetivo declarado).
