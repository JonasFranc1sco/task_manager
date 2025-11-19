from typing import List
from .interfaces import ITaskRepository
from .models import Task

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self._db: List[Task] = []
        
    def add(self, task: Task):
        self._db.append(task)
        
    def list_all(self) -> List[Task]:
        return self._db
    