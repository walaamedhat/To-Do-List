from task_manager import *

def test_add_task():
    tasks.clear()
    task = {"title": "Hit the gym", "priority": "High", "status": "To Do", "description": "Leg day"}
    add_task(task)
    assert tasks[0] == task

g