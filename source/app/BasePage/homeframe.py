import tkinter as tk

from source.app.Sys import set_color


class HomeFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=853, height=584)
        self.window = window

        self.history_canvas = tk.Canvas(self, height=853, width=853, background=set_color('lightgreen'),
                                        highlightthickness=0)

        self.history_canvas.create_text(555, 50, text="Historique des transactions", font=('Roboto', 20, 'bold'),
                                        fill=set_color("darkgreen"))

        self.left_widgets()
        self.history_canvas.pack()

    def left_widgets(self):
        canvas = tk.Canvas(self, width=257, height=585, bg=set_color("entrycolor"), highlightthickness=0)
        canvas.create_line(1000, 0, -10, 0, fill=set_color("lightgreen"))
        canvas.create_line(1000, 520, -10, 520, fill=set_color("lightgreen"))
        canvas.place(x=0,y=0)