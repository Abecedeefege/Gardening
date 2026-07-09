# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots: 08:30 / 13:00 / 18:00 (-03:00) — el slot c
se movió de 19:30 a 18:00 el 05/07 (los clicks de tarde-noche caen 14:40-19:20 UY, nunca después de las 20).
Primer send_at ≥60 min después de la corrida. expires_at = mismo día 22:00 -03:00. Cada notificación a un
destino DISTINTO. Timestamps SIEMPRE con `-03:00`.
**3 pushes curados ganan a 20 — CONFIRMADO.** El usuario abre 2-3/día sin importar cuántos mandes.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — COMISIONADA para identificar 13 fichas
   dudosas + 2 sin ficha. Pre-aprobada, EXENTA de la regla de no-supervivencia. Respuestas llegan como `answer`
   qids `exp-*` (exp-b41-fruta, exp-b41-corteza, exp-b40-hoja, exp-b34-latex, exp-b47-color): PROCESARLAS →
   actualizar `data_plants.py` + la página. **09/07: SIGUE sin respuestas exp-*** (5 días sin señal). Re-push
   suave RECOMENDADO ~10-11/07 (rotar al slot c con copy detective, sin quemar el slot de experiencias).
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07). Paso obligatorio:
   `python tools/gen_top3_tareas.py <fecha> --merge` (self-gated). Corrió 04, 06, 08/07; **09/07 NO tocó**; próxima **10/07**.
3. **Dato clave**: B-41 "caqui" con identidad EN DUDA (nunca mostró flor ni fruto). No usarlo como curio de fruta.
4. Timeline: hechas/cerradas van colapsadas en "🗂️ Pasadas / hechas" (vista Todas).
5. **Splash** «Hora dorada» integrado en Home. Los 6 demos `engage/splash-*.html` = referencia: NO tocar.
6. ⚠️ **Pillow (PIL) no viene instalado** en el runner: `pip install Pillow` ANTES de correr los gen_*.py / build.py
   (importan build.py que usa PIL). Paso previo obligatorio de cada corrida.

## 🆕 FUNCIÓN PARALELA (pedido del usuario 28/06): 2 experiencias NUEVAS de cero por corrida

Cada corrida inicializo DOS agentes con persona product/UX/sales que construyen DOS experiencias news-feed de
cero, cada una con: (1) reacción final (engageReact target=slug), (2) CTA de **suscripción diaria**
(engageAnswer qid `<slug>-suscripcion-diaria`), (3) un **HTML de pitch** aparte con 6 modelos de monetización
(3 innovadores + 3 ultra-creativos). Contrato de proposal igual que siempre (link "← Volver al sitio estable"
primero, react+sub+engage-actions con los botones Aprobar/No-me-interesa reales para las pending, `engage.js`,
SOLO datos verificados de data_plants.py con código). Dos de los 3 pushes llevan a estas experiencias; el 3º
rota una promovida ganadora descansada.

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide

**Convierte amor→SUSCRIPCIÓN: ASOMBRO/ESTATUS/CHISME/IDENTIDAD/1ª-PERSONA-INDIVIDUAL/CELEBRIDAD con el DATO REAL
DEL PRESENTE como protagonista. NO convierten: ficción-protagonista (torneo/gala/reality), utilidad, geografía,
intimidad-coral, DINERO (tasación), PASADO (efemérides/historia), MIEDO/PELIGRO, el envoltorio CHAT-GRUPAL, y —
nuevo 08/07 — RANKING-del-presente cuando ya existe Récords (canibaliza, no suma asombro).**

**CONVIERTEN (love/sub SÍ + aprobado, dwell alto) — PROMOVIDAS:**
- **📱 Feed (red-social, 1ª persona)** — dwell RÉCORD 208s, 😍×2, sub×2. Ganador absoluto.
- **🎙️ Entrevista (CELEBRIDAD, 1ª persona INDIVIDUAL, presente)** — sub SÍ + approved + **206s** (2º dwell all-time).
  Foco INDIVIDUAL + framing prensa convierte donde el 1ª-persona CORAL falló. Confirmado 08/07.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub + 115s/100%.
- **🍵 Chusmerío (tabloide/chisme)** — sub + 86s/100%.
- **🏆 Récords (orgullo/superlativo, número presente)** — 😍 + sub + 141s; re-push 08/07 → re-sub SÍ (meh) 21:41 UY.
- **📰 Diario (editorial/novedad)** — 😍 + sub + 92s/100%.

