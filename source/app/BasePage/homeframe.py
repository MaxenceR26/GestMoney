import tkinter as tk

from source.app.Sys import set_color


class HomeFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=853, height=584)
        self.window = window

        self.history_canvas = tk.Canvas(self, height=853, width=853, background=set_color('lightgreen'),
                                        highlightthickness=0)

        self.history_canvas.create_text(426.5, 50, text="Historique des transactions", font=('Roboto', 20, 'bold'),
                                        fill=set_color("darkgreen"))

        self.history_canvas.pack()