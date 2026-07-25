# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 📌📌 MANDATO DIRECTO DEL USUARIO 24/07 (chat + feedback_text — MÁXIMA AUTORIDAD, NO PISAR)

1. **UNA SOLA PUSH DIARIA PARA TAREAS, NO TRES.** «Estos TRES push [task-dia + pendientes + top3] deberían haber sido UNA comunicación». → El canal-tarea se consolida en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable). **NO encolar task-dia/pendientes/top3 como pushes separados** — su contenido va DENTRO de jardin-hoy. (Aplicado desde 25/07: NO corrí gen_task_reminders/gen_top3 con --merge; jardin-hoy es la única push de tareas, mantenida a mano.)
2. **La landing lleva:** vistazo de 5 s (estado + 3 chips) + menú COLAPSADO «Tareas de julio» + menú COLAPSADO «Para agosto» + caja **«🙋 Pedime lo que necesites»**. Sin bloque de reacción/suscripción/«¿la dejo fija?» (ya es core, no experimento). Mantener menús por mes actualizados con task_states + data_plants cada corrida.
3. **Feedback posterior 24/07 (ejecutado el 25/07):**
   - «¿Qué puedo hacer hoy?» → jardin-hoy ahora abre con una **acción a prueba de lluvia para HOY** (definir la huerta, se hace adentro). No dejar al usuario sin algo accionable en días de lluvia.
   - «¿Justo 3 tareas en cada módulo? ¿Nada más?» → NO capar a 3. Julio son 4 reales (+huerta); **agosto son 12** (la gran poda de fin de invierno). Mostrar el número real, con nota de que son «todas».
   - «Agregame una tarea: definir plantas para huerta y proponeme sugerencias» → **EJECUTADO**: tarea «Definir plantas para la huerta» en jardin-hoy + experiencia dedicada **`2026-07-25-mi-huerta`** con sugerencias por época (datos del calendario HUERTA del catálogo).
4. **CORRECCIÓN factual 24/07 (tu-semana):** «Los plantines de PALTA no los toqué, siguen contra la pared a la sombra». → tu-semana afirmaba de más sobre el vivero. **CORREGIDO** en la página. **HECHO VERIFICADO (no contradecir):** los plantines de palta están contra la pared, a la sombra, SIN MOVER. Lo que sí se reubicó fue el vivero de palmeras (B-46).

## ✅ PIVOTE MINIMALISTA — VALIDADO (24/07, confirmado tier-1)

- **jardin-hoy (minimalista, glanceable, poco texto) = 3 feedback_text el mismo día + clicks repetidos + revisitas.** El formato liviano/garden-close es EL camino. El usuario vuelve, lee y ESCRIBE. Máxima señal.
- **Contraste 23/07: role-play verboso (mercado-pases/ronda-medica) = RECHAZO + «mucho texto, muy cargado».** Muerto y enterrado. NO volver a: médico/DT/presidente/juez/farándula, prosa densa, metáforas rebuscadas, walls de texto.
- **tu-semana (recap de logros) = suscripción «sí» (tier-2)** + la corrección de palta. Ángulo RECAP-DE-LOGROS (héroe=usuario, orgullo) VALIDADO → PROMOVIDO como resumen semanal (domingos), sin competir con la push diaria. Cuidar credibilidad: SOLO tareas realmente cerradas en task_states.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día = 1 tarea (jardin-hoy) + 2 experiencias nuevas

- **jardin-hoy** (canal-tarea consolidado, `format:"tarea"`): **10:00**. Absorbe estado + tareas. Es la ÚNICA push de tareas del día (ya NO task-dia/pendientes/top3 sueltas).
- **2 experiencias nuevas de cero** (función paralela, persona product/UX/growth/sales): slots **13:30 / 18:00** (18:00 = slot dorado histórico → la de mayor conversión ahí). Cada una: reacción + CTA sub diaria + caja feedback propia + botones aprobar/rechazar + HTML de pitch con 6 modelos (3 innovadores + 3 ultra-creativos).
- **🚫 PISO 10:00.** Primer send_at ≥60 min post-corrida. expires_at = mismo día 22:00 -03:00. Timestamps con `-03:00`. Cada notif a destino DISTINTO.
- Nota: bajé de los ~4-5 pushes/día previos (con task-dia+pendientes+top3 sueltos) a estos 3 limpios. Es exactamente el reclamo del usuario resuelto.

