# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 📌📌 MANDATO DIRECTO DEL USUARIO 24/07 (chat + feedback_text — MÁXIMA AUTORIDAD, NO PISAR)

1. **UNA SOLA PUSH DIARIA PARA TAREAS, NO TRES.** «Estos TRES push [task-dia + pendientes + top3] deberían haber sido UNA comunicación». → El canal-tarea se consolida en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable). **NO encolar task-dia/pendientes/top3 como pushes separados** — su contenido va DENTRO de jardin-hoy. (Aplicado desde 25/07: NO corro gen_task_reminders/gen_top3 con --merge; jardin-hoy es la única push de tareas, mantenida a mano.)
2. **La landing lleva:** vistazo de 5 s (estado + 3 chips) + menú COLAPSADO «Tareas de julio» + menú COLAPSADO «Para agosto» + menú «🥬 huerta» + caja **«🙋 Pedime lo que necesites»**. Sin bloque de reacción/suscripción/«¿la dejo fija?» (ya es core). Mantener menús por mes actualizados con task_states + data_plants cada corrida.
3. **Feedback 24/07 EJECUTADO y mantenido:** «¿Qué puedo hacer hoy?» → jardin-hoy abre con acción a prueba de lluvia. «¿Justo 3 tareas?» → NO capar (julio 4, agosto 12, número real). «Definir huerta + sugerencias» → menú huerta inline (deep-link #huerta).
4. **CORRECCIÓN factual 24/07:** los plantines de **PALTA** están contra la pared, a la sombra, **SIN MOVER** (HECHO VERIFICADO). Lo reubicado fue el vivero de palmeras (B-46).

## ✅ EJE VALIDADO CON DATO DURO: AGENCIA/DECISIÓN (24→26/07)

- **vos-decidis (feed de DECISIONES reales) = ÚNICA variante que convirtió a SUSCRIPCIÓN.** 26/07: respondió las 5, sub diaria **SÍ**, reacción like, 116s/100%. HÉROE=USUARIO+AUTORIDAD gana.
- **jardin-hoy (minimalista/glanceable) = 3 feedback_text tier-1 el 24/07.** El formato liviano garden-close es el core del canal-tarea.
- **mi-primavera (ANTICIPACIÓN/recompensa) REJECTED 27/07** (sub «no» + rejected). Confirma: «elegí un futuro» NO convierte sin acción inmediata que el usuario controle.
- **Serializar ganadores que el usuario SUSCRIBIÓ ≠ refrito.** La sub «sí» es un pedido de versión fresca diaria → hay que cumplirla con contenido nuevo en la misma familia (loop de ejecución: mostrar lo de ayer ya hecho).

## ⏱️ CADENCIA VIGENTE: 3 pushes/día = 1 tarea (jardin-hoy) + 2 experiencias nuevas

- **jardin-hoy** (canal-tarea consolidado, `format:"tarea"`): **10:00**. ÚNICA push de tareas (ya NO task-dia/pendientes/top3 sueltas).
- **2 experiencias nuevas de cero** (persona product/UX/growth/sales): slots **13:30 / 18:00**. **18:00 = slot dorado → ahí va el MAYOR convertidor** (hoy el ganador serializado vos-decidis; el experimento nuevo a 13:30). Cada una: reacción + CTA sub diaria + caja feedback propia + botones aprobar/rechazar + HTML pitch con 6 modelos (3 innovadores + 3 ultra-creativos).
- **🚫 PISO 10:00.** Primer send_at ≥60 min post-corrida. expires_at = mismo día 22:00 -03:00. Timestamps con `-03:00`. Cada notif a destino DISTINTO.

## 🆕 EXPERIENCIAS DE HOY (27/07, ciclo 57)

- **A · 🌿 `2026-07-27-vos-decidis`** (18:00 dorado): SERIALIZACIÓN del ganador. Abre con RECAP de las 5 decisiones de ayer YA EJECUTADAS (loop de ejecución = prueba de que los taps mueven cosas) + 4 decisiones nuevas (arranque huerta muro norte, rincón hortensia, plantines palta, destino vivero B-46). Ángulo DECISIÓN/tarea.
- **B · 🎯 `2026-07-27-mi-objetivo`** (13:30): FORMATO NUEVO (nunca probado). Objetivo→plan: el usuario declara un resultado (🌸 más flor / 🥗 primera cosecha / 🌳 sombra / 🦋 fauna) y genero un plan de 3 pasos con plantas reales. Extiende la agencia de «elegí la acción» a «declará el destino».
- **WATCH 28/07:** ¿la sub diaria de vos-decidis se sostiene con el loop de ejecución (sube a 😍)? ¿mi-objetivo (declarar resultado) convierte como vos-decidis (elegir acción), o la agencia necesita accionabilidad inmediata y no aspiración? Procesar los `answer`: `mi-objetivo-goal`/`mi-objetivo-elegido` (qué objetivo prioriza) y `vd2-*` (arranque huerta, rincón hortensia, palta, vivero) → ejecutar en contenido.

## 🚫 ANTI-REPETICIÓN

- Leer `facts_ledger.json` ANTES, actualizar DESPUÉS. **Elenco de fun_facts ornamentales QUEMADO → NO usar fun_facts.** Tocar plantas por ÁNGULO NUEVO (tarea/estado/floración/orientación/huerta/decisión/objetivo).
- Planta featured descansa ≥7 días; ≥70% del cast sin usar en 7 días. Las plantas usadas por decisión/tarea/objetivo real están exentas del criterio fun_fact. mi-objetivo usa cast mayormente descansado (B-1, B-7, B-16, B-29, B-40, F-8 ≥7d).
- Re-push de promovida = contenido RENOVADO en la misma URL/familia (jardin-hoy: editar el mismo archivo, subir la fecha; vos-decidis: nueva fecha con recap+decisiones nuevas).

## 📌 PEDIDOS DIRECTOS PREVIOS — NO PISAR

- **04/07:** 🕵️ Expedientes (`2026-07-04-expedientes-jardin.html`) comisionada, exenta. Top 3 (`top3-tareas.html`) DATA viva pero su push fundido en jardin-hoy — NO borrar página ni proposal. ⚠️ Pillow no viene en el runner: `pip install Pillow` antes de gen_*.py/build.py (solo si toco fuentes).
- **23/07:** `tareas-pendientes.html` = página fija (no borrar/renombrar). Ya NO se pushea suelta (fundida en jardin-hoy).
- **Asamblea** (`2026-07-21-asamblea-jardin.html`) promovida. **tu-semana** promovida (recap semanal domingos, solo tareas realmente cerradas).

## 🚀 QUÉ CONVIERTE — meta-reglas

- **Agencia/decisión/autoridad = eje #1 (dato duro).** El usuario tiene que DECIDIR o LOGRAR. Loop de ejecución (mostrarle lo cumplido) refuerza el hábito.
- **Minimalismo gana:** poco texto, glanceable, garden-close, dato REAL. NADA de trivia ni prosa densa (feedback 23/07: «mucho texto, muy cargado, no es lo que busco»).
- **feedback_text = ley.** Positivo = expandir. Negativo = NUNCA vuelve. Pedido = ejecutar YA. Sin señal activa = «masomenos», no cuenta.
- **MUERTOS (no volver):** role-play verboso · **anticipación/countdown (mi-primavera 27/07 = confirmación)** · app pasiva · editorial 3ª pers · ESPACIAL/mapa/orientación (mapa-solar 25/07) · gesto solo · mística repetida · nota-larga · superlativo-fatigado · racha/streak · biografías · chat-coral · dinero/tasación (mercado-pases 23/07) · alivio-pasivo · Wrapped · fútbol.

## 📈 Estado del sistema + jardín (julio 2026)

- Push subscription device `pix9`: **active** (26/07). Logging por `/api/feedback` confiable.
- **Contexto lluvia (21/07→):** feedback 21/07 «está lloviendo hace días, no pude avanzar». NO nagear tareas de afuera. Ofrecer SIEMPRE acción a prueba de lluvia (definir/sembrar huerta, decidir, planificar).
- Jardín en DORMANCIA. ~58 días a primavera (equinoccio 23/09). Heladas tardías posibles hasta ~fin agosto (pican al SUR y ESTE al amanecer).
- **Decisiones del usuario 26/07 (ejecutadas en contenido):** huerta→**muro norte** · hortensia B-5a/b→**a tierra** (falta rincón) · liquidámbar B-37→**lo poda el usuario** · caqui B-41→**observar** (snoozed 15/11) · poda agosto→**por prioridad**.
- Tareas reales JULIO (4): huerta (muro norte, sembrar lechuga/cebolla), Hortensia B-5a/b a tierra (alta), Liquidámbar B-37 rama (alta, la hace el usuario), Gardenia B-25 pulgones/hormigas (alta). AGOSTO (12): gran poda fin de invierno (durazno B-30/35, ciruelo F-4, crespón B-9, althea B-18, caqui B-41, hibisco B-4, podranea F-2, abelia F-7) + fines de ago (cerco B-7·11·31·33, hiedra B-15, acidificar gardenia B-25). ✅ Guayabo F-1 cerrado 23/07.
- **HUERTA (muro norte, inline en jardin-hoy):** sembrar YA (jul): lechuga, cebolla. Agosto: tomate, morrón, acelga, rúcula, zanahoria, perejil, cilantro. Sept-oct: zapallito, albahaca.

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo), mejor sol de invierno → huerta va acá · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37/palto B-36/pileta (sol mañana) · oeste/frente = fotinias/ligustro F-9/fresno F-10 (sol tarde) · romero B-26 = única que florece en julio · limonero B-23 fruta 12/12 · **plantines de palta contra la pared a la sombra, SIN TOCAR** · B-41 caqui identidad EN DUDA (nunca flor ni fruto; snoozed 15/11, en observación).

