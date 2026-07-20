# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🚨 FEEDBACK DIRECTO DEL USUARIO 18/07 (por chat — máxima autoridad, NO PISAR)

1. **«Me estás repitiendo una y otra vez los mismos funfacts de las mismas plantas»** (vio Se Comenta 10:30). → Sistema anti-repetición
   instalado: `facts_ledger.json` (leer ANTES de armar, actualizar DESPUÉS), planta featured descansa ≥7d, fact no se repite <14d,
   ≥70% elenco fresco. Los quemados al 18/07: romero(12 págs), limonero(11), guayabo/palta-Hass/anacahuita(10), buganvilia/palta-uy/
   viraró/liquidámbar/crespón(9). Cantera fresca: pitósporo, evónimo, fotinia, jazmines, mirto, ciruela amarilla, hortensia, bignonia,
   singonio, hibisco, rosa de Siria, madreselva, roble, lantana, palmeras B-47 (3-5 págs).
2. **Feedback de texto en TODAS las experiencias** → `engageFeedback()` en engage.js + auto-inyección al pie de toda página sin caja
   propia. Evento `feedback_text` = LA señal de mayor peso. Leerlos PRIMERO cada corrida; positivo=expandir, negativo=ese contenido
   NO VUELVE, pedido=ejecutar. Sin feedback = contenido «masomenos» (abrir no es éxito).
3. **Objetivo redefinido:** interacción + marca de buena + buen feedback. Innovar SIEMPRE (formatos nuevos > refritos). Libertad total
   de alcance («hacé LO QUE SEA», experiencias tan grandes y complejas como convenga).
4. **Re-push de promovida = contenido RENOVADO en la misma URL** (la sub prometió «versión fresca diaria»; re-mandar la página estática
   del 01/07 es repetición). Aplicado hoy: Horóscopo re-escrito entero (9 signos nuevos, elenco virgen) antes del slot c.

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
🗺️ Pasaporte (viajes) · 💘 Amores (romance) · 🎙️ Declaraciones (celebridad-feed → sub=NO) · 🔥 Racha (streak/mecánica-abstracta → NO-OPEN 19/07) ·
🕯️ Nombre y Apellido (biografías humanas = PASADO disfrazado de editorial → abre pero masomenos) · 🧭 jardinero-sos / 🎖️ Carnet / 📣 Cable (untested).

**🔑 Meta-regla NUEVA (20/07, tras 6 días flojos):** el GANCHO DE APERTURA necesita asombro/drama/curiosidad CONCRETA del PRESENTE de TUS plantas. Las mecánicas
abstractas de compromiso (racha) o los protagonistas del PASADO (biografías) NO abren, aunque pertenezcan a familias ganadoras. Editorial convierte solo cuando
el protagonista es el PRESENTE del jardín (Diario ✓), no una persona histórica (Nombre y Apellido ✗). **El ÚNICO canal que sigue convirtiendo en la sequía = las TAREAS**
(19/07 el usuario clickeó el reply-landing de la Gardenia B-25). Estrategia 20/07: bridgear experiencia ↔ tarea (Guardia/ER) + mecánica con suscripción NATIVA (Quiniela).

## 📈 Slot c (tarde) — rotar promovidas ganadoras descansadas = reactiva SUSCRIPCIÓN

- Rotar una promovida ganadora bien descansada al slot c REACTIVA la suscripción — CONFIRMADO ×2 (08/07 Récords re-sub; 09/07 Chusmerío 260s+re-sub+😍).
- **18/07 slot c → 🔮 Horóscopo RENOVADO** (misma URL, edición nueva «semana del 18/07»: 9 signos con elenco virgen — pindó/evónimo/rosa de Siria/
  azarero/esparraguera/madreselva/ciruela/roble/palmeras B-47). Regla nueva: rotar promovida = renovar contenido, NUNCA re-mandar estático.
- **18/07 mediodía:** Regalo del Invierno v2 (reescrito pre-push tras el reclamo de repetición: mandarina-fruta-HOY, lantana-semáforo, lavanda-sueño,
  hortensia-programable, hibisco-muro-norte — cero palta/limonero/romero) + caja de feedback propia. Watch: ¿la v2 convierte donde la v1 hubiese repetido?
- 17/07 slot c → 📱 Feed: abrió pero REBOTÓ (9s, 6% scroll) — social 1ª pers NO reactivó como esperaba (día flojo generalizado, no refuta el ángulo per se).
- Candidatas descansadas próximas: Diario, Wrapped, Entrevista, Álbum, Récords. Chusmerío (uso su FAMILIA hoy en Se Comenta) y Feed (17/07) descansar.

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 18 promovidas.
- Recordatorios de tareas SIEMPRE abren: task-dia clic 04,05,08,11/07; task-semana 06/07. Canal más confiable. top3 abierto+like 12/07.
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**, o **verse a sí mismo con estatus**.
- **DROUGHT 10-16/07:** tras la última tanda ganadora (08-10/07), racha larga de fallos (app-UI pasiva, gesto, mística, notas-largas) + una
  VENTANA EN BLANCO 15/07 (0 eventos) y una vuelta DÉBIL 16/07 (ver abajo). Los ÁNGULOS probados con FORMATO correcto (editorial-feed / user-hero
  con logro / orgullo-número) siguen siendo la apuesta; los formatos-gimmick no.

