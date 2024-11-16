

class Project:
    def __init__(self):
      self.projects = {}
    
    def Add_pro(self , new_pro ):
        if new_pro in self.projects:
            raise ValueError(f" project '{new_pro}' Already exist ! ! ")
        self.projects[new_pro] = [] # empty space for the new project tasks
                     
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
