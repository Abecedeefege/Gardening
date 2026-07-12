# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots base: 08:30 / 13:00 / 18:00 (-03:00). **El primer send_at
propio ≥60 min después de la corrida** (hoy corrí ~08:20 UY → arranqué 09:30). expires_at = mismo día 22:00 -03:00.
Cada notificación a un destino DISTINTO. Timestamps SIEMPRE con `-03:00`. **3 pushes curados ganan a 20 — CONFIRMADO.**
El usuario abre 2-3/día.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — COMISIONADA, pre-aprobada, EXENTA de la regla
   de no-supervivencia. Respuestas llegan como `answer` qids `exp-*`: procesarlas → `data_plants.py` + página.
   **exp-* SIGUE mudo** (≥8 días). Re-push slot c fue 10/07 (18:19 UY, sin datos). Si sigue sin enganchar, deprioritizar.
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07): `python tools/gen_top3_tareas.py <fecha> --merge`
   (self-gated). Corrió 04,06,08,10,12/07. **Próxima 14/07.** NO borrar página ni proposal `2026-07-04-top3-tareas`.
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
AMADO CON HÉROE/GESTO**, SIEMPRE con el DATO REAL DEL PRESENTE como protagonista. **NO convierten:** ficción-protagonista
(torneo/gala/reality), utilidad seca, geografía, intimidad-coral, DINERO (tasación), PASADO (efemérides/historia),
MIEDO/PELIGRO, envoltorio CHAT-GRUPAL, RANKING-del-presente (pisa a Récords), y **APP-AMADA de CONSUMO PASIVO**.

**🔑 META-PATRÓN «pedir prestada la UI de una app/formato amado» — MATIZADO 3 veces:** solo convierte si trae un
**HÉROE del presente o un GESTO de PROTAGONISMO del usuario**. GANAN: Wrapped (Spotify, «tus números») 😍+approved+172s;
Álbum (Panini, «completar/rareza») 😍+approved. **PIERDEN (consumo pasivo, sin gesto): JardínFlix (Netflix, no-open) ·
Historias (Stories, 36s no-conv) · Podcast (Spotify pod, 27s no-conv).** → **La app-amada PASIVA ya falló 3 veces.**
Un menú/reproductor donde «mirás pero no te pasa nada» NO engancha aunque sea nativamente-diario.

**⚠️ La métrica de SUSCRIPCIÓN se sigue escapando en lo que gusta pero NO tiene asombro editorial.** Quiz/Wrapped/Álbum
juntaron 😍+aprobación pero SIN sub. **Experimento 11/07 (bloque de SUSCRIPCIÓN PRIMERO + formato nativamente-diario en
Historias/Podcast) FRACASÓ: ambas se abrieron, dwell BAJO (36s/27s) y CERO conversión.** Lección: no se convierte una
suscripción si la experiencia no asombró primero. **La sub la ganan la familia EDITORIAL/PRENSA + alto asombro/dwell**
(Diario, Récords, Chusmerío, Entrevista, Horóscopo → todos sub SÍ), NO el forzar el CTA arriba. Volver al orden normal
(asombro → react → sub) y priorizar ASOMBRO/dwell.

**CONVIERTEN (love/sub + aprobado, dwell alto) — PROMOVIDAS:**
- **📱 Feed (red-social, 1ª persona)** — 208s, 😍×2, sub×2. Dwell récord del canal (tras Chusmerío 260s).
- **🍵 Chusmerío (tabloide/chisme)** — 260s (RÉCORD dwell) + re-sub + 😍.
- **🎙️ Entrevista (CELEBRIDAD, 1ª persona INDIVIDUAL del presente)** — sub + approved + 206s.
- **📗 Álbum (coleccionismo/rareza, app-amada CON gesto)** — 😍 + approved. Sin tap de sub.
- **🎁 Wrapped (app-amada, «tus números»)** — 😍 + approved + 172s. Sin tap de sub.
- **🌱 Quiz «¿Qué planta sos?» (IDENTIDAD)** — 😍 + approved + 103s. Sin sub.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub + 115s.  · **🏆 Récords (orgullo/número presente)** — 😍 + sub + 141s.
- **📰 Diario (editorial/novedad)** — 😍 + sub + 92s.
- **APRUEBAN tibio (aprobado, sin 😍 ni sub):** 😂 Memes · 🧪 Superpoderes · 💌 Consultorio · 🎤 Confesiones (133s) · 📺 Reality.

