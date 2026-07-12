# Plan — Landing conversacional por tarea (push ↔ feedback ↔ push)

**Objetivo:** cada notificación push de tarea abre una landing propia de esa tarea.
Desde ahí el usuario puede dar feedback, hacer preguntas y subir fotos. Claude procesa
lo que llegue y contesta **por push** que deep-linkea a la misma landing, donde la
conversación queda como feed persistente.

**Caso disparador:** el push del 11/07 «⏰ Pendiente: Guayabo del país — Limpieza
invernal de ramas secas» (`plant-F-1`) llevó a `tareas.html#task=plant-F-1` (el Timeline
genérico). Además, el reporte del usuario del 08/05 sobre las manchas negras en las
hojas del guayabo («Enfermo?», `user-1778238699918-71e2`, con foto) quedó sin responder
(`ai_answer: null`) porque hoy no hay ningún actor que procese eso periódicamente.

---

## 1. Qué existe hoy (y qué se reusa)

| Pieza | Estado actual | Rol en el plan |
|---|---|---|
| `docs/tasks/<task_id>.html` | Stubs OG que redirigen a `tareas.html#task=<id>` (build.py ~L1167) | Se convierten en la landing real |
| `tools/gen_task_reminders.py` | Push diario de tarea → `tareas.html#task=<id>` | Cambia la URL → `tasks/<id>.html` |
| `api/feedback.js` | Serverless Vercel, escribe `engagement.json` con token de servidor (sin PAT en el browser) | Patrón a generalizar: nuevo endpoint para mensajes/fotos/estado |
| `docs/engage/engage.js` | Tracking `?nid=`, outbox durable en localStorage, badge de sync | Se reusa en la landing (`../engage/engage.js`) |
| `.github/workflows/push-dispatch.yml` | Cron cada 15 min (07:00–20:00 UY) + `workflow_dispatch` | El agente respondedor lo dispara on-demand para contestar rápido |
| `docs/sync/user_tasks.json` | Preguntas/tareas creadas desde la app (requiere PAT) | Fase 2: se unifica con los threads |
| Routine diaria `/engagement` (~06:00 UY) | Encola las 3 push del día | Queda como está; se agrega una Routine nueva para responder |

## 2. Arquitectura propuesta

```
push "tarea del día" ──deep link──▶ docs/tasks/<task_id>.html   (landing por tarea)
                                        │  render: contexto de la tarea (baked en build)
                                        │        + feed del thread (fetch runtime)
                                        │  composer: texto / foto / botones hecho-posponer
                                        ▼
                                POST /api/tarea  (serverless, token de servidor, sin PAT)
                                        │  escribe en el repo (main):
                                        │   docs/sync/threads/<task_id>.json  (mensaje user)
                                        │   docs/images/uploads/<code>/…      (foto)
                                        │   docs/uploads.json                 (índice)
                                        │   docs/sync/task_states.json        (hecho/snooze)
                                        ▼
                    Routine "respondedor" (cada 1 h, 07–21 UY, sesión fresca)
                        corre /responder-tareas:
                          1. git pull, escanear threads con mensajes user "pending"
                          2. procesar (visión nativa para fotos, contexto data_plants)
                          3. append mensaje "claude" al thread + side-effects
                             (description_override, ai_status en uploads.json, urgencies)
                          4. mergear push de respuesta en queue.json (aditivo, como
                             gen_task_reminders) con url → la MISMA landing
                          5. commit + push a main → disparar workflow_dispatch del
                             push-dispatch → la respuesta llega en ~1-2 min
                                        ▼
                push "🌿 Te contesté sobre el guayabo" ──▶ misma landing, feed actualizado
```

Latencia de respuesta esperada: ≤ 1 h (cadencia de la Routine) + ~2 min de dispatch.
Fuera de la ventana del dispatcher (después de ~20:30 UY) la respuesta queda encolada
para las 07:00.

## 3. Modelo de datos — thread por tarea

`docs/sync/threads/<task_id>.json` (un archivo por tarea → escrituras chicas, casi sin
409 entre el serverless y el agente; retry GET+PUT idéntico a `api/feedback.js`):

```json
{
  "task_id": "plant-F-1",
  "_updated_at": "ISO",
  "messages": [
    {
      "id": "m-<ts>-<rand>",
      "from": "user",                  // "user" | "claude"
      "kind": "text",                  // "text" | "photo" | "action"
      "text": "sigue con las manchas…",
      "photo": null,                   // "uploads/F-1/thread-plant-F-1_<ts>.jpg"
      "ts": "ISO",
      "device": "pix9",
      "status": "pending"              // user: pending → answered (lo marca el agente)
    },
    {
      "id": "m-…",
      "from": "claude",
      "kind": "text",
      "text": "Eso es fumagina…",
      "reply_to": ["m-…"],
      "nid": "2026-07-12-reply-plant-F-1-a",   // push que anunció esta respuesta
      "ts": "ISO"
    }
  ]
}
```

