import tkinter as tk


class MainWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root, width=900, height=1000)
        self.root = root
        self._frame = None

        # Design de la page de base quand on lance l'application

