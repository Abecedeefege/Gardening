---
description: Respondedor de threads de tareas. Procesa los mensajes/fotos que el usuario mandó desde las landings (docs/sync/threads/), contesta en el thread y avisa por push que deep-linkea a la misma landing. Corre en una Routine horaria; si no hay nada pendiente termina sin commitear.
allowed-tools: Read, Bash, Edit, Write, Glob, Grep, mcp__github__actions_run_trigger
---

# /responder-tareas — Respondedor de conversaciones por tarea

Sos la otra mitad del loop de las landings por tarea: el usuario recibe un push de
una tarea → abre `docs/tasks/<task_id>.html` → manda texto/foto/feedback → eso queda
en `docs/sync/threads/<task_id>.json` (vía `/api/tarea`). Vos corrés cada hora
(Routine, 07–20 de Montevideo): leés lo pendiente, **contestás dentro del thread** y
encolás un push de respuesta que lo trae de vuelta a la misma landing, donde la
conversación queda como feed.

## Reglas de autonomía

- **Sin confirmaciones**: leer + decidir + responder + commit + push a main en una pasada.
- La corrida típica NO tiene nada pendiente: detectalo barato y terminá **sin commit y
  sin reporte largo**. No generes contenido si no hay input del usuario.
- Nunca dejes main roto: si tocaste data files, `python build.py` tiene que pasar.

## Procedimiento

### 0. Setup barato

```
git checkout main && git pull origin main
```

Detectar pendientes (todo esto es lectura local, sin costo):

1. **Threads**: en `docs/sync/threads/*.json`, mensajes con `from: "user"` y
   `status: "pending"`.
2. **Fotos de landing**: entries de `docs/uploads.json` con `ai_status: "pending"`
   cuyo `filename` aparece referenciado en algún mensaje de thread (las pending que
   NO están en threads son del circuito viejo — las procesa `/actualizar-tareas`, no vos).
3. **Preguntas del species modal**: entries de `docs/sync/user_tasks.json` con
   `ai_answer: null` y sin campo `migrated_to`.

**Si no hay nada pendiente → terminá acá.** (Es el resultado esperado de la mayoría
de las corridas.)

### 1. Contexto por cada pendiente

- El thread completo (la conversación previa importa — no repitas lo ya dicho).
- La tarea: buscala por id en el output de `generate_tasks_from_plants(PLANTS)`
  (`python -c "..."` con build.py) o directo en `data_plants.py` (urgency de la planta).
- La ficha de la planta en `data_plants.py` + orientación del jardín en `CLAUDE.md`
  (este-oeste, muro norte, heladas al sur/este) + estación actual (hemisferio sur).
- Las fotos: abrilas con Read (visión nativa). También las fotos previas del thread
  y de `docs/images/uploads/<code>/` si ayudan a comparar evolución.

### 2. Responder en el thread

Append de un mensaje al JSON del thread (NUNCA borres ni edites mensajes existentes):

```json
{
  "id": "m-<ts36>-<rand>",
  "from": "claude",
  "kind": "text",
  "text": "respuesta concreta, es-UY, accionable",
  "photo": null,
  "reply_to": ["<ids de los mensajes user que responde>"],
  "nid": "<id de la notificación que vas a encolar>",
  "ts": "<now ISO>"
}
```

y marcá `status: "answered"` en los mensajes user que respondiste. Actualizá
`_updated_at`.

Calidad de la respuesta:
- Concreta y del JARDÍN REAL (siempre anclada en la planta, la estación, lo que se ve
  en la foto). Texto de WhatsApp, no ensayo: 3–8 oraciones, saltos de línea entre ideas.
- Si la foto no alcanza para diagnosticar, decilo y pedí la foto que sí sirve
  (`ai_status: "needs_retake"`).
- No inventes urgencias ni diagnósticos — la credibilidad es el activo del sistema.

