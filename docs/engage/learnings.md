# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🚨🚨 PIVOTE 24/07 — feedback_text tier-1 MATA el role-play verboso (LO MÁS IMPORTANTE)

- **23/07 21:37Z — feedback_text del usuario sobre mercado-pases: «Mucho texto, muy cargado, no es realmente lo que busco en una app de jardín».** Señal tier-1, la de mayor peso. Leyó TODO (150s/97%) y aun así lo RECHAZÓ + reaction 'no' + suscripción 'no'.
- **AMBAS agencias-teatrales del 23/07 fueron RECHAZADAS:** ronda-medica (jefe de guardia) proposal_rejected 78s; mercado-pases (DT) proposal_rejected + feedback negativo. → las 2 DROPEADAS + borradas 24/07.
- **HIPÓTESIS 'AGENCIA convierte donde la pasividad falló' → REFUTADA.** El usuario TUVO agencia/autoridad (decidía altas, armaba el once) y rechazó igual. El problema del 22/07 NO era pasividad: era (y es) la **FORMA — role-play denso, teatral, verboso.** El eje agencia-autoridad-teatral (médico/DT/presidente/juez) está **AGOTADO**.
- **MANDATO DEL USUARIO (deducido del texto):** quiere una **app de jardín de verdad**, calma, con **poco texto**, glanceable. No walls de prosa, no metáforas rebuscadas (fútbol doblemente muerto: Mundial + mercado-pases).
- **PIVOTE 24/07 (ciclo 54):** 2 experiencias RADICALMENTE minimalistas, paleta CLARA, casi sin prosa, ancladas en estado/logros REALES (no trivia — el elenco de fun_facts está QUEMADO, ver facts_ledger):
  - 🌤️ **jardin-hoy** (a, 10:30): vistazo de 5s — estado calmo («hoy nada urgente») + 3 chips (en flor/con fruta/durmiendo). Cero párrafos.
  - ✅ **tu-semana** (b, 18:00): recap de logros — número grande (6) + 6 tildes de 1 línea de las tareas que el usuario CERRÓ el 23/07. HÉROE=USUARIO en modo orgullo, sin peso teatral.
- **WATCH 25/07:** ¿el minimalismo convierte donde el role-play verboso murió? Si jardin-hoy o tu-semana enganchan → el pivote es el camino y hay que despedirse del formato news-feed-cargado. Si el usuario deja feedback_text: ORO, citarlo y ejecutar. Si tampoco convierten → revisar si el problema es fatiga global de push (bajar frecuencia).

## Contexto previo (21-22/07, ahora RE-LEÍDO a la luz del pivote)

- **21/07 — feedback_text POSITIVO** sobre la Asamblea: «Está todo perfecto. Está lloviendo hace días, no he podido avanzar». → Asamblea promovida. PERO ojo: ese «está todo perfecto» era sobre el SITIO en general, y venía con la Asamblea que ERA densa. El 23/07 corrigió: el texto cargado cansa. La Asamblea quizás ganó por HUMOR+bridge, no por su densidad.
- **22/07 — lluvia-tareas y grupo-jardin: 0 clicks.** En su momento lo leí como 'pasividad'. A la luz del 24/07, sumo lectura: ambas TAMBIÉN eran cargadas. Pasividad + densidad, dos pecados.

## 🚨 FEEDBACK DIRECTO DEL USUARIO 18/07 (por chat — máxima autoridad, NO PISAR)

1. **«Me repetís los mismos funfacts»** → anti-repetición: `facts_ledger.json` (leer ANTES, actualizar DESPUÉS), planta featured descansa ≥7d, fact no <14d. **Con el elenco quemado: tocar plantas por ÁNGULO NUEVO (tarea/clima/rol), NUNCA repitiendo su fun_fact.**
2. **feedback_text = LA señal de mayor peso.** Leer PRIMERO. Positivo=expandir, negativo=NUNCA vuelve, pedido=ejecutar.
3. **Objetivo:** interacción + marca de buena + buen feedback. Innovar SIEMPRE (formatos nuevos > refritos).
4. **Re-push de promovida = contenido RENOVADO en misma URL** (nunca re-mandar estático).

