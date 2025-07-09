import tkinter as tk

def on_enter(e):
    e.widget.config(bg="lightblue")

def on_leave(e):
    e.widget.config(bg="SystemButtonFace")

root = tk.Tk()
root.title("Hover Effects")

label = tk.Label(root, text="Hover over me", width=20)
label.pack(pady=10)
label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)

button = tk.Button(root, text="Hover Button")
button.pack(pady=10)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()
