# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json), NO con `tools/gen_queue.py`.
Slots base: 08:30 / 13:00 / 19:30 (-03:00). Primer send_at ≥60 min después de la corrida
(margen de deploy de Vercel para páginas linkeadas). expires_at = mismo día 22:00 -03:00.
Cada notificación a un destino DISTINTO. **3 pushes curados ganan a 20 — CONFIRMADO.**
El usuario abre 2-3/día sin importar cuántos mandes; más pushes solo diluye y sepulta lo nuevo.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 28/06: sigue active.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- Abrir una notificación cuenta como `notification_clicked` vía /api/feedback.
- Compactación al día (28/06): engagement.json y send_log.json trimados de eventos ≤14/06
  → daily_summary (14/06: sent39/40). Ventana viva 15–27/06.
- **OJO con el cutoff de datos:** engagement.json se actualiza cuando el usuario interactúa, no a las 22:00.
  El push C (19:30) suele mandarse tarde (~20:30 local) y su click cae DESPUÉS del último update del día →
  el dato del slot vespertino casi siempre llega recién a la corrida del día siguiente. No leer "C sin click"
  como fracaso si el engagement.json se cortó antes de que C se enviara.

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **Curiosidades verificadas (#curiosidades) = contenido #1 y el MÁS resiliente.** Abre casi
  siempre por click directo. Confirmado 12-13/06, 17-23/06, 25-27/06. **PERO no es infalible carta
  por carta:** el hit por-notificación depende del gancho y del slot (matinal variable). La SECCIÓN
  es el caballo ganador y el sostén fiable. Sigue siendo el núcleo.
- **🌍 mundo-jardin (creado por el usuario): asset GANADOR — VALIDADO ×3.** Ganó test diurno limpio
  23/06 (click+😍love+95s scroll 100%), RE-confirmó 25/06 (click+😍love) y 27/06 (click+😍love+97s
  scroll 100%). El asset-experiencia más fiable que tenemos. Patrón de rotación: día por medio
  (23/25/27). Pushado 27 → DESCANSA hoy 28. NO es proposal (lo creó el usuario), ya vive en engage/.
- **🌿 Duelo = juego rápido GANADOR, 6/6 ×3** (15/06, 22/06, 26/06, todos pleno). Es el juego más
  fuerte. Se FATIGA con uso seguido → rota día por medio igual que mundo (22/26/28). Pushado 26,
  descansó 27 → HOY 28 vuelve. Los juegos rápidos NO están agotados como categoría: lo que mata al
  juego es el uso seguido, no el formato.
- **cual-sobra: REMOVIDO de la nav + página borrada por pedido del usuario (22/06) — NO re-promover.**
- **🧩 memoria-jardin (memory match, del usuario): FALLÓ test diurno limpio (24/06) — 0 engagement.**
  Bencheada de la rotación de push (archivo conservado por ser creación del usuario). El formato
  memory-match NO engancha a este usuario.
- **Postales / curiosidad-ESTACIONAL como experiencia separada = LÍNEA CERRADA (22/06).** v1 (20/06)
  amó (click+3 reacc+60s) pero NO aprobó; v2 (21/06) rebotó 5s/10%. El amor de v1 era NOVEDAD, no
  formato. El contenido-curiosidad ya vive y convierte en la sección fija #curiosidades — ahí va, no aparte.
- **Rueda del año:** aprobada (87s) y promovida (nav), pero sobre-expuesta → FUERA del push desde 17/06.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards: sol-jardin ✗×3,
  ano-jardin ✗); (b) formatos LENTOS (mazo flip-card ✗×3); (c) memory-match (test limpio).
  El usuario quiere **deleite + contenido-curiosidad + juego rápido**, NO herramientas ni mecánicas lentas.

## ✅ APRENDIZAJE CLAVE — el cuello de botella era VOLUMEN (18/06) + el formato (24/06)

- Proposals previas (mazo ×2, V/F) fracasaron SEPULTADAS entre 13-39 pushes — nunca tuvieron test limpio.
  La cadencia baja (3/día) es la única que da test justo. ESO se resolvió.
