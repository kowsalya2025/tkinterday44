import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widget States Tasks")
root.geometry("700x800")

# Task 1: Button that disables itself
def disable_self(btn):
    btn.config(state="disabled")

btn1 = tk.Button(root, text="Click to Disable Me", command=lambda: disable_self(btn1))
btn1.pack(pady=5)

# Task 2: Checkbutton disables a text input
def toggle_entry():
    state = "disabled" if chk_var.get() else "normal"
    entry2.config(state=state)

chk_var = tk.BooleanVar()
chk = tk.Checkbutton(root, text="Disable Entry", variable=chk_var, command=toggle_entry)
chk.pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Task 3: One button disables the other
def disable_btn():
    btn_b.config(state="disabled")

btn_a = tk.Button(root, text="Disable B", command=disable_btn)
btn_a.pack()
btn_b = tk.Button(root, text="Button B")
btn_b.pack(pady=5)

# Task 4: Form with initially disabled Submit button
def enable_submit():
    submit_btn.config(state="normal" if chk_submit.get() else "disabled")

chk_submit = tk.BooleanVar()
tk.Checkbutton(root, text="I agree", variable=chk_submit, command=enable_submit).pack()
submit_btn = tk.Button(root, text="Submit", state="disabled")
submit_btn.pack(pady=5)

# Task 5: Disable entry on button click
def lock_entry():
    entry5.config(state="disabled")

entry5 = tk.Entry(root)
entry5.pack()
tk.Button(root, text="Lock Entry", command=lock_entry).pack(pady=5)

# Task 6: Enable button after 5 seconds
def enable_btn6():
    btn6.config(state="normal")

btn6 = tk.Button(root, text="Wait 5 sec", state="disabled")
btn6.pack(pady=5)
root.after(5000, enable_btn6)

# Task 7: Label changes color on hover
def on_enter(e):
    label7.config(fg="red")

def on_leave(e):
    label7.config(fg="black")

label7 = tk.Label(root, text="Hover Over Me", fg="black")
label7.pack(pady=5)
label7.bind("<Enter>", on_enter)
label7.bind("<Leave>", on_leave)

# Task 8: Button using state="active"
btn8 = tk.Button(root, text="Hover Me (Active)", state="normal", activebackground="yellow")
btn8.pack(pady=5)

# Task 9: Toggle widgets using Combobox
def toggle_widgets(event):
    state = combo.get()
    entry9.config(state=state)
    btn9.config(state=state)

tk.Label(root, text="Choose State:").pack()
combo = ttk.Combobox(root, values=["normal", "disabled"])
combo.current(0)
combo.bind("<<ComboboxSelected>>", toggle_widgets)
combo.pack()
entry9 = tk.Entry(root)
entry9.pack()
btn9 = tk.Button(root, text="Toggle Me")
btn9.pack(pady=5)

# Task 10: Disable group of buttons using loop
btn_group = []
def disable_all_buttons():
    for b in btn_group:
        b.config(state="disabled")

for i in range(3):
    b = tk.Button(root, text=f"Group Button {i+1}")
    b.pack()
    btn_group.append(b)
tk.Button(root, text="Disable Group", command=disable_all_buttons).pack(pady=5)

# Task 11: Reset all widgets to normal state
def reset_all():
    for widget in [btn1, entry2, btn_b, submit_btn, entry5, btn6, entry9, btn9] + btn_group:
        try:
            widget.config(state="normal")
        except:
            pass

tk.Button(root, text="Reset All Widgets", command=reset_all, bg="lightblue").pack(pady=5)

# Task 12: Visual change on state
def toggle_state_12():
    if btn12.cget("state") == "normal":
        btn12.config(state="disabled", bg="gray", fg="white")
    else:
        btn12.config(state="normal", bg="lightgreen", fg="black")

btn12 = tk.Button(root, text="Toggle My State Visually", bg="lightgreen", command=toggle_state_12)
btn12.pack(pady=5)

# Task 13: Disable Spinbox via Checkbutton
def toggle_spin():
    spin.config(state="disabled" if chk_spin.get() else "normal")

chk_spin = tk.BooleanVar()
tk.Checkbutton(root, text="Disable Spinbox", variable=chk_spin, command=toggle_spin).pack()
spin = tk.Spinbox(root, from_=0, to=10)
spin.pack(pady=5)

# Task 14: Radio button selection disables/unlocks widgets
def radio_action():
    val = radio_var.get()
    if val == "A":
        entry14a.config(state="disabled")
        entry14b.config(state="normal")
    else:
        entry14b.config(state="disabled")
        entry14a.config(state="normal")

radio_var = tk.StringVar(value="A")
tk.Radiobutton(root, text="Option A", variable=radio_var, value="A", command=radio_action).pack()
tk.Radiobutton(root, text="Option B", variable=radio_var, value="B", command=radio_action).pack()
entry14a = tk.Entry(root)
entry14a.pack()
entry14b = tk.Entry(root, state="disabled")
entry14b.pack(pady=5)

# Task 15: Combine Entry + Button + Label and toggle states
def toggle_combo():
    state = "disabled" if combo_var.get() else "normal"
    entry15.config(state=state)
    btn15.config(state=state)
    label15.config(text="Disabled" if state == "disabled" else "Enabled")

combo_var = tk.BooleanVar()
tk.Checkbutton(root, text="Disable All (Entry+Btn+Label)", variable=combo_var, command=toggle_combo).pack()
entry15 = tk.Entry(root)
entry15.pack()
btn15 = tk.Button(root, text="Combo Button")
btn15.pack()
label15 = tk.Label(root, text="Enabled")
label15.pack(pady=10)

root.mainloop()