## 🆕 EXPERIENCIAS DE HOY (25/07, ciclo 55) — 2 nuevas de cero

- **A · 🧭 `2026-07-25-mapa-solar`** (13:30): mapa TOCABLE de orientación (compás de 4 zonas: norte cálido / oeste-frente sol de tarde / este-fondo sol de mañana / sur sombrío). Formato NUEVO (espacial, nunca probado) + ángulo FRESCO (orientación, 0 fun_facts) + agencia (tocás y decidís). Ata a dónde poner la huerta y qué proteger de la helada. Hipótesis: valida la capa espacial (feature más pedida).
- **B · 🥬 `2026-07-25-mi-huerta`** (18:00, slot dorado): guía de decisión de huerta. Responde el PEDIDO TEXTUAL directo. Agencia (elegís dónde + qué) + datos reales del calendario HUERTA + a prueba de lluvia. Cast 100% fresco (hortalizas). **Debería ser la de mayor conversión — lo pidió con todas las letras.**
- **WATCH 26/07:** ¿mi-huerta convierte (era pedido explícito)? ¿mapa-solar valida lo espacial/tocable? Si mi-huerta gana → serializar «calendario vivo de huerta». Si mapa-solar gana → invertir en mapa real con plantas ubicadas.

## 🚫 ANTI-REPETICIÓN (reclamo 18/07: «me repetís los mismos funfacts»)

- Leer `facts_ledger.json` ANTES, actualizar DESPUÉS. **Elenco de fun_facts ornamentales QUEMADO** (una mega-experiencia tocó casi todas las plantas <7d). → NO usar fun_facts. Tocar plantas por **ÁNGULO NUEVO** (tarea / estado / orientación / huerta), nunca por su dato curioso.
- mapa-solar usa plantas como LANDMARKS por orientación (no fun_fact). mi-huerta usa hortalizas (cast nuevo, fuera del ledger de ornamentales). Ambas cumplen el espíritu.
- Re-push de promovida = contenido RENOVADO en la misma URL (jardin-hoy: editar el mismo archivo, subir la fecha visible).

## 📌 PEDIDOS DIRECTOS PREVIOS — NO PISAR

- **04/07:** 🕵️ Expedientes (`2026-07-04-expedientes-jardin.html`) comisionada, exenta. B-41 caqui identidad EN DUDA. 🎯 Top 3 (`top3-tareas.html`) — la DATA sigue viva pero su push se fundió en jardin-hoy (mandato 24/07). NO borrar página ni proposal. Splash «Hora dorada» integrado (demos = referencia, no tocar). ⚠️ Pillow no viene: `pip install Pillow` antes de gen_*.py/build.py.
- **23/07:** `tareas-pendientes.html` = página fija (no borrar/renombrar). Ahora es DETALLE complementario; el vistazo diario pasó a jardin-hoy (nota actualizada en la página, 25/07). Ya NO se pushea suelta.
- **Asamblea** (`2026-07-21-asamblea-jardin.html`) promovida (feedback_text positivo).

## 🚀 QUÉ CONVIERTE — meta-reglas

- **HÉROE = USUARIO + AGENCIA/AUTORIDAD/LOGRO/DECISIÓN.** Consumo pasivo NO convierte (22/07: lluvia-tareas y grupo-jardin murieron por pasivos). El usuario tiene que DECIDIR o LOGRAR algo.
- **Minimalismo gana** (24/07 validado): poco texto, paleta clara, glanceable, garden-close, dato REAL (estado/logro/tarea/orientación/huerta). NADA de trivia ni prosa.
- **Las TAREAS y los PEDIDOS EXPLÍCITOS son el canal más fiable.** Cuando el usuario pide algo por texto, ejecutarlo ES la mejor experiencia posible.
- **feedback_text = ley.** Positivo = expandir. Negativo = NUNCA vuelve. Pedido = ejecutar YA. Sin señal activa = «masomenos», no cuenta como éxito.
- **MUERTOS (no volver):** role-play verboso/teatral · countdown/anticipación · app pasiva · editorial pasivo 3ª pers · gesto solo · mística repetida · nota-larga · superlativo-fatigado · racha/streak · biografías · chat-coral · dinero/tasación · alivio-pasivo · Wrapped (fatigado) · fútbol (Mundial + mercado-pases doblemente muerto).

