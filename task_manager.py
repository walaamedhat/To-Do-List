# task_manager.py

# ToDo List to keep track of task and should be dictionary
# Ex: [{"task_id": 1, "title": "AUC CLass", "priority": "High", "status": "To Do" }]
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

    # ToDo => Function to add a new task, task will be a dictionary
    def add_task(self, task_data):
        task = {
            "id": self._next_id,
            **task_data
        }
        self.tasks.append(task)
        self._next_id += 1

    def get_tasks_by_status(self, status):
        print(self.tasks,'statusss')
        return [task for task in self.tasks if task["status"].lower() == status.lower()]

    def clear_tasks(self):
        self.tasks.clear()
        self._next_id = 1

    # ToDo => Function to remove a task by ID
    def remove_task(self, task_id):
        # write your code here
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
            print(f"Task with ID {task_id} has been removed successfully!")
            return
        raise ValueError(f"Task with ID {task_id} not found!.")

    # ToDo => Function to mark a task as completed
    def complete_task(self, task_id):
        result = self.edit_task(task_id, 'status', 'Done') 
        return result
        


    # ToDo => Function to list all tasks
    def list_tasks(self):
        # write your code here
        pass


    # ToDo => Function to edit a task
    def edit_task(self, task_id, field, new_value):
        for task in self.tasks:
            if task["id"] == task_id:
                if field in task:
                    task[field] = new_value  # Update the field
                    print(f"field with id :{task_id} updated to {new_value}")
                    break
            else:
                raise ValueError(f"Field '{field}' does not exist in the task.")
        
        else:
            raise ValueError(f"task with id {task_id} not found")


    
    