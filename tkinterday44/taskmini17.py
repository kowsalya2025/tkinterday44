import tkinter as tk

def move_obj(event):
    dx, dy = 0, 0
    if event.keysym == "Left": dx = -10
    if event.keysym == "Right": dx = 10
    if event.keysym == "Up": dy = -10
    if event.keysym == "Down": dy = 10
    x1, y1, x2, y2 = canvas.coords(obj)
    if 0 < x1+dx < 290 and 0 < y1+dy < 190:
        canvas.move(obj, dx, dy)

root = tk.Tk()
root.title("Canvas Mover")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

obj = canvas.create_oval(50, 50, 80, 80, fill="blue")

root.bind("<Key>", move_obj)

root.mainloop()
