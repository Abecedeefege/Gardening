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

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide (síntesis 03/07)

El news-feed es el formato ganador. Dentro de él el ÁNGULO manda. **El eje que convierte amor→SUSCRIPCIÓN
es ASOMBRO/ESTATUS/CHISME/IDENTIDAD/HUMOR con número o morbo — NO la intimidad sola, NO lo utilitario, NO
el consejo sincero.** Evidencia medida acumulada:

**CONVIERTEN (love + suscripción SÍ + aprobado, dwell alto):**
- **📱 Feed (red-social, 1ª persona)** — dwell RÉCORD 208s, 😍×2, sub×2, aprob×2. Ganador absoluto. 1ª persona
  + gesto "seguir una cuenta" retiene y convierte más que nada. PROMOVIDO.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub SÍ + aprob + 115s/100%. '¿cuál sos vos?' convierte. PROMOVIDO.
- **🍵 Chusmerío (tabloide/chisme)** — sub SÍ + aprob + 86s/100%. El chisme con hecho real se reenvía solo. PROMOVIDO.
- **🏆 Récords (orgullo/superlativo)** — 😍 + sub SÍ + aprob + 141s/100%. Orgullo-número + número grande. PROMOVIDO.
- **📰 Diario (editorial/novedad)** — 😍 + sub SÍ + aprob + 92s/100%. Framing prensa "edición del día". PROMOVIDO.

**APRUEBAN TIBIO (tap Aprobar pero 'meh', SIN suscripción) — lindo pero sin gancho de "increíble":**
- **🧪 Superpoderes (utilidad/accionable)** — aprob 'meh' + 23s/10% + sin sub. La utilidad no dispara "increíble".
- **💌 Consultorio (consejo sincero/calidez)** — aprob 'meh' + 36s/5% + sin sub. El consejo sincero aprueba, no suscribe.
- **🎤 Confesiones (1ª persona/humor/vulnerabilidad, ciclo 33)** — 02/07: aprob + dwell ALTO 133s/100% PERO
  reaction 'meh' + SIN sub. PROMOVIDO 03/07 (TIBIO). **Lección clave:** la intimidad confesional RETIENE
  (133s, leyó todo) pero NO convierte a suscripción por sí sola. La 1ª persona convierte cuando además hay
  número/estatus (Feed 'seguidores') o chisme (Chusmerío) — la vulnerabilidad pura emociona pero no dispara
  el "increíble" ni el gesto de suscribir. Candidata a revisión si no retiene.

**RECHAZAN / NO TRACCIONAN:**
- **🗺️ Pasaporte (viajes/orígenes/geografía)** — RECHAZADO + sub NO pese a 54s/100%. Geografía no engancha. No relanzar.
- **💘 Amores del Cantero (romance/chisme del corazón, ciclo 33)** — DROPPED 03/07. Push despachado 16:21Z, sin
  apertura/reacción/sub en datos (cutoff 18:22Z). Ventana parcialmente incompleta PERO el usuario estuvo activo
  18:22Z (Feed directo) y no lo abrió → soft-negative. El motor chisme ya vive en el Chusmerío; no se relanza.

**Regla operativa para ángulos nuevos:** apuntar a ASOMBRO+NÚMERO, ESTATUS/ORGULLO, CHISME/MORBO, IDENTIDAD,
HUMOR, 1ª PERSONA-CON-GANCHO. Evitar: utilidad accionable, geografía/viajes, consejo sincero, e intimidad
"pura" sin número/chisme que la envuelva (aprueba y retiene pero no suscribe).

## 🎯 SEÑAL REAL MEDIDA — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 8 promovidas: Feed, Horóscopo, Chusmerío, Récords, Diario,
  Superpoderes(tibio), Consultorio(tibio), Confesiones(tibio) + Rueda.
