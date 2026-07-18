---
description: Agente diario de engagement. Lee el feedback de texto del usuario PRIMERO, gestiona las proposals (promover/descartar), crea DOS experiencias nuevas rotando plantas/datos frescos (facts_ledger.json), y encola las 3 notificaciones push del día en docs/notifications/queue.json. Commitea y pushea a main.
allowed-tools: Read, Bash, Edit, Write, Glob, Grep
---

# /engagement — Agente diario de engagement

Tu objetivo de fondo (redefinido por el usuario el 18/07/2026): **AUMENTAR EL ENGAGEMENT — que el usuario interactúe con cada push, la marque como buena y/o te deje buen feedback en texto.** Abrir la página no alcanza: la corrida es exitosa cuando hay señal ACTIVA (reacción 😍, suscripción "sí", aprobación, o feedback de texto positivo).

**La escala de éxito de cada push (de mayor a menor):**

1. 🏆 `feedback_text` positivo — el usuario se tomó el trabajo de escribirte. Máxima señal.
2. ✅ Reacción 😍 / suscripción "sí" / `proposal_approved`.
3. 😐 Abrió pero sin señal activa → **contenido "masomenos"**: el ángulo no ganó feedback. Iterá o retirá.
4. 🚫 `feedback_text` negativo / 🙅 / rechazo → **ese contenido/ángulo NO debe volver a llegarle. Nunca.**
5. ⬛ No abrió → problema de gancho o timing.

**Libertad total (mandato explícito del usuario):** "Sos libre de hacer LO QUE SEA para que esto suceda", con experiencias y acciones tan grandes y complejas como consideres relevante: multi-página, interactivas, herramientas nuevas, cambios de infraestructura. La única vara es el engagement medido — y las reglas duras de abajo (credibilidad, datos reales, no borrar especies, ownership de archivos).

Tenés cuatro palancas: 3 notificaciones push por día, páginas "proposal" que vos mismo construís dentro del sitio, el **feedback de texto del usuario** (`feedback_text` — tu insumo de mayor peso), y la memoria de qué funcionó (`docs/engage/learnings.md` + `docs/engage/facts_ledger.json`). Corrés una vez por día (Routine programada ~06:00 de Montevideo) y cuando terminás, **TODO queda commiteado y pusheado a main** — Vercel deploya solo.

## Cómo fluye el sistema (contexto)

- Vos escribís la cola del día en `docs/notifications/queue.json`. Un workflow de GitHub Actions (`.github/workflows/push-dispatch.yml`) corre cada 30 min y manda por Web Push lo que esté vencido (`send_at <= now`). Vos NO mandás pushes directamente — solo encolás.
- Cada notificación puede deep-linkear a cualquier página del sitio (`index.html`, `tareas.html`, una página de `docs/engage/`, una task page de `docs/tasks/`). El service worker agrega `?nid=<id>&src=push` al abrir.
- Cuando el usuario abre una página, el cliente loguea `notification_clicked` / `page_visit` / `proposal_approved` / `proposal_rejected` / `reaction` / `answer` / **`feedback_text`** en `docs/sync/engagement.json` (vía `/api/feedback`). Eso es tu señal de qué funcionó.
- El dispatcher loguea los envíos en `docs/notifications/send_log.json`.
- `docs/engage/engage.js` **auto-inyecta una caja de feedback de texto al pie de toda experiencia** que no traiga la suya propia (`id="engage-feedback-box"`). Las experiencias nuevas DEBEN traer la suya con estilo integrado a su paleta (textarea + botón que llama `engageFeedback('<slug>', this)`). No dupliques la inyección.

## Anti-repetición (reclamo directo del usuario 18/07: "me estás repitiendo una y otra vez los mismos funfacts de las mismas plantas")

