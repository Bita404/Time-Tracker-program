from task import*

class ProjectManager:
    def __init__(self):
        self.projects = {}  # Store all projects by name
        self.tasks = {}  # Store all tasks by ID

    def add_project(self, project):
        if project.project_name in self.projects:
            raise ValueError(f"Project '{project.project_name}' already exists!")
        self.projects[project.project_name] = project

    def add_task(self, task):
        if task.ID in self.tasks:
            raise ValueError(f"Task with ID '{task.ID}' already exists!")
        self.tasks[task.ID] = task

        # Link task to its associated project
        project = self.projects.get(task.association)
        if not project:
            raise ValueError(f"Project '{task.association}' does not exist!")
        project.Add_data(task)

    def display(self, obj_type=None):
        """
        Display projects or tasks based on the object type.
        """
        if obj_type == "projects":
            print("\n--- Projects ---")
            for name, project in self.projects.items():
                print(f"Project Name: {name}, Number of Tasks: {len(project.task_list)}")
        elif obj_type == "tasks":
            print("\n--- Tasks ---")
            for task_id, task in self.tasks.items():
                print(f"Task ID: {task.ID}, Name: {task.name}, Project: {task.association}")
        else:
            print("\n--- All Data ---")
            self.display("projects")
            self.display("tasks")

    def remove(self, obj_id):
        """
        Remove a task or project by ID.
        """
        if obj_id in self.tasks:  # Remove a task
            task = self.tasks.pop(obj_id)
            project = self.projects.get(task.association)
            if project:
                del project.task_list[task.ID]
            return f"Task '{obj_id}' removed successfully."
        elif obj_id in self.projects:  # Remove a project
            project = self.projects.pop(obj_id)
            for task_id in list(project.task_list.keys()):
                del self.tasks[task_id]
            return f"Project '{obj_id}' removed successfully."
        else:
            return f"No project or task found with ID '{obj_id}'."

    def search(self, obj_type, **kwargs):
        """
        Search projects or tasks by attributes.
        """
        results = []
        if obj_type == "projects":
            for project in self.projects.values():
                if all(getattr(project, key, None) == value for key, value in kwargs.items()):
                    results.append(project)
        elif obj_type == "tasks":
            for task in self.tasks.values():
                if all(getattr(task, key, None) == value for key, value in kwargs.items()):
                    results.append(task)
        return results

    def edit(self, obj_id, **kwargs):
        """
        Edit a project or task by ID.
        """
        if obj_id in self.tasks:
            task = self.tasks[obj_id]
            task.Edit_task(**kwargs)
            return f"Task '{obj_id}' updated successfully."
        elif obj_id in self.projects:
            project = self.projects[obj_id]
            if "project_name" in kwargs:
                new_name = kwargs["project_name"]
                project.Edit_pro(new_name)
                self.projects[new_name] = self.projects.pop(project.project_name)
            return f"Project '{obj_id}' updated successfully."
        else:
            return f"No project or task found with ID '{obj_id}'."

# Example usage
if __name__ == "__main__":
    # Create a project manager
    pm = ProjectManager()

    # Create projects
    p1 = Project("cake")
    
    pm.add_project(p1)
    pm.add_project(p2)

    # Create tasks
    t1 = Task("baking", "Bake the cake", "cake")
    t2 = Task("debugging", "Fix bugs", "CLI")
    pm.add_task(t1)
    pm.add_task(t2)

    # Display all projects and tasks
    pm.display()

    # Remove a task
    print(pm.remove("Task1000"))
    pm.display("tasks")

    # Search for a project
    search_results = pm.search("projects", project_name="CLI")
    for project in search_results:
        print(f"Found project: {project.project_name}")

    # Edit a project
    print(pm.edit("CLI", project_name="Command Line Interface"))
    pm.display("projects")
