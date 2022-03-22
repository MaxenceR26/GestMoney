import tkinter as tk

from ccc import Maieen


class Main(tk.Tk):
    def __init__(self):
        super(Main, self).__init__()

        button = tk.Button(self, text="dddddddddddd", command= lambda: [self.destroy(), Maieen()])
        button.pack()

        self.mainloop()

Main()