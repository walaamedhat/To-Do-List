# KRW To-Do List

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Run the application](#run-the-application)
   - [How to Add Tasks](#how-to-add-tasks)
   - [Task Management](#task-management)
4. [Features](#features)
5. [File Structure](#file-structure)
6. [How It Works](#how-it-works)
7. [Testing](#testing)
8. [Acknowledgements](#acknowledgements)

---

## Project Overview
The **KRW To-Do List** application is a Python-based task management system built using the Tkinter library for the graphical user interface (GUI). It allows users to manage tasks, assign priorities, move tasks between statuses, and track progress with a simple, user-friendly interface. Tasks are organized into three categories: **To-Do**, **Doing**, and **Done**.

Key features of the application:
- Create, edit, and delete tasks.
- Track tasks using a customizable priority (Low, Medium, High).
- Move tasks between different statuses.

---

## Installation

### Pre-requisites:
- **Python** 3.x
- **Tkinter** (usually comes pre-installed with Python)

### Steps:

1. **Clone the repository:**
   - HTTPS
   ```bash
   git clone https://github.com/walaamedhat/To-Do-List.git
   cd To-Do-List
   ```
   - SSH
     ```bash
      git clone git@github.com:walaamedhat/To-Do-List.git
      cd To-Do-List
      ```
     
2. **Install dependencies:**

   - **Tkinter** is usually included with Python, but if you need to install it manually:

     - **On Ubuntu:**
       ```bash
       sudo apt-get install python3-tk
       ```

     - **On macOS:**
       Tkinter comes pre-installed with Python from [python.org](https://www.python.org/downloads/). If you use Homebrew Python:
       ```bash
       brew install python-tk
       ```

     - **On Windows:**
       Tkinter is included with standard Python installations. No extra steps are needed.

---

## Usage

#### Run the application:
- After you’ve cloned the repository and ensured dependencies are installed, run the following command:
> ```bash
> python main.py
> ```

#### How to Add Tasks:
- Launch the app, and in the input field at the top, type the title of the task.
- Choose a priority (Low, Medium, or High) using the dropdown.
- Click the Add button, or hit Enter (or Return) to create the task.
- The task will be added to the "To-Do" section.

#### Task Management:
- **Edit a Task:** To modify a task's title, click the ✎ (edit) button next to the task. After editing, press Enter to save the changes.

- **Delete a Task:** To remove a task, click the ✖ (delete) button next to the task. The task will be deleted permanently.

- **Move a Task:** To move a task between statuses (To-Do, Doing, Done), click on the status button and select a new status.

---

## Features

- **Priority Indicators:** Tasks are displayed with colored circles that represent their priority:
  🟢 High 🟠 Medium 🔴 Low

- **Task Categories:** Tasks are organized into three categories: To-Do, Doing, and Done.

- **Task Editing and Deletion:** Tasks can be edited or deleted at any time.

- **Task Persistence:** Task data remains available during the session.

---

## File Structure

```
KRW-ToDo-App/
├── main.py                # App entry point
├── task_manager.py        # Logic for managing tasks (TaskManager class)
├── ui_components.py       # Tkinter GUI code (TaskListUI class)
├── test_task_manager.py   # Unit tests for task_manager.py
└── README.md              # Project documentation
```
- [`main.py`](https://github.com/walaamedhat/To-Do-List/blob/main/main.py): The entry point for running the application.
- [`task_manager.py`](https://github.com/walaamedhat/To-Do-List/blob/main/task_manager.py): Contains logic to manage tasks, such as adding, removing, editing, and changing task statuses.
- [`ui_components.py:`](https://github.com/walaamedhat/To-Do-List/blob/main/ui_components.py): Contains the Tkinter GUI components, including task display, input fields, and buttons.
- [`test_task_manager.py:`](https://github.com/walaamedhat/To-Do-List/blob/main/test_task_manager.py): Contains unit tests for the task manager functions.

---

## How It Works

1. **Task Manager (task_manager.py):**
    - The TaskManager class is responsible for managing tasks. It stores tasks in a list, validates task input, and handles adding, removing, editing, and completing tasks.
    
2. **Task Representation:**
    - Tasks are stored as dictionaries with the following structure:
        ```
        {
            "id": <int>,            # Unique task ID
            "title": <str>,         # Task title
            "status": <str>,        # Task status (To-Do, Doing, Done)
            "priority": <str>,      # Task priority (Low, Medium, High)
        }

        ```
3. **User Interface (ui_components.py):**

    - The GUI is created using Tkinter. It consists of an input area for task creation, three columns to represent each status (To-Do, Doing, Done), and various buttons to manage tasks.
    - Each task is represented with its title, priority circle, and actions (edit, delete, move).

4. **Task Movement:**
    - Users can move tasks between the columns using a drop-down menu associated with each task.

---

## Testing

The project comes with a set of unit tests for the task manager logic to ensure that tasks are being managed properly. You can run the tests using ```pytest``` or any other testing framework you prefer.

#### Running the Tests:

1. **Install pytest:**
    ```bash
    pip install pytest
    ```
2. **Run tests:**
    ```bash
    pytest test_task_manager.py
    ```

Tests cover various operations such as adding tasks, removing tasks, editing tasks, and checking tasks by status.

---

## Acknowledgements

- Tkinter for providing the GUI toolkit.
- Python's built-in libraries for helping with task management and testing.


