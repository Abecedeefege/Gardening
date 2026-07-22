# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🏆 BREAKTHROUGH 21/07: PRIMER feedback_text — y POSITIVO (Asamblea)

El 21/07 22:23Z el usuario escribió su **primer feedback de texto del canal**, sobre la Asamblea:
**«Esta todo perfecto. Tené en cuenta que está lloviendo hace días en Montevideo, no he podido avanzar»**.
- Es señal **tier-1** (la de mayor peso). → **Asamblea PROMOVIDA 22/07** (Ideas → Experiencias, icono 📋).
- **FÓRMULA GANADORA CONFIRMADA:** user-hero=PRESIDENTE/autoridad **con agencia** + humor + **ancla cultural rioplatense** (asamblea de vecinos) + **PUENTE a tareas reales** (mociones = plagas Gardenia/Guayabo). Este es el molde a explotar.
- **DATO OPERATIVO CLAVE (ejecutado 22/07):** lleva **días de lluvia y NO pudo avanzar** en el jardín. → Las tareas NO se pueden ejecutar ahora. **NO exigir acción / no generar culpa: RELEVAR la culpa.** El contenido del 22/07 se ancló en la lluvia real (ver abajo).

## 🚨 FEEDBACK DIRECTO DEL USUARIO 18/07 (por chat — máxima autoridad, NO PISAR)

1. **«Me repetís los mismos funfacts»** → anti-repetición: `facts_ledger.json` (leer ANTES, actualizar DESPUÉS), planta featured descansa ≥7d, fact no <14d, ≥70% elenco fresco. **La sequía dejó casi todo el elenco quemado en 7d → estrategia validada: tocar plantas por ÁNGULO NUEVO (tarea real, reacción al clima), NUNCA repitiendo su fun_fact.** El «ángulo lluvia» del 22/07 es exactamente esto: dato real de cada planta, cero fun_fact repetido.
2. **feedback_text = LA señal de mayor peso.** Leer PRIMERO. Positivo=expandir, negativo=NUNCA vuelve, pedido=ejecutar. (Ya hay 1: positivo, Asamblea.)
3. **Objetivo:** interacción + marca de buena + buen feedback. Innovar SIEMPRE (formatos nuevos > refritos).
4. **Re-push de promovida = contenido RENOVADO en misma URL** (nunca re-mandar estático).

## ⏱️ CADENCIA VIGENTE: 3 pushes propios/día (fijada 18/06)

Slots base **10:30 / 13:00 / 18:00 -03:00**. **🚫 PISO 10:00: NINGUNA push antes de 10:00.**
task-dia (10:00) + top3 (11:00, cada 2d) son ADICIONALES al cupo. Primer send_at propio ≥60 min post-corrida. expires_at = mismo día 22:00. Cada notif a destino DISTINTO. Timestamps con `-03:00`.
**Regla dura: la cola SIEMPRE 3 propias pending.** El 3º slot lo cubro con rotación de una promovida ganadora descansada (bajo costo) renovada con contenido fresco.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`2026-07-04-expedientes-jardin.html`) — COMISIONADA, pre-aprobada, EXENTA de no-supervivencia. qids `exp-*`. B-41 caqui: identidad EN DUDA (nunca flor ni fruto).
2. **🎯 Top 3** (`top3-tareas.html`) — recurrente cada 2d (ancla 04/07): `gen_top3_tareas.py <fecha> --merge` (self-gated). **Corrió 22/07** (próx 24/07). NO borrar página ni proposal.
3. Timeline: hechas/cerradas colapsadas en "🗂️ Pasadas / hechas".
4. **Splash** «Hora dorada» integrado en Home. Demos `splash-*.html` = referencia, NO tocar.
5. ⚠️ **Pillow (PIL) no viene instalado:** `pip install Pillow` ANTES de gen_*.py / build.py.

## 🆕 FUNCIÓN PARALELA (28/06): 2 experiencias NUEVAS de cero por corrida

Persona product/UX/growth/sales. Cada una: (1) `engageReact` target=slug, (2) CTA sub diaria `engageAnswer` qid `<slug>-suscripcion-diaria`, (3) caja feedback propia `engageFeedback('<slug>')` id `engage-feedback-box`, (4) HTML de pitch aparte con 6 modelos (3 innovadores + 3 ultra-creativos). Contrato: link "← Volver al sitio estable" PRIMERO, `engage.js` al pie, SOLO datos verificados.

## 🚀 QUÉ CONVIERTE — el ÁNGULO decide dentro del news-feed

