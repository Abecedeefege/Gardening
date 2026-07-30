# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 📌📌 MANDATO DIRECTO DEL USUARIO 24/07 (chat + feedback_text — MÁXIMA AUTORIDAD, NO PISAR)

1. **UNA SOLA PUSH DIARIA PARA TAREAS, NO TRES.** El canal-tarea se consolida en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable). **NO encolar task-dia/pendientes/top3 sueltas** — su contenido va DENTRO de jardin-hoy. (NO corro gen_task_reminders/gen_top3 con --merge; jardin-hoy es la única push de tareas, mantenida a mano.)
2. **jardin-hoy lleva:** vistazo de 5 s (estado + 3 chips) + menús COLAPSADOS por mes + menú huerta + cajas de feedback POR TAREA (`engageFeedback('jh-<slug>')`) + fotos reales por tarea + caja «🙋 Pedime lo que necesites». Mantener menús actualizados con task_states + data_plants cada corrida y subir la fecha visible.
3. **CORRECCIÓN factual 24/07 (mantener):** plantines de **PALTA** contra la pared, a la sombra, **SIN MOVER**. Lo reubicado fue el vivero de palmeras (B-46).

## ✈️ CONTEXTO DOMINANTE 29/07 → fin agosto: EL USUARIO SE VA DE VIAJE

- **feedback_text 28/07 (jardin-hoy):** «ignora lo de la lechuga, me voy de viaje en 10 días, a mi vuelta a fin de agosto lo vemos». → **EJECUTADO:** lechuga/huerta EN PAUSA hasta la vuelta (fin ago); jardin-hoy en **modo viaje**; caqui B-41 snoozed 15/11 («caqui ignóralo hasta primavera» ✓); gardenia B-25 neem → a la vuelta.
- Desde ~7 de agosto se va ~3 semanas. Durante el viaje: **NO nagear tareas de afuera.** Invierno/dormancia = el jardín se banca solo. A la vuelta cae la gran poda de agosto + arranque de huerta.

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

## ⏱️ CADENCIA VIGENTE: 3 pushes/día = 1 tarea (jardin-hoy) + 2 experiencias nuevas

- **jardin-hoy** (canal-tarea, `format:"tarea"`): **10:00**. ÚNICA push de tareas.
- **2 experiencias nuevas de cero**: slots **13:30 / 18:00**. **18:00 = slot dorado.** Cada una: reacción + CTA sub diaria + caja feedback propia + botones aprobar/rechazar + HTML pitch con 6 modelos (3 innovadores + 3 ultra-creativos).
- Primer send_at ≥60 min post-corrida. expires_at = mismo día 22:00 -03:00. Timestamps `-03:00`. Cada notif a destino DISTINTO.

## 🆕 EXPERIENCIAS DE HOY (30/07, ciclo 60)

- **A · 🌱 `2026-07-30-se-multiplican-solos`** (13:30): PROPAGACIÓN gratis. Cast 100% fresco (B-12 cinta hijuelos, B-2 jazmín acodo —la foto muestra B-2B/B-2C—, B-15 hiedra esqueje), fotos reales, cómo-hacerlo real. Ángulo «sacale más a lo que ya tenés» = codicia sana + habilidad, NO trivia.
- **B · 🛡️ `2026-07-30-aguantan-solos`** (18:00 dorado): TRANQUILIDAD de viaje CON PRUEBA biológica. Cast fresco (B-34 mandioca, B-42 pata de vaca, B-43 pitósporo), fotos reales. Honra el viaje SIN nagear; alivio pero con sustancia (el porqué: nativa/dormancia/raíz), no alivio pasivo vacío.
- **WATCH 31/07:** ¿la sustancia+foto+cast-fresco convierte donde el gimmick murió? ¿el ángulo «plantas gratis» (A) o «paz mental de viaje» (B) gana reacción/sub? Si el usuario deja fechas exactas del viaje → afinar plan de reentrada fin de agosto.

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
- **Decisiones del usuario (ejecutadas):** huerta→**muro norte** (en pausa por viaje) · arranque→**lechuga** (a la vuelta) · hortensia B-5a/b→**a tierra** (falta rincón: sur vs fondo — se pregunta en jardin-hoy) · liquidámbar B-37→**lo poda el usuario** (thread resuelto: corte de reducción en bifurcación) · caqui B-41→**observar** (snoozed 15/11) · gardenia B-25 neem→**a la vuelta** · poda agosto→**por prioridad** · **OBJETIVO DECLARADO = «más flor»**.
- Tareas reales antes del viaje (día seco): Liquidámbar B-37 rama (la hace el usuario), Hortensia B-5a/b a tierra. AGOSTO (a la vuelta): gran poda fin de invierno (durazno B-30/35, ciruelo F-4, crespón B-9, althea B-18, hibisco B-4, podranea F-2, abelia F-7) + fines de ago (cerco B-7·11·31·33, hiedra B-15, acidificar gardenia B-25).

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