## ⏱️ CADENCIA VIGENTE: 2 pushes propios/día (bajada de 3→2 el 23/07 por PEDIDO DIRECTO del usuario)

**El usuario pidió por chat el 23/07: «bajemos a un máximo de 2 push por día».** → Cadencia propia = **2/día**, NO 3.
Slots base **10:30 / 18:00 -03:00** (se elimina el 13:00). **🚫 PISO 10:00: NINGUNA push antes de 10:00.**
task-dia (10:00) + top3 (11:00, cada 2d) son ADICIONALES al cupo (canal de tareas comisionado, separado). Primer send_at propio ≥60 min post-corrida. expires_at = mismo día 22:00. Cada notif a destino DISTINTO. Timestamps con `-03:00`.
**Regla dura: la cola SIEMPRE 2 propias pending = las 2 experiencias nuevas de la función paralela** (una a 10:30, otra a 18:00). **YA NO hay 3er slot de winner descansado** — con 2/día, ambos slots son para las 2 experiencias nuevas de cero. (Renovar un winner descansado queda como opción solo si algún día NO se crean 2 experiencias nuevas.)

## 🆕 FUNCIÓN PARALELA (28/06): 2 experiencias NUEVAS de cero por corrida

Persona product/UX/growth/sales. Cada una: (1) `engageReact` target=slug, (2) CTA sub diaria `engageAnswer` qid `<slug>-suscripcion-diaria`, (3) caja feedback propia `engageFeedback('<slug>')` id `engage-feedback-box`, (4) botones `engageApprove/engageRejected('<id>')` (proposal pending), (5) HTML de pitch aparte con 6 modelos (3 innovadores + 3 ultra-creativos). Contrato: link "← Volver al sitio estable" PRIMERO, `engage.js` al pie, SOLO datos verificados. Con la cadencia 2/día (23/07), **las 2 experiencias nuevas ocupan los 2 slots propios** (10:30 y 18:00); ya no hay 3er slot de winner descansado.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`2026-07-04-expedientes-jardin.html`) — COMISIONADA, EXENTA de no-supervivencia. B-41 caqui: identidad EN DUDA.
2. **🎯 Top 3** (`top3-tareas.html`) — cada 2d (ancla 04/07): `gen_top3_tareas.py <fecha> --merge` (self-gated). **Corrió 22/07; próx 24/07.** NO borrar página ni proposal.
3. Timeline: hechas/cerradas colapsadas en "🗂️ Pasadas / hechas".
4. **Splash** «Hora dorada» integrado en Home. Demos `splash-*.html` = referencia, NO tocar.
5. ⚠️ **Pillow (PIL) no viene instalado:** `pip install Pillow` ANTES de gen_*.py / build.py.

## 📌 PEDIDO DIRECTO DEL USUARIO 23/07 — landing diaria de pendientes (NO PISAR)

**`docs/engage/tareas-pendientes.html`** = landing FIJA (URL estable, permanente, NO experimento — no borrar/renombrar) que el usuario recibe TODOS LOS DÍAS por push. Ver PASO OBLIGATORIO en `.claude/commands/engagement.md`. Cada corrida: (a) actualizarla a mano desde `task_states.json`+`data_plants.py` — solo lo pendiente, 3 bloques (🔧 Para hacer ahora / 📅 Top 3 próximas / 🗓️ Primavera) + módulo feedback general al pie (`engageFeedback('landing-pendientes')`); (b) encolar su push `<fecha>-pendientes` (`format:"tarea"`, ~10:00, adicional al cupo). La vieja `2026-07-23-resultado-del-dia.html` quedó como redirect a la fija.

## 🚀 QUÉ CONVIERTE — el ÁNGULO decide dentro del news-feed

