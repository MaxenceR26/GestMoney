import tkinter as tk
import tkinter.ttk as ttk

from data.data import get_debit_trace
from source.app.Sys import set_color


class HomeFrame(tk.Frame):

    def __init__(self, window):
        self.window = window

        super().__init__(window, width=1023, height=640, bg=self.set_color('fourthbg'))

        self.history_canvas = tk.Canvas(self, height=640, width=853, bg=self.set_color('fourthbg'),
                                        highlightthickness=0)
        self.history_canvas.create_text(426.5, 40, text="Historique des transactions",
                                        font=('Roboto', 20, 'bold'), fill=self.set_color('text'))

        # Création du style
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('Treeview',
                        background=self.set_color('bg'),
                        foreground=self.set_color('text'),
                        fieldbackground=self.set_color('bg'),
                        highlightthickness = 0, bd = 0,
                        rowheight=50)

        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.map('Treeview', background=[('selected', self.set_color('darkbg'))], foreground=[('selected', self.set_color('text'))])

        tableau = ttk.Treeview(self.history_canvas, columns=('amount', 'market', 'date'))

        tableau.heading('amount', text='Montant')
        tableau.heading('market', text='Magasin')
        tableau.heading('date', text='Date')
        tableau['show'] = 'headings'

        data_debit = get_debit_trace(self.window.user_id)
        tableau.tag_configure('oddrow', background=self.set_color("tertiarybg"))
        tableau.tag_configure('evenrow', background=self.set_color("bg"))

        self.count = 0

        for i in range(len(data_debit)):
            data = data_debit[i]
            if self.count %2 == 0:
                tableau.insert(parent='', index='end', iid=i, text='Market', values=(data['amount'], data['market'], data['date']), tags=('oddrow'))
            else:
                tableau.insert(parent='', index='end', iid=i, text='Market',
                               values=(data['amount'], data['market'], data['date']), tags=('evenrow'))
            self.count += 1

        tableau.place(x=35, y=100, width=690, height=500)

        self.left_widgets()
        self.history_canvas.place(x=257, y=0)

    def left_widgets(self):
        canvas = tk.Canvas(self, width=257, height=645, bg=self.set_color("darkbg"), highlightthickness=0)
        canvas.create_line(1000, 0, -10, 0, fill="black")
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