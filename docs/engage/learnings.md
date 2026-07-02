# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json), NO con `tools/gen_queue.py`.
Slots base: 08:30 / 13:00 / 19:30 (-03:00). Primer send_at ≥60 min después de la corrida
(margen de deploy de Vercel para páginas linkeadas). expires_at = mismo día 22:00 -03:00.
Cada notificación a un destino DISTINTO. **3 pushes curados ganan a 20 — CONFIRMADO.**
El usuario abre 2-3/día sin importar cuántos mandes; más pushes solo diluye y sepulta lo nuevo.

## 🆕 FUNCIÓN PARALELA (pedido del usuario 28/06): 2 experiencias NUEVAS de cero por corrida

En cada corrida inicializo DOS agentes con persona product/UX/sales que construyen DOS experiencias
news-feed de cero, cada una con: (1) reacción final "¿te voló la cabeza?" (engageReact), (2) CTA de
**suscripción diaria** (engageAnswer `<slug>-suscripcion-diaria`), (3) un **HTML de pitch** aparte con
6 modelos de monetización (3 innovadores + 3 ultra-creativos). Contrato de página proposal igual que
siempre (link "← Volver al sitio estable" primero, botones Aprobar/No-me-interesa, `engage.js`, solo
datos verificados de data_plants.py con códigos). Dos de los 3 pushes del día llevan a estas
experiencias; el 3º es el curio ancla. engageReact target = slug corto; qid = `<slug>-suscripcion-diaria`.

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide (síntesis ACTUALIZADA 02/07)

El news-feed es el formato ganador. Dentro de él el ÁNGULO manda. **El eje que convierte amor→SUSCRIPCIÓN
es EMOCIONAL/IDENTITARIO/HUMOR, no utilitario ni sincero-tibio.** Evidencia medida acumulada:

**CONVIERTEN (love + suscripción SÍ + aprobado, dwell alto):**
- **📱 Feed (red-social, 1ª persona)** — dwell RÉCORD 208s (+142s), 😍×2, sub×2, aprob×2. El ganador absoluto.
  Voz en 1ª persona + gesto "seguir una cuenta" retiene y convierte más que nada. PROMOVIDO.
- **🔮 Horóscopo (IDENTIDAD, ciclo 32)** — 01/07: 😍love + sub SÍ + aprobado + 115s/100%. '¿cuál sos vos?'
  convierte. Confirma el eje identidad. PROMOVIDO 02/07.
- **🍵 Chusmerío (tabloide/chisme)** — sub SÍ + aprob + 86s/100%. El chisme con hecho real se reenvía. PROMOVIDO.
- **🏆 Récords (orgullo/superlativo)** — 😍 + sub SÍ + aprob + 141s/100%. Orgullo-número + número grande. PROMOVIDO.
- **📰 Diario (editorial/novedad)** — 😍 + sub SÍ + aprob + 92s/100%. Framing prensa "edición del día". PROMOVIDO.

**APRUEBAN TIBIO (tap Aprobar pero 'meh', dwell bajo, SIN suscripción) — útil-lindo, sin gancho:**
- **🧪 Superpoderes (utilidad/accionable)** — aprob pero 'meh' + 23s/10% + sin sub. La utilidad no dispara "increíble".
- **💌 Consultorio (consejo sincero/calidez, ciclo 32)** — 01/07: aprob pero 'meh' + 36s/5% + sin sub. **MISMO patrón
  que la utilidad: el consejo SINCERO/columna-sabiduría gana la aprobación pero NO la suscripción.** PROMOVIDO 02/07 (débil).
  Lección: la calidez sincera rinde como lo utilitario. Para convertir hay que ENVOLVER el afecto en humor/chisme/identidad,
  no entregarlo como consejo directo. Candidata #1 a revisión si no retiene.

**RECHAZAN (proposal_rejected + sub NO, aun leyéndolo entero):**
- **🗺️ Pasaporte (viajes/orígenes/geografía)** — RECHAZADO + sub NO pese a 54s/100%. Geografía/patrimonio no engancha. No relanzar.

**Regla operativa para elegir ángulos nuevos:** apuntar a IDENTIDAD, PERTENENCIA, HUMOR, ORGULLO, 1ª PERSONA, CHISME.
Evitar: utilidad accionable, geografía/viajes, y consejo/sabiduría entregado en tono sincero (envolverlo en humor si se usa).

## 🎯 SEÑAL REAL MEDIDA — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = el formato #1.** Feed scrolleable + reacción + CTA suscripción.
  7 promovidas: Feed, Horóscopo, Chusmerío, Récords, Diario, Superpoderes(tibio), Consultorio(tibio) + Rueda.
