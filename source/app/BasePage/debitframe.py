import tkinter as tk

from source.app.Sys import set_color
from source.app.BasePage.baseframe import create_buttons, date_valid, show_error, create_copyright
from data.data import add_transaction


class DebitFrame(tk.Frame):

    def __init__(self, window):
        self.window = window
        frame_width = 1023
        
        super().__init__(window, width=frame_width, height=640, bg=self.set_color('bg'))
        
        self.error_canvas = tk.Canvas()
        
        self.canvas = tk.Canvas(self, height=640, width=frame_width, background=self.set_color('bg'), highlightthickness=0)

        self.canvas.create_text(frame_width/2, 50, text="Débiter le compte", font=('Roboto', 30, 'bold'),
                                fill=self.set_color('text'))

        create_copyright(self, self.canvas)

        self.create_inputs()
        self.canvas.pack()

    def create_inputs(self):
        self.canvas.create_text(150, 150, text='Magasin', font=('Roboto', 18), fill=self.set_color('text'), anchor='w')
        self.canvas.create_text(150, 270, text='Achat', font=('Roboto', 18),
                                fill=self.set_color('text'), anchor='w')
        self.canvas.create_text(543, 150, text='Montant', font=('Roboto', 18), fill=self.set_color('text'), anchor='w')
        self.canvas.create_text(543, 270, text='Date', font=('Roboto', 18), fill=self.set_color('text'), anchor='w')
        self.canvas.create_text(150, 375, text='Moyen de paiement', font=('Roboto', 18),
                                fill=self.set_color('text'), anchor='w')

        self.market = tk.Entry(self.canvas, bg=self.set_color('darkbg'), font=('Roboto', 15), fg='white', bd=0,
                               insertbackground=self.set_color('entrytext'))
        self.market.place(x=150, y=170, width=330, height=46)

        self.amount = tk.Entry(self.canvas, bg=self.set_color('darkbg'), font=('Roboto', 15), fg='white', bd=0,
                               insertbackground=self.set_color('entrytext'))
        self.amount.place(x=543, y=170, width=330, height=46)

        self.buy_type = tk.Entry(self.canvas, bg=self.set_color('darkbg'), font=('Roboto', 15), fg='white', bd=0,
                                 insertbackground=self.set_color('entrytext'))
        self.buy_type.place(x=150, y=290, width=330, height=46)

        self.date = tk.Entry(self.canvas, bg=self.set_color('darkbg'), font=('Roboto', 15), fg='white', bd=0,
                             insertbackground=self.set_color('entrytext'))
        self.date.place(x=543, y=290, width=330, height=46)

        cheque_var = tk.IntVar()
        cb_var = tk.IntVar()
        especes_var = tk.IntVar()
        self.check_vars = [cb_var, especes_var, cheque_var]

        cb_checkbutton = tk.Checkbutton(self, text='CB', background=self.set_color('bg'), variable=cb_var,
                                        foreground=self.set_color('text'), font=('Roboto', 16, 'bold'),
                                        highlightthickness=0, bd=0, activebackground=self.set_color('bg'),
                                        activeforeground=self.set_color('text'),
                                        command=lambda: self.uncheck_buttons(0))
        cb_checkbutton.place(x=410, y=360)

        espece_checkbutton = tk.Checkbutton(self, text='Espèce', background=self.set_color('bg'), bd=0,
                                            foreground=self.set_color('text'), font=('Roboto', 16, 'bold'),
                                            activebackground=self.set_color('bg'), highlightthickness=0,
                                            activeforeground=self.set_color('text'), variable=especes_var,
                                            command=lambda: self.uncheck_buttons(1))
        espece_checkbutton.place(x=492, y=360)

        cheque_checkbutton = tk.Checkbutton(self, text='Chèque', background=self.set_color('bg'), bd=0,
                                            foreground=self.set_color('text'), font=('Roboto', 16, 'bold'),
                                            activebackground=self.set_color('bg'), highlightthickness=0,
                                            activeforeground=self.set_color('text'), variable=cheque_var,
                                            command=lambda: self.uncheck_buttons(2))
        cheque_checkbutton.place(x=615, y=360)

        self.check_buttons = [cb_checkbutton, espece_checkbutton, cheque_checkbutton]

        create_buttons(self, self.valid_debit)

    def valid_debit(self):
        market = self.market.get()
        buy_type = self.buy_type.get()
        amount = self.amount.get()
        date = self.date.get()

        transaction = {
            'type': 'debit',
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
            self.show_error('Veuillez choisir un mode paiement')

        else:
            transaction['amount'] = -int(transaction['amount'])
            methods_names = ['Carte Bancaire', 'Espèces', 'Chèque']

            for var in self.check_vars:
                if var.get() == 1:
                    transaction['method'] = methods_names[self.check_vars.index(var)]

            add_transaction(self.window.user_id, transaction)

            self.window.switch_frame('BasePage')

    def show_error(self, text):
        show_error(self, text)

    def uncheck_buttons(self, exception):
        for button in self.check_buttons:
            if button != self.check_buttons[exception]:
                button.deselect()

    def set_color(self, color):
        return set_color(self.window.color_theme, color)