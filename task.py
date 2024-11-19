from project import Project 
import datetime 

class Task(): 
    Last_taskID = 1000
    def __init__(self , name , description , association ):
        self.ID = Task.gen_TID()
        #super().__init__()
        self.name = name 
        self.description = description
        self.association = association
        status = False 
        start_time = None
        end_time = None
        duration = None
        
        
    @classmethod
    def gen_TID(cls):
        ID = "Task" + str(cls.Last_taskID)
        cls.Last_taskID += 1 
        return ID
    
    def Add_task(self , realeted_pro):
        pass
    
    def Edit_task():
        pass
    
    def Remove_task():
        pass
    
    def Mark_task():
        pass
    
    
if __name__ == "__main__" :   
     t1 = Task("eat"  ,  "good for health" , "food" )
     t2 =Task("homeWork" , "good for grades " ,"school")
     print(t2.__dict__)
     print(t1.__dict__)
