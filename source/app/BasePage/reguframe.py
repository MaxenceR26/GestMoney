import tkinter as tk

from source.app.BasePage.baseframe import create_copyright, create_buttons, show_error
from source.app.Sys import set_color


class ReguFrame(tk.Frame):
    def __init__(self, window):
        self.window = window
        frame_width = 1023

        super().__init__(window, width=frame_width, height=640, bg=self.set_color('fourthbg'))

        self.error_canvas = tk.Canvas()

        self.canvas = tk.Canvas(self, height=640, width=frame_width, background=self.set_color('fourthbg'),
                                highlightthickness=0)

        self.canvas.create_line(550, 1000, 550, -10, fill='white')

        self.canvas.create_text(265, 50, text="""
Créer une
dépense régulière
""", font=('Roboto', 30),
                                fill=self.set_color('text2'), justify="center")



        self.create_inputs()
        self.canvas.pack()

    def create_inputs(self):
        x_pos = 100
        entry_width = 330
        entry_height = 46

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

        create_buttons(self, self.valid_debit, 50, 340, 160)

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