# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## 🏆 BREAKTHROUGH 21/07 + LECTURA 22/07: qué convierte y qué NO (crítico)

- **21/07 22:23Z — PRIMER feedback_text del canal, POSITIVO** sobre la Asamblea:
  «Esta todo perfecto. Tené en cuenta que está lloviendo hace días en Montevideo, no he podido avanzar». Señal tier-1. → **Asamblea PROMOVIDA 22/07** (Ideas → Experiencias, 📋).
- **FÓRMULA GANADORA:** HÉROE=USUARIO con AUTORIDAD/AGENCIA (presidente/juez/DT/médico) + humor + ancla cultural rioplatense + **PUENTE a tareas reales**. Este es el molde a explotar.
- **🚨 LECTURA 22/07 (ciclo 52) — la fórmula LLUVIA-PASIVA FALLÓ.** Encolé 2 experiencias ancladas en la lluvia real (lluvia-tareas = checklist auto-tachado por el clima; grupo-jardin = chat de 12 plantas). **Resultado: 0 clicks / 0 reacción en a/b/c. Solo task-dia convirtió** (clic 14:17Z). Diagnóstico: **ambas eran PASIVAS** — lluvia-tareas mostraba que el jardín avanzó *sin* el usuario (le quita agencia); grupo-jardin lo deja *mirando* una charla ajena. **El ancla-lluvia es real y buena, pero el usuario-espectador NO abre.** Confirmado meta-regla (a): sin HÉROE=USUARIO+AGENCIA no hay conversión, por más real que sea el ancla. Las 2 → **DROPEADAS 23/07**.

## 🚨 FEEDBACK DIRECTO DEL USUARIO 18/07 (por chat — máxima autoridad, NO PISAR)

1. **«Me repetís los mismos funfacts»** → anti-repetición: `facts_ledger.json` (leer ANTES, actualizar DESPUÉS), planta featured descansa ≥7d, fact no <14d. **Con el elenco quemado: tocar plantas por ÁNGULO NUEVO (tarea/clima/rol), NUNCA repitiendo su fun_fact.**
2. **feedback_text = LA señal de mayor peso.** Leer PRIMERO. Positivo=expandir, negativo=NUNCA vuelve, pedido=ejecutar.
3. **Objetivo:** interacción + marca de buena + buen feedback. Innovar SIEMPRE (formatos nuevos > refritos).
4. **Re-push de promovida = contenido RENOVADO en misma URL** (nunca re-mandar estático).

## ⏱️ CADENCIA VIGENTE: 3 pushes propios/día (fijada 18/06)

Slots base **10:30 / 13:00 / 18:00 -03:00**. **🚫 PISO 10:00: NINGUNA push antes de 10:00.**
task-dia (10:00) + top3 (11:00, cada 2d) son ADICIONALES al cupo. Primer send_at propio ≥60 min post-corrida. expires_at = mismo día 22:00. Cada notif a destino DISTINTO. Timestamps con `-03:00`.
**Regla dura: la cola SIEMPRE 3 propias pending.** El 3º slot = rotación de una promovida ganadora descansada, RENOVADA con contenido fresco en misma URL.

## 🆕 FUNCIÓN PARALELA (28/06): 2 experiencias NUEVAS de cero por corrida

Persona product/UX/growth/sales. Cada una: (1) `engageReact` target=slug, (2) CTA sub diaria `engageAnswer` qid `<slug>-suscripcion-diaria`, (3) caja feedback propia `engageFeedback('<slug>')` id `engage-feedback-box`, (4) botones `engageApprove/engageRejected('<id>')` (proposal pending), (5) HTML de pitch aparte con 6 modelos (3 innovadores + 3 ultra-creativos). Contrato: link "← Volver al sitio estable" PRIMERO, `engage.js` al pie, SOLO datos verificados. Ambas van a 2 de los 3 pushes; el 3º = winner descansado renovado.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`2026-07-04-expedientes-jardin.html`) — COMISIONADA, EXENTA de no-supervivencia. B-41 caqui: identidad EN DUDA.
2. **🎯 Top 3** (`top3-tareas.html`) — cada 2d (ancla 04/07): `gen_top3_tareas.py <fecha> --merge` (self-gated). **Corrió 22/07; próx 24/07.** NO borrar página ni proposal.
3. Timeline: hechas/cerradas colapsadas en "🗂️ Pasadas / hechas".
4. **Splash** «Hora dorada» integrado en Home. Demos `splash-*.html` = referencia, NO tocar.
5. ⚠️ **Pillow (PIL) no viene instalado:** `pip install Pillow` ANTES de gen_*.py / build.py.

