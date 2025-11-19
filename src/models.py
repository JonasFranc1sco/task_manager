from enum import Enum
from .interfaces import IObserver, ISubject

class Status(Enum):
    PENDING = "Pendente"
    IN_PROGRESS = "Em Andamento"
    COMPLETED = "Concluída"
    
class User(IObserver):
    def __init__(self, name: str):
        self.name = name
        
    def update(self, message: str):
        print(f"[NOTIFICAÇÃO para {self.name}]: {message}")
        
class Task(ISubject):
    def __init__(self, title: str, description: str, owner: User):
        self.title = title
        self.description = description
        self.status = Status.PENDING
        self.owner = owner
        self._observers = []
        self.attach(owner)
        
    def attach(self, observer: IObserver):
        if observer not in self._observers:
            self._observers.append(observer)
        
    def notify(self):
        for observer in self._observers:
            observer.update(f"A tarefa '{self.title}' mudou para: {self.status.value}")
            
    def set_status(self, new_status: Status):
        self.status = new_status
        self.notify()
        
    def __str__(self):
        return f"[{self.status.value}] {self.title} (Resp: {self.owner.name})"
        