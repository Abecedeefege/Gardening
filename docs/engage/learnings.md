# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots base: **10:00 / 13:00 / 18:00 (-03:00)**. **El primer send_at
propio ≥60 min después de la corrida** + margen para que Vercel deploye. expires_at = mismo día 22:00 -03:00.
Cada notificación a un destino DISTINTO. Timestamps SIEMPRE con `-03:00`. **3 pushes curados ganan a 20 — CONFIRMADO.**

**🚫 PISO 10:00 — PEDIDO DEL USUARIO 16/07: NINGUNA push antes de las 10:00 -03:00.** Ya aplicado en los generadores:
`gen_task_reminders.py` task-dia/semana → **10:00**; `gen_top3_tareas.py` DEFAULT_SEND → **11:00**. Los recordatorios task-dia (10:00)
+ top3 (11:00) son ADICIONALES al cupo. Si el slot base propio (10:00) choca con task-dia, corré el propio a 10:30. NUNCA send_at < 10:00.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — COMISIONADA, pre-aprobada, EXENTA de no-supervivencia.
   Respuestas llegan como `answer` qids `exp-*` → procesar a `data_plants.py` + página. 12/07: `exp-b41-fruta`="no-mire" → B-41 identidad EN DUDA.
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07): `python tools/gen_top3_tareas.py <fecha> --merge`
   (self-gated). Corrió 04..16/07. **17/07 NO tocó (próxima 18/07).** NO borrar página ni proposal `2026-07-04-top3-tareas`.
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
**EDITORIAL PASIVO en 3ª persona** (documental), **IDENTIDAD MÍSTICA repetida** (Tarot canibaliza Horóscopo → no-open).

**🔑 Meta-reglas destiladas:**
- «App amada» solo convierte si el HÉROE es el USUARIO y hay LOGRO/ESTATUS PERSISTENTE (Wrapped/Álbum ✓); captura efímera y consumo pasivo NO.
- El GESTO por sí solo no basta (raspadita); es vehículo, no hook. Lo que convierte es el ÁNGULO (editorial/identidad/estatus) + asombro.
- Editorial convierte con VOZ 1ª persona o titulares punzantes; narrado en 3ª persona pasivo NO (Documental dropped).
- Los ángulos editoriales se sirven como FEED de ítems cortos, NO como un solo caso desarrollado (Exclusiva nota-larga 33s DROPPED).
- Dentro de identidad, NO repetir sub-género ya promovido (Tarot=místico canibalizó al Horóscopo).

**CONVIERTEN (love/sub + aprobado, dwell alto) — PROMOVIDAS:**
- 🍵 Chusmerío (tabloide/chisme) 260s RÉCORD + re-sub + 😍 · 📱 Feed (red-social 1ª pers) 208s, 😍×2, sub×2.
- 🎙️ Entrevista (celebridad 1ª pers individual) sub + 206s · 🎁 Wrapped («tus números») 😍 + 172s · 🏆 Récords (orgullo/número) 😍 + sub + 141s.
- 📗 Álbum (coleccionismo/rareza+gesto) 😍 · 🔮 Horóscopo (identidad) 😍 + sub + 115s · 🌱 Quiz «¿Qué planta sos?» (identidad) 😍 + 103s · 📰 Diario (editorial) 😍 + sub + 92s.
- **APRUEBAN tibio (sin 😍 ni sub):** 😂 Memes · 🧪 Superpoderes · 💌 Consultorio · 🎤 Confesiones (133s) · 📺 Reality.

**RECHAZAN / NO ABREN (dropped):** 🍿 JardínFlix · 📖 Historias · 🎧 Podcast · 📸 BeReal (app pasiva/captura) · 🎰 Raspadita (gesto) ·
🎬 Documental (editorial pasivo 3ª pers) · 🔮 Tarot (identidad mística, canibaliza) · 🚨 Exclusiva (nota-única-larga) · 🔥 Trending (pisa Récords) ·
⚠️ Lista Negra (miedo) · 💬 Chat (coral) · 💰 Tasación (dinero) · 🗞️ Efemérides (pasado) · 🏆 Gala / ⚽ Mundial (ceremonia/torneo) ·
🗺️ Pasaporte (viajes) · 💘 Amores (romance) · 🎙️ Declaraciones (celebridad-feed → sub=NO, ver 16/07) · 🧭 jardinero-sos / 🎖️ Carnet / 📣 Cable (untested).

