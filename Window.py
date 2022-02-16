import tkinter as tk


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Gest Money")
        self.geometry("679x406")
        # window.iconbitmap("")
        self.config(bg='#A27147')

    def update(self):
        self.mainloop()