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

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 22/06: sigue active.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- Abrir una notificación cuenta como `notification_clicked` vía /api/feedback.

## 🎯 SEÑAL REAL MEDIDA — qué engancha

- **Curiosidades verificadas (#curiosidades) = contenido #1 y el MÁS resiliente.** Abre casi
  siempre, por click directo. Confirmado 12-13/06 (😍 + 104s), 17/06, 18/06, 19/06, 20/06 (A y C
  ambos click directo), **21/06 (A limonero y C lavanda ambos click directo).** Sección fija. Caballo ganador.
- **Juegos rápidos sobre SUS plantas (duelo/adiviná/cual-sobra/quiz) = enganchan PERO se FATIGAN
  con uso seguido.** Pico 15/06 (duelo 6/6 ×2). Fatiga clara 19/06. **Funcionan en ROTACIÓN con
  descanso:** dejar ≥2-3 días sin pushear un juego para que vuelva a sentirse fresco. NO apilar variantes
  nuevas (canibalizan los mismos 2-3 opens — ver "cuello de botella = volumen" abajo). Duelo es el más
  fuerte (6/6 ×2); cual-sobra está aprobado y fijo en nav.
- **ROTACIÓN-CON-DESCANSO CONFIRMADA (22/06).** Duelo, descansado 3 días (último push 19/06), volvió a
  enganchar SOLO: 6/6 ✓ + replay, 37s + 17s dwell, scroll 100%. Es la 2ª vez que duelo da 6/6. Fórmula
  validada: un juego ganador se "recarga" con 2-3 días de descanso. NO quemar el mismo juego días seguidos.
- **Postales / curiosidad-ESTACIONAL como experiencia separada = LÍNEA CERRADA (22/06).** v1 (20/06)
  juntó la señal implícita más fuerte de un no-juego (click + 3 reacciones + 60s 100%), pero NO aprobó.
  v2 (21/06) con contenido fresco + CTA más claro: se abrió y **rebotó en 5s, scroll 10%, 0 reacciones,
  0 aprobación.** Veredicto: el amor de v1 era NOVEDAD, no formato; una 2ª edición no retiene. El
  contenido-curiosidad ya vive y convierte en la sección fija #curiosidades — ahí va, no como página aparte.
- **Rueda del año:** aprobada (87s) y promovida (nav), pero sobre-expuesta → FUERA del push desde 17/06.
- **Perdedores confirmados:** (a) herramientas utilitarias (mapas/calendarios/dashboards: sol-jardin ✗×3,
  ano-jardin ✗); (b) formatos LENTOS (mazo flip-card ✗×3). El usuario quiere **deleite + juego**, NO herramientas.

## ✅ APRENDIZAJE CLAVE — el cuello de botella era VOLUMEN, no el formato (18/06, confirmado)

- Proposals previas (mazo ×2, V/F) fracasaron SEPULTADAS entre 13-39 pushes — nunca tuvieron test limpio.
- 18/06 cual-sobra con slot diurno dedicado (13:00) juntó click+juego+aprobación en su 1er turno.
- Una proposal nueva merece un día de bajo volumen y un slot diurno propio (13:00). No lanzar varias
  variantes-juego seguidas que canibalizan los mismos 2-3 opens.

## Conclusiones de los pushN enviados hasta ahora (por feedback real)

- **12/06** — curiosidades @14:30 → GANADOR ("MUY buena" + 😍). Origen de la sección fija.
- **13/06** — usuario ACTIVO: aprobó la rueda (87s), rechazó vistas utilitarias (ano/sol-jardin).
- **14/06** — 39 pushes → "0 eventos" por flood + bug de medición. Inservible.
- **15/06** — ~20/día → juego profundo (duelo 6/6 ×2). Pico de engagement, pero sepultó proposals.
- **16/06** — 20 pushes → pushes propios NO juntaron clicks; V/F=0; rueda otro "no". Dilución pura.
- **17/06** — 13 pushes → 1 solo click directo y fue curiosidades.
- **18/06** — **3 pushes. GANADOR.** A(curio)→click; B(cual-sobra 13:00)→click+juego+APROBADA+29s; C tarde.
- **19/06** — 3 pushes. Curiosidades RE-confirmada (A→click directo); juegos empezando a fatigar (B/C bounce).
- **20/06** — **3 pushes. 3/3 CLICKS.** A(curio)→click; B(Postales v1)→click+3 reacc+60s SIN aprobar; C(curio)→click.
- **21/06** — **3 pushes. 3/3 CLICKS pero proposal MUERTA.** A(curio limonero)→click; C(curio lavanda)→click;
  B(Postales v2)→click pero REBOTE 5s/10%/0 reacc/0 aprob. La 2ª postal no retuvo → cierra la línea postales.
  Lectura: los 2 curios son el sostén fiable; el slot del medio (proposal) es el débil cuando repito formato.
- **22/06** — **3 pushes + 2 sorpresas manuales del usuario.** A(curio Palta B-22)→CLICK. B(Duelo, descansado
  3 días)→**6/6 ✓ + replay, 37s+17s dwell, scroll 100%**: el re-test del juego descansado FUNCIONÓ. C(curio
  Gardenia)→sin click logueado. A medianoche el usuario se auto-mandó 2 sorpresas (🌍 mundo-jardin + 🧩
  memoria-jardin, formatos NUEVOS que él mismo creó) — sin engagement aún (mandadas ~00:58, dormido). Señal
  clave: usuario MUY activo y buscando JUEGOS por iniciativa propia → los juegos NO están fatigados ahora,
  están en demanda. mundo/memoria son assets nuevos sin test diurno todavía.

## Decisiones de hoy (23/06)

- **Proposals:** postales-invierno-2 quedó con status "pending" por bug de la corrida del 22 (el HTML ya estaba
  borrado y las notas decían DROPPED) → corregido a "dropped" hoy. NO hay proposals pendientes vivas.
- **NO se crea proposal nueva hoy.** El usuario está auto-explorando juegos (creó mundo + memoria anoche); no
  tengo una hipótesis genuinamente nueva que esos assets no cubran ya. Próxima proposal sólo con mecánica nueva.
- **Experimento del día:** dar a 🌍 mundo-jardin (nuevo, scrollytelling "5 continentes", creado por el usuario
  anoche) su PRIMER test diurno limpio. La sorpresa de medianoche probablemente no se vio (dormido). Slot 13:00.
- **Estructura:** 2 curiosidades (sostén fiable) + 1 experiencia nueva (mundo-jardin). Sin postales, sin proposal.
  Duelo NO se re-pushea hoy (se jugó anoche → descanso para no quemarlo, fórmula rotación-con-descanso).
- **Cola de 3:** (a) 08:30 curio Hortensia B-13 (cambia de color según suelo) → #curiosidades; (b) 13:00
  experiencia 🌍 mundo-jardin; (c) 19:30 curio Aguaribay B-7 (pimienta rosa real, sagrado incas/guaraníes) →
  #curiosidades. Curios de plantas sin solape con días recientes (palta/gardenia/limonero/lavanda ya usadas).
- Sin compactación: el evento más viejo es 12/06 (11 días) < 14. send_log y engagement quedan completos.

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

- ✅ RESUELTO 22/06: re-test de Duelo descansado → enganchó 6/6 + replay. Rotación-con-descanso CONFIRMADA.
- **Medir el test diurno de 🌍 mundo-jardin (23/06):** la sorpresa de medianoche probablemente no se vio. Si en su
  slot diurno (13:00) junta click + dwell/reacciones → es un asset ganador estable para la rotación. Si rebota →
  el formato scrollytelling no retiene de día y conviene priorizar juegos rápidos + curiosidades. Idem 🧩 memoria
  cuando le toque turno diurno.
- **Proposals:** próxima sólo con hipótesis GENUINAMENTE nueva (no variante de algo medido). Postales, mazo, V/F,
  mapas y calendarios ya están descartados. Pensar mecánicas nuevas de deleite, no más de lo mismo.
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
</content>
</invoke>
