# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

**18/06 el usuario instruyó explícitamente "la cola del día con sus 3 notificaciones
pending".** Eso reemplaza la cadencia de "1 cada 30 min" del 15/06. La cola se escribe
A MANO (3 entries pending en queue.json), NO con `tools/gen_queue.py`. Slots base:
08:30 / 13:00 / 19:30 (-03:00). Primer send_at ≥60 min después de la corrida (margen
de deploy de Vercel para páginas linkeadas). expires_at = mismo día 22:00 -03:00.

**Por qué 3 y no 20 tiene respaldo en datos, no solo en la instrucción:** el volumen
alto se mostró CONTRAPRODUCENTE. 15/06 (~20 pushes) hubo juego profundo, pero
16/06 y 17/06 (13-20 pushes) el engagement CAYÓ a 2-3 aperturas y los pushes propios
casi no juntaron clicks directos — el usuario abre 2-3/día sin importar cuántos mandes,
así que más pushes solo diluye y sepulta lo nuevo. 3 pushes curados ganan a 20.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06).
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- Abrir una notificación cuenta como `notification_clicked` vía /api/feedback (sin PAT).

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **Curiosidades verificadas (#curiosidades) = contenido #1 y el MÁS resiliente.** 12-13/06
  todas 😍 + 104s dwell. Y el 17/06, de 13 pushes, el ÚNICO click directo fue el de
  curiosidades (x13, 21:48). Sección fija promovida. Sigue siendo el caballo ganador.
- **Juegos rápidos sobre SUS plantas (duelo / adiviná / quiz) = enganchan.** 15/06 fue el
  pico: duelo completo 2× 6/6 (42+24s), adiviná 32s. PERO se enfrían con sobre-exposición:
  16/06 más liviano, 17/06 muy liviano (visita directa a duelo + r1, después rebotes de 2s).
  adiviná tiene el mejor récord de APERTURA-por-push (clicks 15/06 x06 y 16/06 x10).
- **Rueda del año:** aprobada 13/06 (87s) y promovida (nav), pero sobre-expuesta → fatiga
  (meh/meh/no). FUERA del push desde 17/06. Feature sigue en nav, no se empuja. NO re-meter.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards:
  sol-jardin ✗×3, ano-jardin ✗); (b) formatos LENTOS (mazo flip-card, ✗×3, nunca test limpio).
  El usuario quiere **deleite + juego**, NO herramientas.

## ⚠️ APRENDIZAJE CLAVE (16-17/06) — el cuello de botella era VOLUMEN, no formatos

- 16/06: 20 pushes, NINGUNO de los 20 propios juntó click directo; el engagement vino de un
  push viejo + visitas directas. La proposal ⚡V/F (4 promotores) tuvo CERO engagement: nunca
  se abrió, sepultada. Mismo modo de falla que el mazo. NO fue el formato — fue dilución.
- **Por eso 3 proposals seguidas (mazo ×2, V/F) fallaron: NUNCA tuvieron un test limpio.**
  Siempre quedaron enterradas entre 18-39 pushes. La lección no es "no crear proposals",
  es "darles un test limpio en día de bajo volumen / slot que se abre".

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **11/06** — 1 push poda @20:00: inconcluyente (deshora, 1ª noche).
- **12/06** — curiosidades @14:30 → GANADOR ("MUY buena" + 😍). Origen de la sección.
- **13/06** — cadencia rotada → usuario ACTIVO: aprobó la rueda, rechazó vistas utilitarias.
- **14/06** — 39 pushes a fichas #especie → "0 eventos" por BUG de medición (PAT). Inservible.
- **15/06** — ~20/día rotados → juego profundo (duelo 6/6 ×2). Pico de engagement.
- **16/06** — 20 pushes → pushes propios NO juntaron clicks; V/F=0; rueda otro "no". Dilución.
- **17/06** — 13 pushes (quiz/duelo/adivina ×4 + curio). Engagement LIVIANO: 1 solo click
  directo y fue curiosidades (x13); juegos con visita directa + rebotes de 2s. Confirma:
  más volumen ≠ más engagement, y curiosidades es lo más robusto.

## Decisiones de hoy (18/06)

- **Cola de 3** (instrucción explícita del usuario): (a) 08:30 curiosidades #curiosidades
  (proven, único click de ayer); (b) 13:00 teaser de la proposal nueva; (c) 19:30 adiviná
  (mejor récord de apertura-por-push). 3 ángulos distintos, todos anclados en algo real.
- **Proposal NUEVA: "¿Cuál es la intrusa?" (2026-06-18-cual-sobra)** — odd-one-out: 4 plantas,
  3 comparten un rasgo VERIFICADO (fruta/nativa/aromática/trepadora), cazar la intrusa.
  Mecánica genuinamente nueva (no quiz/duelo/adivina). Reusa solo booleanos verificados (cero
  invención). **Se lanza HOY porque es la 1ª ventana de bajo volumen (3 pushes) = test LIMPIO**
  que las proposals anteriores nunca tuvieron, con slot diurno dedicado (13:00) sin competencia.
- **FIX:** la corrida del 17/06 dejó `2026-06-16-vof-jardin` con status "pending" (archivo y
  entrada de gen_queue ya removidos); status corregido a "dropped" hoy.
- Sin compactación: ningún evento supera 14 días (todo es de 06-12 en adelante).

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. Tareas casi todas `done`; las `active` son IDs
  scheduleadas para floración/ID de primavera. **NO inventar urgencia de invierno.**
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno
  B-30/35, ciruelos F-4/B-38, caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept
  post-helada**: buganvilia B-1, lantana B-29, cítricos, paltas. NO inventar.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Tareas/uploads del usuario → los procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Medir el test limpio de "¿Cuál sobra?"** mañana: ¿con 3 pushes y slot dedicado SÍ junta
  click/aprobación? Si sí → confirma que el problema siempre fue volumen, e integrar como
  juego fijo. Si no → el formato odd-one-out no engancha aun con atención limpia.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