**CONVIERTEN (PROMOVIDAS):** 📋 **Asamblea (usuario=PRESIDENTE+agencia+humor+bridge-tareas) = feedback_text POSITIVO, la señal top** · 🍵 Chusmerío 260s😍 · 📱 Feed(social 1ª pers, habla AL usuario) 208s😍 · 🎙️ Entrevista(celebridad) sub+206s · 🎁 Wrapped 😍+172s (⚠️ FATIGADO: descansar) · 🏆 Récords 😍+sub+141s · 📗 Álbum · 🔮 Horóscopo(identidad) 😍+sub · 🌱 Quiz «¿qué planta sos?» 😍+103s · 📰 Diario · 😂Memes/🧪Superpoderes/💌Consultorio/🎤Confesiones/📺Reality (tibio).

**RECHAZAN/NO ABREN (dropped):** app pasiva · gesto solo · editorial pasivo 3ª pers · mística repetida · nota-larga · ranking-presente · miedo · **chat coral (grupo-jardin 22/07: 0 clicks)** · dinero/tasación · pasado/biografías · ceremonia/torneo (Gala/Mundial) · viajes · romance · celebridad-frases · mecánica abstracta (racha/streak) · superlativo-fatigado · **⏳ countdown/anticipación (CERRADO)** · **💧 alivio-PASIVO** · **🎭 ROLE-PLAY VERBOSO / agencia-teatral (ronda-medica + mercado-pases 23/07: RECHAZADOS pese a agencia — feedback tier-1 «mucho texto, muy cargado». CERRADO: médico/DT/presidente/juez/farándula con prosa densa NO va).**

**🔑 Meta-reglas:** (a) **«app amada» solo convierte con HÉROE=USUARIO + AGENCIA/AUTORIDAD/LOGRO** — consumo/observación PASIVA NO (confirmado x2: 22/07 lluvia-tareas y grupo-jardin murieron por pasivos). (b) convierte el ÁNGULO (agencia/autoridad/identidad/estatus) + drama del PRESENTE. (c) editorial con VOZ 1ª pers que le habla AL usuario, no que lo deja mirando. (d) feed de ítems cortos, no caso-largo. (e) no repetir sub-género de identidad ya promovido. (f) el GANCHO necesita drama/curiosidad CONCRETA del PRESENTE. (g) **las TAREAS son el canal más fiable** (task-dia convierte casi siempre). (h) el CLIMA REAL es buen ancla, PERO solo si el usuario es protagonista-que-decide, no espectador.

## 📈 Estado del sistema + lluvia

- Push subscription device `pix9`: **active** (22/07). Logging por `/api/feedback` confiable.
- **Contexto lluvia (21/07→):** días de lluvia en MVD, usuario no puede avanzar. Tareas no ejecutables → NO nagear/culpar. La lluvia es contenido real (drenaje, plagas volteadas, dormancia) PERO enmarcado con el usuario decidiendo, no mirando.
- **Compactación 24/07:** engagement.json −eventos <10/07 → daily_summary (89 vivos); send_log −4 del 09/07 (66 vivos); queue −entries 23/07.

## Conclusiones de los pushN enviados (por feedback real)

- **23/07 (ciclo 53) — DOBLE RECHAZO + feedback tier-1 (dato decisivo):** a=ronda-medica (jefe de guardia) → proposal_rejected, 78s, sin reacción/sub · b=mercado-pases (DT) → proposal_rejected + reaction 'no' + sub 'no' + **feedback_text «Mucho texto, muy cargado, no es lo que busco en una app de jardín»** (150s/97%). task-dia (fumagina) y el reply de gardenia SÍ clicaron (canal-tarea sigue firme). **Conclusión: el role-play verboso está muerto — la densidad cansa aunque el usuario lea todo. La agencia NO alcanza si viene envuelta en texto.** Las 2 dropeadas + borradas.
- **24/07 (ciclo 54) — PIVOTE a minimalismo:** dejo el news-feed-cargado y pruebo 2 experiencias liviano-glanceable de estado/logro real. Ver bloque PIVOTE arriba.

