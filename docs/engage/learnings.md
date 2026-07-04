# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots base: 08:30 / 13:00 / 19:30 (-03:00).
Primer send_at ≥60 min después de la corrida (margen de deploy de Vercel para páginas linkeadas).
expires_at = mismo día 22:00 -03:00. Cada notificación a un destino DISTINTO. Timestamps SIEMPRE con `-03:00`.
**3 pushes curados ganan a 20 — CONFIRMADO.** El usuario abre 2-3/día sin importar cuántos mandes.

## 🆕 FUNCIÓN PARALELA (pedido del usuario 28/06): 2 experiencias NUEVAS de cero por corrida

En cada corrida inicializo DOS agentes con persona product/UX/sales que construyen DOS experiencias
news-feed de cero, cada una con: (1) reacción final "¿te voló la cabeza?" (engageReact target=slug corto),
(2) CTA de **suscripción diaria** (engageAnswer qid `<slug>-suscripcion-diaria`), (3) un **HTML de pitch**
aparte con 6 modelos de monetización (3 innovadores + 3 ultra-creativos). Contrato de proposal igual que
siempre (link "← Volver al sitio estable" primero, react+sub+engage-actions, `engage.js`, SOLO datos
verificados de data_plants.py con código). Dos de los 3 pushes llevan a estas experiencias; el 3º es el
curio ancla (#curiosidades).

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide (síntesis 04/07)

El news-feed es el formato ganador. Dentro de él el ÁNGULO manda. **El eje que convierte amor→SUSCRIPCIÓN
es ASOMBRO/ESTATUS/CHISME/IDENTIDAD con número o morbo — NO la intimidad sola, NO lo utilitario, NO el
consejo sincero, NO la competencia deportiva, NO el reality serializado.** Evidencia medida acumulada:

**CONVIERTEN (love + suscripción SÍ + aprobado, dwell alto):**
- **📱 Feed (red-social, 1ª persona)** — dwell RÉCORD 208s, 😍×2, sub×2, aprob×2. Ganador absoluto. PROMOVIDO.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub SÍ + aprob + 115s/100%. '¿cuál sos vos?' convierte. PROMOVIDO.
- **🍵 Chusmerío (tabloide/chisme)** — sub SÍ + aprob + 86s/100%. El chisme con hecho real se reenvía solo. PROMOVIDO.
- **🏆 Récords (orgullo/superlativo)** — 😍 + sub SÍ + aprob + 141s/100%. Orgullo-número + número grande. PROMOVIDO.
- **📰 Diario (editorial/novedad)** — 😍 + sub SÍ + aprob + 92s/100%. Framing prensa "edición del día". PROMOVIDO.

**APRUEBAN TIBIO (tap Aprobar pero 'meh', SIN suscripción) — lindo pero sin gancho de "increíble":**
- **🧪 Superpoderes (utilidad/accionable)** — 'meh' + 23s/10% + sin sub. La utilidad no dispara "increíble".
- **💌 Consultorio (consejo sincero/calidez)** — 'meh' + 36s/5% + sin sub. El consejo sincero aprueba, no suscribe.
- **🎤 Confesiones (1ª persona/intimidad)** — aprob + 133s/100% PERO 'meh' + sin sub. La intimidad RETIENE, no convierte.
- **📺 Reality (Gran Hermano serializado, ciclo 34)** — 03/07: aprob + 62s/100% PERO 'meh' + sin sub. PROMOVIDO
  04/07 (TIBIO). El reality retuvo menos que Confesiones (62s vs 133s) y tampoco suscribió: la serialización
  ("capítulo de mañana") NO fue gancho suficiente. Chisme convierte como TABLOIDE (dato directo), no como drama actuado.

**RECHAZAN / NO TRACCIONAN:**
- **⚽ Mundial (competencia/deporte, ciclo 34)** — RECHAZO EXPLÍCITO 03/07 pese a dwell 87s/100%: 'meh' + sub NO +
  botón "No me interesa". Leyó todo y aun así lo rechazó → la competencia inventada entre plantas no vale la
  suspensión de incredulidad; el "drama deportivo" diluye el dato real. No relanzar deportes/torneos.
- **🗺️ Pasaporte (viajes/orígenes)** — RECHAZADO + sub NO pese a 54s/100%. Geografía no engancha. No relanzar.
- **💘 Amores del Cantero (romance)** — soft-negative (push sin apertura con usuario activo). DROPPED 03/07.

**Regla operativa para ángulos nuevos:** apuntar a ASOMBRO+NÚMERO, ESTATUS/ORGULLO, CHISME/MORBO-directo,
IDENTIDAD, HUMOR. Evitar: utilidad, geografía, consejo sincero, intimidad pura, competencia/torneo inventado,
drama serializado/actuado. **El patrón se afina: el usuario suscribe cuando el DATO REAL es el protagonista
(récord, chisme, identidad); rechaza o tibia cuando la FICCIÓN es la protagonista y el dato es utilería
(mundial, reality, romance).** La ficción liviana como envoltorio sí; la ficción como plato principal no.

## 🎯 SEÑAL REAL MEDIDA — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 9 promovidas: Feed, Horóscopo, Chusmerío, Récords, Diario,
  Superpoderes(tibio), Consultorio(tibio), Confesiones(tibio), Reality(tibio) + Rueda.
- **Curiosidades verificadas (#curiosidades) = contenido #1 histórico** PERO ⚠️ 2 curios seguidos sin click:
  Caqui B-41 (02/07-c, despacho tardío 20:36 UY) sin click en ventana completa de 24h; Pera Williams B-39
  (03/07-c, despacho 19:45 UY) sin click hasta cutoff 23:14Z (ventana parcial — puede aparecer mañana).
  Posible fatiga del slot curio 19:30 o del formato "andá a Curiosidades". VIGILAR: si Pera tampoco clickeó,
  probar rotar el 3er slot (mundo-jardin, duelo descansado, o curio a OTRA hora).
- **🌍 mundo-jardin: asset GANADOR ×3** (click+😍+95-97s). NO es proposal. Disponible para rotar en un slot.
- **🌿 Duelo = juego GANADOR 6/6 ×3** PERO necesita ≥3-4 días de descanso; el uso seguido lo mata. Último uso 23/06 → descansado.
- **Perdedores confirmados:** herramientas utilitarias (mapas/calendarios/dashboards ✗); formatos LENTOS (mazo
  flip-card ✗×3); memory-match (0); postales separadas; cual-sobra (removido por usuario); Rueda sobre-expuesta;
  Pasaporte/viajes (✗); Amores/romance (✗); Mundial/competencia (✗ explícito); Reality/serializado (tibio).
- El usuario quiere **deleite + dato real asombroso como protagonista** (récord/chisme/identidad/humor), NO
  herramientas, NO mecánicas lentas, NO ficción elaborada donde el dato es decorado.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 04/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-03T23:14Z**. Cubre Mundial y Reality completos.
  NO cubre el click del curio Pera Williams (despacho 22:45Z, cutoff 23:14Z — puede aparecer mañana).
- Compactación 04/07: 19/06 movido a daily_summary (sent3/click2/visits2/appr0 en engagement; sent3 en
  send_log). Ventana viva ahora **20/06–03/07**.

## Conclusiones de los pushN enviados (por feedback real)

- **29/06** — Diario + Récords → ambos 😍 + SUSCRIPCIÓN SÍ + aprobados (92s/141s). PROMOVIDOS.
- **30/06** — **Feed → 😍×2 + sub×2 + aprob×2 + 208s (RÉCORD)**; **Pasaporte → RECHAZADO + sub NO (54s)**.
- **30/06 ciclo 31** — **Chusmerío → sub SÍ + aprob + 86s (GANÓ)**; **Superpoderes → 'meh' + 23s + sin sub (tibio)**.
- **01/07 ciclo 32** — **Horóscopo → 😍 + sub SÍ + aprob + 115s (GANÓ)**; **Consultorio → 'meh' + 36s + sin sub
  (tibio)**; curio Evónimo B-44 → CLICK.
- **02/07 ciclo 33** — **Confesiones → aprob + 133s/100% PERO 'meh' + sin sub (TIBIO)**; **Amores → sin señal,
  soft-negative, DROPPED**; **curio Caqui B-41 → SIN CLICK en ventana completa (primera vez que un curio no abre)**.
- **03/07 ciclo 34** — **Mundial → RECHAZO EXPLÍCITO** (click 10:47 UY, 87s/100%, 'meh', sub NO, "No me interesa" —
  leyó todo y lo rechazó igual: la ficción deportiva no vale el dato); **Reality → APROBADO TIBIO** (17:21 UY, 62s/100%,
  'meh', sin sub — retuvo menos que Confesiones y tampoco suscribió; promovido por regla de aprobación explícita);
  **curio Pera Williams B-39 → sin datos aún (despacho 19:45 UY, post-cutoff)**.
- **Meta-conclusión de la serie completa:** 5 convierten (dato-protagonista), 4 tibias (envoltorio emocional sin
  gancho), 3-4 rechazadas (ficción-protagonista). El "increíble" + suscripción aparece SOLO cuando el push promete
  y la página entrega un dato real con número/morbo/identidad en el primer scroll.

## 🔭 Corrida 04/07 — ciclo 35 (esta corrida)

- **Proposals resueltas:** Mundial→DROPPED (rechazo explícito; página+pitch git rm). Reality→PROMOVIDO (TIBIO;
  entrada en Ideas → ✨ Experiencias vía build.py, footer a nota de integración).
- **2 experiencias NUEVAS de cero (pending, created=04/07), vía agentes persona — ambas ponen el DATO como
  protagonista con envoltorio liviano, corrigiendo la lección del ciclo 34:**
  - 🏆 **La Gala de Premios del Jardín** (`engage/2026-07-04-gala-jardin.html`) — premios estilo Oscars con
    categorías ganadas por superlativos REALES y discursos 1ª persona con humor. Apuesta: ESTATUS/ORGULLO+NÚMERO
    (el eje de Récords, el 2º mejor) con envoltorio de gala, no de torneo. Promotor a (08:30).
  - 😂 **Memes del Jardín** (`engage/2026-07-04-memes-jardin.html`) — feed de memes CSS/texto con remate de dato
    verificado ("no es chiste: dato real"). Apuesta: HUMOR es el único eje ganador sin probar; el meme es
    compartible y el dato es el punchline, no el decorado. Promotor b (13:00).
- **Cola ciclo 35:** (a) 08:30 🏆 Gala; (b) 13:00 😂 Memes; (c) 19:30 curio **Clivia B-13** (puede vivir 100 años;
  hay ejemplares de 1830; honra a Charlotte Clive) → index #curiosidades. Si el curio tampoco clickea hoy
  (3ª vez seguida), mañana rotar el slot c a otro asset/hora.
- **Watch 35:** ¿dato-protagonista con envoltorio liviano (gala/meme) convierte donde ficción-protagonista
  (mundial/reality) falló? Y ¿el slot curio 19:30 sigue vivo? Si una proposal no junta aprobación con ventana
  limpia, se dropea el 05/07.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (curios): cítricos cargados (mandarina B-24, limonero B-23); caqui B-41 fruta may-jul;
  romero B-26 flor jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, ciruelos F-4/B-38,
  pera Williams B-39); perennes verdes (mirto B-27, guayabo F-1, lavanda B-19, evónimo B-44).
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial=Diario(✓), superlativos=Récords(✓), red-social=Feed(✓), viajes=Pasaporte(✗),
  tabloide=Chusmerío(✓), utilidad=Superpoderes(tibio), identidad=Horóscopo(✓), consejo=Consultorio(tibio),
  confesión=Confesiones(tibio), romance=Amores(✗), competencia=Mundial(✗), reality=Reality(tibio),
  premios/gala=Gala(hoy), humor/memes=Memes(hoy).
  **Sin usar (apuntar a asombro/número/estatus/humor):** efemérides "un día como hoy", before/after con fotos del
  usuario, entrevista/Q&A a una planta, playlist/canción, subasta/tasación ("¿cuánto vale tu jardín?").
- **Curios frescos NO usados** (fun_fact verificado): tras Clivia B-13 (HOY), quedan rosa de Siria B-18 (flor de
  1 día), lantana B-29 (cambia de color). Plantas a descansar: B-1/B-36/B-3/B-5/I-2/F-9/B-27/B-25/B-4 + elenco
  Mundial (B-15/B-41/B-12/B-24/B-16/F-1) + elenco Reality (B-29/B-9/B-38/B-18/B-40/B-2/B-37/F-2).
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
