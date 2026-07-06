# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots: 08:30 / 13:00 / 18:00 (-03:00) — el slot c
se movió de 19:30 a 18:00 el 05/07 (los clicks de tarde-noche caen 14:40-19:20 UY, nunca después de las 20).
Primer send_at ≥60 min después de la corrida. expires_at = mismo día 22:00 -03:00. Cada notificación a un
destino DISTINTO. Timestamps SIEMPRE con `-03:00`.
**3 pushes curados ganan a 20 — CONFIRMADO.** El usuario abre 2-3/día sin importar cuántos mandes.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 (por chat, sesión Claude Code) — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — experiencia COMISIONADA para identificar
   las 13 fichas dudosas + 2 plantas sin ficha. Pre-aprobada, EXENTA de la regla de no-supervivencia. Vive hasta
   cerrar los casos. Sus respuestas llegan como `answer` con qids `exp-*` (exp-b41-fruta, exp-b41-corteza,
   exp-b40-hoja, exp-b34-latex, exp-b47-color): PROCESARLAS en cada corrida → actualizar `data_plants.py` y la
   página. **06/07: aún SIN respuestas exp-* en engagement.json** (2 días sin señal; considerar re-push suave ~08/07).
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07). Paso obligatorio de cada
   corrida: `python tools/gen_top3_tareas.py <fecha> --merge` (self-gated; corrió 06/07, próxima 08/07).
   Sus entries (id `*-top3`, format tarea) son ADICIONALES al cupo, como las de gen_task_reminders.
3. **Dato clave**: B-41 "caqui" con identidad EN DUDA (nunca mostró flor ni fruto). No usarlo como curio de fruta.
4. Timeline: tareas hechas/cerradas van colapsadas en "🗂️ Pasadas / hechas" (vista Todas).
5. **Splash** «Hora dorada — amanecer» integrado en el Home. Los 6 demos `engage/splash-*.html` quedan como
   referencia: NO son proposals del ciclo — no dropear, no borrar, no pushear.

## 🆕 FUNCIÓN PARALELA (pedido del usuario 28/06): 2 experiencias NUEVAS de cero por corrida

En cada corrida inicializo DOS agentes con persona product/UX/sales que construyen DOS experiencias
news-feed de cero, cada una con: (1) reacción final (engageReact target=slug corto), (2) CTA de **suscripción
diaria** (engageAnswer qid `<slug>-suscripcion-diaria`), (3) un **HTML de pitch** aparte con 6 modelos de
monetización (3 innovadores + 3 ultra-creativos). Contrato de proposal igual que siempre (link "← Volver al
sitio estable" primero, react+sub+engage-actions, `engage.js`, SOLO datos verificados de data_plants.py con
código). Dos de los 3 pushes llevan a estas experiencias; el 3º rota (mundo-jardin / duelo / promovidas).

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide

**Convierte amor→SUSCRIPCIÓN: ASOMBRO/ESTATUS/CHISME/IDENTIDAD/HUMOR con el DATO REAL DEL PRESENTE como
protagonista. NO convierten: ficción-protagonista (torneo/gala/reality), utilidad, geografía, intimidad pura,
y — nuevo del 05/07 — DINERO (tasación) y PASADO (efemérides).** Evidencia:

**CONVIERTEN (love + suscripción SÍ + aprobado, dwell alto):**
- **📱 Feed (red-social, 1ª persona)** — dwell RÉCORD 208s, 😍×2, sub×2, aprob×2. Ganador absoluto. PROMOVIDO.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub SÍ + aprob + 115s/100%. PROMOVIDO.
- **🍵 Chusmerío (tabloide/chisme)** — sub SÍ + aprob + 86s/100%. PROMOVIDO.
- **🏆 Récords (orgullo/superlativo)** — 😍 + sub SÍ + aprob + 141s/100%. PROMOVIDO.
- **📰 Diario (editorial/novedad)** — 😍 + sub SÍ + aprob + 92s/100%. PROMOVIDO.

**APRUEBAN pero sin conversión completa (tibios):**
- **😂 Memes (HUMOR + dato-remate)** — aprob + 71s/100%; reacción/sub NUNCA llegaron en syncs posteriores
  (2 días). El humor gana apertura+aprobación pero NO confirmó suscripción. PROMOVIDO, queda con los tibios.
