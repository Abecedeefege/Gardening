# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 📌📌 MANDATO DIRECTO DEL USUARIO 24/07 (chat + feedback_text — MÁXIMA AUTORIDAD, NO PISAR)

1. **UNA SOLA PUSH DIARIA PARA TAREAS, NO TRES.** El canal-tarea se consolida en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable). **NO encolar task-dia/pendientes/top3 sueltas** — su contenido va DENTRO de jardin-hoy. (NO corro gen_task_reminders/gen_top3 con --merge; jardin-hoy es la única push de tareas, mantenida a mano.)
2. **jardin-hoy lleva:** vistazo de 5 s (estado + 3 chips) + menús COLAPSADOS por mes + menú huerta + caja «🙋 Pedime lo que necesites». Sin bloque de reacción/suscripción. Mantener menús actualizados con task_states + data_plants cada corrida.
3. **NUEVO pedido 28/07 EJECUTADO (29/07):** «Cada tarea debería tener una caja de feedback» → agregué **cajas de feedback POR TAREA** (`engageFeedback('jh-<slug>')`) en jardin-hoy. «Incluir foto de la especie» → agregué **fotos reales** por tarea (B-37 liquidámbar, gardenia). «mándame esto de nuevo» → jardin-hoy es la push 10:00.
4. **CORRECCIÓN factual 24/07 (mantener):** plantines de **PALTA** contra la pared, a la sombra, **SIN MOVER**. Lo reubicado fue el vivero de palmeras (B-46).

## ✈️ CONTEXTO DOMINANTE 29/07 → fin agosto: EL USUARIO SE VA DE VIAJE

- **feedback_text 28/07 (jardin-hoy):** «ignora lo de la lechuga, me voy de viaje en 10 días, a mi vuelta a fin de agosto lo vemos». → **EJECUTADO:** lechuga/huerta EN PAUSA hasta la vuelta (fin ago); jardin-hoy reencuadrado a **modo viaje**; caqui B-41 ya snoozed 15/11 (pedido: «caqui ignóralo hasta primavera» ✓).
- Durante el viaje: NO nagear tareas de afuera. Invierno/dormancia = jardín se banca 3 semanas solo. A la vuelta cae justo la gran poda de agosto + arranque de huerta.

## 🚫 EJES/FORMATOS MUERTOS (feedback duro — NO volver, ni variaciones)

- **cero-lectura / duelos binarios (esto-o-esto 28/07):** reacción meh + sub NO + feedback «No es mi tipo de experiencia. Revisa lo del liquidámbar» = quiere SUSTANCIA y diálogo real (estilo thread liquidámbar), no toques-gimmick sin contenido. MUERTO.
- **vos-decidis (feed-de-decisiones):** ganó 26/07 (sub sí) pero se FATIGÓ en 3 días → 28/07 sub CANCELADA + rejected, abierta 23:50 fuera de ventana. El eje AGENCIA sigue vivo; el CONTENEDOR feed-de-decisiones repetido se quema rápido. Rotar la agencia a formatos nuevos, no serializar el mismo molde.
- Otros muertos previos: role-play verboso · anticipación/countdown (mi-primavera) · app pasiva · editorial 3ª pers · ESPACIAL/mapa/orientación · gesto solo · mística repetida · nota-larga · superlativo-fatigado · racha/streak · biografías · chat-coral · dinero/tasación (mercado-pases) · alivio-pasivo · Wrapped · fútbol · **mucho texto/cargado** (queja 23/07).

## 🚀 QUÉ CONVIERTE — meta-reglas vigentes

- **Agencia/decisión/autoridad = eje #1 (dato duro).** El usuario decide o logra. Loop de ejecución (mostrarle lo cumplido) refuerza el hábito. PERO: rotar el CONTENEDOR, no repetir el mismo formato >2-3 días.
- **Minimalismo + REAL + VISUAL gana.** Poco texto, glanceable, garden-close, dato/foto REAL. Nada de trivia ni prosa densa.
- **feedback_text = ley.** Positivo = expandir. Negativo = NUNCA vuelve. Pedido = ejecutar YA. Sin señal activa = «masomenos», no cuenta como éxito.
- **Sustancia > gimmick.** El usuario valora ayuda contextual real de SU jardín (ver threads: liquidámbar, guayabo). Las experiencias que le hablan de su jardín con acciones reales pesan más que juegos.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día = 1 tarea (jardin-hoy) + 2 experiencias nuevas

