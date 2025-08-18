# ui_component.py

import tkinter as tk
from tkinter import ttk, messagebox

ICON_FONT = ("Arial", 10, "bold")

class TaskListUI:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.task_widgets = {}

        self.root.title("KRW To-Do List")
        self.root.geometry("800x800")
        self.root.configure()

        # Title
        header = tk.Label(self.root, text="🧠 Task Board", font=("Helvetica", 18, "bold"))
        header.pack(pady=10)

        # Add task area
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.task_entry = ttk.Entry(input_frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=10)

        # Priority dropdown
        self.priority_combobox = ttk.Combobox(input_frame, values=["Low", "Medium", "High"], width=10)
        self.priority_combobox.set("Medium")  # Set default priority to "Medium"
        self.priority_combobox.grid(row=0, column=1, padx=10)

        # Add button
        add_button = ttk.Button(input_frame, text="Add", command=self.add_task)
        add_button.grid(row=0, column=2, padx=10)

        # Bind Enter key to add_task method
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Container for 3 columns
        self.column_frame = tk.Frame(self.root, bg="white")
        self.column_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        self.todo_frame = self.create_section("📝 To Do")
        self.doing_frame = self.create_section("🔄 Doing")
        self.done_frame = self.create_section("✅ Done")

        self.refresh_task_list()

    def create_section(self, title):
        frame = tk.Frame(self.column_frame, bd=1, relief=tk.SOLID)
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

        label = tk.Label(frame, text=title, font=("Helvetica", 14, "bold"))
        label.pack(pady=5)

        container = tk.Frame(frame)
        container.pack(fill=tk.BOTH, expand=True)

        return container

    def refresh_task_list(self):
        print("Refreshing task list...")
        self.task_widgets.clear()  # Clear current widgets
        for section in [self.todo_frame, self.doing_frame, self.done_frame]:
            for widget in section.winfo_children():
                widget.destroy()

        # Add tasks to each section (To Do, Doing, Done)
        self.add_tasks_to_section("todo", self.todo_frame)
        self.add_tasks_to_section("doing", self.doing_frame)
        self.add_tasks_to_section("done", self.done_frame)

    def add_tasks_to_section(self, status, section_frame):
        tasks = self.task_manager.get_tasks_by_status(status)
        for task in tasks:
            task_id = task["id"]
            title = task["title"]
            priority = task["priority"]

            # Define priority color
            if priority == "Low":
                priority_color = "red"
            elif priority == "Medium":
                priority_color = "orange"
            elif priority == "High":
                priority_color = "green"

            task_row = tk.Frame(section_frame, pady=3)
            task_row.pack(fill=tk.X, padx=5, pady=2)

            # Create a canvas to draw a circle
            canvas = tk.Canvas(task_row, width=15, height=15)
            canvas.create_oval(5, 5, 15, 15, fill=priority_color, outline="")
            canvas.pack(side=tk.LEFT, padx=2)

            # Display the task title next to the priority circle
            label = tk.Label(task_row, text=f"{title}", anchor="w")
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)

            self.task_widgets[task_id] = {'frame': task_row, 'label': label, 'entry': None}

            # Move button
            move_btn = ttk.Menubutton(task_row, text="status")
            menu = tk.Menu(move_btn, tearoff=0)
            for target_status in ["todo", "doing", "done"]:
                if target_status != status:
                    menu.add_command(label=f"Move to {target_status.title()}",
                                     command=lambda tid=task_id, s=target_status: self.move_task(tid, s))
            move_btn["menu"] = menu
            move_btn.pack(side=tk.RIGHT, padx=2)

            # Delete button
            del_button = tk.Button(
                task_row,
                text="✖",
                width=2,
                font=ICON_FONT,
                command=lambda tid=task_id: self.delete_task(tid),
                fg="red",
            )
            del_button.pack(side=tk.RIGHT, padx=2)

            # Edit button
            edit_button = tk.Button(
                task_row,
                text="✎",
                width=2,
                font=ICON_FONT,
                command=lambda tid=task_id: self.edit_task(tid),
                fg="blue"
            )
            edit_button.pack(side=tk.RIGHT, padx=2)

    def add_task(self):
        title = self.task_entry.get().strip()
        priority = self.priority_combobox.get()  # Get selected priority
        if title:
            # Add the new task using TaskManager's add_task method
            task_data = {
                "title": title,
                "status": "todo",  # Default to 'todo'
                "priority": priority,  # Use selected priority
            }
            task = self.task_manager.add_task(task_data)
            if task:
                self.task_entry.delete(0, tk.END)  # Clear input field
                self.priority_combobox.set("Medium") # Reset to default priority after adding
                self.refresh_task_list()  # Refresh task list to show new task
        else:
            messagebox.showwarning(title="Input Error", message="Please enter a task title.")

    def delete_task(self, task_id):
        result = self.task_manager.remove_task(task_id)
        if result:
            self.refresh_task_list()  # Refresh the list to reflect the deletion
            messagebox.showinfo("Success", f"Your task has been deleted successfully!")

    def move_task(self, task_id, new_status):
        # Move task to a new status ('todo', 'doing', 'done')
        if new_status == "done":
            self.task_manager.complete_task(task_id)  # Mark task as completed
        else:
            self.task_manager.edit_task(task_id, 'status', new_status)  # Change task status
        self.refresh_task_list()

    def edit_task(self, task_id):
        widgets = self.task_widgets.get(task_id)
        if not widgets:
            return

        # If already editing, don't open another entry box
        if widgets.get('entry') is not None:
            return

        label = widgets.get('label')
        if label:
            label.destroy()
            self.task_widgets[task_id]['label'] = None

        task = self.task_manager.get_task(task_id)
        if not task:
            return

        task_row = widgets['frame']

        # Create Entry widget for task editing
        entry = tk.Entry(task_row)
        entry.insert(0, task["title"])  # Pre-fill with current task title
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.task_widgets[task_id]['entry'] = entry
        entry.focus_set()

        # Bind Enter key to save the task
        entry.bind("<Return>", lambda event: self.save_task(task_id))

    def save_task(self, task_id):
        widgets = self.task_widgets.get(task_id)
        if not widgets:
            return

        entry = widgets.get('entry')
        if not entry:
            return

        new_title = entry.get().strip()
        if not new_title:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")
            entry.focus_set()
            return

        # Save the task title to the TaskManager
        self.task_manager.edit_task(task_id, 'title', new_title)

        # Remove the entry widget and refresh the task list
        entry.destroy()
        self.refresh_task_list()

        messagebox.showinfo("Success", "Your task was updated successfully!")
