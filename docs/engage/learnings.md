# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

La cola se escribe A MANO (3 entries pending en queue.json), NO con `tools/gen_queue.py`.
Slots base: 08:30 / 13:00 / 19:30 (-03:00). Primer send_at ≥60 min después de la corrida
(margen de deploy de Vercel para páginas linkeadas). expires_at = mismo día 22:00 -03:00.
Cada notificación a un destino DISTINTO. **3 pushes curados ganan a 20 — CONFIRMADO.**
El usuario abre 2-3/día sin importar cuántos mandes; más pushes solo diluye y sepulta lo nuevo.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 24/06: sigue active.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- Abrir una notificación cuenta como `notification_clicked` vía /api/feedback.

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **Curiosidades verificadas (#curiosidades) = contenido #1 y el MÁS resiliente.** Abre casi
  siempre, por click directo. Confirmado 12-13/06 (😍 + 104s), 17-22/06, **23/06 (A Hortensia y C
  Aguaribay ambos click directo)**. Sección fija. Caballo ganador. NUNCA falla como sostén.
- **Experiencias scrollytelling/narrativas SOBRE SUS plantas = ganan si son NUEVAS y bien hechas.**
  **🌍 mundo-jardin (creado por el usuario): GANÓ su test diurno limpio 23/06 — click + reacción 😍love
  + 95s dwell scroll 100%.** Es ahora un asset ganador estable para la rotación (rotar con descanso, igual
  que los juegos). NO es proposal (lo creó el usuario), no necesita aprobación formal; ya vive en engage/.
- **Juegos rápidos sobre SUS plantas (duelo/adiviná/quiz/memoria) = enganchan PERO se FATIGAN con uso
  seguido.** Funcionan en ROTACIÓN con descanso ≥2-3 días. Duelo es el más fuerte (6/6 ×2: 15/06 y
  re-test 22/06 con 37s+17s, scroll 100% tras 3 días de descanso → rotación-con-descanso CONFIRMADA).
  **cual-sobra: REMOVIDO de la nav + página borrada por pedido del usuario (22/06) — NO re-promover.**
- **🧩 memoria-jardin (memory match, 6 pares, creado por el usuario): SIN test diurno limpio todavía.**
  Es el asset-juego que falta medir. Hoy 24/06 recibe su primer turno diurno (slot 13:00).
- **Postales / curiosidad-ESTACIONAL como experiencia separada = LÍNEA CERRADA (22/06).** v1 (20/06) amó
  (click+3 reacc+60s) pero NO aprobó; v2 (21/06) rebotó 5s/10%/0 reacc. El amor de v1 era NOVEDAD, no
  formato. El contenido-curiosidad ya vive y convierte en la sección fija #curiosidades — ahí va, no aparte.
- **Rueda del año:** aprobada (87s) y promovida (nav), pero sobre-expuesta → FUERA del push desde 17/06.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards: sol-jardin ✗×3,
  ano-jardin ✗); (b) formatos LENTOS (mazo flip-card ✗×3). El usuario quiere **deleite + juego**, NO herramientas.

## ✅ APRENDIZAJE CLAVE — el cuello de botella era VOLUMEN, no el formato (18/06, confirmado)

- Proposals previas (mazo ×2, V/F) fracasaron SEPULTADAS entre 13-39 pushes — nunca tuvieron test limpio.
- Una proposal/asset nuevo merece un día de bajo volumen y un slot diurno propio (13:00). No lanzar varias
  variantes-juego seguidas que canibalizan los mismos 2-3 opens.

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **12/06** — curiosidades @14:30 → GANADOR ("MUY buena" + 😍). Origen de la sección fija.
- **15/06** — ~20/día → juego profundo (duelo 6/6 ×2). Pico de engagement, pero sepultó proposals.
- **16-17/06** — 13-20 pushes → dilución pura; el único click directo fue curiosidades.
- **18/06** — **3 pushes. GANADOR.** A(curio)→click; B(cual-sobra 13:00)→click+juego+APROBADA; C tarde.
- **19/06** — 3 pushes. Curiosidades RE-confirmada (A→click directo); juegos empezando a fatigar (B/C bounce).
- **20/06** — **3 pushes. 3/3 CLICKS.** A(curio)→click; B(Postales v1)→click+3 reacc+60s SIN aprobar; C(curio)→click.
- **21/06** — **3 pushes. 3/3 CLICKS pero proposal MUERTA.** Postales v2 abrió pero rebotó 5s/10% → cierra postales.
- **22/06** — **3 pushes.** A(curio Palta)→CLICK; B(Duelo descansado 3 días)→**6/6 + replay, 37s+17s, 100%**; C(curio
  Gardenia)→sin click. A medianoche el usuario se auto-mandó 2 sorpresas (🌍 mundo + 🧩 memoria) → MUY activo, busca JUEGOS.