## Estado del sistema

- Push subscription device `pix9`: **active** (verificado 19/07 — sigue active).
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **🔴 SEÑAL DÉBIL SOSTENIDA 16-19/07 (6 días):** el usuario VUELVE cada día y a veces ABRE, pero NO convierte (0 reacción/sub/aprobación/feedback_text en 6 días).
  19/07 (ciclo 49): Racha (streak) NO-OPEN; Nombre y Apellido (biografías) abrió 15:55 UY pero sin señal (masomenos); Quiz renovado NO-OPEN. **PERO** el usuario clickeó
  el reply-landing de la Gardenia (B-25-3, tarea) → **el canal TAREAS es el único que sigue convirtiendo.** El cuello NO es el canal push (anda); es el GANCHO de las
  experiencias. **Watch 20/07:** ¿convierte (a) la GUARDIA/ER que bridgea con el canal-tarea + drama, o (b) la QUINIELA con suscripción nativa? Si sigue 0-conversión
  el 21/07 → bajar a 2/día propias + reforzar el canal-tarea (task-día/top3/replies), que es lo único que abre+convierte de forma consistente.
- **Compactación 20/07:** 05/07 movido a daily_summary. Ventana viva **06/07–20/07**. (04/07 ya estaba resumido.)
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).
- **🐛 Fix 20/07:** el Diario (promovido) tenía un ERROR real — su lead presentaba al caqui B-41 «cargado de fruta de oro», pero B-41 tiene identidad EN DUDA
  y NUNCA confirmó fruto (learnings 04/07). Se corrigió al renovarlo: lead nuevo = mandioca brava B-34 (cianuro). Credibilidad primero.

## Conclusiones de los pushN enviados (por feedback real)

- **08-10/07 (última tanda GANADORA)** — Entrevista (sub+206s), Quiz (😍+103s), Wrapped (😍+172s), Álbum (😍) → 4 PROMOVIDAS.
- **11-17/07 (racha larga de fallos)** — app-pasiva (Historias/Podcast/BeReal), gesto (Raspadita), editorial-pasivo (Documental), mística (Tarot),
  nota-larga (Exclusiva 33s), celebridad-feed-de-frases (Declaraciones, sub=NO), y **orgullo/superlativo-sobre-PLANTAS fatigado** (Reseñas 3s-rebote / Anuario
  12s-100%-sin-convertir, 17/07: dos superlativos el mismo día saturó). TODOS DROPPED. Timing: push matinal en día de actividad vespertina = MISS (jardinero-sos 16/07).
- **18/07 (ciclo 48) — DECISIÓN:** ante 4º día flojo, cambio de EJE (no más orgullo-superlativo-sobre-plantas) y vuelvo a las 2 familias que más
  convirtieron, cada una en un eje bien distinto:
  - 🗣️ **Se Comenta en el Cantero** (`2026-07-18-secomenta.html`) — CHISME/tabloide (familia Chusmerío = 260s RÉCORD +😍+re-sub), rebrand fresco,
    rumores 100% verídicos anclados al PRESENTE (romero en flor, guayabo con drama). Push a (10:30). react `secomenta`, sub `secomenta-suscripcion-diaria`.
  - 🎁 **El Regalo del Invierno** (`2026-07-18-regalo-invierno.html`) — USER-HERO/gratitud (familia Wrapped/Álbum = las 😍): héroe=USUARIO, «todo lo que
    tu jardín te da hoy» (52 especies vivas, limón 365 días, romero en flor). Da vuelta la cámara: gratitud, no tareas. Push b (13:00). react `regalo`, sub `regalo-suscripcion-diaria`.
  - **Cola ciclo 48:** (a) 10:30 🗣️ Se Comenta; (b) 13:00 🎁 Regalo; (c) 18:00 🔮 Horóscopo (rotación descansada 7d, identidad 😍+sub). + 10:00 task-día
    (Guayabo F-1 fumagina, ALTA); 11:00 top3 (tocó hoy: Gardenia/Guayabo/Liquidámbar). 3 ejes: chisme · user-hero-gratitud · identidad.
- **18/07 (ciclo 48) — RESULTADO: 5º día flojo, 0 conversión.** Se Comenta (chisme) leyó 100%/15s pero pasivo → DROPPED (chisme fatigado). Regalo
  (gratitud) NO-OPEN → DROPPED (el hook no motivó apertura). Horóscopo renovado abrió a medianoche (timing) → sin señal. Chisme + gratitud-emotivo fuera por ahora.
