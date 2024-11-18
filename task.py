from project import Project 
import datetime 

class Task(Project): 
    def __init__(self , name , ID , description , association ):
        super().__init__()
        self.name = name 
        self.ID = ID
        ID = 1000
        self.description = description
        status = False 
        start_time = None
        end_time = None
        duration = None
    
    def Add_task(self):
        pass
    
    def Edit_task():
        pass
    
    def Remove_task():
        pass
    
    def Mark_task():
        pass
    