import tkinter as tk

from source.app.Sys import set_color
from source.app.BasePage.baseframe import create_buttons


class CreditFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=853, height=584)
        self.window = window

        self.canvas = tk.Canvas(self, height=853, width=853, background=set_color('lightgreen'), highlightthickness=0)

        self.canvas.create_text(426.5, 50, text="Créditer le compte", font=('Roboto', 30, 'bold'),
                                fill=set_color("darkgreen"))

        self.create_inputs()
        self.canvas.pack()

    def create_inputs(self):
        self.canvas.create_text(50, 150, text='Montant', font=('Roboto', 18), fill=set_color('darkgreen'), anchor='w')
        self.canvas.create_text(50, 270, text='Origine de la somme', font=('Roboto', 18),
                                fill=set_color('darkgreen'), anchor='w')
        self.canvas.create_text(470, 150, text='Date', font=('Roboto', 18), fill=set_color('darkgreen'), anchor='w')

        self.canvas.create_text(470, 270, text='Moyen de paiement', font=('Roboto', 18),
                                fill=set_color('darkgreen'), anchor='w')

        self.amount = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.amount.place(x=50, y=170, width=330, height=46)

        self.origin = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.origin.place(x=50, y=290, width=330, height=46)

        self.date = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.date.place(x=470, y=170, width=330, height=46)

        cb_checkbutton = tk.Checkbutton(self, text='CB', background=set_color("lightgreen"),
                                        foreground=set_color("darkgreen"), font=('Roboto', 16, 'bold'),
                                        highlightthickness=0, bd=0, activebackground=set_color("lightgreen"),
                                        activeforeground=set_color("darkgreen"),
                                        command=lambda: self.uncheck_buttons(0))
        cb_checkbutton.place(x=470, y=300)

        espece_checkbutton = tk.Checkbutton(self, text='Espèce', background=set_color("lightgreen"), bd=0,
                                            foreground=set_color("darkgreen"), font=('Roboto', 16, 'bold'),
                                            activebackground=set_color("lightgreen"), highlightthickness=0,
                                            activeforeground=set_color("darkgreen"),
                                            command=lambda: self.uncheck_buttons(1))
        espece_checkbutton.place(x=545, y=300)

        cheque_checkbutton = tk.Checkbutton(self, text='Chèque', background=set_color("lightgreen"), bd=0,
                                            foreground=set_color("darkgreen"), font=('Roboto', 16, 'bold'),
                                            activebackground=set_color("lightgreen"), highlightthickness=0,
                                            activeforeground=set_color("darkgreen"),
                                            command=lambda: self.uncheck_buttons(2))
        cheque_checkbutton.place(x=660, y=300)

        self.check_buttons = [cb_checkbutton, espece_checkbutton, cheque_checkbutton]

        create_buttons(self, self.valid_credit)


    def valid_credit(self):
        pass

    def uncheck_buttons(self, exception):
        for button in self.check_buttons:
            if button != self.check_buttons[exception]:
                button.deselect()