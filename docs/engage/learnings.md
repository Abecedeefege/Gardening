# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots: 08:30 / 13:00 / 18:00 (-03:00) — el slot c
se movió de 19:30 a 18:00 el 05/07 (los clicks de tarde-noche caen 14:40-19:20 UY, nunca después de las 20).
Primer send_at ≥60 min después de la corrida. expires_at = mismo día 22:00 -03:00. Cada notificación a un
destino DISTINTO. Timestamps SIEMPRE con `-03:00`.
**3 pushes curados ganan a 20 — CONFIRMADO.** El usuario abre 2-3/día sin importar cuántos mandes.
⚠️ **La corrida del 07/07 se SALTÓ** (gap de routine): el 08/07 procesa las proposals del 06/07 y arranca ciclo 38.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — COMISIONADA para identificar 13 fichas
   dudosas + 2 sin ficha. Pre-aprobada, EXENTA de la regla de no-supervivencia. Respuestas llegan como `answer`
   qids `exp-*` (exp-b41-fruta, exp-b41-corteza, exp-b40-hoja, exp-b34-latex, exp-b47-color): PROCESARLAS →
   actualizar `data_plants.py` + la página. **08/07: SIGUE sin respuestas exp-*** (4 días sin señal). Re-push
   suave recomendado ~09-10/07 (rota al slot c cuando toque, con copy detective).
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07). Paso obligatorio:
   `python tools/gen_top3_tareas.py <fecha> --merge` (self-gated). Corrió 04, 06 y **08/07** (tocó); próxima 10/07.
3. **Dato clave**: B-41 "caqui" con identidad EN DUDA (nunca mostró flor ni fruto). No usarlo como curio de fruta.
4. Timeline: hechas/cerradas van colapsadas en "🗂️ Pasadas / hechas" (vista Todas).
5. **Splash** «Hora dorada» integrado en Home. Los 6 demos `engage/splash-*.html` = referencia: NO tocar.
6. ⚠️ **Pillow (PIL) no viene instalado** en el runner: `pip install Pillow` ANTES de correr los gen_*.py
   (importan build.py que usa PIL). Paso previo obligatorio de cada corrida.

## 🆕 FUNCIÓN PARALELA (pedido del usuario 28/06): 2 experiencias NUEVAS de cero por corrida

Cada corrida inicializo DOS agentes con persona product/UX/sales que construyen DOS experiencias news-feed de
cero, cada una con: (1) reacción final (engageReact target=slug), (2) CTA de **suscripción diaria**
(engageAnswer qid `<slug>-suscripcion-diaria`), (3) un **HTML de pitch** aparte con 6 modelos de monetización
(3 innovadores + 3 ultra-creativos). Contrato de proposal igual que siempre (link "← Volver al sitio estable"
primero, react+sub+engage-actions con los botones Aprobar/No-me-interesa reales para las pending, `engage.js`,
SOLO datos verificados de data_plants.py con código). Dos de los 3 pushes llevan a estas experiencias; el 3º
rota (mundo-jardin / duelo / promovidas rested).

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide

**Convierte amor→SUSCRIPCIÓN: ASOMBRO/ESTATUS/CHISME/IDENTIDAD/1ª-PERSONA con el DATO REAL DEL PRESENTE como
protagonista. NO convierten: ficción-protagonista (torneo/gala/reality), utilidad, geografía, intimidad pura,
DINERO (tasación), PASADO (efemérides/historia), y — nuevo — MIEDO/PELIGRO y el envoltorio CHAT-GRUPAL.**

**CONVIERTEN (love + sub SÍ + aprobado, dwell alto) — PROMOVIDAS:**
- **📱 Feed (red-social, 1ª persona)** — dwell RÉCORD 208s, 😍×2, sub×2. Ganador absoluto.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub + 115s/100%.
- **🍵 Chusmerío (tabloide/chisme)** — sub + 86s/100%.
- **🏆 Récords (orgullo/superlativo, número presente)** — 😍 + sub + 141s/100%.
- **📰 Diario (editorial/novedad)** — 😍 + sub + 92s/100%.