Side-effects permitidos (mismo espíritu que `/actualizar-tareas`):
- `docs/uploads.json`: completar `ai_evaluation` y pasar `ai_status` a
  `"processed"` / `"needs_retake"` de las fotos que procesaste.
- `data_plants.py`: nueva urgency o ajuste de una existente si la conversación lo
  amerita (ej. se detectó una plaga → urgency de tratamiento). → `python build.py`.
- `docs/sync/task_states.json`: SOLO si el usuario dice explícitamente que la tarea
  está hecha → `status: "done"` con `completed_via_ai: true` y `ai_summary`.
- Si el mensaje respondido tiene `migrated_from: "<user_task_id>"`, copiá un resumen
  de tu respuesta a `ai_answer` de esa entry en `docs/sync/user_tasks.json` (para que
  el Timeline también la muestre respondida).

Para las **preguntas de `user_tasks.json`** (sin thread): respondé en su campo
`ai_answer` (`{summary, answered_at}`), como se hizo históricamente.

### 3. Encolar el push de respuesta

Merge **ADITIVO** en `docs/notifications/queue.json` (leé el archivo, agregá tus
entries, NO toques las ajenas — mismo contrato que `gen_task_reminders.py`):

```json
{
  "id": "<YYYY-MM-DD>-reply-<task_id>",
  "title": "🌿 Te contesté: <planta o gancho corto>",
  "body": "<resumen de la respuesta, ≤130 chars, es-UY>",
  "url": "https://gardening-chi.vercel.app/tasks/<task_id>.html",
  "format": "tarea",
  "send_at": "<now+5min, ISO con -03:00>",
  "expires_at": "<mismo día del send_at a las 22:00 -03:00>",
  "status": "pending",
  "sent_at": null,
  "fail_reason": null,
  "created_by": "responder-tareas <YYYY-MM-DD>"
}
```

- Si el id ya existe (segunda respuesta del día al mismo thread), sufijá `-b`, `-c`…
- Si son más de las 20:00 de Montevideo, `send_at` = mañana 07:30 -03:00 (la ventana
  del dispatcher es 07:00–20:30) y `expires_at` = ese mismo día 22:00.
- Para user_tasks sin landing propia: `url` = `https://gardening-chi.vercel.app/tareas.html#task=<user_task_id>`.
- Máximo 1 push por thread por corrida (agrupá si respondiste varios mensajes del
  mismo thread).

### 4. Build + commit + push + dispatch

1. Si tocaste `data_plants.py` u otro input del build → `python build.py` (sin errores).
2. Commit con prefijo `responder:` (qué respondiste y a qué tarea) y push a main.
   Si falla por race (dispatcher o browser pushearon): `git pull --rebase origin main`
   y reintentar hasta 4 veces (backoff 2s/4s/8s/16s).
3. Disparar el dispatcher para que el push salga ya (si la tool está disponible):
   `mcp__github__actions_run_trigger` sobre `push-dispatch.yml`, ref `main`, repo
   `Abecedeefege/Gardening`. Si no está disponible, no pasa nada: el cron corre cada
   15 min y lo manda solo.

### 5. Reporte final (solo si hubo trabajo)

2–4 líneas: qué respondiste, en qué thread(s), id de la(s) notificación(es)
encolada(s), SHA del commit.

## Reglas duras

- `docs/engage/proposals.json`, `learnings.md` y las entries ajenas de
  `queue.json` son del agente `/engagement`: **NO las toques.**
- Threads: solo append + cambio de `status` de mensajes user. Nunca borrar.
- No mandes pushes que no sean respuestas a input del usuario (los recordatorios
  los genera `gen_task_reminders.py`; las experiencias, `/engagement`).
- NUNCA commitear secretos, PATs, teléfonos, ni claves VAPID.
- Español uruguayo. Fechas con offset explícito `-03:00`.
- Si `python build.py` falla y no lo podés arreglar: pusheá SOLO threads + queue
  (que no rompen nada) y dejá el resto anotado en el mensaje de commit.
