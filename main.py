from src.repositories import InMemoryTaskRepository
from src.services import TaskService
from src.views import ConsoleView

if __name__ == "__main__":
    
    repo = InMemoryTaskRepository()
    service = TaskService(repo)
    view = ConsoleView(service)
    
    view.start()