- **08-10/07 (tanda ganadora):** Entrevista(sub+206s), Quiz(😍+103s), Wrapped(😍+172s), Álbum(😍) → 4 PROMOVIDAS.
- **11-20/07:** racha de fallos (app-pasiva, gesto, mística, nota-larga, celebridad, superlativo, racha, biografías). Único positivo sostenido: canal-tarea.
- **21/07 (ciclo 51):** a=Cuenta Regresiva (NO abrió) · b=Wrapped-reno (meh, fatiga) · c=**Asamblea (feedback_text POSITIVO)** 🏆. Lectura: agencia+humor+bridge GANA; countdown y Wrapped pierden.
- **22/07 (ciclo 52) — DATO CLAVE:** a=lluvia-tareas (0) · b=Horóscopo-lluvia (0) · c=grupo-jardin (0, slot dorado 18:00) · **solo task-dia clicó.** Confirma: **el ancla-lluvia sin agencia del usuario NO abre.** Las 2 experiencias pasivas murieron → dropeadas.
- **24/07 (ciclo 54) — Cola (2/día):** (a)10:30 🌤️ jardin-hoy (vistazo minimalista); (b)18:00 ✅ tu-semana (recap de logros). + canal-tarea: 10:00 task-dia (Guayabo F-1 limpieza), 10:00 pendientes (landing fija), 11:00 top3 (Gardenia/Liquidámbar/Hortensia). react `jardin-hoy`/`tu-semana`, sub `<slug>-suscripcion-diaria`.

## Contexto del jardín (julio 2026 = pleno invierno + LLUVIA, lat -34.9°S)

- Jardín en DORMANCIA + lluvia. **NO inventar urgencia; usuario no puede salir.** ~62 días a primavera (equinoccio 23/09); heladas tardías posibles hasta ~fin agosto (pegan al sur y este al amanecer).
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA en julio) — mediterráneo, odia pies mojados; palta B-22/B-36 y pindó B-8 con fruto; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, pera B-39) acumulando frío+agua → primeros en florecer en agosto; perennes verdes (guayabo F-1, mirto B-27, hiedra B-15). Hortensia B-5a = la más sedienta (= gran ganadora de la lluvia).
- Efecto lluvia (horticultura estándar): riego profundo; agua voltea pulgones y desarma hormigas (Gardenia B-25); enjuaga fumagina (Guayabo F-1); PERO mediterráneas (romero/lavanda B-10) resienten encharcamiento → hongos de base (Phytophthora).
- Tareas activas reales: Gardenia B-25 pulgones+hormigas (alta); Guayabo F-1 fumagina (alta, task-dia hoy); Liquidámbar B-37 limpieza copa (alta).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 · palta Hass B-36 = clon de 1926 (~80% mercado) · anacahuita B-16 = protegida por ley 1986 · hiedra B-15 = +400 años · liquidámbar B-37 = storax/«ámbar líquido» · gardenia B-25 = 600kg flores→1L Chanel Nº22 · pindó B-8 = fruto coco-banana mar-jul · B-41 caqui = identidad EN DUDA · B-46 vivero = ~30 plantines · B-49 = trifoliado ¿glicinia? (revela en primavera).

## TODO pendiente

- **DIRECCIÓN 24/07+:** MINIMALISMO. Poco texto, paleta clara, glanceable, garden-close, dato REAL (estado/logro/tarea, NO trivia — elenco quemado). **Evitar:** role-play verboso/teatral (CERRADO 23/07), countdown, gesto, editorial-pasivo, app-pasiva, nota-larga, superlativo-fatigado, racha, biografías, Wrapped (fatigó), chat-coral, alivio-pasivo.
- Si jardin-hoy o tu-semana convierten → serializar (vistazo diario / resumen semanal fijo) y empezar a mover el core hacia lo liviano. Si NO → el problema es fatiga global de push; bajar frecuencia y consultar al usuario dentro de la app.
- Formatos livianos aún sin probar: before/after con fotos reales del usuario; una sola foto grande + 3 palabras; mini-mapa del jardín tocable.
- Regenerar dataset M de la rueda desde data_plants.py en build-time. Reconciliar arrays `pruning` antes de cualquier vista de poda.
