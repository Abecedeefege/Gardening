# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots base: 08:30 / 13:00 / 18:00 (-03:00). **El primer send_at
propio ≥60 min después de la corrida** + margen para que Vercel deploye. expires_at = mismo día 22:00 -03:00.
Cada notificación a un destino DISTINTO. Timestamps SIEMPRE con `-03:00`. **3 pushes curados ganan a 20 — CONFIRMADO.**
El usuario abre 2-3/día. Los recordatorios task-dia/task-semana (08:00) + top3 (09:00) son ADICIONALES al cupo.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — COMISIONADA, pre-aprobada, EXENTA de la regla
   de no-supervivencia. Respuestas llegan como `answer` qids `exp-*`: procesarlas → `data_plants.py` + página.
   12/07: `exp-b41-fruta`="no-mire" (no miró si el caqui B-41 dio fruta) → B-41 sigue con identidad EN DUDA.
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07): `python tools/gen_top3_tareas.py <fecha> --merge`
   (self-gated). Corrió 04,06,08,10,12,14/07. **15/07 NO tocó (próxima 16/07).** NO borrar página ni proposal `2026-07-04-top3-tareas`.
3. **Dato clave**: B-41 "caqui" identidad EN DUDA (nunca flor ni fruto confirmado). No usarlo como curio de fruta.
4. Timeline: hechas/cerradas van colapsadas en "🗂️ Pasadas / hechas" (vista Todas).
5. **Splash** «Hora dorada» integrado en Home. Los 6 demos `engage/splash-*.html` = referencia: NO tocar.
6. ⚠️ **Pillow (PIL) no viene instalado** en el runner: `pip install Pillow` ANTES de correr los gen_*.py / build.py.

## 🆕 FUNCIÓN PARALELA (pedido 28/06): 2 experiencias NUEVAS de cero por corrida

Cada corrida inicializo persona product/UX/sales y construyo DOS experiencias news-feed de cero, cada una con:
(1) reacción final (engageReact target=slug), (2) CTA de **suscripción diaria** (engageAnswer qid `<slug>-suscripcion-diaria`),
(3) un **HTML de pitch** aparte con 6 modelos de monetización (3 innovadores + 3 ultra-creativos). Contrato de proposal igual
que siempre (link "← Volver al sitio estable" primero, react+sub+engage-actions reales, `engage.js`, SOLO datos verificados de
data_plants.py con código). Dos de los 3 pushes llevan a estas experiencias; el 3º rota una promovida ganadora descansada.

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide

**Convierten a SUSCRIPCIÓN:** familia EDITORIAL/PRENSA + alto asombro/dwell (Diario, Récords, Chusmerío, Entrevista,
Horóscopo → sub SÍ); ASOMBRO/ESTATUS/CHISME/IDENTIDAD/1ª-PERSONA-INDIVIDUAL/CELEBRIDAD + el DATO REAL DEL PRESENTE como
protagonista; **UI de app AMADA CON HÉROE=USUARIO + LOGRO/ESTATUS persistente** (Wrapped «tus números» 172s, Álbum «coleccionar/rareza»).
**NO convierten:** ficción-protagonista (torneo/gala/reality), utilidad seca, geografía/viajes, DINERO (tasación), PASADO
(efemérides/historia), MIEDO/PELIGRO, CHAT-GRUPAL coral, RANKING-del-presente (pisa Récords), **APP-AMADA de CONSUMO PASIVO**
(catálogo/player/stories/captura: JardínFlix, Historias 36s, Podcast 27s, BeReal 12s), **GESTO desechable** (raspadita 23s),
**EDITORIAL PASIVO en 3ª persona** (documental para "mirar"), **IDENTIDAD MÍSTICA repetida** (Tarot canibaliza Horóscopo → no-open).