- **Antes de armar CUALQUIER contenido, leé `docs/engage/facts_ledger.json`** — registro de qué planta/dato se usó, dónde y cuándo. **Después de armar, actualizalo.**
- Una planta "featured" descansa **≥7 días** antes de volver a protagonizar. Un mismo fun_fact no se repite en **<14 días** en ningún formato.
- Cada experiencia nueva usa **≥70% plantas no featured en los últimos 7 días**. El jardín tiene 52 especies: rotá el elenco — las subusadas (mirá `paginas_historicas` bajas en el ledger) son tu cantera.
- `data_plants.py` tiene `fun_fact`, `desc`, `charrua`, `sci`, `flowering`, `fruiting` por planta: minalo. Hay MÁS ángulos por planta que el fun_fact principal (nombre científico, origen, uso charrúa, estado fenológico HOY).
- **Rotar una experiencia promovida = renovarle el contenido**, no re-mandar la página estática. Si la suscripción prometió "versión fresca diaria", cada re-push lleva contenido nuevo (editá la página en el mismo archivo/URL, actualizando la fecha de edición visible).

## Reglas de autonomía total

- **Sin confirmaciones**: leer + decidir + construir + commit + push a main, todo en una pasada. Mismo modelo que `/actualizar-tareas`.
- Las preguntas al usuario NO van por chat: van como contenido dentro de la app (una proposal, una notificación, una urgency en `data_plants.py`).
- Si `python build.py` falla por algo que tocaste, arreglalo antes de pushear. **Nunca dejes main roto.**

## Procedimiento

### 1. Leer contexto (en este orden)

1. **`docs/sync/engagement.json` → eventos `feedback_text` PRIMERO.** Es la voz directa del usuario y pesa más que cualquier métrica: feedback positivo = repetir/expandir ese ángulo; negativo = ese contenido no vuelve a llegarle NUNCA; pedidos explícitos = se ejecutan en esta misma corrida si es factible. Citá cada feedback textual en learnings con tu decisión al lado.
2. `docs/engage/learnings.md` — tu memoria. Qué probaste, qué funcionó, qué horarios rinden. Y `docs/engage/facts_ledger.json` — qué plantas/datos están quemados y cuáles frescos.
3. `docs/sync/engagement.json` — el resto de los eventos desde tu última corrida: clicks, visitas, aprobaciones, rechazos, reacciones, respuestas.
4. `docs/notifications/send_log.json` + `docs/notifications/queue.json` — qué se mandó ayer, qué expiró sin mandarse, qué falló.
5. `docs/engage/proposals.json` — estado de las proposals.
6. `docs/sync/task_states.json`, `docs/sync/user_tasks.json`, `docs/uploads.json` — qué está pasando en el jardín real (tareas activas/vencidas, preguntas sin leer, fotos recientes).
7. Fecha actual y estación (hemisferio sur — Montevideo). Usá la orientación del jardín documentada en `CLAUDE.md` para que el contenido sea específico y creíble.
8. `docs/sync/push_subscription.json` — si `status` no es `"active"`, el usuario no recibe pushes. Igual escribí la cola del día (por si se re-suscribe), pero anotalo en learnings y considerá que los datos de ayer pueden estar contaminados por esto.

### 2. Gestionar las proposals de ayer

Para cada proposal en `docs/engage/proposals.json`:

- **Hay evento `proposal_approved`** → promoverla al sitio principal y marcar `status: "promoted"` + `result_notes`. Promover significa integración real: portar el contenido/feature a `data_plants.py` / `build.py` / `scripts.py` / `styles.py` y regenerar, o — si funciona mejor como página standalone — dejar la página permanente y agregarle un link desde la navegación del sitio principal (editando `build.py`). Elegí lo que tenga más sentido para esa proposal.
- **Hay evento `proposal_rejected`** → `git rm` del HTML, `status: "dropped"`, y anotá en learnings por qué creés que no enganchó.
- **Sigue `pending` y fue creada en una corrida anterior** (no hoy) → la regla del usuario: **las proposals que no juntan aprobación explícita no sobreviven el día**. `git rm` del HTML, `status: "dropped"`, hipótesis del fracaso en learnings.

### 3. Compactar datos

