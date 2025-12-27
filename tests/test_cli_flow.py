import unittest
from unittest.mock import patch
from io import StringIO
from src.models.task import Task
from src.repositories.task_repository import InMemoryTaskRepository
from src.services.task_service import TaskService
from src.ui.cli import CLI

# Implements: T-033 (Automated verification)
class TestCLIFlow(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryTaskRepository()
        self.service = TaskService(self.repo)
        self.cli = CLI(self.service)

    @patch('builtins.input', side_effect=['A', 'Milk', 'Buy some', 'V', 'E'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_and_view_flow(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            self.cli.handle_input()
        
        output = mock_stdout.getvalue()
        self.assertIn("Task 'Milk' added", output)
        # self.assertIn("Buy some", output) # Spec FR-004 only requires ID, Status, Title in view

    @patch('builtins.input', side_effect=['A', '', 'Milk', '', 'E']) # Empty title retry
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_empty_title_retry(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            self.cli.handle_input()
        
        output = mock_stdout.getvalue()
        self.assertIn("Error: Title cannot be empty", output)
        self.assertIn("Task 'Milk' added", output)

    @patch('builtins.input', side_effect=['C', '1', 'V', 'E'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_complete_task_flow(self, mock_stdout, mock_input):
        # Add a task first
        self.repo.add(Task(id=0, title="Test Toggle"))
        
        with self.assertRaises(SystemExit):
            self.cli.handle_input()
        
        output = mock_stdout.getvalue()
        self.assertIn("status updated to: Completed", output)

    @patch('builtins.input', side_effect=['U', 'abc', 'E']) # Invalid ID
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_id_input(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            self.cli.handle_input()
        
        output = mock_stdout.getvalue()
        self.assertIn("Error: Invalid ID", output)

    @patch('builtins.input', side_effect=['C', '99', 'E']) # Non-existent ID for complete
    @patch('sys.stdout', new_callable=StringIO)
    def test_non_existent_id_complete(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            self.cli.handle_input()
        
        output = mock_stdout.getvalue()
        self.assertIn("Error: Task ID not found", output)

    @patch('builtins.input', side_effect=['U', '99', 'New Title', '', 'E']) # Non-existent ID for update
    @patch('sys.stdout', new_callable=StringIO)
    def test_non_existent_id_update(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            self.cli.handle_input()
        
        output = mock_stdout.getvalue()
        self.assertIn("Error: Task ID not found", output)

if __name__ == '__main__':
    unittest.main()
