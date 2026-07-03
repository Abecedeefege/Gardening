# Experiencias diarias con Routines — Playbook replicable

Cómo montar en **cualquier app estática** el sistema de experiencias diarias que
corre en este jardín: una **Routine de Claude Code** despierta un agente cada
mañana, el agente **construye experiencias nuevas** (páginas HTML efímeras),
las **promociona por Web Push** al teléfono, **mide** qué enganchó (clicks,
dwell, reacciones, aprobación explícita) y **adapta** el contenido del día
siguiente. Todo sin backend propio: el estado vive como JSON en el repo.

Este documento cubre la capa de **orquestación y contenido**. La capa de
**push** (VAPID, service worker, dispatcher, cola) está documentada aparte en
[`WEB_PUSH_PLAYBOOK.md`](WEB_PUSH_PLAYBOOK.md) — implementala primero, es el
prerequisito. Al final hay **cuatro prompts listos para pegar** que
bootstrapean el sistema completo en findmetea.com, la Biblioteca,
Psicologeando y LunesDeUNO.

---

## 0. La idea en una imagen

```
                 ┌─────────────────────────────────────────────────┐
  06:00 UY       │  ROUTINE (Claude Code, cron diario)             │
  ───────────▶   │  corre el comando /engagement en el repo        │
                 └────────────────────┬────────────────────────────┘
                                      │ lee memoria + datos de ayer
                                      ▼
                 ┌─────────────────────────────────────────────────┐
                 │  AGENTE DIARIO                                  │
                 │  1. lee learnings.md + engagement.json          │
                 │  2. promueve / dropea proposals de ayer         │
                 │  3. construye 1-2 experiencias NUEVAS (HTML)    │
                 │  4. encola N pushes del día (queue.json)        │
                 │  5. reescribe learnings.md + commit + push      │
                 └────────────────────┬────────────────────────────┘
                                      │ push a main → deploy automático
                                      ▼
   teléfono  ◀── Web Push ◀── dispatcher (GitHub Actions, cada 30 min)
      │
      │ el usuario toca la notificación → abre la experiencia
      ▼
   engage.js loguea: notification_clicked · page_visit · dwell ·
   reaction (😍/🙂/😐/🙅) · answer (CTAs) · proposal_approved/rejected
      │
      └──▶ docs/sync/engagement.json  ──▶  lo lee el agente MAÑANA
```

Es un **loop de experimentación**: cada experiencia es una hipótesis, cada
push es un test, y la memoria (`learnings.md`) acumula qué convierte y qué no.

---

## 1. Los 6 componentes

| # | Componente | Archivo(s) en este repo | Rol |
|---|---|---|---|
| 1 | Capa Web Push | `docs/sw.js`, `docs/notifications/*`, `tools/send_push.js`, `.github/workflows/push-dispatch.yml` | Entregar la notificación aunque la app esté cerrada |
| 2 | Comando del agente | `.claude/commands/engagement.md` | El "cerebro": procedimiento + reglas duras del agente diario |
| 3 | Routine | Configurada en claude.ai/code (no vive en el repo) | Despertar al agente todos los días a la misma hora |
| 4 | Páginas de experiencia | `docs/engage/<YYYY-MM-DD>-<slug>.html` + `proposals.json` | El contenido efímero que se testea |
| 5 | Tracking de feedback | `docs/engage/engage.js` + `api/feedback.js` (Vercel) | Medir sin backend y sin perder eventos en mobile |
| 6 | Memoria del agente | `docs/engage/learnings.md` | Qué funcionó, qué no, cadencia vigente — se REESCRIBE, no se acumula |

**Regla de oro de ownership (no cruzar escrituras):**

| Actor | Escribe |
|---|---|
| Agente diario (Routine) | `queue.json` (rewrite), `engage/*`, data files + build |
| Dispatcher (Actions) | statuses de la queue, `send_log.json`, invalidación de suscripción |
| Browser (usuario) | `sync/push_subscription.json`, `sync/engagement.json` (vía `/api/feedback`) |

---

## 2. Componente 1 — Web Push (prerequisito)

Seguí el checklist de `WEB_PUSH_PLAYBOOK.md` §10. Resumen mínimo:

1. `npx web-push generate-vapid-keys` → pública al repo, privada como secret
   `VAPID_PRIVATE_KEY` de GitHub Actions.
2. `sw.js` en el directorio publicado (recibe el push, abre el deep link con
   `?nid=&src=push`).
3. Botón "Activar notificaciones" que suscribe y persiste la suscripción en
   `notifications/subscription.json` (vía GitHub API con PAT del usuario, o
   vía una serverless function).
4. `queue.json` + `tools/send_push.js` + workflow `push-dispatch.yml` con
   **triple trigger**: cron cada 30 min (respaldo) + `workflow_dispatch` +
   `on: push` a la cola (encolar = despachar al instante).