**RECHAZAN / NO ABREN (dropped):** 🍿 JardínFlix (app pasiva, no-open) · 📖 Historias (app pasiva, 36s no-conv) ·
🎧 Podcast (app pasiva, 27s no-conv) · 🔥 Trending (pisa a Récords) · ⚠️ Lista Negra (miedo) · 💬 Chat (coral) ·
💰 Tasación (dinero, 198s y rechazó) · 🗞️ Efemérides (pasado) · 🏆 Gala / ⚽ Mundial (ceremonia/torneo) ·
🗺️ Pasaporte (viajes) · 💘 Amores (romance).

**Regla operativa:** apuntar a CHISME, 1ª PERSONA foco INDIVIDUAL, IDENTIDAD, CELEBRIDAD/ESTATUS, ORGULLO-superlativo,
HUMOR, **UI-de-app-amada SOLO con héroe/gesto de protagonismo**, y **GESTO ACTIVO real** (rascar, coleccionar, jugar) —
siempre sobre el AHORA. Evitar: miedo, chat-coral, dinero, pasado, geografía, ceremonias/torneos, ranking que pise a
Récords, y **cualquier app-amada de consumo pasivo (catálogo/reproductor/stories)**.

## 📈 Slot c (tarde) — rotar promovidas ganadoras descansadas = reactiva SUSCRIPCIÓN

- Curios como destino propio = MUERTO. Curios solo DENTRO de experiencias.
- **08/07 Récords re-push → re-sub SÍ. 09/07 Chusmerío re-push → 260s RÉCORD + re-sub + 😍.** Rotar una promovida
  ganadora bien descansada al slot c REACTIVA la suscripción — CONFIRMADO ×2. Chusmerío/Récords usadas 08-09/07 →
  descansar hasta ~16/07. Récords/Chusmerío descansan.
- **11/07 slot c → 🔮 Horóscopo (sin datos aún, sent 18:06 UY tras el cutoff). 12/07 slot c → 📱 Feed** (dwell récord 208s,
  sub-converter, MUY descansado: última promoción-push 29/06). Candidatas descansadas próximas: Diario, Récords (~15/07).

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 18 promovidas (Álbum, Quiz, Wrapped confirmadas hoy).
- Recordatorios de tareas SIEMPRE abren: task-dia clic 04,05,08,11/07; task-semana 06/07. Canal más confiable.
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 09/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-11T21:16Z**, último evento **19:44Z (16:44 UY)**. Cubre 11/07
  hasta la tarde: Historias abierta 11:20 UY (36s, sin conv), task-dia clic 12:21 UY, Podcast abierto 16:44 UY (27s, sin
  conv). **Horóscopo (slot c) SIN datos** (sent 18:06 UY, después del último evento). Esperar sync de mañana.
- Compactación 12/07: 27/06 movido a daily_summary (engagement + send_log). Ventana viva **28/06–11/07**.
- Fix 12/07: statuses stale del ciclo 40 corregidos en proposals.json (JardínFlix→dropped, Álbum→promoted; ambos habían
  quedado "pending" por error el 11/07 aunque ya estaban resueltos).
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **08/07** — Entrevista → GANADORA (sub+approved+206s) PROMOVIDA; Trending → DROPPED (pisa Récords); Récords slot c
  → re-sub SÍ; task-dia+top3 → click.
- **09/07** — DÍA FUERTE. Quiz (identidad) 😍+approved+103s → PROMOVIDA. Wrapped (app-amada «tus números») 😍+approved+172s
  → PROMOVIDA + META-PATRÓN. Chusmerío slot c re-push → 260s RÉCORD + re-sub + 😍. Hueco: Quiz/Wrapped sin tap de sub.
- **10/07** — Álbum (coleccionismo/app-amada CON gesto) 😍+approved → PROMOVIDA. JardínFlix (Netflix pasivo) → NO-OPEN
  → DROPPED. task-dia+top3 sin click hasta cutoff.
- **11/07 (ciclo 41)** — **Experimento sub-primero FRACASÓ.** 📖 Historias (Stories, sub-primero) → abierta 36s, CERO
  conversión → DROPPED. 🎧 Podcast (Spotify pod, individual Palta B-36, sub-primero) → abierto 27s, CERO conversión →
  DROPPED. 🔮 Horóscopo slot c → sin datos (sent tras cutoff). task-dia (Guayabo) → click. **Con esto la app-amada PASIVA
  va 0/3** (JardínFlix, Historias, Podcast). Dwell bajísimo (36s/27s) = el envoltorio de app no asombra por sí solo.
- **Meta-conclusión:** convierten social / celebridad-individual / identidad / chisme / orgullo-superlativo / editorial /
  humor-tibio / **app-amada SOLO con héroe-gesto de protagonismo** / **gesto activo real**. FOCO INDIVIDUAL + dato del
  PRESENTE + asombro/dwell alto. La suscripción la ganan la familia EDITORIAL/PRENSA + asombro, no el CTA forzado arriba.

