# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots: 08:30 / 13:00 / 18:00 (-03:00). Primer send_at
≥60 min después de la corrida. expires_at = mismo día 22:00 -03:00. Cada notificación a un destino DISTINTO.
Timestamps SIEMPRE con `-03:00`. **3 pushes curados ganan a 20 — CONFIRMADO.** El usuario abre 2-3/día.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — COMISIONADA, pre-aprobada, EXENTA de la regla
   de no-supervivencia. Respuestas llegan como `answer` qids `exp-*`: procesarlas → `data_plants.py` + página.
   **exp-* SIGUE mudo** (≥7 días). Re-push slot c fue 10/07 (18:19 UY, después del cutoff → sin datos aún). Si el
   sync de mañana confirma que tampoco enganchó, deprioritizar Expedientes en slot c y rotar promovidas descansadas.
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07). Paso obligatorio:
   `python tools/gen_top3_tareas.py <fecha> --merge` (self-gated). Corrió 04,06,08,10/07. **11/07 NO tocó. Próxima 12/07.**
3. **Dato clave**: B-41 "caqui" identidad EN DUDA (nunca flor ni fruto). No usarlo como curio de fruta.
4. Timeline: hechas/cerradas van colapsadas en "🗂️ Pasadas / hechas" (vista Todas).
5. **Splash** «Hora dorada» integrado en Home. Los 6 demos `engage/splash-*.html` = referencia: NO tocar.
6. ⚠️ **Pillow (PIL) no viene instalado** en el runner: `pip install Pillow` ANTES de correr los gen_*.py / build.py.

## 🆕 FUNCIÓN PARALELA (pedido 28/06): 2 experiencias NUEVAS de cero por corrida

Cada corrida inicializo persona product/UX/sales y construyo DOS experiencias news-feed de cero, cada una con:
(1) reacción final (engageReact target=slug), (2) CTA de **suscripción diaria** (engageAnswer qid
`<slug>-suscripcion-diaria`), (3) un **HTML de pitch** aparte con 6 modelos de monetización (3 innovadores +
3 ultra-creativos). Contrato de proposal igual que siempre (link "← Volver al sitio estable" primero, react+sub+
engage-actions reales, `engage.js`, SOLO datos verificados de data_plants.py con código). Dos de los 3 pushes llevan
a estas experiencias; el 3º rota una promovida ganadora descansada (o una comisionada, ej. Expedientes).

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide

**Convierten a SUSCRIPCIÓN:** ASOMBRO/ESTATUS/CHISME/IDENTIDAD/1ª-PERSONA-INDIVIDUAL/CELEBRIDAD + **UI de app/formato
AMADO**, SIEMPRE con el DATO REAL DEL PRESENTE como protagonista. **NO convierten:** ficción-protagonista
(torneo/gala/reality), utilidad seca, geografía, intimidad-coral, DINERO (tasación), PASADO (efemérides/historia),
MIEDO/PELIGRO, envoltorio CHAT-GRUPAL, RANKING-del-presente (pisa a Récords), y **catálogo PASIVO** (ver JardínFlix).

**🔑 META-PATRÓN (validado ×2): pedir prestada la UI de una app/formato querido.** Wrapped (Spotify) 😍+approved+172s;
Álbum (figuritas Panini) 😍+approved (10/07). **MATIZ NUEVO 11/07:** la app-UI convierte solo si trae un HÉROE del
presente o un GESTO activo. Wrapped=tus números; Álbum=rareza+completar. **JardínFlix (catálogo Netflix) NO-ABRIÓ** —
un menú pasivo donde "no te pasa nada" no engancha. → hoy doblo con **Historias (tap-through)** y **Podcast (episodio
+ invitado)**: ambos app-amada CON gesto/héroe.

**CONVIERTEN (love/sub + aprobado, dwell alto) — PROMOVIDAS:**
- **📱 Feed (red-social, 1ª persona)** — 208s, 😍×2, sub×2. Dwell récord del canal (tras Chusmerío 260s).
- **🍵 Chusmerío (tabloide/chisme)** — 260s (RÉCORD dwell) + re-sub + 😍.
- **🎙️ Entrevista (CELEBRIDAD, 1ª persona INDIVIDUAL)** — sub + approved + 206s.
- **📗 Álbum (coleccionismo/rareza, app-amada)** — 😍 + approved (10/07). Sin tap de sub.
- **🎁 Wrapped (app-amada/número-presente)** — 😍 + approved + 172s. Sin tap de sub.
- **🌱 Quiz «¿Qué planta sos?» (IDENTIDAD)** — 😍 + approved + 103s. Sin tap de sub.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub + 115s.  · **🏆 Récords (orgullo/número presente)** — 😍 + sub + 141s.
- **📰 Diario (editorial/novedad)** — 😍 + sub + 92s.