- **Curiosidades verificadas (#curiosidades) = contenido #1 histórico y el MÁS resiliente.** Abre casi
  siempre por click directo. Sección fija; sigue siendo el sostén del slot curio (3er push ancla).
- **🌍 mundo-jardin (del usuario): asset GANADOR ×3** (23/25/27, click+😍love+95-97s). NO es proposal. Descansa
  desde 28/06 → disponible para rotar en un slot curio futuro.
- **🌿 Duelo = juego GANADOR 6/6 ×3** (15/22/26) PERO necesita ≥3-4 días de descanso; el uso seguido lo mata.
- **Perdedores confirmados:** herramientas utilitarias (mapas/calendarios/dashboards ✗); formatos LENTOS
  (mazo flip-card ✗×3); memory-match (0); postales como experiencia SEPARADA (el amor era novedad, no
  formato); cual-sobra (removido por el usuario); Rueda sobre-expuesta (fuera del push desde 17/06);
  Pasaporte/viajes (rechazado 30/06); y ahora el eje consejo-sincero/utilidad aprueba-sin-suscribir.
- El usuario quiere **deleite + curiosidad verificada + news-feed emocional/identitario/humor**, NO
  herramientas, NO mecánicas lentas, NO ángulos informativos-útiles ni consejo sincero.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 02/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json se actualiza cuando el usuario interactúa. Último sync
  **2026-07-01T23:53Z** — cubre TODO el ciclo 32 (Horóscopo/Consultorio/curio-Evónimo ya medidos).
- Compactación 02/07: 17/06 cruzó el umbral >14 días → movido a daily_summary (engagement 17/06:
  sent13/click1/visits4/appr0; send_log 17/06: sent13). Ventana viva ahora **18/06–01/07**.

## Conclusiones de los pushN enviados (por feedback real)

- **28/06** — B(🌿 Duelo, 1d descanso)→sin juego; C(curio Mirto B-27)→CLICK al día sgte.
- **29/06** — Diario + Récords descubiertos directo → ambos 😍love + SUSCRIPCIÓN SÍ + aprobados + 92s/141s. PROMOVIDOS.
- **29/06 ciclo 30 (Feed 08:30 / Pasaporte 13:00 / Lavanda 19:30)** — medido 30/06:
  **Feed → 😍×2 + sub×2 + aprob×2 + 208s (RÉCORD)**; **Pasaporte → RECHAZADO + sub NO (leyó 54s)**.
- **30/06 ciclo 31 (Chusmerío 08:30 / Superpoderes 13:00 / Lapachillo 19:30)** — **Chusmerío → sub SÍ +
  aprob + 86s (GANÓ)**; **Superpoderes → aprob pero 'meh' + 23s/10% + sin sub (tibio)**; **Lapachillo B-14 → CLICK**.
- **01/07 ciclo 32 (🔮 Horóscopo 08:30 / 💌 Consultorio 13:00 / curio Evónimo B-44 19:30)** — medido 01/07 noche:
  **Horóscopo → 😍love + sub SÍ + aprob + 115s/100% (GANÓ — identidad convierte)**; **Consultorio → aprob pero
  'meh' + 36s/5% + sin sub (TIBIO — consejo sincero aprueba, no suscribe)**; **curio Evónimo B-44 → CLICK a index 23:53Z**.

## 🔭 Corrida 02/07 — ciclo 33 (esta corrida)

- **Proposals resueltas con dato sincronizado:** Horóscopo→PROMOVIDO (fuerte, identidad convierte),
  Consultorio→PROMOVIDO (TIBIO, aprobó sin suscribir; consejo sincero = techo aprobación). Ambas sumadas a
  Ideas → ✨ Experiencias (build.py approved_experiences); footers pasados a "ya integrada".
- **2 experiencias NUEVAS de cero (proposals pending, created=02/07, test limpio), vía agentes persona —
  ambas DUPLICAN los ejes ganadores (1ª persona/humor + chisme), evitando el tono sincero que salió tibio:**
  - 🎤 **Confesiones del Jardín** (`engage/2026-07-02-confesiones-jardin.html`) — news-feed 1ª persona +
    HUMOR + VULNERABILIDAD: cada planta confiesa un secreto real (clon Hass B-36, caña muda I-2, impostora B-3,
    invasora F-9, camaleónica B-5, robo-crédito B-1...). Apuesta: la voz que dio el récord (Feed 208s) + intimidad
    confesional + compartibilidad. Promotor a (08:30).
  - 💘 **Amores del Cantero** (`engage/2026-07-02-amores-cantero.html`) — news-feed tabloide de ROMANCES
    (revista del corazón, tono chisme juguetón, NO consejo sincero): mirto B-27 de Venus, romero B-26 fiel,
    fresno F-10 dioico, gardenia B-25 femme fatale, abelia F-7 naufragio, buganvilia B-1 Jeanne Baret. Apuesta:
    el motor viral del Chusmerío llevado al romance (se reenvía solo). Promotor b (13:00).
- **Cola ciclo 33:** (a) 08:30 🎤 Confesiones; (b) 13:00 💘 Amores; (c) 19:30 curio **Caqui B-41**
  ("fruto de los dioses" — Diospyros; en Japón símbolo de longevidad, caquis de 600 años aún produciendo;
  fruta AHORA en pleno invierno may-jul; astringente hasta ablandar). Fresca, estacional REAL, no usada en experiencias.
  → index #curiosidades.
- **Watch 33:** ¿Confesiones (1ª persona/humor) y Amores (chisme romántico) convierten amor→suscripción como
  Feed/Chusmerío? Confirma la regla "envolver afecto en humor/chisme convierte; entregarlo sincero no".
  Si una NO junta aprobación con ventana limpia, se dropea el 03/07.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (curios): cítricos cargados (mandarina B-24, limonero B-23); caqui B-41 fruta
  may-jul; romero B-26 flor jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37,
  ciruelos F-4/B-38); perennes verdes (mirto B-27, guayabo F-1, lavanda B-19, evónimo B-44).
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial=Diario, superlativos=Récords, red-social=Feed, viajes=Pasaporte(✗),
  tabloide=Chusmerío, utilidad=Superpoderes(tibio), identidad=Horóscopo(✓), consejo/calidez=Consultorio(tibio),
  confesión/1ª-persona=Confesiones(hoy), romance/chisme=Amores(hoy).
  **Sin usar (apuntar a lo emocional/humor):** efemérides "un día como hoy", before/after con fotos del usuario,
  entrevista/Q&A a una planta, "rankings de personalidad", memes/humor absurdo verificado.
- **Curios frescos NO usados** (fun_fact verificado): pera Williams B-39 (doble robo de nombre), caqui B-41 (hoy curio).
  Plantas MUY usadas a descansar: B-1/B-12/B-16/B-23/B-25/B-36/F-1/F-8/B-29.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
