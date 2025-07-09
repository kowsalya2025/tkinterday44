import tkinter as tk

def draw_circle(event):
    r = 20
    canvas.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill='blue')
    coords.config(text=f"Circle at ({event.x}, {event.y})")

def draw_rect(event):
    w, h = 40, 30
    canvas.create_rectangle(event.x, event.y, event.x + w, event.y + h, fill='green')
    coords.config(text=f"Rectangle at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Shape Drawer")

canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()
coords = tk.Label(root, text="Click to draw", font=("Arial", 12))
coords.pack()

canvas.bind("<Button-1>", draw_circle)
canvas.bind("<Button-3>", draw_rect)

root.mainloop()