**⚠️ PROBLEMA ABIERTO — la métrica de SUSCRIPCIÓN se escapa en lo que MÁS gusta.** Quiz, Wrapped y Álbum juntaron
😍+aprobación pero NINGUNO tocó el CTA de suscripción diaria. Hipótesis: aprobar ya se siente como "sí", o el bloque
de sub (debajo del de aprobar/react) se saltea. **Experimento 11/07: en Historias y Podcast pongo el bloque de
SUSCRIPCIÓN PRIMERO** (antes de reacción y de aprobar) y uso formatos NATIVAMENTE diarios (Stories caducan en 24h;
podcast = "episodio nuevo cada mañana") para que la suscripción sea el gesto natural del formato. Medir si convierte.

**APRUEBAN sin conversión completa (tibios, promovidos):** 😂 Memes · 🧪 Superpoderes · 💌 Consultorio ·
🎤 Confesiones (133s, sin sub) · 📺 Reality.

**RECHAZAN / NO ABREN (dropped):** 🍿 JardínFlix (catálogo pasivo, no-open) · 🔥 Trending (pisa a Récords) ·
⚠️ Lista Negra (miedo) · 💬 Chat (coral) · 💰 Tasación (dinero, 198s y rechazó) · 🗞️ Efemérides (pasado) ·
🏆 Gala / ⚽ Mundial (ceremonia/torneo) · 🗺️ Pasaporte (viajes) · 💘 Amores (romance).

**Regla operativa:** apuntar a CHISME, 1ª PERSONA foco INDIVIDUAL, IDENTIDAD, CELEBRIDAD/ESTATUS, ORGULLO-superlativo,
HUMOR y **UI-de-app-amada CON héroe/gesto** — siempre sobre el AHORA. Evitar: miedo, chat-coral, dinero, pasado,
utilidad seca, geografía, ceremonias/torneos, ranking que pise a Récords, y catálogos pasivos.

## 📈 Slot c (tarde) — rotar promovidas ganadoras descansadas = reactiva SUSCRIPCIÓN

- Curios como destino propio = MUERTO. Curios solo DENTRO de experiencias.
- **08/07 Récords re-push → re-sub SÍ. 09/07 Chusmerío re-push → 260s RÉCORD + re-sub SÍ + 😍.** Rotar una promovida
  ganadora bien descansada al slot c REACTIVA la suscripción — CONFIRMADO ×2. Chusmerío/Récords usadas 08-09/07 →
  descansar ≥1 semana.
- **10/07 slot c → Expedientes** (comisionada). **11/07 slot c → 🔮 Horóscopo** (descansada desde 01/07, identidad+sub,
  la única promovida-que-tocó-sub sin re-usar). Candidatas descansadas próximas: Diario, Feed.

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 15 promovidas (Álbum sumada 11/07).
- Recordatorios de tareas SIEMPRE abren: task-dia clickeado 04,05,08/07; task-semana 06/07. Canal más confiable.
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 09/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-10T17:41Z (14:41 UY)**. Cubre 10/07 hasta el mediodía:
  Álbum clic+😍+approved 14:40-41 UY. JardínFlix (push 09:24 UY) SIN click hasta el cutoff = no-open. task-dia/top3
  10/07 sin click registrado (pero cutoff temprano). **NO hay datos de la tarde/noche del 10/07** (Expedientes 18:19 UY,
  exp-*). Esperar sync de mañana.
- Compactación 11/07: 26/06 movido a daily_summary (engagement + send_log). Ventana viva **27/06–10/07**.
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **05/07** — Tasación → RECHAZO pese a 198s (dinero); Efemérides → NO-OPEN (pasado).
- **06/07** — Lista Negra → NO-OPEN (miedo); Chat → RECHAZO (coral); task-semana → CLICK.
- **08/07** — Entrevista → GANADORA (sub+approved+206s) PROMOVIDA; Trending → DROPPED (pisa Récords); Récords slot c
  → re-sub SÍ; task-dia+top3 → click.
- **09/07** — DÍA FUERTE 3/3. Quiz (identidad) 😍+approved+103s → PROMOVIDA. Wrapped (app-amada) 😍+approved+172s →
  PROMOVIDA + META-PATRÓN "UI de app querida". Chusmerío slot c re-push → 260s RÉCORD + re-sub + 😍. Hueco: Quiz/Wrapped
  sin tap de sub.
- **10/07 (ciclo 40)** — **Álbum (coleccionismo/app-amada)** 😍+approved 14:41 UY → PROMOVIDA (2ª validación del
  meta-patrón, ahora CON gesto de completar). **JardínFlix (catálogo Netflix)** → NO-OPEN → DROPPED: el catálogo pasivo
  NO engancha aunque sea UI-de-app-amada; falta héroe/gesto. task-dia (Pindó) + top3 sin click hasta cutoff.
