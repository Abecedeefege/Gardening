# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: cada 30 min (~20/día) — fijada por el usuario el 15/06

**Cadencia = 1 push cada 30 min, ventana 10:30–20:00 (~20 slots).** Generá con
`python tools/gen_queue.py <YYYY-MM-DD>` (rota la biblioteca de formatos, sin
formato adyacente repetido, assert URLs únicas, CERO fichas `#especie`).

**NO bajar la cadencia por "fatiga".** La "fatiga del 14/06" fue un BUG DE MEDICIÓN
(las fichas logueaban por PAT, que en la PWA no existe → 0 eventos falsos). El usuario
confirmó (15/06): "hubo engagement, claramente no lo mediste bien". Ya está parchado:
hoy el abrir cualquier notificación cuenta vía `/api/feedback` (sin PAT).

**Reglas duras:**
- **Cada push explora un FORMATO nuevo.** Los formatos que el usuario marca 👍 pueden
  repetir pero SIEMPRE con contenido fresco (los juegos randomizan, la rueda cambia de
  mes). Lo garantiza `gen_queue.py`. **Construir formatos nuevos = prioridad permanente**
  (más entradas en `build_formats()` → más cerca de "un formato distinto por push").
- **PROHIBIDO el módulo original de especie** (`index.html#especie=CODE`): "las que llevan
  al módulo original de una especie no quiero verlas más". Solo experiencias NUEVAS o
  módulos marcados buenos (rueda, #curiosidades).
- El ABRIR la notificación cuenta como engagement (`notification_clicked`), logueado vía
  `/api/feedback` en TODAS las páginas (engage/* e index.html).
- NUNCA linkear a una página efímera que vayas a borrar el mismo día (404 — pasó el 13/06).
- Formatos vivos en gen_queue: 🧠 quiz, ⚔️ duelo, 🔍 adiviná, ⚡ V/F (proposal 16/06),
  🌀 rueda (aprobada, recortada a 3 slots), 💡 curiosidades (#curiosidades, promovido).

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06).
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.

## 🎯 SEÑAL REAL MEDIDA — los juegos RÁPIDOS son el ganador claro

- **15/06 (1er día de ~20/día):** 19 pushes mandados. Engagement real en 2 sesiones:
  - **⚔️ Duelo = ganador top:** jugado COMPLETO 2 veces seguidas, 6/6 ambas, dwell 42+24s.
  - **🔍 Adiviná = engancha:** jugado (1✓/4✗), dwell 32s.
  - **🌀 Rueda = sobre-expuesta → meh/meh/no.** Apareció 6/19 veces; el usuario la calificó
    meh, meh, no. NO es que el formato sea malo (aprobada 13/06 con 87s dwell): es FATIGA por
    repetición. → recortada a 3 slots/día en gen_queue (16/06).
- **12-13/06 (sigue válido):** Curiosidades verificadas = contenido #1 (todas 😍 + 104s dwell);
  Rueda = formato animado #2 (aprobada, 87s). Perdedores: mapas/calendarios utilitarios (sol-jardin
  rechazada ×3, ano-jardin rechazada). El usuario quiere **deleite + juego**, NO herramientas.

**Lectura inequívoca:** juegos rápidos sobre SUS plantas (duelo/adiviná/quiz) + datos verificados.
Lo que NO funciona: (a) herramientas utilitarias (mapas, listas, dashboards); (b) formatos LENTOS
(el mazo flip-card fracasó 3 veces); (c) sobre-exponer un mismo formato (rueda ×6 → fatiga).

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **11/06** — 1 push poda @20:00: inconcluyente (deshora, 1ª noche).
- **12/06** — curiosidades @14:30 → GANADOR ("MUY buena" en chat + 😍). Origen de la sección.
  Noche: barrida de 8 pushes a la MISMA página → sobre-saturación. De acá: "1 destino por push".
- **13/06** — cadencia 15min rotada → usuario ACTIVO: aprobó la rueda, rechazó vistas utilitarias,
  😍 a curiosidades. La rotación importa.
- **14/06** — 39 pushes casi todos a fichas `#especie` → "0 eventos", pero fue BUG de medición
  (PAT), no fatiga. Igual: no usar fichas (formato repetido prohibido) ni inflar volumen sin variar.
- **15/06** — ~20/día con formatos rotados (gen_queue) → engagement real y profundo en los JUEGOS
  (duelo 6/6 ×2). Confirma: volumen alto ESTÁ BIEN si cada push es un formato/contenido distinto.
  La rueda repetida 6× cansó. El mazo (proposal) nunca se mandó (la cola fue la serie x, sin él).

## Principios vigentes (no romper)

1. **Una experiencia/contenido DISTINTO por push.** Variar formato; no repetir el mismo >3×/día.
2. **Deleite + JUEGO > herramientas.** Juegos rápidos + curiosidades verificadas. NO mapas/listas/
   dashboards. NO formatos lentos (flip-card).
3. **Verificar la horticultura antes de publicar.** Jamás inventar urgencia ni dato no observable.
   Los juegos derivan de booleanos estructurales verificados (nat/fru/perf/trep/zona), no inventan.
4. **El destino cumple lo que promete el copy.** Hashes correctos (#m=N, #set=N, #curiosidades).
5. **Promotores de proposal → varios slots diurnos.** Primer `send_at` siempre ≥60 min post-corrida.
6. **Proposals sin aprobación explícita de un día anterior se borran hoy.** La aprobación es el
   único pase a permanencia.

## Decisiones de hoy (16/06)

- **CADENCIA → 20/día** vía gen_queue (sin cambio de modelo; el de 3/día del 15/06 quedó superado).
- **RECORTE rueda 6→3** en gen_queue.py: el 15/06 a 6 slots se sobre-expuso (meh/meh/no). Sigue
  rotando (#m=6 actual, #m=11 pico flor, #m=9 despertar) pero sin dominar.
- **DROP mazo (2026-06-15)** — 3er intento fallido, nunca tuvo test limpio (el 15/06 la cola pasó a
  gen_queue, que no lo incluye → su promotor nunca se mandó). Se abandona el flip-card lento.
- **NUEVA proposal: ⚡ Verdadero o Falso (2026-06-16-vof-jardin)** — misma tesis del mazo (datos
  verificados + juego) PERO en formato RÁPIDO binario, que es lo que mide bien. 7 afirmaciones V/F
  derivadas de booleanos verificados. Agregada a gen_queue (4 variantes); promovida en x04/x09/x14/x19.
  Hipótesis: el ritmo rápido del duelo/adiviná + dato verificado engancha; si la aprueban → fija.
- **Cola 16/06:** 20 slots — quiz×4, duelo×4, adiviná×4, V/F×4, rueda×3, curio×1. Sin adyacentes.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en dormancia: poco que hacer. Tareas reales casi todas `done`; las `active` son IDs
  scheduleadas para floración primavera. NO inventar urgencia de invierno.
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno B-30/35,
  ciruelos F-4/B-38, caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept post-helada**:
  buganvilia B-1, lantana B-29, cítricos, paltas. NO inventar.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Tareas/uploads del usuario → los procesa `/actualizar-tareas`, no este agente (hay 1 foto pending).

## TODO pendiente

- **Si ⚡ V/F engancha** → integrarlo como experiencia fija y dejarlo estable en gen_queue.
- Regenerar el dataset `M` de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de hacer cualquier vista de poda.
- Roadmap de formatos nuevos para gen_queue: antes/después con fotos subidas, número del día,
  cuenta-regresiva a floración, memoria/pares (ojo: pares es flip → cuidado, el flip lento fracasó).
