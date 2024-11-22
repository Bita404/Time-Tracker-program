####>>>>>>>  Add Task <<<<<<<<
class Task: 
    Last_taskID = 1000
    def __init__(self , name , description , association ):
        self.ID = Task.gen_TID()
        self.name = name 
        self.description = description
        self.association = association
        self.status = False 
        self.start_time = None
        self.end_time = None
        self.duration = None
        
    #########..... ID generator like Task1001   ....########
    @classmethod
    def gen_TID(cls):
        ID = "Task" + str(cls.Last_taskID)
        cls.Last_taskID += 1 
        return ID
    
  ######       >>>>>>  time validation  <<<<<<<<    
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
        
 #######> >>>>>>> Edit <<<<<<< 
    def Edit_task(self , name=None , description= None  , status = None, start_time =None, end_time=None , duration= None ):
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
                if start_time :        
                     self.start_time = self.valid_time(start_time)  
                if end_time :
                     self.end_time = self.valid_time(end_time)   
                if start_time is not None and end_time is not None:
                     self.duration = self.time_Duration()
            else :
                self.status = False
                self.start_time = None
                self.end_time = None
                self.duration = None    
                        
   #   >>>>>>>>>>>>> duration <<<<<<<<<<<<<<<<< 
    def time_Duration(self):
        """
        calculate the time between start and end ~
        """
        if self.end_time >= self.start_time :
            self.duration = self.end_time - self.start_time
        else :
             self.duration = self.end_time + (24 - self.start_time) 
        return self.duration   
          
    #####..... Mark as Done ....####    
    def Mark_task(self):
        self.status = True
        return self.status 
    
    
if __name__ == "__main__" :    
     t1 = Task("food"  ,  "good for health" , "html" )
     t2 =Task("homeWork" , "good for grades " ,"school")
     print(t2.__dict__)
     print(t1.__dict__)
     t3 =Task("break" , "arrrrrrrrr" , "rest")
     t3.Edit_task(name ="sleep" ,start_time="8" , end_time=12)
     print(t3.__dict__)
    
     t3.Mark_task()
     print(t3.__dict__)
     