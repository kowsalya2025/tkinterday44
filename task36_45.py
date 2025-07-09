import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Custom Widget Creation")
root.geometry("800x1000")

# Task 36: Label + Button custom widget
class LabelButtonWidget(tk.Frame):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, **kwargs)
        self.label = tk.Label(self, text=text)
        self.label.pack(side="left", padx=5)
        self.button = tk.Button(self, text="Click", command=self.say_hello)
        self.button.pack(side="left")

    def say_hello(self):
        messagebox.showinfo("Hello", "You clicked the button!")

LabelButtonWidget(root, "Hello Widget:").pack(pady=10)

# Task 37: Label + Entry, updates label live
class LiveEntryLabel(tk.Frame):
    def __init__(self, master, label_text="Live: ", **kwargs):
        super().__init__(master, **kwargs)
        self.label = tk.Label(self, text=label_text)
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.entry.bind("<KeyRelease>", self.update_label)

    def update_label(self, event):
        self.label.config(text="Live: " + self.entry.get())

LiveEntryLabel(root).pack(pady=10)

# Task 38: OK/Cancel button group
class OkCancelButtons(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.ok = tk.Button(self, text="OK", command=lambda: messagebox.showinfo("OK", "OK Pressed"))
        self.ok.pack(side="left", padx=5)
        self.cancel = tk.Button(self, text="Cancel", command=lambda: messagebox.showwarning("Cancel", "Cancelled"))
        self.cancel.pack(side="left", padx=5)

OkCancelButtons(root).pack(pady=10)

# Task 39: SearchBox widget
class SearchBox(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.entry = tk.Entry(self)
        self.entry.pack(side="left", fill="x", expand=True)
        self.btn = tk.Button(self, text="Search", command=self.search)
        self.btn.pack(side="left")

    def search(self):
        query = self.entry.get()
        messagebox.showinfo("Search", f"Searching for: {query}")

SearchBox(root).pack(fill="x", padx=10, pady=10)

# Task 40: Calculator row widget
class CalculatorRow(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.num1 = tk.Entry(self, width=5)
        self.num1.pack(side="left")
        self.op = tk.Label(self, text="+")
        self.op.pack(side="left", padx=5)
        self.num2 = tk.Entry(self, width=5)
        self.num2.pack(side="left")
        self.equals = tk.Button(self, text="=", command=self.calculate)
        self.equals.pack(side="left", padx=5)
        self.result = tk.Label(self, text="Result")
        self.result.pack(side="left")

    def calculate(self):
        try:
            val = float(self.num1.get()) + float(self.num2.get())
            self.result.config(text=str(val))
        except:
            self.result.config(text="Error")

CalculatorRow(root).pack(pady=10)

# Task 41: Reusable login widget
class LoginWidget(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        tk.Label(self, text="Username:").pack()
        self.user = tk.Entry(self)
        self.user.pack()
        tk.Label(self, text="Password:").pack()
        self.pwd = tk.Entry(self, show="*")
        self.pwd.pack()
        tk.Button(self, text="Submit", command=self.submit).pack(pady=5)

    def submit(self):
        messagebox.showinfo("Login", f"Welcome, {self.user.get()}!")

LoginWidget(root).pack(pady=10)

# Task 42: Rating bar (5 stars)
class RatingBar(tk.Frame):
    def __init__(self, master, stars=5, **kwargs):
        super().__init__(master, **kwargs)
        self.rating = tk.IntVar(value=0)
        self.buttons = []
        for i in range(1, stars+1):
            btn = tk.Button(self, text="☆", font=("Arial", 20), command=lambda i=i: self.set_rating(i))
            btn.pack(side="left")
            self.buttons.append(btn)

    def set_rating(self, val):
        self.rating.set(val)
        for i, btn in enumerate(self.buttons):
            btn.config(text="★" if i < val else "☆")

RatingBar(root).pack(pady=10)

# Task 43: Color Picker
class ColorPicker(tk.Frame):
    def __init__(self, master, colors=None, **kwargs):
        super().__init__(master, **kwargs)
        if colors is None:
            colors = ["red", "green", "blue", "yellow", "purple"]
        for color in colors:
            tk.Button(self, bg=color, width=3, command=lambda c=color: self.pick_color(c)).pack(side="left", padx=2)
        self.label = tk.Label(self, text="No color selected")
        self.label.pack(pady=5)

    def pick_color(self, color):
        self.label.config(text=f"Selected: {color}", fg=color)

ColorPicker(root).pack(pady=10)

# Task 44: Toolbar widget
class Toolbar(tk.Frame):
    def __init__(self, master, buttons=("Open", "Save", "Exit"), **kwargs):
        super().__init__(master, **kwargs)
        for btn in buttons:
            tk.Button(self, text=btn, command=lambda b=btn: self.action(b)).pack(side="left", padx=3)

    def action(self, name):
        if name == "Exit":
            root.destroy()
        else:
            messagebox.showinfo(name, f"{name} clicked")

Toolbar(root).pack(fill="x", pady=10)

# Task 45: LabeledEntry using class inheritance
class LabeledEntry(tk.Frame):
    def __init__(self, master, label_text, entry_width=20, **kwargs):
        super().__init__(master, **kwargs)
        tk.Label(self, text=label_text, fg="darkblue", font=("Arial", 10, "bold")).pack(side="left", padx=5)
        self.entry = tk.Entry(self, width=entry_width, bg="lightyellow")
        self.entry.pack(side="left")

LabeledEntry(root, "Name:").pack(pady=10)
LabeledEntry(root, "Email:").pack(pady=10)

root.mainloop()
