import tkinter as tk

from data.data import add_transaction
from source.app.Sys import set_color
from source.app.BasePage.baseframe import create_buttons, date_valid, show_error, create_copyright


class CreditFrame(tk.Frame):

    def __init__(self, window):
        self.window = window
        super().__init__(window, width=1023, height=640, bg=self.set_color('fourthbg'))
        frame_width = 1023

        self.error_canvas = tk.Canvas()

        self.canvas = tk.Canvas(self, height=640, width=1023, background=self.set_color('fourthbg'),
                                highlightthickness=0)
        self.canvas.create_text(frame_width / 2, 50, text="Créditer le compte", font=('Roboto', 30),
                                fill=self.set_color('text2'))

        create_copyright(self, self.canvas)

        self.create_inputs()
        self.canvas.pack()

    def create_inputs(self):
        self.canvas.create_text(350, 110, text='Montant', font=('Roboto', 18), fill=self.set_color('text'), anchor='w')
        self.canvas.create_text(350, 220, text='Origine de la somme', font=('Roboto', 18),
                                fill=self.set_color('text'), anchor='w')
        self.canvas.create_text(350, 330, text='Date', font=('Roboto', 18), fill=self.set_color('text'), anchor='w')

        self.canvas.create_text(343, 420, text='Type', font=('Roboto', 18),
                                fill=self.set_color('text'), anchor='w')

        self.amount = tk.Entry(self.canvas, bg=self.set_color('bg'), font=('Roboto', 15), fg='white',
                               bd=0, insertbackground=self.set_color('entrytext'))
        self.amount.place(x=350, y=130, width=330, height=46)

        self.origin = tk.Entry(self.canvas, bg=self.set_color('bg'), font=('Roboto', 15), fg='white',
                               bd=0, insertbackground=self.set_color('entrytext'))
        self.origin.place(x=350, y=240, width=330, height=46)

        self.date = tk.Entry(self.canvas, bg=self.set_color('bg'), font=('Roboto', 15), fg='white',
                             bd=0, insertbackground=self.set_color('entrytext'))
        self.date.place(x=350, y=240 + 110, width=330, height=46)

        cheque_var = tk.IntVar()
        virement_var = tk.IntVar()
        especes_var = tk.IntVar()
        self.check_vars = [virement_var, especes_var, cheque_var]

        vir_checkbutton = tk.Checkbutton(self, text='Virement', background=self.set_color('fourthbg'),
                                         foreground=self.set_color('text2'), font=('Roboto', 16),
                                         highlightthickness=0, bd=0, activebackground=self.set_color('fourthbg'),
                                         activeforeground=self.set_color('text2'), variable=virement_var,
                                         command=lambda: self.uncheck_buttons(0))
        vir_checkbutton.place(x=343, y=440)

        espece_checkbutton = tk.Checkbutton(self, text='Espèce', background=self.set_color('fourthbg'), bd=0,
                                            foreground=self.set_color('text2'), font=('Roboto', 16),
                                            activebackground=self.set_color('fourthbg'), highlightthickness=0,
                                            activeforeground=self.set_color('text2'), variable=especes_var,
                                            command=lambda: self.uncheck_buttons(1))
        espece_checkbutton.place(x=468, y=440)

        cheque_checkbutton = tk.Checkbutton(self, text='Chèque', background=self.set_color('fourthbg'), bd=0,
                                            foreground=self.set_color('text2'), font=('Roboto', 16),
                                            activebackground=self.set_color('fourthbg'), highlightthickness=0,
                                            activeforeground=self.set_color('text2'), variable=cheque_var,
                                            command=lambda: self.uncheck_buttons(2))
        cheque_checkbutton.place(x=583, y=440)

        self.check_buttons = [vir_checkbutton, espece_checkbutton, cheque_checkbutton]

        create_buttons(self, self.valid_credit)

    def valid_credit(self):
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

        elif not date_valid(date):
            self.show_error('Veuillez entrer une date au format dd/mm/yy')

        elif 1 not in [var.get() for var in self.check_vars]:
            self.show_error('Veuillez choisir un mode de paiement')

        else:
            transaction['amount'] = int(transaction['amount'])
            methods_names = ['Virement', 'Espèces', 'Chèque']

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