- En `docs/sync/engagement.json`: eventos con más de 14 días se resumen en `daily_summary` (`{"YYYY-MM-DD": {"sent": N, "clicked": N, "visits": N, "approvals": N}}`) y se eliminan del array `events`.
- En `docs/notifications/send_log.json`: misma regla, borrar eventos > 14 días (el resumen ya quedó en `daily_summary`).
- En `docs/notifications/queue.json`: eliminar las entries de días anteriores (ya quedaron reflejadas en send_log/summary).
- Reescribir `docs/engage/learnings.md`: condensar, no acumular. Máximo ~150 líneas. Registrá click-through por slot horario y por tipo de contenido.

### 4. Crear las experiencias nuevas del día (función paralela — pedido 28/06, reforzado 18/07)

Cada corrida construís **DOS experiencias news-feed NUEVAS de cero** (persona: product/UX/growth/sales expert). El usuario pidió explícitamente (18/07) que **inoves**: formatos nunca probados valen más que refritos de ganadores. Cada una lleva: (1) reacción final (`engageReact`), (2) CTA de suscripción diaria (`engageAnswer` qid `<slug>-suscripcion-diaria`), (3) **caja de feedback de texto propia** (ver contrato), (4) un HTML de pitch aparte con 6 modelos de monetización (3 innovadores + 3 ultra-creativos). Cada proposal es un experimento: anotá la `hypothesis` en `proposals.json`.

Antes de elegir tema: consultá `facts_ledger.json` (elenco fresco) y la lista de ángulos usados en learnings. Si un ángulo recibió feedback de texto negativo o 🙅, está MUERTO — ni variaciones.

**Contrato OBLIGATORIO de toda página proposal** (`docs/engage/<YYYY-MM-DD>-<slug>.html`):

- HTML standalone, `lang="es-UY"`, mobile-first, CSS inline usando la paleta del sitio (`#2d5016` verde, `#f5faf0` fondo). No carga el bundle principal. Sin frameworks, sin `<form>`, sin APIs externas en runtime (los datos del jardín se inlinean al generarla, leyéndolos de `data_plants.py` / sync JSONs).
- **Primer elemento visible: un link al sitio estable** — `<a href="https://gardening-chi.vercel.app/index.html">← Volver al sitio estable</a>`. Esto es regla del usuario, sin excepciones.
- **Caja de feedback de texto integrada a la paleta de la página** (regla del usuario 18/07, sin excepciones):
  ```html
  <section class="blk fb-blk reveal" id="engage-feedback-box">
    <h3>💬 Decime qué te pareció</h3>
    <p>Esto lo leo yo, el agente del jardín, antes de armar la próxima…</p>
    <textarea rows="3" placeholder="Escribime lo que quieras…"></textarea>
    <button type="button" class="fb-send" onclick="engageFeedback('<slug>', this)">Enviar feedback</button>
    <span class="fb-hint"></span>
  </section>
  ```
  El `id="engage-feedback-box"` evita que `engage.js` inyecte la genérica encima. En páginas viejas sin caja propia, la inyección automática de `engage.js` cubre — no hace falta patchearlas.
- Al pie, el bloque de decisión:
  ```html
  <div class="engage-actions">
    <button onclick="engageApprove('<proposal_id>')">✅ Aprobar esta mejora</button>
    <button onclick="engageRejected('<proposal_id>')">✕ No me interesa</button>
  </div>
  <script src="engage.js"></script>
  ```
  `engage.js` ya existe en `docs/engage/` — loguea clicks/visitas/decisiones solo. No lo dupliques ni lo reemplaces.
- Registrá la proposal en `docs/engage/proposals.json`:
  ```json
  {
    "id": "<YYYY-MM-DD>-<slug>",
    "title": "...",
    "page": "engage/<YYYY-MM-DD>-<slug>.html",
    "created": "<YYYY-MM-DD>",
    "status": "pending",
    "hypothesis": "qué creés que va a pasar y por qué",
    "notified_by": ["<ids de notificaciones que la promocionan>"],
    "result_notes": null
  }
  ```

### 5. Escribir la cola del día — según la CADENCIA VIGENTE

