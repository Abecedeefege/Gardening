# CLAUDE.md — Contexto del proyecto para Claude Code

## Qué es esto

Sitio estático de un jardín casero en Montevideo, Uruguay. Páginas:
- **Home = Biblioteca** (`docs/index.html`) — la Biblioteca de especies ES la pantalla de inicio: tabs por ubicación Frente / Fondo / Interior (sin vista "Todo"), subtabs Info / Calendario anual. `docs/biblioteca.html` es solo un stub de redirect a index.html para links viejos
- **Ideas** (`docs/ideas.html`) — subtabs en 2 filas: Ornamentales / Huerta / Espacios / Experiencias / Mejoras. Las **Curiosidades** del catálogo viven dentro de Experiencias (`#curiosidades-section`, deep link `ideas.html#curiosidades`) y las **Mejoras** son un subtab propio
- **Tareas** (`docs/tareas.html`) — **Timeline de tareas** estilo Tinder con WhatsApp pre-armado por contacto. NO se linkea desde la Home: las tareas se comunican por **notificación push** (recordatorio diario / resumen semanal, ver `tools/gen_task_reminders.py`) y se llega por deep link

## Orientación del jardín (datos físicos clave)

La casa tiene una alineación casi perfecta este-oeste. Esto define el comportamiento solar de cada zona y debe usarse para razonar sobre cuidados (sol directo, exposición al frío, sombra de mediodía, etc.):

| Punto cardinal | Zona/landmark | Implicancia solar |
|---|---|---|
| **Este** | Fondo (zona "fondo" en `data_plants.py`) | Sale el sol acá. Sol matinal hasta el mediodía. Donde está el liquidámbar B-37, la pileta, el palto B-36. |
| **Oeste** | Frente (zona "frente") | Se oculta el sol acá. Sol vespertino hasta el atardecer. Las Fotinias F-1..F-6, F-9 (ligustro), F-10 (fresno) están en este eje. |
| **Norte** | Muro del hibisco y el lapachillo | Pared/landmark que mira norte → recibe sol todo el día en invierno (hemisferio sur). Lado más cálido y luminoso del año. |
| **Sur** | Pera Williams | Lado que mira sur → menos sol directo en invierno, más sombra. Suele acumular más humedad. |

**Reglas de pulgar para Montevideo (lat ~34.9° S):**
- Las plantas **heliófilas** (necesitan sol pleno: frutales, rosales, hierbas mediterráneas) andan mejor en frente o muro norte.
- Las plantas de **sombra parcial** o **interior tropical** (helechos, hortensias, gardenias) prefieren fondo (este) o sur — luz suave.
- En **invierno**, el sol pasa más bajo y por el norte: revisar si las podas estructurales liberan luz al lado norte.
- **Heladas tardías** (junio-agosto) pegan más fuerte al sur y al este al amanecer — proteger pies tiernos en esa franja.

Esta info se puede extender a futuro como campo `cardinal_exposure` derivado por planta en `data_plants.py` (no implementado todavía).

## Stack y arquitectura

**Build-time:** Python 3 con Pillow para optimizar e incrustar imágenes como base64.
**Runtime:** HTML5 + CSS + JS vanilla — sin frameworks, sin build step en el browser.
**Hosting:** GitHub Pages servido desde `docs/index.html`.
**Estado del cliente:** `localStorage` (no hay backend).

### Flujo de build

```
data_plants.py + data_ideas.py
       ↓
   build.py
       ↓ (lee imágenes desde images/, las codifica base64,
          genera HTML con CSS de styles.py y JS de scripts.py,
          inyecta TASKS y DEFAULT_CONTACTS como JSON globales)
       ↓
docs/index.html      ← Home = Biblioteca de especies (Frente/Fondo/Interior + Info/Calendario)
                       Incluye el splash «Hora dorada — amanecer» inline al inicio del <body>
                       (SPLASH_CSS en styles.py + SPLASH_JS en scripts.py + render_splash() en
                       build.py): foto real del fondo (images/splash-otono.jpg, servida desde
                       docs/images/, NO base64) que arranca de noche y amanece atada a la carga
                       real, 1 vez por sesión (sessionStorage jardineando_splash_v1), tap = saltar.
                       Demos/pitch de todas las variantes: docs/engage/splash-*.html
docs/biblioteca.html ← stub de redirect a index.html (links viejos)
docs/tareas.html     ← Timeline de tareas (se llega por push deep link)
docs/tasks/<id>.html ← Landing por tarea (destino de los push de recordatorio): contexto +
                       acciones hecha/posponer + feed de conversación con Claude. Comparten
                       docs/tasks/tarea.js. Ver sección «Landings por tarea + threads».
docs/ideas.html      ← ideas + huerta + espacios + experiencias (con curiosidades) + mejoras
```

