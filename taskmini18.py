import tkinter as tk

def add_tooltip(widget, text):
    tooltip = tk.Label(root, text=text, bg="lightyellow", relief="solid", bd=1)

    def show(event):
        tooltip.place(x=event.x_root - root.winfo_rootx() + 20,
                      y=event.y_root - root.winfo_rooty() + 10)

    def hide(event):
        tooltip.place_forget()

    widget.bind("<Enter>", show)
    widget.bind("<Leave>", hide)

root = tk.Tk()
root.title("Tooltip Demo")

btn = tk.Button(root, text="Hover me")
btn.pack(pady=20)
add_tooltip(btn, "Click to perform an action")

root.mainloop()