## 📈 Estado del sistema + jardín (julio 2026)

- Push subscription device `pix9`: **active** (25/07). Logging por `/api/feedback` confiable.
- **Contexto lluvia (21/07→):** sigue lloviendo en MVD, usuario no puede salir a podar/tocar tierra mojada. NO nagear. Ofrecer SIEMPRE una acción a prueba de lluvia (definir huerta, planificar, decidir). La lluvia es real: no inventar urgencias afuera.
- Jardín en DORMANCIA. ~60 días a primavera (equinoccio 23/09). Heladas tardías posibles hasta ~fin agosto (pican al SUR y ESTE al amanecer → mapa-solar lo usa como ancla real).
- Tareas reales JULIO (4): huerta (pedido), Hortensia B-5a/b trasplante (alta), Liquidámbar B-37 rama (alta), Gardenia B-25 pulgones/hormigas (alta). AGOSTO (12): gran poda de fin de invierno cuando hinchen las yemas (durazno B-30/35, ciruelo F-4, crespón B-9, althea B-18, caqui B-41, hibisco B-4, podranea F-2, abelia F-7, B-4) + fines de ago (cerco B-7·11·31·33, hiedra B-15, acidificar gardenia B-25). ✅ Guayabo F-1 limpieza cerrada 23/07.
- **HUERTA (calendario del catálogo):** sembrar YA (jul): lechuga, cebolla. Arranca agosto: tomate, morrón, acelga, rúcula, zanahoria, perejil, cilantro. Sept-oct: zapallito, albahaca. Sol: frente (oeste) o muro norte = mejores (6h+). Fondo (este) = solo mañana, hojas de media sombra.

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo, sol todo el invierno) · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37/palto B-36/pileta (sol mañana) · oeste/frente = fotinias/ligustro F-9/fresno F-10 (sol tarde) · romero B-26 = única que florece en julio · limonero B-23 fruta 12/12 · **plantines de palta contra la pared a la sombra, SIN TOCAR** (aclaración usuario 24/07) · B-41 caqui identidad EN DUDA.

## Conclusiones de los pushN (por feedback real)

- **24/07 (ciclo 54) — jardin-hoy GANADORA (3 feedback_text tier-1) + tu-semana sub «sí».** El minimalismo + tareas reales + pedime-box = el usuario vuelve y escribe. Ejecuté sus 3 pedidos el 25/07. tu-semana promovida (recap semanal) con la palta corregida.
- **25/07 (ciclo 55) — Cola limpia (3): 10:00 jardin-hoy (consolidada, +huerta +agosto expandido +acción-de-hoy) · 13:30 mapa-solar (espacial/orientación) · 18:00 mi-huerta (pedido explícito).** Cero pushes de tareas sueltas: reclamo del usuario resuelto.
- **23/07 (ciclo 53):** doble rechazo role-play + feedback tier-1 «mucho texto». Mató el teatro verboso.
- **08-10/07:** tanda ganadora (Entrevista, Quiz, Wrapped, Álbum → 4 promovidas). **11-20/07:** racha de fallos (pasivo/mística/nota-larga/celebridad/racha/biografías); único sostenido = canal-tarea.

## TODO / próximos experimentos livianos (aún sin probar)

- before/after con fotos reales del usuario · una sola foto grande + 3 palabras · mapa del jardín REAL con cada planta ubicada (si mapa-solar valida lo espacial) · calendario vivo de huerta (si mi-huerta valida) · reordenar tareas de agosto por prioridad / plan por fin de semana (ofrecido en jardin-hoy — si el usuario lo pide, ejecutar).