### Archivos clave

| Archivo | Qué contiene | Cuándo tocarlo |
|---|---|---|
| `data_plants.py` | Array `PLANTS` con 40 dicts | Agregar/editar plantas, cambiar urgencias |
| `data_ideas.py` | `NEW_IDEAS_*`, `HUERTA`, `HUERTA_LOCATION_IDEAS`, `DEFAULT_CONTACTS` | Editar ideas o defaults de contactos |
| `build.py` | Render HTML, generación de tareas, helpers | Cambiar layout/estructura de páginas |
| `styles.py` | Todo el CSS como string raw | Cambios visuales |
| `scripts.py` | Todo el JS como string raw | Lógica del Timeline, modales, swipe |
| `images/` | Fotos del jardín (62 archivos) | Agregar fotos nuevas |
| `tools/gen_task_reminders.py` | Recordatorios push de tareas (diario + semanal, todas las especies) | Cambiar política de recordatorios de tareas |
| `tools/gen_top3_tareas.py` | Top 3 de tareas prioritarias cada 2 días (regenera `docs/engage/top3-tareas.html` + encola push) | Cambiar ranking/cadencia del top 3 |
| `docs/tasks/tarea.js` | JS compartido de las landings por tarea (feed del thread + composer texto/foto + estado + tracking) | Cambiar lógica de la conversación en la landing |
| `api/tarea.js` | Serverless de Vercel: backend de las landings (message/photo/state → repo, sin PAT en el browser) | Cambiar qué/cómo escribe la landing al repo |
| `.claude/commands/responder-tareas.md` | Agente respondedor de threads (Routine horaria) | Cambiar política de respuestas por tarea |
| `docs/index.html`, `docs/biblioteca.html`, `docs/tareas.html`, `docs/ideas.html`, `docs/tasks/<id>.html` | Output del build — **NO editar a mano** | Generado siempre por `python build.py` |

### Modelo de datos — Tarea

Las tareas viven en el JS como `const TASKS = [...]` (inyectado por build.py desde `generate_tasks_from_plants`).

```javascript
{
  id: "plant-B-30",                    // único; usado como key en localStorage
  kind: "plant_action",
  plant_codes: ["B-30", "B-35"],       // ids del catálogo
  plant_common: "Durazno",
  plant_zone: "fondo",                 // "frente" | "fondo"
  plant_photo: "b30.jpg",              // referencia al objeto IMG
  title: "Poda invernal urgente",
  description: "Durazno (B-30, B-35) — Poda invernal urgente.",
  priority: "alta",                    // "alta" | "media" | "baja"
  due_label: "Junio-julio 2026",
  due_month: 6,
  due_year: 2026,
  suggested_contact: "jardinero",      // id de contacto sugerido (puede ser null)
}
```

### Estado de tareas (localStorage)

Clave: `jardineando_task_states_v2`. Valor: objeto `{taskId: {status, snoozed_until, completed_at}}`.

```javascript
{
  "plant-B-30": {
    status: "active" | "done" | "snoozed",
    snoozed_until: "2026-06-15T00:00:00.000Z" | null,
    completed_at: "2026-05-15T14:30:00.000Z" | null
  }
}
```

Lógica:
- Si `status === "snoozed"` y `snoozed_until` ya pasó, la tarea vuelve automáticamente a `active` al renderizar.
- "Reactivar" (botón en tareas done/snoozed) limpia todo y vuelve a active.

### Contactos (localStorage)

Clave: `jardineando_contacts_v1`. Valor: array idéntico en estructura a `DEFAULT_CONTACTS` de `data_ideas.py`:

```javascript
[
  { id, name, icon, phone, default_template }
]
```

`default_template` puede contener `{task}` que se reemplaza con `${title} — ${plant_common} (${plant_codes})` al abrir el modal.

URL de WhatsApp: `https://wa.me/PHONE?text=ENCODED_MESSAGE` donde PHONE es el teléfono sin signos (regex `[^0-9]` se reemplaza por vacío).

### Swipe gestures

Implementado en `setupSwipe(card)` (scripts.py). Soporta touch + mouse:
- `>100px` derecha → marcar hecho (anima `swipe-out-right`)
- `>100px` izquierda → abrir modal snooze
- `<100px` → vuelve a posición
- Ignora si el target es un `<button>` (para que los botones funcionen)
- Distingue swipe horizontal vs scroll vertical en los primeros 12px

