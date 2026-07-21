# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🚨 FEEDBACK DIRECTO DEL USUARIO 18/07 (por chat — máxima autoridad, NO PISAR)

1. **«Me repetís los mismos funfacts de las mismas plantas»** → anti-repetición: `facts_ledger.json` (leer ANTES, actualizar DESPUÉS),
   planta featured descansa ≥7d, fact no se repite <14d, ≥70% elenco fresco. **⚠️ 21/07: la sequía forzó rotación pesada → CASI TODO el
   elenco quedó featured en 7d.** Cantera genuinamente fresca hoy: F-2 (Podranea), F-5 (coronita), B-41 (caqui id-en-duda), B-46 (vivero),
   B-49 (trifoliado misterio), B-20/B-45 (sin identificar). Estrategia: protagonistas frescos + a los quemados solo tocarlos por ÁNGULO NUEVO (tarea real), nunca repitiendo su fun_fact.
2. **Feedback de texto = LA señal de mayor peso.** Leer `feedback_text` PRIMERO. Positivo=expandir, negativo=NUNCA vuelve, pedido=ejecutar.
   Sin feedback = «masomenos» (abrir no es éxito). **0 eventos `feedback_text` hasta hoy.**
3. **Objetivo:** interacción + marca de buena + buen feedback. Innovar SIEMPRE (formatos nuevos > refritos).
4. **Re-push de promovida = contenido RENOVADO en la misma URL** (nunca re-mandar estático).

## ⏱️ CADENCIA VIGENTE: 3 pushes propios/día (fijada 18/06)

Slots base **10:00 / 13:00 / 18:00 -03:00**; ajustables. **🚫 PISO 10:00 (pedido 16/07): NINGUNA push antes de 10:00.**
task-dia (10:00) + top3 (11:00, cada 2d) son ADICIONALES al cupo — si mi slot base choca con task-dia, corro el propio a 10:30.
Primer send_at propio ≥60 min post-corrida. expires_at = mismo día 22:00. Cada notif a destino DISTINTO. Timestamps con `-03:00`.
**Instrucción permanente de la Routine: la cola SIEMPRE se pushea con 3 notifs propias pending.** (Aunque la sequía tiente a bajar a 2/día,
la regla dura es 3: el 3º slot lo cubro con rotación de una promovida ganadora descansada = bajo costo.)

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`2026-07-04-expedientes-jardin.html`) — COMISIONADA, pre-aprobada, EXENTA de no-supervivencia. `answer` qids `exp-*`.
   12/07: `exp-b41-fruta`="no-mire" → B-41 identidad EN DUDA (nunca flor ni fruto). No usarlo como curio de fruta.
