import unittest
from src.models.task import Task
from src.repositories.task_repository import InMemoryTaskRepository

# Implements: T-009
class TestInMemoryTaskRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryTaskRepository()

    def test_add_task(self):
        task = Task(id=0, title="Test Task")
        added_task = self.repo.add(task)
        self.assertEqual(added_task.id, 1)
        self.assertEqual(added_task.title, "Test Task")

    def test_get_all(self):
        self.repo.add(Task(id=0, title="Task 1"))
        self.repo.add(Task(id=0, title="Task 2"))
        tasks = self.repo.get_all()
        self.assertEqual(len(tasks), 2)

    def test_get_by_id(self):
        added_task = self.repo.add(Task(id=0, title="Find Me"))
        retrieved_task = self.repo.get_by_id(added_task.id)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.title, "Find Me")

    def test_get_by_id_not_found(self):
        task = self.repo.get_by_id(999)
        self.assertIsNone(task)

if __name__ == '__main__':
    unittest.main()
