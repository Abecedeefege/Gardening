# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots base: 08:30 / 13:00 / 18:00 (-03:00). **El primer send_at
propio ≥60 min después de la corrida** + margen para que Vercel deploye las páginas linkeadas. expires_at = mismo día 22:00 -03:00.
Cada notificación a un destino DISTINTO. Timestamps SIEMPRE con `-03:00`. **3 pushes curados ganan a 20 — CONFIRMADO.**
El usuario abre 2-3/día. Los recordatorios task-dia/task-semana (08:00) + top3 (09:00) son ADICIONALES al cupo.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — COMISIONADA, pre-aprobada, EXENTA de la regla
   de no-supervivencia. Respuestas llegan como `answer` qids `exp-*`: procesarlas → `data_plants.py` + página.
   **NOVEDAD 12/07: exp-* dejó de estar mudo** — el usuario respondió `exp-b41-fruta` = "no-mire" (no miró si el
   caqui B-41 dio fruta). Inconcluso: B-41 sigue con identidad EN DUDA, sin update a data_plants.py. Pero confirma
   que Expedientes ENGANCHA cuando el usuario lo abre. Seguir sirviendo casos.
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07): `python tools/gen_top3_tareas.py <fecha> --merge`
   (self-gated). Corrió 04,06,08,10,12,14/07. **Próxima 16/07.** NO borrar página ni proposal `2026-07-04-top3-tareas`.
3. **Dato clave**: B-41 "caqui" identidad EN DUDA (nunca flor ni fruto confirmado). No usarlo como curio de fruta.
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

**Convierten a SUSCRIPCIÓN:** familia EDITORIAL/PRENSA + alto asombro/dwell (Diario, Récords, Chusmerío, Entrevista,
Horóscopo → todos sub SÍ); ASOMBRO/ESTATUS/CHISME/IDENTIDAD/1ª-PERSONA-INDIVIDUAL/CELEBRIDAD + el DATO REAL DEL
PRESENTE como protagonista; **UI de app/formato AMADO CON HÉROE/GESTO de protagonismo** (Wrapped, Álbum).
**NO convierten:** ficción-protagonista (torneo/gala/reality), utilidad seca, geografía/viajes, intimidad-coral,
DINERO (tasación), PASADO (efemérides/historia), MIEDO/PELIGRO, envoltorio CHAT-GRUPAL, RANKING-del-presente
(pisa Récords), **APP-AMADA de CONSUMO PASIVO** (catálogo/player/stories), **GESTO desechable de un solo uso**
(raspadita), y **EDITORIAL de CONSUMO PASIVO en 3ª persona** (documental para "mirar").

**🔑 META-PATRÓN «UI de app amada» — MATIZADO:** solo convierte con **HÉROE del presente o GESTO de PROTAGONISMO**.
GANAN: Wrapped (Spotify, «tus números») 😍+approved+172s; Álbum (Panini, «completar/rareza») 😍+approved.
**PIERDEN (consumo pasivo, sin héroe/gesto): JardínFlix (Netflix, no-open) · Historias (Stories, 36s) · Podcast (Spotify pod, 27s).**

**🔑 META-PATRÓN «el GESTO no basta» (NUEVO 12/07):** Raspadita (gesto activo de rascar) → abierta 23s, CERO conversión
→ DROPPED. El gesto por sí solo NO convierte, igual que la app-amada pasiva. Lo que convierte es el ÁNGULO
(editorial/identidad/estatus) + asombro. El Álbum ganó porque el gesto (coleccionar) traía rareza/estatus PERSISTENTE
y héroes brillantes; la raspadita era sorteo desechable. → El gesto es vehículo, no hook.

**🔑 META-PATRÓN «editorial PASIVO tampoco» (NUEVO 12/07):** Documental (nature-doc de prestigio, héroe Liquidámbar
del presente) → abierto vía push, NO convirtió → DROPPED. Editorial SÍ convierte, pero el framing "documental para
MIRAR" (narración en 3ª persona) se lee PASIVO como el Podcast. Los editoriales que convierten tienen VOZ 1ª persona
(Entrevista=Q&A) o titulares punzantes con gancho (Diario). El asombro-wonder narrado en 3ª persona no basta.

