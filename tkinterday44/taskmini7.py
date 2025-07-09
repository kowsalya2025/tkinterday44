import tkinter as tk
import re

def validate_email(*args):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email.get()):
        submit_btn.config(state='normal')
    else:
        submit_btn.config(state='disabled')

root = tk.Tk()
root.title("Email Validator")

tk.Label(root, text="Enter Email:").pack()
email = tk.StringVar()
tk.Entry(root, textvariable=email).pack()
email.trace_add("write", validate_email)

submit_btn = tk.Button(root, text="Submit", state='disabled')
submit_btn.pack(pady=10)

root.mainloop()