- **19/07 (ciclo 49) — DECISIÓN:** ante 5 días flojos, dos apuestas NUEVAS en los dos ejes que MÁS convirtieron, cada una con un giro de formato nunca probado:
  - 🔥 **La Racha del Jardín** (`2026-07-19-racha-jardin.html`) — MECÁNICA DE RETENCIÓN (racha Duolingo) sobre user-hero+estatus-persistente (los 😍: Wrapped/Álbum/Récords).
    Optimizada para SUSCRIPCIÓN: «te aviso para no romperla» = el usuario pide la notif. Racha real (28d desde solsticio 21/06). Elenco fresco: Cinta B-12/Anacahuita B-16/Mirto B-27/Aguaribay F-8/Singonio I-1. Push a (10:30). react `racha-jardin`, sub `racha-jardin-suscripcion-diaria`.
  - 🕯️ **Nombre y Apellido** (`2026-07-19-nombre-apellido.html`) — EDITORIAL+AWE+INDIVIDUAL (Diario 😍+sub, Entrevista sub+206s): las biografías humanas reales
    detrás de los nombres científicos, feed de 6 ítems cortos. Lead=Jeanne Baret (buganvilia B-1, 1ª mujer en circunnavegar). Elenco fresco: B-1/F-7/B-9/B-13/B-42/F-4. Push b (13:00). react `nombre-apellido`, sub `nombre-apellido-suscripcion-diaria`.
  - **Slot c (18:00) → 🌱 Quiz «¿Qué planta sos?» RENOVADO** (identidad, 😍+103s, descansado 10d). Regla re-push=contenido nuevo: 6 resultados reescritos con elenco
    fresco NO-colisionante (Fresno F-10/Lapachillo B-14/Jazmín B-2/Viraró B-32/Jazmín de leche B-3/Fotinia F-3); preguntas+scoring intactos. Reactivar sub por identidad.
  - **Cola ciclo 49:** (a)10:30 Racha; (b)13:00 Nombre y Apellido; (c)18:00 Quiz-reno. + 10:00 task-día (Liquidámbar B-37 limpieza copa). top3 NO tocó (próx 20/07).
- **19/07 (ciclo 49) — RESULTADO: 6º día flojo, 0 conversión.** Racha (streak) NO-OPEN → DROPPED (mecánica abstracta no abre). Nombre y Apellido (biografías)
  abrió 15:55 UY sin señal → DROPPED (pasado disfrazado de editorial = masomenos). Quiz-reno NO-OPEN. Único hecho positivo: click al reply-landing de la Gardenia (tarea).
- **20/07 (ciclo 50) — DECISIÓN:** dos formatos NUEVOS, cada uno atacando un problema medido distinto:
  - 🩺 **La Guardia del Jardín** (`2026-07-20-guardia-jardin.html`) — ER/triage, user-hero=MÉDICO. Bridgea la experiencia con el ÚNICO canal que convierte (tareas):
    los críticos son tareas REALES (Gardenia B-25 pulgones — el task que el usuario tocó ayer; Liquidámbar B-37; Guayabo F-1). Drama + stakes, no mecánica abstracta
    (≠ Racha) ni balance sentimental (≠ Regalo). Sub nativa: «el pase de sala diario». Slot c (18:00, el mejor-abierto). react `guardia-jardin`, sub `guardia-jardin-suscripcion-diaria`.
  - 🎲 **La Quiniela del Jardín** (`2026-07-20-quiniela-jardin.html`) — prediccón/apuesta, formato NUNCA probado. Suscripción INTRÍNSECA (la notif ES el resultado que pediste,
    no interrupción) → ataca directo el gap de tasa-de-suscripción. Anclaje cultural rioplatense (quiniela). Jugadas reales sobre fenología verificada (carrera 1ª flor
    durazno B-30 vs pera B-39 en agosto, cosecha palta B-22, ¿otra helada?, invicto hiedra B-15). Slot a (10:30). react `quiniela-jardin`, sub `quiniela-jardin-suscripcion-diaria`.
  - **Slot b (13:00) → 📰 Diario RENOVADO** (rested winner, reactiva sub): edición «Lunes 20/07», lead corregido (caqui-error → mandioca brava B-34) + pitósporo B-43. Elenco fresco no-colisionante.
  - **Cola ciclo 50:** (a)10:30 Quiniela; (b)13:00 Diario-reno; (c)18:00 Guardia. + 10:00 task-semana (lunes) · 11:00 top3 (Gardenia/Guayabo/Liquidámbar). 3 ejes: apuesta-predicción · editorial-presente · guardia-ER-user-hero.
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

- **Ángulos NEWS-FEED usados:** editorial (Diario ✓/Entrevista ✓) · superlativos/estatus (Récords ✓ / Reseñas ✗ / Anuario ✗) · red-social ✓ ·
  tabloide ✓ · identidad (Horóscopo ✓/Quiz ✓/Tarot ✗) · celebridad (Entrevista ✓/Declaraciones ✗) · app-amada (Wrapped ✓/Álbum ✓ · pasivas ✗) ·
  gesto (Álbum ✓/Raspadita ✗) · gratitud/user-hero (Regalo-hoy). **Sin usar:** before/after con fotos del usuario; user-hero-rango vespertino.
  Evitar: gesto-desechable, editorial-pasivo, app-pasiva, nota-única-larga, dobles del mismo eje en el día, push matinal si abre de tarde.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
