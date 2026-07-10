# Learnings del agente de engagement

Memoria del agente diario. Se REESCRIBE y condensa cada día (máx ~150 líneas).
No es un log: es lo que necesito recordar para decidir el contenido de mañana.

## ⏱️ CADENCIA VIGENTE: 3 pushes/día — fijada por el usuario el 18/06

Cola escrita A MANO (3 entries pending en queue.json). Slots: 08:30 / 13:00 / 18:00 (-03:00) — el slot c
se movió de 19:30 a 18:00 el 05/07. Primer send_at ≥60 min después de la corrida. expires_at = mismo día
22:00 -03:00. Cada notificación a un destino DISTINTO. Timestamps SIEMPRE con `-03:00`.
**3 pushes curados ganan a 20 — CONFIRMADO.** El usuario abre 2-3/día sin importar cuántos mandes.

## 📌 PEDIDOS DIRECTOS DEL USUARIO 04/07 — NO PISAR

1. **🕵️ Expedientes** (`engage/2026-07-04-expedientes-jardin.html`) — COMISIONADA para identificar 13 fichas
   dudosas + 2 sin ficha. Pre-aprobada, EXENTA de la regla de no-supervivencia. Respuestas llegan como `answer`
   qids `exp-*`: PROCESARLAS → actualizar `data_plants.py` + la página. **10/07: SIGUE sin respuestas exp-***
   (6 días sin señal). Re-push HECHO hoy en slot c (18:00) con copy detective. Si sigue mudo, deprioritizar.
2. **🎯 Top 3** (`engage/top3-tareas.html`) — recurrente CADA 2 DÍAS (ancla 04/07). Paso obligatorio:
   `python tools/gen_top3_tareas.py <fecha> --merge` (self-gated). Corrió 04,06,08,10/07; próxima **12/07**.
3. **Dato clave**: B-41 "caqui" con identidad EN DUDA (nunca mostró flor ni fruto). No usarlo como curio de fruta.
4. Timeline: hechas/cerradas van colapsadas en "🗂️ Pasadas / hechas" (vista Todas).
5. **Splash** «Hora dorada» integrado en Home. Los 6 demos `engage/splash-*.html` = referencia: NO tocar.
6. ⚠️ **Pillow (PIL) no viene instalado** en el runner: `pip install Pillow` ANTES de correr los gen_*.py / build.py.
   Paso previo obligatorio de cada corrida.

## 🆕 FUNCIÓN PARALELA (pedido del usuario 28/06): 2 experiencias NUEVAS de cero por corrida

Cada corrida inicializo persona product/UX/sales y construyo DOS experiencias news-feed de cero, cada una con:
(1) reacción final (engageReact target=slug), (2) CTA de **suscripción diaria** (engageAnswer qid
`<slug>-suscripcion-diaria`), (3) un **HTML de pitch** aparte con 6 modelos de monetización (3 innovadores +
3 ultra-creativos). Contrato de proposal igual que siempre (link "← Volver al sitio estable" primero,
react+sub+engage-actions con Aprobar/No-me-interesa reales para las pending, `engage.js`, SOLO datos verificados
de data_plants.py con código). Dos de los 3 pushes llevan a estas experiencias; el 3º rota una promovida ganadora
descansada (o una comisionada con pedido real, ej. Expedientes).

## 🚀 EL NEWS-FEED CONVIERTE — y dentro del formato, el ÁNGULO decide

**Convierte amor→SUSCRIPCIÓN: ASOMBRO/ESTATUS/CHISME/IDENTIDAD/1ª-PERSONA-INDIVIDUAL/CELEBRIDAD + — nuevo 09/07 —
la UI de una APP AMADA (Spotify Wrapped), siempre con el DATO REAL DEL PRESENTE como protagonista. NO convierten:
ficción-protagonista (torneo/gala/reality), utilidad, geografía, intimidad-coral, DINERO (tasación), PASADO
(efemérides/historia), MIEDO/PELIGRO, el envoltorio CHAT-GRUPAL, y RANKING-del-presente cuando ya existe Récords.**

