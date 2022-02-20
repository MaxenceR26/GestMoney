import tkinter as tk

from source.app.Sys import set_color


class DebitFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=853, height=584)
        self.window = window