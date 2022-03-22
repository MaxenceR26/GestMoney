import tkinter as tk
from tkinter import ttk
from datetime import datetime

from data.data import get_transactions
from source.app.BasePage.baseframe import create_copyright, create_buttons, show_error
from source.app.Sys import set_color


class ReguFrame(tk.Frame):
    def __init__(self, window):
        self.window = window
        self.frame_width = 1023

        super().__init__(window, width=self.frame_width, height=640, bg=self.set_color('fourthbg'))

        self.error_canvas = tk.Canvas()
        self.canvas = tk.Canvas(self, height=640, width=self.frame_width, background=self.set_color('fourthbg'),
                                highlightthickness=0)

        self.left_inputs()
        self.right_treeview()
        create_copyright(self, self.canvas)

        self.canvas.pack()

    def left_inputs(self):

        self.canvas.create_line(self.frame_width / 2, 30, self.frame_width / 2, 610, fill='white')

        self.canvas.create_text(self.frame_width / 4, 50, text="Créer une\ndépense régulière", font=('Roboto', 30),
                                fill=self.set_color('text2'), justify="center")

        entry_width = 330
        entry_height = 46

        x_pos = self.frame_width / 4 - entry_width / 2

        self.canvas.create_text(x_pos, 145, text='Montant', font=('Roboto', 18),
                                fill=self.set_color('text'), anchor='w')
        self.canvas.create_text(x_pos, 255, text='Objet', font=('Roboto', 18),
                                fill=self.set_color('text'), anchor='w')
        self.canvas.create_text(x_pos, 365, text='Jour du prélèvement', font=('Roboto', 18),
                                fill=self.set_color('text'), anchor='w')

        self.amount = tk.Entry(self.canvas, bg=self.set_color('bg'), font=('Roboto', 15), fg='white',
                               bd=0, insertbackground=self.set_color('entrytext'))
        self.amount.place(x=x_pos, y=165, width=entry_width, height=entry_height)

        self.origin = tk.Entry(self.canvas, bg=self.set_color('bg'), font=('Roboto', 15), fg='white',
                               bd=0, insertbackground=self.set_color('entrytext'))
        self.origin.place(x=x_pos, y=275, width=entry_width, height=entry_height)

        self.date = tk.Entry(self.canvas, bg=self.set_color('bg'), font=('Roboto', 15), fg='white',
                             bd=0, insertbackground=self.set_color('entrytext'))
        self.date.place(x=x_pos, y=275 + 110, width=entry_width, height=entry_height)

        create_buttons(self, self.valid_debit, 50, 301.5, 160)

    def right_treeview(self):

        def title_treeview():
            self.title_canvas = tk.Canvas(self, width=width, height=20, bg=self.set_color("bg"), highlightthickness=0,
                                          bd=0)
            self.title_canvas.create_text(width/6, 10, text="Montant",
                                          font=('Roboto', 13, 'bold'), fill=self.set_color('text2'))

            self.title_canvas.create_text(width/3, 8, text=" | ",
                                          font=('Roboto', 13), fill=self.set_color('text2'))

            self.title_canvas.create_text(width/2, 10, text="Objet",
                                          font=('Roboto', 13, 'bold'), fill=self.set_color('text2'))

            self.title_canvas.create_text(width/1.5, 8, text=" | ",
                                          font=('Roboto', 13), fill=self.set_color('text2'))

            self.title_canvas.create_text(width/6*5, 10, text="Date",
                                          font=('Roboto', 13, 'bold'), fill=self.set_color('text2'))

            self.title_canvas.place(x=x_pos, y=y_pos+1)

        x_pos = self.frame_width / 2 + 50
        y_pos = 74
        width = 411
        height = 500

        style = ttk.Style()
        style.theme_use('alt')
        style.configure('Treeview',
                        background=self.set_color('tertiarybg'),
                        foreground=self.set_color('text2'),
                        highlightthickness=0, bd=0,
                        font=('Roboto', 9, 'bold'),
                        rowheight=40)

        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.map('Treeview', background=[('selected', '#172F6E')],
                  foreground=[('selected', self.set_color('text'))])

        tableau = ttk.Treeview(self.canvas, columns=('amount', 'object', 'date'))

        tableau.column("#1", width=width//3, anchor=tk.CENTER, stretch=tk.NO)
        tableau.column("#2", width=width//3, anchor=tk.CENTER, stretch=tk.NO)
        tableau.column("#3", width=width//3, anchor=tk.CENTER, stretch=tk.NO)

        tableau.heading('amount', text='Montant')
        tableau.heading('object', text='Objet')
        tableau.heading('date', text='Date')
        tableau['show'] = 'headings'

        transacs = get_transactions(self.window.user_id)
        transacs = sorted(transacs, key=lambda x: datetime.strptime(x['date'], "%d/%m/%y").strftime("%y-%m-%d"))[::-1]

        for index in range(len(transacs)):

            transac = transacs[index]

            if transac['type'] == 'credit':
                tableau.insert(parent='', index='end', iid=index, text='Market',
                               values=(f"{transac['amount']}€", transac['origin'], transac['date']))

            else:
                tableau.insert(parent='', index='end', iid=index, text='Market',
                               values=(f"{transac['amount']}€", f"{transac['market']} / {transac['buy_type']}", transac['date']))

        tableau.place(x=x_pos, y=y_pos+1, width=width, height=height)

        title_treeview()

        # Création bande entre chaque ligne et sur les côtés

        for i in range(min(len(transacs), 12)):
            line = tk.Canvas(self, width=width, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
            line.place(x=x_pos, y=i * 40 + 94)

        top = tk.Canvas(self, width=width, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
        top.place(x=x_pos, y=y_pos)

        bottom = tk.Canvas(self, width=width, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
        bottom.place(x=x_pos, y=y_pos+height)

        left = tk.Canvas(self, width=2, height=height, bg=self.set_color('darkbg'), highlightthickness=0)
        left.place(x=x_pos, y=y_pos)

        right = tk.Canvas(self, width=2, height=height, bg=self.set_color('darkbg'), highlightthickness=0)
        right.place(x=x_pos+width, y=y_pos)

    def valid_debit(self):
        origin = self.origin.get()
        amount = self.amount.get()
        date = self.date.get()

        transaction = {
            'type': 'credit',
            'origin': origin,
            'amount': amount,
            'date': date
        }

        if '' in transaction.values():
            self.show_error('Veuillez remplir toutes les cases')

        elif not amount.isdigit():
            self.show_error('Veuillez entrer un montant valide')

        elif not date.isdigit() or int(date) > 31:
            self.show_error('Veuillez entrer un jour valide')

        else:
            transaction['amount'] = int(transaction['amount'])

            self.window.switch_frame('BasePage')

    def show_error(self, text):
        show_error(self, text, 215)

    def set_color(self, color):
        return set_color(self.window.color_theme, color)