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
experiencias; el 3º es el curio ancla.

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide (dato 30/06, sincronizado 01/07)

El news-feed es el formato ganador (Diario+Récords 29/06). El dato del ciclo 30/31, que recién
sincronizó el 01/07, prueba que **dentro del news-feed el ÁNGULO manda**. Resultados medidos:

- **📱 Feed (red-social, 1ª persona) → GANADOR ABSOLUTO.** 30/06: 😍love ×2 + suscripción SÍ ×2 +
  aprobado ×2 + dwell **142s Y 208s**/100%. El **208s es el DWELL RÉCORD del canal** (batió 141s de Récords).
  El gesto "seguir una cuenta" + voz en 1ª persona + formato IG retiene y convierte más que nada. PROMOVIDO.
- **🍵 Chusmerío (tabloide/chisme) → GANADOR.** 30/06: suscripción SÍ + aprobado + 86s/100%. El chisme
  con hecho verificado convierte. 2º mejor del ciclo. PROMOVIDO.
- **🧪 Superpoderes (utilidad/asombro) → APROBADO PERO TIBIO.** 30/06: tocó Aprobar (→promovido, la
  aprobación es el único pase a permanencia) PERO reaction 'meh' + 23s/scroll 10% + **NO tocó suscripción**.
  Aprobó sin amar ni suscribirse. **La utilidad accionable gana la aprobación pero NO la suscripción.** Es
  la más débil de las promovidas; candidata #1 a revisión si no retiene.
- **🗺️ Pasaporte (viajes/orígenes/geografía) → RECHAZADO.** 30/06: proposal_rejected + suscripción NO,
  y eso que leyó 54s/scroll 100%. **Primer news-feed que el usuario rechaza.** Leerlo entero no bastó:
  el ángulo viajes/geografía/patrimonio NO dispara el "increíble". Ángulo perdedor. No relanzar.

**Síntesis de ángulos (la lección central hoy):**
- CONVIERTEN a suscripción: **social/1ª-persona (Feed), chisme/humor (Chusmerío), orgullo-número (Récords),
  editorial-novedad (Diario).** Todos tocan EMOCIÓN/IDENTIDAD/ESTATUS.
- NO convierten: **utilidad/accionable (Superpoderes: aprueba, no se suscribe), viajes/geografía
  (Pasaporte: rechaza).** Lo informativo-útil o lo geográfico no genera el gancho emocional.
- **Hipótesis operativa:** el eje que convierte amor→SUSCRIPCIÓN es emocional/identitario, no utilitario.
  Los próximos ángulos deben apuntar a IDENTIDAD, PERTENENCIA, HUMOR, ORGULLO, AFECTO.

## 🎯 SEÑAL REAL MEDIDA — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = el formato #1.** Curiosidad servida como feed scrolleable +
  reacción + CTA de suscripción. 5 promovidas ya (Feed, Chusmerío, Superpoderes, Récords, Diario) + Rueda.