**🔑 Meta-reglas destiladas:**
- «App amada» solo convierte si el HÉROE es el USUARIO y hay LOGRO/ESTATUS PERSISTENTE (Wrapped/Álbum ✓); captura efímera y consumo pasivo NO.
- El GESTO por sí solo no basta (raspadita); es vehículo, no hook. Lo que convierte es el ÁNGULO (editorial/identidad/estatus) + asombro.
- Editorial convierte con VOZ 1ª persona o titulares punzantes; narrado en 3ª persona pasivo NO (Documental dropped).
- Dentro de identidad, NO repetir sub-género ya promovido (Tarot=místico canibalizó al Horóscopo).

**CONVIERTEN (love/sub + aprobado, dwell alto) — PROMOVIDAS:**
- 🍵 Chusmerío (tabloide/chisme) 260s RÉCORD + re-sub + 😍 · 📱 Feed (red-social 1ª pers) 208s, 😍×2, sub×2.
- 🎙️ Entrevista (celebridad 1ª pers individual) sub + 206s · 🎁 Wrapped («tus números») 😍 + 172s · 🏆 Récords (orgullo/número) 😍 + sub + 141s.
- 📗 Álbum (coleccionismo/rareza+gesto) 😍 · 🔮 Horóscopo (identidad) 😍 + sub + 115s · 🌱 Quiz «¿Qué planta sos?» (identidad) 😍 + 103s · 📰 Diario (editorial) 😍 + sub + 92s.
- **APRUEBAN tibio (sin 😍 ni sub):** 😂 Memes · 🧪 Superpoderes · 💌 Consultorio · 🎤 Confesiones (133s) · 📺 Reality.

**RECHAZAN / NO ABREN (dropped):** 🍿 JardínFlix · 📖 Historias · 🎧 Podcast · 📸 BeReal (app pasiva/captura) · 🎰 Raspadita (gesto) ·
🎬 Documental (editorial pasivo 3ª pers) · 🔮 Tarot (identidad mística, canibaliza) · 🚨 Exclusiva (chisme+celebridad pero UN caso LARGO, ver abajo) ·
🔥 Trending (pisa Récords) · ⚠️ Lista Negra (miedo) · 💬 Chat (coral) · 💰 Tasación (dinero, 198s y rechazó) · 🗞️ Efemérides (pasado) ·
🏆 Gala / ⚽ Mundial (ceremonia/torneo) · 🗺️ Pasaporte (viajes) · 💘 Amores (romance).

**🔑 NUEVO 15/07 — «el ángulo bueno en el FORMATO malo tampoco convierte»:** La 🚨 Exclusiva (14/07) fusionó los 2 ejes MÁS
confiables (chisme Chusmerío 260s + celebridad Entrevista 206s) pero como UNA nota-bomba LARGA de un solo caso → lectura débil
33s/22%, cero conversión → DROPPED. El chisme/celebridad SIGUEN vivos (Chusmerío/Feed/Entrevista promovidos): lo que falló fue el
FORMATO nota-única-larga (build-up que cansa) vs el scroll rápido de muchos titulares cortos que retuvo al Chusmerío. Lección para
15/07 en adelante: los ángulos editoriales se sirven como FEED de ítems cortos, no como un solo caso desarrollado.

## 📈 Slot c (tarde) — rotar promovidas ganadoras descansadas = reactiva SUSCRIPCIÓN

