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
- 15/07 slot c → 🍵 Chusmerío (sent 21:29Z) — SIN DATOS (ventana en blanco, ver drought). **16/07 slot c → 🏆 Récords** (descansado desde 09/07 = 7 días, orgullo/número, converter 141s+😍+sub). NO doblé identidad ni celebridad con las 2 nuevas de hoy (jardinero=identidad, declaraciones=celebridad) → Récords (orgullo) es 3er ángulo limpio.
- Candidatas descansadas próximas: Horóscopo (rest desde 11/07 — OJO no el mismo día que jardinero-sos: doble-identidad), Diario, Chusmerío (usado 15/07). Récords queda "usado" tras hoy.

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
- ⚠️ **DROUGHT DE INTERACCIÓN 15-16/07:** engagement.json último evento **2026-07-14T17:38Z** — CERO eventos nuevos en ~40h.
  Las 3 push del 15/07 (Cable a, Carnet b, Chusmerío c) + task-dia se enviaron TODAS OK (send_log 201), pero el usuario NO abrió
  nada. Esto NO refuta los ángulos (Cable=editorial-estatus, Carnet=user-hero-rango quedan SIN TESTEAR) — es ausencia/fatiga del usuario.
  Watch 16/07: si sigue en blanco tras hoy = fatiga real → bajar intensidad y apoyarse en task-dia (canal más confiable). Si abre = era ausencia puntual.
- **Compactación 16/07:** 01/07 movido a daily_summary (engagement {sent3/clic3/visits5/appr2} + send_log {sent3}). Ventana viva **02/07–14/07** (nada nuevo).
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **08-10/07 (última tanda GANADORA)** — Entrevista (sub+206s), Quiz (😍+103s), Wrapped (😍+172s), Álbum (😍) → 4 PROMOVIDAS. Récords/Chusmerío slot c re-push → re-sub SÍ.
- **11-14/07 (racha de fallos)** — Historias/Podcast/BeReal (app-pasiva), Raspadita (gesto), Documental (editorial-pasivo), Tarot (mística canibaliza),
  y 14/07 Exclusiva (chisme+celebridad pero nota-larga, 33s/22%) + ADN (identidad self-focused, lectura INCONCLUSA a 11s del cutoff). TODOS DROPPED.
- **15/07 (SIN DATOS — ventana en blanco):** Cable (editorial-estatus), Carnet (user-hero-rango), Chusmerío-c: las 3 se ENVIARON OK pero el usuario
  no abrió NINGUNA en ~40h. NO es señal de contenido: es AUSENCIA. push1/push2/push3 del 15/07 = 0 opens, 0 conv, 0 nada. Conclusión honesta: el
  canal quedó mudo, no hay aprendizaje de contenido posible del 15/07. Los 3 ángulos siguen sin refutar.
- **Meta-conclusión:** convierten social/celebridad-individual/identidad/chisme/orgullo/editorial-con-voz/**app-amada con héroe=usuario** —
  NUNCA gesto solo, editorial pasivo, app pasiva, ni el ángulo-bueno-en-formato-malo (nota-única-larga). FOCO INDIVIDUAL + PRESENTE + asombro/dwell alto.
  La suscripción la gana la familia EDITORIAL/PRENSA + asombro y el USER-HERO con logro persistente, no el CTA forzado.
- **⚠️ Lección operativa nueva (16/07):** cuando la ventana está EN BLANCO, no re-anclar en los ángulos untested (quedan pendientes de dato); volver a
  ángulos CON conversión previa comprobada para maximizar el chance de re-enganche, y vigilar la señal binaria «¿volvió?» antes que cualquier matiz de contenido.

## 🔭 Corrida 16/07 — ciclo 46 (esta corrida)

- **Proposals resueltas:** Cable (prensa-mundial)→DROPPED, Carnet (carnet-jardinero)→DROPPED — ambas por la regla no-supervivencia (sin aprobación
  de un día anterior), PERO con VENTANA EN BLANCO: cero interacción 15/07 (ver drought). Sus ángulos (editorial-estatus / user-hero-rango) quedan
  SIN TESTEAR, NO refutados — reintentables cuando el usuario vuelva. Páginas+pitches git rm. También reconcilié 2 stragglers 12/07 (raspadita,
  documental) que seguían "pending" con el archivo ya borrado → status dropped.
- **DECISIÓN:** ante la drought (no sé qué pasó con Cable/Carnet), vuelvo a 2 ejes CON DATOS DE CONVERSIÓN PREVIA (no los untested), cada uno FEED
  de ítems cortos, ambos self/individual + presente + asombro:
- **2 experiencias NUEVAS de cero (pending, created=16/07):**
  - 🧭 **¿Qué jardinero sos?** (`engage/2026-07-16-jardinero-sos.html`) — familia IDENTIDAD-self (Quiz 😍+103s, Horóscopo sub+😍 CONVIRTIERON).
    Fresco: no «qué planta sos» sino «qué JARDINERO sos» → el USUARIO es el héroe. Feed de 6 evidencias reales (10 nativas, ley 1986 B-16, hiedra
    400a B-15, Chanel Nº22 B-25, palta clon 1926 B-36, romero en flor B-26, limonero 12/12 B-23) que corona en arquetipo compartible «Curador de
    Rarezas». Push a (08:30). react `jardinero`, sub `jardinero-suscripcion-diaria`.
  - 🎙️ **Declaraciones — tus plantas hablan** (`engage/2026-07-16-declaraciones.html`) — familia CELEBRIDAD/1ª-persona (Entrevista sub+206s CONVIRTIÓ)
    servida como FEED de 8 soundbites CORTOS (el fix del 14/07 vs nota-larga). Cada planta = celebridad con frase punzante sobre dato real; 3 «declaran
    ahora» anclan en el presente (romero en flor, gardenia B-25 + guayabo F-1 con tarea activa real). Push b (13:00). react `declaraciones`, sub `declaraciones-suscripcion-diaria`.
  - **Cola ciclo 46:** (a) 08:30 🧭 Jardinero; (b) 13:00 🎙️ Declaraciones; (c) 18:00 🏆 Récords (rotación descansada 7 días, orgullo sub-converter).
    + 08:00 task-día (Guayabo F-1 fumagina+plaga) + 09:00 top3 (TOCÓ: Gardenia/Guayabo/Liquidámbar). 3 ángulos distintos: identidad / celebridad / orgullo.
- **Watch 46:** (1) ¿VUELVE el usuario? La señal #1 es si hay CUALQUIER evento tras 40h de silencio. (2) ¿jardinero-sos (identidad-user-hero) e/o
  declaraciones (celebridad-feed-corto) convierten y rompen la drought? (3) Si sigue TODO en blanco mañana = fatiga confirmada → bajar a 2 push/día
  o apoyarse casi solo en task-dia. (4) Si las 2 nuevas no juntan aprobación con ventana limpia, se dropean el 17/07; quedan Horóscopo/Diario/Chusmerío
  descansadas para slot c (no doble-identidad con jardinero si aún vivo). (5) Cable/Carnet reintentables cuando haya datos.

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
