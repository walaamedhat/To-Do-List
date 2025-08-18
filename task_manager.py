# task_manager.py

# ToDo List to keep track of task and should be a dictionary
# Ex: [{"task_id": 1, "title": "AUC Class", "status": "To Do", "priority": "High" }]
# Task_id => Number
# Title => String
# Status => String ("To Do" / "Doing" / "Done")
# Priority => String ("High" / "Medium" / "Low")

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self._next_id = 1

    # Function to validate task, task will be a dictionary
    def validation(self, task_input):
        for field in ["title", "status", "priority"]:
            if field not in task_input:
                raise ValueError(f"Missing required field: {field}")

        valid_statuses = ["Todo", "Doing", "Done"]
        valid_priorities = ["Low", "Medium", "High"]

        if task_input["status"].title() not in valid_statuses:
            raise ValueError(f"Invalid status: {task_input['status']}. Must be one of {valid_statuses}")

        if task_input["priority"].title() not in valid_priorities:
            raise ValueError(f"Invalid priority: {task_input['priority']}. Must be one of {valid_priorities}")

        return True

    # Function to add a new task, task will be a dictionary
    def add_task(self, task_data):
        if self.validation(task_data):
            task = {
                "id": self._next_id,
                **task_data
            }
            self.tasks[self._next_id] = task  # Store task by id for fast lookup
            self._next_id += 1
            return task  # Return the added task

    # Function to get tasks by status
    def get_tasks_by_status(self, status):
        tasks_by_status = [task for task in self.tasks.values() if task["status"].lower() == status.lower()]
        return tasks_by_status

    # Function to remove a task by ID
    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task with ID {task_id} has been removed successfully!")
            return True
        else:
            print(f"Task with ID {task_id} not found!")
            return False

    # Function to mark a task as completed
    def complete_task(self, task_id):
        return self.edit_task(task_id, 'status', 'Done')

    # Function to get a task by ID
    def get_task(self, task_id):
        return self.tasks.get(task_id, None)

    # Function to edit a task
    def edit_task(self, task_id, field, new_value):
        task = self.tasks.get(task_id)
        if task:
            if field in task:
                task[field] = new_value
                print(f"Task {task_id} updated: set {field} to {new_value}")
                return task
            else:
                print(f"Field '{field}' does not exist in task {task_id}.")
                return None
        else:
            print(f"Task with ID {task_id} not found!")
            return None