2. **🎯 Top 3** (`top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07): `gen_top3_tareas.py <fecha> --merge` (self-gated). Corrió 20/07;
   **21/07 NO tocó (próx 22/07).** NO borrar página ni proposal `2026-07-04-top3-tareas`.
3. Timeline: hechas/cerradas colapsadas en "🗂️ Pasadas / hechas".
4. **Splash** «Hora dorada» integrado en Home. Demos `splash-*.html` = referencia, NO tocar.
5. ⚠️ **Pillow (PIL) no viene instalado:** `pip install Pillow` ANTES de gen_*.py / build.py.

## 🆕 FUNCIÓN PARALELA (28/06): 2 experiencias NUEVAS de cero por corrida

Persona product/UX/growth/sales. Cada una: (1) reacción final `engageReact` target=slug, (2) CTA suscripción diaria `engageAnswer` qid
`<slug>-suscripcion-diaria`, (3) caja de feedback propia `engageFeedback('<slug>')`, (4) HTML de pitch aparte con 6 modelos de monetización
(3 innovadores + 3 ultra-creativos). Contrato: link "← Volver al sitio estable" PRIMERO, `engage.js` al pie, SOLO datos verificados con código.

## 🚀 QUÉ CONVIERTE — el ÁNGULO decide dentro del news-feed

**CONVIERTEN (love/sub, dwell alto) — PROMOVIDAS:** 🍵 Chusmerío 260s+😍+re-sub · 📱 Feed(social 1ª pers) 208s😍×2 · 🎙️ Entrevista(celebridad
individual) sub+206s · 🎁 Wrapped(«tus números»/user-hero) 😍+172s · 🏆 Récords(orgullo/número) 😍+sub+141s · 📗 Álbum(coleccionismo) 😍 ·
🔮 Horóscopo(identidad) 😍+sub · 🌱 Quiz «¿qué planta sos?»(identidad) 😍+103s · 📰 Diario(editorial-presente) 😍+sub · 😂Memes/🧪Superpoderes/💌Consultorio/🎤Confesiones/📺Reality (aprueban tibio).

**RECHAZAN/NO ABREN (dropped):** app pasiva (JardínFlix/Historias/Podcast/BeReal) · gesto solo (Raspadita) · editorial pasivo 3ª pers (Documental) ·
identidad mística repetida (Tarot canibaliza Horóscopo) · nota-única-larga (Exclusiva 33s) · ranking-presente (Trending pisa Récords) · miedo (Lista Negra) ·
chat coral · dinero (Tasación) · pasado (Efemérides / **Nombre y Apellido**=biografías humanas) · ceremonia/torneo (Gala/Mundial) · viajes (Pasaporte) ·
romance (Amores) · celebridad-feed-de-frases (Declaraciones sub=NO) · **mecánica abstracta (Racha/streak NO-OPEN)** · superlativo-sobre-plantas FATIGADO (Reseñas/Anuario 17/07).

**🔑 Meta-reglas:** (a) «app amada» solo convierte con HÉROE=USUARIO + LOGRO/ESTATUS persistente (Wrapped/Álbum ✓); consumo pasivo NO. (b) El GESTO
no basta: convierte el ÁNGULO (editorial/identidad/estatus) + asombro del PRESENTE. (c) Editorial convierte con VOZ 1ª pers/titulares punzantes, no 3ª pers pasivo.
(d) Feed de ítems cortos, no un caso-largo. (e) No repetir sub-género de identidad ya promovido. (f) **El GANCHO necesita drama/curiosidad CONCRETA del
PRESENTE de TUS plantas** — mecánicas abstractas (racha) y protagonistas del PASADO (biografías) NO abren aunque sean de familia ganadora.
(g) **El ÚNICO canal que sigue convirtiendo en la sequía = las TAREAS** (19/07 el usuario clickeó el reply-landing de la Gardenia).

## 📈 Estado del sistema + sequía

- Push subscription device `pix9`: **active** (verificado 21/07). Logging por `/api/feedback` confiable.
- **🔴 SEQUÍA SOSTENIDA 16-21/07 (7 días):** el usuario a veces vuelve/abre pero NO convierte (0 reacción/sub/aprobación/feedback_text). El cuello NO es
  el canal push (anda) ni el formato news-feed (probado): es el GANCHO de apertura. **20/07 = VENTANA EN BLANCO TOTAL (0 eventos, 5 pushes enviados 201):
  el usuario NO abrió NADA** — muy probablemente ausente, así que 20/07 no refuta ningún ángulo, solo no hay dato.
- **Compactación 21/07:** send_log −5 eventos >14d (movidos a daily_summary). engagement.json: sin compactar (evento más viejo 11/07, dentro de 14d).
- Upload pendiente: 1 foto B-15 (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **08-10/07 (última tanda GANADORA):** Entrevista(sub+206s), Quiz(😍+103s), Wrapped(😍+172s), Álbum(😍) → 4 PROMOVIDAS.
- **11-19/07:** racha larga de fallos — app-pasiva, gesto, editorial-pasivo, mística, nota-larga, celebridad-feed, superlativo-fatigado, **racha(streak) NO-OPEN**,
  **Nombre-y-Apellido(biografías=pasado) abre pero masomenos**. TODOS DROPPED. Único positivo sostenido: clicks al canal-tarea (task-dia/top3/reply-landing).
- **20/07 (ciclo 50):** Quiniela(a) + Diario-reno(b) + Guardia(c). **RESULTADO: ventana en blanco (0 eventos).** Guardia + Quiniela → DROPPED 21/07 SIN aprobación,
  pero con CONFOUND explícito (día en blanco = no dato, no refutación). El bridge-con-tareas (Guardia) y la suscripción-intrínseca (Quiniela) quedan SIN test limpio.
- **21/07 (ciclo 51) — DECISIÓN:** ante 7 días flojos + un día en blanco, reintento los dos mecanismos más prometedores que quedaron sin test limpio, en formatos NUEVOS:
  - ⏳ **La Cuenta Regresiva** (`2026-07-21-cuenta-regresiva.html`) — formato NUEVO. Ataca directo el gap de suscripción con **suscripción INTRÍNSECA**: la notif no
    interrumpe, ES el evento que el usuario pidió (el día que abra la 1ª flor). Anticipación + Zeigarnik. Cast FRESCO: F-2 Podranea(reclasif.1980), F-5 coronita, B-49
    misterio-glicinia + eventos de estación (primavera 23/09=64d, heladas). Push a (10:30). react `cuenta-regresiva`, sub `cuenta-regresiva-suscripcion-diaria`.
  - 📋 **La Asamblea del Jardín** (`2026-07-21-asamblea-jardin.html`) — formato NUEVO (asamblea de vecinos, ancla cultural rioplatense). **User-hero=PRESIDENTE**
    con poder de resolución + humor + editorial-con-voz. **Puentea con el canal que convierte:** puntos 1-2 = tareas REALES con link a landing (Gardenia B-25, Guayabo F-1);
    puntos 3-4 cast fresco (vivero B-46 adopción, caqui B-41 id-en-duda). Push c (18:00, mejor-abierto). react `asamblea-jardin`, sub `asamblea-jardin-suscripcion-diaria`.
  - **Slot b (13:00) → 🎁 Wrapped RENOVADO** (rested winner 12d, user-hero, familia NO-fatigada): edición «semana del 21/07», Top-5 reframeado a «las que empujan a la
    primavera» (64d al equinoccio), fecha visible actualizada. Renovación real en misma URL (regla re-push).
  - **Cola ciclo 51:** (a)10:30 Cuenta Regresiva; (b)13:00 Wrapped-reno; (c)18:00 Asamblea. + 10:00 task-dia (Hortensia B-5a, trasplante). top3 NO tocó (próx 22/07).
    3 ejes: anticipación-suscripción-intrínseca · user-hero-estatus · user-hero-presidente-con-bridge-a-tareas.
- **Watch 22/07:** si vuelve a haber apertura, ¿convierte (a) la suscripción INTRÍNSECA de la Cuenta Regresiva, o (b) la Asamblea que envuelve tareas en agencia+humor?
  Si sigue 0-conversión CON aperturas (no otro día en blanco) → bajar peso a experiencias nuevas y volcar el cupo al canal-tarea (task-dia/top3/replies), lo único que convierte.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia.** A 64 días de la primavera (equinoccio 23/09); heladas tardías posibles hasta ~fin agosto (pegan más al sur y este al amanecer).
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA en julio); palta B-22/B-36 y pindó B-8 con fruto;
  caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, pera B-39) acumulando frío → primeros en florecer en agosto; perennes verdes (guayabo F-1, mirto B-27, hiedra B-15).
- Tareas activas urgentes reales: Guayabo F-1 fumagina (alta); Gardenia B-25 pulgones+hormigas (alta); Liquidámbar B-37 limpieza copa (alta); Hortensia B-5a trasplante (task-dia hoy).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas (F-1,F-8,B-8,B-14,B-16,B-29,B-32,B-34,B-42,B-47) · 30 perennes · 15 caducos · 11 frutales ·
romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 (híbrido cidro×naranja) · palta Hass B-36 = clon de 1 árbol de 1926 (~80% mercado) ·
anacahuita B-16 = protegida por ley desde 1986 · hiedra B-15 = +400 años · cinta B-12 = purifica aire (NASA) · liquidámbar B-37 = storax/«ámbar líquido» ·
gardenia B-25 = 600kg flores → 1L aceite (Chanel Nº22) · F-2 Podranea = separada de Bignonia en 1980, flor nov-abr · F-5 coronita/Spiraea = flor oct-nov (id a confirmar) ·
B-41 caqui = identidad EN DUDA (nunca flor ni fruto); Diospyros=«fruto de los dioses» · B-46 vivero = ~30 plantines (palmera vale 200-500$) · B-49 = trifoliado, ¿glicinia? (revela en primavera).

## TODO pendiente

- **Formatos SIN usar:** before/after con fotos del usuario. **Evitar:** gesto-desechable, editorial-pasivo, app-pasiva, nota-única-larga, superlativo-sobre-plantas (fatigado), mecánica abstracta (racha), biografías/pasado, dobles del mismo eje en el día.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático). Reconciliar arrays `pruning` antes de cualquier vista de poda.
