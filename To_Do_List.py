# task_manager.py

# ToDo List to keep track of task and should be dictionary
# Ex: [{"task_id": 1, "title": "AUC CLass", "priority": "High", "status": "To Do", "description": "Python Class" }]
# Task_id => Number
# Title => String
# Priority => String ("High" / "Medium" / "Low")
# Status => String ("To Do" / "Doing" / "Done")
# Description => String

class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    # ToDo => Function to validate task, task will be a dictionary
    def validation(self, task_input):
        
        for field in ["title", "priority", "status"]:
            if field not in task_input:
                raise ValueError(f"Missing required field: {field}")

        if task_input["priority"] not in ["Low", "Medium", "High"]:
                raise ValueError(f"Invalid priority: {task_input['priority']}. Must be one of ['Low', 'Medium', 'High']")

        if task_input["status"] not in ["To Do", "In Progress", "Done"]:
                raise ValueError(f"Invalid status: {task_input['status']}. Must be one of ['To Do', 'In Progress', 'Done']")
        pass

    # ToDo => Function to add a new task, task will be a dictionary
    def add_task(self, task_data):
        # write your code here
        for field in ["title", "priority", "status"]:
            if field not in task_data:
                raise ValueError(f"Missing required field: {field}")

            if task_data["priority"] not in ["Low", "Medium", "High"]:
                raise ValueError(f"Invalid priority: {task_data['priority']}. Must be one of ['Low', 'Medium', 'High']")

            if task_data["status"] not in ["To Do", "In Progress", "Done"]:
                raise ValueError(f"Invalid status: {task_data['status']}. Must be one of ['To Do', 'In Progress', 'Done']")
        task = {
            "id": self._next_id,
            **task_data
        }
        self.tasks.append(task)
        self._next_id += 1

    def get_tasks(self):
        return self.tasks

    def clear_tasks(self):
        self.tasks.clear()
        self._next_id = 1

    # ToDo => Function to remove a task by ID
    def remove_task(self, task_id):
        # write your code here
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
            print(f"Task with ID {task_id} removed successfully!")
            return
        raise ValueError(f"Task with ID {task_id} not found.")

        pass


    # ToDo => Function to mark a task as completed
    def complete_task(self, task_id):
        # write your code here
        pass


    # ToDo => Function to list all tasks
    def list_tasks(self):
        # write your code here
        pass


    # ToDo => Function to edit a task
    def edit_task(self, task_id, field, new_value):
        # write your code here
        pass