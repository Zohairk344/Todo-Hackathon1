from typing import Union, Optional
from src.models.task import Task
from src.repositories.task_repository import InMemoryTaskRepository

# Implements: T-010
class TaskService:
    def __init__(self, repository: InMemoryTaskRepository):
        self.repository = repository

    # Implements: T-010, T-011
    def create_task(self, title: str, description: str = "") -> Union[Task, str]:
        """
        Creates a new task.
        Returns the created Task object or an error string.
        """
        if not title or not title.strip():
            return "Error: Title cannot be empty."
        
        # Additional validation (optional based on constraints)
        if len(title) > 200:
             return "Error: Title must be 200 characters or fewer."

        task = Task(id=0, title=title.strip(), description=description.strip() if description else None)
        return self.repository.add(task)

    # Implements: T-016
    def list_tasks(self) -> list[Task]:
        """Returns a list of all tasks."""
        return self.repository.get_all()

    # Implements: T-021
    def complete_task(self, task_id: int) -> Union[Task, str]:
        """
        Toggles a task between 'Pending' and 'Completed'.
        Returns the updated Task or an error string.
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            return "Error: Task ID not found."
        
        # Toggle logic: Pending <-> Completed
        if task.status == "Completed":
            task.status = "Pending"
        else:
            task.status = "Completed"
            
        self.repository.update(task)
        return task

    # Implements: T-025
    def delete_task(self, task_id: int) -> Union[bool, str]:
        """
        Deletes a task.
        Returns True if successful, or an error string.
        """
        success = self.repository.delete(task_id)
        if not success:
            return "Error: Task ID not found."
        return True

    # Implements: T-028
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Union[Task, str]:
        """
        Updates a task's title and/or description.
        Only updates fields that are provided (not None).
        Returns the updated Task or an error string.
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            return "Error: Task ID not found."
        
        if title is not None:
             if not title.strip():
                 # Spec says blank input preserves value, but here we expect the caller (CLI) 
                 # to pass None or the original value if blank. 
                 # However, strictly, if an update is requested with empty string, we should probably validate 
                 # or assume the CLI handles the "blank means keep" logic.
                 # Let's enforce the CLI logic: if passed empty string, it's invalid unless CLI filters it.
                 # Re-reading FR-005: "If a user provides blank input... system MUST preserve existing value."
                 # This logic is best placed in CLI to determine *what* to pass here, 
                 # OR we treat empty string here as "no change".
                 # Let's treat empty string as no change here for safety.
                 pass 
             else:
                 task.title = title.strip()
                 
        if description is not None:
             # Description can be empty, but if the intention is "keep existing", 
             # the CLI should handle that. If the user *wants* to clear description, 
             # they might pass empty string. 
             # But FR-005 says "blank input... preserve existing".
             # So if description is "", we do nothing.
             if description.strip():
                task.description = description.strip()

        self.repository.update(task)
        return task