**APRUEBAN sin conversión completa (tibios, promovidos):** 😂 Memes (humor, 71s, sub no confirmada) ·
🧪 Superpoderes (utilidad, meh/23s) · 💌 Consultorio (consejo, meh/36s) · 🎤 Confesiones (intimidad coral, 133s
retiene pero meh/sin sub) · 📺 Reality (serializado, meh/62s).

**RECHAZAN / NO ABREN / SOFT-NEG (dropped):**
- **🔥 Trending (RANKING-del-presente)** — 08/07 abrió pero SIN reacción/sub/approval (entró y salió). Canibaliza
  a Récords: mismo eje número-presente/orgullo, no agrega asombro. El número convierte como SUPERLATIVO (Récords),
  no como ranking-feed semanal. No relanzar. Nuevo perdedor 09/07.
- **⚠️ Lista Negra (MIEDO/PELIGRO)** — NO-OPEN: el miedo REPELE donde el chisme atrae.
- **💬 Grupo/Chat (chat-grupal)** — RECHAZO explícito (meh+sub NO, 18s): se lee como MÁS notificaciones, fragmenta
  el dato. El 1ª-persona rinde con POST/nota propia (Feed/Entrevista), no coral.
- **💰 Tasación (dinero)** — 198s y rechazó: ponerle precio des-romantiza. **🗞️ Efemérides (pasado)** — no-open.
- **🏆 Gala / ⚽ Mundial (ceremonia/torneo)** — no-open/rechazo. **🗺️ Pasaporte (viajes)** · **💘 Amores (romance)** — neg.

**Regla operativa:** apuntar a MORBO-CHISME, 1ª PERSONA con foco INDIVIDUAL, IDENTIDAD, CELEBRIDAD/ESTATUS,
ORGULLO-superlativo, HUMOR — siempre sobre el AHORA. Evitar: miedo, chat-coral, dinero, pasado, utilidad,
geografía, consejo, intimidad-coral, ceremonias/torneos/serialización, y RANKING que pise a Récords.

## 📈 Slot c (tarde) — rotar promovidas ganadoras descansadas

- Curios como destino propio = MUERTO (Caqui/Pera/Clivia sin click). Curios solo DENTRO de experiencias.
- **08/07 slot c → 🏆 Récords** (re-push): clickeado 21:41 UY → re-sub SÍ + reacción meh. Rotar promovidas
  ganadoras descansadas al slot c FUNCIONA para reactivar suscripción. Récords ya usada 08/07 → descansar.
- **09/07 slot c → 🍵 Chusmerío** (chisme, promovida 01/07, NUNCA re-pusheada — bien descansada, eje distinto a
  las 2 nuevas identidad/novedad). Duelo/Mundo gastados: descansarlos ≥1 semana.

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 12 promovidas (Entrevista sumada 09/07).
- Recordatorios de tareas SIEMPRE abren: task-dia clickeado 04, 05 y **08/07** (Gardenia 11:22 UY); task-semana
  06/07. El canal tareas-por-push es el más confiable del sistema.
- **Perdedores confirmados:** utilitarias; formatos LENTOS (flip-card ×3); memory-match; postales; Rueda
  sobre-expuesta; Pasaporte; Amores; Mundial; Gala; Tasación; Efemérides; Lista Negra (miedo); Chat (coral); Trending (ranking).
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 08/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-09T00:42Z** (08/07 21:42 UY). Cubre TODO el 08/07:
  task-dia 11:22, Entrevista aprob+sub+206s 11:23-11:27, top3 15:00, Trending abierto-sin-señal 14:59, Récords
  re-push 21:41 (re-sub SÍ + meh). NO hay datos del 09/07 todavía.
- Compactación 09/07: 24/06 movido a daily_summary (engagement + send_log). Ventana viva **25/06–08/07**.
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **30/06** — Feed → 😍×2 + sub×2 + 208s RÉCORD; Pasaporte → RECHAZO; Chusmerío → sub + 86s; Superpoderes → meh/23s.
- **01/07** — Horóscopo → 😍 + sub + 115s; Consultorio → meh/36s; curio Evónimo → click.
- **02/07** — Confesiones → aprob + 133s pero meh/sin sub; Amores → soft-neg DROPPED; curio Caqui → sin click.
- **03/07** — Mundial → RECHAZO (87s); Reality → aprob TIBIO (62s, sin sub); curio Pera → sin click.
- **04/07** — Memes → APROBADO (71s; sub nunca confirmada → tibio); Gala → NO-OPEN DROPPED; task-día → click.
- **05/07** — Tasación → RECHAZO pese a 198s (dinero des-romantiza); Efemérides → NO-OPEN; mundo slot c → visita sin love.
- **06/07** — Lista Negra → NO-OPEN (miedo no abre); Chat → RECHAZO (meh+sub NO+18s); Duelo revancha 5/6 sin love/sub;
  task-semana → CLICK. Ciclo flojo, 2 ángulos nuevos quemados.