**APRUEBAN sin conversión completa (tibios, promovidos):** 😂 Memes (humor, 71s, sin sub confirmada) ·
🧪 Superpoderes (utilidad, meh/23s) · 💌 Consultorio (consejo, meh/36s) · 🎤 Confesiones (intimidad, 133s
retiene pero meh/sin sub) · 📺 Reality (serializado, meh/62s).

**RECHAZAN / NO ABREN (dropped):**
- **⚠️ Lista Negra (MIEDO/PELIGRO)** — 06/07 NO-OPEN pese a usuario activo. El miedo REPELE donde el chisme
  atrae: "esto puede lastimarte" no es algo que uno quiera abrir. Nuevo perdedor confirmado.
- **💬 Grupo/Chat (envoltorio chat-grupal)** — 06/07 RECHAZO explícito (meh+sub NO+rejected, 18s) pese a fusionar
  3 ejes ganadores (Feed+Chusmerío+Memes). El formato "grupo de WhatsApp" se lee como MÁS notificaciones, no como
  experiencia-destino; fragmenta el dato en burbujas. El 1ª-persona rinde con POST propio (Feed), no coral.
- **💰 Tasación (dinero)** — leyó 198s y rechazó: ponerle precio des-romantiza. **🗞️ Efemérides (pasado)** — no-open.
- **🏆 Gala / ⚽ Mundial (ceremonia/torneo)** — no-open / rechazo. **🗺️ Pasaporte (viajes)** — rechazo.
  **💘 Amores (romance)** — soft-negative.

**Regla operativa:** apuntar a MORBO-CHISME, 1ª PERSONA con foco individual, IDENTIDAD, ORGULLO-número-presente,
ESTATUS/CELEBRIDAD, HUMOR — siempre sobre el AHORA. Evitar: miedo/peligro, chat-coral, dinero, pasado, utilidad,
geografía, consejo, intimidad pura, ceremonias/torneos/serialización.

## 📈 Slot c (tarde) — rotación funciona, curios muertos

- Curios como destino propio = MUERTO (3 sin click: Caqui/Pera/Clivia). Curios solo DENTRO de experiencias.
- **Duelo** 06/07 (slot c 18:00): JUGADO completo pero 5/6 (falló r2), dwell 36s, SIN love ni sub. El juego
  retiene pero ya no sorprende — descansarlo ≥1 semana. Mundo visitado 05/07 sin love (gastándose).
- **08/07 slot c → 🏆 Récords** (promovida rested, número-presente, nunca re-pusheada desde promo 29/06):
  eje distinto a las 2 nuevas. Rotar promovidas ganadoras descansadas es lo más sano para el slot c.

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 11 promovidas.
- Recordatorios de tareas SIEMPRE abren: task-dia clickeado 04/07 y 05/07; task-semana clickeado **06/07 11:56 UY**.
  El canal tareas-por-push es el más confiable del sistema.
- **Perdedores confirmados:** utilitarias; formatos LENTOS (flip-card ×3); memory-match; postales; Rueda
  sobre-expuesta; Pasaporte; Amores; Mundial; Gala; Tasación; Efemérides; Lista Negra (miedo); Chat (coral).
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 08/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-07T02:49Z** (06/07 23:49 UY). Cubre TODO el 06/07:
  task-semana click 11:56 UY, chat rechazo 14:53 UY, duelo 5/6 19:20 UY, + browsing directo pix9 a feed/
  superpoderes/chusmerio la madrugada 07/07. Lista Negra: sin ningún evento (no-open). NO hay datos del 07/07
  (corrida saltada) ni de la reacción tardía de nada.
