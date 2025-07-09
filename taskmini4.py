import tkinter as tk

def change_color(event):
    colors = {
        "Left": "red",
        "Right": "green",
        "Up": "blue",
        "Down": "yellow"
    }
    color = colors.get(event.keysym, "white")
    frame.config(bg=color)
    color_label.config(text=f"Color: {color}", bg=color)

root = tk.Tk()
root.title("Arrow Key Color Picker")

frame = tk.Frame(root, width=300, height=200)
frame.pack_propagate(False)
frame.pack()

color_label = tk.Label(frame, text="Color: white", font=("Arial", 14))
color_label.pack()

for key in ["Left", "Right", "Up", "Down"]:
    root.bind(f"<{key}>", change_color)

root.mainloop()
