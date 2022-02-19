import tkinter as tk
from source.app.Sys import set_color, set_appwindow, center


class InscriptionFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=431, height=473)

        self.ROBOTO_14 = ('Roboto', 14, 'bold')

        self.window = window

        # Config Window
        self.config(background=set_color("lightgreen"))

        self.x, self.y = None, None

        # Design

        self.title_bar()

        # Les entrées et leurs noms
        self.inputs_canvas = tk.Canvas(self, height=421, width=431, background=set_color("lightgreen"),
                                       highlightthickness=0)
        self.inputs_name()
        self.inputs_entry()

        # Bouton valider
        validate = tk.Button(self.inputs_canvas, text='Valider', bg=set_color('darkgreen'), fg=set_color('entrycolor'),
                             activebackground=set_color('buttonactive'), activeforeground=set_color('entrycolor'),
                             font=self.ROBOTO_14, relief='flat', cursor='hand2',
                             bd=0, command=lambda: print(self.mdp.get()))
        validate.place(x=165, y=345, width=100, height=40)

        self.inputs_canvas.place(x=0, y=52)

        # Copyright
        copyright_text = tk.Label(self, text="© 2022 GestMoney", background=set_color("lightgreen"),
                                  foreground=set_color("gray"), font=('Roboto', 10))
        copyright_text.place(x=155, y=450)

    # Fonctions déplacement fenêtre
    def mouse_down(self, event):
        self.x, self.y = event.x, event.y

    def mouse_up(self, event):
        self.x, self.y = None, None

    def mouse_drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x0 = self.window.winfo_x() + deltax
        y0 = self.window.winfo_y() + deltay
        self.window.geometry("+%s+%s" % (x0, y0))

    def apply_drag(self, elements):
        for element in elements:
            element.bind('<ButtonPress-1>', self.mouse_down)
            element.bind('<B1-Motion>', self.mouse_drag)
            element.bind('<ButtonRelease-1>', self.mouse_up)

    def inputs_name(self):
        names = ['Identifiant', 'E-mail', 'Mot de passe', 'Confirmation mot de passe', 'Montant actuel']

        for i in range(5):
            self.inputs_canvas.create_text(114, (i*59)+50, text=names[i], font=('Roboto', 13, 'bold'),
                                           fill=set_color("darkgreen"), anchor='w')

    def inputs_entry(self):
        self.user_id = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                                font=('Roboto', 12, 'bold'), fg='#FFFFFF')
        self.user_id.place(x=114, y=60, height=29, width=204)

        self.email = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                              font=('Roboto', 12, 'bold'), fg='#FFFFFF')
        self.email.place(x=114, y=119, height=29, width=204)

        self.mdp = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                            font=('Roboto', 12, 'bold'), fg='#FFFFFF', show='*')
        self.mdp.place(x=114, y=178, height=29, width=204)

        self.mdp_confirm = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                                    font=('Roboto', 12, 'bold'), fg='#FFFFFF', show='*')
        self.mdp_confirm.place(x=114, y=237, height=29, width=204)

        self.money = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                              font=('Roboto', 12, 'bold'), fg='#FFFFFF')
        self.money.place(x=114, y=296, height=29, width=204)

    def title_bar(self):
        title_bar = tk.Canvas(self, height=52, width=431, background=set_color("entrycolor"),
                              highlightthickness=0)
        title_bar.create_text(205, 25, text="GestMoney", font=('Roboto', 20, 'bold'), fill=set_color("gray"))
        title_bar.place(x=0, y=0)

        logo = tk.PhotoImage(file=r'img/icon.png').subsample(11)
        icon = tk.Label(self, image=logo, background=set_color("entrycolor"), bd=0,
                        foreground=set_color("lightgreen"))
        icon.photo = logo
        icon.place(x=10, y=5)

        quit_button = tk.Button(self, text="X", bd=2, background=set_color("entrycolor"), cursor='hand2',
                                relief='groove', foreground=set_color("buttontext"),
                                activebackground=set_color("lightgreen"), activeforeground=set_color("buttontext"),
                                font=self.ROBOTO_14, command=self.window.destroy)
        quit_button.place(x=385, y=5, height=40, width=40)

        self.apply_drag([title_bar, icon])


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry(f"431x473")
    window.wm_overrideredirect(True)
    window.after(10, lambda: set_appwindow(window))
    center(window)
    frame = InscriptionFrame(window)
    frame.pack()
    window.mainloop()