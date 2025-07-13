# ui_components.py

import tkinter as tk
from tkinter import ttk

def create_welcome_label(root):
    label = tk.Label(root, text="Welcome to Our To-Do List App", font=("Arial", 20))
    label.pack(pady=20)
    return label

def create_task_entry(root):
    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)
    return entry

def create_tasks_frame(root):
    frame = tk.Frame(root)
    frame.pack()
    return frame

def create_add_button(root, command):
    button = tk.Button(root, text="Add Task", command=command)
    button.pack(pady=10)
    return button
