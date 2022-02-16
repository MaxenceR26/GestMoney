import tkinter as tk


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__()

        width, height = 679, 406
        self.title("Gest Money")
        self.geometry(f"{width}x{height}")
        self.minsize(width, height)
        self.maxsize(width, height)
        # window.iconbitmap("")
        self.config(bg='#A27147')

    def run(self):
        self.mainloop()