- Compactación 08/07: 22/06 y 23/06 movidos a daily_summary (engagement + send_log). Ventana viva **24/06–06/07**.
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **30/06** — Feed → 😍×2 + sub×2 + 208s RÉCORD; Pasaporte → RECHAZO; Chusmerío → sub + 86s; Superpoderes → meh/23s.
- **01/07** — Horóscopo → 😍 + sub + 115s; Consultorio → meh/36s; curio Evónimo → click.
- **02/07** — Confesiones → aprob + 133s pero meh/sin sub; Amores → soft-neg DROPPED; curio Caqui → sin click.
- **03/07** — Mundial → RECHAZO (87s); Reality → aprob TIBIO (62s, sin sub); curio Pera → sin click.
- **04/07** — Memes → APROBADO (71s; reacción/sub nunca confirmadas → tibio); Gala → NO-OPEN DROPPED; task-día → click.
- **05/07** — Tasación → RECHAZO pese a 198s (dinero des-romantiza); Efemérides → NO-OPEN; mundo slot c → visita sin love.
- **06/07 (ciclo 37)** — **Lista Negra → NO-OPEN** (miedo no abre); **Chat → RECHAZO explícito** (meh+sub NO+18s,
  el chat-coral no es experiencia-destino); **Duelo revancha → jugado 5/6 sin love/sub** (juego gastado);
  **task-semana → CLICK 11:56 UY**. Cero conversiones nuevas: ciclo flojo, 2 ángulos nuevos quemados.
- **Meta-conclusión:** 5 convierten (social/chisme/identidad/orgullo-número/editorial), 5 tibias (humor/utilidad/
  consejo/intimidad/reality), 8 rechazadas/no-abiertas (ficción, geografía, dinero, pasado, miedo, chat-coral).
  El push gana apertura cuando promete morbo-CHISME, número del PRESENTE, estatus o personalidad individual;
  pierde cuando promete evento, historia, precio, AMENAZA o "otro chat".

## 🔭 Corrida 08/07 — ciclo 38 (esta corrida)

- **Proposals resueltas:** Lista Negra→DROPPED (no-open, miedo repele). Chat→DROPPED (rechazo explícito, chat-coral
  no convierte). Ambas páginas+pitches git rm. Sin promociones (el 06/07 no dejó aprobaciones).
- **2 experiencias NUEVAS de cero (pending, created=08/07):**
  - 🎙️ **La Entrevista Exclusiva** (`engage/2026-07-08-entrevista-jardin.html`) — nota de tapa de revista: UNA
    planta-celebridad del presente entrevistada en 1ª persona. Fusiona los 2 ejes que MÁS retienen: 1ª-persona
    (Feed 208s) + estatus (Récords 141s), con foco INDIVIDUAL (a diferencia del coral que fracasó). Push a (08:30).
  - 🔥 **Trending del Jardín** (`engage/2026-07-08-trending-jardin.html`) — ranking-feed tipo X/Twitter de lo que
    EXPLOTA esta semana de invierno, número grande de posición por ítem, todo del PRESENTE (no pasado). Eje
    número-presente + orgullo (Récords) en formato ranking. Push b (13:00).
- **Cola ciclo 38:** (a) 08:30 🎙️ Entrevista; (b) 13:00 🔥 Trending; (c) 18:00 🏆 Récords (promovida rested).
  + 08:00 task-día (Gardenia B-25) + 09:00 top3 (tocaba por ancla).
- **Watch 38:** (1) ¿Entrevista (foco individual) convierte donde el chat coral falló? (2) ¿Trending-presente
  convierte como Récords sin canibalizarlo? (3) ¿Récords revive el slot c con love? (4) ¿aparecen respuestas exp-*?
  Si el 09/07 siguen sin ninguna, re-push suave a Expedientes ~09-10/07. (5) Proposals sin aprobación se dropean 09/07.
  El 10/07 TOCA top3.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno: cítricos cargados (mandarina B-24, limonero B-23 da 12/12 meses); romero B-26
  florece jun-oct; palta B-22 y pindó (B-8/21/28) con fruto hasta julio; caducos pelados (durazno B-30/35,
  crespón B-9, liquidámbar B-37, ciruelos F-4/B-38, pera B-39); perennes verdes (guayabo F-1, mirto B-27,
  lavanda B-19, evónimo B-44). Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial(✓), superlativos(✓), red-social(✓), viajes(✗), tabloide(✓),
  utilidad(tibio), identidad(✓), consejo(tibio), confesión(tibio), romance(✗), competencia(✗), reality(tibio),
  gala(✗), memes(tibio), tasación(✗), efemérides(✗), lista-negra/miedo(✗), chat-coral(✗), entrevista(hoy),
  trending(hoy). **Sin usar (ejes ganadores):** before/after con fotos del usuario, playlist/canción del jardín,
  quiz de personalidad "¿qué planta sos?" (identidad, convierte — probar en news-feed shape).
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
