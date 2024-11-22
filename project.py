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
                 raise ValueError(f"Task '{task_to_add.name}' does not belong to project '{self.project_name}'!")
            self.task_list[task_to_add.ID] = task_to_add
        elif isinstance(task_to_add, str):  #>>>>>>>> If its a task ID 
            for project in Project.name_List.values():
                 if task_to_add in project.task_list:
                    task = project.task_list[task_to_add]
                    if task.association != self.project_name:
                        raise ValueError(f"Task '{task.name}' does not belong to project '{self.project_name}'!")
                    self.task_list[task.ID] = task
                    return
            raise ValueError(f"Task with ID '{task_to_add}' not found!")
        else:
            raise TypeError("Invalid input! Provide a Task object or a valid task ID.") 
        ########################## another way to do that :
        #if not isinstance(task, Task):
        #    raise ValueError("Only instances of Task can be added.")
        #if task.ID in self.task_list:
        #    raise ValueError(f"Task ID '{task.ID}' already exists in the project '{self.project_name}'.")
        #self.task_list[task.ID] = task     
        
         
    ######### >>> edit a project <<< ###########
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
                return f"No project found with name '{project_name}'"
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
                return f"No tasks found with name '{task_name}'"
            print(f"\nTasks Found with Name '{task_name}':")
            for project_name, task in found_tasks:
                print(f"Project: {project_name} | Task ID: {task.ID} | Name: {task.name} | Description: {task.description} "
                      f"| Status: {'Done' if task.status else 'Not Done'} | Start: {task.start_time} | End: {task.end_time} "
                      f"| Duration: {task.duration}")
            return found_tasks

        else:
            return "Provide either a project name or task name to search!"

    ########>>>>>>>>>>>> REMOVE Functions <<<<<<<<<<###########
    ##.....remove task
    def Remove_task(self, task_id):       
        if task_id in self.task_list:
            del self.task_list[task_id]
        else:
            raise ValueError(f"Task ID '{task_id}' not found in project '{self.project_name}'.")     
    ##......remove project
    def Remove_project(self):
        if self.project_name not in Project.name_List : 
            raise ValueError(f"'{self.project_name}' Invalid project ! ! ")
        del Project.name_List[self.project_name]
        
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
Project.Remove_task("Task2000")

Project.Display_pro()

p1.Edit_pro( "bake")
print(p1)

p1.Remove_pro()
Project.Display_pro()
p3 = Project("html")

Project.Search("CLI")
Project.Search(task_name= "food")

print(p3.task_list)