## 📈 Slot c (tarde) — rotar promovidas ganadoras descansadas = reactiva SUSCRIPCIÓN

- Rotar una promovida ganadora bien descansada al slot c REACTIVA la suscripción — CONFIRMADO ×2 (08/07 Récords re-sub; 09/07 Chusmerío 260s+re-sub+😍).
- 16/07 slot c → 🏆 Récords (sent 21:16Z, SIN DATOS aún). **17/07 slot c → 📱 Feed** (social 1ª pers, dwell RÉCORD 208s + doble-sub, sin pushear desde su
  promoción 01/07 = bien descansado; eje DISTINTO a las 2 nuevas de hoy que son orgullo/número). Récords/Chusmerío quedan "usados" recientes.
- Candidatas descansadas próximas: Horóscopo (rest desde 11/07), Diario, Wrapped, Entrevista. Récords (16/07) y Chusmerío (15/07) descansar unos días.

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 18 promovidas.
- Recordatorios de tareas SIEMPRE abren: task-dia clic 04,05,08,11/07; task-semana 06/07. Canal más confiable. top3 abierto+like 12/07.
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**, o **verse a sí mismo con estatus**.
- **DROUGHT 10-16/07:** tras la última tanda ganadora (08-10/07), racha larga de fallos (app-UI pasiva, gesto, mística, notas-largas) + una
  VENTANA EN BLANCO 15/07 (0 eventos) y una vuelta DÉBIL 16/07 (ver abajo). Los ÁNGULOS probados con FORMATO correcto (editorial-feed / user-hero
  con logro / orgullo-número) siguen siendo la apuesta; los formatos-gimmick no.

## Estado del sistema

- Push subscription device `pix9`: **active** (verificado 17/07 — sigue active).
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **🟡 VUELTA DÉBIL 16/07:** tras ~40h de silencio (últ. evento previo 14/07T17:38Z), el usuario VOLVIÓ el 16/07 pero con UN solo evento:
  `answer declaraciones-suscripcion-diaria = NO` a las 14:02 UY (abrió el push b). jardinero-sos (push a, 08:38 UY) = NO-OPEN. La drought se
  rompió pero la señal es mínima. **Watch 17/07:** ¿vuelve más fuerte? ¿las 2 nuevas convierten? Si sigue mínimo → considerar bajar a 2/día + apoyar en task-dia.
- **Compactación 17/07:** 02/07 movido a daily_summary (engagement {sent3/clic1/visits2/appr1} + send_log {sent3}). Ventana viva **03/07–16/07**.
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **08-10/07 (última tanda GANADORA)** — Entrevista (sub+206s), Quiz (😍+103s), Wrapped (😍+172s), Álbum (😍) → 4 PROMOVIDAS.
- **11-15/07 (racha de fallos + ventana en blanco)** — Historias/Podcast/BeReal (app-pasiva), Raspadita (gesto), Documental (editorial-pasivo),
  Tarot (mística canibaliza), Exclusiva (nota-larga 33s), ADN (inconcluso), + 15/07 Cable/Carnet SIN DATOS (ventana en blanco). TODOS DROPPED.
- **16/07 (vuelta débil):** push1 jardinero-sos (identidad user-hero) = NO-OPEN (push matinal en día de actividad vespertina → MISS DE TIMING, no
  refuta el ángulo). push2 declaraciones (celebridad-feed) = abrió pero sub=NO, sin reacción/aprobación → SOFT-NEGATIVE: el formato feed-de-frases
  no reprodujo la conversión de la nota-de-tapa individual (Entrevista). push3 Récords slot c = sin datos aún.