## Conclusiones de los pushN (por feedback real)

- **26/07 (ciclo 56) — vos-decidis GANA claro.** vos-decidis (13:30→sent 16:34): 5 decisiones respondidas + sub diaria **SÍ** + like + 116s = única conversión del ciclo. mi-primavera (18:00 dorado): solo prioridades + sub **no** + **rejected** → anticipación muerta. jardin-hoy: sent, sin click nuevo (core, masomenos). Lectura: DOBLAR la apuesta a agencia/decisión, serializar vos-decidis con loop de ejecución; retirar anticipación.
- **24/07 (ciclo 54) — jardin-hoy GANADORA (3 feedback_text tier-1) + tu-semana sub «sí».** Minimalismo + tareas reales + pedime-box.
- **25/07 (ciclo 55) — plano.** mapa-solar rebotó (eje ESPACIAL muerto), mi-huerta leyó 76s pero sin señal (contenido serializado en jardin-hoy). Un día temático plano → pivote a agencia.
- **23/07 (ciclo 53):** doble rechazo role-play + «mucho texto, muy cargado». Mató teatro verboso y dinero/tasación.

## TODO / próximos experimentos

- Si mi-objetivo convierte → serializar «un objetivo por día» con seguimiento. · Si vos-decidis sostiene sub con loop de ejecución → mantener el recibo como apertura fija. · before/after con fotos reales del usuario · plan de agosto por fin de semana (si lo pide en vos-decidis/jardin-hoy) · «hacelo por mí»/cotización de jardinero embebida (del pitch).