## 🔭 Corrida 12/07 — ciclo 42 (esta corrida)

- **Proposals resueltas:** Historias→DROPPED, Podcast→DROPPED (ambas abiertas sin conversión; app-amada pasiva). Statuses
  stale corregidos (Álbum→promoted, JardínFlix→dropped).
- **2 experiencias NUEVAS de cero (pending, created=12/07) — PIVOT tras app-amada-pasiva 0/3:**
  - 🎰 **La Raspadita del Jardín** (`engage/2026-07-12-raspadita-jardin.html`) — 9 raspaditas de lotería tap-para-revelar
    (GESTO activo real), 3 premio-mayor holográficas (Palta clon 1926 B-36, Hiedra +400 años B-15, Anacahuita ley 1986
    B-16), romero B-26 con chip «EN VIVO floreciendo AHORA». Coleccionismo (Álbum ✓) + gesto + asombro-presente. Push a (09:30).
  - 🎬 **La Especie del Día — El Documental** (`engage/2026-07-12-documental-jardin.html`) — nature-doc de prestigio
    (Nat Geo), héroe individual del presente = Liquidámbar B-37 (último en desnudarse / «sangra ámbar» storax), reparto de
    invierno. Familia EDITORIAL (sub-converter) + héroe del presente + asombro. Push b (13:00). Orden normal (asombro→sub).
  - **Cola ciclo 42:** (a) 09:30 🎰 Raspadita; (b) 13:00 🎬 Documental; (c) 18:00 📱 Feed (rotación descansada, reactiva sub).
    + 08:00 task-día (Liquidámbar B-37 limpieza de copa) + 09:00 top3 (TOCÓ hoy: Gardenia/Guayabo/Liquidámbar).
- **Watch 42:** (1) ¿el GESTO activo (Raspadita) convierte donde la app-amada pasiva falló 3 veces? (2) ¿el Documental
  editorial-prestigio con héroe del presente recupera la SUSCRIPCIÓN (familia que sí convierte)? (3) ¿aparece por fin
  data del Horóscopo 11/07 y de exp-*? (4) ¿Feed re-push reactiva sub como Récords/Chusmerío? **El 14/07 TOCA top3.**

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA
  en julio); palta B-22/B-36 y pindó B-8 con fruto hasta jul-oct; caducos pelados (durazno B-30/35, crespón B-9,
  liquidámbar B-37 último en pelarse — recién ahora; pera B-39); perennes verdes (guayabo F-1, mirto B-27, hiedra B-15).
  Heladas tardías pegan más al **sur y al este al amanecer**.
- Tarea activa urgente real: Guayabo F-1-4 fumagina + plaga (alta). Gardenia B-25 pulgones + hormigas (alta).
  Liquidámbar B-37 limpieza de copa en dormancia (alta, cuando pierda TODAS las hojas ~julio) = task-día de hoy.

## Verificados clave (stats consistentes entre experiencias — NO contradecir)

52 especies · 65 id_codes · 10 nativas (F-1,F-8,B-8,B-14,B-16,B-29,B-32,B-34,B-42,B-47) · 30 perennes · 15 caducos ·
11 frutales · romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 meses ·
palta Hass B-36 = clon de 1 árbol de 1926 · anacahuita B-16 = protegida por ley desde 1986 · hiedra B-15 = +400 años ·
cinta B-12 = purifica aire (lista NASA) · liquidámbar B-37 = storax/"ámbar líquido" (mayas lo masticaban) ·
mirto B-27 = sagrado para Venus · aguaribay F-8 = verdadera pimienta rosa · mandarina B-24 = cítrico más antiguo (3000 a.C.).

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial ✓, superlativos ✓, red-social ✓, tabloide ✓, identidad ✓, celebridad ✓,
  humor/consejo/confesión/reality (tibios), app-amada: Wrapped ✓ / Álbum ✓ / JardínFlix ✗ / Historias ✗ / Podcast ✗,
  gesto-activo: Raspadita (hoy), documental-prestigio (hoy). ✗ perdedores: viajes, romance, competencia, gala, tasación,
  efemérides, miedo, chat, ranking, app-amada-pasiva.
  **Sin usar (posibles ganadores):** before/after con fotos del usuario (esperar más uploads); Wordle/juego-diario;
  otras app-amadas SOLO si tienen héroe/gesto (BeReal doble-cámara, mapa Pokémon-GO); más gesto-activo (scratch, girar).
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
