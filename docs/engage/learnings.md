# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 📌📌 MANDATO DIRECTO DEL USUARIO 24/07 (chat + feedback_text — MÁXIMA AUTORIDAD, NO PISAR)

1. **UNA SOLA PUSH DIARIA PARA TAREAS, NO TRES.** El canal-tarea se consolida en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable). **NO encolar task-dia/pendientes/top3 sueltas** — su contenido va DENTRO de jardin-hoy. (NO corro gen_task_reminders/gen_top3 con --merge; jardin-hoy es la única push de tareas, mantenida a mano.)
2. **jardin-hoy lleva:** vistazo de 5 s (estado + 3 chips) + menús COLAPSADOS + menú huerta + **foto real de la especie en TODAS las tareas** + **caja de comentario en TODAS** (`engageFeedback('jh-<slug>')`, colapsada tras botón «💬 Comentar» para no cargar la vista) + caja «🙋 Pedime lo que necesites». Mantener menús actualizados con task_states + data_plants cada corrida y subir la fecha visible.
   → **Reforzado 30/07** (feedback_text): «Agregame una foto a las especies en las tareas de agosto también así sé a qué hacen referencia. Cada especie/tarea debería tener la posibilidad de dejarte un comentario». **EJECUTADO**: las 16 tarjetas tienen foto + comentario. NO volver a publicar una tarea sin foto y sin caja.
3. **CORRECCIÓN factual 24/07 (mantener):** plantines de **PALTA** contra la pared, a la sombra, **SIN MOVER**. Lo reubicado fue el vivero de palmeras (B-46).

## ✈️ CONTEXTO DOMINANTE — VIAJE CONFIRMADO **7 al 23 DE AGOSTO** (fechas exactas, feedback 30/07)

- **feedback_text 30/07 (jh-hortensia-B5):** «Mi viaje va a ser del 7-23 de agosto. Actualiza esta y todas las otras pendientes de julio y agosto para recomendarme si conviene hacerlo antes o después del viaje». → **EJECUTADO 30/07**: jardin-hoy reordenada en **3 ventanas** con veredicto antes/después POR TAREA.
- **Las 3 ventanas (usar SIEMPRE hasta el 24/08):**
  - **Antes de irte (30/7–6/8) = 4 tareas.** Los 3 carozos (durazno B-30/35, ciruelo F-4, ciruela amarilla B-38): son los primeros en florecer, para el 23 ya arrancaron → podar después es tarde. + Hortensia B-5a/b a tierra (pelada y dormida no toma agua; plantarla a la vuelta = justo en brotación). **Si solo llega a una: el durazno.**
  - **Durante (7–23/8) = 0.** Dormancia + lluvia de agosto. **NO nagear NADA.**
  - **A la vuelta (24–31/8) = 11.** Todas tienen margen real: crespón B-9 y althea B-18 brotan en octubre; caqui B-41 es el último en despertar; hibisco B-4 conviene ATRASARLO (perenne + heladas tardías hasta fin de agosto); pitósporo B-43 reducción rebrota mejor con el empuje cerca; gardenia neem B-25-3 son 2-3 aplicaciones cada 7-10 días (inútil arrancarlo antes de irse); gardenia acidificar B-25, cerco B-7·11·31·33, abelia F-7 tienen su ventana en la última semana de agosto; podranea F-2 y hiedra B-15 sin reloj.
