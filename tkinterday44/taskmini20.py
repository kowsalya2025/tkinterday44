import tkinter as tk

class EmojiBar(tk.Frame):
    def __init__(self, parent, target_label):
        super().__init__(parent)
        self.label = target_label
        for emoji in ["😀", "😢", "😠", "😍"]:
            btn = tk.Button(self, text=emoji, command=lambda e=emoji: self.react(e))
            btn.pack(side="left", padx=2)

    def react(self, emoji):
        self.label.config(text=f"Reacted with: {emoji}")

root = tk.Tk()
root.title("Emoji Reactions")

msg1 = tk.Label(root, text="Post #1: Hello World")
msg1.pack()
EmojiBar(root, msg1).pack()

msg2 = tk.Label(root, text="Post #2: Good Night")
msg2.pack()
EmojiBar(root, msg2).pack()

root.mainloop()