- **Curiosidades verificadas (#curiosidades) = contenido #1 histórico y el MÁS resiliente.** Abre casi siempre por
  click directo. Sección fija; sostén del slot curio (3er push ancla).
- **🌍 mundo-jardin: asset GANADOR ×3** (click+😍+95-97s). NO es proposal. Disponible para rotar en un slot curio.
- **🌿 Duelo = juego GANADOR 6/6 ×3** PERO necesita ≥3-4 días de descanso; el uso seguido lo mata.
- **Perdedores confirmados:** herramientas utilitarias (mapas/calendarios/dashboards ✗); formatos LENTOS (mazo
  flip-card ✗×3); memory-match (0); postales como experiencia SEPARADA (amor era novedad, no formato); cual-sobra
  (removido por el usuario); Rueda sobre-expuesta (fuera del push desde 17/06); Pasaporte/viajes (rechazado);
  Amores/romance (soft-negative). El eje consejo-sincero/utilidad/intimidad-pura aprueba sin suscribir.
- El usuario quiere **deleite + curiosidad verificada + news-feed emocional/chisme/identidad/orgullo/humor**, NO
  herramientas, NO mecánicas lentas, NO informativo-útil ni consejo sincero.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 02/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-02T18:22Z**. Cubre Confesiones (medida). NO cubre la
  ventana real de Amores (despacho 16:21Z, sin apertura hasta el cutoff) NI el curio Caqui B-41 (despacho 23:36Z,
  post-cutoff — su click puede aparecer mañana).
- Compactación 03/07: 18/06 cruzó el umbral >14 días → movido a daily_summary (engagement 18/06:
  sent3/click2/visits3/appr1; send_log 18/06: sent3). Ventana viva ahora **19/06–02/07**.

## Conclusiones de los pushN enviados (por feedback real)

- **29/06** — Diario + Récords → ambos 😍 + SUSCRIPCIÓN SÍ + aprobados (92s/141s). PROMOVIDOS.
- **30/06** — **Feed → 😍×2 + sub×2 + aprob×2 + 208s (RÉCORD)**; **Pasaporte → RECHAZADO + sub NO (54s)**.
- **30/06 ciclo 31** — **Chusmerío → sub SÍ + aprob + 86s (GANÓ)**; **Superpoderes → 'meh' + 23s + sin sub (tibio)**.
- **01/07 ciclo 32** — **Horóscopo → 😍 + sub SÍ + aprob + 115s (GANÓ, identidad)**; **Consultorio → 'meh' + 36s +
  sin sub (TIBIO, consejo sincero)**; curio Evónimo B-44 → CLICK.
- **02/07 ciclo 33 (🎤 Confesiones 08:30 / 💘 Amores 13:00 / curio Caqui B-41 19:30)** — medido parcial (cutoff 18:22Z):
  **Confesiones → aprob + 133s/100% PERO 'meh' + sin sub (TIBIO — intimidad retiene, no suscribe)**; **Amores → sin
  señal, soft-negative, DROPPED**; **Caqui → post-cutoff, sin datos aún**.

## 🔭 Corrida 03/07 — ciclo 34 (esta corrida)

- **Proposals resueltas:** Confesiones→PROMOVIDO (TIBIO, aprobó+133s pero sin sub; añadida a Ideas → ✨ Experiencias,
  footer a nota de integración). Amores→DROPPED (soft-negative + regla de no-supervivencia; página+pitch git rm).
- **2 experiencias NUEVAS de cero (proposals pending, created=03/07), vía agentes persona — ambas apuntan a ejes
  ganadores con frame de ENTRETENIMIENTO fresco, evitando la intimidad-pura que salió tibia:**
  - ⚽ **El Mundial del Jardín** (`engage/2026-07-03-mundial-jardin.html`) — COMPETENCIA/ORGULLO/PERTENENCIA con
    timing del Mundial de fútbol REAL 2026 (se juega ahora). 8 plantas = selecciones; cada cruce lo gana el
    superlativo real (hiedra B-15 +400a, caqui B-41 600a, cinta B-12 NASA, mandarina B-24 la más antigua) y la
    final la gana una NATIVA URUGUAYA (Anacahuita B-16 protegida por ley / Guayabo F-1) = pay-off de orgullo local.
    Apuesta: orgullo-número (Récords 141s) + drama deportivo + gancho cultural del Mundial. Promotor a (08:30).
  - 📺 **El Reality del Jardín** (`engage/2026-07-03-reality-jardin.html`) — REALITY SHOW estilo Gran Hermano
    (fenómeno rioplatense): plantas participantes con confesionario 1ª persona, nominaciones, "el más votado".
    Cada una esconde un secreto REAL (lantana B-29 miente su edad, crespón B-9 se desnuda en invierno, ciruela
    B-38 pasaporte falso, rosa de Siria B-18 belleza de 1 día, madreselva B-40 nombre exagerado, jazmín B-2 hijos
    sin permiso, liquidámbar B-37 sangra perfume, podranea F-2 se cambió el apellido). Apuesta: motor viral del
    Chusmerío llevado al reality serializado. Promotor b (13:00).
- **Cola ciclo 34:** (a) 08:30 ⚽ Mundial; (b) 13:00 📺 Reality; (c) 19:30 curio **Pera Williams B-39** (doble robo de
  nombre: la cultivó Stair 1765, la compró Williams; en EE.UU. la llaman Bartlett) → index #curiosidades. Fresca, no usada.
- **Watch 34:** ¿el frame ENTRETENIMIENTO (competencia/orgullo + reality/chisme) convierte amor→SUSCRIPCIÓN mejor que
  la intimidad-pura de Confesiones? Confirma la regla "asombro/número/chisme convierte; intimidad sola retiene pero no
  suscribe". Si una NO junta aprobación con ventana limpia, se dropea el 04/07.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (curios): cítricos cargados (mandarina B-24, limonero B-23); caqui B-41 fruta may-jul;
  romero B-26 flor jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, ciruelos F-4/B-38,
  pera Williams B-39); perennes verdes (mirto B-27, guayabo F-1, lavanda B-19, evónimo B-44).
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial=Diario, superlativos=Récords, red-social=Feed, viajes=Pasaporte(✗),
  tabloide=Chusmerío, utilidad=Superpoderes(tibio), identidad=Horóscopo(✓), consejo/calidez=Consultorio(tibio),
  confesión/1ª-persona=Confesiones(tibio), romance=Amores(✗), competencia/deporte=Mundial(hoy), reality/GH=Reality(hoy).
  **Sin usar (apuntar a asombro/número/estatus/humor):** efemérides "un día como hoy", before/after con fotos del
  usuario, entrevista/Q&A a una planta, awards/gala de premios, memes/humor absurdo verificado, playlist/canción.
- **Curios frescos NO usados** (fun_fact verificado): pera Williams B-39 (HOY curio), luego revisar clivia B-13
  (100 años/1830), rosa de Siria B-18 (flor 1 día), lantana B-29 (cambia de color). Plantas MUY usadas a descansar:
  B-1/B-36/B-3/B-5/I-2/F-9 (Confesiones), B-27/B-25/B-4 (Amores).
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
