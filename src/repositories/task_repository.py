from typing import List, Optional, Dict
from src.models.task import Task

# Implements: T-005
class InMemoryTaskRepository:
    def __init__(self):
        # Internal storage: ID -> Task
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    # Implements: T-006
    def add(self, task: Task) -> Task:
        """
        Adds a new task to the repository.
        Assigns a unique ID to the task.
        """
        task.id = self._next_id
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    # Implements: T-007
    def get_all(self) -> List[Task]:
        """Returns a list of all tasks."""
        return list(self._tasks.values())

    # Implements: T-008
    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieves a task by its ID."""
        return self._tasks.get(task_id)

    # Implements: T-020
    def update(self, task: Task) -> bool:
        """
        Updates an existing task.
        Returns True if successful, False if task ID not found.
        """
        if task.id in self._tasks:
            self._tasks[task.id] = task
            return True
        return False

    # Implements: T-024
    def delete(self, task_id: int) -> bool:
        """
        Deletes a task by its ID.
        Returns True if successful, False if task ID not found.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