Reglas de ownership (mismo espíritu que el sistema de engagement):
- **Serverless (`/api/tarea`)**: append de mensajes `from: "user"` + fotos + task_states.
- **Agente respondedor**: append de mensajes `from: "claude"`, marcar `status: "answered"`,
  side-effects en data files, entries nuevas en `queue.json` (nunca tocar las ajenas).
- **Agente `/engagement`**: threads en solo-lectura (los suma a su lectura de contexto
  diaria para calibrar contenido, igual que ya lee `user_tasks.json`).

## 4. Fases de implementación

### Fase 1 — Landing por tarea (catálogo) + escritura sin PAT

1. **`build.py`**: reemplazar el generador de stubs de `docs/tasks/` por
   `render_task_landing(task)`:
   - Mantiene los OG tags actuales (no perder el share bonito).
   - Mobile-first, standalone (CSS inline, paleta `#2d5016`/`#f5faf0`), **sin** el bundle
     de 13 MB del sitio: solo la foto de ESA planta embebida como thumb chico.
   - Header: primer elemento visible el link «← Volver al sitio estable» (regla del
     usuario), título de la tarea, planta + códigos, prioridad, `due_label`, descripción.
   - Acciones de estado: ✅ Marcar hecha · 💤 Posponer (via `/api/tarea`, ver abajo).
   - Feed del thread: `fetch('../sync/threads/<id>.json?_=' + Date.now())` al cargar y
     al `visibilitychange` → burbujas user/claude, fotos desde `../images/uploads/…`.
     Runtime fetch = el feed se actualiza sin rebuild del sitio.
   - Composer: textarea + botón «📷 Foto» (input file + compresión canvas a ~1280px
     JPEG, mismo patrón que el upload actual de scripts.py) + «Enviar». Sin `<form>`.
   - `<script src="../engage/engage.js">` para tracking `?nid=`/visitas/dwell.
   - JS de la landing en un archivo compartido `docs/tasks/tarea.js` (no inline por
     página) para no multiplicar bytes × 60 tareas.

2. **`api/tarea.js`** (nuevo, hermano de `api/feedback.js`, mismo `GH_FEEDBACK_TOKEN`):
   `POST { task_id, type, … }` con retry-on-409 ×3:
   - `type: "message"` → append a `docs/sync/threads/<task_id>.json`.
   - `type: "photo"` → `{ base64, filename }` → crea `docs/images/uploads/<code>/thread-<task_id>_<ts>.jpg`
     + entry en `docs/uploads.json` (`context: "task"`, `ai_status: "pending"`) + mensaje
     `kind: "photo"` en el thread. Límite ~3 MB base64 (Vercel corta en 4.5 MB).
   - `type: "state"` → `{ status: "done"|"snoozed", snoozed_until }` → merge por taskId
     en `docs/sync/task_states.json` (last-write-wins, igual que el sync del browser).
   - La landing usa el outbox durable de engage.js-style: guardar local → flush →
     badge honesto (sin "guardado" mentiroso).

3. **`tools/gen_task_reminders.py`**: la URL del recordatorio diario y del top-3 pasa de
   `tareas.html#task=<id>` → `tasks/<id>.html`. (El resumen semanal de los lunes sigue
   yendo a `tareas.html` — es multi-tarea.) Igual ajuste en `tools/gen_top3_tareas.py`
   si linkea tareas individuales.

4. **Seed del guayabo**: migrar el reporte del 08/05 («Enfermo?» + su foto
   `user-1778238699918-71e2_20260508-111139.jpg`) como primer mensaje `pending` del
   thread `plant-F-1`, así la primera corrida del respondedor lo contesta (hipótesis a
   validar con la foto: fumagina sobre secreción de cochinillas, muy típico en feijoa —
   y cómo se relaciona con la tarea de limpieza invernal).

### Fase 2 — Agente respondedor + Routine

