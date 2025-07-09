import tkinter as tk

def check_fields(*args):
    if username.get() and password.get():
        login_btn.config(state='normal')
    else:
        login_btn.config(state='disabled')

root = tk.Tk()
root.title("Login Form")

tk.Label(root, text="Username").pack()
username = tk.StringVar()
tk.Entry(root, textvariable=username).pack()
username.trace_add('write', check_fields)

tk.Label(root, text="Password").pack()
password = tk.StringVar()
tk.Entry(root, textvariable=password, show='*').pack()
password.trace_add('write', check_fields)

login_btn = tk.Button(root, text="Login", state='disabled')
login_btn.pack(pady=10)

root.mainloop()