### Estructura de uploads (fotos subidas runtime desde el browser)

Las fotos que el usuario sube desde el sitio (botón "📷 Subir foto" en tareas o "📷 Sumar foto" en cards de especie) NO entran al pipeline de `images/` (curated, base64-inline). Tienen su propia rama paralela:

```
docs/
├── images/
│   └── uploads/                   ← Fotos subidas runtime (referenciadas via URL relativa, NO base64)
│       ├── B-25/
│       │   ├── plant-B-25-2_20260503-153012.jpg     ← upload de tarea
│       │   └── species-B-25_20260512-091040.jpg     ← upload de especie
│       └── ...
├── uploads.json                   ← Índice de uploads (estado pending/processed/n_a)
└── sync/
    ├── task_states.json           ← Backup + sync de localStorage.jardineando_task_states_v2
    └── contacts.json              ← Backup + sync de localStorage.jardineando_contacts_v1
```

Convención de filename:
- Tarea: `<task_id>_<YYYYMMDD-HHMMSS>.jpg` → `plant-B-25-2_20260503-153012.jpg`
- Especie: `species-<plant_id>_<YYYYMMDD-HHMMSS>.jpg` → `species-B-25_20260512-091040.jpg`

Las fotos llevan un overlay quemado en la esquina inferior izquierda con `task_id` + fecha + título corto (cuando son uploads de tarea). Sirve como referencia visual y como sanity check al procesar con `/actualizar-tareas`.

`docs/uploads.json` shape:
```json
{
  "<plant_id>": [
    {
      "filename": "...",
      "uploaded_at": "ISO",
      "uploaded_by": "device-name",
      "context": "task" | "species",
      "task_id": "plant-XXX" (solo si context=task),
      "task_title_snapshot": "..." (solo task),
      "ai_status": "pending" | "processed" | "needs_retake" | "needs_review" | "superseded" | "orphaned" | "n/a",
      "ai_evaluation": null | { "resolved": bool, "summary": "...", "next_steps": "...", "processed_at": "ISO" }
    }
  ]
}
```

### Landings por tarea + threads de conversación

Cada tarea tiene una **landing propia** en `docs/tasks/<task_id>.html` (generada por `build_task_page()` en `build.py`; comparten el JS `docs/tasks/tarea.js` y el CSS `TAREA_LANDING_CSS` de `styles.py`). Es el destino de los push de recordatorio de tareas: standalone (~11 KB, NO carga el bundle del sitio), abre instantáneo desde la notificación. Muestra el contexto de la tarea (foto por URL relativa, prioridad, fecha, cómo/tips), botones **hecha / posponer**, y un **feed de conversación con Claude** con composer de texto + foto. Mantiene los OG tags para el preview de WhatsApp.

El usuario escribe desde la landing → `api/tarea.js` (serverless de Vercel, mismo `GH_FEEDBACK_TOKEN` de servidor que `api/feedback.js`, el browser **NO necesita PAT**) escribe al repo. Un mensaje/foto queda como `status: "pending"` en el thread; el agente `/responder-tareas` lo procesa y contesta por push que deep-linkea a la misma landing.

```
docs/
├── tasks/
│   ├── tarea.js                   ← JS compartido de todas las landings (feed + composer + estado + tracking)
│   └── <task_id>.html             ← Landing por tarea (destino de los push de recordatorio)
└── sync/
    └── threads/
        └── <task_id>.json         ← Conversación de esa tarea (un archivo por tarea → sin contención de 409)
```

`docs/sync/threads/<task_id>.json` shape:
```json
{
  "task_id": "plant-F-1",
  "_updated_at": "ISO",
  "messages": [
    { "id": "m-...", "from": "user" | "claude", "kind": "text" | "photo",
      "text": "...", "photo": "uploads/<code>/<task_id>_<ts>.jpg" | null,
      "ts": "ISO", "device": "...", "status": "pending" | "answered",
      "reply_to": ["<ids>"], "nid": "<push que anunció la respuesta>" }
  ]
}
```

Fotos de thread: convención `<task_id>_<YYYYMMDD-HHMMSS>.jpg` en `docs/images/uploads/<code>/` + entry en `docs/uploads.json` (`context: "task"`, `via: "landing"`, `ai_status: "pending"`), igual que los uploads del Timeline — así `/responder-tareas` y `/actualizar-tareas` las levantan del mismo índice.

**Ownership (4 actores, escrituras disjuntas):** las landings/`api/tarea.js` hacen append de mensajes `from: "user"` + fotos + `task_states.json`; `/responder-tareas` hace append de `from: "claude"`, marca `answered`, toca data files y encola push `-reply-*`; `/engagement` lee los threads solo para calibrar contenido; el dispatcher solo manda la queue. Nadie pisa lo del otro.

