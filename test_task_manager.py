from task_manager import Task, TaskManager

# Sample tasks for setup
tasks = [
    Task("Task One", status="Todo", priority="High"),
    Task("Task Two", status="Doing", priority="Low"),
    Task("Task Three", status="Todo", priority="Medium")
]


def setup():
    """Helper function to set up initial tasks for testing."""
    tm = TaskManager()
    # Add tasks using the task objects from the tasks array
    for task in tasks:
        tm.add_task({"title": task.title, "status": task.status, "priority": task.priority})
    return tm


def test_add_task():
    tm = setup()  # Setup adds all tasks automatically

    # New task to add
    new_task = Task("Go to the AUC", status="Todo", priority="High")

    # Add the task
    tm.add_task({"title": new_task.title, "status": new_task.status, "priority": new_task.priority})

    # Expected task (with ID assigned)
    expected = new_task
    expected.id = 4  # Assuming the next ID will be 4

    # Fetch the actual task added
    actual = tm.get_task(4)

    assert actual.id == expected.id
    assert actual.title == expected.title
    assert actual.status == expected.status
    assert actual.priority == expected.priority


def test_get_tasks_by_status():
    tm = setup()  # Setup adds all tasks automatically

    # Fetch tasks by status
    todo_tasks = tm.get_tasks_by_status("Todo")
    doing_tasks = tm.get_tasks_by_status("Doing")

    # Test exact match for "Todo" tasks
    assert len(todo_tasks) == 2
    assert todo_tasks[0].title == "Task One"
    assert todo_tasks[1].title == "Task Three"

    # Test exact match for "Doing" tasks
    assert len(doing_tasks) == 1
    assert doing_tasks[0].title == "Task Two"


def test_remove_task():
    tm = setup()  # Setup adds all tasks automatically

    # Remove task with ID 1 ("Task One")
    result = tm.remove_task(1)
    assert result is True, f"Expected {True}, but got {result}"

    # Ensure the task is removed
    assert tm.get_task(1) is None


def test_complete_task():
    tm = setup()  # Setup adds all tasks automatically

    # Mark task with ID 1 as "Done"
    updated_task = tm.complete_task(1)  # Task "Task One"

    assert updated_task.status == "Done", f"Expected status 'Done', but got {updated_task.status}"


def test_edit_task():
    tm = setup()  # Setup adds all tasks automatically

    # Edit task with ID 1 ("Task One") and change the title
    updated_task = tm.edit_task(1, 'title', 'Updated Task One')

    assert updated_task.title == "Updated Task One", f"Expected title 'Updated Task One', but got {updated_task.title}"


def test_task_validation():
    tm = TaskManager()

    # Valid task data
    valid_task = {"title": "Valid Task", "status": "Todo", "priority": "High"}
    assert tm.validation(valid_task) is True

    # Invalid task data (missing title)
    invalid_task = {"status": "Todo", "priority": "Low"}
    try:
        tm.validation(invalid_task)
    except ValueError as e:
        assert str(e) == "Title is required", f"Expected validation error for missing title, got {e}"

    # Invalid task data (wrong status)
    invalid_status_task = {"title": "Invalid Status Task", "status": "Invalid", "priority": "Low"}
    try:
        tm.validation(invalid_status_task)
    except ValueError as e:
        assert str(
            e) == "Status must be one of ['Todo', 'Doing', 'Done']", f"Expected validation error for invalid status, got {e}"
