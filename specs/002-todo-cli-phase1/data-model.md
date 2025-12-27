# Data Model

## Entity: Task

Represents a single item of work to be tracked.

| Field | Type | Required | constraints | Description |
|-------|------|----------|-------------|-------------|
| `id` | `int` | Yes | Unique, Auto-increment | Primary identifier for the task. |
| `title` | `str` | Yes | Length: 1-200 chars | The name of the task. Cannot be empty or whitespace only. |
| `description` | `str` | No | Max length: 1000 chars | Additional details about the task. Defaults to empty string. |
| `status` | `str` | Yes | Values: "Pending", "Completed" | The current state of the task. Defaults to "Pending". |

## Storage Schema (In-Memory)

The repository will hold a list or dictionary of `Task` objects.

```python
# Example Internal Structure
_tasks: Dict[int, Task] = {}
_next_id: int = 1
```
