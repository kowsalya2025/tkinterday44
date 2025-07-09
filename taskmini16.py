import tkinter as tk

def toggle_state():
    global enabled
    enabled = not enabled
    state = "normal" if enabled else "disabled"
    for child in frame.winfo_children():
        child.config(state=state)

root = tk.Tk()
root.title("Enable/Disable Panel")

frame = tk.LabelFrame(root, text="Panel")
frame.pack(pady=10)

tk.Entry(frame).pack(padx=10, pady=5)
tk.Button(frame, text="Submit").pack(pady=5)

enabled = True
tk.Button(root, text="Toggle Panel", command=toggle_state).pack()

root.mainloop()