## 🚀 QUÉ CONVIERTE — el ÁNGULO decide dentro del news-feed

**CONVIERTEN (PROMOVIDAS):** 📋 **Asamblea (usuario=PRESIDENTE+agencia+humor+bridge-tareas) = feedback_text POSITIVO, la señal top** · 🍵 Chusmerío 260s😍 · 📱 Feed(social 1ª pers, habla AL usuario) 208s😍 · 🎙️ Entrevista(celebridad) sub+206s · 🎁 Wrapped 😍+172s (⚠️ FATIGADO: descansar) · 🏆 Récords 😍+sub+141s · 📗 Álbum · 🔮 Horóscopo(identidad) 😍+sub · 🌱 Quiz «¿qué planta sos?» 😍+103s · 📰 Diario · 😂Memes/🧪Superpoderes/💌Consultorio/🎤Confesiones/📺Reality (tibio).

**RECHAZAN/NO ABREN (dropped):** app pasiva · gesto solo · editorial pasivo 3ª pers · mística repetida · nota-larga · ranking-presente · miedo · **chat coral (grupo-jardin 22/07: 0 clicks)** · dinero/tasación · pasado/biografías · ceremonia/torneo (Gala/Mundial) · viajes · romance · celebridad-frases · mecánica abstracta (racha/streak) · superlativo-fatigado · **⏳ countdown/anticipación (CERRADO)** · **💧 alivio-PASIVO (lluvia-tareas 22/07: checklist auto-tachado = le quita agencia al usuario, 0 clicks).**

**🔑 Meta-reglas:** (a) **«app amada» solo convierte con HÉROE=USUARIO + AGENCIA/AUTORIDAD/LOGRO** — consumo/observación PASIVA NO (confirmado x2: 22/07 lluvia-tareas y grupo-jardin murieron por pasivos). (b) convierte el ÁNGULO (agencia/autoridad/identidad/estatus) + drama del PRESENTE. (c) editorial con VOZ 1ª pers que le habla AL usuario, no que lo deja mirando. (d) feed de ítems cortos, no caso-largo. (e) no repetir sub-género de identidad ya promovido. (f) el GANCHO necesita drama/curiosidad CONCRETA del PRESENTE. (g) **las TAREAS son el canal más fiable** (task-dia convierte casi siempre). (h) el CLIMA REAL es buen ancla, PERO solo si el usuario es protagonista-que-decide, no espectador.

## 📈 Estado del sistema + lluvia

- Push subscription device `pix9`: **active** (22/07). Logging por `/api/feedback` confiable.
- **Contexto lluvia (21/07→):** días de lluvia en MVD, usuario no puede avanzar. Tareas no ejecutables → NO nagear/culpar. La lluvia es contenido real (drenaje, plagas volteadas, dormancia) PERO enmarcado con el usuario decidiendo, no mirando.
- **Compactación 23/07:** engagement.json −12 eventos <09/07 → daily_summary (75 vivos); send_log −5 <09/07 (66 vivos); queue −entries 22/07.

## Conclusiones de los pushN enviados (por feedback real)

