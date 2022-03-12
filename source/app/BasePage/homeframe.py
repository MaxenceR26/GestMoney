import tkinter as tk

from data.data import add_debit_trace, get_debit_trace, get_number_of_purchase
from source.app.Sys import set_color


class HomeFrame(tk.Frame):

    def __init__(self, window):
        self.window = window
        super().__init__(window, width=1023, height=720, bg=self.set_color('bg'))

        self.history_canvas = tk.Canvas(self, height=853, width=853, bg=self.set_color('bg'),
                                        highlightthickness=0)

        self.history_canvas.create_text(555, 40, text="Historique des transactions", font=('Roboto', 20, 'bold'),
                                        fill=self.set_color('text'))

        self.listbox = tk.Listbox(width=45, height=20, bd=0, bg="#77AB7D", highlightthickness=2,
                                  highlightcolor=self.set_color('text'), highlightbackground=self.set_color('text'))
        self.listbox.place(x=307, y=160)
        self.listbox.configure(justify="center", foreground="white", font=('Roboto', 14),
                               selectbackground=self.set_color('text'))

        data_debit = get_debit_trace(self.window.user_id)

        for i in range(len(data_debit)):
            self.listbox.insert(i, data_debit[i])

        self.left_widgets()
        self.history_canvas.pack()

    def left_widgets(self):
        canvas = tk.Canvas(self, width=257, height=645, bg=self.set_color("entrycolor"), highlightthickness=0)
        canvas.create_line(1000, 0, -10, 0, fill=self.set_color('bg'))
        canvas.create_line(1000, 520, -10, 520, fill=self.set_color('bg'))

        canvas.create_text(128.5, 30, text='Rechercher', font=('Roboto', 17), fill=self.set_color('text2'))
        canvas.create_text(30, 100, text='Date', font=('Roboto', 17), fill=self.set_color('text2'), anchor='w')
        canvas.create_text(30, 175, text='Magasin', font=('Roboto', 17), fill=self.set_color('text2'), anchor='w')

        self.date_entry = tk.Entry(self, background=self.set_color('text'), bd=0, font=('Roboto', 15, 'bold'),
                                   fg='#FFFFFF', insertbackground=self.set_color('entrytext'))
        self.date_entry.place(x=20, y=120, width=200, height=32)

        self.magasin_entry = tk.Entry(self, background=self.set_color('text'), bd=0, font=('Roboto', 15, 'bold'),
                                      fg='#FFFFFF', insertbackground=self.set_color('entrytext'))
        self.magasin_entry.place(x=20, y=195, width=200, height=32)

        canvas.place(x=0, y=0)

    def set_color(self, color):
        return set_color(self.window.color_theme, color)