import tkinter as tk
from tkinter import messagebox, PhotoImage

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_idx = selected_task[0]
        task_listbox.delete(task_idx)
        tasks.pop(task_idx)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_idx = selected_task[0]
        task_listbox.itemconfig(task_idx, {'bg': 'light green'})
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

root = tk.Tk()
root.title("To-Do List App")
root.geometry("350x350")

bg_image = PhotoImage(file=r'c:\Users\TechDotpk\Downloads\green.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

task_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
mark_done_button = tk.Button(root, text="Mark as Done", command=mark_done)
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)

task_entry.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
add_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
remove_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
mark_done_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
task_listbox.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

tasks = []

root.mainloop()
