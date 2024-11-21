
from abc import ABC , abstractmethod

class ADD(ABC):
    Last_taskID = 1000
    def __init__(self):
        self.project_list ={}
        
    
    def Add_project(self, project_name ):
        if project_name not in self.project_list:
             self.project_name = project_name
             self.project.name_List[project_name] = self
             self.task_list ={}    
        else : 
            raise ValueError("This project Already exists ! ")
      
    def Add_task(self , name , description , association ):
        self.ID = ADD.gen_TID()
        self.name = name 
        self.description = description
        #### 
        if association in self.project_list : # to see if the project exist for adding task 
            self.association = association
            if self.ID not in self.task_list :
                self.task_list[self.ID]
            else :
                raise ValueError("This task already exists for this project ! ! ")    
             
        else :
            raise ValueError(f"'{association}' Project Not found to add task to it ! ! ")    
        
        
        
    @classmethod
    def gen_TID(cls):
        ID = "Task" + str(cls.Last_taskID)
        cls.Last_taskID += 1 
        return ID
        
        
    def __str__(self):
        return f"Projects : {self.project} , Task : {self.task}"  
    
      
    @abstractmethod
    def tasks_len():
        pass 
    
    
b1 = ADD.Add_project("cheese cake")
t1 = ADD.Add_task("cheese" , "for the cream" , "cheese cake")
    