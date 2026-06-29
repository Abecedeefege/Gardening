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

En cada corrida construyo DOS experiencias news-feed armadas DE CERO (vía agentes con persona
product/UX/sales), cada una con: (1) reacción final "¿te voló la cabeza?" (engageReact), (2) CTA de
**suscripción diaria** (engageAnswer `<slug>-suscripcion-diaria`), (3) un **HTML de pitch** aparte
con 6 modelos de monetización (3 innovadores + 3 ultra-creativos). Contrato de página proposal igual
que siempre (link "← Volver al sitio estable" primero, botones Aprobar/No-me-interesa, `engage.js`,
solo datos verificados de data_plants.py con códigos). Dos de los 3 pushes del día llevan a estas
experiencias; el 3º es el curio ancla.

## 🚀 BREAKTHROUGH 29/06 — la SUSCRIPCIÓN por fin se logró (news-feed = el formato que convierte)

La noche del 28 (eventos 00:33–00:43Z del 29) el usuario, por **navegación DIRECTA** (sin esperar el
push), abrió las 2 experiencias del ciclo 29 y disparó la señal MÁS COMPLETA del canal:
- **📰 Diario de tu Jardín** → 😍love + **answer `diario-suscripcion-diaria`=SÍ** + proposal_approved + 92s/100%.
- **🏆 Récords de tu Jardín** → 😍love + **answer `records-suscripcion-diaria`=SÍ** + proposal_approved + **141s/100%** (dwell récord del canal).

Esto cierra el gap que mataron las postales (amor sí, suscripción nunca). **El formato NEWS-FEED
convierte amor→SUSCRIPCIÓN.** Dos hipótesis validadas: (a) framing editorial (Diario) y (b)
orgullo/estatus+número-grande (Récords). El ángulo orgullo retiene aún más (141s > 92s).
→ **AMBAS PROMOVIDAS 29/06**: páginas permanentes + links fijos «📰 El Diario» y «🏆 Récords» en la
nav del inicio (todo-strip de build.py). Footers: se sacaron los botones aprobar/rechazar (nota de
integración + link al inicio); reacciones/suscripción siguen logueando. Status=promoted en proposals.json.

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **NEWS-FEED de contenido verificado = el formato ganador NUEVO** (validado 29/06, ver arriba). Es la
  evolución del activo #1: la curiosidad servida como feed scrolleable + reacción + CTA de suscripción.
- **Curiosidades verificadas (#curiosidades) = contenido #1 histórico y el MÁS resiliente.** Abre casi
  siempre por click directo. La SECCIÓN fija es el sostén fiable. Sigue siendo el núcleo del slot curio.
- **🌍 mundo-jardin (del usuario): asset GANADOR ×3** (23/25/27, click+😍love+95-97s/100%). Rota día por
  medio. NO es proposal (lo creó el usuario), vive en engage/. Descansó 28-29 → disponible para rotar.
- **🌿 Duelo = juego rápido GANADOR 6/6 ×3** (15/22/26) PERO necesita ≥3-4 días de descanso: el 28/06
  con solo 1 día de reposo NO repitió (0 juego). El juego no está agotado; lo mata el uso seguido.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards: sol-jardin ✗×3,
  ano-jardin ✗); (b) formatos LENTOS (mazo flip-card ✗×3); (c) memory-match (test limpio 24/06 = 0);
  (d) postales/curiosidad-estacional como experiencia SEPARADA (línea cerrada 22/06: el amor de v1 era
  novedad, no formato); (e) cual-sobra: removido por el usuario (22/06), no re-promover; (f) Rueda del año:
  aprobada y promovida (nav) pero sobre-expuesta → FUERA del push desde 17/06.
- El usuario quiere **deleite + contenido-curiosidad/verificado + (ahora) news-feed**, NO herramientas ni mecánicas lentas.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 28/06.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **OJO con el cutoff de datos:** engagement.json se actualiza cuando el usuario interactúa, no a las 22:00.
  El push C (19:30) suele mandarse tarde (~20:30 local) y su click cae DESPUÉS del último update del día →
  el dato vespertino casi siempre llega recién a la corrida del día siguiente. NO leer "C sin click" como
  fracaso si el engagement.json se cortó antes. (Confirmado otra vez: 28-c/mirto se clickeó 00:33Z del 29.)
- Compactación: engagement.json y send_log.json trimados de eventos ≤14/06 → daily_summary (14/06: sent39/40).
  Ventana viva ahora 15–29/06. Nada cruzó el umbral >14 días esta corrida (15/06 = exactamente 14 días) → sin nueva compactación.

