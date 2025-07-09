import tkinter as tk

def submit():
    dialog = tk.Toplevel(root)
    dialog.title("Form Submitted")
    tk.Label(dialog, text=f"Name: {name.get()}").pack()
    tk.Label(dialog, text=f"Email: {email.get()}").pack()
    tk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=5)

root = tk.Tk()
root.title("Form with Dialog")

tk.Label(root, text="Name").pack()
name = tk.StringVar()
tk.Entry(root, textvariable=name).pack()

tk.Label(root, text="Email").pack()
email = tk.StringVar()
tk.Entry(root, textvariable=email).pack()

tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()
