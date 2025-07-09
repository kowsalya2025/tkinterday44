import tkinter as tk

def key_pressed(event):
    key_label.config(text=f"Key Pressed: {event.keysym}")
    log.insert(tk.END, f"{event.keysym}\n")

root = tk.Tk()
root.title("Key Press Tracker")
root.geometry("300x250")

key_label = tk.Label(root, text="Press a key", font=("Arial", 14))
key_label.pack()

log = tk.Text(root, height=10)
log.pack()

root.bind("<KeyPress>", key_pressed)
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
