

class Project :
    name_List={}
    def __init__(self , project_name ):
        if project_name not in Project.name_List:
             self.project_name = project_name
             Project.name_List[project_name] = self     
        else : 
            raise ValueError("This project Already exists ! ")   
      
    
    #def Add_pro(self , new_pro ):
    #    if new_pro in self.projects:
    #        raise ValueError(f" project '{new_pro}' Already exist ! ! ")
    #    self.projects[new_pro] = [] # empty space for the new project tasks
                     
    def Edit_pro(self,  old_name , new_name):
        if old_name not in self.projects :
             raise ValueError(f"'{old_name}' Invalid project name ! ")
        if new_name in self.projects :
              raise ValueError(f" '{new_name}' Already exist  !!! try another name")
    
    def Remove_pro(self , rem_pro):
        if rem_pro in self.projects : 
            raise ValueError(f"'{rem_pro}' Invalid project ! ! ")
        del self.projects[rem_pro]
    
    def Display_pro(self):
        if not self.projects :
            print(" No Projects Found ! ! ")
        else :
           print(f"{self.projects}")    
             
    def __str__(self):
        return f"project : {self.project_name}"       

p1 =Project("cake")
print(p1)
p2 =Project("CLI")
print(p2)
p3=Project("cake")
print(p3)