## Conclusiones de los pushN enviados (por feedback real)

- **23/06** — 3/3 CLICKS. A(curio); **B(🌍 mundo, 1er test diurno)→click+😍love+95s/100% = GANÓ**; C(curio).
- **24/06** — 1/3. A(curio) sin click; **B(🧩 memoria, test limpio)→0 = FALLÓ**; C(curio) click.
- **25/06** — 2/3. A(curio Mandarina)→CLICK; **B(🌍 mundo)→CLICK+😍love** (re-validó); C sin click.
- **26/06** — A(curio Liquidámbar) sin click; **B(🌿 Duelo, descansó 4d)→CLICK + 6/6** (3ª vez); C tras cutoff.
- **27/06** — 2/3. A(curio Ciruelo F-4, matinal, hook fuerte)→CLICK; **B(🌍 mundo)→CLICK+😍love+97s/100%**; C tras cutoff.
- **28/06** — A(curio Caqui B-41) sin click; B(🌿 Duelo, solo 1d descanso)→sin click/juego (poco reposo); **C(curio Mirto B-27)→CLICK 00:33Z** (llegó al día sgte). Día matinal/mediodía flojo → bien timing para inyectar novedad.
- **29/06 (noche del 28)** — **EVENTO CLAVE: Diario + Récords descubiertos directo → ambos 😍love + SUSCRIPCIÓN SÍ + aprobados + 92s/141s.** Ver breakthrough arriba.

## 🔭 Corrida 29/06 — ciclo 30 (esta corrida)

- **Gestión de proposals:** Diario + Récords (aprobadas+suscriptas) → PROMOVIDAS (nav + integración). Sus push
  promotores 29-a/29-b se retiran. Sin pending viejas que dropear.
- **2 experiencias NUEVAS de cero (proposals pending, created=29/06, test limpio):**
  - 📱 **El Feed de tu Jardín** (`engage/2026-06-29-feed-jardin.html`) — "JardínGram": cada planta es una
    cuenta de red social que postea su dato real en 1ª persona (avatar/handle/seguidores/likes de atributos
    reales). 10 posteos (B-22, B-1, F-1, B-12, B-5, B-16, B-27, B-36, B-30, B-13). Apuesta: voz + viralidad
    del gesto "seguir". + pitch. Promotor 2026-06-29-feed (08:30).
  - 🗺️ **Pasaporte Botánico** (`engage/2026-06-29-pasaporte-jardin.html`) — despachos de viaje: origen real
    de cada planta + nombres indígenas charrúa/guaraní. Orgullo nativo (F-1, B-16, F-8, pindó, B-29) +
    asombro exótico (B-22, B-23, B-25, F-4, B-15). + pitch. Promotor 2026-06-29-pasaporte (13:00).
- **Cola ciclo 30:** (a) 08:30 📱 Feed; (b) 13:00 🗺️ Pasaporte; (c) 19:30 curio **Lavanda B-19** (etimología
  'lavare'=lavar + espanta polillas; fresca, seasonless, NO aparece en las 2 experiencias ni en Récords).
- **Watch 30:** ¿las 2 nuevas igualan la conversión amor→suscripción del 29? ¿"Feed" (viral/red social) o
  "Pasaporte" (patrimonio/orgullo) convierte mejor? ¿el orgullo-nativo repite el dwell récord de Récords?
  Si una NO junta aprobación mañana, se dropea por la regla de no-supervivencia.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (curios): cítricos cargados (mandarina B-24/B-25, limonero B-23); caqui B-41
  FRUIT may-jul; romero B-26 FLOR jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37,
  ciruelos F-4/B-38); perennes verdes (mirto B-27, guayabo F-1, lavanda B-19).
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Hay 1 upload pending (B-15) → lo procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Curios frescos NO usados recientemente** (fun_fact verificado): viraró B-32 (sépalos-helicóptero — mejor
  en otoño/verano), lapachillo B-14, difenbaquia I-2 ('caña muda', oxalato). OJO ya usadas/en experiencias:
  clivia B-13 (Feed), cinta B-12 (Récords/Feed), anacahuita B-16 (Récords/Feed/Pasaporte), hiedra B-15
  (Récords/Pasaporte), ciruelo F-4 (27/Pasaporte), lavanda (29-c).
- **Función paralela:** seguir inventando ángulos NEWS-FEED distintos (hechos: editorial=Diario,
  superlativos=Récords, red-social=Feed, viajes/origen=Pasaporte). Próximos: efemérides "un día como hoy",
  entrevista/Q&A a una planta, "el chusmerío del cantero", before/after con sus fotos subidas.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
