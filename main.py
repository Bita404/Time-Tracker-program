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
            project_name = input("Enter the associated project : ")
            project = Project.name_List.get(project_name)
            if not project:
                print(f"Project '{project_name}' Not Found ! !  :3 ")
            else:
                task_id = input("Enter the task ID to Edit : ")
                task = project.task_list.get(task_id)
                if not task:
                    print(f"Task ID '{task_id}' does Not Found in project '{project_name}' ! ! :3 ")
                else:
                    name = input("write a new task name OR press enter to skip to next detail : ") or None
                    description = input("write a new task description OR press enter to skip to next detail: ") or None
                    status = input("Mark as done? enter 'yes' if done OR press enter to skip if No: ").lower() or None
                    start_time = input("Enter new start time (if u didnt mark ur task as done, time wont be saved !): ") or None
                    end_time = input("Enter new end time (if u didnt mark ur task as done, time wont be saved !): ") or None

                    try:
                        task.Edit_task(name=name, description=description, status=bool(status),
                                       start_time=start_time, end_time=end_time)
                        print(f"'{task_id}' updated Successfully ^^ !")
                        
                    except ValueError as e:
                        print(e)
                        
        #########################>>>>>>>> REMOVE
        elif answer =="5":
            option = input("Do you want to Remove a Project (1) OR a Task (2) ?? ")
            
            if option == "1":
                project_name = input("Enter the name of the project to Remove : ")
                try:
                    Project.Remove_project(project_name)
                    
                except ValueError as e:
                    print(e)
                    
            elif option == "2":
                project_name = input("Enter the Associated Project for the Task: ")
                project = Project.name_List.get(project_name)
                
                if not project:
                    print(f"Project '{project_name}' Nor Found ! ! ")
                else:
                    task_id = input("Enter the task ID to Remove : ")
                    try:
                        project.Remove_task(task_id)
                        print(f"Task '{task_id}' Removed Successfully ^^ !")
                        
                    except ValueError as e:
                        print(e)
            else:
                print("Invalid choice! !")
        ############################>>>>>> MARK        
        elif answer =="6":
            project_name = input("Enter the Associated Project for the task : ")
            project = Project.name_List.get(project_name)
            
            if not project:
                print(f"'{project_name}' Not Found ! !")
            else:
                task_id = input("Enter the task ID to Mark as Done : ")
                task = project.task_list.get(task_id)
                
                if not task:
                    print(f"ID '{task_id}' does Not Found in '{project_name}' Project ! !")
                else:
                    task.Mark_task()
                    print(f"Task '{task_id}' Marked as Done ^^ ! !")
                    
        #####################>>>>>>>>>>>>>>>> DISPLAY            
        elif answer =="7":
            option = input("Do you want to display all Projects (1) OR All Tasks in a Project (2) ? ")
            if option == "1":
                
                Project.Display_pro()
                
            elif option == "2":
                project_name = input("Enter the project name: ")
                project = Project.name_List.get(project_name)
                if not project:
                    print(f"Project '{project_name}' Not Found ! ! !")
                else:
                    for task in project.task_list.values():
                        print(task)
            else:
                print("womp womp ! Invalid choice ! !")
            
        ######################>>>>>>>>>>>>>> SEARCH        
        elif answer=="8":
            option = input("Do you want to search for a Project (1) OR a Task (2) ? ")
            if option == "1":
                project_name = input("Enter the project name to Search : ")
                Project.Search(project_name=project_name)
                
            elif option == "2":
                task_name = input("Enter the task name to Search : ")
                Project.Search(task_name=task_name)
            else:
                print(" brrrr... Invalid choice ! !")
                
        ######################>>>>>>>>>>>>>>> SAVE DATA        
        elif answer=="9":
            project_name = input("Enter the Project name to Save its data : ")
            project = Project.name_List.get(project_name)
            
            if not project:
                print(f"'{project_name}' Not Found ! !")
            else:
                filename =input("Enter a name for the Saving File :")
                project.txt_file(f"{filename}")
                
        ############################>>>>>>>>>>> EXIT        
        elif answer=="10":
            print("ok Goodbye (*＾▽＾)／  Exiting ...")
            break
        else :
            print("Invalid choice ! ! ! Please choose a number (1-10) :3 ")
            
if __name__ == "__main__":
    main()            
            