- **Meta-conclusión:** 8 ejes convierten (social / celebridad-individual / identidad / chisme / orgullo-superlativo /
  editorial / humor-tibio / **UI-de-app-amada con héroe-gesto**). Gana apertura+conversión con FOCO INDIVIDUAL + dato
  del PRESENTE + interfaz de una app/formato amado que TENGA protagonista o gesto activo (no menú pasivo).

## 🔭 Corrida 11/07 — ciclo 41 (esta corrida)

- **Proposals resueltas:** Álbum→PROMOVIDA (tarjeta en Ideas→✨ Experiencias, build.py; footer a nota de integración).
  JardínFlix→DROPPED (no-open; catálogo pasivo; página+pitch git rm).
- **2 experiencias NUEVAS de cero (pending, created=11/07):**
  - 📖 **Las Historias de tu Jardín** (`engage/2026-07-11-historias-jardin.html`) — Stories tap-through reales (barras
    de progreso, hold-para-pausar), 9 plantas en 1ª persona con dato del presente invernal. Caducidad 24h = motor de
    retorno honesto. Push a (08:30).
  - 🎧 **El Podcast de tu Jardín / «Voces del Cantero»** (`engage/2026-07-11-podcast-jardin.html`) — UI Spotify podcast,
    episodio del día + invitado individual (Palta Hass B-36 "clon de 1926"), lista de episodios expandibles, botón
    Seguir. Celebridad-individual + "episodio nuevo cada mañana". Push b (13:00).
  - **AMBAS** ponen el bloque de SUSCRIPCIÓN PRIMERO (experimento de la métrica de sub) y usan formatos nativamente
    diarios. Ambas son app-amada CON héroe/gesto (la corrección post-JardínFlix).
- **Cola ciclo 41:** (a) 08:30 📖 Historias; (b) 13:00 🎧 Podcast; (c) 18:00 🔮 Horóscopo (rotación descansada).
  + 08:00 task-día (Guayabo F-1 limpieza). Top3 NO tocó (próxima 12/07).
- **Watch 41:** (1) ¿el bloque de SUB-primero + formato nativamente-diario por fin recupera la métrica de suscripción
  que Quiz/Wrapped/Álbum perdieron? (2) ¿Historias (efímero/tap-through) y Podcast (episodio/celebridad) confirman que
  la app-amada convierte cuando hay gesto/héroe (vs JardínFlix pasivo)? (3) ¿aparecen respuestas exp-* del re-push
  10/07? (4) ¿Horóscopo re-push reactiva sub como Récords/Chusmerío? **El 12/07 TOCA top3.**

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA
  en julio); palta B-22/B-36 y pindó B-8 con fruto hasta jul-oct; caducos pelados (durazno B-30/35, crespón B-9,
  liquidámbar B-37, pera B-39); perennes verdes (guayabo F-1, mirto B-27, hiedra B-15, lavanda, evónimo B-44).
  Heladas tardías pegan más al **sur y al este al amanecer**.
- Tarea activa urgente real: Guayabo F-1-4 fumagina + plaga (alta). Gardenia B-25 pulgones + hormigas (alta).
  Liquidámbar B-37 limpieza de copa en dormancia. task-día de hoy = Guayabo F-1 limpieza (baja, cualquier momento).

## Verificados clave (stats consistentes entre experiencias — NO contradecir)

52 especies · 65 id_codes · 10 nativas (F-1,F-8,B-8,B-14,B-16,B-29,B-32,B-34,B-42,B-47) · 30 perennes · 15 caducos ·
11 frutales · romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 meses ·
palta Hass B-36 = clon de 1 árbol de 1926 · anacahuita B-16 = protegida por ley desde 1986 · hiedra B-15 = +400 años ·
cinta B-12 = purifica aire (lista NASA) · liquidámbar B-37 = storax/"ámbar líquido" · mirto B-27 = sagrado para Venus.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial ✓, superlativos ✓, red-social ✓, tabloide ✓, identidad ✓ (horóscopo+quiz),
  celebridad ✓, humor (tibio), consejo (tibio), confesión-coral (tibio), reality (tibio), app-amada: Wrapped ✓ /
  Álbum ✓ / JardínFlix ✗ / hoy Historias(Stories) + Podcast(Spotify). ✗ perdedores: viajes, romance, competencia, gala,
  tasación, efemérides, miedo, chat, ranking, catálogo pasivo.
  **Sin usar (posibles ganadores):** before/after con fotos del usuario (esperar más uploads); otras apps-amadas
  (Wordle/juego-diario, mapa tipo Pokémon-GO, playlist real, BeReal doble-cámara — idea en el pitch de Historias).
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
