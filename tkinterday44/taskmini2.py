import tkinter as tk

def check_selection():
    if q1.get() and q2.get():
        next_btn.config(state='normal')
    else:
        next_btn.config(state='disabled')

root = tk.Tk()
root.title("Survey Form")

q1 = tk.IntVar()
q2 = tk.IntVar()

tk.Label(root, text="1. Do you like Python?").pack()
for i, txt in enumerate(["Yes", "No"], 1):
    tk.Radiobutton(root, text=txt, variable=q1, value=i, command=check_selection).pack()

tk.Label(root, text="2. Do you use Tkinter?").pack()
for i, txt in enumerate(["Yes", "No"], 1):
    tk.Radiobutton(root, text=txt, variable=q2, value=i, command=check_selection).pack()

next_btn = tk.Button(root, text="Next", state='disabled')
next_btn.pack(pady=10)

root.mainloop()
