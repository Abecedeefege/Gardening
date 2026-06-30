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

## 🚀 BREAKTHROUGH 29/06 — la SUSCRIPCIÓN por fin se logró (news-feed = el formato que convierte)

La noche del 28 (eventos 00:33–00:43Z del 29) el usuario, por navegación DIRECTA, abrió las 2
experiencias del ciclo 29 y disparó la señal MÁS COMPLETA del canal:
- **📰 Diario de tu Jardín** → 😍love + answer `diario-suscripcion-diaria`=SÍ + proposal_approved + 92s/100%.
- **🏆 Récords de tu Jardín** → 😍love + answer `records-suscripcion-diaria`=SÍ + proposal_approved + **141s/100%** (dwell récord del canal).

Cierra el gap que mataron las postales (amor sí, suscripción nunca). **El formato NEWS-FEED convierte
amor→SUSCRIPCIÓN.** Validado: (a) framing editorial (Diario) y (b) orgullo/estatus+número-grande (Récords).
El ángulo orgullo retiene aún más (141s > 92s). → **AMBAS PROMOVIDAS 29/06**: páginas permanentes + links
fijos «📰 El Diario» y «🏆 Récords» en la nav del inicio. Footers sin botones aprobar/rechazar (nota de
integración + link al inicio); reacciones/suscripción siguen logueando. Status=promoted en proposals.json.

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **NEWS-FEED de contenido verificado = el formato ganador.** Evolución del activo #1: la curiosidad
  servida como feed scrolleable + reacción + CTA de suscripción. Convierte amor→suscripción (29/06).
- **Curiosidades verificadas (#curiosidades) = contenido #1 histórico y el MÁS resiliente.** Abre casi
  siempre por click directo. La SECCIÓN fija es el sostén fiable. Sigue siendo el núcleo del slot curio.
- **🌍 mundo-jardin (del usuario): asset GANADOR ×3** (23/25/27, click+😍love+95-97s/100%). Rota día por
  medio. NO es proposal (lo creó el usuario), vive en engage/. Descansó 28-30 → disponible para rotar.
- **🌿 Duelo = juego rápido GANADOR 6/6 ×3** (15/22/26) PERO necesita ≥3-4 días de descanso (el 28/06 con
  1 día de reposo NO repitió). El juego no está agotado; lo mata el uso seguido.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards: sol-jardin ✗×3,
  ano-jardin ✗); (b) formatos LENTOS (mazo flip-card ✗×3); (c) memory-match (0, 24/06); (d) postales/
  curiosidad-estacional como experiencia SEPARADA (cerrada 22/06: el amor de v1 era novedad, no formato);
  (e) cual-sobra: removido por el usuario (22/06), no re-promover; (f) Rueda del año: promovida pero
  sobre-expuesta → FUERA del push desde 17/06.
- El usuario quiere **deleite + contenido-curiosidad/verificado + news-feed**, NO herramientas ni mecánicas lentas.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 28/06.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **⚠️ CUTOFF DE DATOS (clave esta corrida):** engagement.json se actualiza cuando el usuario interactúa,
  NO a las 22:00. Su último sync fue **2026-06-29T13:11Z** — ANTES de que se mandaran los 3 pushes del
  ciclo 30 (feed 13:15Z, pasaporte 17:12Z, lavanda 23:33Z). ⇒ **0 datos sobre Feed/Pasaporte/lavanda
  todavía**: el dato del 29 recién va a sincronizar en la próxima corrida. NO leer "sin click/sin aprobación"
  como fracaso cuando el cutoff precede al push.
- Compactación 30/06: 15/06 cruzó el umbral >14 días → movido a daily_summary (engagement 15/06:
  sent19/click2/visits4/appr0; send_log 15/06: sent19). Ventana viva ahora **16–30/06**. 16/06 = exacto 14 días → se mantiene.

## Conclusiones de los pushN enviados (por feedback real)