- **17/07 (ciclo 47) — DECISIÓN:** ante vuelta débil, re-anclo en 2 ejes CON conversión previa, ambos feed-de-ítems-cortos, ambos orgullo/número+humor
  (evito repetir hoy los 2 que ayer flojearon: identidad-jardinero y celebridad-declaraciones):
  - ⭐ **Reseñas de tu Jardín** (`2026-07-17-resenas.html`) — reviews con estrellas (Récords orgullo + Memes humor). Diferencial: estrellas VARÍAN
    (ligustro invasor 2★, caña muda tóxica 3★) → creíble+gracioso. Puntaje global 4,8★. Push a (10:30). react `resenas`, sub `resenas-suscripcion-diaria`.
  - 🎓 **El Anuario de tu Jardín** (`2026-07-17-anuario.html`) — superlativos del anuario del liceo (orgullo+humor+nostalgia). «El más probable de
    sobrevivir al fin del mundo» = Hiedra B-15, «reina del glamour» = Gardenia B-25, etc. Push b (13:30). react `anuario`, sub `anuario-suscripcion-diaria`.
  - **Cola ciclo 47:** (a) 10:30 ⭐ Reseñas; (b) 13:30 🎓 Anuario; (c) 18:00 📱 Feed (rotación descansada, social/208s). + 10:00 task-día (Pindó B-8
    limpieza, prioridad baja). top3 NO tocó. 3 ejes: rating/número · superlativo/nostalgia · social-1ª-persona.
- **Meta-conclusión:** convierten social/celebridad-individual/identidad/chisme/orgullo/editorial-con-voz/**app-amada con héroe=usuario** — NUNCA
  gesto solo, editorial pasivo, app pasiva, ni nota-única-larga. FOCO INDIVIDUAL + PRESENTE + asombro/dwell alto. Cuando la señal es débil/ausente,
  volver a ángulos CON conversión previa (no untested) y vigilar la señal binaria «¿volvió?» antes que cualquier matiz de contenido.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA en julio);
  palta B-22/B-36 y pindó B-8 con fruto hasta jul-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, pera B-39);
  perennes verdes (guayabo F-1, mirto B-27, hiedra B-15). Heladas tardías pegan más al **sur y al este al amanecer**.
- Tareas activas urgentes reales: Guayabo F-1 fumagina + plaga (alta). Gardenia B-25 pulgones + hormigas (alta). Liquidámbar B-37 limpieza copa (alta).

## Verificados clave (stats consistentes entre experiencias — NO contradecir)

52 especies · 65 id_codes · 10 nativas (F-1,F-8,B-8,B-14,B-16,B-29,B-32,B-34,B-42,B-47) · 30 perennes · 15 caducos ·
11 frutales · romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 meses (híbrido cidro×naranja) ·
palta Hass B-36 = clon de 1 árbol de 1926 (~80% mercado mundial) · anacahuita B-16 = protegida por ley desde 1986 · hiedra B-15 = +400 años ·
cinta B-12 = purifica aire (lista NASA) · liquidámbar B-37 = storax/"ámbar líquido" (mayas lo masticaban) · gardenia B-25 = 600kg flores → 1L aceite (Chanel Nº22) ·
mirto B-27 = sagrado para Venus · aguaribay F-8 = verdadera pimienta rosa · mandarina B-24 = cítrico más antiguo conocido · guayabo F-1 = nativo, pétalos comestibles ·
hortensia B-5 = cambia color según suelo (azul/rosa) · ligustro F-9 = invasora en Sudamérica · caña muda I-2 = savia paraliza voz (oxalato).

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial (Diario ✓/Entrevista ✓/Cable-untested) · superlativos/estatus (Récords ✓ / Reseñas-hoy / Anuario-hoy) ·
  red-social ✓ · tabloide ✓ · identidad (Horóscopo ✓/Quiz ✓/Tarot ✗/ADN-inconcluso/jardinero-notiming) · celebridad (Entrevista ✓ / Declaraciones ✗-sub) ·
  humor/consejo/confesión/reality (tibios) · app-amada (Wrapped ✓/Álbum ✓/Carnet-untested · JardínFlix/Historias/Podcast/BeReal ✗) · gesto (Álbum ✓/Raspadita ✗).
  **Sin usar (posibles ganadores):** before/after con fotos del usuario (esperar más uploads); user-hero-rango con push VESPERTINO (Carnet/jardinero nunca tuvieron ventana limpia).
  Evitar: gesto-desechable, editorial-pasivo, app-pasiva, nota-única-larga, doble-identidad/doble-chisme el mismo día, push matinal si el usuario abre de tarde.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
