from task import *

class Project :
    ####### Add project #########
    name_List={}
    def __init__(self , project_name ):
        if project_name not in Project.name_List:
             self.project_name = project_name
             Project.name_List[project_name] = self
             self.task_list ={}    
        else : 
            raise ValueError("This project Already exists ! ")
        
    ######### >>>>>>......painful method for nigger class to add tasks to project........<<<<<<<      
    def task_list_update(self ,task_id , task_obj ):
        """Add tasks to this project's task list """
        if task_id not in self.task_list :
            print("nigga leave me alone ") #### remove this later 
            self.task_list[task_id] = task_obj
        else: 
            raise ValueError(f"'{task_id}' this task ID already exist ! ")    
         
           
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
        
    ####### Diaplay Projects List ##########     >>>>I need to add task len for each pro<<<<
    @classmethod
    def Display_pro(cls):
        if not cls.name_List:
            print("No Project has made yet :3 ")
        else :
            print("Projects :")
            for name,pro in cls.name_List.items():    
               print(f"-{name} , tasks {len(pro.task_list)}")    
             
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

p1.Remove_pro()
Project.Display_pro()
p3 = Project("html")


print(p3.task_list)