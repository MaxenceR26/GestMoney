import tkinter as tk

from source.app.Sys import set_color


class CreditFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=853, height=584)
        self.window = window

        self.canvas = tk.Canvas(self, height=853, width=853, background=set_color('lightgreen'),
                                highlightthickness=0)

        self.canvas.create_text(426.5, 30, text="Créditer de l'argent", font=('Roboto', 30, 'bold'),
                                fill=set_color("darkgreen"))
        self.canvas.pack()