**🔑 META-PATRÓN GANADOR (09/07): pedir prestada la UI de una app querida.** El Wrapped (Spotify Wrapped) dio
😍+approved+172s. La familiaridad del molde + novedad + dato-presente convierte. → hoy DOBLO con JardínFlix (Netflix).

**CONVIERTEN (love/sub SÍ + aprobado, dwell alto) — PROMOVIDAS:**
- **📱 Feed (red-social, 1ª persona)** — dwell 208s, 😍×2, sub×2.
- **🍵 Chusmerío (tabloide/chisme)** — 09/07 slot c re-push → **260s (NUEVO RÉCORD dwell del canal)** + re-sub SÍ + 😍.
- **🎙️ Entrevista (CELEBRIDAD, 1ª persona INDIVIDUAL)** — sub + approved + 206s.
- **🎁 Wrapped (app-amada/número-presente)** — 😍 + approved + 172s (3er dwell). Sin tap de sub (ver abajo).
- **🌱 Quiz «¿Qué planta sos?» (IDENTIDAD)** — 😍 + approved + 103s. Sin tap de sub.
- **🔮 Horóscopo (IDENTIDAD)** — 😍 + sub + 115s.  · **🏆 Récords (orgullo/número presente)** — 😍 + sub + 141s.
- **📰 Diario (editorial/novedad)** — 😍 + sub + 92s.

**⚠️ Patrón 09/07 a vigilar:** Quiz y Wrapped juntaron 😍+aprobación+dwell alto pero NINGUNO tocó el CTA de
suscripción diaria. Hipótesis: aprobar ya se siente como "sí", o el bloque de sub debajo del de aprobación se
saltea. Idea a probar: poner el bloque de SUSCRIPCIÓN ANTES del de aprobar, o fusionarlos. La aprobación explícita
alcanza para promover, pero la métrica de sub se está perdiendo en las experiencias que más gustan.

**APRUEBAN sin conversión completa (tibios, promovidos):** 😂 Memes · 🧪 Superpoderes · 💌 Consultorio ·
🎤 Confesiones (133s retiene, sin sub) · 📺 Reality.

**RECHAZAN / NO ABREN (dropped):** 🔥 Trending (ranking pisa a Récords) · ⚠️ Lista Negra (miedo) · 💬 Chat (coral,
"más notificaciones") · 💰 Tasación (dinero des-romantiza, 198s y rechazó) · 🗞️ Efemérides (pasado) · 🏆 Gala /
⚽ Mundial (ceremonia/torneo) · 🗺️ Pasaporte (viajes) · 💘 Amores (romance).

**Regla operativa:** apuntar a MORBO-CHISME, 1ª PERSONA foco INDIVIDUAL, IDENTIDAD, CELEBRIDAD/ESTATUS,
ORGULLO-superlativo, HUMOR, y UI-de-app-amada — siempre sobre el AHORA. Evitar: miedo, chat-coral, dinero, pasado,
utilidad seca, geografía, consejo, intimidad-coral, ceremonias/torneos, y ranking que pise a Récords.

## 📈 Slot c (tarde) — rotar promovidas ganadoras descansadas = reactiva SUSCRIPCIÓN

- Curios como destino propio = MUERTO. Curios solo DENTRO de experiencias.
- **08/07 slot c → Récords re-push → re-sub SÍ. 09/07 slot c → Chusmerío re-push → 260s RÉCORD + re-sub SÍ + 😍.**
  Rotar una promovida ganadora bien descansada al slot c REACTIVA la suscripción — CONFIRMADO 2 veces, es la jugada
  más confiable para recuperar subs. Chusmerío/Récords ya usadas 08-09/07 → descansar ≥1 semana.
- **10/07 slot c → Expedientes** (comisionada, exp-* mudo 6 días). No es "descansada-ganadora" sino pedido real;
  si no traccciona, el slot c vuelve a rotar promovidas (candidatas descansadas: Diario, Feed, Horóscopo).

