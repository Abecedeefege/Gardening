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

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 26/06: sigue active.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- Abrir una notificación cuenta como `notification_clicked` vía /api/feedback.
- Compactación al día (26/06): engagement.json y send_log.json trimados de eventos ≤12/06
  → daily_summary {12/06: sent14/click1/visit1}. Ventana viva ahora 13–25/06 (rolling 14d).

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **Curiosidades verificadas (#curiosidades) = contenido #1 y el MÁS resiliente.** Abre casi
  siempre por click directo. Confirmado 12-13/06 (😍 +104s), 17-23/06. **PERO no es infalible
  carta por carta:** el 24/06 el curio de cierre (Hibisco) abrió por click directo pero el de
  apertura (Buganvilia/Santa Rita, 08:30) NO se abrió. Lectura: la SECCIÓN es el caballo ganador
  y el sostén fiable; el hit por-notificación depende del gancho y del slot. Sigue siendo el núcleo.
- **🌍 mundo-jardin (creado por el usuario): asset GANADOR estable — VALIDADO 2 veces.** Ganó su
  test diurno limpio 23/06 (click + 😍love + 95s dwell scroll 100%) y RE-confirmó 25/06 (click +
  😍love). Es el asset-experiencia más fiable que tenemos. Rota CON descanso (no 2 días seguidos):
  pushado 23 y 25 → DESCANSA hoy 26/06 para no sobre-exponerlo. NO es proposal (lo creó el usuario),
  ya vive en engage/.
- **Juegos rápidos sobre SUS plantas (duelo/adiviná/quiz) = enganchan PERO se FATIGAN con uso
  seguido.** Funcionan en ROTACIÓN con descanso ≥2-3 días. Duelo es el más fuerte (6/6 ×2: 15/06 y
  re-test 22/06 con 37s+17s, scroll 100% tras 3 días → rotación-con-descanso CONFIRMADA).
  **cual-sobra: REMOVIDO de la nav + página borrada por pedido del usuario (22/06) — NO re-promover.**
- **🧩 memoria-jardin (memory match, creado por el usuario): FALLÓ su test diurno limpio (24/06).**
  Slot 13:00 dedicado, SIN competencia, día de bajo volumen → CERO engagement (sin click, sin
  page_visit, sin reacción). Es el escenario IDEAL que mundo SÍ aprovechó el 23 — y memoria no.
  **Veredicto: memoria NO retiene; se BENCHEA de la rotación de push.** No se borra el archivo (es
  creación del usuario; sigue accesible en engage/), pero NO se vuelve a pushear. El gemelo ganó
  (mundo) y el gemelo perdió (memoria): el formato memory-match no es lo que engancha a ESTE usuario.
- **Postales / curiosidad-ESTACIONAL como experiencia separada = LÍNEA CERRADA (22/06).** v1 (20/06)
  amó (click+3 reacc+60s) pero NO aprobó; v2 (21/06) rebotó 5s/10%. El amor de v1 era NOVEDAD, no
  formato. El contenido-curiosidad ya vive y convierte en la sección fija #curiosidades — ahí va, no aparte.
- **Rueda del año:** aprobada (87s) y promovida (nav), pero sobre-expuesta → FUERA del push desde 17/06.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards: sol-jardin ✗×3,
  ano-jardin ✗); (b) formatos LENTOS (mazo flip-card ✗×3); (c) memory-match (memoria ✗, test limpio).
  El usuario quiere **deleite + contenido-curiosidad + juego rápido**, NO herramientas ni mecánicas lentas.

## ✅ APRENDIZAJE CLAVE — el cuello de botella era VOLUMEN (18/06) + el formato (24/06)

- Proposals previas (mazo ×2, V/F) fracasaron SEPULTADAS entre 13-39 pushes — nunca tuvieron test limpio.
  La cadencia baja (3/día) es la única que da test justo. ESO se resolvió.
- PERO un test limpio también puede dar NEGATIVO real: memoria tuvo el día perfecto (24/06) y aun así 0.
  Cuando hay test limpio y no engancha, es señal de FORMATO, no de volumen. Memoria es el primer caso así.

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **18/06** — **3 pushes. GANADOR.** A(curio)→click; B(cual-sobra 13:00)→click+juego+APROBADA; C tarde.
- **19/06** — 3 pushes. Curiosidades RE-confirmada (A→click); juegos empezando a fatigar (B/C bounce).
- **20/06** — **3/3 CLICKS.** A(curio)→click; B(Postales v1)→click+3 reacc+60s SIN aprobar; C(curio)→click.
- **21/06** — **3/3 CLICKS pero proposal MUERTA.** Postales v2 abrió pero rebotó 5s/10% → cierra postales.
- **22/06** — A(curio Palta)→CLICK; B(Duelo descansado 3 días)→**6/6 + replay, 37s+17s, 100%**; C(curio
  Gardenia)→sin click. Medianoche: el usuario se auto-mandó 🌍 mundo + 🧩 memoria → busca JUEGOS/experiencias.
- **23/06** — **3/3 CLICKS.** A(curio Hortensia)→click; **B(🌍 mundo, 1er test diurno)→click + 😍love +
  95s scroll 100% = GANÓ, asset validado**; C(curio Aguaribay)→click.