5. **`urgency: 'high'` + TTL 4h** en cada envío — sin esto Android retiene o
   descarta las notificaciones (Lección #1 del playbook).

No sigas hasta que un push de prueba llegue al teléfono con la app cerrada.

---

## 3. Componente 2 — El comando del agente (`/engagement`)

Es un archivo markdown en `.claude/commands/engagement.md` con frontmatter
YAML. Claude Code lo expone como slash command; la Routine simplemente lo
invoca. La versión completa está en este repo — la anatomía es:

```markdown
---
description: Agente diario de engagement. Lee datos de ayer, gestiona
  proposals, crea experiencias, encola los pushes del día. Commitea a main.
allowed-tools: Read, Bash, Edit, Write, Glob, Grep
---

# /engagement — Agente diario

Objetivo de fondo: <QUÉ QUERÉS LOGRAR — ej. "que el usuario vuelva a abrir
la app y pase tiempo en ella">. Palancas: N pushes/día, páginas proposal,
y la memoria de qué funcionó.

## Procedimiento
1. LEER contexto (en orden): learnings.md → engagement.json →
   send_log.json + queue.json → proposals.json → datos reales de la app →
   fecha/estación → estado de la suscripción push.
2. GESTIONAR proposals de ayer: approved → promover al sitio;
   rejected → git rm + dropped; pending de días anteriores → git rm
   (sin aprobación explícita NO sobreviven — regla clave).
3. COMPACTAR datos: eventos >14 días → daily_summary; queue limpia;
   learnings.md se REESCRIBE (máx ~150 líneas).
4. CREAR experiencias nuevas (según la cadencia vigente de learnings.md).
5. ESCRIBIR la cola del día (queue.json) — cada push a un destino DISTINTO.
6. BUILD + COMMIT + PUSH a main. Nunca dejar main roto.
7. REPORTAR: datos de ayer, decisiones sobre proposals, pushes de hoy, SHA.

## Reglas duras
- Autonomía total: sin confirmaciones por chat. Las preguntas al usuario
  van DENTRO de la app (una pregunta con botones en una experiencia).
- Proposals sin aprobación explícita se eliminan al día siguiente.
- Archivos del usuario (estado, uploads) son SOLO LECTURA para el agente.
- Nunca commitear secretos / PATs / claves privadas.
- No inventar urgencias ni datos para generar clicks: la credibilidad
  del canal es EL activo. Todo dato afirmado, verificado contra la fuente.
```

Puntos que costaron aprender (bakealos desde el día 1):

- **La memoria se reescribe, no se acumula.** Un `learnings.md` que solo
  crece se vuelve inútil en dos semanas. Tope de líneas + condensar cada día.
- **La cadencia vive en la memoria** ("CADENCIA VIGENTE: 3/día"), no
  hardcodeada en el comando. Así el usuario la cambia con una frase y el
  agente la respeta al día siguiente. En este jardín: **3 pushes curados
  ganan a 20** — más volumen solo diluye.
- **El primer `send_at` del día ≥ 60 min después de la corrida** — margen
  para que el hosting deploye las páginas que las notificaciones linkean.
- **Cada notificación a un destino distinto.** Repetir destino en el mismo
  día fue la queja #1 del usuario.
- **`expires_at` el mismo día** (~22:00 local). Un push trasnochado quema
  confianza.

---

## 4. Componente 3 — La Routine (el scheduler)

Una **Routine de Claude Code** es un trigger programado que abre una sesión
en tu entorno remoto (el repo ya clonado) y le manda un prompt. Es lo que
convierte el comando en un agente *diario* sin que toques nada.

### Cómo crearla (claude.ai/code)

1. Abrí [claude.ai/code](https://claude.ai/code) y asegurate de tener un
   **entorno** con el repo de la app como source (el mismo desde el que
   trabajás en sesiones web).
2. Andá a **Routines** (o pedíselo a Claude en una sesión del entorno:
   *"creá una routine diaria a las 06:00 America/Montevideo que corra
   /engagement en una sesión nueva"* — Claude usa su tool `create_trigger`).
3. Configuración recomendada:
   - **Cron:** `0 6 * * *` hora de Montevideo (= `0 9 * * *` UTC; verificá
     cómo interpreta la zona tu configuración — si el cron es UTC, calculá
     el offset: UY = UTC-3 todo el año, sin DST).
   - **Sesión nueva por corrida** (fresh session): cada día arranca limpio;
     toda la memoria que importa está en `learnings.md`, no en el chat.
   - **Prompt:** literalmente `/engagement` (o `/engagement` + una línea de
     contexto fijo si tu comando lo necesita).
4. La primera semana, revisá las sesiones que deja la Routine: el reporte
   final del agente (datos de ayer, decisiones, pushes de hoy, SHA) es tu
   ventana de control sin intervenir.

### Por qué a las 06:00

El agente corre **antes** de la primera ventana de envío (acá 07:00–20:30).
Le da tiempo a: leer el feedback de anoche, construir las experiencias,
pushear, que el hosting deploye, y que el primer push del día (≥60 min
después) linkee a páginas que ya existen.

### Alternativa sin Routines

Si no usás Claude Code web: un workflow de GitHub Actions con cron que corra
`claude -p "/engagement"` (Claude Code headless con `ANTHROPIC_API_KEY` como
secret), o correrlo a mano cada mañana. La Routine es la opción cero-fricción
porque hereda el entorno, los permisos y el historial de sesiones.

---

## 5. Componente 4 — Las páginas de experiencia

Cada experiencia es **un HTML standalone efímero** con contrato fijo. Del
contrato depende todo el loop: sin botones de decisión no hay señal, sin
link de vuelta el usuario queda varado, sin registro en `proposals.json` el
agente de mañana no sabe qué juzgar.

### Contrato obligatorio

```html
<!DOCTYPE html><html lang="es-UY"><head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>🎤 Nombre de la experiencia</title>
  <style>/* TODO inline. Mobile-first. Paleta de TU app. Sin frameworks. */</style>
</head><body>

  <!-- 1) PRIMER elemento visible: escape al sitio estable. Sin excepciones. -->
  <a class="back" href="https://TU-APP/index.html">← Volver al sitio estable</a>

  <!-- 2) El contenido: anclado en DATOS REALES de la app, verificados. -->
  ...

  <!-- 3) Reacción granular al final del contenido -->
  <div class="react">
    ¿Te voló la cabeza?
    <button onclick="engageReact('<slug>','love',this)">😍</button>
    <button onclick="engageReact('<slug>','like',this)">🙂</button>
    <button onclick="engageReact('<slug>','meh',this)">😐</button>
    <button onclick="engageReact('<slug>','no',this)">🙅</button>
    <span class="react-hint"></span>
  </div>

  <!-- 4) CTA de compromiso (la señal que separa "lindo" de "lo quiero") -->
  <div class="cta">
    ¿Querés recibir esto todos los días?
    <button onclick="engageAnswer('<slug>-suscripcion-diaria','si',this)">Sí, todos los días</button>
    <button onclick="engageAnswer('<slug>-suscripcion-diaria','no',this)">No hace falta</button>
    <span class="q-hint"></span>
  </div>

  <!-- 5) Bloque de decisión de la proposal (permanencia) -->
  <div class="engage-actions">
    <button onclick="engageApprove('<YYYY-MM-DD>-<slug>')">✅ Aprobar esta mejora</button>
    <button onclick="engageRejected('<YYYY-MM-DD>-<slug>')">✕ No me interesa</button>
  </div>

  <script src="engage.js"></script>
</body></html>
```

Y su registro en `proposals.json`:

```json
{
  "id": "2026-07-02-confesiones",
  "title": "🎤 Confesiones (news-feed 1ª persona + humor)",
  "page": "engage/2026-07-02-confesiones.html",
  "created": "2026-07-02",
  "status": "pending",
  "hypothesis": "La voz en 1ª persona + humor + vulnerabilidad convierte amor→suscripción tan bien como el chisme. Qué espero que pase y por qué.",
  "notified_by": ["2026-07-02-a"],
  "result_notes": null
}
```

### El ciclo de vida (regla dura)

```
creada (pending) ──usuario toca "Aprobar"──▶ promoted  → se integra al sitio real
       │
       ├──usuario toca "No me interesa"───▶ dropped   → git rm + hipótesis del fracaso en learnings
       │
       └──pasa 1 día sin aprobación───────▶ dropped   → git rm (efímera por default)
```

**Efímera por default** es lo que mantiene el sitio limpio: solo sobrevive lo
que el usuario pidió explícitamente. La aprobación es el único pase a
permanencia.

### La página "pitch" (opcional, para evaluar features como producto)

Por cada experiencia el agente puede generar un segundo HTML
(`<slug>-pitch.html`) con el caso de negocio: para quién es, por qué
engancharía, y 6 modelos de monetización (3 realistas + 3 ultra-creativos).
Sirve para evaluar la experiencia como *feature candidata de producto*, no
solo como contenido. Linkeala discretamente desde la experiencia.

---

## 6. Componente 5 — Tracking de feedback (medir sin backend)

`engage.js` (copiá el de este repo y ajustá 4 constantes) captura:

| Evento | Cuándo | Qué te dice |
|---|---|---|
| `notification_clicked` | llega con `?nid=` en la URL (dedup por nid) | qué push convirtió |
| `page_visit` | cada carga (throttle 1/hora si es visita directa) | alcance real |
| `dwell` + `scroll_pct` | al ocultar/cerrar la página | retención: 208s/100% ≠ 23s/10% |
| `reaction` | botones 😍/🙂/😐/🙅 | sentimiento granular |
| `answer` | CTAs sí/no (suscripción diaria, preguntas de estado) | compromiso e info que no podés observar |
| `proposal_approved/rejected` | botones de decisión | permanencia |
| `push_unsubscribe` | control de desuscripción (auto-inyectado al pie) | fatiga — respetalo YA |

Dos patrones no negociables (los dos costaron feedback perdido):

1. **Outbox en localStorage.** El evento se guarda SINCRÓNICO en
   localStorage ANTES de intentar mandarlo, con flush reintentable, dedup
   por id y reintento al volver a foco. En mobile, un `fetch` disparado justo
   antes de minimizar la app NO completa — sin outbox perdés casi todo.
2. **Badge de sync honesto.** Un cartelito fijo que muestra
   "⏳ Sincronizando N…" / "⚠️ No se pudo guardar" / "✓ Sincronizado". Un
   botón que dice "Guardado" cuando no guardó, miente y envenena tus datos.

### Dónde persiste el feedback

- **Opción A (la que usa este repo, recomendada): serverless function.**
  `api/feedback.js` en Vercel recibe `POST {events, device}` y hace GET+PUT
  de `sync/engagement.json` vía GitHub API con un token **del lado del
  servidor** (env var `GH_FEEDBACK_TOKEN`, fine-grained, solo
  Contents:write de ese repo). El browser no necesita ningún PAT →
  funciona desde cualquier dispositivo sin configurar nada.
- **Opción B: PAT en localStorage** (como el sync engine del jardín). Sirve
  para un solo usuario/dispositivo; más fricción de setup.

En GitHub Pages puro (sin Vercel) usá la opción B, o montá solo la function
de feedback en un proyecto Vercel gratis apuntando al mismo repo.

---

## 7. Componente 6 — La memoria (`learnings.md`)

El archivo más importante del sistema. Estructura probada:

```markdown
# Learnings del agente
## ⏱️ CADENCIA VIGENTE: <N pushes/día — quién la fijó y cuándo>
## 🚀 SÍNTESIS: qué formato/ángulo convierte (evidencia medida, no vibes)
   - CONVIERTEN: ... (con números: dwell, reacción, suscripción, aprobación)
   - TIBIOS: aprueban pero no suscriben — qué patrón comparten
   - RECHAZADOS: no relanzar
   - Regla operativa para elegir el próximo ángulo
## 📊 Estado del sistema: suscripción activa?, cutoff de datos, compactaciones
## 🔭 Corrida de HOY: qué se decidió, qué se apostó, qué mirar mañana
## Contexto real de la app (estación, qué hay de nuevo en los datos)
## TODO / ángulos sin usar
```

Reglas: máximo ~150 líneas, se **reescribe** cada corrida, y toda afirmación
de "esto funciona" lleva el dato que la respalda. La sección "Corrida de HOY"
es el handoff al agente de mañana.

---

## 8. Exprimir los assets — ejemplos detallados

El contenido que convierte **se ancla en datos reales y específicos** de la
app. Genérico = ignorado. Este es el hallazgo central medido en este jardín
(léelo como tabla de sustitución para tu app):

### 8.1 Qué ángulos convierten (evidencia real de este sistema)

| Ángulo | Ejemplo en el jardín | Resultado medido |
|---|---|---|
| **1ª persona / red social** | "📱 Feed": las plantas postean como cuentas que podés 'seguir' | 😍×2, suscripción×2, dwell récord 208s — el ganador absoluto |
| **Identidad** ("¿cuál sos vos?") | "🔮 Horóscopo del jardín" | 😍 + suscripción + 115s/100% |
| **Chisme / tabloide** | "🍵 Chusmerío": escándalos botánicos reales | suscripción + 86s — se reenvía solo |
| **Orgullo / superlativos** | "🏆 Récords: tu árbol más viejo, tu flor más rara" | 😍 + suscripción + 141s |
| **Editorial / novedad** | "📰 El Diario del Jardín — edición de hoy" | 😍 + suscripción + 92s |
| Utilidad accionable | "🧪 Superpoderes: usos prácticos de tus plantas" | aprueba pero 'meh', 23s, SIN suscripción |
| Consejo sincero / calidez | "💌 Consultorio" | mismo patrón tibio que la utilidad |
| Geografía / orígenes | "🗺️ Pasaporte" | RECHAZADO aun leído entero |

**Regla operativa:** apuntar a IDENTIDAD, PERTENENCIA, HUMOR, ORGULLO,
1ª PERSONA, CHISME. La utilidad y el consejo sincero ganan aprobación tibia
pero no suscripción — si querés dar valor útil, **envolvelo en humor o
chisme**, no lo entregues como consejo directo.

Otros hallazgos transferibles: los juegos buenos **se queman con el uso
seguido** (rotá con 3-4 días de descanso); las herramientas (mapas,
dashboards, calendarios) pierden contra el contenido emocional; las mecánicas
lentas (flip-cards, memory) mueren; el contenido verificado con datos
concretos es lo más resiliente a largo plazo.

### 8.2 Anatomía de un buen push

```json
{
  "id": "2026-07-02-a",
  "title": "🎤 Tu jardín confiesa",
  "body": "El palto te ocultó algo 8 años. Hoy habla. 9 confesiones verificadas de tus plantas.",
  "url": "https://TU-APP/engage/2026-07-02-confesiones.html",
  "send_at": "2026-07-02T08:30:00-03:00",
  "expires_at": "2026-07-02T22:00:00-03:00",
  "status": "pending", "sent_at": null, "fail_reason": null,
  "created_by": "engagement-agent 2026-07-02"
}
```

- **title ~40 chars con gancho; body ~110 chars concreto.**
- **El copy cumple lo que promete su destino** — si decís "9 confesiones",
  la página tiene 9 confesiones. Nunca linkear al home "a ver qué hay".
- Posesivo + dato específico gana: "**Tu** árbol más viejo tiene **600
  años** de linaje" > "Descubrí curiosidades".
- **No afirmar estados que no podés observar** ("tu árbol está pelado") —
  fraseá condicional o preguntalo con botones `engageAnswer` y guardá la
  respuesta como dato.
- Slots probados: 08:30 / 13:00 / 19:30 local. Ajustá con tus datos.

### 8.3 Inventario de assets → generador de ángulos

Antes del primer ciclo, hacé (o hacé que el agente haga) un inventario:

1. **Entidades** con nombre propio (plantas / tés / libros) — cuántas, qué
   campos tienen (origen, fecha, rareza, historia, foto).
2. **Datos verificables** por entidad (fun facts, records, relaciones entre
   entidades). El chisme y los récords salen de acá.
3. **Dimensión temporal** (estación, "un día como hoy", qué está "activo"
   ahora). Da frescura diaria sin inventar nada.
4. **Lo del usuario** (sus fotos, su historial, sus elecciones). Todo lo
   posesivo convierte mejor que lo enciclopédico.
5. **Preguntas que no podés responder solo** → CTAs `engageAnswer` que
   convierten al usuario en sensor de su propio sistema.

Cruzá inventario × ángulos ganadores y tenés meses de experimentos:
horóscopo de X, chusmerío de X, récords de X, X habla en 1ª persona,
el diario de X, confesiones de X, romances de X…

---

## 9. Checklist de replicación (app nueva)

- [ ] Web Push funcionando de punta a punta (`WEB_PUSH_PLAYBOOK.md` §10)
- [ ] `engage.js` adaptado (repo, paths, claves de localStorage propias)
- [ ] Persistencia de feedback: `api/feedback.js` (Vercel) o PAT fallback
- [ ] `engage/proposals.json` (`{"proposals": []}`) y `engage/learnings.md`
      inicial con la CADENCIA VIGENTE y el inventario de assets (§8.3)
- [ ] `.claude/commands/engagement.md` adaptado a la app (objetivo, datos
      reales a leer, reglas de contenido, URL del sitio estable)
- [ ] Routine diaria en claude.ai/code → `/engagement`, sesión nueva, ~06:00
- [ ] Primer ciclo a mano: 1 experiencia + 2-3 pushes, verificar el loop
      completo (push → click → evento en engagement.json → el agente lo lee)
- [ ] Regla de efimeridad activa: proposal sin aprobar = borrada mañana

---

## 10. Prompt específico — findmetea.com

Pegá esto en una sesión de Claude Code sobre el repo de findmetea
(idealmente después de leer este playbook y `WEB_PUSH_PLAYBOOK.md`, que
conviene copiar al repo destino):

```
Quiero implementar en findmetea.com el sistema de "experiencias diarias con
Routine" documentado en EXPERIENCIAS_DIARIAS_PLAYBOOK.md y
WEB_PUSH_PLAYBOOK.md (copiados a este repo). Objetivo: que cada mañana un
agente construya experiencias efímeras sobre mi catálogo de tés, me las
mande por push al teléfono, mida qué me engancha y adapte al día siguiente.

CONTEXTO DE LA APP
- findmetea.com: recomendador de tés. Next.js (detectá si es SSG/export
  estático o server), deploy actual en producción — averiguá el hosting
  antes de tocar nada y adaptá el playbook: si es Vercel, sw.js e íconos
  van en public/, la queue puede vivir en public/notifications/ y el
  feedback usa una API route nativa de Next (en vez de api/feedback.js
  suelto); el dispatcher de GitHub Actions no cambia.
- Assets: ~140 tés con origen (23+ países), tipo (verde/blanco/oolong/
  negro/herbal/mate), temperaturas y tiempos de infusión, tags
  descriptivos; escenarios por momento del día y por objetivo (dormir,
  energía, foco, digestión); sección de fun facts (L-teanina, historia,
  botánica); bilingüe EN/ES.

FASES (en orden, commiteando por fase)
1. AUDITORÍA: inventario de assets según §8.3 del playbook — entidades,
   datos verificables por té, dimensión temporal (momento del día ES la
   dimensión natural de esta app), qué es posesivo/personalizable, qué
   preguntas podrían responderse con botones. Guardalo como la sección
   "Inventario" del learnings.md inicial.
2. CAPA PUSH: implementar el checklist §10 de WEB_PUSH_PLAYBOOK.md
   adaptado al hosting detectado. Botón "Activar notificaciones" discreto.
   Probar de punta a punta con un push de send_at pasado antes de seguir.
3. TRACKING: portar engage.js (claves de localStorage con prefijo
   findmetea_, outbox + badge de sync honesto) y el endpoint de feedback.
4. AGENTE: crear .claude/commands/engagement.md siguiendo la anatomía del
   §3 del playbook, con estas especificidades:
   - Objetivo: que yo abra la app y descubra tés que no conocía.
   - Cadencia inicial: 3 pushes/día (08:30 / 13:00 / 19:30 hora
     America/Montevideo), expires_at mismo día 22:00, timestamps -03:00.
   - Idioma del contenido: español rioplatense (la app es bilingüe pero
     yo soy el único usuario del canal push).
   - Política de contenido: cada push anclado en un té REAL del catálogo
     con sus datos verificados; prohibido inventar propiedades de salud;
     el momento del día del push debe ser coherente con el té (nada de
     matcha a las 19:30).
   - Ángulos iniciales a testear (del §8.1 — identidad/humor/chisme/
     orgullo/1ª persona; evitar utilidad pura y consejo sincero):
     "🔮 Horóscopo del té" (qué té sos hoy), "🍵 Chusmerío de la tetera"
     (escándalos reales de la historia del té: espionaje del té, monopolios,
     el robo de Robert Fortune), "🏆 Récords del catálogo" (el té más raro,
     el país más improbable), "📱 Feed" (los tés postean en 1ª persona),
     "📰 El Diario del Té — edición de hoy", "🎤 Confesiones de la alacena".
   - Experiencias efímeras en un dir engage/ del directorio publicado, con
     el contrato completo del §5 (back-link primero, reacción, CTA
     suscripción diaria, Aprobar/No me interesa, pitch page opcional).
5. ROUTINE: dejame escritas las instrucciones exactas para crear la
   Routine diaria (~06:00 UY, sesión nueva, prompt "/engagement") y NO la
   crees vos — la activo yo.
6. PRIMER CICLO MANUAL: generá la primera experiencia (elegí el ángulo con
   mejor prior: horóscopo o chusmerío), encolá los 3 pushes de mañana y
   dejá learnings.md inicializado con cadencia, inventario e hipótesis.

REGLAS DURAS
- Nada de frameworks nuevos ni dependencias runtime; las experiencias son
  HTML standalone con CSS inline usando la paleta de findmetea.
- Secretos jamás al repo (VAPID privada = secret de Actions; token de
  feedback = env var del hosting).
- No romper nada del sitio actual: todo lo nuevo es aditivo.
- Cada afirmación sobre un té debe salir de los datos del repo o de una
  fuente verificada; si no está verificado, no se publica.
```

**Nota previa:** findmetea es Next.js — la única adaptación real del
playbook es *dónde viven los archivos publicados* (`public/`) y *cómo se
sirve el endpoint de feedback* (API route). El resto (VAPID, dispatcher,
queue, contrato de experiencias, agente, Routine) es idéntico.

---

## 11. Prompt específico — Biblioteca (abecedeefege.github.io/Biblioteca)

```
Quiero implementar en este repo (Biblioteca — mi catálogo visual de ~400
libros en GitHub Pages) el sistema de "experiencias diarias con Routine"
documentado en EXPERIENCIAS_DIARIAS_PLAYBOOK.md y WEB_PUSH_PLAYBOOK.md
(copiados a este repo). Objetivo: que un agente diario me haga redescubrir
mi propia biblioteca — libros que tengo y olvidé, conexiones entre ellos,
ganas de agarrar uno esta noche.

CONTEXTO DE LA APP
- Sitio estático en GitHub Pages, sin framework, servido bajo el path
  /Biblioteca/ — OJO con eso en toda la capa push: registrá el sw.js con
  scope relativo al path, los íconos y notifications/ van dentro del
  directorio publicado, y los deep links son URLs absolutas bajo
  https://abecedeefege.github.io/Biblioteca/.
- Catálogo: ~400 volúmenes organizados por estantería física (3 columnas ×
  8 estantes, pared oeste como foco), géneros: clásicos encuadernados,
  misterio, ciencia, arte, genealogía, y una colección grande de Stephen
  King en español. Averiguá primero CÓMO están modelados los datos (¿hay
  JSON/JS con los libros? ¿o solo imágenes?): si el catálogo no tiene
  metadata estructurada por libro, la FASE 1 incluye proponerme un
  data_books con los campos mínimos (título, autor, año, género, estante,
  estado de lectura) y poblarlo con lo que se pueda extraer del repo,
  marcando lo no verificado para que yo lo complete.

FASES (en orden, commiteando por fase)
1. AUDITORÍA + DATOS: inventario según §8.3 del playbook. La dimensión
   posesiva acá es máxima (TODOS los libros son míos): explotala. Datos
   verificables por libro: autor, año, historia de la edición, premios,
   adaptaciones, muertes trágicas de autores, rivalidades literarias.
   Preguntas engageAnswer naturales: "¿este lo leíste?", "¿sigue en este
   estante?", "¿lo prestaste?" — cada respuesta enriquece el catálogo.
2. CAPA PUSH: checklist §10 de WEB_PUSH_PLAYBOOK.md sobre GitHub Pages
   (dispatcher de Actions en este mismo repo). Para el feedback, como
   Pages no tiene serverless: opción PAT en localStorage (soy un solo
   usuario) o un proyecto Vercel mínimo solo para /api/feedback apuntando
   a este repo — proponeme una y justificá.
3. TRACKING: engage.js con prefijo biblioteca_ en las claves, outbox +
   badge de sync honesto.
4. AGENTE: .claude/commands/engagement.md según §3 del playbook:
   - Objetivo: que agarre un libro físico esta noche. El CTA estrella no
     es solo "suscripción diaria": es "¿lo vas a leer? Sí/Ya lo leí/No"
     (engageAnswer) — esa respuesta es oro para personalizar.
   - Cadencia inicial: 2 pushes/día (08:30 y 20:30 -03:00 — el slot
     nocturno es EL slot de biblioteca: "¿qué leés esta noche?").
     expires_at mismo día 23:00.
   - Contenido en español rioplatense.
   - Ángulos iniciales (§8.1 — identidad/chisme/orgullo/1ª persona;
     evitar reseña sincera y utilidad tipo "cómo organizar tu biblioteca"):
     "🍷 Chusmerío de la estantería" (escándalos reales de mis autores:
     plagios, feudos, seudónimos), "🏆 Récords de mi biblioteca" (el más
     viejo, el más largo, el más raro), "📱 Feed" (mis libros postean en
     1ª persona: "hace 6 años que nadie me abre"), "🎤 Confesiones del
     estante 3", "🔮 Horóscopo lector" (qué libro tuyo sos hoy),
     "🕯️ Un día como hoy" (efemérides de MIS autores), "💘 Romances de
     estantería" (qué libros míos se amarían entre sí).
   - Regla de honestidad: no afirmar que un libro está en X estante o
     leído/no-leído si el dato no está — preguntarlo con botones.
   - Experiencias efímeras en engage/ con el contrato completo del §5.
5. ROUTINE: instrucciones exactas para crear la Routine diaria (~06:00
   UY, sesión nueva, "/engagement"); no la crees vos.
6. PRIMER CICLO MANUAL: primera experiencia (prior más fuerte para
   biblioteca: "Feed de libros abandonados en 1ª persona" — culpa +
   humor + posesivo) + cola de mañana + learnings.md inicial.

REGLAS DURAS
- GitHub Pages manda: no cambiar la estructura publicada, no build steps
  nuevos obligatorios, todo estático.
- HTML standalone con CSS inline para cada experiencia, estética acorde a
  una biblioteca (serif, papel, madera) pero mobile-first.
- Secretos jamás al repo. Datos de libros: solo lo verificable; lo dudoso
  se pregunta, no se afirma.
- Todo aditivo: el catálogo visual actual queda intacto.
```

---

## 12. Prompt específico — Psicologeando

Este prompt asume que lo pegás en una sesión de Claude Code **sobre el repo
de Psicologeando**. Como la app no está publicada en una URL que el agente
pueda inspeccionar de antemano, arranca con una fase de auto-descubrimiento
— y como el dominio es psicología, lleva reglas de privacidad reforzadas:
**todo lo que entra a `queue.json` o a una página de experiencia queda
público en el repo**, así que nada personal ni clínico puede tocar el canal.

```
Quiero implementar en este repo (Psicologeando) el sistema de "experiencias
diarias con Routine" documentado en EXPERIENCIAS_DIARIAS_PLAYBOOK.md y
WEB_PUSH_PLAYBOOK.md (copiados a este repo). Objetivo: que un agente diario
me sorprenda con contenido de psicología anclado en MI app — que la abra,
aprenda algo que no sabía y quiera volver mañana.

FASE 0 — DESCUBRIMIENTO (antes de tocar NADA)
Auditá el repo y reportame en el primer commit (docs/AUDIT.md o similar):
- Qué es la app exactamente: qué pantallas tiene, qué datos modela
  (¿conceptos/sesgos/autores? ¿notas o registros personales? ¿tests?
  ¿diario emocional?), dónde viven los datos (JSON/JS/HTML hardcodeado),
  y si hay estado de usuario en localStorage.
- Hosting y estructura publicada (GitHub Pages con path /Psicologeando/,
  Vercel, otro) — de esto depende cómo adaptar la capa push: scope del
  sw.js, dónde va notifications/, URLs absolutas de los deep links, y si
  el feedback puede ser serverless o va con PAT en localStorage.
- CLASIFICÁ los datos en dos pilas: (a) contenido de conocimiento público
  (conceptos, autores, experimentos, sesgos) — utilizable en pushes y
  experiencias; (b) datos personales/sensibles (estados de ánimo, notas,
  registros propios) — PROHIBIDOS en el canal push y en páginas del repo;
  como mucho, referenciables de forma abstracta ("tenés registros sin
  completar esta semana") y solo si yo lo apruebo explícitamente.

FASES (en orden, commiteando por fase)
1. AUDITORÍA DE ASSETS: inventario según §8.3 del playbook sobre la pila
   (a): entidades con nombre propio, datos verificables, dimensión
   temporal (efemérides de la psicología, "un experimento como hoy"),
   qué es posesivo (mi progreso, mis conceptos vistos), y qué preguntas
   engageAnswer tienen sentido. Guardalo en el learnings.md inicial.
2. CAPA PUSH: checklist §10 de WEB_PUSH_PLAYBOOK.md adaptado al hosting
   detectado en la fase 0. Probar de punta a punta antes de seguir.
3. TRACKING: engage.js con prefijo psicologeando_ en las claves de
   localStorage, outbox + badge de sync honesto, y el endpoint de
   feedback según el hosting (serverless si hay; si no, PAT).
4. AGENTE: .claude/commands/engagement.md según §3 del playbook:
   - Objetivo: aprendizaje con deleite — que cada push me enseñe algo
     real de psicología conectado con lo que la app ya contiene.
   - Cadencia inicial: 2 pushes/día (08:30 y 19:30 -03:00, hora
     America/Montevideo), expires_at mismo día 22:00. Empezar más suave
     que el jardín: el contenido de aprendizaje satura más rápido.
   - Contenido en español rioplatense.
   - Ángulos iniciales (§8.1 — identidad/humor/chisme/orgullo/1ª persona;
     evitar el tono manual-de-autoayuda y el consejo sincero, que miden
     tibio): "🔮 Horóscopo cognitivo" (qué sesgo sos hoy — identidad),
     "🍷 Chusmerío de la psicología" (feudos reales: Freud vs. Jung,
     los escándalos de los experimentos famosos, Milgram, Zimbardo),
     "🏆 Récords de la mente" (superlativos verificados de la cognición),
     "📱 Feed" (los sesgos y conceptos postean en 1ª persona: "soy el
     sesgo de confirmación y hoy te acompañé 14 veces"), "🎤 Confesiones
     de un experimento", "🕯️ Un día como hoy en la psicología".
   - Política de contenido: TODO dato afirmado verificado contra una
     fuente; los experimentos citados con año y autor reales; prohibido
     diagnosticar, patologizar o dar consejo clínico — esto es
     divulgación con humor, no terapia. Y la regla de la fase 0: nada
     personal/sensible sale al canal.
   - Experiencias efímeras en engage/ con el contrato completo del §5
     (back-link primero, reacción, CTA suscripción diaria,
     Aprobar/No me interesa).
5. ROUTINE: instrucciones exactas para crear la Routine diaria (~06:00
   UY, sesión nueva, "/engagement"); no la crees vos.
6. PRIMER CICLO MANUAL: primera experiencia (prior más fuerte: "Horóscopo
   cognitivo" — identidad es el eje que mejor convierte) + cola de mañana
   + learnings.md inicial con cadencia, inventario e hipótesis.

REGLAS DURAS
- Privacidad primero: datos personales/clínicos/emocionales míos JAMÁS en
  queue.json, en páginas de engage/ ni en learnings.md — todo eso es
  público en el repo.
- HTML standalone con CSS inline por experiencia, paleta de la app,
  mobile-first, sin frameworks nuevos.
- Secretos jamás al repo (VAPID privada = secret de Actions).
- Todo aditivo: la app actual queda intacta.
- Sin afirmaciones psicológicas inventadas: si no está verificado con
  fuente, no se publica.
```

---

## 13. Prompt específico — LunesDeUNO (abecedeefege.github.io/LunesDeUNO)

Acá el sistema cambia de forma: LunesDeUNO no es un catálogo para
redescubrir sino un **ritual semanal con personas reales** (partidas de UNO
de los lunes, tabla a 500, castigos tipo "debe postre/picada"). La cadencia
correcta no es N pushes/día — es una **semana editorial anclada al lunes**.
Los ángulos ganadores (chisme, orgullo, identidad, 1ª persona) acá tienen
esteroides porque el chisme es sobre gente real de tu mesa.

```
Quiero implementar en este repo (LunesDeUNO — tracker de nuestras partidas
de UNO de los lunes: tabla acumulada a 500, historial de partidas,
castigos/deudas tipo "Tano debe postre por perder el 23 de junio", fotos)
el sistema de "experiencias con Routine" documentado en
EXPERIENCIAS_DIARIAS_PLAYBOOK.md y WEB_PUSH_PLAYBOOK.md (copiados a este
repo), ADAPTADO a cadencia semanal. Objetivo: que la semana gire alrededor
del lunes — anticipación antes, épica después — y que las deudas no se
olviden jamás.

CONTEXTO DE LA APP
- Sitio estático en GitHub Pages bajo el path /LunesDeUNO/ — mismo
  cuidado que con cualquier Pages: sw.js con scope relativo al path,
  notifications/ dentro del directorio publicado, deep links absolutos
  bajo https://abecedeefege.github.io/LunesDeUNO/. Auditá primero cómo
  están modelados los datos (¿scores y historial en JSON/JS? ¿en
  localStorage? ¿fotos dónde?): el agente necesita leer la tabla, el
  historial de partidas y las deudas para generar contenido real.
- Los jugadores son personas reales y el sitio es público: usar SOLO los
  apodos que ya aparecen en la app, jamás apellidos/teléfonos/datos
  personales. El tono del chisme es interno-cariñoso, nunca hiriente:
  celebrar y picantear, no humillar.

FASES (en orden, commiteando por fase)
1. AUDITORÍA: inventario según §8.3 — jugadores, tabla acumulada, rachas,
   historial con fechas, deudas activas y saldadas, fotos. Derivá stats
   que hoy no se muestran: quién ganó más lunes seguidos, la remontada
   más grande, la deuda más vieja impaga, el "rival histórico" de cada
   uno. Eso es el combustible de todo el contenido.
2. CAPA PUSH: checklist §10 de WEB_PUSH_PLAYBOOK.md sobre GitHub Pages
   (dispatcher de Actions en este repo). Feedback: PAT en localStorage o
   proyecto Vercel mínimo para /api/feedback — proponeme una y justificá.
   NOTA multi-dispositivo: el playbook guarda UNA suscripción; si más
   adelante los demás jugadores quieren recibir pushes, extendé
   subscription.json a un array de suscripciones y que el dispatcher
   itere (invalidando individualmente los endpoints muertos). Arrancá
   solo conmigo.
3. TRACKING: engage.js con prefijo lunesdeuno_ en las claves, outbox +
   badge de sync honesto.
4. AGENTE + CADENCIA SEMANAL: .claude/commands/engagement.md según §3
   del playbook, pero con SEMANA EDITORIAL en vez de N/día:
   - LUNES 10:00 — previa de la partida: "🔥 Hoy se juega. Tano defiende
     la punta / la deuda de X cumple N días" → experiencia "La Previa"
     (tabla actual + qué se juega hoy + pronóstico en broma).
   - MARTES 09:00 — crónica del lunes: recap épico de la partida de
     anoche escrito como periodismo deportivo (si hay datos nuevos en el
     historial; si nadie cargó la partida, el push es "¿anoche se jugó?
     Cargá el resultado" con deep link al form de la app).
   - JUEVES 19:30 — contenido de mitad de semana rotando ángulos:
     "🍿 Chusmerío de la mesa" (rachas, deudas impagas con días
     contados, rivalidades históricas — TODO con datos reales de la
     tabla), "🏆 Récords del grupo", "🔮 Horóscopo unístico" (qué carta
     sos esta semana), "📱 Feed" (las cartas o los jugadores postean en
     1ª persona), "🎤 Confesiones del mazo".
   - DOMINGO 20:00 — teaser de la previa: "Mañana es lunes. La tabla
     dice X. ¿Va postre o picada?"
   - Timestamps -03:00, expires_at el mismo día ~23:00. Fuera de esos 4
     slots, silencio: acá el exceso mata el ritual.
   - Si el historial muestra que un lunes NO se jugó, la crónica del
     martes no se inventa: el agente lo registra y adapta ("semana de
     descanso — la tabla queda congelada").
   - Experiencias efímeras en engage/ con el contrato del §5. Las deudas
     son el mejor CTA engageAnswer del sistema: "¿Tano ya pagó el
     postre? Sí / Todavía no" — la respuesta actualiza el contenido de
     la semana siguiente.
5. ROUTINE: instrucciones para crear la Routine — acá conviene DIARIA
   igual (~06:00 UY, sesión nueva, "/engagement"): el agente corre cada
   día, lee qué día de la semana es y solo encola lo que toca según la
   semana editorial (la mayoría de los días no encola nada o compacta
   datos). No la crees vos.
6. PRIMER CICLO MANUAL: generá la experiencia de la próxima previa de
   lunes + el chusmerío del jueves con los datos reales de la tabla, y
   encolá la semana. learnings.md inicial con la semana editorial como
   CADENCIA VIGENTE.

REGLAS DURAS
- GitHub Pages manda: todo estático, nada que rompa la app actual.
- Solo apodos ya públicos en la app; cero datos personales; tono
  picante-cariñoso, jamás cruel — son mis amigos.
- Datos SIEMPRE reales de la tabla/historial: un chisme inventado sobre
  una persona real quema el canal para siempre.
- HTML standalone con CSS inline, estética de la app (o de revista
  deportiva/tabloide para las crónicas), mobile-first.
- Secretos jamás al repo.
```

---

## 14. Errores que ya pagamos (no los repitas)

1. **Escribir la cola a mano sin assert anti-duplicados** → dos pushes al
   mismo destino el mismo día → queja del usuario. Un destino por slot.
2. **Push que promete lo que la landing no tiene** → confianza quemada.
3. **Afirmar estados no observables** ("tu árbol está pelado") → preguntar
   con botones en vez de afirmar.
4. **Fiarse del cron de Actions para el timing** → deriva y saltea; el
   trigger `on: push` a la queue es el que da inmediatez.
5. **`fetch` de feedback sin outbox** → en mobile se pierde casi todo.
6. **Memoria que solo acumula** → a las 2 semanas el agente no encuentra
   la señal. Reescribir y condensar cada día.
7. **Features que nadie pidió acumulándose** → efímera por default; la
   aprobación explícita es el único pase a permanencia.
8. **Más pushes ≠ más engagement** → el usuario abre 2-3/día sin importar
   cuántos mandes; el resto diluye y sepulta lo nuevo.

---

*Generado a partir del sistema en producción de este repo (jardín,
Montevideo). Los números del §8.1 son mediciones reales de engagement.json
entre el 11/06 y el 02/07 de 2026.*