- **jardin-hoy** (canal-tarea, `format:"tarea"`): **10:00**. ÚNICA push de tareas.
- **2 experiencias nuevas de cero**: slots **13:30 / 18:00**. **18:00 = slot dorado → el MAYOR convertidor del día.** Cada una: reacción + CTA sub diaria + caja feedback propia + botones aprobar/rechazar + HTML pitch con 6 modelos (3 innovadores + 3 ultra-creativos).
- Primer send_at ≥60 min post-corrida. expires_at = mismo día 22:00 -03:00. Timestamps `-03:00`. Cada notif a destino DISTINTO.

## 🆕 EXPERIENCIAS DE HOY (29/07, ciclo 59)

- **A · ✈️ `2026-07-29-antes-de-irte`** (18:00 dorado): honra el feedback directo del viaje. Checklist calmada de 4 pasos (barra de progreso) + cuenta regresiva diaria opcional. Ancla en dormancia real (invierno = fácil dejar solo). Cast: interior I-1/I-2 (riego/ausencia) + liquidámbar B-37 (día seco antes de irse). Vende TRANQUILIDAD = agencia sobre lo controlable, timing perfecto.
- **B · 🌿 `2026-07-29-los-que-no-duermen`** (13:30): FORMATO NUEVO (feed visual con **FOTOS REALES inline** — primer engage con fotos de plantas). 3 cartas: Singonio I-1, Difenbaquia I-2, Evónimo B-44 (cast descansado ≥10 d) — las plantas ACTIVAS en invierno. Voto «cuál te alegra más» (agencia low-friction + dato de gusto). Ataca la temporada muerta y responde el pedido «fotos para saber cuál es cuál».
- **WATCH 30/07:** ¿el visual+real (fotos) convierte donde el texto y los gestos-gimmick murieron? ¿la experiencia de VIAJE (escuchar el dato exacto) gana reacción/sub? Procesar: `los-que-no-duermen-favorita` (gusto de invierno) + `antes-de-irte-check-*` (qué prep hizo) + fechas exactas del viaje si las deja → afinar cuenta regresiva y plan de reentrada.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizar DESPUÉS. **Fun_facts ornamentales QUEMADOS → NO usar.** Tocar plantas por ÁNGULO NUEVO (tarea/estado/floración/interior/perenne-invernal/decisión/objetivo).
- Planta featured descansa ≥7 días; ≥70% del cast sin usar en 7 días. Las usadas por tarea/decisión real están exentas del criterio fun_fact.
- Re-push de promovida = contenido RENOVADO en la misma URL (jardin-hoy: editar el mismo archivo, subir la fecha).

## 📌 PEDIDOS DIRECTOS PREVIOS — NO PISAR

- **04/07:** 🕵️ Expedientes + Top 3 (`top3-tareas.html`) comisionadas/exentas — NO borrar página ni proposal (su push está fundido en jardin-hoy). ⚠️ Pillow NO viene en el runner: `pip install Pillow` antes de gen_*.py/build.py (solo si toco fuentes).
- **23/07:** `tareas-pendientes.html` = página fija (no borrar/renombrar). Ya NO se pushea suelta (fundida en jardin-hoy).
- **Asamblea** (`2026-07-21-asamblea-jardin.html`) y **tu-semana** promovidas (recap semanal domingos, solo tareas realmente cerradas).

## 📈 Estado del sistema + jardín (julio 2026)