5. **`.claude/commands/responder-tareas.md`** (nuevo, autonomía total estilo
   `/engagement`, pero con ownership distinto):
   - Leer threads con mensajes `from: "user", status: "pending"` + `docs/uploads.json`
     con `ai_status: "pending"` de contexto task + (fase 2b) `user_tasks.json` con
     `ai_answer: null`.
   - **Si no hay nada pendiente: terminar sin commit** (corrida barata, es el caso común).
   - Procesar cada pendiente: Read de la foto (visión nativa), contexto de la planta
     desde `data_plants.py`, orientación del jardín de CLAUDE.md, estación.
   - Responder: append al thread + marcar `answered` + side-effects (igual que
     `/actualizar-tareas`: `description_override`, urgencies nuevas, `ai_status:
     "processed"`). Si tocó data files → `python build.py`.
   - Encolar push de respuesta (aditivo en `queue.json`, id `<fecha>-reply-<task_id>-<letra>`,
     `send_at` = ahora redondeado, `expires_at` mismo día 22:00 -03:00, url →
     `tasks/<id>.html`). Título tipo «🌿 Te contesté sobre el guayabo», body con el
     gancho de la respuesta.
   - Commit + push a main (retry con rebase, igual que /engagement) + disparar
     `push-dispatch.yml` vía `workflow_dispatch` para que el push salga ya.
   - Regla dura: NO tocar entries ajenas de la queue, NO tocar proposals/learnings
     (eso es de /engagement), NO inventar diagnósticos si la foto no alcanza — pedir
     otra foto por el mismo canal (`ai_status: "needs_retake"`).

6. **Routine nueva** (separada de la diaria de engagement — fallas y ownership aislados):
   - Cron `0 10-23 * * *` (UTC) = cada hora 07:00–20:00 UY, sesión fresca por corrida.
   - Prompt: «Corré /responder-tareas para la fecha de hoy. Si no hay mensajes ni fotos
     pendientes, terminá sin commitear.»
   - Alternativa descartada pero documentada: rewrite de la Routine de engagement para
     que corra cada hora y decida qué rol jugar según la hora. Funciona, pero mezcla
     ownership de archivos y un fallo del respondedor rompería la corrida diaria.
   - Alternativa de menor latencia (si algún día molesta la hora de espera): GitHub
     Action `claude-code-action` disparada por push a `docs/sync/threads/**`. Requiere
     `ANTHROPIC_API_KEY` como secret del repo; queda anotada, no es parte de este plan.

### Fase 2b — Unificar las preguntas existentes

7. Las preguntas del species modal (`user_tasks.json`, las que hoy quedan con
   `ai_answer: null`) entran al mismo circuito: el respondedor las contesta y el push
   linkea a la landing correspondiente. Para tareas/preguntas creadas en runtime (ids
   `user-…`, sin página estática) se agrega una landing genérica `docs/tarea.html` que
   renderiza por `#id=` leyendo `user_tasks.json` + thread — misma UI, datos runtime.

### Fase 3 — Documentación y cierre

8. `CLAUDE.md`: sección nueva «Threads por tarea» (modelo de datos, ownership de los
   3+1 actores, convención de filenames de fotos de thread) + actualizar la tabla de
   archivos clave y el diagrama de build.
9. `docs/engage/learnings.md` / `/engagement`: sumar los threads a la lectura de
   contexto diaria (solo lectura).
10. Verificación end-to-end en preview: abrir landing → mandar texto + foto → correr
    /responder-tareas a mano → ver el push encolado y el feed actualizado.

## 5. Decisiones tomadas (con fundamento) — objetar si no cierran

| Decisión | Por qué |
|---|---|
| Landing estática por tarea (no una SPA genérica) | Ya existen los stubs con OG; página liviana (~100 KB vs 13 MB de tareas.html) que abre instantáneo desde el push |
| Feed por fetch runtime, contexto baked en build | La conversación avanza sin rebuild; el contexto de la tarea cambia poco |
| Serverless sin PAT para escribir | El teléfono que abre el push no tiene por qué tener el PAT configurado; `api/feedback.js` ya validó el patrón |
| Un thread JSON por tarea | Evita contención de 409 con `engagement.json` y entre tareas |
| Routine horaria separada, sesión fresca | Corrida no-op barata; no arriesga la Routine diaria de engagement |
| Push de respuesta aditivo en queue.json + workflow_dispatch | Respeta el ownership del dispatcher y baja la latencia a minutos |

**Punto abierto (menor):** el endpoint `/api/tarea` queda sin auth, igual que
`/api/feedback` (cualquiera que conozca la URL puede escribir un mensaje). Precedente
ya aceptado en el proyecto; si se quiere endurecer, un secreto liviano por device en
localStorage enviado como header, verificado en la función. No bloquea la fase 1.

## 6. Orden y tamaño estimado

1. Fase 1 (landing + api + URLs de push + seed guayabo): **1 sesión de trabajo**, es el
   grueso. Deployable solo — aunque el respondedor no exista todavía, la landing ya
   junta feedback/fotos en el repo.
2. Fase 2 (comando + Routine): **corta**, es prompt-engineering + crear la Routine.
3. Fase 2b y 3: incrementales.
