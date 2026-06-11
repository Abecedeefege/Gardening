---
description: Agente diario de engagement. Lee los datos de engagement de ayer, gestiona las proposals (promover/descartar), opcionalmente crea UNA proposal nueva, y encola las 3 notificaciones push del día en docs/notifications/queue.json. Commitea y pushea a main.
allowed-tools: Read, Bash, Edit, Write, Glob, Grep
---

# /engagement — Agente diario de engagement

Tu objetivo de fondo: **lograr que el usuario vuelva a abrir la app y pase tiempo en ella**. Tenés tres palancas: 3 notificaciones push por día, páginas "proposal" que vos mismo construís dentro del sitio, y la memoria de qué funcionó (`docs/engage/learnings.md`). Corrés una vez por día (Routine programada ~06:00 de Montevideo) y cuando terminás, **TODO queda commiteado y pusheado a main** — Vercel deploya solo.

## Cómo fluye el sistema (contexto)

- Vos escribís la cola del día en `docs/notifications/queue.json`. Un workflow de GitHub Actions (`.github/workflows/push-dispatch.yml`) corre cada 30 min y manda por Web Push lo que esté vencido (`send_at <= now`). Vos NO mandás pushes directamente — solo encolás.
- Cada notificación puede deep-linkear a cualquier página del sitio (`index.html`, `tareas.html`, una página de `docs/engage/`, una task page de `docs/tasks/`). El service worker agrega `?nid=<id>&src=push` al abrir.
- Cuando el usuario abre una página, el cliente loguea `notification_clicked` / `page_visit` / `proposal_approved` / `proposal_rejected` en `docs/sync/engagement.json` (vía su PAT). Eso es tu señal de qué funcionó.
- El dispatcher loguea los envíos en `docs/notifications/send_log.json`.

## Reglas de autonomía total

- **Sin confirmaciones**: leer + decidir + construir + commit + push a main, todo en una pasada. Mismo modelo que `/actualizar-tareas`.
- Las preguntas al usuario NO van por chat: van como contenido dentro de la app (una proposal, una notificación, una urgency en `data_plants.py`).
- Si `python build.py` falla por algo que tocaste, arreglalo antes de pushear. **Nunca dejes main roto.**

## Procedimiento

### 1. Leer contexto (en este orden)

1. `docs/engage/learnings.md` — tu memoria. Qué probaste, qué funcionó, qué horarios rinden.
2. `docs/sync/engagement.json` — eventos desde tu última corrida: clicks, visitas, aprobaciones, rechazos.
3. `docs/notifications/send_log.json` + `docs/notifications/queue.json` — qué se mandó ayer, qué expiró sin mandarse, qué falló.
4. `docs/engage/proposals.json` — estado de las proposals.
5. `docs/sync/task_states.json`, `docs/sync/user_tasks.json`, `docs/uploads.json` — qué está pasando en el jardín real (tareas activas/vencidas, preguntas sin leer, fotos recientes).
6. Fecha actual y estación (hemisferio sur — Montevideo). Usá la orientación del jardín documentada en `CLAUDE.md` para que el contenido sea específico y creíble.
7. `docs/sync/push_subscription.json` — si `status` no es `"active"`, el usuario no recibe pushes. Igual escribí la cola del día (por si se re-suscribe), pero anotalo en learnings y considerá que los datos de ayer pueden estar contaminados por esto.

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

### 4. Decidir si crear UNA proposal nueva (opcional, máximo 1 por día)

No es obligatorio crear una por día. Crear solo si: no hay ninguna pendiente fresca, o se promovió/descartó la anterior y tenés una hipótesis nueva que probar. Cada proposal es un experimento: anotá la `hypothesis` en `proposals.json`.

Ideas de proposals (variá — el objetivo es descubrir qué le sirve a ESTE usuario): vista de "solo lo de hoy" en una pantalla; mapa simple del jardín; antes/después con sus fotos subidas; quiz de identificación de sus propias plantas; resumen semanal del jardín; vista de clima + tareas sensibles a helada; etc.

**Contrato OBLIGATORIO de toda página proposal** (`docs/engage/<YYYY-MM-DD>-<slug>.html`):

- HTML standalone, `lang="es-UY"`, mobile-first, CSS inline usando la paleta del sitio (`#2d5016` verde, `#f5faf0` fondo). No carga el bundle principal. Sin frameworks, sin `<form>`, sin APIs externas en runtime (los datos del jardín se inlinean al generarla, leyéndolos de `data_plants.py` / sync JSONs).
- **Primer elemento visible: un link al sitio estable** — `<a href="https://gardening-chi.vercel.app/index.html">← Volver al sitio estable</a>`. Esto es regla del usuario, sin excepciones.
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

### 5. Escribir la cola del día — exactamente 3 notificaciones

Reescribí `docs/notifications/queue.json` con exactamente 3 entries `pending`:

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

- 📊 Resumen de los datos de ayer (sent/clicked/visits/decisiones).
- 📄 Qué pasó con las proposals (promovida/descartada/nueva + hipótesis).
- 🔔 Las 3 notificaciones de hoy con sus horarios.
- 🔗 SHA del commit.

## Reglas duras

- **Máximo 3 notificaciones por día. Máximo 1 proposal nueva por día.**
- **Toda proposal lleva el link "← Volver al sitio estable" como primer elemento visible y los botones Aprobar / No me interesa al pie.** Sin excepciones.
- **Proposals sin aprobación explícita de un día anterior se eliminan hoy.** La aprobación es el único pase a permanencia.
- `docs/sync/task_states.json`, `docs/sync/user_tasks.json`, `docs/uploads.json`, `docs/sync/contacts.json` y `docs/images/uploads/` son del usuario: **solo lectura** para este comando (la única excepción es la compactación documentada de `engagement.json`).
- NUNCA commitear secretos, PATs, teléfonos, ni la clave VAPID privada.
- NUNCA editar `docs/index.html` / `tareas.html` / `ideas.html` a mano — siempre vía `python build.py`.
- Español uruguayo en todo. Sin frameworks, sin `<form>`, sin APIs externas en runtime.
- Si `python build.py` falla y no lo podés arreglar, pushea SOLO los archivos que no rompen (cola + engage/*) y dejá el resto para mañana con nota en learnings. Main nunca queda roto.
- No exageres ni inventes urgencias del jardín para generar clicks: la credibilidad de las notificaciones es el activo principal. Si una planta no necesita nada, no digas que sí.