### Slash commands de Claude Code

Viven en `.claude/commands/<nombre>.md`. Son markdown con frontmatter YAML que describe permisos y body con instrucciones para Claude Code.

Comandos definidos:

- **`/actualizar-tareas`** — procesador manual de fotos uploadeadas. Lee `docs/uploads.json`, filtra entries con `ai_status: "pending"`, evalúa cada foto contra el contexto de su tarea, propone resoluciones (marcar hecha o `description_override`) y commitea cuando el usuario confirma. Usa la visión nativa de Claude Code, sin Anthropic API key separada.
- **`/engagement`** — agente diario de engagement (lo corre una Routine de Claude Code ~06:00 UY). Gestiona proposals, encola las 3 notificaciones push del día y commitea a main. Ver sección "Sistema de engagement" abajo.
- **`/responder-tareas`** — respondedor de los threads de las landings por tarea (lo corre una Routine horaria, 07–20 UY, sesión fresca). Lee `docs/sync/threads/*.json` buscando mensajes/fotos del usuario con `status: "pending"` (+ `user_tasks.json` con `ai_answer: null`), contesta dentro del thread con visión nativa, encola un push `-reply-*` que deep-linkea a la misma landing, y commitea a main. Si no hay nada pendiente, termina sin commitear. Ver sección "Landings por tarea + threads".

### Sistema de engagement (push + proposals)

Tres actores con ownership disjunto de archivos (NO cruzar escrituras):

| Actor | Corre | Escribe |
|---|---|---|
| Agente diario (`/engagement` vía Routine) | 1×/día ~06:00 UY | `docs/notifications/queue.json` (rewrite), `docs/engage/*` , data files + build |
| Dispatcher (`.github/workflows/push-dispatch.yml` → `tools/send_push.js`) | cron cada 30 min, 07:00–20:30 UY | statuses de la queue, `docs/notifications/send_log.json`, invalidación de suscripción |
| Browser (PAT, scripts.py + `docs/engage/engage.js`) | al interactuar | `docs/sync/push_subscription.json`, `docs/sync/engagement.json` |

Estructura:

```
docs/
├── notifications/
│   ├── vapid_public.txt           ← Clave VAPID pública (la privada es secret VAPID_PRIVATE_KEY en GitHub Actions — NUNCA al repo)
│   ├── queue.json                 ← Cola del día (el agente escribe, el dispatcher manda y actualiza status)
│   ├── task_reminders_plan.json   ← Plan de recordatorios de tareas (generado por tools/gen_task_reminders.py --plan)
│   └── send_log.json              ← Log de envíos del dispatcher
├── engage/
│   ├── engage.js                  ← Tracking + aprobación para páginas proposal (standalone)
│   ├── proposals.json             ← Registro de proposals (pending/approved/promoted/dropped)
│   ├── learnings.md               ← Memoria del agente (se reescribe, máx ~150 líneas)
│   └── <YYYY-MM-DD>-<slug>.html   ← Páginas proposal (efímeras: sin aprobación, se borran al día siguiente)
└── sync/
    ├── push_subscription.json     ← Suscripción Web Push del device (status active/disabled/invalid)
    └── engagement.json            ← Eventos: notification_clicked / page_visit / proposal_approved / proposal_rejected
```

**Recordatorios de tareas por push:** las tareas NO tienen sección en la Home — se comunican por push. `tools/gen_task_reminders.py <fecha> --merge` genera y mergea en la queue el recordatorio del día (martes-domingo 08:00: "tarea del día" rotando entre las tareas activas de todas las especies, deep link a la **landing de la tarea** `tasks/<id>.html`; lunes 08:00: resumen semanal → `tareas.html`). Respeta `task_states.json` (done/snoozed). El agente de `/engagement` lo corre como paso obligatorio de su corrida diaria; sus entries (`format: "tarea"`) son adicionales a la cadencia de experiencias. Además, `tools/gen_top3_tareas.py <fecha> --merge` (también paso obligatorio de `/engagement`, self-gated a cada 2 días con ancla 2026-07-04) regenera `docs/engage/top3-tareas.html` con las 3 tareas prioritarias de todas las especies y encola su push (09:00) — pedido directo del usuario del 04/07/2026.

**Timeline — tareas pasadas:** en la vista "Todas" de `tareas.html`, las tareas hechas/cerradas NO aparecen en el flujo principal: van en un módulo colapsado "🗂️ Pasadas / hechas" al final (mismo patrón que las tareas futuras), para dar foco a las pendientes. El deep link `#task=<id>` abre el módulo automáticamente si la tarea está adentro.

