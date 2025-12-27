import os
import sys
from src.services.task_service import TaskService

# Implements: T-012
class CLI:
    def __init__(self, service: TaskService):
        self.service = service

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        print("\n=== Todo App ===")
        print("[A]dd Task")
        print("[V]iew Tasks")
        # Implements: T-026
        print("[U]pdate Task") # Preparing for next phase too to keep order clean
        print("[D]elete Task")
        print("[C]omplete Task")
        print("[E]Exit")
        print("===============")

    # Implements: T-014
    def prompt_add_task(self):
        while True:
            title = input("Enter Title: ").strip()
            # Validation handled here to create a retry loop as per T-014 / Spec Clarification
            if not title:
                print("Error: Title cannot be empty. Please try again.")
                continue
            
            description = input("Enter Description (Optional): ").strip()
            result = self.service.create_task(title, description)
            
            if isinstance(result, str): # Error message
                print(result)
            elif result is not None:
                print(f"Task '{result.title}' added with ID {result.id}.")
            break

    # Implements: T-018, T-019
    def display_tasks(self):
        tasks = self.service.list_tasks()
        if not tasks:
            print("No tasks found.")
            return

        print(f"{ 'ID':<5} {'Status':<12} {'Title'}")
        print("-" * 30)
        for task in tasks:
            if task is not None:
                print(f"{task.id:<5} {task.status:<12} {task.title}")

    # Implements: T-023
    def prompt_complete_task(self):
        task_id_input = input("Enter Task ID to complete: ").strip()
        try:
            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid ID. Please enter a number.")
            return

        result = self.service.complete_task(task_id)
        if isinstance(result, str):
            print(result)
        elif result is not None:
            print(f"Task '{result.title}' status updated to: {result.status}")

    # Implements: T-027
    def prompt_delete_task(self):
        task_id_input = input("Enter Task ID to delete: ").strip()
        try:
            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid ID. Please enter a number.")
            return

        result = self.service.delete_task(task_id)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Task ID {task_id} deleted.")

    # Implements: T-030
    def prompt_update_task(self):
        task_id_input = input("Enter Task ID to update: ").strip()
        try:
            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid ID. Please enter a number.")
            return

        # We need to fetch the task first to show current values or just pass logic to service
        # But FR-005 says "If provided blank input... preserve".
        # Service logic I wrote assumes "if not None/Empty, update". 
        # So here we capture input, if blank, we pass None.
        
        title_input = input("Enter New Title (Leave blank to keep current): ").strip()
        desc_input = input("Enter New Description (Leave blank to keep current): ").strip()

        title = title_input if title_input else None
        description = desc_input if desc_input else None

        result = self.service.update_task(task_id, title, description)
        if isinstance(result, str):
            print(result)
        elif result is not None:
            print(f"Task '{result.title}' updated.")

    # Implements: T-013
    def handle_input(self):
        while True:
            self.display_menu()
            choice = input("Enter command: ").strip().upper()

            if choice == 'A':
                self.prompt_add_task()
            elif choice == 'V':
                self.display_tasks()
            elif choice == 'C':
                self.prompt_complete_task()
            elif choice == 'U':
                self.prompt_update_task()
            elif choice == 'D':
                self.prompt_delete_task()
            elif choice == 'E':
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid command. Please try again.")