- **🧪 Superpoderes (utilidad)** — 'meh' + 23s/10% + sin sub. **💌 Consultorio (consejo)** — 'meh' + 36s/5% + sin sub.
- **🎤 Confesiones (intimidad)** — 'meh' + 133s/100% + sin sub. La intimidad RETIENE, no convierte.
- **📺 Reality (serializado)** — 'meh' + 62s/100% + sin sub.

**RECHAZAN / NO ABREN:**
- **💰 Tasación (DINERO/VALOR)** — 05/07: leyó TODO (198s/100%, 2º dwell del canal) y aun así tripleta negativa:
  reaction 'no' + sub NO + RECHAZO EXPLÍCITO. Ponerle precio al jardín des-romantiza: el orgullo funciona con
  superlativos (Récords), NO monetizado. No relanzar precios/tasaciones.
- **🗞️ Efemérides (PASADO/historia)** — 05/07: NI SE ABRIÓ (usuario activo a las 11:25 y 19:17 UY). El número
  gigante convierte cuando habla del PRESENTE (Récords), no del pasado. Con Gala (no-open) y Mundial (rechazo):
  ni ceremonias ni historia ganan la apertura.
- **🏆 Gala** — no-open con usuario activo. **⚽ Mundial** — rechazo explícito. **🗺️ Pasaporte** — rechazado.
- **💘 Amores del Cantero (romance)** — soft-negative. DROPPED.

**Regla operativa:** apuntar a MORBO/CHISME, 1ª PERSONA social, IDENTIDAD, ORGULLO-superlativo, HUMOR — siempre
sobre el AHORA del jardín. Evitar: dinero, pasado/historia, utilidad, geografía, consejo, intimidad pura,
eventos/ceremonias/torneos/serialización.

## 📈 Slot c (tarde) — rotación funciona, curios muertos

- 3 curios seguidos SIN click (Caqui 02/07, Pera 03/07, Clivia 04/07 — confirmado 06/07: nunca apareció el click).
  El formato "andá a Curiosidades" como destino propio está MUERTO. Curios solo DENTRO de experiencias.
- **mundo-jardin 05/07 (18:00): VISITADO ~19:17 UY** (dwell 25s+9s/100%; sin evento click sincronizado, pero la
  visita es del push — 4ª apertura de mundo). La rotación del slot c a experiencias ganadoras FUNCIONA.
  Sin love esta vez: mundo empieza a gastarse — rotarlo (06/07: duelo, descansado 10 días).
- **Duelo**: juego GANADOR con ≥3-4 días de descanso; última jugada 26/06 → 06/07 va revancha (slot c 18:00).

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 11 promovidas.
- Recordatorios de tareas SIEMPRE abren: task-dia clickeado 04/07 (09:02 UY) y 05/07 (08:58 UY). El canal
  tareas-por-push es el más confiable del sistema.
- **Perdedores confirmados:** herramientas utilitarias; formatos LENTOS (flip-card ×3); memory-match; postales;
  cual-sobra (removido por usuario); Rueda sobre-expuesta; Pasaporte; Amores; Mundial; Gala; Tasación; Efemérides.
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 06/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-05T22:18Z** (19:18 UY). Cubre todo el 05/07 hasta
  ahí: task-dia click 08:58 UY, Tasación click+rechazo 11:25-11:29 UY, mundo dwell 19:17 UY. NO cubre: la noche
  del 05/07 (posible apertura tardía de Efemérides — vigilar mañana, aunque el drop ya está decidido por regla).
- Compactación 06/07: 21/06 movido a daily_summary (sent3/click3/visits3/appr0). Ventana viva **22/06–05/07**.
- Upload pendiente de evaluación: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **29/06** — Diario + Récords → ambos 😍 + SUSCRIPCIÓN SÍ + aprobados (92s/141s). PROMOVIDOS.
- **30/06** — **Feed → 😍×2 + sub×2 + 208s (RÉCORD)**; **Pasaporte → RECHAZADO (54s)**;
  **Chusmerío → sub SÍ + aprob + 86s**; **Superpoderes → 'meh' + 23s (tibio)**.