**🔑 META-PATRÓN «identidad-mística CANIBALIZA» + «app-captura NO retiene» (NUEVO 14/07, ciclo 43 doble fallo):**
- 🔮 **Tarot (IDENTIDAD mística)** → NO-OPEN pese a usuario activo. Identidad convierte (Horóscopo/Quiz), pero el
  sub-género místico/predicción YA lo cubre el Horóscopo promovido → el gancho "te tiró las cartas" se leyó como "otro
  horóscopo" y ni abrió. REGLA: dentro de identidad, NO repetir sub-género ya promovido; buscar identidad FRESCA
  (test/perfil self-focused), no otra tirada astral.
- 📸 **BeReal (app-amada captura)** → abierto vía push, REBOTE 12s/18%, cero conversión → DROPPED. Con Historias(36s)/
  Podcast(27s)/JardínFlix(no-open), la app-amada de FORMATO-CAPTURA/PLAYER ya va 0/4. Lo que sostuvo la app-amada fue
  Wrapped (tus NÚMEROS) y Álbum (COLECCIONAR+rareza): el héroe es el USUARIO/su logro persistente, NO una foto/feed del
  momento. Meta: «app amada» solo convierte si el HÉROE es el usuario y hay LOGRO/ESTATUS persistente, no captura efímera.

**CONVIERTEN (love/sub + aprobado, dwell alto) — PROMOVIDAS:**
- **🍵 Chusmerío (tabloide/chisme)** — 260s (RÉCORD dwell) + re-sub + 😍.
- **📱 Feed (red-social, 1ª persona)** — 208s, 😍×2, sub×2. 2º dwell del canal.
- **🎙️ Entrevista (CELEBRIDAD, 1ª persona INDIVIDUAL del presente)** — sub + approved + 206s.
- **🎁 Wrapped (app-amada, «tus números»)** — 😍 + approved + 172s. Sin tap de sub.
- **🏆 Récords (orgullo/número presente)** — 😍 + sub + 141s.  · **📗 Álbum (coleccionismo/rareza+gesto)** — 😍 + approved.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub + 115s.  · **🌱 Quiz «¿Qué planta sos?» (IDENTIDAD)** — 😍 + approved + 103s.
- **📰 Diario (editorial/novedad)** — 😍 + sub + 92s.
- **APRUEBAN tibio (aprobado, sin 😍 ni sub):** 😂 Memes · 🧪 Superpoderes · 💌 Consultorio · 🎤 Confesiones (133s) · 📺 Reality.

**RECHAZAN / NO ABREN (dropped):** 🍿 JardínFlix · 📖 Historias · 🎧 Podcast (app pasiva) · 🎰 Raspadita (gesto desechable) ·
🎬 Documental (editorial pasivo 3ª persona) · 🔥 Trending (pisa Récords) · ⚠️ Lista Negra (miedo) · 💬 Chat (coral) ·
💰 Tasación (dinero, 198s y rechazó) · 🗞️ Efemérides (pasado) · 🏆 Gala / ⚽ Mundial (ceremonia/torneo) ·
🗺️ Pasaporte (viajes) · 💘 Amores (romance).

**Regla operativa:** apuntar a CHISME · 1ª PERSONA foco INDIVIDUAL · IDENTIDAD · CELEBRIDAD/ESTATUS · ORGULLO-superlativo ·
EDITORIAL con voz/gancho · HUMOR · **UI-de-app-amada SOLO con héroe/gesto de protagonismo** — siempre sobre el AHORA
con dato real. Evitar: miedo, chat-coral, dinero, pasado, geografía, ceremonias/torneos, ranking que pise a Récords,
app-amada pasiva, gesto desechable, editorial pasivo en 3ª persona.

## 📈 Slot c (tarde) — rotar promovidas ganadoras descansadas = reactiva SUSCRIPCIÓN

- Curios como destino propio = MUERTO. Curios solo DENTRO de experiencias. Rotar una promovida ganadora bien descansada
  al slot c REACTIVA la suscripción — CONFIRMADO ×2 (08/07 Récords re-sub; 09/07 Chusmerío 260s+re-sub+😍).