## 🎯 Señal real medida — qué engancha (histórico)

- **NEWS-FEED de contenido verificado = formato #1.** 14 promovidas (Quiz + Wrapped sumadas 10/07).
- Recordatorios de tareas SIEMPRE abren: task-dia clickeado 04,05,08/07; task-semana 06/07. Canal más confiable.
- **Perdedores confirmados:** utilitarias secas; flip-card ×3; memory-match; postales; Pasaporte; Amores; Mundial;
  Gala; Tasación; Efemérides; Lista Negra (miedo); Chat (coral); Trending (ranking).
- El usuario quiere **deleite + dato real asombroso del PRESENTE como protagonista**.

## Estado del sistema

- Push subscription device `pix9`: **active** (desde 11/06). Verificado 09/07.
- Logging por `/api/feedback` (outbox localStorage, sin PAT). Confiable desde 15/06.
- **Cutoff de datos:** engagement.json último sync **2026-07-09T23:11Z** (20:11 UY). Cubre TODO el 09/07:
  Quiz 😍+approved 14:33 UY, Wrapped clic+😍+approved+172s 15:18 UY, Chusmerío slot c 260s+re-sub+😍 20:11 UY.
  task-dia 09/07 (Guayabo) sin click registrado. NO hay datos del 10/07 todavía.
- Compactación 10/07: 25/06 movido a daily_summary (engagement + send_log). Ventana viva **26/06–09/07**.
- Upload pendiente: 1 foto de B-15 en uploads.json (territorio de /actualizar-tareas, no tocar).

## Conclusiones de los pushN enviados (por feedback real)

- **04/07** — Memes → APROBADO tibio (71s, sub no confirmada); task-día → click.
- **05/07** — Tasación → RECHAZO pese a 198s (dinero des-romantiza); Efemérides → NO-OPEN.
- **06/07** — Lista Negra → NO-OPEN (miedo); Chat → RECHAZO (18s, coral); task-semana → CLICK.
- **08/07 (ciclo 38)** — Entrevista → GANADORA (sub+approved+206s) PROMOVIDA; Trending → SOFT-NEG DROPPED
  (canibaliza Récords); Récords slot c → re-sub SÍ; task-dia + top3 → click.
- **09/07 (ciclo 39)** — **DÍA FUERTE, 3/3 con señal.** Quiz (identidad) → 😍+approved+103s → PROMOVIDA.
  Wrapped (app-amada Spotify) → 😍+approved+172s → PROMOVIDA + descubrimiento del META-PATRÓN "UI de app querida".
  Chusmerío slot c re-push → **260s RÉCORD** + re-sub SÍ + 😍 (rotar promovida al slot c reactiva sub, 2ª vez).
  Único hueco: Quiz y Wrapped NO tocaron el CTA de suscripción (ver «Patrón 09/07 a vigilar»).
- **Meta-conclusión:** 7 ejes convierten (social / celebridad-individual / identidad / chisme / orgullo-superlativo /
  editorial / **UI-de-app-amada**). El push gana apertura+conversión con FOCO INDIVIDUAL + dato del PRESENTE, y ahora
  también prestando la interfaz de una app que la gente ya ama.

## 🔭 Corrida 10/07 — ciclo 40 (esta corrida)

- **Proposals resueltas:** Quiz→PROMOVIDA + Wrapped→PROMOVIDA (ambas 😍+approved el 09/07; tarjetas en Ideas→✨
  Experiencias; footers a nota de integración). NOTA: ambas FALTABAN en proposals.json (la corrida del 09/07 creó
  páginas+queue+learnings pero no las registró) → registradas hoy directamente como promoted.
