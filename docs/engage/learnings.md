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
   (self-gated). Corrió 04,06,08,10,12/07. **13/07 NO tocó. Próxima 14/07.** NO borrar página ni proposal `2026-07-04-top3-tareas`.
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

- Curios como destino propio = MUERTO. Curios solo DENTRO de experiencias.
- **08/07 Récords re-push → re-sub SÍ. 09/07 Chusmerío re-push → 260s RÉCORD + re-sub + 😍.** Rotar una promovida
  ganadora bien descansada al slot c REACTIVA la suscripción — CONFIRMADO ×2. Récords/Chusmerío usadas 08-09/07 →
  descansan hasta ~16/07. Feed usado 12/07 slot c (sin datos, sent 21:23Z tras cutoff).
- **13/07 slot c → 📰 Diario** (editorial sub-converter, MUY descansado: última promoción-push 29/06). Candidatas
  descansadas próximas: Entrevista (rest desde 08/07), Horóscopo (rest desde 11/07), Récords/Chusmerío (~16/07).

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 18 promovidas.
- Recordatorios de tareas SIEMPRE abren: task-dia clic 04,05,08,11/07; task-semana 06/07. Canal más confiable.
- top3 abierto+like 12/07. El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 13/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último evento **2026-07-12T21:26Z** (page_visit landing plant-F-1). Cubre el 12/07:
  Raspadita abierta 23s sin conv (~13:09 UY), exp-b41-fruta="no-mire" (16:09 UY), top3 clic+like (16:10 UY),
  Documental abierto vía push sin conv (16:24 UY). **Feed re-push (slot c) SIN datos** (sent 18:23 UY tras el cutoff).
- Compactación 13/07: 28/06 movido a daily_summary (engagement + send_log). Ventana viva **29/06–12/07**.
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **08/07** — Entrevista → GANADORA (sub+approved+206s) PROMOVIDA; Trending → DROPPED (pisa Récords); Récords slot c → re-sub SÍ.
- **09/07** — DÍA FUERTE. Quiz (identidad) 😍+approved+103s → PROMOVIDA. Wrapped («tus números») 😍+approved+172s → PROMOVIDA.
  Chusmerío slot c re-push → 260s RÉCORD + re-sub + 😍.
- **10/07** — Álbum (coleccionismo/app-amada CON gesto) 😍+approved → PROMOVIDA. JardínFlix (Netflix pasivo) → NO-OPEN → DROPPED.
- **11/07 (ciclo 41)** — Experimento sub-primero FRACASÓ. Historias (36s) + Podcast (27s), ambas app-amada pasiva → DROPPED.
  Con esto app-amada PASIVA va 0/3.
- **12/07 (ciclo 42)** — **PIVOT falló doble.** 🎰 Raspadita (GESTO activo) → abierta 23s, cero conv → DROPPED (el gesto
  desechable no basta). 🎬 Documental (editorial-prestigio, héroe presente) → abierto vía push, sin conv → DROPPED (editorial
  PASIVO en 3ª persona se lee como el Podcast). task-día (Liquidámbar) sin clic hasta cutoff; top3 clic+like; exp-* respondió (¡al fin!).
- **Meta-conclusión:** convierten social / celebridad-individual / identidad / chisme / orgullo-superlativo / editorial-con-voz /
  humor-tibio / **app-amada SOLO con héroe-gesto** — NUNCA el gesto solo ni el editorial pasivo. FOCO INDIVIDUAL + dato del
  PRESENTE + asombro/dwell alto. La suscripción la ganan la familia EDITORIAL/PRENSA + asombro, no el CTA forzado arriba.

## 🔭 Corrida 13/07 — ciclo 43 (esta corrida)

- **Proposals resueltas:** Raspadita→DROPPED (gesto desechable, 23s sin conv), Documental→DROPPED (editorial pasivo, sin conv).
- **2 experiencias NUEVAS de cero (pending, created=13/07) — vuelvo a los ejes SEGUROS tras el doble fallo del pivot:**
  - 🔮 **El Tarot del Jardín** (`engage/2026-07-13-tarot-jardin.html`) — IDENTIDAD (el eje que MÁS convirtió: Horóscopo 😍+sub,
    Quiz 😍). Tirada de 9 Arcanos Mayores flip-card; cada planta = un Arcano con mensaje de identidad + dato REAL (Palta clon
    1926=El Inmortal, Liquidámbar storax=El Alquimista, Romero floreciendo AHORA=Arcano del Día/vivo). Categoría de mayor retorno
    diario del planeta (tarot/horóscopo). El gesto (flip) es vehículo de un payload IDENTITARIO, no lotería. Push a (08:30).
  - 📸 **El BeReal de tu Jardín** (`engage/2026-07-13-bereal-jardin.html`) — meta-patrón «app-amada CON héroe/gesto» (Wrapped/Álbum ✓),
    con la app cuya gramática ES la suscripción diaria (BeReal: «es hora, sin filtro, ahora», push a hora random). Héroe = el
    presente real del invierno; gesto = dar vuelta la cámara frontal→trasera para revelar el dato verificado. 8 capturas. Suma
    1ª persona/social (Feed 208s). Distinto de la app-pasiva: acá HAY héroe+gesto. Push b (13:00). Orden normal (asombro→react→sub).
  - **Cola ciclo 43:** (a) 08:30 🔮 Tarot; (b) 13:00 📸 BeReal; (c) 18:00 📰 Diario (rotación descansada, editorial sub-converter,
    reactiva sub). + 08:00 task-semana (lunes, 7 tareas del mes → tareas.html). top3 NO tocó hoy (próx 14/07).
- **Watch 43:** (1) ¿la IDENTIDAD (Tarot) reconfirma conversión donde el gesto/editorial-pasivo fallaron? (2) ¿BeReal recupera la
  SUSCRIPCIÓN con héroe+gesto donde la app-pasiva 0/3 falló? (3) ¿aparece por fin data del Feed re-push 12/07? (4) ¿Diario re-push
  reactiva sub como Récords/Chusmerío? **El 14/07 TOCA top3.**

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
