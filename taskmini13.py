import tkinter as tk

def toggle_task(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        task = listbox.get(index)
        if task.startswith("✔ "):
            task = task[2:]
        else:
            task = "✔ " + task
        listbox.delete(index)
        listbox.insert(index, task)

root = tk.Tk()
root.title("Task Manager")

tasks = ["Buy groceries", "Finish project", "Call mom"]
listbox = tk.Listbox(root, width=30)
for task in tasks:
    listbox.insert(tk.END, task)
listbox.pack()

listbox.bind("<Double-Button-1>", toggle_task)

root.mainloop()
