
from abc import ABC , abstractmethod

class All(ABC):
    def __init__(self, task ):
        self.task = task 
        
    def __str__(self):
        return f"Projects : {self.project} , Task : {self.task}"  
    
      
    @abstractmethod
    def tasks_len():
        pass