# CLAUDE.md — Contexto del proyecto para Claude Code

## Qué es esto

Sitio estático de un jardín casero en Montevideo, Uruguay. Catálogo de 40 plantas (frente + fondo) con:
- Información detallada por especie
- Calendario anual (floración / fructificación / poda)
- Ideas para sumar plantas nuevas
- Catálogo de huerta
- **Timeline de tareas** estilo Tinder con WhatsApp pre-armado por contacto

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
docs/index.html  ← un único archivo monolítico de ~13MB
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
| `docs/index.html` | Output del build — **NO editar a mano** | Generado siempre por `python build.py` |

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

Clave: `jardineando_task_states_v1`. Valor: objeto `{taskId: {status, snoozed_until, completed_at}}`.

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
    ├── task_states.json           ← Backup + sync de localStorage.jardineando_task_states_v1
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

### Slash commands de Claude Code

Viven en `.claude/commands/<nombre>.md`. Son markdown con frontmatter YAML que describe permisos y body con instrucciones para Claude Code.

Comandos definidos:

- **`/actualizar-tareas`** — procesador manual de fotos uploadeadas. Lee `docs/uploads.json`, filtra entries con `ai_status: "pending"`, evalúa cada foto contra el contexto de su tarea, propone resoluciones (marcar hecha o `description_override`) y commitea cuando el usuario confirma. Usa la visión nativa de Claude Code, sin Anthropic API key separada.
- **`/engagement`** — agente diario de engagement (lo corre una Routine de Claude Code ~06:00 UY). Gestiona proposals, encola las 3 notificaciones push del día y commitea a main. Ver sección "Sistema de engagement" abajo.

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
