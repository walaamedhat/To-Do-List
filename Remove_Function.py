def remove_task(task_id):
    for task in tasks:
        if task["task_id"] == task_id:
            tasks.remove(task)
            print(f"Task with ID {task_id} removed successfully!")
            return
    raise ValueError(f"Task with ID {task_id} not found.")
