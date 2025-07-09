import tkinter as tk

class Counter(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.count = 0
        self.label = tk.Label(self, text="0", font=("Arial", 16))
        self.label.pack()

        tk.Button(self, text="+", command=self.increment).pack(side="left")
        tk.Button(self, text="-", command=self.decrement).pack(side="left")
        tk.Button(self, text="Reset", command=self.reset).pack(side="left")

    def update_label(self):
        self.label.config(text=str(self.count))

    def increment(self):
        self.count += 1
        self.update_label()

    def decrement(self):
        self.count -= 1
        self.update_label()

    def reset(self):
        self.count = 0
        self.update_label()

root = tk.Tk()
root.title("Counter Widget")

Counter(root).pack(pady=10)

root.mainloop()
