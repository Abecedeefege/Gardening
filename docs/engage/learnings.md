# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots base: 08:30 / 13:00 / 19:30 (-03:00),
PERO el slot c 19:30-curio está en revisión (ver abajo). Primer send_at ≥60 min después de la corrida.
expires_at = mismo día 22:00 -03:00. Cada notificación a un destino DISTINTO. Timestamps SIEMPRE con `-03:00`.
**3 pushes curados ganan a 20 — CONFIRMADO.** El usuario abre 2-3/día sin importar cuántos mandes.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 (por chat, sesión Claude Code) — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — experiencia COMISIONADA para identificar
   las 13 fichas dudosas + 2 plantas sin ficha. Pre-aprobada, EXENTA de la regla de no-supervivencia. Vive hasta
   cerrar los casos. Sus respuestas llegan como `answer` con qids `exp-*` (exp-b41-fruta, exp-b41-corteza,
   exp-b40-hoja, exp-b34-latex, exp-b47-color): PROCESARLAS en cada corrida → actualizar `data_plants.py` y la
   página. **05/07: aún SIN respuestas exp-* en engagement.json** (push abierto: sin datos de click hasta cutoff).
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07). Paso obligatorio de cada
   corrida: `python tools/gen_top3_tareas.py <fecha> --merge` (self-gated; NO tocaba el 05/07, próxima 06/07).
   Sus entries (id `*-top3`, format tarea) son ADICIONALES al cupo, como las de gen_task_reminders.
3. **Dato clave**: B-41 "caqui" con identidad EN DUDA (nunca mostró flor ni fruto). No usarlo como curio de fruta.
4. Timeline: tareas hechas/cerradas van colapsadas en "🗂️ Pasadas / hechas" (vista Todas).
5. **Splash** «Hora dorada — amanecer» integrado en el Home. Los 6 demos `engage/splash-*.html` quedan como
   referencia: NO son proposals del ciclo — no dropear, no borrar, no pushear.

## 🆕 FUNCIÓN PARALELA (pedido del usuario 28/06): 2 experiencias NUEVAS de cero por corrida