- **01/07 c32** — **Horóscopo → 😍 + sub SÍ + 115s**; **Consultorio → 'meh' + 36s (tibio)**; curio Evónimo → CLICK.
- **02/07 c33** — **Confesiones → aprob + 133s PERO 'meh' + sin sub**; **Amores → soft-negative, DROPPED**;
  **curio Caqui → SIN CLICK (1er curio muerto)**.
- **03/07 c34** — **Mundial → RECHAZO EXPLÍCITO** (87s/100%); **Reality → aprobado TIBIO** (62s, sin sub);
  **curio Pera → SIN CLICK (2º curio muerto)**.
- **04/07 c35** — **Memes → APROBADO** (71s/100%; reacción/sub nunca llegaron → tibio); **Gala → NO SE ABRIÓ**
  (DROPPED); **tarea-día → CLICK 09:02 UY**; **curio Clivia → SIN CLICK (3er curio muerto, confirmado)**.
- **05/07 c36** — **Tasación → RECHAZO EXPLÍCITO pese a 198s de lectura** (dinero des-romantiza — reaction no
  + sub no + rejected); **Efemérides → NO SE ABRIÓ** (pasado no gana apertura); **mundo-jardin en slot c 18:00
  → VISITADO 19:17 UY** (rotación del slot c validada; sin love — gastándose); **task-dia → CLICK 08:58 UY**.
- **Meta-conclusión:** 5 convierten (dato-presente protagonista: social/chisme/identidad/orgullo/editorial),
  6 tibias (humor/utilidad/consejo/intimidad/reality — aprueban sin suscribir), 6 rechazadas/no-abiertas
  (ficción, geografía, dinero, pasado). El push gana apertura cuando promete morbo o número del PRESENTE
  del jardín; pierde cuando promete evento, historia o precio.

## 🔭 Corrida 06/07 — ciclo 37 (esta corrida)

- **Proposals resueltas:** Tasación→DROPPED (rechazo explícito pese a lectura completa). Efemérides→DROPPED
  (no-open, regla de no-supervivencia). Ambas páginas+pitches git rm.
- **2 experiencias NUEVAS de cero (pending, created=06/07):**
  - ⚠️ **La Lista Negra del Jardín** (`engage/2026-07-06-lista-negra-jardin.html`) — dossier de morbo/peligro:
    lo tóxico/invasor/oscuro que vive en su casa, dato verificado por expediente. MORBO máximo. Push a (08:30).
  - 💬 **El Grupo del Jardín** (`engage/2026-07-06-chat-jardin.html`) — chat grupal de las plantas: 1ª persona
    (Feed 208s) + chisme (Chusmerío) + humor con remate de dato (Memes), anclado en el invierno actual. Push b (13:00).
- **Cola ciclo 37:** (a) 08:30 ⚠️ Lista Negra; (b) 13:00 💬 Grupo; (c) 18:00 🌿 Duelo revancha (descansado 10 días).
  + 08:00 resumen semanal (lunes) + 09:00 top3 (tocaba por ancla).
- **Watch 37:** (1) ¿Lista Negra/Grupo convierten (love+sub)? (2) ¿Duelo revive el slot c con love? (3) ¿Efemérides
  se abrió tarde anoche? (4) ¿respuestas exp-*? — si el 07/07 sigue sin ninguna, re-push suave a Expedientes el 08/07.
  (5) Si una proposal no junta aprobación con ventana limpia, se dropea el 07/07. El 08/07 TOCA top3.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (para contenido): cítricos cargados (mandarina B-24, limonero B-23); romero B-26
  flor jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, ciruelos F-4/B-38, pera B-39);
  perennes verdes (mirto B-27, guayabo F-1, lavanda B-19, evónimo B-44).
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial(✓), superlativos(✓), red-social(✓), viajes(✗), tabloide(✓),
  utilidad(tibio), identidad(✓), consejo(tibio), confesión(tibio), romance(✗), competencia(✗), reality(tibio),
  gala(✗), memes(tibio: aprobó sin sub), tasación(✗ rechazo), efemérides(✗ no-open), lista-negra(hoy), chat(hoy).
  **Sin usar (dentro de ejes ganadores):** before/after con fotos del usuario, entrevista/Q&A a una planta,
  playlist/canción del jardín.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
