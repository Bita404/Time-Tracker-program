from project import *
import sys
from task import *

def main():
    while True:
        print("\n xX--- Time Trackere App ---Xx")
        print("1. Add Project")
        print("2. Add Task")
        print("3. Edit Project")
        print("4. Edit Task")
        print("5. Remove Project or Task")  # it has 2 options
        print("6. Mark a Task as Done ")
        print("7. Display")  # it has 2 options
        print("8. Search")   # 2 options 
        print("9. Save Data ")  # data export
        print("10. Exit")
        
        
        answer = input("Choose an option ! ! (1-10): ")
        
        
        ###################>>>>>>>> ADD PROJECT
        if answer =="1":
            project_name = input("Enter the project name: ")
            
            try:
                Project(project_name)
                print(f"Project '{project_name}' Created Successfully ^^ ")
            except ValueError as e:
                print(e)
                
        #######################>>>> ADD TASK TO PROJECT        
        elif answer =="2":
            project_name = input("Enter the project for the association : ")
            project = Project.name_List.get(project_name)
            if not project:
                print(f"Project '{project_name}' Not Found !!!! ")
            else:
                task_name = input("Enter task name: ")
                description = input("Enter task description : ")
                
                try:
                    task = Task(task_name, description, project_name)
                    project.Add_data(task)
                    print(f"Task '{task_name}' Added to '{project_name}' Successfully ^^ !")
                    
                except ValueError as e:
                    print(e)
                    
        ######################>>>>>> EDIT PROJECT        
        elif answer =="3":
            old_name = input("Enter the project name to edit  : ")
            project = Project.name_List.get(old_name)
            if not project:
                print(f"Project '{old_name}' Not Found ! ! ")
            else:
                new_name = input("Enter the new name : ")
                try:
                    project.Edit_pro(new_name)
                    print(f"Project '{old_name}' Updated to '{new_name}' Successfully ^^ !")
                    
                except ValueError as e:
                    print(e)
                    
        ########################>>>>>> EDIT TASK            
        elif answer =="4":
            pass
        elif answer =="5":
            pass
        elif answer =="6":
            pass
        elif answer =="7":
            pass
        elif answer=="8":
            pass
        elif answer=="9":
            pass
        elif answer=="10":
            print("ok Goodbye (*＾▽＾)／  Exiting ...")
            break
        else :
            print("Invalid choice ! ! ! Please choose a number (1-10) :3 ")