**CONVIERTEN (love/sub/feedback+, dwell alto) — PROMOVIDAS:** 📋 **Asamblea (user-hero=PRESIDENTE + agencia + humor + bridge a tareas) = feedback_text POSITIVO, la señal top** · 🍵 Chusmerío 260s😍 · 📱 Feed(social 1ª pers) 208s😍 · 🎙️ Entrevista(celebridad) sub+206s · 🎁 Wrapped(«tus números») 😍+172s (⚠️ empezó a fatigar: 21/07 re-push = meh) · 🏆 Récords 😍+sub+141s · 📗 Álbum · 🔮 Horóscopo(identidad) 😍+sub · 🌱 Quiz «¿qué planta sos?» 😍+103s · 📰 Diario · 😂Memes/🧪Superpoderes/💌Consultorio/🎤Confesiones/📺Reality (aprueban tibio).

**RECHAZAN/NO ABREN (dropped):** app pasiva (JardínFlix/Historias/Podcast/BeReal) · gesto solo (Raspadita) · editorial pasivo 3ª pers (Documental) · mística repetida (Tarot) · nota-larga (Exclusiva) · ranking-presente (Trending) · miedo (Lista Negra) · chat coral · dinero (Tasación) · pasado/biografías (Efemérides/Nombre-y-Apellido) · ceremonia/torneo (Gala/Mundial) · viajes (Pasaporte) · romance (Amores) · celebridad-frases (Declaraciones) · **mecánica abstracta (Racha/streak)** · superlativo-fatigado (Reseñas/Anuario) · **⏳ countdown/anticipación (Cuenta Regresiva 21/07 NO abrió, Quiniela 20/07 en blanco) = línea CERRADA: la espera pasiva de un evento futuro NO abre; el usuario responde a AGENCIA+PRESENTE.**

**🔑 Meta-reglas:** (a) «app amada» solo convierte con HÉROE=USUARIO + AGENCIA/LOGRO/ESTATUS (Asamblea/Wrapped/Álbum ✓); consumo pasivo NO. (b) convierte el ÁNGULO (agencia/editorial/identidad/estatus) + asombro/drama del PRESENTE. (c) editorial con VOZ 1ª pers/titulares punzantes. (d) feed de ítems cortos, no caso-largo. (e) no repetir sub-género de identidad ya promovido. (f) el GANCHO necesita drama/curiosidad CONCRETA del PRESENTE; countdown y pasado NO abren. (g) **las TAREAS siguen siendo el canal más fiable** — y la Asamblea GANÓ envolviéndolas en agencia+humor. (h) **el CLIMA REAL es un ancla poderosa y creíble** — el usuario mismo lo trajo (lluvia); anclar contenido ahí es específico y empático.

## 📈 Estado del sistema + sequía + lluvia

- Push subscription device `pix9`: **active** (verificado 22/07). Logging por `/api/feedback` confiable.
- **Sequía 16-21/07 quebrada el 21/07:** el usuario abrió Y dejó feedback positivo (Asamblea) → el cuello era el GANCHO, no el canal. La fórmula agencia+humor+bridge-tareas rompió el hielo.
- **Contexto lluvia (21/07→):** días de lluvia en MVD, usuario no puede avanzar. Doble efecto: (1) tareas no ejecutables → aliviar culpa, no nagear; (2) la lluvia es contenido real (riego, plagas volteadas, drenaje, dormancia).
- **Compactación 22/07:** engagement.json −eventos 06-07/07 (>14d) → daily_summary (85 eventos vivos). send_log sin tocar (oldest 08/07 = 14d, dentro de ventana).

## Conclusiones de los pushN enviados (por feedback real)

