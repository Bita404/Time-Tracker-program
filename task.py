from project import *
import datetime 

####>>>>>>>  Add Task <<<<<<<<
class Task(): 
    Last_taskID = 1000
    def __init__(self , name , description , association ):
        self.ID = Task.gen_TID()
        #super().__init__(self)
        self.name = name 
        self.description = description
        self.association = self.check_association(association)
        self.status = False 
        self.start_time = None
        self.end_time = None
        self.duration = None
        
    def check_association(self, related_pro):
        if related_pro not in Project.name_List:
            raise ValueError(f"'{related_pro}' Project Not Exists ! ! ") 
        
        good_project = Project.name_List[related_pro]
        good_project.task_list_update(self.ID, self) 
        return good_project

            
                
    #########..... ID generator like Task1001   ....########
    @classmethod
    def gen_TID(cls):
        ID = "Task" + str(cls.Last_taskID)
        cls.Last_taskID += 1 
        return ID
    
  ###############        >>>>>>  time validation  <<<<<<<<    
    def valid_time(self, time_input):
        """
        Validates the time that if its float and between 1 and 24 representing hours 
        """
        try:
            time_float = float(time_input)
            if not (1 <= time_float <= 24):
                raise ValueError(f" '{time_input}' Invalid time ! time must be between 1 and 24 ! ! ! ")
            return time_float
        except ValueError as e:
            raise ValueError(f"Invalid time'{time_input}' Enter a valid float ! ! ") from e
        
 #######        >>>>>>>> Edit <<<<<<< 
    def Edit_task(self , name=None , description= None  , status = None, start_time =None, end_time=None ):
        """
        edit any detail of the tasks like name , description , status and start or end time 
        """
        if name :
            self.name = name 
        if description:
            self.description = description
        if status :
            if bool(status) == True:
                self.status = True
            else :
                self.status = False
        if start_time :        
            self.start_time = self.valid_time(start_time)  
        if end_time :
            self.end_time = self.valid_time(end_time)              
                        
   #   >            >>>>>>>>>>>>> duration <<<<<<<<<<<<<<<<< 
    def time_Duration(self):
        """
        calculate the time between start and end ~
        """
        if self.start_time is None or self.end_time is None:
            raise ValueError("No time set for start time or end time !!! ")
        if self.end_time >= self.start_time :
            self.duration = self.end_time - self.start_time
        else :
             self.duration = self.end_time + (24 - self.start_time) 
        return self.duration         
    
    def Remove_task(self):       #################### HELPPPPPPPPPPPPPPPPPPPPPPPPP <<<<<<sjdlasghdfpiasgd
        pass
        
    
    def Mark_task(self):
        self.status = True
        return self.status
    
    
if __name__ == "__main__" :   
     t1 = Task("food"  ,  "good for health" , "html" )
     #t2 =Task("homeWork" , "good for grades " ,"school")
     #print(t2.__dict__)
     #print(t1.__dict__)
     #t3 =Task("break" , "arrrrrrrrr" , "rest")
     #t3.Edit_task(name ="sleep",status= True ,start_time="8" , end_time=12)
     #print(t3.__dict__)
     #print(t3.time_Duration()) 