- PERO un test limpio también puede dar NEGATIVO real: memoria tuvo el día perfecto (24/06) y aun así 0.
  Cuando hay test limpio y no engancha, es señal de FORMATO, no de volumen.
- **Patrón estable de invierno: 2 curios frescos + 1 ganador-experiencia rotado día por medio
  (mundo ↔ duelo).** Es el core que rinde 2-3 clicks/día sin desgaste. No tocar hasta tener mecánica
  GENUINAMENTE nueva que probar.

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **18/06** — 3 pushes. GANADOR. A(curio)→click; B(cual-sobra)→click+juego+APROBADA; C tarde.
- **20/06** — 3/3 CLICKS. A(curio); B(Postales v1)→click+3 reacc+60s SIN aprobar; C(curio).
- **22/06** — A(curio Palta)→CLICK; B(Duelo, descansó 3d)→**6/6 +replay, 37+17s, 100%**; C(curio) sin click.
- **23/06** — 3/3 CLICKS. A(curio); **B(🌍 mundo, 1er test diurno)→click+😍love+95s 100% = GANÓ**; C(curio).
- **24/06** — 1/3. A(curio matinal) sin click; **B(🧩 memoria, test limpio)→0 = FALLÓ**; C(curio) click.
- **25/06** — 2/3. A(curio Mandarina, matinal)→CLICK; **B(🌍 mundo)→CLICK+😍love** (re-validó); C sin click.
- **26/06** — A(curio Liquidámbar) sin click; **B(🌿 Duelo, descansó 4d)→CLICK + 6/6 COMPLETO** (3ª vez 6/6);
  C(curio Crespón) sin dato (se mandó 23:35Z, tras el último update del engagement.json).
- **27/06** — **2/3 confirmados.** A(curio Ciruelo Pissardii F-4, matinal, hook Persia/1880)→**CLICK 12:54Z**
  (el matinal SÍ engancha con hook fuerte — patrón confirmado); **B(🌍 mundo, día por medio)→CLICK+😍love+97s
  scroll 100%** (3ª validación de mundo, sostiene día por medio); C(curio Guayabo F-1) sin dato (se mandó
  23:34Z, después del cutoff). Lectura: core probado intacto; matinal rinde si el gancho es fuerte.
- **28/06** — **0/2 al cierre de datos (cutoff engagement.json 21:03Z), C pendiente.** A(curio Caqui B-41,
  matinal, hook 'fruto de los dioses'/600 años, sent 11:46Z)→SIN click; B(🌿 Duelo, sent 16:36Z, tras SOLO
  1 día de descanso)→SIN click ni juego a las 4.5h. C(curio Mirto B-27) se manda 19:30 local (cae tras el
  cutoff → su dato llega mañana). Lectura preliminar: **día flojo**. Dos hipótesis de la corrida matinal NO
  se confirmaron — (a) matinal con hook fuerte NO siempre engancha (falló hoy, vs 27/06 que sí); (b) **Duelo
  con solo 1 día de descanso NO repitió** (sus 6/6 previos tuvieron ≥3-4 días de descanso → el juego necesita
  MÁS reposo del que se le dio). Posible fatiga acumulada del core probado → **bien timing para inyectar
  novedad** (las 2 experiencias nuevas de cero del ciclo 29).

## Corrida matinal 28/06 (ya hecha, commit 5e44a3b)

- Cola del 28: A(curio Caqui B-41) + B(🌿 Duelo rotado) + C(curio Mirto B-27). Mundo descansó. Resultado: ver
  conclusión 28/06 arriba — día flojo (0 clicks medibles a las 21:03Z, C aún por enviar).

## 🆕 Corrida VESPERTINA 28/06 — nueva función paralela del usuario (ciclo 29)

Pedido nuevo del usuario (28/06): en cada corrida, presentar notificación(es) que lleven a **experiencias NUEVAS
armadas de CERO**, en formato **news-feed**, con 3 objetivos medibles: (1) que la marque como increíble (reacción
final), (2) que se **suscriba a una versión fresca diaria** (engageAnswer de suscripción), (3) un **HTML de pitch**
aparte para monetizarla (3 modelos innovadores + 3 ultra-creativos). "2 en paralelo" → construí DOS experiencias.