- **24/06** — **1/3 CLICKS.** A(curio Buganvilia 08:30)→sin click; **B(🧩 memoria, test diurno limpio)→
  CERO engagement = FALLÓ**; C(curio Hibisco 19:30)→click directo. Lectura: memoria se benchea; el curio
  matinal no enganchó (¿gancho/horario?), el vespertino sí. Volver al core probado.
- **25/06** — **2/3 CLICKS, día sólido.** A(curio Mandarina B-24, 08:30)→**CLICK** (13:54, el matinal
  SÍ enganchó esta vez, a diferencia del 24); **B(🌍 mundo-jardin, 13:00)→CLICK + 😍love** (re-validación
  limpia, 2da vez que ama mundo); C(curio Romero B-26, 19:30)→sin click. Lectura: el core probado
  (curio + mundo) sigue rindiendo; el slot matinal es variable (engancha según gancho, no garantizado);
  un curio por día sin click es ruido normal, no señal. mundo CONFIRMADO ×2 → rotar con descanso.

## Decisiones de hoy (26/06)

- **Proposals:** NO hay pendientes vivas (todas dropped/promoted/removed). Nada que gestionar. NO se crea
  proposal nueva: sigue sin haber hipótesis genuinamente nueva (postales/mazo/V/F/mapas/calendarios/
  memory-match ya descartados). Próxima proposal SOLO con mecánica realmente nueva de deleite o juego rápido.
- **Estrategia: CORE PROBADO + rotación de ganadores con descanso.** mundo-jardin se pushó ayer (25) →
  hoy DESCANSA para no sobre-exponerlo. Se trae de vuelta el **Duelo** (el juego más fuerte: 6/6 ×2,
  último push 22/06 = 4 días de descanso ≥ umbral). Estructura = 2 curios frescos + 1 experiencia-juego rotada.
- **Cola de 3:** (a) 08:30 curio **Liquidámbar B-37** (hoy silueta pelada de invierno = ancla estacional real;
  storax/bálsamo que los mayas masticaban como chicle, 'ámbar líquido') → #curiosidades; (b) 13:00 **🌿 Duelo
  de plantas** (descansó 4 días; gancho personal 'hiciste 6/6, ¿lo repetís?') → engage/duelo-jardin.html;
  (c) 19:30 curio **Crespón B-9** (hoy caduco pelado = ancla invernal; nombre por Magnus von Lagerström,
  flores de papel crepé) → #curiosidades. Curios sin solape con mandarina/romero (25) ni palta/gardenia/
  limonero/lavanda/hortensia/aguaribay/buganvilia/hibisco (días recientes). Ambos anclados en señal REAL de invierno.
- **Watch:** si el Duelo no engancha hoy (4 días de descanso, su mejor ventana), es señal de que los juegos
  rápidos también se están agotando como categoría → el próximo turno priorizar mundo + curios y dejar
  descansar TODOS los juegos ≥1 semana. Si SÍ engancha, confirma rotación-con-descanso para duelo igual que mundo.
- **Compactación:** engagement.json y send_log.json trimados de eventos ≤12/06 → daily_summary
  (12/06: sent14/click1/visit1). queue.json reescrita con los 3 de hoy.

## Contexto del jardín (junio 2026 = invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. Tareas casi todas `done`; las `active` son IDs scheduleadas para
  floración/ID de primavera. **NO inventar urgencia de invierno.**
- Señales REALES de invierno (sirven para curios): cítricos cargados (mandarina B-24 FRUIT jun-ago; limonero
  B-23 fruta casi todo el año); romero B-26 FLOR jun-oct; caducos pelados (durazno B-30/35, crespón B-9,
  liquidámbar B-37 silueta tras color otoñal, con su storax).
- Poda: jun-jul **solo limpiezas** + trasplantes en dormancia. **Fines jul-ago**: durazno B-30/35, ciruelos
  F-4/B-38, caqui B-41, crespón B-9, althea B-18, hibisco B-4. **Sept post-helada**: buganvilia B-1, lantana
  B-29, cítricos, paltas.
- Heladas tardías (jun-ago) pegan más al **sur y al este al amanecer**.
- Hay 1 upload pending (B-15) → lo procesa `/actualizar-tareas`, no este agente.

## TODO pendiente

- ✅ RESUELTO 23/06: 🌍 mundo-jardin pasó su test diurno → asset ganador estable (rotar con descanso).
- ✅ RESUELTO 24/06: 🧩 memoria-jardin FALLÓ su test diurno limpio → bencheada de la rotación de push (archivo
  conservado por ser creación del usuario; no re-pushear). El formato memory-match no engancha a este usuario.
- **Curios frescos disponibles** (no usados recientemente, fun_fact verificado): ciruelo Pissardii (1 ejemplar
  1880), liquidámbar B-37 (storax/maya goma de mascar), crespón B-9 (Lagerström/papel crepé), guayabo (pétalos
  comestibles), hiedra (vive 400 años, 2 fases), clivia (vive 100 años), espada/sansevieria (NASA purifica aire).
- **Proposals:** próxima SOLO con hipótesis GENUINAMENTE nueva (no variante de algo medido). Descartados:
  postales, mazo, V/F, mapas, calendarios, memory-match. Pensar mecánicas nuevas, no más de lo mismo.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
