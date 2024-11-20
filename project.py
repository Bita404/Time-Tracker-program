
class Project :
    ####### Add project #########
    name_List={}
    def __init__(self , project_name ):
        if project_name not in Project.name_List:
             self.project_name = project_name
             Project.name_List[project_name] = self     
        else : 
            raise ValueError("This project Already exists ! ")   
       
    #########  edit a project  ###########
    def Edit_pro(self , new_name):
        if new_name  in Project.name_List :
             raise ValueError(f"'{new_name}' Already exist  !!! try another name ")
        del Project.name_List[self.project_name]
        self.project_name = new_name
        Project.name_List[new_name] = self
        
    ############## Remove a Project #########
    def Remove_pro(self):
        if self.project_name not in Project.name_List : 
            raise ValueError(f"'{self.project_name}' Invalid project ! ! ")
        del Project.name_List[self.project_name]
        
    ####### Diaplay Projects List ##########    
    @classmethod
    def Display_pro(cls):
        if not cls.name_List:
            print("No Project has made yet :3 ")
        else :
            print("Projects :")
            for name in cls.name_List:    
               print(f"-{name}")    
             
    def __str__(self):
        return f"project : {self.project_name}"       

###################################
p1 =Project("cake")
print(p1)
p2 =Project("CLI")
print(p2)
#p3=Project("cake")
#print(p3)

Project.Display_pro()

p1.Edit_pro( "bake")
print(p1)

Project.Display_pro()