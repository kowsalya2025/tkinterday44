import tkinter as tk

class Notification(tk.Frame):
    def __init__(self, parent, message):
        super().__init__(parent, bg='lightyellow', pady=5)
        tk.Label(self, text="🔔", bg='lightyellow').pack(side="left", padx=5)
        tk.Label(self, text=message, bg='lightyellow').pack(side="left")
        tk.Button(self, text="X", command=self.destroy).pack(side="right", padx=5)
        self.pack(fill="x")
        self.after(5000, self.destroy)

root = tk.Tk()
root.title("Notification Demo")

def show_notification():
    Notification(root, "This is a test notification!")

tk.Button(root, text="Show Notification", command=show_notification).pack(pady=20)

root.mainloop()
