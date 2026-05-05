---
description: Procesa las fotos uploadeadas pendientes de evaluación. Lee docs/uploads.json, evalúa cada foto vs el contexto de su tarea, y propone resoluciones (marcar hecha o actualizar descripción) antes de commitear.
allowed-tools: Read, Bash, Edit, Write
---

# /actualizar-tareas — Procesador de fotos pendientes

Tu trabajo: revisar las fotos que el usuario subió desde el sitio web a `docs/images/uploads/` y decidir si cada tarea asociada queda resuelta o necesita pasos adicionales. NO haces commits automáticamente — siempre proponés primero y esperás confirmación.

## Procedimiento

### 1. Leer el índice de uploads

Leé `docs/uploads.json`. Tiene la forma:

```json
{
  "B-25": [
    {
      "filename": "plant-B-25-2_20260503-153012.jpg",
      "uploaded_at": "2026-05-03T18:30:12Z",
      "uploaded_by": "iPhone-Lucia",
      "context": "task",
      "task_id": "plant-B-25-2",
      "task_title_snapshot": "Inspección + foto cercana de hojas",
      "ai_status": "pending",
      "ai_evaluation": null
    }
  ]
}
```

Filtrar entries con `ai_status: "pending"`. Si no hay ninguna, decir "No hay items pendientes de evaluar" y terminar.

Tipos de entries posibles según `context`:
- `"task"` → upload de foto para una tarea. Tiene `filename` válido, leer la imagen.
- `"task_text"` → respuesta SOLO TEXTO sin foto. `filename` es `null`. El contenido a evaluar está en `user_context`. NO intentar leer una imagen.
- `"species"` → foto de catálogo, no requiere evaluación de IA. Saltar (dejar `ai_status: "n/a"`).

**Importante:** Si una entry tiene campo `user_context`, ese texto es contexto valioso del usuario (ej: "ambas comparten la base de un tronco viejo", "no germina hace 3 semanas"). Leerlo SIEMPRE antes de evaluar y usarlo para informar la decisión. Para `task_text`, ES la respuesta del usuario; para `task` con foto, complementa lo que se observa.

### 2. Para cada entry pendiente

#### Identificar la tarea

El `task_id` tiene la forma `plant-<plant_id>` (idx=0) o `plant-<plant_id>-<N>` (idx=N-1, ej. `plant-B-25-2` = idx=1).

Buscá la planta en `data_plants.py` por `id_codes[0] == plant_id`. Leé la urgencia correspondiente — el dict tiene `title`, `short_desc`, `detail`, `how_to`, `tips`, `priority`, `when`. Esta es la TAREA — cuál es el objetivo, qué se espera ver para considerarla cumplida.

Si no encontrás la tarea (porque fue eliminada del catálogo entre la subida y el procesamiento), marcá la entry como `ai_status: "orphaned"` y avisá al usuario al final.

#### Leer la imagen

`Read docs/images/uploads/<plant_id>/<filename>` — el Read tool acepta JPEG/PNG y te muestra el contenido visualmente.

La foto debería tener un overlay de metadata quemado en la esquina inferior izquierda con el `task_id` + fecha + título corto. Usalo como sanity check vs el entry del JSON. Si no coincide o no hay overlay, marcalo como warning pero seguí con el entry del JSON como fuente de verdad.

#### Evaluar la foto contra la tarea

Mirá la imagen. Considerá:
- ¿La foto evidencia inequívocamente que la tarea está cumplida? Pensá en qué se espera ver según el `detail` y `how_to` de la tarea.
- ¿Hay algo que merezca atención (plagas, enfermedades, daño) que se vea en la foto? Sin asumir nada que no se vea claramente — regla del catálogo: NO inventar plagas sin evidencia visual.
- ¿La foto es de calidad suficiente para evaluar? Si está muy oscura, fuera de foco, o no muestra lo que la tarea pide, marcá `resolved=false` con `next_steps` tipo "Volver a sacar la foto mostrando X específicamente".

Producí estructura de decisión:

```
{
  "resolved": true | false,
  "summary": "1-2 oraciones de qué ves en la foto",
  "next_steps": "Si no resolved: pasos concretos faltantes. Si resolved: vacío."
}
```

Reglas:
- Español uruguayo claro, sin tecnicismos sin explicar.
- summary describe lo OBSERVADO, no el contexto general de la planta.
- next_steps son pasos accionables y concretos, no consejos genéricos.

### 3. Aplicar cambios INMEDIATAMENTE — sin confirmación

**El flow es autónomo.** Cuando el user invoca `/actualizar-tareas`, el comportamiento esperado es: procesar todo + aplicar + commit + push. Sin presentar batch para confirmación, sin pedir permiso, sin esperar.

**Si necesitás clarificación de algo (foto ambigua, decisión que requiere juicio del user), NO preguntes en el chat.** En su lugar:
- Agregá una **nueva urgencia accionable** en `data_plants.py` para esa planta describiendo qué necesitás (ej: "Sacar foto cercana del nudo de B-43 — confirmar si es jazmín solano o jasminum").
- Esa urgencia aparece en la app del user como una tarea más, donde él la responde con foto o texto cuando puede.
- Marcá la entry actual como `processed` con el summary de lo que detectaste y el next_steps que apunta a la nueva urgencia.