- Rotar una promovida ganadora bien descansada al slot c REACTIVA la suscripción — CONFIRMADO ×2 (08/07 Récords re-sub; 09/07 Chusmerío 260s+re-sub+😍).
- 14/07 slot c → 🎙️ Entrevista (sent 21:14Z, tras cutoff → sin datos). **15/07 slot c → 🍵 Chusmerío** (descansado desde 09/07 = 6 días, chisme sub-converter 260s).
- Candidatas descansadas próximas: Récords (rest desde 09/07), Horóscopo (rest desde 11/07), Diario. Chusmerío queda "usado" tras hoy. NO doble-chisme ni doble-identidad el mismo día.

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 18 promovidas.
- Recordatorios de tareas SIEMPRE abren: task-dia clic 04,05,08,11/07; task-semana 06/07. Canal más confiable. top3 abierto+like 12/07.
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**, o **verse a sí mismo con estatus**.
- **DROUGHT de conversión desde 10/07 (Álbum):** 11-14/07 = racha de fallos (app-UI pasiva, gesto, mística, y el 14/07 Exclusiva/ADN con
  lecturas débiles/incompletas). Los ÁNGULOS-de-contenido probados (Entrevista/Quiz/Wrapped/Álbum 08-10/07) convierten; los formatos-gimmick
  y las notas-largas no. Ciclo 45 re-ancla FUERTE en 2 ejes probados con FORMATO correcto: editorial-estatus como FEED de titulares + user-hero-rango.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 13/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último evento **2026-07-14T17:38Z** (ADN abierto 14:37 UY, dwell 11s). Cubre el 14/07 hasta ahí:
  Exclusiva lectura 33s/22% (browse directo ~12:41 UY, sin conv); ADN abierto vía push 11s ANTES del cutoff (INCONCLUSO). NO cubre:
  slot c Entrevista (sent 21:14Z tras cutoff → sin datos).
- **Compactación 15/07:** 30/06 movido a daily_summary (engagement {sent3/clic5/visits6/appr4} + send_log {sent3}). Ventana viva **01/07–14/07**.
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **08-10/07 (última tanda GANADORA)** — Entrevista (sub+206s), Quiz (😍+103s), Wrapped (😍+172s), Álbum (😍) → 4 PROMOVIDAS. Récords/Chusmerío slot c re-push → re-sub SÍ.
- **11-14/07 (racha de fallos)** — Historias/Podcast/BeReal (app-pasiva), Raspadita (gesto), Documental (editorial-pasivo), Tarot (mística canibaliza),
  y 14/07 Exclusiva (chisme+celebridad pero nota-larga, 33s/22%) + ADN (identidad self-focused, lectura INCONCLUSA a 11s del cutoff). TODOS DROPPED.
