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

Filtrar entries con `ai_status: "pending"`. Si no hay ninguna, decir "No hay fotos pendientes de evaluar" y terminar.

Las entries con `context: "species"` no requieren evaluación de IA — sólo registran fotos del catálogo. Saltarlas (no procesarlas, dejar `ai_status: "n/a"` como están).

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

### 3. Mostrar el batch ANTES de modificar nada

Presentá un resumen en el chat con este formato:

```
Encontré N fotos pendientes:

📷 [1] plant-B-25-2 (Inspección gardenia)
   Foto: docs/images/uploads/B-25/plant-B-25-2_20260503-153012.jpg
   → resolved=false. Veo cochinilla algodonosa en el envés de 2 hojas inferiores.
   → Propongo description_override="Tratar zona afectada con jabón potásico (5 ml/L) pulverizado sobre envés. Repetir a los 7 días."

📷 [2] plant-F-1-2 (Rastrillado del frente)
   Foto: docs/images/uploads/F-1/plant-F-1-2_20260503-160245.jpg
   → resolved=true. Cantero limpio, hojas removidas, base de los árboles despejada.
   → Propongo marcar hecha con summary="Cantero limpio, sin hojas acumuladas".

📷 [3] plant-B-9-3 (Foto de corteza Crespón)
   Foto: docs/images/uploads/B-9/plant-B-9-3_20260503-161030.jpg
   → resolved=true. Corteza canela exfoliante visible y bien enfocada, consistente con L. indica.
   → Propongo marcar hecha + sumar la foto al gallery del catálogo.

¿Aplico estos cambios y commiteo? (sí / no / detalles de N / saltear N)
```

### 4. Esperar confirmación del usuario

Opciones que el usuario puede responder:
- **"sí"** o **"adelante"** → aplicá todos los cambios + commit + push.
- **"no"** o **"cancelar"** → no toques nada.
- **"detalles de N"** → mostrá el contenido completo de la entry N y la decisión, sin commitear nada.
- **"saltear N"** → marcá la entry N como `ai_status: "needs_review"` (la dejamos para revisar manualmente después) y aplicá solo el resto.
- Cualquier corrección puntual ("la 1 marcala hecha igual" / "la 2 cambiá el next_steps a X") → ajustá según lo que pida y volvé a presentar el batch.

NUNCA apliques cambios sin confirmación explícita del usuario.

### 5. Aplicar cambios (cuando el usuario confirme)

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

- NUNCA commitear sin confirmación explícita.
- NUNCA modificar `data_plants.py` sin pedir permiso.
- NO inventar plagas/enfermedades sin evidencia visual clara.
- Si dudás de la evaluación de una foto, marcala `resolved=false` con `next_steps="Volver a sacar la foto con [criterio específico]"`. Más vale conservador que cerrar tarea sin certeza.