- **23/06** — 3/3 CLICKS. A(curio); **B(🌍 mundo, 1er test diurno)→click+😍love+95s/100% = GANÓ**; C(curio).
- **24/06** — 1/3. A(curio) sin click; **B(🧩 memoria, test limpio)→0 = FALLÓ**; C(curio) click.
- **25/06** — 2/3. A(curio Mandarina)→CLICK; **B(🌍 mundo)→CLICK+😍love** (re-validó); C sin click.
- **26/06** — A(curio Liquidámbar) sin click; **B(🌿 Duelo, descansó 4d)→CLICK + 6/6** (3ª vez); C tras cutoff.
- **27/06** — 2/3. A(curio Ciruelo F-4)→CLICK; **B(🌍 mundo)→CLICK+😍love+97s/100%**; C tras cutoff.
- **28/06** — A(curio Caqui B-41) sin click; B(🌿 Duelo, solo 1d descanso)→sin juego; **C(curio Mirto B-27)→CLICK 00:33Z** (al día sgte).
- **29/06 (noche del 28)** — **EVENTO CLAVE: Diario + Récords descubiertos directo → ambos 😍love + SUSCRIPCIÓN SÍ + aprobados + 92s/141s.** Ver breakthrough.
- **29/06 ciclo 30 (Feed 08:30 / Pasaporte 13:00 / Lavanda 19:30)** — **DATO PENDIENTE: el cutoff (13:11Z) precede a los 3 envíos** → sin medición todavía. Se evalúa el 01/07 cuando sincronice.

## 🔭 Corrida 30/06 — ciclo 31 (esta corrida)

- **Gestión de proposals:** Diario + Récords ya promovidas (sin acción). **Feed + Pasaporte (pending,
  created 29/06) NO se dropean**: su test window se abrió DESPUÉS del cutoff de datos → confounded, sin
  medición. Se mantienen 1 corrida más; re-evaluar 01/07 (aprobado→promover / ventana limpia sin aprobación→dropear).
- **2 experiencias NUEVAS de cero (proposals pending, created=30/06, test limpio), vía agentes persona:**
  - 🍵 **El Chusmerío del Cantero** (`engage/2026-06-30-chusmerio-jardin.html`) — news-feed TABLOIDE/chimentos:
    cada planta esconde un escándalo/impostura/robo-de-crédito REAL (B-1, B-39, I-2, B-3, B-6, B-32, F-4, F-7,
    B-9, B-34, F-9). Apuesta: compartibilidad viral del chisme + novedad serializada. + pitch. Promotor a (08:30).
  - 🧪 **Los Superpoderes de tu Jardín** (`engage/2026-06-30-superpoderes-jardin.html`) — news-feed UTILIDAD/
    asombro con giro comic: cada planta un poder real (B-12 NASA, B-26 memoria, F-8 pimienta rosa, B-4 té,
    B-42 medicinal, B-37 storax, F-1 golosina, B-24, B-41, B-29, B-44, B-7). Apuesta: contenido accionable =
    el ángulo MÁS monetizable (kits). + pitch. Promotor b (13:00).
- **Cola ciclo 31:** (a) 08:30 🍵 Chusmerío; (b) 13:00 🧪 Superpoderes; (c) 19:30 curio **Lapachillo B-14**
  (prima del lapacho, madera durísima charrúa/guaraní; fresca, seasonless, NO en ninguna de las 2 experiencias).
- **Watch 31:** ¿Chusmerío (viral/chisme) o Superpoderes (utilidad/asombro) convierte mejor amor→suscripción?
  ¿la utilidad accionable retiene como el orgullo (Récords 141s)? Si una NO junta aprobación con ventana de
  datos limpia, se dropea. Además, mañana revisar por fin el dato real de Feed/Pasaporte (ciclo 30).

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (curios): cítricos cargados (mandarina B-24, limonero B-23); caqui B-41 fruta
  may-jul; romero B-26 flor jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37,
  ciruelos F-4/B-38); perennes verdes (mirto B-27, guayabo F-1, lavanda B-19, evónimo B-44).
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Hay 1 upload pending (B-15) → lo procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Curios frescos NO usados** (fun_fact verificado): viraró B-32 (en Chusmerío hoy), difenbaquia I-2 (Chusmerío),
  fresno F-10 (dioico, samaras helicóptero — fresco), pera Williams B-39 (Chusmerío), abelia F-7 (naufragio).
  Plantas MUY usadas: B-1/B-12/B-16/B-23/B-25/B-15/B-36/F-1/F-8/B-29 — descansar.
- **Función paralela:** próximos ángulos NEWS-FEED sin usar: entrevista/Q&A a una planta, efemérides "un día
  como hoy", before/after con fotos del usuario, el "horóscopo botánico". (Usados: editorial=Diario,
  superlativos=Récords, red-social=Feed, viajes=Pasaporte, tabloide=Chusmerío, utilidad/poderes=Superpoderes.)
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
