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

        canvas.create_text(128.5, 30, text='Rechercher', font=('Roboto', 17), fill="white")
        canvas.create_text(30, 100, text='Date', font=('Roboto', 17), fill="white", anchor='w')
        canvas.create_text(30, 175, text='Magasin', font=('Roboto', 17), fill="white", anchor='w')

        self.date_entry = tk.Entry(self, background=set_color("darkgreen"), bd=0,
                                   font=('Roboto', 15, 'bold'), fg='#FFFFFF')
        self.date_entry.place(x=20, y=120, width=200, height=32)

        self.magasin_entry = tk.Entry(self, background=set_color("darkgreen"), bd=0,
                                      font=('Roboto', 15, 'bold'), fg='#FFFFFF')
        self.magasin_entry.place(x=20, y=195, width=200, height=32)

        # E-mail utilisateur actuel
        canvas.create_text(128.5, 555, text=self.window.user_connected, font=('Roboto', 13),
                           fill="white")

        canvas.place(x=0, y=0)