- **23/06** — **3 pushes. 3/3 CLICKS.** A(curio Hortensia B-13)→click directo; **B(🌍 mundo-jardin, 1er test diurno)→
  click + 😍love + 95s dwell scroll 100% = GANÓ su test, asset validado**; C(curio Aguaribay B-7)→click directo (23:16).
  Lectura: el experimento del 23 cerró bien — mundo-jardin es ahora rotación estable; falta solo medir memoria-jardin.

## Decisiones de hoy (24/06)

- **Proposals:** NO hay pendientes vivas (las 12 del registro están dropped/promoted/removed). Nada que gestionar.
- **NO se crea proposal nueva hoy.** No tengo hipótesis genuinamente nueva (postales/mazo/V/F/mapas/calendarios ya
  descartados). El trabajo pendiente es medir el último asset-juego sin test diurno: 🧩 memoria. Próxima proposal
  sólo con mecánica genuinamente nueva.
- **Experimento del día:** dar a 🧩 memoria-jardin (memory match, 6 pares planta↔dato, creado por el usuario) su
  PRIMER test diurno limpio. La sorpresa de medianoche del 22 probablemente no se vio (dormido). Slot 13:00, sin
  competencia. Es el gemelo no medido de mundo-jardin (que ayer ganó). mundo NO se re-pushea hoy → descanso.
- **Estructura:** 2 curiosidades (sostén fiable, plantas frescas sin solape reciente) + 1 experiencia (memoria).
- **Cola de 3:** (a) 08:30 curio Buganvilia B-1 (Jeanne Baret, 1ª mujer en circunnavegar, disfrazada de hombre) →
  #curiosidades; (b) 13:00 🧩 memoria-jardin; (c) 19:30 curio Hibisco B-4 (flor en el pelo izq/der = soltera/casada;
  flor nacional de Malasia/Corea/Hawái) → #curiosidades. Curios sin solape con palta/gardenia/limonero/lavanda/
  hortensia/aguaribay (ya usadas días recientes).
- Sin compactación: evento más viejo en engagement.json = 12/06 (12 días) < 14; send_log más viejo = 11/06 (13 días) < 14.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. Tareas casi todas `done`; las `active` son IDs scheduleadas para
  floración/ID de primavera. **NO inventar urgencia de invierno.**
- Señales REALES de invierno verificadas (sirven para curios): cítricos cargados (mandarina B-24 FRUIT jun-ago;
  limonero B-23 fruta casi todo el año); romero B-26 FLOR jun-oct; caducos pelados (durazno B-30/35, crespón B-9,
  liquidámbar B-37 silueta tras color otoñal).
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno B-30/35, ciruelos F-4/B-38,
  caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept post-helada**: buganvilia B-1, lantana B-29, cítricos, paltas.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Hay 1 upload pending (B-15) → lo procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- ✅ RESUELTO 23/06: 🌍 mundo-jardin pasó su test diurno (click + love + 95s/100%) → asset ganador estable.
- **Medir el test diurno de 🧩 memoria-jardin (24/06):** si junta click + dwell/reacción → 2º asset-juego estable
  para rotar (con mundo + duelo). Si rebota → priorizar duelo + curiosidades + mundo, y archivar memoria.
- **Proposals:** próxima sólo con hipótesis GENUINAMENTE nueva (no variante de algo medido). Postales, mazo, V/F,
  mapas y calendarios ya están descartados. Pensar mecánicas nuevas de deleite, no más de lo mismo.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