- Push subscription device `pix9`: **active**. Logging por `/api/feedback` confiable.
- Jardín en DORMANCIA. ~55 días a primavera (equinoccio 23/09). Heladas tardías posibles hasta ~fin agosto (pican al SUR y ESTE al amanecer).
- **Decisiones del usuario (ejecutadas):** huerta→**muro norte** (en pausa por viaje) · huerta arranque→**lechuga** (a la vuelta) · hortensia B-5a/b→**a tierra** (falta rincón: sur vs fondo — pendiente, se pregunta en jardin-hoy) · liquidámbar B-37→**lo poda el usuario** · caqui B-41→**observar** (snoozed 15/11) · gardenia B-25 neem→**a la vuelta** · poda agosto→**por prioridad** · **OBJETIVO DECLARADO = «más flor»**.
- Tareas reales JULIO (activas antes del viaje, día seco): Liquidámbar B-37 rama (la hace el usuario), Hortensia B-5a/b a tierra. En pausa: huerta, Gardenia B-25. AGOSTO (a la vuelta): gran poda fin de invierno (durazno B-30/35, ciruelo F-4, crespón B-9, althea B-18, caqui B-41, hibisco B-4, podranea F-2, abelia F-7) + fines de ago (cerco B-7·11·31·33, hiedra B-15, acidificar gardenia B-25).
- **HUERTA (muro norte, en pausa):** al volver (fin ago/sept): lechuga, cebolla. Luego: tomate, morrón, acelga, rúcula, zanahoria, perejil, cilantro. Sept-oct: zapallito, albahaca.

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta va acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37/palto B-36/pileta (sol mañana) · oeste/frente = fotinias/ligustro F-9/fresno F-10 (sol tarde) · romero B-26 = única que florece en julio · limonero B-23 fruta 12/12 · **plantines de palta contra la pared a la sombra, SIN TOCAR** · Singonio I-1/Difenbaquia I-2 = interior, riego cada 14 d en invierno · Evónimo B-44 = perenne, color plateado invernal · B-41 caqui identidad EN DUDA (snoozed 15/11).

## Conclusiones de los pushN (por feedback real)

- **28/07 (ciclo 58) — DÍA NEGATIVO, dos muertes claras.** **esto-o-esto** (13:30, duelos cero-lectura): respondió los 5 duelos PERO sub NO + reacción meh + feedback «No es mi tipo de experiencia» + rejected → formato cero-lectura MUERTO, quiere sustancia. **vos-decidis v3** (18:00 dorado): abierta 23:50 (fuera de ventana) + sub CANCELADA + rejected → serie fatigada, el molde feed-de-decisiones se quemó. **jardin-hoy:** feedback_text RICO (cajas por tarea + fotos + defer lechuga por viaje) = el usuario invierte en mejorarlo → es el activo que MÁS le importa. **Lectura 29/07:** (1) ejecutar TODO el feedback de jardin-hoy; (2) rotar la agencia a formatos NUEVOS (visual+real, viaje); (3) el viaje como eje del día.
- **27/07 (ciclo 57):** vos-decidis v2 leyó 100% pero respondió 1/4 (fatiga de 4 decisiones), sin conversión. mi-objetivo: «flor» dominante pero sin sub (aspiración sin acción inmediata no convierte).
- **26/07 (ciclo 56):** vos-decidis GANÓ (sub sí + like + 116s) — pico del eje agencia, luego fatigado. mi-primavera rejected (anticipación muerta).
- **24/07 (ciclo 54):** jardin-hoy GANADORA (3 feedback_text tier-1) + tu-semana sub «sí». Minimalismo + tareas reales + pedime-box.
- **23/07 (ciclo 53):** doble rechazo role-play + «mucho texto, muy cargado». Mató teatro verboso y dinero/tasación.

## TODO / próximos experimentos

- Si los-que-no-duermen (visual+fotos) convierte → serializar «quién brilla hoy» con foto real rotando. · Si antes-de-irte gana → cuenta regresiva diaria del viaje + plan de reentrada para fin de agosto. · before/after con fotos reales del usuario. · Explorar el eje «ayuda contextual real de SU jardín» (estilo threads) como formato de experiencia.
