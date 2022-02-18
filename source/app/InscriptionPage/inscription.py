import tkinter as tk
from ctypes import windll
from source.app.Sys import set_color


def set_appwindow(mainWindow):  # Pour afficher l'icon dans la barre des taches

    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)

    mainWindow.wm_withdraw()
    mainWindow.after(10, mainWindow.wm_deiconify)


class InscriptionWindow(tk.Frame):

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
                             activebackground=set_color('entrycolor'), activeforeground=set_color('darkgreen'),
                             font=self.ROBOTO_14, relief='flat', cursor='hand2', bd=0)
        validate.place(x=165, y=330, width=100, height=40)

        self.inputs_canvas.place(x=0, y=52)

        # Copyright
        copyright_text = tk.Label(self, text="© 2022 GestMoney", background=set_color("lightgreen"),
                                  foreground=set_color("gray"), font=('Roboto', 13))
        copyright_text.place(x=130, y=450)

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
            self.inputs_canvas.create_text(114, (i*59)+25, text=names[i], font=('Roboto', 13, 'bold'),
                                           fill=set_color("darkgreen"), anchor='w')

    def inputs_entry(self):
        user_id = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                           font=('Roboto', 12, 'bold'), fg='#FFFFFF')
        user_id.place(x=114, y=35, height=29, width=204)

        email = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                         font=('Roboto', 12, 'bold'), fg='#FFFFFF')
        email.place(x=114, y=94, height=29, width=204)

        mdp = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                       font=('Roboto', 12, 'bold'), fg='#FFFFFF', show='*')
        mdp.place(x=114, y=153, height=29, width=204)

        mdp_confirm = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                               font=('Roboto', 12, 'bold'), fg='#FFFFFF', show='*')
        mdp_confirm.place(x=114, y=212, height=29, width=204)

        money = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                         font=('Roboto', 12, 'bold'), fg='#FFFFFF')
        money.place(x=114, y=271, height=29, width=204)

    def title_bar(self):
        title_bar = tk.Canvas(self, height=52, width=431, background=set_color("entrycolor"),
                              highlightthickness=0)
        title_bar.create_text(205, 25, text="GestMoney", font=('Roboto', 20, 'bold'), fill=set_color("gray"))
        title_bar.place(x=0, y=0)

        logo = tk.PhotoImage(file=r'../img/icon.png').subsample(11)
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
    frame = InscriptionWindow(window)
    frame.pack()
    window.wm_overrideredirect(True)
    window.after(10, lambda: set_appwindow(window))
    window.mainloop()