- **2 experiencias NUEVAS de cero (pending, created=10/07):**
  - 🍿 **JardínFlix** (`engage/2026-07-10-jardinflix.html`) — catálogo estilo Netflix. DOBLA el meta-patrón ganador
    (UI de app amada, que el Wrapped validó). Top 10 del presente + títulos "basados en hechos reales" + estreno
    DIARIO (más cadencia que el Wrapped estacional). Push a (08:30).
  - 📗 **El Álbum de tu Jardín** (`engage/2026-07-10-album-figuritas.html`) — figuritas Panini. Rareza/brillantes
    (nativa protegida, +400 años, origen único) derivada de rasgos reales. Colección+completar+estatus+cultura
    "¿la tenés?" + timing Mundial 2026. 2 figuritas fantasma (caqui B-41 dudoso, B-20 sin nombre). Push b (13:00).
- **Cola ciclo 40:** (a) 08:30 🍿 JardínFlix; (b) 13:00 📗 Álbum; (c) 18:00 🕵️ Expedientes (re-push comisionado).
  + 08:00 task-día (Pindó B-8 limpieza). + 09:00 top3 (10/07 TOCÓ).
- **Watch 40:** (1) ¿JardínFlix confirma que el meta-patrón "UI de app amada" es replicable (no fue solo el Wrapped)?
  (2) ¿el Álbum (coleccionismo/rareza/estatus) convierte, o el "álbum" se lee como lo utilitario que el usuario
  rechaza? (3) ¿por fin aparecen respuestas exp-* con el re-push detective? (4) probar mover el bloque de SUB antes
  del de aprobar para recuperar la métrica de suscripción que Quiz/Wrapped perdieron. (5) Proposals sin aprobación
  se dropean 11/07. **El 12/07 TOCA top3.**

## Contexto del jardín (julio 2026 = pleno invierno, lat -34.9°S)

- Jardín en DORMANCIA: poco real que hacer. **NO inventar urgencia de invierno.**
- Señales REALES: cítricos cargados (mandarina B-24, limonero B-23 da 12/12); romero B-26 florece jun-oct (ÚNICA
  en julio); palta B-22/B-36 y pindó B-8 con fruto hasta jul-oct; caducos pelados (durazno B-30/35, crespón B-9,
  liquidámbar B-37, pera B-39); perennes verdes (guayabo F-1, mirto B-27, lavanda, evónimo B-44). Heladas tardías
  pegan más al **sur y al este al amanecer**.
- Tarea activa urgente real: Guayabo F-1-4 fumagina + plaga (alta, mayo 2026, sigue abierta). Gardenia B-25 pulgones
  + hormigas (alta). Liquidámbar B-37 limpieza de copa en dormancia.

## Verificados clave (stats consistentes entre experiencias — NO contradecir)

52 especies · 65 id_codes · 10 nativas (F-1,F-8,B-8,B-14,B-16,B-29,B-32,B-34,B-42,B-47) · 30 perennes · 15 caducos ·
11 frutales · romero B-26 = única que florece en julio · limonero B-23 = fruta 12/12 meses ·
palta Hass B-36 = clon de 1 árbol de 1926 · anacahuita B-16 = protegida por ley desde 1986 · hiedra B-15 = +400 años.

## TODO pendiente

- **Ángulos NEWS-FEED usados:** editorial ✓, superlativos ✓, red-social ✓, tabloide ✓, identidad ✓ (×2: horóscopo+quiz),
  celebridad ✓, humor (tibio), consejo (tibio), confesión-coral (tibio), reality (tibio), app-amada ✓ (Wrapped; hoy
  JardínFlix), coleccionismo (hoy Álbum). ✗: viajes, romance, competencia, gala, tasación, efemérides, miedo, chat, ranking.
  **Sin usar (posibles ganadores):** before/after con fotos del usuario (esperar más uploads); otras apps-amadas
  (stories, Wordle/juego-diario, spotify-playlist real, mapa tipo Pokémon-GO).
- Regenerar el dataset M de la rueda desde data_plants.py en build-time (hoy snapshot estático).
- Reconciliar arrays `pruning` con el timing corregido antes de cualquier vista de poda.
- Idea de UX a testear: bloque de SUSCRIPCIÓN antes del de aprobación (Quiz/Wrapped aprobaron sin tocar sub).
