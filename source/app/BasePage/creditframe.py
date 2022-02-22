import tkinter as tk

from source.app.Sys import set_color


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
        self.canvas.create_text(50, 130, text='Montant', font=('Roboto', 18), fill=set_color('darkgreen'), anchor='w')
        self.canvas.create_text(50, 250, text='Origine de la somme', font=('Roboto', 18),
                                fill=set_color('darkgreen'), anchor='w')
        self.canvas.create_text(470, 130, text='Date', font=('Roboto', 18), fill=set_color('darkgreen'), anchor='w')

        self.amount = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.amount.place(x=50, y=150, width=330, height=46)

        self.origin = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.origin.place(x=50, y=270, width=330, height=46)

        self.date = tk.Entry(self.canvas, bg=set_color('entrycolor'), font=('Roboto', 15), fg='white', bd=0)
        self.date.place(x=470, y=150, width=330, height=46)

        Cb_checkbutton = tk.Checkbutton(self, text='CB', onvalue=1, offvalue=0, background=set_color("lightgreen"), foreground=set_color("darkgreen"),
                                        font=('Roboto', 16, 'bold'), highlightthickness=0, bd=0,
                                        activebackground=set_color("lightgreen"),
                                        activeforeground=set_color("darkgreen")
                                        )
        Cb_checkbutton.place(x=480, y=280)

        Espece_checkbutton = tk.Checkbutton(self, text='Espèce', onvalue=1, offvalue=0, background=set_color("lightgreen"), foreground=set_color("darkgreen"),
                                            font=('Roboto', 16, 'bold'), highlightthickness=0, bd=0,
                                            activebackground=set_color("lightgreen"),
                                            activeforeground=set_color("darkgreen")
                                            )
        Espece_checkbutton.place(x=555, y=280)

        Cheque_checkbutton = tk.Checkbutton(self, text='Chèque', onvalue=1, offvalue=0, background=set_color("lightgreen"), foreground=set_color("darkgreen"),
                                            font=('Roboto', 16, 'bold'), highlightthickness=0, bd=0, activebackground=set_color("lightgreen"),
                                            activeforeground=set_color("darkgreen"))
        Cheque_checkbutton.place(x=670, y=280)

        valid_button = tk.Button(self, text="Valider", background=set_color("lightgreen"), foreground=set_color("darkgreen"),
                                 font=('Roboto', 16, 'bold'), relief="ridge", activebackground=set_color("lightgreen"),
                                 activeforeground=set_color("darkgreen"))
        valid_button.place(x=100, y=400, width=211,height=84)

        annuler_button = tk.Button(self, text="Annuler", background=set_color("lightgreen"),
                                 foreground="red", font=('Roboto', 16, 'bold'), relief="ridge", activebackground=set_color("lightgreen"),
                                 activeforeground="red", command=lambda: self.window.switch_frame('HomePage'))
        annuler_button.place(x=550, y=400, width=211, height=84)
