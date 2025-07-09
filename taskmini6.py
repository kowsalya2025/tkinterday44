import tkinter as tk

class ToggleSwitch(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.state = False
        self.label = tk.Label(self, text="OFF", width=8)
        self.label.pack(side="left")
        self.button = tk.Button(self, text="Toggle", command=self.toggle)
        self.button.pack(side="right")

    def toggle(self):
        self.state = not self.state
        self.label.config(text="ON" if self.state else "OFF")

root = tk.Tk()
root.title("Toggle Switch Widget")

ToggleSwitch(root).pack(pady=10)
ToggleSwitch(root).pack(pady=10)

root.mainloop()