En cada corrida inicializo DOS agentes con persona product/UX/sales que construyen DOS experiencias
news-feed de cero, cada una con: (1) reacción final "¿te voló la cabeza?" (engageReact target=slug corto),
(2) CTA de **suscripción diaria** (engageAnswer qid `<slug>-suscripcion-diaria`), (3) un **HTML de pitch**
aparte con 6 modelos de monetización (3 innovadores + 3 ultra-creativos). Contrato de proposal igual que
siempre (link "← Volver al sitio estable" primero, react+sub+engage-actions, `engage.js`, SOLO datos
verificados de data_plants.py con código). Dos de los 3 pushes llevan a estas experiencias; el 3º rota
(curio #curiosidades / mundo-jardin / duelo descansado — según fatiga medida).

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide

**El eje que convierte amor→SUSCRIPCIÓN es ASOMBRO/ESTATUS/CHISME/IDENTIDAD con número o morbo — el DATO
REAL como protagonista. La ficción como plato principal (torneo, reality, romance, ceremonia) NO convierte,
y desde el ciclo 35 sabemos que la ceremonia/espectáculo ni siquiera gana la APERTURA.** Evidencia:

**CONVIERTEN (love + suscripción SÍ + aprobado, dwell alto):**
- **📱 Feed (red-social, 1ª persona)** — dwell RÉCORD 208s, 😍×2, sub×2, aprob×2. Ganador absoluto. PROMOVIDO.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub SÍ + aprob + 115s/100%. PROMOVIDO.
- **🍵 Chusmerío (tabloide/chisme)** — sub SÍ + aprob + 86s/100%. PROMOVIDO.
- **🏆 Récords (orgullo/superlativo)** — 😍 + sub SÍ + aprob + 141s/100%. PROMOVIDO.
- **📰 Diario (editorial/novedad)** — 😍 + sub SÍ + aprob + 92s/100%. PROMOVIDO.

**APRUEBAN pero sin señal completa de conversión:**
- **😂 Memes (HUMOR + dato-remate)** — 04/07: click 13:56 UY + aprob + 71s/100%, PERO el sync cortó justo tras
  la aprobación (16:57Z): reacción y suscripción DESCONOCIDAS. PROMOVIDO 05/07. VIGILAR el sync de mañana:
  si aparece 😍+sub, el humor entra al grupo ganador; si no, queda con los tibios.
- **🧪 Superpoderes (utilidad)** — 'meh' + 23s/10% + sin sub. TIBIO.
- **💌 Consultorio (consejo sincero)** — 'meh' + 36s/5% + sin sub. TIBIO.
- **🎤 Confesiones (intimidad 1ª persona)** — 'meh' + 133s/100% + sin sub. La intimidad RETIENE, no convierte. TIBIO.
- **📺 Reality (serializado)** — 'meh' + 62s/100% + sin sub. TIBIO.

**RECHAZAN / NO ABREN:**
- **🏆 Gala de Premios (ceremonia/espectáculo)** — 04/07 NI SE ABRIÓ: usuario activo ese día (abrió tareas 09:02 UY
  y Memes 13:56 UY) pero ignoró el push de la Gala. DROPPED 05/07. Con Mundial (rechazo explícito) cierra el
  patrón: el envoltorio teatral-competitivo (torneo, gala, ceremonia) no genera ni curiosidad de apertura.
  El eje orgullo-número ya está cubierto por Récords; disfrazarlo de evento le AGREGA fricción.
- **⚽ Mundial (competencia)** — RECHAZO EXPLÍCITO pese a 87s/100%. No relanzar deportes/torneos.
- **🗺️ Pasaporte (viajes/orígenes)** — RECHAZADO + sub NO. Geografía no engancha.
- **💘 Amores del Cantero (romance)** — soft-negative. DROPPED.

**Regla operativa:** apuntar a ASOMBRO+NÚMERO, ESTATUS/ORGULLO directo, CHISME/MORBO, IDENTIDAD, HUMOR(a
confirmar). Evitar: utilidad, geografía, consejo sincero, intimidad pura, y TODO envoltorio de evento/
espectáculo/torneo/ceremonia/serialización — la ficción como protagonista mata la apertura o la conversión.

## ⚠️ SLOT CURIO 19:30 EN CRISIS — rotado el 05/07

- Curio Caqui B-41 (02/07-c): SIN click en ventana completa de 24h.
- Curio Pera Williams B-39 (03/07-c): SIN click en ventana completa (despacho 19:45 UY, cutoff 04/07 16:57Z ≈ 18h).
- **2 curios seguidos muertos** → el formato "andá a Curiosidades" del slot nocturno está fatigado.
- Curio Clivia B-13 (04/07-c): despachado tardísimo (20:34 UY) post-cutoff — sin datos aún; puede aparecer mañana.
- **Decisión 05/07: slot c rotado a 🌍 mundo-jardin (asset ganador ×3: click+😍+95-97s) a las 18:00** (los 3 clicks
  históricos de mundo fueron 14:41-18:00 UY — franja de tarde, no noche). Si mundo clickea y el curio Clivia no,
  queda confirmado: rotar el 3er slot entre mundo/duelo(descansado desde 26/06)/experiencias promovidas, y dejar
  los curios como contenido DENTRO de experiencias, no como destino propio.

## 🎯 SEÑAL REAL MEDIDA — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 10 promovidas.
- **🌍 mundo-jardin: asset GANADOR ×3** (click+😍+95-97s). NO es proposal. En rotación del slot c desde hoy.
- **🌿 Duelo = juego GANADOR** pero necesita ≥3-4 días de descanso; última jugada 26/06 → descansado.
- **Perdedores confirmados:** herramientas utilitarias; formatos LENTOS (flip-card ×3); memory-match; postales;
  cual-sobra (removido por usuario); Rueda sobre-expuesta; Pasaporte; Amores; Mundial; Gala; Reality(tibio).
- El usuario quiere **deleite + dato real asombroso como protagonista**, NO herramientas ni ficción elaborada.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 05/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-04T16:57Z**. Cubre: click tarea-día 09:02 UY,
  click+aprobación Memes 13:56 UY. NO cubre: resto de la tarde/noche del 04/07 (curio Clivia 20:34 UY,
  posible reacción/sub de Memes, posibles aperturas de top3/expedientes — el send_log confirma despachados 13:30 UY).
- Compactación 05/07: 20/06 movido a daily_summary (sent3/click3/visits3/appr0). Ventana viva **21/06–04/07**.
- Upload pendiente de evaluación: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **29/06** — Diario + Récords → ambos 😍 + SUSCRIPCIÓN SÍ + aprobados (92s/141s). PROMOVIDOS.
- **30/06** — **Feed → 😍×2 + sub×2 + 208s (RÉCORD)**; **Pasaporte → RECHAZADO (54s)**.
- **30/06 c31** — **Chusmerío → sub SÍ + aprob + 86s**; **Superpoderes → 'meh' + 23s (tibio)**.
- **01/07 c32** — **Horóscopo → 😍 + sub SÍ + 115s**; **Consultorio → 'meh' + 36s (tibio)**; curio Evónimo → CLICK.
- **02/07 c33** — **Confesiones → aprob + 133s PERO 'meh' + sin sub (tibio)**; **Amores → soft-negative, DROPPED**;
  **curio Caqui → SIN CLICK (1er curio muerto)**.
- **03/07 c34** — **Mundial → RECHAZO EXPLÍCITO** (87s/100% y aun así "No me interesa"); **Reality → aprobado TIBIO**
  (62s, sin sub); **curio Pera Williams → SIN CLICK en ventana completa (2º curio muerto seguido)**.
- **04/07 c35** — **Memes → APROBADO** (click 13:56 UY, 71s/100%, aprobación a los ~80s; reacción/sub desconocidas
  por cutoff) → el HUMOR gana al menos la apertura+aprobación donde la ceremonia (Gala) ni se abrió;
  **Gala → NO SE ABRIÓ** (usuario activo ese día — soft-negative fuerte, DROPPED);
  **tarea-día → CLICK 09:02 UY** (los recordatorios de tareas siguen abriendo);
  **curio Clivia + top3 + expedientes → despachados, sin datos hasta el cutoff**.
- **Meta-conclusión:** 5 convierten (dato-protagonista), 5 tibias/incompletas (envoltorio emocional sin gancho
  o dato incompleto), 4 rechazadas/no-abiertas (ficción-protagonista). El push que promete un NÚMERO o un dato
  con morbo en el título gana la apertura; el que promete un "evento" la pierde.

## 🔭 Corrida 05/07 — ciclo 36 (esta corrida)

- **Proposals resueltas:** Memes→PROMOVIDO (Ideas → ✨ Experiencias; vigilar sub en sync de mañana).
  Gala→DROPPED (no-open con usuario activo; página+pitch git rm).
- **2 experiencias NUEVAS de cero (pending, created=05/07), ambas dato-protagonista con NÚMERO gigante:**
  - 💰 **La Gran Tasación del Jardín** (`engage/2026-07-05-tasacion-jardin.html`) — catálogo de subasta:
    cuánto vale cada planta (argumento = dato real) + valor total del jardín. ESTATUS+NÚMERO+morbo. Push a (08:30).
  - 🗞️ **Efemérides — Un día como hoy** (`engage/2026-07-05-efemerides-jardin.html`) — el calendario histórico
    del jardín, años transcurridos como titular gigante. ASOMBRO+NÚMERO puro. Push b (13:00).
- **Cola ciclo 36:** (a) 08:30 💰 Tasación; (b) 13:00 🗞️ Efemérides; (c) 18:00 🌍 mundo-jardin (slot curio rotado).
- **Watch 36:** (1) ¿Memes confirma sub/😍 en el sync? (2) ¿mundo-jardin revive el 3er slot donde el curio murió
  2 veces? (3) ¿Clivia clickeó anoche? (4) ¿tasación/efemérides convierten? (5) ¿llegaron respuestas exp-*?
  Si una proposal no junta aprobación con ventana limpia, se dropea el 06/07. El 06/07 TOCA top3 (ancla 04/07).

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (curios): cítricos cargados (mandarina B-24, limonero B-23); romero B-26 flor
  jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, ciruelos F-4/B-38, pera B-39);
  perennes verdes (mirto B-27, guayabo F-1, lavanda B-19, evónimo B-44).
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial(✓), superlativos(✓), red-social(✓), viajes(✗), tabloide(✓),
  utilidad(tibio), identidad(✓), consejo(tibio), confesión(tibio), romance(✗), competencia(✗), reality(tibio),
  gala(✗ no-open), memes(✓ aprobado, sub por confirmar), tasación(hoy), efemérides(hoy).
  **Sin usar (apuntar a asombro/número/estatus/humor):** before/after con fotos del usuario, entrevista/Q&A
  a una planta, playlist/canción del jardín.
- **Curios frescos NO usados** (fun_fact verificado): rosa de Siria B-18 (flor de 1 día — usada en Reality,
  descansar), lantana B-29 (cambia de color — usada en Reality, descansar). El slot curio está en pausa igual.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
