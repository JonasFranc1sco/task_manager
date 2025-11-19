from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update(self, message: str):
        pass
    
class ISubject(ABC):
    @abstractmethod
    def attach(self, observer: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass
    
class ITaskRepository(ABC):
    @abstractmethod
    def add(self, task):
        pass
    
    @abstractmethod
    def list_all(self):
        pass