import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Keyboard Events Tasks")
root.geometry("700x700")

# Task 26: Bind <KeyPress> to log pressed key
def log_key(event):
    text26.insert(tk.END, f"Key pressed: {event.char} ({event.keysym})\n")
    text26.see(tk.END)

text26 = tk.Text(root, height=5, width=50)
text26.pack(pady=10)
root.bind("<KeyPress>", log_key)

# Task 27: Show key name in a Label
def show_keysym(event):
    label27.config(text=f"Pressed Key: {event.keysym}")

label27 = tk.Label(root, text="Press any key...", font=("Arial", 12), fg="blue")
label27.pack(pady=10)
root.bind("<KeyPress>", show_keysym)

# Task 28: Login form with <Return> to submit
def login_submit(event=None):
    user = entry_user.get()
    pwd = entry_pwd.get()
    messagebox.showinfo("Login Attempt", f"Username: {user}\nPassword: {pwd}")

tk.Label(root, text="Username:").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password:").pack()
entry_pwd = tk.Entry(root, show="*")
entry_pwd.pack()

entry_pwd.bind("<Return>", login_submit)
tk.Button(root, text="Login", command=login_submit).pack(pady=10)

# Task 29: Arrow keys to move shape on canvas
canvas29 = tk.Canvas(root, width=300, height=200, bg="lightgray")
canvas29.pack(pady=10)
oval = canvas29.create_oval(130, 80, 170, 120, fill="green")

def move_shape(event):
    if event.keysym == "Left":
        canvas29.move(oval, -10, 0)
    elif event.keysym == "Right":
        canvas29.move(oval, 10, 0)
    elif event.keysym == "Up":
        canvas29.move(oval, 0, -10)
    elif event.keysym == "Down":
        canvas29.move(oval, 0, 10)

root.bind("<Left>", move_shape)
root.bind("<Right>", move_shape)
root.bind("<Up>", move_shape)
root.bind("<Down>", move_shape)

# Task 30: B/W toggles background color
def toggle_bg(event):
    if event.char.lower() == 'b':
        root.config(bg="black")
    elif event.char.lower() == 'w':
        root.config(bg="white")

root.bind("<KeyPress>", toggle_bg)

# Task 31: <KeyRelease> for Shift key
def shift_released(event):
    if event.keysym == "Shift_L" or event.keysym == "Shift_R":
        messagebox.showinfo("Key Released", "Shift key released!")

root.bind("<KeyRelease>", shift_released)

# Task 32: Pressing Esc closes app
root.bind("<Escape>", lambda e: root.destroy())

# Task 33: Ctrl+S to simulate Save
def simulate_save(event):
    messagebox.showinfo("Save", "Data Saved (Ctrl+S)")

root.bind("<Control-s>", simulate_save)

# Task 34: F1 opens Help
def show_help(event):
    messagebox.showinfo("Help", "This is a sample help dialog.\nPress F1 to access help.")

root.bind("<F1>", show_help)

# Task 35: Entry field that capitalizes input
def capitalize_input(event):
    entry35.delete(0, tk.END)
    entry35.insert(0, event.widget.get().upper())

tk.Label(root, text="Type here (auto-capitalized):").pack()
entry35 = tk.Entry(root)
entry35.pack(pady=10)
entry35.bind("<KeyRelease>", capitalize_input)

root.mainloop()