- **13/07 slot c → 📰 Diario** (sin datos: sent 18:28 UY tras el cutoff). **14/07 slot c → 🎙️ Entrevista** (celebridad
  individual sub-converter, rest desde 08/07 = 6 días). Candidatas descansadas próximas: Horóscopo (rest desde 11/07),
  Récords/Chusmerío (~16/07), Diario (re-medir su re-push del 13/07 cuando sincronice). NO doble-identidad ni doble-chisme el mismo día.

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 18 promovidas.
- Recordatorios de tareas SIEMPRE abren: task-dia clic 04,05,08,11/07; task-semana 06/07. Canal más confiable.
- top3 abierto+like 12/07. El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**.
- **Racha de 8 experimentos-gimmick FALLIDOS 10-14/07** (app-UI/gesto/mística). Lección: los ÁNGULOS-de-contenido convierten
  (Entrevista/Quiz/Wrapped/Álbum 08-10/07), los FORMATOS-gimmick no. Ciclo 44 re-ancla en ángulos: chisme+celebridad e identidad-fresca.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 13/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último evento **2026-07-13T21:30Z** (dwell BeReal 18:30 UY). Cubre el 13/07 hasta
  ahí: Tarot NO-OPEN (sin ningún evento), BeReal clic+visita+dwell 12s/18% sin conv (18:30 UY). NO cubre: la noche del
  13/07 (Diario re-push slot c sent 18:28 UY tras cutoff → sin datos; Feed re-push del 12/07 sigue sin datos).
- Compactación 14/07: 29/06 movido a daily_summary (engagement + send_log): {sent3/clic1/visits3/appr2}. Ventana viva **30/06–13/07**.
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **08-10/07 (última tanda GANADORA)** — Entrevista (celebridad, sub+206s), Quiz (identidad, 😍+103s), Wrapped («tus números»,
  😍+172s), Álbum (coleccionismo+gesto, 😍) → 4 PROMOVIDAS. Récords/Chusmerío slot c re-push → re-sub SÍ. Trending/JardínFlix → DROPPED.
- **11-13/07 (racha de 8 fallos, todos formato-gimmick)** — Historias(36s)/Podcast(27s) app-pasiva; Raspadita(23s) gesto-desechable;
  Documental editorial-pasivo-3ªpersona; Tarot(no-open) identidad-mística que canibaliza Horóscopo; BeReal(12s) app-captura. TODOS DROPPED.
- **Meta-conclusión:** convierten social / celebridad-individual / identidad / chisme / orgullo-superlativo / editorial-con-voz /
  humor-tibio / **app-amada SOLO con héroe-gesto** — NUNCA el gesto solo ni el editorial pasivo. FOCO INDIVIDUAL + dato del
  PRESENTE + asombro/dwell alto. La suscripción la ganan la familia EDITORIAL/PRENSA + asombro, no el CTA forzado arriba.

## 🔭 Corrida 14/07 — ciclo 44 (esta corrida)

- **Proposals resueltas:** Tarot→DROPPED (identidad mística NO-OPEN, canibaliza Horóscopo), BeReal→DROPPED (app-captura rebote
  12s/18%). Ambas páginas+pitches git rm. 7º+8º fallo seguidos de formatos-gimmick.
- **DECISIÓN de estrategia:** dejo de perseguir formatos-gimmick (app-UI, gesto, mística) y RE-ANCLO en ángulos-de-contenido
  probados. Las 2 experiencias de hoy son ambas de ÁNGULO ganador (una segura, una identidad-fresca):