**Las preguntas, dudas y pedidos de más info viajan SIEMPRE por la app (urgencies en data_plants.py)**, nunca por el chat de Claude Code. El chat es solo para reportar lo que se hizo después del push.

### 4. Aplicar cambios

Para cada entry procesada, hacé estas modificaciones:

#### a) `docs/sync/task_states.json`

Leé el archivo actual. La forma es:
```json
{
  "_synced_at": "2026-05-03T...",
  "_last_writer": "claude-code-cli",
  "tasks": {
    "plant-B-25-2": { ... }
  }
}
```

Para cada tarea procesada, actualizá `tasks[task_id]`:
- Si `resolved=true`:
  ```json
  {
    "status": "done",
    "completed_at": "<now ISO>",
    "completed_via_ai": true,
    "ai_summary": "<summary>",
    "last_modified_at": "<now ISO>"
  }
  ```
- Si `resolved=false`:
  ```json
  {
    "status": "active",
    "description_override": "<next_steps>",
    "description_override_at": "<now ISO>",
    "last_ai_summary": "<summary>",
    "last_modified_at": "<now ISO>"
  }
  ```
  (Mergear con el state existente — preservar `snoozed_until` si existía, etc.)

Setear `_synced_at` al timestamp actual y `_last_writer: "claude-code-cli"`.

#### b) `docs/uploads.json`

Para cada entry procesada, actualizar:
```json
{
  "ai_status": "processed",
  "ai_evaluation": {
    "resolved": true | false,
    "summary": "<summary>",
    "next_steps": "<next_steps>",
    "processed_at": "<now ISO>"
  }
}
```

#### c) Commit + push

Commit con mensaje descriptivo:
```
ai: procesar N foto(s) pendiente(s) — M resueltas, K con next_steps

- plant-B-25-2: resolved=false, override de descripción (cochinilla detectada)
- plant-F-1-2: resolved=true, marcada hecha
- plant-B-9-3: resolved=true, marcada hecha
```

Push a main con `git push -u origin main`.

### 6. Reportar al usuario

Después del push, reportá:
- ✅ Cantidad de tareas marcadas hechas.
- 📝 Cantidad de tareas con override de descripción.
- ⚠️ Cantidad de orphaned o needs_review.
- 🔗 SHA del commit final + URL del compare en GitHub.

## Casos especiales

### Foto de upload de especie (`context: "species"`)

No requiere evaluación. Solo registrar (ya está en uploads.json). Si querés, podés sumar a gallery de la planta en `data_plants.py` (campo `gallery: [...]`) — preguntale al usuario si lo hacemos. Marcar `ai_status: "n/a"` (no es pending).

### Múltiples fotos para la misma tarea

Si hay 2+ uploads para el mismo `task_id`, evaluar la MÁS RECIENTE (mayor `uploaded_at`) y marcar las anteriores como `ai_status: "superseded"`.

### Foto sin overlay legible

Warning al usuario, pero seguir adelante con el entry del JSON.

### Tarea que no existe en data_plants.py

Marcá `ai_status: "orphaned"` y avisá al usuario al final.

## Reglas duras

- **El flow es 100% AUTÓNOMO**: procesar + aplicar + commit + push, todo en una pasada sin pedir confirmación. El user invoca el comando esperando que cuando termine, todo esté hecho y pusheado. NO presentar batch para que confirme.
- **Las preguntas, dudas y feedback que necesites del user van como urgencies nuevas en data_plants.py** (que aparecen como tareas en la app), NUNCA por chat. El chat es solo para reportar lo hecho al final.
- **`data_plants.py` se modifica automáticamente cuando el feedback lo amerite** — sin pedir permiso aparte. Casos típicos: refactor de urgencias, agregar urgencias nuevas (por tipo, por incógnita, por plaga detectada), reschedule (cambiar `due_year`/`due_month`), eliminar tareas no útiles, ajustar wording. Si eliminás una urgencia que tenía estado `done`/`snoozed` en `sync/task_states.json`, migrar el sync state para preservar el estado del task_id correcto.
- NO inventar plagas/enfermedades sin evidencia visual clara.
- Si dudás de la evaluación de una foto, marcala `resolved=false` con `next_steps="Volver a sacar la foto con [criterio específico]"`. Más vale conservador que cerrar tarea sin certeza.
- **Cuando el user dice "borra esta" sobre una entry de uploads.json, eliminala del JSON** (no marques superseded — borrá el registro).
- Las tareas (`urgency` en data_plants.py) deben ser **accionables**: title = la acción, short_desc = 1 oración, detail máximo 2-3 oraciones, how_to en 3-5 pasos numerados de 1 oración cada uno. Si el user pide "tareas accionables" o critica que una tarea "no le dice nada", refactorizar ese formato.
