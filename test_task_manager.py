# test_task_manager.py

from task_manager import TaskManager

def test_add_task():
    tm = TaskManager()
    task_input = {
        "title": "Go to the AUC",
        "priority": "High",
        "status": "To Do",
        "description": "Python Class"
    }

    tm.add_task(task_input)

    expected = {
        "id": 1,
        **task_input
    }
    print("Actual task:", tm.get_tasks()[0])
    print("Expected task:", expected)
    assert tm.get_tasks()[0] == expected