- **08/07 (ciclo 38)** — **🎙️ Entrevista → GANADORA CLARA** (sub SÍ + approved + **206s**, 2º dwell all-time):
  celebridad/1ª-persona-INDIVIDUAL del presente convierte donde el coral falló → PROMOVIDA. **🔥 Trending →
  SOFT-NEG** (abrió 14:59 UY, entró y salió sin reacción/sub/approval): el ranking-del-presente canibaliza a
  Récords, no agrega asombro → DROPPED. **🏆 Récords (slot c re-push) → re-sub SÍ + meh** (funciona re-activar
  suscripción rotando promovidas). task-dia + top3 → click. 1 conversión nueva fuerte (Entrevista).
- **Meta-conclusión:** 6 ejes convierten (social/celebridad-individual/identidad/chisme/orgullo-superlativo/editorial),
  5 tibios (humor/utilidad/consejo/intimidad-coral/reality), 9 rechazados/no-abiertos (ficción, geografía, dinero,
  pasado, miedo, chat-coral, ranking). El push gana apertura+conversión con FOCO INDIVIDUAL + dato del PRESENTE.

## 🔭 Corrida 09/07 — ciclo 39 (esta corrida)

- **Proposals resueltas:** Entrevista→PROMOVIDA (sub SÍ+approved+206s; tarjeta en Ideas→✨Experiencias, footer a
  nota de integración). Trending→DROPPED (abierto sin señal, canibaliza Récords; página+pitch git rm).
- **2 experiencias NUEVAS de cero (pending, created=09/07):**
  - 🌱 **¿Qué planta sos?** (`engage/2026-07-09-quiz-planta.html`) — test de personalidad estilo BuzzFeed, eje
    IDENTIDAD (Horóscopo convirtió 😍+sub). Ultra-compartible (resultado screenshot). Push a (08:30).
  - 🎁 **El Wrapped de tu Jardín** (`engage/2026-07-09-wrapped-jardin.html`) — resumen estacional estilo Spotify
    Wrapped: stats reales del invierno (número-presente) + top 5 + canción por planta. Novedad viral. Push b (13:00).
- **Cola ciclo 39:** (a) 08:30 🌱 Quiz; (b) 13:00 🎁 Wrapped; (c) 18:00 🍵 Chusmerío (promovida rested).
  + 08:00 task-día (Guayabo F-1-4 fumagina). Top3 NO tocó (próxima 10/07).
- **Watch 39:** (1) ¿el quiz-identidad convierte como Horóscopo? (2) ¿el formato Wrapped (número-presente pero
  envoltorio novedoso) convierte donde Trending/ranking falló, o también canibaliza a Récords? (3) ¿Chusmerío
  descansado revive el slot c? (4) exp-* SIGUEN sin aparecer → re-push Expedientes 10-11/07. (5) Proposals sin
  aprobación se dropean 10/07. **El 10/07 TOCA top3.**

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno: cítricos cargados (mandarina B-24, limonero B-23 da 12/12 meses); romero B-26
  florece jun-oct; palta B-22 y pindó (B-8/21/28) con fruto hasta julio; caducos pelados (durazno B-30/35,
  crespón B-9, liquidámbar B-37, ciruelos F-4/B-38, pera B-39); perennes verdes (guayabo F-1, mirto B-27,
  lavanda B-19, evónimo B-44). Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Tarea activa urgente real: Guayabo F-1-4 fumagina + plaga origen (alta, mayo 2026, sigue abierta).

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial(✓), superlativos(✓), red-social(✓), tabloide(✓), identidad(✓),
  celebridad/entrevista(✓), utilidad(tibio), consejo(tibio), confesión-coral(tibio), reality(tibio), memes(tibio),
  viajes(✗), romance(✗), competencia(✗), gala(✗), tasación(✗), efemérides(✗), lista-negra/miedo(✗), chat-coral(✗),
  ranking/trending(✗), quiz-identidad(hoy), wrapped(hoy). **Sin usar (ejes ganadores):** before/after con fotos del
  usuario (esperar más uploads), playlist/canción del jardín (parcialmente en Wrapped).
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
