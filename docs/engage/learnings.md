# Learnings del agente de engagement

Memoria del agente. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🆕🆕 MANDATO NUEVO 31/07 (prompt de la Routine — FUNCIÓN PARALELA, MÁXIMA AUTORIDAD)

- **Cada corrida ahora salen 2 instancias EN PARALELO.** Cada instancia DEBE encolar **una notificación nueva** que lleve a una **experiencia armada DE CERO**, construida **inicializando un agente al momento de la ejecución** con persona product/UX/growth + ventas/marketing.
- La experiencia es **news-feed**, y sus objetivos medibles: (1) que el usuario la marque 😍 (increíble), (2) que **prenda un slot** (recurrencia), (3) **HTML de pitch** con 6 modelos de monetización (3 innovadores + 3 ultra-creativos).
- Esto **pisa la regla «Viernes = 0 push»** los días que la Routine corre: si corre, se manda una experiencia nueva igual. La cadencia semanal de la tabla sigue siendo la base para tareas; las experiencias ahora pueden salir además por este canal paralelo.
- **Implicancia operativa:** cada instancia usa un slug propio y hace `git pull --rebase` + reintento en el push (la otra instancia pushea en paralelo → 409 esperable).

## 📌📌 MANDATO 24/07 (chat + feedback — NO PISAR)

