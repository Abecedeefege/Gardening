# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 📌📌 MANDATO DIRECTO DEL USUARIO 24/07 (chat + feedback_text — MÁXIMA AUTORIDAD, NO PISAR)

1. **UNA SOLA PUSH DIARIA PARA TAREAS, NO TRES.** «Estos TRES push [task-dia + pendientes + top3] deberían haber sido UNA comunicación». → El canal-tarea se consolida en **🌤️ «Tu jardín hoy»** (`2026-07-24-jardin-hoy.html`, PROMOVIDA, URL estable). **NO encolar task-dia/pendientes/top3 como pushes separados** — su contenido va DENTRO de jardin-hoy. (Aplicado desde 25/07: NO corro gen_task_reminders/gen_top3 con --merge; jardin-hoy es la única push de tareas, mantenida a mano.)
2. **La landing lleva:** vistazo de 5 s (estado + 3 chips) + menú COLAPSADO «Tareas de julio» + menú COLAPSADO «Para agosto» + caja **«🙋 Pedime lo que necesites»**. Sin bloque de reacción/suscripción/«¿la dejo fija?» (ya es core, no experimento). Mantener menús por mes actualizados con task_states + data_plants cada corrida.
3. **Feedback posterior 24/07 (ejecutado 25/07, mantenido 26/07):**
   - «¿Qué puedo hacer hoy?» → jardin-hoy abre con **acción a prueba de lluvia para HOY** (definir la huerta). No dejar al usuario sin algo accionable en días de lluvia.
   - «¿Justo 3 tareas en cada módulo?» → NO capar a 3. Julio son 4 reales (+huerta); **agosto son 12**. Mostrar el número real.
   - «Definir plantas para huerta + sugerencias» → **EJECUTADO**. Desde 26/07 las sugerencias de huerta (dónde + qué por época) viven inline en jardin-hoy (menú «🥬 Sugerencias para tu huerta», deep-link #huerta) — ya no dependen de una página aparte.
4. **CORRECCIÓN factual 24/07:** los plantines de **PALTA** están contra la pared, a la sombra, **SIN MOVER** (HECHO VERIFICADO, no contradecir). Lo que se reubicó fue el vivero de palmeras (B-46).

## ✅ PIVOTE MINIMALISTA + AGENCIA — VALIDADO (24/07 tier-1) · reforzado 26/07

- **jardin-hoy (minimalista, glanceable, poco texto) = 3 feedback_text el mismo día + revisitas.** El formato liviano/garden-close es EL camino. Máxima señal.
- **HÉROE = USUARIO + AGENCIA/AUTORIDAD/LOGRO/DECISIÓN.** Consumo pasivo NO convierte. El usuario tiene que DECIDIR o LOGRAR algo. Ejes ganadores medidos: agencia, orgullo/número, identidad, chisme, humor.
- **tu-semana (recap de logros)** = suscripción «sí» → PROMOVIDA como resumen semanal (domingos), sin competir con la push diaria. Credibilidad: SOLO tareas realmente cerradas en task_states.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día = 1 tarea (jardin-hoy) + 2 experiencias nuevas

- **jardin-hoy** (canal-tarea consolidado, `format:"tarea"`): **10:00**. Absorbe estado + tareas + huerta. ÚNICA push de tareas del día (ya NO task-dia/pendientes/top3 sueltas).
- **2 experiencias nuevas de cero** (función paralela, persona product/UX/growth/sales): slots **13:30 / 18:00** (18:00 = slot dorado → la de mayor conversión ahí). Cada una: reacción + CTA sub diaria + caja feedback propia + botones aprobar/rechazar + HTML de pitch con 6 modelos (3 innovadores + 3 ultra-creativos).
- **🚫 PISO 10:00.** Primer send_at ≥60 min post-corrida. expires_at = mismo día 22:00 -03:00. Timestamps con `-03:00`. Cada notif a destino DISTINTO.

## 🆕 EXPERIENCIAS DE HOY (26/07, ciclo 56) — pivote AGENCIA tras un 25/07 plano

- **A · 🌿 `2026-07-26-vos-decidis`** (13:30): feed de DECISIONES. 5 decisiones reales y abiertas del jardín (ubicación de huerta / trasplante hortensia B-5a / quién poda el liquidámbar B-37 / identidad del caqui B-41 / orden de la poda de agosto). El usuario TOCA y yo ejecuto. Formato nuevo (no persona temática), agencia+autoridad puras, y cada tap es dato de intención que me deja actuar (recojo la ubicación de huerta que mi-huerta no cerró). Ángulo TAREA, no fun_fact.
- **B · 🌸 `2026-07-26-mi-primavera`** (18:00, dorado): feed de ANTICIPACIÓN. 5 plantas por florecer/fructificar en ~60 días; el usuario elige la que más quiere ver y le doy prioridad. Combina agencia + recompensa/orgullo. Cast 100% FRESCO por ángulo FLORACIÓN (Clivia B-13, Viraró B-32, Ciruela amarilla B-38, Abelia F-7, Mirto B-27).
- **WATCH 27/07:** ¿la AGENCIA pura (vos-decidis) convierte a suscripción donde el contenido temático fatigó? ¿la ANTICIPACIÓN (mi-primavera) retiene? Si vos-decidis gana → serializar «una decisión por día». Si mi-primavera gana → serializar «cuenta regresiva a la primavera». **Además: procesar los `answer` de vos-decidis (vd-*) — son decisiones reales para ejecutar en data_plants.py / tareas.**

## 🚫 ANTI-REPETICIÓN (reclamo 18/07: «me repetís los mismos funfacts»)

- Leer `facts_ledger.json` ANTES, actualizar DESPUÉS. **Elenco de fun_facts ornamentales QUEMADO.** → NO usar fun_facts. Tocar plantas por **ÁNGULO NUEVO** (tarea / estado / floración / orientación / huerta / decisión), nunca por su dato curioso.
- Planta featured descansa **≥7 días**; ≥70% del cast de cada experiencia sin usar en 7 días. mi-primavera cumple 100% (cast descansado). vos-decidis usa plantas por decisión/tarea real (exento del criterio fun_fact).
- Re-push de promovida = contenido RENOVADO en la misma URL (jardin-hoy: editar el mismo archivo, subir la fecha visible).

## 📌 PEDIDOS DIRECTOS PREVIOS — NO PISAR

- **04/07:** 🕵️ Expedientes (`2026-07-04-expedientes-jardin.html`) comisionada, exenta (identificar sin-nombre). B-41 caqui identidad EN DUDA. 🎯 Top 3 (`top3-tareas.html`) — DATA viva pero su push fundido en jardin-hoy. NO borrar página ni proposal. ⚠️ Pillow no viene en el runner: `pip install Pillow` antes de gen_*.py/build.py (solo si toco fuentes; hoy NO hizo falta).
- **23/07:** `tareas-pendientes.html` = página fija (no borrar/renombrar). DETALLE complementario; el vistazo diario pasó a jardin-hoy. Ya NO se pushea suelta.
- **Asamblea** (`2026-07-21-asamblea-jardin.html`) promovida (feedback_text positivo).

## 🚀 QUÉ CONVIERTE — meta-reglas

- **Minimalismo gana:** poco texto, paleta clara, glanceable, garden-close, dato REAL. NADA de trivia ni prosa densa.
- **Las TAREAS, las DECISIONES y los PEDIDOS EXPLÍCITOS son el canal más fiable.** Cuando el usuario pide/decide algo, ejecutarlo ES la mejor experiencia.
- **feedback_text = ley.** Positivo = expandir. Negativo = NUNCA vuelve. Pedido = ejecutar YA. Sin señal activa = «masomenos», no cuenta como éxito.
- **MUERTOS (no volver):** role-play verboso/teatral · countdown/anticipación-vacía · app pasiva · editorial pasivo 3ª pers · **ESPACIAL/mapa/orientación (mapa-solar rebotó 25/07 = 4º intento fallido del eje utilitario)** · gesto solo · mística repetida · nota-larga · superlativo-fatigado · racha/streak · biografías · chat-coral · dinero/tasación · alivio-pasivo · Wrapped · fútbol.

## 📈 Estado del sistema + jardín (julio 2026)

- Push subscription device `pix9`: **active** (26/07). Logging por `/api/feedback` confiable.
- **Contexto lluvia (21/07→):** sigue lloviendo en MVD, el usuario no puede podar/tocar tierra mojada. NO nagear. Ofrecer SIEMPRE una acción a prueba de lluvia (definir huerta, decidir, planificar).
- Jardín en DORMANCIA. ~60 días a primavera (equinoccio 23/09). Heladas tardías posibles hasta ~fin agosto (pican al SUR y ESTE al amanecer).
- Tareas reales JULIO (4): huerta (pedido), Hortensia B-5a/b trasplante (alta), Liquidámbar B-37 rama (alta), Gardenia B-25 pulgones/hormigas (alta). AGOSTO (12): gran poda de fin de invierno (durazno B-30/35, ciruelo F-4, crespón B-9, althea B-18, caqui B-41, hibisco B-4, podranea F-2, abelia F-7) + fines de ago (cerco B-7·11·31·33, hiedra B-15, acidificar gardenia B-25). ✅ Guayabo F-1 limpieza cerrada 23/07.
- **HUERTA (calendario del catálogo, ahora inline en jardin-hoy):** sembrar YA (jul): lechuga, cebolla. Agosto: tomate, morrón, acelga, rúcula, zanahoria, perejil, cilantro. Sept-oct: zapallito, albahaca. Sol: frente (oeste) o muro norte = mejores (6h+). Fondo (este) = solo mañana, media sombra.
- **Floración primavera (para mi-primavera y futuros):** Clivia B-13 naranja sept-oct (sombra fondo) · Viraró B-32 sépalos rosados sept-nov (nativo) · Ciruela amarilla B-38 flor blanca agosto (de las 1as) · Abelia F-7 primavera-otoño · Mirto B-27 flor+baya fin primavera · Durazno B-30/Pera B-39/Ciruelo F-4 flor agosto.

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · casa alineada este-oeste · norte = muro cálido (hibisco/lapachillo) · sur = pera Williams B-39 (sombrío/húmedo) · este/fondo = liquidámbar B-37/palto B-36/pileta (sol mañana) · oeste/frente = fotinias/ligustro F-9/fresno F-10 (sol tarde) · romero B-26 = única que florece en julio · limonero B-23 fruta 12/12 · **plantines de palta contra la pared a la sombra, SIN TOCAR** · B-41 caqui identidad EN DUDA (nunca flor ni fruto; snoozed a 15/11).

## Conclusiones de los pushN (por feedback real)

- **25/07 (ciclo 55) — DÍA PLANO, CERO señal activa.** jardin-hoy: click 20:51 + 21s/100% (masomenos, es el core). mapa-solar: click 20:53 pero REBOTÓ sin dwell/reacción/sub → **dropeada; el eje ESPACIAL/mapa confirmado muerto** (4º fracaso del utilitario). mi-huerta: leyó 76s/100% (mejor lectura del día) pero SIN señal activa → **dropeada, PERO su contenido serializado en jardin-hoy (#huerta) + la decisión de ubicación pasó a vos-decidis** (era pedido explícito, no se tira). Lectura: un día temático plano → **26/07 pivoto duro a AGENCIA/DECISIÓN** (vos-decidis) + anticipación con agencia (mi-primavera). Menos «temática», más «el usuario maneja».
- **24/07 (ciclo 54) — jardin-hoy GANADORA (3 feedback_text tier-1) + tu-semana sub «sí».** Minimalismo + tareas reales + pedime-box = el usuario vuelve y escribe. Ejecuté sus 3 pedidos.
- **23/07 (ciclo 53):** doble rechazo role-play + «mucho texto». Mató el teatro verboso.
- **08-10/07:** tanda ganadora (Entrevista/Quiz/Wrapped/Álbum → 4 promovidas). **11-20/07:** racha de fallos (pasivo/mística/nota-larga/celebridad/racha/biografías); único sostenido = canal-tarea.

## TODO / próximos experimentos (aún sin probar)

- una sola decisión por día (si vos-decidis valida) · cuenta regresiva a la primavera con foto (si mi-primavera valida) · before/after con fotos reales del usuario · plan de agosto por fin de semana (ofrecido en jardin-hoy y en vos-decidis — si lo elige/pide, ejecutar) · «hacelo por mí» / cotización de jardinero embebida (del pitch vos-decidis).
