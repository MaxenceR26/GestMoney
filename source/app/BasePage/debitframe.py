import tkinter as tk

from source.app.Sys import set_color
from source.app.BasePage.baseframe import create_buttons, date_valid
from data.data import add_transaction


class DebitFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=853, height=584)
        self.window = window

        self.canvas = tk.Canvas(self, height=853, width=853, background=set_color('lightgreen'), highlightthickness=0)

        self.canvas.create_text(426.5, 50, text="Débiter le compte", font=('Roboto', 30, 'bold'),
                                fill=set_color("darkgreen"))

        self.error_canvas = tk.Canvas(self, height=5040, width=self.window.winfo_width(),
                                      background=set_color("lightgreen"), highlightthickness=0)

        self.create_inputs()
        self.canvas.pack()

    def create_inputs(self):
        self.canvas.create_text(50, 150, text='Magasin', font=('Roboto', 18), fill=set_color('darkgreen'), anchor='w')
        self.canvas.create_text(50, 270, text='Achat', font=('Roboto', 18),
                                fill=set_color('darkgreen'), anchor='w')
        self.canvas.create_text(470, 150, text='Montant', font=('Roboto', 18), fill=set_color('darkgreen'), anchor='w')
        self.canvas.create_text(470, 270, text='Date', font=('Roboto', 18), fill=set_color('darkgreen'), anchor='w')
        self.canvas.create_text(50, 375, text='Moyen de paiement', font=('Roboto', 18),
                                fill=set_color('darkgreen'), anchor='w')

        self.market = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.market.place(x=50, y=170, width=330, height=46)

        self.buy_type = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.buy_type.place(x=50, y=290, width=330, height=46)

        self.amount = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.amount.place(x=470, y=170, width=330, height=46)

        self.date = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.date.place(x=470, y=290, width=330, height=46)

        self.cheque_var = tk.IntVar()
        self.cb_var = tk.IntVar()
        self.especes_var = tk.IntVar()
        self.check_vars = [self.cb_var, self.especes_var, self.cheque_var]

        cb_checkbutton = tk.Checkbutton(self, text='CB', background=set_color("lightgreen"), variable=self.cb_var,
                                        foreground=set_color("darkgreen"), font=('Roboto', 16, 'bold'),
                                        highlightthickness=0, bd=0, activebackground=set_color("lightgreen"),
                                        activeforeground=set_color("darkgreen"), command=lambda: self.uncheck_buttons(0))
        cb_checkbutton.place(x=310, y=360)

        espece_checkbutton = tk.Checkbutton(self, text='Espèce', background=set_color("lightgreen"), bd=0,
                                            foreground=set_color("darkgreen"), font=('Roboto', 16, 'bold'),
                                            activebackground=set_color("lightgreen"), highlightthickness=0,
                                            activeforeground=set_color("darkgreen"), variable=self.especes_var,
                                            command=lambda: self.uncheck_buttons(1))
        espece_checkbutton.place(x=392, y=360)

        cheque_checkbutton = tk.Checkbutton(self, text='Chèque', background=set_color("lightgreen"), bd=0,
                                            foreground=set_color("darkgreen"), font=('Roboto', 16, 'bold'),
                                            activebackground=set_color("lightgreen"), highlightthickness=0,
                                            activeforeground=set_color("darkgreen"), variable=self.cheque_var,
                                            command=lambda: self.uncheck_buttons(2))
        cheque_checkbutton.place(x=515, y=360)

        self.check_buttons = [cb_checkbutton, espece_checkbutton, cheque_checkbutton]

        create_buttons(self, self.valid_debit)

    def valid_debit(self):
        market = self.market.get()
        buy_type = self.buy_type.get()
        amount = self.amount.get()
        date = self.date.get()

        transaction = {
            'market': market,
            'buy_type': buy_type,
            'amount': amount,
            'date': date
        }

        if '' in transaction.values():
            self.show_error('Veuillez remplir toutes les cases')

        elif not amount.isdigit():
            self.show_error('Veuillez entrer un montant valide')

        elif not date_valid(date):
            self.show_error('Veuillez entrer une date au format dd/mm/yy')

        elif 1 not in [var.get() for var in self.check_vars]:
            self.show_error('Veuillez cocher une case')

        else:
            transaction['amount'] = -int(transaction['amount'])
            methods_names = ['cb', 'especes', 'cheque']

            for var in self.check_vars:
                if var.get() == 1:
                    transaction['method'] = methods_names[self.check_vars.index(var)]

            add_transaction(self.window.user_id, transaction)

            self.window.switch_frame('BasePage')

    def show_error(self, text):
        self.error_canvas.destroy()
        self.error_canvas = tk.Canvas(self, height=50, width=self.window.winfo_width(),
                                      background=set_color("lightgreen"), highlightthickness=0)
        self.error_canvas.create_text(self.winfo_width() / 2, 25, text=text, font=('Roboto', 14), fill='red')

        self.error_canvas.place(x=0, y=80)

    def uncheck_buttons(self, exception):
        for button in self.check_buttons:
            if button != self.check_buttons[exception]:
                button.deselect()