import tkinter as tk

def on_key(event):
    idx = listbox.curselection()
    if idx:
        index = idx[0]
        if event.keysym == "Down" and index < listbox.size() - 1:
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(index + 1)
        elif event.keysym == "Up" and index > 0:
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(index - 1)

def show_selected(event):
    idx = listbox.curselection()
    if idx:
        label.config(text=f"Selected: {listbox.get(idx)}")

root = tk.Tk()
root.title("Listbox Navigator")

items = ["Item A", "Item B", "Item C", "Item D"]
listbox = tk.Listbox(root)
for item in items:
    listbox.insert(tk.END, item)
listbox.pack()

label = tk.Label(root, text="Selected: None")
label.pack()

root.bind("<Up>", on_key)
root.bind("<Down>", on_key)
root.bind("<Return>", show_selected)

listbox.selection_set(0)

root.mainloop()
