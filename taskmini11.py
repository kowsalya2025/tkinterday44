import tkinter as tk

def update_timer():
    global running, seconds
    if running:
        seconds += 1
        timer_label.config(text=f"{seconds} s")
        root.after(1000, update_timer)

def start():
    global running
    running = True
    start_btn.config(state='disabled')
    stop_btn.config(state='normal')
    update_timer()

def stop():
    global running
    running = False
    start_btn.config(state='normal')
    stop_btn.config(state='disabled')

def reset():
    global seconds
    seconds = 0
    timer_label.config(text="0 s")

root = tk.Tk()
root.title("Timer")

seconds = 0
running = False

timer_label = tk.Label(root, text="0 s", font=("Arial", 20))
timer_label.pack()

start_btn = tk.Button(root, text="Start", command=start)
start_btn.pack(side="left", padx=5)
stop_btn = tk.Button(root, text="Stop", command=stop, state='disabled')
stop_btn.pack(side="left", padx=5)
reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.pack(side="left", padx=5)

root.mainloop()

