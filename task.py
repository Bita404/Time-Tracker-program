from project import Project 
import datetime 

class Task(Project): 
    def __init__(self , name , ID , description , start_time , end_time, duration, pro_association ,  status=False ):
        super().__init__()
        self.name = name 
        self.ID = ID
        ID = 1000
        self.description = description
        self.status = status 
        self.start_time = start_time
        self.end_time = end_time 
        self.duration = duration
        self.pro_association = pro_association  
    
    def Add_task(self):
        pass
    
    def Edit_task():
        pass
    
    def Remove_task():
        pass
    
    def Mark_task():
        pass
    