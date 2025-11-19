import unittest
from src.services import TaskService
from src.repositories import InMemoryTaskRepository
from src.models import Status

class TestTaskSystem(unittest.TestCase):
    
    def setUp(self):
        self.repo = InMemoryTaskRepository()
        self.service = TaskService(self.repo)

    def test_create_task(self):
        task = self.service.create_new_task("Estudar Python", "SOLID e Patterns", "Dev")
        self.assertEqual(task.title, "Estudar Python")
        self.assertEqual(len(self.repo.list_all()), 1)

    def test_observer_notification(self):
        # Este teste valida se o status muda corretamente
        task = self.service.create_new_task("Deploy", "Prod", "DevOps")
        self.assertEqual(task.status, Status.PENDING)
        
        self.service.complete_task(0)
        updated_task = self.repo.list_all()[0]
        
        self.assertEqual(updated_task.status, Status.COMPLETED)

if __name__ == '__main__':
    unittest.main()