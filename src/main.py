import sys
import os

# Add the project root to sys.path to allow 'src.' imports when running directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.repositories.task_repository import InMemoryTaskRepository
from src.services.task_service import TaskService
from src.ui.cli import CLI

# Implements: T-015
def main():
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    cli = CLI(service)
    
    # Start the application loop
    try:
        cli.handle_input()
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()

