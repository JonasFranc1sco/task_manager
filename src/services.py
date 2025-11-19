from .models import Task, User, Status
from .interfaces import ITaskRepository

class TaskFactory:
    @staticmethod
    def create_task(title: str, description: str, owner_name: str) -> Task:
        user = User(owner_name)
        return Task(title, description, user)
    
class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository
        
    def create_new_task(self, title: str, description: str, owner_name: str):
        task = TaskFactory.create_task(title, description, owner_name)
        self.repository.add(task)
        return task
    
    def list_tasks(self):
        return self.repository.list_all()
    
    def complete_task(self, task_index: int):
        tasks = self.repository.list_all()
        if 0 <= task_index < len(tasks):
            tasks[task_index].set_status(Status.COMPLETED)
    