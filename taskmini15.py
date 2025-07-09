import tkinter as tk

def update_count(event=None):
    length = len(entry.get())
    counter_label.config(text=f"Characters: {length}")

root = tk.Tk()
root.title("Character Counter")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_count)

counter_label = tk.Label(root, text="Characters: 0")
counter_label.pack()

root.mainloop()