- **08-10/07 (tanda ganadora):** Entrevista(sub+206s), Quiz(😍+103s), Wrapped(😍+172s), Álbum(😍) → 4 PROMOVIDAS.
- **11-20/07:** racha de fallos (app-pasiva, gesto, mística, nota-larga, celebridad, superlativo, racha, biografías). Único positivo sostenido: canal-tarea.
- **21/07 (ciclo 51):** a=Cuenta Regresiva (NO abrió) · b=Wrapped-reno (meh, fatiga) · c=**Asamblea (feedback_text POSITIVO)** 🏆. Lectura: agencia+humor+bridge GANA; countdown y Wrapped pierden.
- **22/07 (ciclo 52) — DATO CLAVE:** a=lluvia-tareas (0) · b=Horóscopo-lluvia (0) · c=grupo-jardin (0, slot dorado 18:00) · **solo task-dia clicó.** Confirma: **el ancla-lluvia sin agencia del usuario NO abre.** Las 2 experiencias pasivas murieron → dropeadas.
- **23/07 (ciclo 53) — DECISIÓN:** vuelvo 100% a la fórmula ganadora (HÉROE=USUARIO+AUTORIDAD+bridge-tareas) con 2 formatos NUEVOS de AGENCIA, dejando la lluvia como ancla real pero con el usuario decidiendo:
  - 🩺 **Ronda médica del jardín** (`2026-07-23-ronda-medica.html`) — usuario=JEFE DE GUARDIA, cada planta paciente con signos vitales + decisión (alta/tratamiento/observación). Ataca el dolor #1 del jardinero («¿enfermo o normal?») = miedo→control. Cast: Romero B-26 (pie mojado post-lluvia), Gardenia B-25 (tarea real), Hortensia B-5a (alta feliz), Lavanda B-10, Durazno B-30/35 (dormancia). Push a (10:30). react `ronda-medica`, sub `ronda-medica-suscripcion-diaria`.
  - 🔧 **Mercado de pases** (`2026-07-23-mercado-pases.html`) — usuario=DT, el invierno = pretemporada (ataca el valle de retención invernal). Decisiones: subir cantera B-46 (30 plantines), renovar Limonero B-23 (12/12), pretemporada Crespón B-9, intransferible Palto B-36 (clon 1926), Gardenia B-25 tocada (tarea real). Push c (18:00, slot dorado). react `mercado-pases`, sub `mercado-pases-suscripcion-diaria`.
  - Slot b (13:00) → 🍵 **Chusmerío RENOVADO** (winner 260s😍, descansado): «edición de lluvia», kicker a 23/07 + chisme nuevo prepend (Romero B-26 = única que florece bajo la lluvia + riesgo Phytophthora). Renovación real en misma URL.
  - **Cola ciclo 53:** (a)10:30 ronda-medica; (b)13:00 chusmerio-lluvia; (c)18:00 mercado-pases. + 10:00 task-dia (Guayabo F-1 fumagina). top3 no toca (próx 24/07).
- **Watch 24/07:** ¿la vuelta a AGENCIA (médico/DT) repite el clic de la Asamblea que la lluvia-pasiva no dio? Si ronda-medica o mercado-pases convierten → confirmado que el problema del 22/07 fue PASIVIDAD, no fatiga del canal. Si el usuario deja feedback_text: oro, citarlo y ejecutar.

## Contexto del jardín (julio 2026 = pleno invierno + LLUVIA, lat -34.9°S)

- Jardín en DORMANCIA + lluvia. **NO inventar urgencia; usuario no puede salir.** ~62 días a primavera (equinoccio 23/09); heladas tardías posibles hasta ~fin agosto (pegan al sur y este al amanecer).
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA en julio) — mediterráneo, odia pies mojados; palta B-22/B-36 y pindó B-8 con fruto; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, pera B-39) acumulando frío+agua → primeros en florecer en agosto; perennes verdes (guayabo F-1, mirto B-27, hiedra B-15). Hortensia B-5a = la más sedienta (= gran ganadora de la lluvia).
- Efecto lluvia (horticultura estándar): riego profundo; agua voltea pulgones y desarma hormigas (Gardenia B-25); enjuaga fumagina (Guayabo F-1); PERO mediterráneas (romero/lavanda B-10) resienten encharcamiento → hongos de base (Phytophthora).
- Tareas activas reales: Gardenia B-25 pulgones+hormigas (alta); Guayabo F-1 fumagina (alta, task-dia hoy); Liquidámbar B-37 limpieza copa (alta).

## Verificados clave (NO contradecir)

52 especies · 65 id_codes · 10 nativas · romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 · palta Hass B-36 = clon de 1926 (~80% mercado) · anacahuita B-16 = protegida por ley 1986 · hiedra B-15 = +400 años · liquidámbar B-37 = storax/«ámbar líquido» · gardenia B-25 = 600kg flores→1L Chanel Nº22 · pindó B-8 = fruto coco-banana mar-jul · B-41 caqui = identidad EN DUDA · B-46 vivero = ~30 plantines · B-49 = trifoliado ¿glicinia? (revela en primavera).

## TODO pendiente

- **Formatos SIN usar:** before/after con fotos del usuario; user=juez (litigios entre plantas). **Evitar:** countdown (cerrado), gesto, editorial-pasivo, app-pasiva, nota-larga, superlativo-fatigado, racha, biografías, Wrapped (fatigó), **chat-coral y alivio-pasivo (ambos murieron 22/07)**.
- Si ronda-medica o mercado-pases convierten → serializar (parte de guardia diario / informe de pretemporada). Si NO → el problema NO era pasividad y hay que revisar frecuencia/fatiga global.
- Regenerar dataset M de la rueda desde data_plants.py en build-time. Reconciliar arrays `pruning` antes de cualquier vista de poda.
