import datetime
from task import *

class Project :
    #######>>>>>> Add project <<<<<<#########
    name_List={}
    def __init__(self , project_name ):    
        if project_name not in Project.name_List:
             self.project_name = project_name
             Project.name_List[project_name] = self
             self.task_list ={}    
        else : 
            raise ValueError("This project Already exists ! ")
        
    #######>>>>>>>> ADD AND ASSOCIATE TASK to a project <<<<<<<<<<<<<<<############
    def Add_data(self , task_to_add ): 
        if isinstance(task_to_add, Task):  #>>>>>>>> If its a Task object 
            if task_to_add.association != self.project_name:
                 raise ValueError(f"Task '{task_to_add.name}' does NOT belong to  '{self.project_name}' ! ! !")
            self.task_list[task_to_add.ID] = task_to_add
        elif isinstance(task_to_add, str):  #>>>>>>>> If its a task ID 
            for project in Project.name_List.values():
                 if task_to_add in project.task_list:
                    task = project.task_list[task_to_add]
                    if task.association != self.project_name:
                        raise ValueError(f"Task '{task.name}' does NOT belong to project '{self.project_name}'! ! !")
                    self.task_list[task.ID] = task
                    return
            raise ValueError(f"Task with '{task_to_add}' ID Not Found ! !")
        else:
            raise TypeError("Invalid input ! ! Enter an existing Task object or task ID ! ! ") 
         
    ############ >>> edit a project <<< ###########
    def Edit_pro(self , new_name):
        if new_name  in Project.name_List :
             raise ValueError(f"'{new_name}' Already exist  !!! try another name ")
        del Project.name_List[self.project_name]
        self.project_name = new_name
        Project.name_List[new_name] = self
        
    ######>>>>>>>>>>>> SEARCH for projects or tasks <<<<<<<<<<<<<<<##########
    @classmethod
    def Search(cls, project_name=None , task_name=None ):
        if project_name:
            project = cls.name_List.get(project_name)
            if not project:
                return f"No project Found named '{project_name}' ! ! ! "
            print(f"\nProject Found: {project.project_name}")
            print("Tasks:")
            for task in project.task_list.values():
                print(f"- {task.ID}: {task.name} | Status: {'Done' if task.status else 'Not Done'}")
            return project

        elif task_name:
            found_tasks = []
            for project in cls.name_List.values():
                for task in project.task_list.values():
                    if task.name == task_name:
                        found_tasks.append((project.project_name, task))
            if not found_tasks:
                return f"No '{task_name}' Found ! ! ! "
            print(f"\nTasks Found with Name '{task_name}':")
            for project_name, task in found_tasks:
                print(f"Project: {project_name} | Task ID: {task.ID} | Name: {task.name} | Description: {task.description} "
                      f"| Status: {'Done' if task.status else 'Not Done'} | Started at: {task.start_time} | Ended at: {task.end_time} "
                      f"| Duration time: {task.duration}")
            return found_tasks

        else:
            return "Provide either a project name or task name to search ! ! !"

    ########>>>>>>>>>>>> REMOVE Functions <<<<<<<<<<###########
    ##.....remove task
    def Remove_task(self, task_id):       
        if task_id in self.task_list:
            del self.task_list[task_id]
            print(f"'{task_id}' Task Removed Succesfully :3 ")
        else:
            raise ValueError(f"Task ID '{task_id}' Not Found in project '{self.project_name}'! ! !")     
    ##......remove project
    def Remove_project(self , pro_name):
        if pro_name not in Project.name_List :
            raise ValueError(f"'{pro_name}' Project Not Found ! !")
        else :
            del pro_name
            self.task_list.clear()
            print(f"Project '{pro_name}' and all its tasks Removed Succesfully :3 ")
            

    #######>>>>>>>>>>>> DISPLAY functions <<<<<<<<<<<<##########
    #.........project 
    @classmethod
    def Display_pro(cls):
        if not cls.name_List:
            print("No Project has made yet :3 ")
        else :
            print("Projects :")
            for name,pro in cls.name_List.items():    
               print(f"-{name} , tasks {len(pro.task_list)}")  
    #......task             
    def Display():
        pass
    
    ################ str #######################    
    def __str__(self):
        return f"project : {self.project_name}"  
    
    ############>>>>>>>>  DATA EXPORT TO TXT FILE <<<<<<<<########## 
    def txt_file():
        pass  

###################################
p1 =Project("cake")
print(p1)
p2 =Project("CLI")
print(p2)
t1 = Task("food"  ,  "good for health" , "CLI" )
p2.Add_data(t1)
#p3=Project("cake")
#print(p3)
p2.Remove_task("Task1000")

Project.Display_pro()

p1.Edit_pro( "bake")
print(p1)


Project.Display_pro()
p3 = Project("html")

Project.Search("CLI")
Project.Search(task_name= "food")

print(p3.task_list)