1. **UNA SOLA PUSH DE TAREAS, NO TRES.** Canal-tarea consolidado en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable). NO encolar task-dia/pendientes/top3 sueltas — van DENTRO de jardin-hoy. NO correr gen_task_reminders/gen_top3 con --merge.
2. **jardin-hoy lleva:** vistazo 5s + menús COLAPSADOS + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`, colapsada) + caja «🙋 Pedime lo que necesites». Reforzado 30/07 y EJECUTADO (16 tarjetas con foto+comentario). NO volver a publicar tarea sin foto+caja.
3. **PALTA:** plantines contra la pared a la sombra, **SIN MOVER**. Lo reubicado fue el vivero de palmeras (B-46).

## ✈️ CONTEXTO DOMINANTE — VIAJE **7 al 23 DE AGOSTO** (fechas exactas, feedback 30/07)

- jardin-hoy reordenada en **3 ventanas** con veredicto antes/después POR TAREA (EJECUTADO 30/07). Usar SIEMPRE hasta el 24/08:
  - **Antes de irte (30/7–6/8) = 4:** carozos (durazno B-30/35, ciruelo F-4, ciruela amarilla B-38) + hortensia B-5a/b a tierra. **Si solo una: el durazno.**
  - **Durante (7–23/8) = 0.** Dormancia + lluvia. **NO nagear NADA.**
  - **A la vuelta (24–31/8) = 11.** Todas con margen (crespón B-9, althea B-18, caqui B-41, pitósporo B-43-2, gardenia neem B-25-3, hibisco B-4 atrasarlo, podranea F-2, gardenia acidificar B-25, cerco B-7·11·31·33, hiedra B-15, abelia F-7).
- Verificar la lista de agosto SIEMPRE contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página.
- La gran poda NO es «mediados de agosto» este año: con el viaje, la ventana real es **fin de agosto en adelante**.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **cero-lectura / duelos binarios (esto-o-esto 28/07):** meh + sub NO + «No es mi tipo. Revisá lo del liquidámbar» = quiere SUSTANCIA, no gimmick. MUERTO.
- **vos-decidis / feed-de-decisiones:** ganó 26/07 pero se fatigó en 3 días → 28/07 rejected. El eje AGENCIA vive; el CONTENEDOR feed-de-decisiones repetido se quema.
- **mi-objetivo (goal→plan):** rejected 27/07. Aspiración abstracta sin acción NO convierte.
- Otros muertos: role-play verboso · countdown/anticipación · app pasiva · editorial 3ª pers · ESPACIAL/mapa · gesto solo · mística · nota-larga · superlativo · racha/streak · biografías · chat-coral · dinero/tasación · alivio-PASIVO vacío · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Lo que MÁS pesa: ayuda contextual REAL de SU jardín. El thread del liquidámbar (poda de reducción paso a paso) = pico de engagement, el usuario lo cita de referencia. El contenido real gana al contenedor.
- **Minimalismo + REAL + VISUAL.** Poco texto, glanceable. **FOTOS REALES = NEED validado.** Usarlas siempre.
- **feedback_text = ley.** Positivo = expandir. Negativo = NUNCA vuelve. Pedido = ejecutar YA. Sin señal activa = «masomenos», no cuenta como éxito.

## ⏱️ CADENCIA (base semanal para TAREAS; experiencias además por el canal paralelo 31/07)

| Día | Tarea (jardin-hoy) | Experiencia (slot) |
|---|---|---|
| **Lunes** | ✅ 10:00 | ✅ 18:00 |
| Mar/Mié/Vie/Dom | — | — (pero el canal paralelo 31/07 manda experiencia nueva cuando la Routine corre) |
| **Jueves** | ✅ 10:00 | — |
| **Sábado** | ✅ 10:00 | ✅ 11:00 |

- **Aprobación = recurrencia.** Una experiencia solo se re-manda si el usuario la **aprobó** (`engageApprove`). La original nueva SIEMPRE va (experimento). Pending sin aprobar NO se borra el mismo día: solo no recurre.
- **CTA = "slots disponibles"** (Lun18/Sáb11, opt-in): `<slug>-slot-lun18` / `<slug>-slot-sab11`.
- Cada experiencia: back-link primero + reacción + selector de slots + caja feedback propia (`id=engage-feedback-box`) + botones aprobar/rechazar + HTML pitch (6 modelos). send_at ≥60min post-corrida. expires_at = mismo día 22:00 -03:00. Timestamps `-03:00`.

## 🆕 EXPERIENCIAS EN EL POOL

- **31/07 (HOY, canal paralelo) — `2026-07-31-el-parte` «📰 El Parte del Jardín»:** formato NOTICIERO/diario personalizado (despachos fechados con foto+dato verídico). Apuesta: el diario entrega la SUSTANCIA que el usuario premia y **justifica la recurrencia** por naturaleza (edición nueva cada día). Cast fresco+seasonal: **B-24 mandarina** (en fruto, lead), **B-8 pindó** (coquitos, nativa), **B-32 viraró** (florece agosto = corresponsal del viaje, nativa), **B-10 lavanda** (aromática invernal + nota de heladas). Push 18:00. **WATCH:** ¿el formato-diario convierte donde el gimmick murió? ¿prende slot? ¿reacción 😍? Si gana → serializar «El Parte» diario con cast rotando.
- **Pool 30/07 (nunca pusheadas, Jue = task-only) — siguen `pending` como candidatas:** `2026-07-30-se-multiplican-solos` (propagación gratis: B-12/B-2/B-15) y `2026-07-30-aguantan-solos` (tranquilidad viaje con prueba: B-34/B-42/B-43). Sin datos de engagement (no se mostraron). Reutilizables en un slot de experiencia si hace falta.

## 🚫 ANTI-REPETICIÓN (queja 18/07: «me repetís los mismos funfacts de las mismas plantas»)

- Leer `facts_ledger.json` ANTES, actualizar DESPUÉS. **Fun_facts quemados → NO usar.** Tocar plantas por ÁNGULO NUEVO (tarea/estado/propagación/resistencia/decisión).
- Planta featured descansa ≥7 días; ≥70% del cast sin usar en 7 días. Las usadas por tarea/estado-real están exentas del criterio fun_fact.
- ⚠️ **Cuidado con «romero única flor de julio»**: ya se usó 4× (22/23/24/28/07). Descansar ese ángulo hasta ~mediados de agosto.
- Re-push de promovida = contenido RENOVADO en la misma URL.

## 📌 PEDIDOS DIRECTOS PREVIOS — NO PISAR

- **04/07:** Expedientes + Top 3 (`top3-tareas.html`) NO borrar (push fundida en jardin-hoy). ⚠️ Pillow NO viene en el runner: `pip install Pillow` antes de gen_*.py/build.py (solo si toco fuentes).
- **23/07:** `tareas-pendientes.html` = página fija (no borrar). Ya no se pushea suelta.
- **Asamblea, tu-semana, vos-decidis** promovidas (no borrar aunque el molde esté fatigado).

## 📈 Estado del sistema + jardín (julio 2026)

- Push subscription device `pix9`: **active**. Logging por `/api/feedback` confiable.
- Jardín en DORMANCIA. ~54 días a primavera (equinoccio 23/09). Heladas tardías posibles hasta ~fin agosto (pican al SUR y ESTE al amanecer).
- **Decisiones del usuario ejecutadas:** huerta→muro norte (pausa hasta la vuelta) · arranque→lechuga (a la vuelta) · hortensia B-5a/b→a tierra ANTES del viaje · rincón→le recomendé sur junto a la pera B-39 · liquidámbar B-37→✅ HECHO 30/07 («Ya quedó hecho esto») · caqui B-41→observar (poda plant-B-41 sigue activa, a la vuelta) · gardenia B-25 neem→a la vuelta · **OBJETIVO DECLARADO = «más flor»**.
- **Pendientes reales al 31/07: 15** (4 antes del viaje + 11 a la vuelta, ver ventanas arriba).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37/palto B-36/pileta (sol mañana) · oeste/frente = fotinias/ligustro F-9/fresno F-10 (sol tarde) · **romero B-26 = única que florece en julio** · **mandarina B-24 + pindó B-8 = en fruto en invierno** · **viraró B-32 (nativo) florece agosto** · limonero B-23 fruta 12/12 · plantines de palta contra la pared a la sombra, SIN TOCAR · B-41 caqui identidad EN DUDA (snoozed 15/11) · B-45 sin id (snoozed 15/10).

## Conclusiones de los pushN (por feedback real)

- **30/07 (jueves) — jardin-hoy GANADORA (día tier-1).** 3 push de tarea (2 cadencia/pedido + 1 extra a pedido explícito en chat). Engagement fortísimo: dwell **199s / 45s / 37s**, scroll 100%. **3 feedback_text (oro):** (1) liquidámbar «Ya quedó hecho» → marcado done; (2) «foto + caja de comentario en tareas de agosto» → EJECUTADO (16 tarjetas); (3) «viaje 7-23 ago, recomendame antes/después» → EJECUTADO (3 ventanas). **Lectura:** la ayuda REAL por-tarea con foto+comentario es EL activo. Las 2 experiencias construidas ese día NO se pushearon (Jue = task-only) → quedan de pool.
- **29/07 — DÍA MASOMENOS.** los-que-no-duermen + antes-de-irte: ambas abiertas de noche, dwell 14-30s, SIN voto/reacción/sub → dropped. Las FOTOS solas no alcanzan: hace falta sustancia + gancho de acción. «Checklist de viaje» no engancha → viaje como TRANQUILIDAD, no como deberes.
- **28/07 — negativo.** esto-o-esto (cero-lectura): sub NO + meh + «No es mi tipo» → MUERTO. vos-decidis v3: rejected → molde fatigado. jardin-hoy: feedback_text RICO = el activo que MÁS importa.
- **26/07:** vos-decidis GANÓ (sub sí + like + 116s) — pico agencia, luego fatigado.
- **24/07:** jardin-hoy GANADORA (3 feedback_text tier-1). Minimalismo + tareas reales + pedime-box.
- **21/07:** asamblea «Está todo perfecto». Sustancia/foro + honestidad = bien.

## TODO / próximos experimentos

- **Si El Parte (diario) gana** → serializarlo diario con cast rotando (una edición fresca por día = el hábito news-feed que el usuario podría suscribir). · El eje MÁS fuerte sin explotar como formato: **ayuda contextual real estilo thread** (el liquidámbar) — una consulta profunda por día sobre SU jardín. · before/after con fotos reales del usuario. · Plan de reentrada fin de agosto (poda por prioridad) para cuando vuelva del viaje.