Flujo: el agente encola 3 notificaciones con `send_at` (-03:00) → Vercel deploya → el dispatcher manda lo vencido → el SW (`docs/sw.js`) muestra la notificación y al click abre el deep link con `?nid=&src=push` → el cliente loguea el click/visita en `engagement.json` → el agente lee los datos a la mañana siguiente y adapta. Las proposals necesitan aprobación explícita (botón en la página) para sobrevivir; aprobadas se promueven al sitio principal.

### Sync engine

Estado del usuario (tareas hechas/pospuestas, contactos, evaluaciones de IA) vive en `localStorage`. Para que sincronice entre dispositivos, el browser **lee** `docs/sync/task_states.json` y `docs/sync/contacts.json` al cargar la página y al recuperar foco (`visibilitychange`), y los **escribe** vía GitHub API después de cada cambio (debounce 5 s).

Conflict resolution: last-write-wins por taskId basado en `last_modified_at`. Si el browser hace PUT y recibe 409 (alguien más pushó en el medio), refetch + remerge + reintento (max 3).

Status visible en barra arriba del Timeline: 🟢 sincronizado · 🟡 sincronizando · 🔴 N pendientes · ⚫ deshabilitado.

API keys (GitHub PAT, device name) viven SOLO en localStorage de cada device — NUNCA se sincronizan al repo.

## Workflow para iterar

1. Editar `.py` (data o build/styles/scripts)
2. Correr `python build.py`
3. Abrir `docs/index.html` localmente para verificar
4. `git add . && git commit && git push` → GitHub Pages actualiza automáticamente

## Convenciones

- **No editar `docs/index.html` a mano** — siempre regenerar con `python build.py`
- **Al cambiar lógica del Timeline**, editar `scripts.py` (no `build.py`)
- **Al cambiar look & feel**, editar `styles.py`
- **Al cambiar estructura de zonas / sub-tabs**, editar `build.py`
- **Strings en español** — todo el sitio es es-UY
- **Spanish localized dates** — usar `toLocaleDateString('es-UY', ...)`
- **Sin dependencias externas en runtime** — solo Google Fonts vía `@import`. Todo el resto inline.

## Ideas para futuras mejoras

Estas son ideas que el usuario podría querer pedirte:

### Storage / Sync
- Sincronizar estado entre dispositivos (Firebase / Supabase / Pocketbase)
- Exportar / importar estado como JSON
- Backup automático del estado a un Gist privado

### Notificaciones
- Service worker + Notification API para recordar tareas con `due_date` cercana
- Banner arriba del Timeline cuando hay tareas vencidas

### Más datos en cada planta
- Fotos múltiples (galería swipe) — ahora solo `main_photo` y `loc_photo`
- Histórico de podas / cuidados realizados (con fecha y notas)
- Notas libres por planta (editables desde la UI)

### Timeline avanzado
- Repetición de tareas (ej. "regar lavanda cada 7 días")
- Tareas custom creadas desde la UI (no solo derivadas de plantas)
- Drag-and-drop para reordenar
- Búsqueda/filtro por planta o por contacto sugerido

### Optimización
- Mover imágenes a `docs/images/` (paths relativos) en lugar de base64 inline
  → reduce tamaño del HTML de 13MB a ~50KB y permite caché del browser
- Code splitting: cargar timeline.js solo cuando se entra a esa pestaña
- Service worker para cachear el sitio offline

### Visualizaciones
- Mapa del jardín con coords aproximadas de cada planta (clickeable)
- Timeline cronológico (eje horizontal con meses) con todas las tareas

## Cosas a NO hacer

- ❌ No introducir frameworks (React, Vue, etc) — la simplicidad es un feature
- ❌ No usar `<form>` ni `submit` events — el usuario reportó que en Claude Artifacts dan problema
- ❌ No agregar fetch a APIs externas sin avisar — el sitio debe funcionar offline.
  *Excepción documentada:* sync engine y upload de fotos llaman a la GitHub API (PAT del usuario en localStorage) y a `docs/sync/*.json` y `docs/uploads.json` del propio repo. Es opt-in: sin PAT, sync queda deshabilitado y el sitio sigue funcionando 100% offline.
- ❌ No subir teléfonos al repo — los contactos viven solo en localStorage. Tampoco se sincronizan API keys ni el GitHub PAT — quedan locales por device.
- ❌ No cambiar estructura de `docs/` — GitHub Pages depende de eso