- **08-10/07 (tanda ganadora):** Entrevista(sub+206s), Quiz(😍+103s), Wrapped(😍+172s), Álbum(😍) → 4 PROMOVIDAS.
- **11-20/07:** racha de fallos (app-pasiva, gesto, mística, nota-larga, celebridad, superlativo-fatigado, racha, biografías). Único positivo sostenido: canal-tarea (task-dia/top3/reply-landing). 20/07 = ventana en blanco (no dato).
- **21/07 (ciclo 51):** a=Cuenta Regresiva (NO abrió) · b=Wrapped-reno (**meh** — el winner empieza a fatigar, descansarlo) · c=**Asamblea (feedback_text POSITIVO)** 🏆. Lectura: agencia+humor+bridge GANA; countdown pierde; Wrapped saturado.
- **22/07 (ciclo 52) — DECISIÓN:** promuevo Asamblea; explota la fórmula + responde al dato «no pude avanzar por la lluvia» con 2 experiencias NUEVAS ancladas en la lluvia real:
  - 💧 **La lluvia te está haciendo las tareas** (`2026-07-22-lluvia-tareas.html`) — formato NUEVO (checklist auto-completado por el clima). Eje ALIVIO+agencia+humor: da vuelta la culpa mostrando con datos reales que el jardín avanzó sin él (5/7 tareas «tachadas» por la lluvia + 2 honestas pendientes). Respuesta directa al feedback. Push a (10:30, mañana lluviosa). react `lluvia-tareas`, sub `lluvia-tareas-suscripcion-diaria`.
  - 🌿 **El grupo de WhatsApp del Jardín** (`2026-07-22-grupo-jardin.html`) — formato NUEVO (chat grupal vs feed). Lleva el eje 1ª-persona-social (Feed 208s récord) al hábitat más pegajoso rioplatense; 12 plantas chatean la lluvia con conflicto+humor, cada mensaje un dato real por ángulo-clima. Push c (18:00, slot dorado donde ganó la Asamblea). react `grupo-jardin`, sub `grupo-jardin-suscripcion-diaria`.
  - Slot b (13:00) → 🔮 **Horóscopo RENOVADO** (rested winner, identidad, promovido 02/07): «edición de lluvia», kicker/fecha a 22/07 + framing lluvioso. Renovación real en misma URL.
  - **Cola ciclo 52:** (a)10:30 lluvia-tareas; (b)13:00 Horóscopo-lluvia; (c)18:00 grupo-jardin. + 10:00 task-dia (Gardenia B-25) + 11:00 top3 (corrió). 3 ejes: alivio-anti-culpa · identidad-renovada · social-1ª-persona-humor.
- **Watch 23/07:** ¿la fórmula lluvia (alivio + social/grupo, ambas ancladas al clima real que el usuario trajo) repite el feedback positivo de la Asamblea? Si el grupo-WhatsApp convierte → el chat-grupal es un nuevo molde ganador a serializar. Si el usuario deja otro feedback_text, es oro: citarlo y ejecutarlo.

## Contexto del jardín (julio 2026 = pleno invierno + LLUVIA, lat -34.9°S)

- Jardín en DORMANCIA + días de lluvia. **NO inventar urgencia; usuario no puede salir.** 62 días a la primavera (equinoccio 23/09); heladas tardías posibles hasta ~fin agosto (pegan al sur y este al amanecer).
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA en julio) — mediterráneo, odia pies mojados; palta B-22/B-36 y pindó B-8 con fruto; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, pera B-39) acumulando frío+agua → primeros en florecer en agosto; perennes verdes (guayabo F-1, mirto B-27, hiedra B-15). Hortensia B-5a = la más sedienta.
- Efecto lluvia (verificado/horticultura estándar): riego profundo; agua voltea pulgones y desarma hormigas (Gardenia B-25); enjuaga fumagina de hojas (Guayabo F-1); recarga humedad de suelo; PERO mediterráneas (romero/lavanda B-10) resienten encharcamiento y la humedad pegada al cuello del tronco favorece hongos de base (Phytophthora).
- Tareas activas reales: Gardenia B-25 pulgones+hormigas (alta, task-dia hoy); Guayabo F-1 fumagina (alta); Liquidámbar B-37 limpieza copa (alta).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas (F-1,F-8,B-8,B-14,B-16,B-29,B-32,B-34,B-42,B-47) · 30 perennes · 15 caducos · 11 frutales ·
romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 · palta Hass B-36 = clon de 1926 (~80% mercado) · anacahuita B-16 = protegida por ley 1986 · hiedra B-15 = +400 años · cinta B-12 = NASA aire · liquidámbar B-37 = storax/«ámbar líquido» · gardenia B-25 = 600kg flores→1L Chanel Nº22 · pindó B-8 = fruto coco-banana mar-jul · B-41 caqui = identidad EN DUDA · B-46 vivero = ~30 plantines · B-49 = trifoliado ¿glicinia? (revela en primavera).

## TODO pendiente

- **Formatos SIN usar:** before/after con fotos del usuario. **Evitar:** countdown/anticipación (cerrado), gesto-desechable, editorial-pasivo, app-pasiva, nota-larga, superlativo-fatigado, racha, biografías/pasado, Wrapped (descansar, fatigó), dobles del mismo eje en el día.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time. Reconciliar arrays `pruning` antes de cualquier vista de poda.
- Si el grupo-WhatsApp o la lluvia-tareas convierten, considerar serializarlos (grupo diario / parte de lluvia recurrente).