- **2 experiencias NUEVAS de cero (pending, created=14/07):**
  - 🚨 **La Exclusiva del Jardín** (`engage/2026-07-14-exclusiva-jardin.html`) — ANCLA SEGURA: fusión de los 2 mayores dwell del
    canal, TABLOIDE/CHISME (Chusmerío 260s) + CELEBRIDAD INDIVIDUAL (Entrevista 206s). Portada-bomba de UNA planta protagonista
    (Palta Hass B-36, el clon de 1926) con revelaciones que escalan + recuadros verificados. Morbo jugoso (NO miedo). Foco
    individual + presente. Push a (08:30). react target `exclusiva`, sub qid `exclusiva-suscripcion-diaria`.
  - 🧬 **El ADN de tu Jardín** (`engage/2026-07-14-adn-jardin.html`) — IDENTIDAD FRESCA (eje 2× ganador: Horóscopo/Quiz), pero
    NO mística (esquiva la canibalización que mató al Tarot): perfil psicológico del DUEÑO leído en su colección real, framing
    ciencia/test genético. Self-focused («esto sos VOS» = hook de identidad más fuerte), screenshot-eable. 5-7 "genes" derivados
    de datos verificados (10 nativas, 11 frutales, palta clon, hiedra 400 años, romero a contramano). Push b (13:00). react
    target `adn`, sub qid `adn-suscripcion-diaria`.
  - **Cola ciclo 44:** (a) 08:30 🚨 Exclusiva; (b) 13:00 🧬 ADN; (c) 18:00 🎙️ Entrevista (rotación descansada 6 días, celebridad
    sub-converter). + 08:00 task-día (Hortensia B-5a, trasplante) + 09:00 top3 (tocaba por ancla). 3 ángulos distintos: chisme, identidad, celebridad.
- **Watch 44:** (1) ¿la Exclusiva (chisme+celebridad) rompe la racha de 8 fallos y reconvierte? (2) ¿el ADN (identidad self-focused,
  no místico) convierte donde el Tarot no-abrió? (3) ¿aparecen por fin datos del Diario re-push (13/07 slot c) y del Feed (12/07)?
  (4) Si las 2 nuevas no juntan aprobación con ventana limpia, se dropean el 15/07. **El 16/07 TOCA top3** y descansan Récords/Chusmerío (libres para slot c).

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA en julio);
  palta B-22/B-36 y pindó B-8 con fruto hasta jul-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37 último
  en pelarse; pera B-39); perennes verdes (guayabo F-1, mirto B-27, hiedra B-15). Heladas tardías pegan más al **sur y al este al amanecer**.
- Tareas activas urgentes reales: Guayabo F-1-4 fumagina + plaga (alta). Gardenia B-25 pulgones + hormigas (alta).
  Liquidámbar B-37 limpieza de copa en dormancia (alta, cuando pierda TODAS las hojas ~julio).

## Verificados clave (stats consistentes entre experiencias — NO contradecir)

52 especies · 65 id_codes · 10 nativas (F-1,F-8,B-8,B-14,B-16,B-29,B-32,B-34,B-42,B-47) · 30 perennes · 15 caducos ·
11 frutales · romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 meses (híbrido cidro×naranja, cáscara 4× vit C) ·
palta Hass B-36 = clon de 1 árbol de 1926 · anacahuita B-16 = protegida por ley desde 1986 · hiedra B-15 = +400 años ·
cinta B-12 = purifica aire (lista NASA) · liquidámbar B-37 = storax/"ámbar líquido" (mayas lo masticaban) ·
mirto B-27 = sagrado para Venus · aguaribay F-8 = verdadera pimienta rosa (sagrado incas/guaraníes) ·
mandarina B-24 = cítrico más antiguo (3000 a.C.) · guayabo F-1 = nativo, pétalos comestibles dulces.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial ✓, superlativos ✓, red-social ✓, tabloide ✓, identidad (Horóscopo/Quiz/Tarot-hoy) ✓,
  celebridad ✓, humor/consejo/confesión/reality (tibios), app-amada: Wrapped ✓ / Álbum ✓ / BeReal-hoy / JardínFlix ✗ / Historias ✗ /
  Podcast ✗, gesto: Álbum ✓ / Raspadita ✗, editorial-doc: Documental ✗.
  **Sin usar (posibles ganadores):** before/after con fotos del usuario (esperar más uploads); otras app-amadas SOLO con héroe/gesto
  (Duolingo-racha, mapa Pokémon-GO); Wordle/juego-diario compartible (grid). Evitar más gesto-desechable y editorial-pasivo.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