- **Corrección importante que salió de este repaso:** la **ciruela amarilla B-38** y el **pitósporo B-43-2** (reducción a 2-3 m) faltaban en la lista de agosto de jardin-hoy. Verificar SIEMPRE la lista contra `generate_tasks_from_plants(PLANTS)` + `task_states.json`, no contra la edición anterior de la página.
- **La gran poda NO es «mediados de agosto» este año** — con el viaje, la ventana real es **fin de agosto en adelante**, y horticulturalmente da igual o mejor para casi todo.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **cero-lectura / duelos binarios (esto-o-esto 28/07):** reacción meh + sub NO + «No es mi tipo de experiencia. Revisa lo del liquidámbar» = quiere SUSTANCIA y diálogo real, no gimmick sin contenido. MUERTO.
- **vos-decidis / feed-de-decisiones:** ganó 26/07 (sub sí) pero se fatigó en 3 días → 28/07 rejected + sub cancelada. El eje AGENCIA sigue vivo; el CONTENEDOR feed-de-decisiones repetido se quema. Rotar la agencia a formatos nuevos, no serializar el molde.
- **mi-objetivo (goal→plan):** rejected 27/07. La aspiración abstracta («más flor») sin acción inmediata NO convierte. NO re-servir «plan de tu objetivo».
- Otros muertos: role-play verboso · anticipación/countdown (mi-primavera, cuenta-regresiva) · app pasiva · editorial 3ª pers · ESPACIAL/mapa/orientación · gesto solo · mística · nota-larga · superlativo · racha/streak · biografías · chat-coral · dinero/tasación (mercado-pases) · alivio-PASIVO vacío · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **SUSTANCIA > gimmick (regla #1).** Lo que MÁS pesa: ayuda contextual REAL de SU jardín. El thread del liquidámbar (preguntó altura de corte, le di poda de reducción paso a paso) es el pico de engagement — y el usuario lo cita como referencia («revisa lo del liquidámbar»). El contenido real gana al contenedor.
- **Minimalismo + REAL + VISUAL.** Poco texto, glanceable, garden-close. **FOTOS REALES = NEED validado** (pedido explícito 28/07: «incluime foto de la especie así sé cuál es»). Usarlas siempre que se pueda.
- **Agencia/decisión** sigue siendo eje fuerte, pero rotar el contenedor (no >2-3 días el mismo molde).
- **feedback_text = ley.** Positivo = expandir. Negativo = NUNCA vuelve. Pedido = ejecutar YA. Sin señal activa = «masomenos», no cuenta como éxito.

## ⏱️ CADENCIA VIGENTE 30/07 (pedido directo del usuario — MÁXIMA AUTORIDAD): SEMANAL, día-consciente

**Total 5 push/semana. La corrida es día-consciente: encolá SOLO lo que toca ese día.**

| Día | Tarea (jardin-hoy) | Experiencia |
|---|---|---|
| **Lunes** | ✅ 10:00 | ✅ 18:00 |
| Mar / Mié / Vie / Dom | — | — |
| **Jueves** | ✅ 10:00 | — |
| **Sábado** | ✅ 10:00 | ✅ 11:00 |

- **Tareas = 3/sem** (Lun/Jue/Sáb 10:00): push `jardin-hoy` (`format:"tarea"`), refrescada.
- **Experiencias = 2/sem** (Lun 18:00, Sáb 11:00): **UNA sola push por slot**. Esa landing = **original NUEVA (protagonista) + experiencias YA APROBADAS agrupadas dentro (links)**. Nunca pushes separadas — si hay varias, una linkea a la otra.
- **Días sin slot:** mantenimiento (feedback/proposals/compactar/ledger/learnings), **0 push nuevas**.
- **Aprobación = recurrencia.** Una experiencia solo se re-manda si el usuario la **aprobó** (`engageApprove` → `status:"approved"`, se conserva la página). La original nueva SIEMPRE va (es el experimento), pero para VOLVER necesita aprobación. Pending sin aprobar **ya NO se borra el mismo día**: simplemente no recurre.
- **CTA nuevo = "slots disponibles"** (reemplaza suscripción diaria): cada experiencia muestra Lun 18:00 / Sáb 11:00 como opt-in (`<slug>-slot-lun18` / `<slug>-slot-sab11`).
- Cada experiencia: reacción + selector de slots + caja feedback propia + botones aprobar/rechazar + HTML pitch (6 modelos). send_at ≥60 min post-corrida. expires_at = mismo día 22:00 -03:00. Timestamps `-03:00`.
- **NO correr** gen_task_reminders / gen_top3 con --merge (canal tarea consolidado en jardin-hoy).

## 🆕 EXPERIENCIAS EN EL POOL (ciclo 60, 30/07) — ambas con CTA de slots, esperando aprobación

⚠️ **30/07 fue JUEVES = día tarea-only** con la cadencia nueva. Las 2 experiencias construidas hoy NO se pushearon (saqué `-a`/`-b` de la cola; jardin-hoy 10:00 sí salió). Quedan como **candidatas del pool** para el próximo slot de experiencia (**Sáb 01/08 11:00**). Ambas ya migradas al CTA de **slots disponibles** (Lun18/Sáb11):

- **🌱 `2026-07-30-se-multiplican-solos`**: PROPAGACIÓN gratis. Cast 100% fresco (B-12 cinta hijuelos, B-2 jazmín acodo —foto muestra B-2B/B-2C—, B-15 hiedra esqueje), fotos reales, cómo-hacerlo. Ángulo «sacale más a lo que ya tenés» = codicia sana + habilidad, NO trivia.
- **🛡️ `2026-07-30-aguantan-solos`**: TRANQUILIDAD de viaje CON PRUEBA biológica. Cast fresco (B-34 mandioca, B-42 pata de vaca, B-43 pitósporo), fotos reales. Honra el viaje SIN nagear; alivio con sustancia (nativa/dormancia/raíz), no alivio pasivo vacío.
- **SÁBADO 01/08 11:00:** slot de experiencia → **1 push**. Protagonista = una original NUEVA de cero (SIEMPRE) + linkear las aprobadas que haya. Si el usuario prende slots en alguna de estas dos, entran como recurrentes. Si no, la original nueva del sábado igual va.
- **WATCH:** ¿la sustancia+foto+cast-fresco convierte donde el gimmick murió? ¿prende algún slot? Si deja fechas exactas del viaje → plan de reentrada fin de agosto.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizar DESPUÉS. **Fun_facts ornamentales QUEMADOS → NO usar.** Tocar plantas por ÁNGULO NUEVO (tarea/estado/propagación/resistencia/decisión/interior/perenne).
- Planta featured descansa ≥7 días; ≥70% del cast sin usar en 7 días. Las usadas por tarea/decisión/propagación/resistencia real están exentas del criterio fun_fact.
- Re-push de promovida = contenido RENOVADO en la misma URL (jardin-hoy: editar el mismo archivo, subir la fecha).

## 📌 PEDIDOS DIRECTOS PREVIOS — NO PISAR

- **04/07:** 🕵️ Expedientes + Top 3 (`top3-tareas.html`) comisionadas/exentas — NO borrar página ni proposal (su push está fundido en jardin-hoy). ⚠️ Pillow NO viene en el runner: `pip install Pillow` antes de gen_*.py/build.py (solo si toco fuentes; hoy NO toqué fuentes → sin build).
- **23/07:** `tareas-pendientes.html` = página fija (no borrar/renombrar). Ya NO se pushea suelta (fundida en jardin-hoy).
- **Asamblea** (`2026-07-21-asamblea-jardin.html`), **tu-semana**, **vos-decidis** promovidas (no borrar aunque el molde esté fatigado).

## 📈 Estado del sistema + jardín (julio 2026)

- Push subscription device `pix9`: **active**. Logging por `/api/feedback` confiable.
- Jardín en DORMANCIA. ~55 días a primavera (equinoccio 23/09). Heladas tardías posibles hasta ~fin agosto (pican al SUR y ESTE al amanecer).
- **Decisiones del usuario (ejecutadas):** huerta→**muro norte** (en pausa hasta la vuelta) · arranque→**lechuga** (a la vuelta) · hortensia B-5a/b→**a tierra ANTES del viaje**; rincón: le recomendé el **sur junto a la pera B-39** (sombra fresca/húmeda) y quedó abierto a que elija fondo por comentario · liquidámbar B-37→**✅ HECHO 30/07** (avisó él: «Ya quedó hecho esto» → `task_states.json` marcado done) · caqui B-41 identidad→**observar** (plant-B-41-3 snoozed 15/11; ojo: la PODA plant-B-41 sigue activa, va a la vuelta) · gardenia B-25 neem→**a la vuelta** · **OBJETIVO DECLARADO = «más flor»**.
- **Pendientes reales al 30/07: 15.** 4 antes del viaje (B-30/35 durazno, F-4 ciruelo, B-38 ciruela amarilla, B-5a/b hortensia) + 11 a la vuelta (B-9 crespón, B-18 althea, B-41 caqui, B-43-2 pitósporo reducción, B-25-3 gardenia neem, B-4 hibisco, F-2 podranea, B-25 gardenia acidificar, B-7·11·31·33 cerco, B-15 hiedra, F-7 abelia).
- **30/07 (jueves) salieron 3 push de tarea** — las 2 de cadencia/pedido + **una extra a pedido explícito del usuario en chat** («revisá el feedback y mandame una push actualizando las tareas»): `2026-07-30-jardin-hoy-viaje` 15:45. Un pedido directo del usuario pisa la cadencia semanal.

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta va acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37/palto B-36/pileta (sol mañana) · oeste/frente = fotinias/ligustro F-9/fresno F-10 (sol tarde) · romero B-26 = única que florece en julio · limonero B-23 fruta 12/12 · **plantines de palta contra la pared a la sombra, SIN TOCAR** · B-12 cinta/B-15 hiedra/B-2 jazmín = fáciles de multiplicar · B-34 mandioca/B-42 pata de vaca/B-43 pitósporo = rústicas, toleran sequía · B-41 caqui identidad EN DUDA (snoozed 15/11) · B-45 sin id (snoozed 15/10).

## Conclusiones de los pushN (por feedback real)

- **29/07 (ciclo 59) — DÍA MASOMENOS, dos experiencias sin señal activa.** **los-que-no-duermen** (13:30, visual+fotos reales): abierta 23:08, dwell 15s, SIN voto/reacción/sub. **antes-de-irte** (18:00 dorado, checklist viaje): abierta 23:44, dwell 30s, SIN reacción/sub. Ambas abiertas de noche juntas → el usuario revisa tarde. Ninguna gatilló interacción → ambas **dropped**. **Lectura:** (1) abrir sin señal = el ángulo no ganó; (2) las FOTOS no son suficientes solas, hace falta sustancia+gancho de acción; (3) el eje viaje es real pero «checklist de prep» no engancha → probar viaje como TRANQUILIDAD, no como lista de deberes (→ aguantan-solos hoy).
- **28/07 (ciclo 58) — negativo.** esto-o-esto (duelos cero-lectura): sub NO + meh + «No es mi tipo» + rejected → cero-lectura MUERTO. vos-decidis v3: abierta 23:50 fuera de ventana + sub cancelada + rejected → molde fatigado. jardin-hoy: feedback_text RICO (cajas por tarea + fotos + defer lechuga) = el activo que MÁS le importa.
- **26/07 (ciclo 56):** vos-decidis GANÓ (sub sí + like + 116s) — pico del eje agencia, luego fatigado en 3 días.
- **24/07 (ciclo 54):** jardin-hoy GANADORA (3 feedback_text tier-1) + tu-semana sub «sí». Minimalismo + tareas reales + pedime-box.
- **21/07:** asamblea feedback «Está todo perfecto» (+ dato: llueve hace días, no pudo avanzar). Sustancia/foro de plantas + honestidad = bien.

## TODO / próximos experimentos

- Si aguantan-solos (tranquilidad+prueba) gana → serializar «el parte tranquilo del viaje» diario mientras esté afuera. · Si se-multiplican-solos gana → «una planta gratis por día» con foto rotando. · El eje MÁS fuerte sin explotar como formato: **ayuda contextual real estilo thread** (el liquidámbar) — una consulta profunda por día sobre SU jardín. · before/after con fotos reales del usuario. · Si deja fechas del viaje → plan de reentrada fin de agosto (poda por prioridad).
