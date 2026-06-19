# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

La cola se escribe A MANO (3 entries pending en queue.json), NO con `tools/gen_queue.py`.
Slots base: 08:30 / 13:00 / 19:30 (-03:00). Primer send_at ≥60 min después de la corrida
(margen de deploy de Vercel para páginas linkeadas). expires_at = mismo día 22:00 -03:00.

**3 pushes curados ganan a 20 — ahora CONFIRMADO por datos, no solo por instrucción.**
El volumen alto (13-39 pushes, 14-17/06) fue contraproducente: el usuario abre 2-3/día sin
importar cuántos mandes, así que más pushes solo diluye y sepulta lo nuevo. El 18/06 (1er día
de cadencia 3) la señal fue limpia y FUERTE (ver abajo).

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06).
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- Abrir una notificación cuenta como `notification_clicked` vía /api/feedback (sin PAT).

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **Curiosidades verificadas (#curiosidades) = contenido #1 y el MÁS resiliente.** Loved ×varias
  + 104s dwell (12-13/06); único click directo del 17/06 (de 13 pushes); y el 18/06 su push (08:30)
  juntó click directo. Sección fija promovida. Caballo ganador, abre casi siempre.
- **Juegos rápidos sobre SUS plantas (duelo / adiviná / cual-sobra / quiz) = enganchan.** Duelo
  6/6 ×2 (42+24s, 15/06). adiviná: mejor récord de APERTURA-por-push (clicks 15/06 x06, 16/06 x10).
  cual-sobra: click+juego+aprobación en su 1er turno limpio (18/06). Se enfrían con sobre-exposición.
- **Rueda del año:** aprobada 13/06 (87s) y promovida (nav), pero sobre-expuesta → fatiga. FUERA
  del push desde 17/06. Feature sigue en nav, no se empuja. NO re-meter en la cola.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards: sol-jardin
  ✗×3, ano-jardin ✗); (b) formatos LENTOS (mazo flip-card ✗×3, nunca test limpio). El usuario quiere
  **deleite + juego**, NO herramientas.

## ✅ APRENDIZAJE CLAVE CONFIRMADO (18/06) — el cuello de botella era VOLUMEN, no el formato

- Las 3 proposals previas (mazo ×2, V/F) fracasaron SEPULTADAS entre 13-39 pushes — nunca
  tuvieron un test limpio del formato.
- El 18/06, 1er día de cadencia baja (3 pushes), la proposal **"¿Cuál es la intrusa?" (cual-sobra)**
  con slot diurno dedicado (13:00) sin competencia juntó **click + juego (r1✓ r2✓ r3✗ r5✗) +
  proposal_approved + 29s dwell 100%** en su PRIMER turno. Hipótesis del volumen → CONFIRMADA.
- Lección operativa: una proposal nueva merece un día de bajo volumen y un slot diurno propio.
  No lanzar varias variantes-juego seguidas que canibalizan los mismos 2-3 opens.

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **12/06** — curiosidades @14:30 → GANADOR ("MUY buena" + 😍). Origen de la sección fija.
- **13/06** — usuario ACTIVO: aprobó la rueda (87s), rechazó vistas utilitarias (ano/sol-jardin).
- **14/06** — 39 pushes → "0 eventos" por flood + bug de medición. Inservible.
- **15/06** — ~20/día → juego profundo (duelo 6/6 ×2). Pico de engagement, pero por volumen sepultó proposals.
- **16/06** — 20 pushes → pushes propios NO juntaron clicks; V/F=0; rueda otro "no". Dilución pura.
- **17/06** — 13 pushes → engagement LIVIANO: 1 solo click directo y fue curiosidades (x13).
- **18/06** — **3 pushes (cadencia nueva). GANADOR.** A(curio 08:30)→click directo; B(cual-sobra 13:00)
  →click+juego+APROBADA+29s; C(adiviná) se mandó TARDE (20:20, fuera de un slot útil) y se perdió.
  → Lección C: respetar el slot de 19:30 y que el dispatcher no lo atrase tanto; igual el día fue un éxito.

## Decisiones de hoy (19/06)

- **Promovida cual-sobra** (aprobada ayer): página permanente (CTA aprobar/rechazar reemplazado por
  link a inicio + nota; reacciones siguen logueando) + link fijo «🎯 ¿Cuál sobra?» en la todo-strip
  del inicio (build.py), mismo patrón que la rueda.
- **NO se crea proposal nueva hoy** (decisión deliberada). Razón: (1) acabo de promover un juego y
  conviene medirlo como feature fija antes de sumar otra cosa; (2) el learning explícito es no lanzar
  más variantes-juego que canibalizan los 2-3 opens diarios; (3) ya hay 4 experiencias-juego cubriendo
  la categoría ganadora (cual-sobra, duelo, adiviná, quiz) + rueda + curiosidades. Mejor invertir los
  3 slots en contenido probado y dejar respirar.
- **Cola de 3:** (a) 08:30 curiosidades #curiosidades (aguaribay nativo+aromático, proven, abre casi
  siempre); (b) 13:00 cual-sobra YA fija (celebra la aprobación + invita a otra ronda); (c) 19:30
  adiviná en su slot nocturno PROPIO (ayer se perdió por mandarse tarde; mejor récord apertura-por-push).
- Sin compactación: ningún evento supera 14 días (corte 05/06; todo es 12/06+).

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. Tareas casi todas `done`; las `active` son IDs
  scheduleadas para floración/ID de primavera. **NO inventar urgencia de invierno.**
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno B-30/35,
  ciruelos F-4/B-38, caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept post-helada**:
  buganvilia B-1, lantana B-29, cítricos, paltas. NO inventar.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Tareas/uploads del usuario → los procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Medir cual-sobra como feature fija** (ya no proposal): ¿se sigue jugando ahora que está en la nav?
  Si mantiene tracción → confirma que los juegos rápidos + variedad de mecánica retienen.
- Si en 2-3 días la señal vuelve a aplanarse, considerar UNA proposal nueva NO-juego (ej. antes/después
  con fotos subidas, resumen semanal) en día de bajo volumen + slot diurno dedicado.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
