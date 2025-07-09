import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.title("Widget Functionality & Dynamic Behavior")
root.geometry("600x600")

# Task 46: Label changes color when clicked
def change_color(event):
    lbl46.config(bg="orange")

lbl46 = tk.Label(root, text="Click Me to Change Color", bg="lightblue", width=30)
lbl46.bind("<Button-1>", change_color)
lbl46.pack(pady=15)

# Task 47: Resize font on mouse hover
def enlarge_font(e):
    lbl47.config(font=("Arial", 18, "bold"))

def reset_font(e):
    lbl47.config(font=("Arial", 12))

lbl47 = tk.Label(root, text="Hover to Enlarge Font", font=("Arial", 12), bg="white")
lbl47.pack(pady=15)
lbl47.bind("<Enter>", enlarge_font)
lbl47.bind("<Leave>", reset_font)

# Task 48: Password Entry with visibility toggle
class PasswordEntry(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var, show="*")
        self.entry.pack(side="left", padx=5)
        self.btn = tk.Button(self, text="Show", command=self.toggle)
        self.btn.pack(side="left")
        self.visible = False

    def toggle(self):
        if self.visible:
            self.entry.config(show="*")
            self.btn.config(text="Show")
        else:
            self.entry.config(show="")
            self.btn.config(text="Hide")
        self.visible = not self.visible

tk.Label(root, text="Password:").pack()
PasswordEntry(root).pack(pady=15)

# Task 49: Progress tracker with button clicks
class ProgressTracker(tk.Frame):
    def __init__(self, master, length=10, **kwargs):
        super().__init__(master, **kwargs)
        self.length = length
        self.progress = 0
        self.label = tk.Label(self, text="_ " * length, font=("Courier", 14))
        self.label.pack()
        self.button = tk.Button(self, text="Advance Progress", command=self.advance)
        self.button.pack(pady=5)

    def advance(self):
        if self.progress < self.length:
            display = ("# " * (self.progress + 1)) + ("_ " * (self.length - self.progress - 1))
            self.label.config(text=display)
            self.progress += 1
        else:
            self.button.config(state="disabled")

ProgressTracker(root).pack(pady=15)

# Task 50: Real-time character counter for text input
class CharCounter(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.var = StringVar()
        self.entry = tk.Entry(self, textvariable=self.var, width=40)
        self.entry.pack()
        self.label = tk.Label(self, text="Characters: 0")
        self.label.pack()
        self.var.trace("w", self.update_count)

    def update_count(self, *args):
        count = len(self.var.get())
        self.label.config(text=f"Characters: {count}")

CharCounter(root).pack(pady=15)

root.mainloop()
