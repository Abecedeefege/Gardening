# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

La cola se escribe A MANO (3 entries pending en queue.json), NO con `tools/gen_queue.py`.
Slots base: 08:30 / 13:00 / 19:30 (-03:00). Primer send_at ≥60 min después de la corrida
(margen de deploy de Vercel para páginas linkeadas). expires_at = mismo día 22:00 -03:00.
Cada notificación a un destino DISTINTO (salvo variación de una feature aprobada como #curiosidades).

**3 pushes curados ganan a 20 — CONFIRMADO por datos.** El usuario abre 2-3/día sin importar
cuántos mandes; más pushes solo diluye y sepulta lo nuevo. Con cadencia 3 la señal es limpia y fuerte.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 21/06: sigue active.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- Abrir una notificación cuenta como `notification_clicked` vía /api/feedback (sin PAT).

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **Curiosidades verificadas (#curiosidades) = contenido #1 y el MÁS resiliente.** Abre casi siempre,
  por click directo. Confirmado 12-13/06 (😍 + 104s), 17/06 (único click de 13 pushes), 18/06, 19/06
  (click directo <2min), **20/06 (A y C ambos click directo a #curiosidades).** Sección fija. Caballo ganador.
- **Postales de invierno (curiosidad-ESTACIONAL, NO-juego) = formato nuevo VALIDADO.** 20/06 su push
  juntó la señal implícita más fuerte de cualquier no-juego: click + 3 reacciones (wow + 2 love) + 60s
  dwell 100%. PERO no convirtió el botón Aprobar → la regla lo dropeó. El gap es de CONVERSIÓN, no de
  formato. Re-lanzado 21/06 (v2, contenido fresco + CTA más claro) para cerrar ese gap.
- **Juegos rápidos sobre SUS plantas (duelo/adiviná/cual-sobra/quiz) = enganchan PERO FATIGADOS.**
  Pico 15/06 (duelo 6/6 ×2). Fatiga clara 19/06 (cual-sobra 0 opens, adiviná bounce 2s). 4 experiencias-juego
  ya cubren la categoría. **EN DESCANSO desde 20/06** — 0 juegos en la cola a propósito. Re-introducir UNO
  recién tras ≥2-3 días sin pushearlos para que vuelva a sentirse fresco. NO apilar más variantes-juego.
- **Rueda del año:** aprobada (87s) y promovida (nav), pero sobre-expuesta → FUERA del push desde 17/06.
  Feature sigue en nav, no se empuja. NO re-meter en la cola.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards: sol-jardin ✗×3,
  ano-jardin ✗); (b) formatos LENTOS (mazo flip-card ✗×3). El usuario quiere **deleite + juego**, NO herramientas.

## ✅ APRENDIZAJE CLAVE — el cuello de botella era VOLUMEN, no el formato (18/06, re-confirmado)

- Proposals previas (mazo ×2, V/F) fracasaron SEPULTADAS entre 13-39 pushes — nunca tuvieron test limpio.
- 18/06 (1er día cadencia baja) cual-sobra con slot diurno dedicado juntó click+juego+aprobación en su 1er turno.
- Lección operativa: una proposal nueva merece un día de bajo volumen y un slot diurno propio (13:00).
  No lanzar varias variantes-juego seguidas que canibalizan los mismos 2-3 opens.

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **12/06** — curiosidades @14:30 → GANADOR ("MUY buena" + 😍). Origen de la sección fija.
- **13/06** — usuario ACTIVO: aprobó la rueda (87s), rechazó vistas utilitarias (ano/sol-jardin).
- **14/06** — 39 pushes → "0 eventos" por flood + bug de medición. Inservible.
- **15/06** — ~20/día → juego profundo (duelo 6/6 ×2). Pico de engagement, pero por volumen sepultó proposals.
- **16/06** — 20 pushes → pushes propios NO juntaron clicks; V/F=0; rueda otro "no". Dilución pura.
- **17/06** — 13 pushes → engagement LIVIANO: 1 solo click directo y fue curiosidades (x13).
- **18/06** — **3 pushes. GANADOR.** A(curio)→click; B(cual-sobra 13:00)→click+juego+APROBADA+29s; C llegó tarde, perdido.
- **19/06** — 3 pushes. Curiosidades RE-confirmada (A aguaribay→click directo <2min); juegos fatigando (B/C 0/bounce).
- **20/06** — **3 pushes. MEJOR DÍA: 3/3 CLICKS.** A(curio Buganvilia 08:30)→click directo a #curiosidades en 1min.
  B(Postales invierno v1, 13:00, dispatcher lo mandó 14:25)→click + 3 reacciones (wow+2love) + 60s dwell 100%,
  pero SIN tap Aprobar. C(curio Hibisco 19:30, mandado 19:49)→click directo a #curiosidades. Lectura: la
  cadencia 3 + estructura "2 curio + 1 proposal-curio-estacional" funciona redondo. Postales: formato amado,
  falta cerrar la conversión a aprobación. Juegos NO se pushearon (descanso) y no se los extrañó.

## Decisiones de hoy (21/06)

- **Proposal v1 (postales-invierno) DROPEADA** por regla (pending sin proposal_approved), pese a la señal
  implícita fortísima. Página efímera eliminada. El aprendizaje se conserva: el formato funciona.
- **Proposal NUEVA: «❄️ Postales de invierno II»** (`2026-06-21-postales-invierno-2`). Mismo formato ganador,
  contenido FRESCO y verificado (mandarina B-24 cargada de fruta en invierno [FRUIT 4-8]; romero B-26 floreciendo
  en pleno frío [FLWR 6-10]; liquidámbar B-37 vuelto silueta + storax). CTA de aprobación más claro y explícito
  ("tocá ✅ y queda fija rotando con la estación; sin aprobación, mañana desaparece"). Hipótesis: cerrar el gap
  reacción→aprobación que dejó v1. Slot diurno dedicado 13:00, día sin juegos.
- **Estrategia del día: repetir la fórmula que dio 3/3 el 20/06** — 2 curiosidades + 1 proposal-curio-estacional.
- **Cola de 3:** (a) 08:30 curio Limonero B-23 (no existe silvestre, híbrido India 2500 años) → #curiosidades;
  (b) 13:00 proposal Postales II (slot diurno propio); (c) 19:30 curio Lavanda B-10 (nombre romano = lavare,
  espanta polillas), ángulo nocturno liviano y relajante → #curiosidades. Plantas de los curios distintas de
  las de la proposal (sin solapamiento). Juegos en descanso (día 2).
- Sin compactación: ningún evento supera 14 días (corte 07/06; todo es 12/06+). send_log y queue limpios.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. Tareas casi todas `done`; las `active` son IDs scheduleadas para
  floración/ID de primavera. **NO inventar urgencia de invierno.**
- Señales REALES de invierno verificadas en data_plants.py (sirven para postales/curios):
  cítricos cargados (mandarina B-24 FRUIT jun-ago; limonero B-23 fruta casi todo el año); romero B-26 FLOR jun-oct;
  caducos pelados (durazno B-30/35, crespón B-9, liquidámbar B-37 — silueta tras color otoñal).
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno B-30/35, ciruelos F-4/B-38,
  caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept post-helada**: buganvilia B-1, lantana B-29, cítricos, paltas.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Tareas/uploads del usuario → los procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Medir «Postales de invierno II» (21/06):** ¿el CTA más claro convierte la reacción en aprobación explícita?
  Si APRUEBA → promover como sección fija 'Postales' rotativa por estación (integrar en build.py). Si vuelve a
  reaccionar sin aprobar → el gap es estructural (quizá el botón no se ve / no se entiende qué hace) y conviene
  evaluar promover por señal implícita fuerte. Si la ignora → el amor de v1 era novedad, no formato.
- **Juegos en descanso desde 20/06.** Re-introducir UN juego recién tras ≥2-3 días sin pushearlos. cual-sobra sigue
  fija en la nav; si nadie la juega orgánicamente, no forzarla con push.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
