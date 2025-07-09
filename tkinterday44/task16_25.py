import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Mouse Events Tasks")
root.geometry("700x800")

# Task 16: Print mouse coordinates on button click
def show_coords(event):
    print(f"Mouse clicked at: ({event.x}, {event.y})")

btn16 = tk.Button(root, text="Click Me for Coords")
btn16.bind("<Button-1>", show_coords)
btn16.pack(pady=10)

# Task 17: Label changes color on hover
def enter_label(e):
    lbl17.config(bg="yellow")

def leave_label(e):
    lbl17.config(bg="lightgray")

lbl17 = tk.Label(root, text="Hover Over Me", bg="lightgray", width=30)
lbl17.bind("<Enter>", enter_label)
lbl17.bind("<Leave>", leave_label)
lbl17.pack(pady=10)

# Task 18: Button moves to random position on click
def move_button(event):
    x = random.randint(0, root.winfo_width() - 100)
    y = random.randint(0, root.winfo_height() - 100)
    btn18.place(x=x, y=y)

btn18 = tk.Button(root, text="Catch Me!")
btn18.place(x=100, y=300)
btn18.bind("<Button-1>", move_button)

# Task 19: Right-click popup
def show_popup(event):
    messagebox.showinfo("Right Click", "You right-clicked me!")

btn19 = tk.Button(root, text="Right Click Me")
btn19.bind("<Button-3>", show_popup)
btn19.pack(pady=10)

# Task 20: Tooltip on hover
def show_tooltip(e):
    tooltip.place(x=e.x_root - root.winfo_rootx(), y=e.y_root - root.winfo_rooty() + 20)

def hide_tooltip(e):
    tooltip.place_forget()

btn20 = tk.Button(root, text="Hover Me for Tooltip")
btn20.pack()
tooltip = tk.Label(root, text="I am a Tooltip!", bg="black", fg="white", padx=5, pady=2)
btn20.bind("<Enter>", show_tooltip)
btn20.bind("<Leave>", hide_tooltip)

# Task 21: Double-click changes label text
def change_text(event):
    lbl21.config(text="You double-clicked me!")

lbl21 = tk.Label(root, text="Double Click Me", fg="blue")
lbl21.pack(pady=10)
lbl21.bind("<Double-Button-1>", change_text)

# Task 22: Draw small circle on canvas where clicked
canvas22 = tk.Canvas(root, bg="white", width=300, height=200)
canvas22.pack(pady=10)

def draw_circle(event):
    r = 5
    x, y = event.x, event.y
    canvas22.create_oval(x - r, y - r, x + r, y + r, fill="blue")

canvas22.bind("<Button-1>", draw_circle)

# Task 23: Draw rectangle by clicking two points
canvas23 = tk.Canvas(root, bg="lightyellow", width=300, height=200)
canvas23.pack(pady=10)
click_coords = []

def draw_rectangle(event):
    click_coords.append((event.x, event.y))
    if len(click_coords) == 2:
        x1, y1 = click_coords[0]
        x2, y2 = click_coords[1]
        canvas23.create_rectangle(x1, y1, x2, y2, outline="red", width=2)
        click_coords.clear()

canvas23.bind("<Button-1>", draw_rectangle)

# Task 24: Log all mouse events in Text widget
def log_event(event):
    log.insert(tk.END, f"{event.type} at ({event.x},{event.y})\n")
    log.see(tk.END)

log = tk.Text(root, height=6, width=50)
log.pack(pady=10)

for ev in ["<Enter>", "<Leave>", "<Button-1>", "<Button-3>"]:
    root.bind(ev, log_event)

# Task 25: Entry border color changes on hover
def hover_entry(e):
    entry25.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)

def leave_entry(e):
    entry25.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=1)

entry25 = tk.Entry(root)
entry25.pack(pady=10)
entry25.bind("<Enter>", hover_entry)
entry25.bind("<Leave>", leave_entry)

root.mainloop()
