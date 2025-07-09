import tkinter as tk

def click(val):
    entry.insert(tk.END, val)

def evaluate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 18))
entry.pack(fill="both", padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

for i, val in enumerate(buttons):
    cmd = evaluate if val == '=' else (clear if val == 'C' else lambda v=val: click(v))
    tk.Button(btn_frame, text=val, width=5, command=cmd).grid(row=i//4, column=i%4)

def key_input(event):
    if event.char in '0123456789+-*/':
        click(event.char)
    elif event.keysym == 'Return':
        evaluate()
    elif event.keysym == 'BackSpace':
        entry.delete(len(entry.get())-1, tk.END)

root.bind('<Key>', key_input)

root.mainloop()
