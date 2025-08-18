# main.py

import tkinter as tk
from task_manager import TaskManager
from ui_components import TaskListUI


def main():
    # Create the main Tkinter window
    root = tk.Tk()

    # Initialize TaskManager to manage tasks
    task_manager = TaskManager()

    # Initialize the UI and pass the root window and TaskManager instance
    TaskListUI(root, task_manager)

    # Start Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()