- **Meta-conclusión:** convierten social/celebridad-individual/identidad/chisme/orgullo/editorial-con-voz/**app-amada con héroe=usuario** —
  NUNCA gesto solo, editorial pasivo, app pasiva, ni el ángulo-bueno-en-formato-malo (nota-única-larga). FOCO INDIVIDUAL + PRESENTE + asombro/dwell alto.
  La suscripción la gana la familia EDITORIAL/PRENSA + asombro y el USER-HERO con logro persistente, no el CTA forzado.

## 🔭 Corrida 15/07 — ciclo 45 (esta corrida)

- **Proposals resueltas:** Exclusiva→DROPPED (chisme+celebridad OK pero nota-larga, 33s/22% sin conv), ADN→DROPPED por la regla (lectura
  INCONCLUSA, abierto 11s antes del cutoff — NO concluir que identidad self-focused está muerta). Ambas páginas+pitches git rm.
- **DECISIÓN:** re-ancla FUERTE en los 2 ejes MÁS probados, cada uno con el FORMATO correcto (la lección del 14/07):
- **2 experiencias NUEVAS de cero (pending, created=15/07):**
  - 📣 **El Cable — el mundo habla de tu jardín** (`engage/2026-07-15-prensa-mundial.html`) — EDITORIAL/PRENSA + ESTATUS, ángulo FRESCO:
    agencia de noticias internacional, 8 despachos CORTOS (feed, no nota-larga) donde el mundo REAL (NASA, ley uruguaya 1986, Chanel Nº22,
    ciencia memoria, arqueología maya) habló de UNA planta suya. Estatus prestado de máxima autoridad + PRESENTE (romero en flor, cosechas).
    Esquiva canibalizar Récords (leaderboard interno) y Chusmerío (chisme). Push a (08:30). react `prensa`, sub `prensa-suscripcion-diaria`.
  - 🎖️ **El Carnet de Jardinero** (`engage/2026-07-15-carnet-jardinero.html`) — META-PATRÓN GANADOR «app amada, héroe=USUARIO, logro persistente»
    (Wrapped/Álbum) + identidad self-focused + orgullo. Perfil de jugador estilo Duolingo/Steam: rango LEYENDA, XP al próximo nivel, medallero de
    8 logros REALES (anacahuita protegida por ley B-16, hiedra 400 años B-15, cinta NASA B-12, palta clon B-36), misión del día atada a acciones
    reales. El usuario es la estrella, screenshot-eable. Push b (13:00). react `carnet`, sub `carnet-suscripcion-diaria`.
  - **Cola ciclo 45:** (a) 08:30 📣 El Cable; (b) 13:00 🎖️ Carnet; (c) 18:00 🍵 Chusmerío (rotación descansada 6 días, sub-converter).
    + 08:00 task-día (Gardenia B-25 pulgones+hormigas). Top3 NO tocó (próx 16/07). 3 ángulos distintos: editorial-estatus / user-hero / chisme.
- **Watch 45:** (1) ¿el re-ancla en 2 ejes probados con FORMATO correcto rompe la drought de conversión (5 días sin sub/love)? (2) ¿el Cable
  (editorial-estatus como FEED de titulares) convierte donde la Exclusiva (nota-larga) no? (3) ¿el Carnet (user-hero rango) iguala a Wrapped/Álbum?
  (4) Si hay FATIGA real (varios días sin ningún click a experiencias), bajar intensidad / apoyarse más en task-dia (canal confiable). (5) Si las 2
  nuevas no juntan aprobación con ventana limpia, se dropean el 16/07 — que TOCA top3, y quedan libres Récords/Horóscopo para slot c.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA en julio);
  palta B-22/B-36 y pindó B-8 con fruto hasta jul-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37 último en pelarse; pera B-39);
  perennes verdes (guayabo F-1, mirto B-27, hiedra B-15). Heladas tardías pegan más al **sur y al este al amanecer**.
- Tareas activas urgentes reales: Guayabo F-1 fumagina + plaga (alta). Gardenia B-25 pulgones + hormigas (alta). Liquidámbar B-37 limpieza de copa en dormancia (alta).

## Verificados clave (stats consistentes entre experiencias — NO contradecir)

52 especies · 65 id_codes · 10 nativas (F-1,F-8,B-8,B-14,B-16,B-29,B-32,B-34,B-42,B-47) · 30 perennes · 15 caducos ·
11 frutales · romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 meses (híbrido cidro×naranja, cáscara 4× vit C) ·
palta Hass B-36 = clon de 1 árbol de 1926 (~80% mercado mundial) · anacahuita B-16 = protegida por ley desde 1986 · hiedra B-15 = +400 años ·
cinta B-12 = purifica aire (lista NASA, ~10m²) · liquidámbar B-37 = storax/"ámbar líquido" (mayas lo masticaban) · gardenia B-25 = 600kg flores → 1L aceite (Chanel Nº22) ·
mirto B-27 = sagrado para Venus · aguaribay F-8 = verdadera pimienta rosa (sagrado incas/guaraníes) · mandarina B-24 = cítrico más antiguo (3000 a.C.) · guayabo F-1 = nativo, pétalos comestibles.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial (Diario ✓ / Entrevista ✓ / Cable-hoy) · superlativos/estatus (Récords ✓) · red-social ✓ · tabloide ✓ ·
  identidad (Horóscopo ✓ / Quiz ✓ / Tarot ✗ / ADN-inconcluso) · celebridad ✓ · humor/consejo/confesión/reality (tibios) · app-amada (Wrapped ✓ / Álbum ✓ /
  Carnet-hoy · JardínFlix ✗ / Historias ✗ / Podcast ✗ / BeReal ✗) · gesto (Álbum ✓ / Raspadita ✗) · editorial-doc ✗.
  **Sin usar (posibles ganadores):** before/after con fotos del usuario (esperar más uploads); Wordle/juego-diario compartible (grid, con cuidado — juegos fatigaron).
  Evitar: gesto-desechable, editorial-pasivo, app-pasiva, nota-única-larga, doble-identidad/doble-chisme el mismo día.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
