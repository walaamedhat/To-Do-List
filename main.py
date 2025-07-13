# main.py

import tkinter as tk
# from task_manager import add_task, remove_task, get_tasks
import ui_components

def main():
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("800x800")

    # UI setup
    ui_components.create_welcome_label(root)

    task_entry = ui_components.create_task_entry(root)
    tasks_frame = ui_components.create_tasks_frame(root)

    ui_components.create_add_button(root, command=task_entry)

    root.mainloop()

if __name__ == "__main__":
    main()