- **NO toqué la cola del 28** (A/B ya enviadas, C pendiente esta noche → se respeta; re-enviar quema credibilidad).
  Esta corrida arma el **ciclo 29** con las 2 experiencias nuevas como contenido marquee + 1 curio ancla.
- **2 experiencias nuevas (proposals pending, created=29/06 para tener test limpio):**
  - 📰 **Diario de tu Jardín** (`engage/2026-06-29-diario-jardin.html`) — news-feed editorial: 8 "noticias"
    de lo que SUS plantas hacen hoy en invierno (caqui carga fruta, romero en flor, cítricos cargados, caducos
    pelados resistiendo helada, perennes verdes). Reencuadra el contenido-curiosidad (asset #1) como prensa diaria.
    + pitch HTML. Promotor: 2026-29-a (08:30).
  - 🏆 **Récords de tu Jardín** (`engage/2026-06-29-records-jardin.html`) — news-feed de 8 superlativos suyos
    (hiedra 400 años, cinta NASA, limonero 4× vit C, mirto/Venus, althea flor-de-1-día, Hass de 1 árbol,
    buganvilia/Jeanne Baret, anacahuita protegida por ley). Apuesta: orgullo/estatus + coleccionable/viral.
    + pitch HTML. Promotor: 2026-29-b (13:00).
  - Ambas con: bloque "¿te voló la cabeza?" (engageReact) + CTA de **suscripción diaria** (engageAnswer) +
    botones Aprobar/No-me-interesa + link al pitch. Solo datos verificados de data_plants.py, con códigos.
- **Cola ciclo 29:** (a) 08:30 📰 Diario → experiencia; (b) 13:00 🏆 Récords → experiencia; (c) 19:30 curio
  **Hiedra B-15** (vive +400 años, doble vida juvenil/adulta — fresco, no usado; B-15 además tiene upload pending).
  queue.json = [28-c holdover] + [29-a/b/c]. Es un día de **inyección de novedad** (no el core 2-curios+1-juego),
  justificado por el pedido del usuario + la señal de fatiga del 28.
- **Watch 29:** ¿las experiencias news-feed convierten amor→**suscripción** explícita (el gap que mataron las
  postales)? ¿"Récords" dispara el orgullo-de-MI-jardín? ¿Diario o Récords junta su primer proposal_approved?
- **Proposals previas:** ninguna viva (todas dropped/promoted/removed). Sin eventos approve/reject nuevos desde
  la matinal. Nada que promover/descartar hoy.
- **Compactación:** ya hecha en la matinal (≤14/06 → daily_summary). Sin nueva compactación necesaria.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. Tareas casi todas `done`; las `active` son IDs scheduleadas para
  floración/ID de primavera. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (sirven para curios): cítricos cargados (mandarina B-24 FRUIT abr-ago; limonero
  B-23 fruta casi todo el año); **caqui B-41 FRUIT may-jul** (fruta naranja en árbol pelado); romero B-26 FLOR
  jun-oct; caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37, ciruelos F-4/B-38); perennes que
  siguen verdes (mirto B-27, guayabo F-1, lavanda B-19).
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno B-30/35, ciruelos
  F-4/B-38, caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept post-helada**: buganvilia B-1, lantana
  B-29, cítricos, paltas.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Hay 1 upload pending (B-15) → lo procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Curios frescos disponibles** (no usados recientemente, fun_fact verificado en data_plants.py): clivia B-13
  (vive 100 años, honra duquesa de Northumberland), cinta B-12 (NASA purifica aire), durazno B-30/35 (de China,
  no Persia), anacahuita B-16 (protegida por ley UY 1986), viraró B-32 (sépalos-helicóptero), lapachillo B-14,
  difenbaquia I-2 ('caña muda', oxalato paraliza la garganta). Usados recién: hiedra B-15 (29-c), caqui/mirto
  (28), ciruelo/guayabo (27). OJO: limonero/cinta/anacahuita/hiedra aparecen en la experiencia 🏆 Récords del 29.
- **Proposals:** próxima SOLO con hipótesis GENUINAMENTE nueva (no variante de algo medido). Descartados:
  postales, mazo, V/F, mapas, calendarios, memory-match. Pensar mecánicas nuevas, no más de lo mismo.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
