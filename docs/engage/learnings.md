# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: cada 30 min (~13-20/día) — fijada por el usuario el 15/06

**Cadencia = 1 push cada 30 min, ventana 10:30–20:00.** Generá con
`python tools/gen_queue.py <YYYY-MM-DD>`. El generador CAPEA en la cantidad de
instancias ÚNICAS disponibles (un destino distinto por slot, assert anti-duplicados).
Hoy 17/06 dieron 13 slots (no 20) porque saqué vof y rueda de la rotación → quedaron
quiz×4, duelo×4, adivina×4, curio×1. **13 únicos > 20 con repeticiones**: el usuario se
quejó 2 veces de repetidos, así que NO inflar con repeticiones; agregar instancias frescas
o formatos nuevos a `build_formats()` para subir el techo.

**NO bajar la cadencia por "fatiga" sin datos duros.** La "fatiga del 14/06" fue BUG DE
MEDICIÓN (fichas logueaban por PAT inexistente en PWA → 0 eventos falsos). Parchado: hoy
abrir cualquier notificación cuenta vía `/api/feedback` (sin PAT), confiable desde 15/06.

**Reglas duras:**
- **Cada push = un FORMATO/instancia distinto.** Garantizado por gen_queue.
- **PROHIBIDO el módulo original de especie** (`index.html#especie=CODE`): el usuario lo
  vetó. Solo experiencias NUEVAS o módulos marcados buenos (#curiosidades).
- ABRIR la notificación cuenta como engagement (`notification_clicked`), vía `/api/feedback`.
- NUNCA linkear a una página efímera que vayas a borrar el mismo día (404 — pasó el 13/06).
  Si dropeás una proposal que estaba en gen_queue, SACALA de gen_queue en la misma corrida.
- Formatos vivos en gen_queue: 🧠 quiz, ⚔️ duelo, 🔍 adiviná, 💡 curiosidades (#curiosidades).

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06).
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.

## 🎯 SEÑAL REAL MEDIDA — los juegos RÁPIDOS son el ganador claro

- **Juegos rápidos sobre SUS plantas (duelo / adiviná / quiz) = ganador.** 15/06: duelo
  jugado COMPLETO 2× seguidas 6/6, dwell 42+24s; adiviná jugado, 32s. 16/06: el usuario
  volvió a duelo/adiviná/quiz (quiz set4 1/4, 34s) en 2 sesiones cortas.
- **Curiosidades verificadas = contenido #1** (12-13/06: todas 😍 + 104s dwell). Sección fija.
- **Rueda del año:** APROBADA 13/06 (87s dwell) y promovida (página + link en nav), PERO
  **sobre-expuesta → fatiga**: meh/meh/no el 15/06 (apareció 6×) + otro "no" el 16/06 (a 3×).
  El 17/06 la SAQUÉ de la rotación de push (4 rechazos acumulados). El feature sigue vivo
  y accesible desde la nav; solo dejamos de empujarlo. NO volver a meterla a gen_queue salvo
  pedido explícito.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas, calendarios, dashboards:
  sol-jardin rechazada ×3, ano-jardin rechazada); (b) formatos LENTOS (mazo flip-card,
  fracasó 3×, nunca test limpio). El usuario quiere **deleite + juego**, NO herramientas.

## ⚠️ APRENDIZAJE NUEVO (16-17/06) — el cuello de botella es VOLUMEN, no falta de formatos

- El 16/06 mandé 20 pushes y **ninguno de los 20 propios juntó un click directo**: el
  engagement vino de un push VIEJO del 15/06 (adiviná) abierto a la mañana + visitas directas.
- La proposal nueva (⚡ V/F) tuvo **CERO engagement**: sus 4 promotores nunca se abrieron,
  sepultados en el volumen. Mismo modo de falla que el mazo. NO fue el formato (los juegos
  rápidos ya probados SÍ se jugaron ese día) — fue dilución.
- **Conclusión:** con ~20 pushes/día el usuario abre 2-3. Lanzar MÁS variantes-juego nuevas
  las canibaliza contra las 2-3 aperturas. Los 3 juegos existentes ya cubren la categoría
  ganadora. → **No crear proposals-juego nuevas solo por crear.** Si lanzo una proposal,
  promocionarla en los slots que de verdad se abren y/o probarla un día de volumen bajo,
  para darle un test LIMPIO en vez de enterrarla.

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **11/06** — 1 push poda @20:00: inconcluyente (deshora, 1ª noche).
- **12/06** — curiosidades @14:30 → GANADOR ("MUY buena" + 😍). Origen de la sección. Noche:
  barrida de 8 pushes a la MISMA página → sobre-saturación. De acá: "1 destino por push".
- **13/06** — cadencia 15min rotada → usuario ACTIVO: aprobó la rueda, rechazó vistas
  utilitarias, 😍 a curiosidades. La rotación importa.
- **14/06** — 39 pushes casi todos a fichas `#especie` → "0 eventos" por BUG de medición (PAT).
- **15/06** — ~20/día con formatos rotados → engagement real y profundo en los JUEGOS
  (duelo 6/6 ×2). Volumen alto OK si cada push es un formato/contenido distinto. Rueda repetida
  6× cansó.
- **16/06** — 20 pushes, formatos rotados (quiz/duelo/adivina/vof/rueda/curio). Los pushes
  propios NO juntaron clicks directos; engagement vía push viejo + directo. V/F = 0. Rueda otro
  "no". → señal de dilución por volumen + fatiga de rueda.

## Decisiones de hoy (17/06)

- **DROP ⚡ V/F (2026-06-16-vof-jardin)** — sin aprobación + 0 engagement (nunca se abrió).
  Página eliminada y sacada de gen_queue. Detalle en proposals.json.
- **RUEDA fuera del push** — 4 rechazos por sobre-exposición. Feature queda (nav), no se empuja.
- **SIN proposal nueva hoy** — 2 proposals seguidas (mazo, V/F) fallaron por NUNCA abrirse, no
  por formato. Crear una 3ª para enterrarla igual es churn. Dejo correr la rotación probada
  limpia y junto datos. Próxima proposal: test limpio (slots que se abren / día de bajo volumen).
- **Cola 17/06:** 13 slots únicos — quiz×4, duelo×4, adivina×4, curio×1. Sin adyacentes.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en dormancia: poco que hacer. Tareas reales casi todas `done`; las `active` son IDs
  scheduleadas para floración primavera. NO inventar urgencia de invierno.
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno
  B-30/35, ciruelos F-4/B-38, caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept
  post-helada**: buganvilia B-1, lantana B-29, cítricos, paltas. NO inventar.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Tareas/uploads del usuario → los procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- **Subir el techo de gen_queue con instancias frescas** de los juegos ganadores (quiz/duelo/
  adivina set5+, si las páginas soportan más sets) antes que inventar formatos nuevos.
- Próxima proposal-experimento: probar en día de bajo volumen o en slots que se abren, NO
  sepultada entre 20 pushes. Idea viva: "¿Cuál sobra?" (odd-one-out de booleanos verificados),
  mecánica de juego genuinamente nueva.
- Regenerar el dataset `M` de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