**PASO OBLIGATORIO — recordatorios de tareas.** Las tareas ya no son una sección
accesible desde la Home: se comunican SOLO por push. Después de escribir la cola
del día, corré SIEMPRE:

```
python tools/gen_task_reminders.py <YYYY-MM-DD> --merge
```

Eso mergea en `queue.json` el recordatorio de tareas del día (1 "tarea del día"
a las 08:00, o el resumen semanal los lunes), rotando entre las tareas activas de
todas las especies y respetando `task_states.json`. Estas entries (`format: "tarea"`,
ids `-task-dia`/`-task-semana`) son ADICIONALES a la cadencia de experiencias:
no las cuentes contra el cupo, no las edites ni las borres. Si tus propias
notificaciones también van a las 08:00, corré las tuyas a otro slot.

**PASO OBLIGATORIO — Top 3 cada 2 días (pedido directo del usuario 04/07/2026).**
Corré SIEMPRE (el script decide solo si toca por cadencia — cada 2 días, ancla 04/07):

```
python tools/gen_top3_tareas.py <YYYY-MM-DD> --merge
```

Cuando toca, regenera `docs/engage/top3-tareas.html` (las 3 tareas prioritarias de
todas las especies, respetando `task_states.json`) y encola su push (09:00). Igual
que los recordatorios: sus entries (id `-top3`, `format: "tarea"`) son ADICIONALES
a la cadencia — no las cuentes contra el cupo, no las edites ni las borres, y NO
elimines la página `top3-tareas.html` ni la proposal `2026-07-04-top3-tareas`
(experiencia comisionada permanente, no experimento).

**Mirá la sección "CADENCIA VIGENTE" de `docs/engage/learnings.md`.** Si pide alta
frecuencia (ej. cada 15 min), **NO escribas la cola a mano**: corré

```
python tools/gen_queue.py <YYYY-MM-DD>
```

que genera `queue.json` con **un destino ÚNICO por slot** (assert anti-duplicados),
mezclando fichas `#especie` + variaciones de experiencias aprobadas. Escribir la cola
a mano fue lo que metió repeticiones (el usuario se quejó 2 veces). Si la cadencia es
el default (3/día) y querés curar a mano, igual: **cada notificación a un destino
distinto**, salvo variación de una aprobada.

Formato de cada entry `pending` (lo que produce el generador):

```json
{
  "_updated_at": "<now ISO>",
  "notifications": [
    {
      "id": "<YYYY-MM-DD>-a",
      "title": "máx ~40 chars, con gancho",
      "body": "máx ~110 chars, concreto, es-UY",
      "url": "https://gardening-chi.vercel.app/<página>",
      "send_at": "<YYYY-MM-DD>T08:30:00-03:00",
      "expires_at": "<YYYY-MM-DD>T22:00:00-03:00",
      "status": "pending",
      "sent_at": null,
      "fail_reason": null,
      "created_by": "engagement-agent <YYYY-MM-DD>"
    }
  ]
}
```

Política de contenido:

- **Cada notificación se ancla en algo REAL del jardín** — una tarea vencida, una planta en floración este mes, una foto que subió, el clima de la semana. Nada genérico tipo "¡visitá tu jardín!".
- **Variá el ángulo entre las 3**: (a) recordatorio de tarea urgente/estacional → deep link a `tareas.html` o a la task page; (b) teaser con curiosidad hacia la proposal activa; (c) tip estacional, celebración de progreso o dato curioso de una planta suya.
- **Horarios**: arrancá con 08:30 / 13:00 / 19:30 (-03:00) y ajustá según learnings. El dispatcher corre cada 30 min entre 07:00 y 20:30 de Montevideo — `send_at` fuera de esa ventana no se manda hasta la próxima ventana. **El primer `send_at` del día tiene que ser ≥ 60 min después de tu corrida** (margen para que Vercel deploye las páginas que las notificaciones linkean).
- `expires_at`: el mismo día a las 22:00 -03:00. Una notificación vieja que llega a deshora quema confianza.
- Timestamps SIEMPRE con offset explícito `-03:00` (Montevideo no tiene DST).
- **Frecuencia adaptativa**: si los datos muestran fatiga (varios días seguidos sin ningún click), bajá la intensidad — usá menos gancho, espaciá horarios, o dejá 1-2 slots con contenido de muy bajo costo de atención. Anotá el cambio de estrategia en learnings. El máximo es 3/día; no hay mínimo inteligente que ignore los datos.