- **Curiosidades verificadas (#curiosidades) = contenido #1 histórico y el MÁS resiliente.** Abre casi
  siempre por click directo. Sección fija; sigue siendo el sostén del slot curio (3er push ancla).
- **🌍 mundo-jardin (del usuario): asset GANADOR ×3** (23/25/27, click+😍love+95-97s). Rota día por medio.
  NO es proposal (lo creó el usuario). Descansó desde 28/06 → disponible para rotar en un slot curio futuro.
- **🌿 Duelo = juego GANADOR 6/6 ×3** (15/22/26) PERO necesita ≥3-4 días de descanso; el uso seguido lo mata.
- **Perdedores confirmados:** herramientas utilitarias (mapas/calendarios/dashboards ✗); formatos LENTOS
  (mazo flip-card ✗×3); memory-match (0); postales como experiencia SEPARADA (el amor era novedad, no
  formato); cual-sobra (removido por el usuario); Rueda del año sobre-expuesta (fuera del push desde 17/06);
  y ahora **Pasaporte/viajes (rechazado 30/06)** dentro del news-feed.
- El usuario quiere **deleite + curiosidad verificada + news-feed emocional/identitario**, NO herramientas
  ni mecánicas lentas ni ángulos meramente informativos.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 01/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json se actualiza cuando el usuario interactúa. Su último sync fue
  **2026-06-30T23:50Z** — cubre TODO el ciclo 30 y 31 (Feed/Pasaporte/Chusmerío/Superpoderes ya medidos).
- Compactación 01/07: 16/06 cruzó el umbral >14 días → movido a daily_summary (engagement 16/06:
  sent20/click1/visits3/appr0; send_log 16/06: sent20). Ventana viva ahora **17–30/06**.

## Conclusiones de los pushN enviados (por feedback real)

- **27/06** — 2/3. A(curio Ciruelo F-4)→CLICK; B(🌍 mundo)→CLICK+😍love+97s; C tras cutoff.
- **28/06** — B(🌿 Duelo, solo 1d descanso)→sin juego; C(curio Mirto B-27)→CLICK al día sgte.
- **29/06 (noche del 28)** — Diario + Récords descubiertos directo → ambos 😍love + SUSCRIPCIÓN SÍ + aprobados + 92s/141s. PROMOVIDOS.
- **29/06 ciclo 30 (Feed 08:30 / Pasaporte 13:00 / Lavanda 19:30)** — medido el 30/06 al sincronizar:
  **Feed → 😍×2 + sub×2 + aprob×2 + 208s (RÉCORD)**; **Pasaporte → RECHAZADO + sub NO (leyó 54s)**.
- **30/06 ciclo 31 (Chusmerío 08:30 / Superpoderes 13:00 / Lapachillo 19:30)** — **Chusmerío → sub SÍ +
  aprob + 86s (GANÓ)**; **Superpoderes → aprob pero 'meh' + 23s/10% + sin sub (tibio)**; **Lapachillo B-14
  → CLICK 23:50Z** (curio ancla funcionó, abrió directo a index).

## 🔭 Corrida 01/07 — ciclo 32 (esta corrida)

- **Proposals resueltas con dato ya sincronizado:** Feed→PROMOVIDO, Chusmerío→PROMOVIDO,
  Superpoderes→PROMOVIDO (tibio), Pasaporte→DROPPED (rechazado; página+pitch git rm). Las 3 promovidas
  se sumaron a Ideas → ✨ Experiencias con su tarjeta; footers pasados a "ya integrada".
- **2 experiencias NUEVAS de cero (proposals pending, created=01/07, test limpio), vía agentes persona —
  ambas apuntan al eje EMOCIONAL/IDENTITARIO que la síntesis de ángulos marcó como el que convierte:**
  - 🔮 **El Horóscopo del Jardín** (`engage/2026-07-01-horoscopo-jardin.html`) — news-feed IDENTIDAD:
    cada planta un 'signo' con lectura del día (personalidad+predicción) sobre rasgo real verificado.
    Apuesta: '¿cuál sos vos?' + compartibilidad + categoría de monetización probada. Promotor a (08:30).
  - 💌 **El Consultorio del Jardín** (`engage/2026-07-01-consultorio-jardin.html`) — news-feed CALIDEZ:
    cada planta una columnista que da un consejo de vida anclado en un dato real. Apuesta: afecto +
    frase-del-día screenshot-eable + mercado wellness/daily-affirmation. Promotor b (13:00).
- **Cola ciclo 32:** (a) 08:30 🔮 Horóscopo; (b) 13:00 💌 Consultorio; (c) 19:30 curio **Abelia F-7**
  (naufragio de Clarke Abel: el barco se hundió al volver, la planta sobrevivió, las semillas se perdieron;
  fresca, seasonless, NO usada en ninguna experiencia). → index #curiosidades.
- **Watch 32:** ¿el ángulo IDENTIDAD (Horóscopo) o AFECTO (Consultorio) convierte amor→suscripción como
  el social/chisme? Confirma o refuta la hipótesis "lo emocional/identitario convierte, lo utilitario no".
  Si una NO junta aprobación con ventana limpia, se dropea el 02/07.

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (curios): cítricos cargados (mandarina B-24, limonero B-23); caqui B-41 fruta
  may-jul; romero B-26 flor jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37,
  ciruelos F-4/B-38); perennes verdes (mirto B-27, guayabo F-1, lavanda B-19, evónimo B-44).
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Hay 1 upload pending (B-15) → lo procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial=Diario, superlativos=Récords, red-social=Feed, viajes=Pasaporte(✗),
  tabloide=Chusmerío, utilidad=Superpoderes(tibio), identidad=Horóscopo(hoy), afecto/consejo=Consultorio(hoy).
  **Sin usar (apuntar a lo emocional):** efemérides "un día como hoy", before/after con fotos del usuario,
  entrevista/Q&A a una planta, "confesiones", cartas de amor entre plantas.
- **Curios frescos NO usados** (fun_fact verificado): fresno F-10 (dioico, samaras helicóptero), pera
  Williams B-39 (doble robo de nombre), difenbaquia I-2 (caña muda, tóxica). Plantas MUY usadas a descansar:
  B-1/B-12/B-16/B-23/B-25/B-15/B-36/F-1/F-8/B-29.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
</content>