### 6. Build + commit + push

1. Si tocaste `data_plants.py`, `data_ideas.py`, `build.py`, `scripts.py` o `styles.py` → correr `python build.py` y verificar que termina sin error.
2. Commit(s) con prefijo `engage:` describiendo qué se decidió y por qué (1 línea de hipótesis si hay proposal nueva).
3. `git push origin main`. Si falla por race (el dispatcher o el sync del browser pushearon), `git pull --rebase origin main` y reintentar (hasta 4 veces, backoff 2s/4s/8s/16s).

### 7. Reportar (mensaje final de la sesión)

- 💬 Feedback de texto recibido (citado) y qué decidiste con cada uno.
- 📊 Resumen de los datos de ayer (sent/clicked/visits/decisiones — recordá: abrir sin señal activa = "masomenos").
- 📄 Qué pasó con las proposals (promovida/descartada/nueva + hipótesis).
- 🔔 Las 3 notificaciones de hoy con sus horarios.
- 🔗 SHA del commit.

## Reglas duras

- **Cantidad de notificaciones: la que indique la CADENCIA VIGENTE de learnings.md (default 3/día). Dos experiencias nuevas por corrida (función paralela).** Cada notificación, a una experiencia distinta.
- **Toda experiencia lleva: link "← Volver al sitio estable" como primer elemento visible, caja de feedback de texto (`engageFeedback`), y los botones Aprobar / No me interesa al pie.** Sin excepciones.
- **El feedback de texto del usuario es ley:** positivo = expandir ese ángulo; negativo = ese contenido no vuelve NUNCA; pedido explícito = se ejecuta en la corrida siguiente (o en la misma). Sin feedback = "masomenos", no lo cuentes como éxito.
- **Anti-repetición:** leé y actualizá `docs/engage/facts_ledger.json` en cada corrida. Planta featured descansa ≥7 días; fact no se repite en <14 días; ≥70% del elenco de cada experiencia nueva sin usar en 7 días. Re-push de una promovida = contenido renovado en la misma URL.
- **Proposals sin aprobación explícita de un día anterior se eliminan hoy.** La aprobación es el único pase a permanencia.
- `docs/sync/task_states.json`, `docs/sync/user_tasks.json`, `docs/uploads.json`, `docs/sync/contacts.json`, `docs/sync/threads/` y `docs/images/uploads/` son del usuario: **solo lectura** para este comando (la única excepción es la compactación documentada de `engagement.json`). Los threads (`docs/sync/threads/*.json`) los sumás a tu lectura de contexto para calibrar contenido, pero los escribe el agente `/responder-tareas`, no vos.
- En `queue.json`, las entries con `format: "tarea"` (ids `-task-dia`/`-task-semana`/`-top3`/`-reply-*`) son de `gen_task_reminders.py` / `gen_top3_tareas.py` / `/responder-tareas`: **no las cuentes contra el cupo, no las edites ni las borres.**
- NUNCA commitear secretos, PATs, teléfonos, ni la clave VAPID privada.
- NUNCA editar `docs/index.html` / `tareas.html` / `ideas.html` a mano — siempre vía `python build.py`.
- Español uruguayo en todo. Sin frameworks, sin `<form>`, sin APIs externas en runtime.
- Si `python build.py` falla y no lo podés arreglar, pushea SOLO los archivos que no rompen (cola + engage/*) y dejá el resto para mañana con nota en learnings. Main nunca queda roto.
- No exageres ni inventes urgencias del jardín para generar clicks: la credibilidad de las notificaciones es el activo principal. Si una planta no necesita nada, no digas que sí.
