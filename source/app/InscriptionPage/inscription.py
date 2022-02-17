import tkinter as tk
from ctypes import windll


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

        self.COLOR = {
            'lightgreen': '#EAFCEC',
            'entrycolor': '#89DA92',
            'buttontext': '#45794A',
            'gray': '#666666',
            'darkgreen': '#41A04C',
            'white': '#FFFFFF'
        }

        ROBOTO_14 = ('Roboto', 14, 'bold')

        self.window = window

        # Config Window
        self.config(background=self.COLOR["lightgreen"])

        self.x, self.y = None, None

        # Design

        title_bar = tk.Canvas(self, height=52, width=431, background=self.COLOR["entrycolor"],
                              highlightthickness=0)
        title_bar.create_text(205, 25, text="GestMoney", font=('Roboto', 20, 'bold'), fill=self.COLOR["gray"])
        title_bar.place(x=0, y=0)

        logo = tk.PhotoImage(file=r'../img/icon.png').subsample(11)
        icon = tk.Label(self, image=logo, background=self.COLOR["entrycolor"], bd=0,
                        foreground=self.COLOR["lightgreen"])
        icon.photo = logo
        icon.place(x=10, y=5)

        quit_button = tk.Button(self, text="X", bd=2, background=self.COLOR["entrycolor"],
                                foreground=self.COLOR["buttontext"], activebackground=self.COLOR["lightgreen"],
                                activeforeground=self.COLOR["buttontext"], font=ROBOTO_14,
                                command=self.window.destroy)
        quit_button.place(x=385, y=5, height=40, width=40)

        # Les noms des entrées

        inputs_canvas = tk.Canvas(self, height=421, width=431, background=self.COLOR["lightgreen"],
                                  highlightthickness=0)
        inputs_canvas.create_text(110, 25, text="Identifiant", font=('Roboto', 13, 'bold'),
                                  fill=self.COLOR["darkgreen"], anchor='w')
        inputs_canvas.create_text(110, 84, text="E-mail", font=('Roboto', 13, 'bold'),
                                  fill=self.COLOR["darkgreen"], anchor='w')
        inputs_canvas.create_text(110, 143, text="Mot de passe", font=('Roboto', 13, 'bold'),
                                  fill=self.COLOR["darkgreen"], anchor='w')
        inputs_canvas.create_text(110, 202, text="Confirmation mot de passe", font=('Roboto', 13, 'bold'),
                                  fill=self.COLOR["darkgreen"], anchor='w')
        inputs_canvas.create_text(110, 261, text="Montant actuel", font=('Roboto', 13, 'bold'),
                                  fill=self.COLOR["darkgreen"], anchor='w')
        inputs_canvas.place(x=0, y=52)

        # Les différentes entrées

        id = tk.Entry(inputs_canvas, bd=0, bg=self.COLOR['entrycolor'], font=('Roboto', 13, 'bold'), fg='#FFFFFF')
        id.place(x=110, y=35, height=29, width=204)

        email = tk.Entry(inputs_canvas, bd=0, bg=self.COLOR['entrycolor'], font=('Roboto', 13, 'bold'), fg='#FFFFFF')
        email.place(x=110, y=94, height=29, width=204)

        mdp = tk.Entry(inputs_canvas, bd=0, bg=self.COLOR['entrycolor'],
                       font=('Roboto', 13, 'bold'),fg='#FFFFFF', show='*')
        mdp.place(x=110, y=153, height=29, width=204)

        mdp_confirm = tk.Entry(inputs_canvas, bd=0, bg=self.COLOR['entrycolor'],
                               font=('Roboto', 13, 'bold'), fg='#FFFFFF', show='*')
        mdp_confirm.place(x=110, y=212, height=29, width=204)

        money = tk.Entry(inputs_canvas, bd=0, bg=self.COLOR['entrycolor'], font=('Roboto', 13, 'bold'), fg='#FFFFFF')
        money.place(x=110, y=271, height=29, width=204)

        # Bouton valider

        validate = tk.Button(inputs_canvas, text='Valider', bg=self.COLOR['entrycolor'], fg=self.COLOR['darkgreen'], bd=0)
        validate.place(x=190, y=320, width=100, height=40)

        # Copyright

        copyright_text = tk.Label(self, text="© 2022 GestMoney", background=self.COLOR["lightgreen"],
                                  foreground=self.COLOR["gray"], font=('Roboto', 13))
        copyright_text.place(x=130, y=450)

        # Permettre le mouvement seulement sur la title bar
        self.apply_drag([title_bar, icon])

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


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry(f"431x473")
    frame = InscriptionWindow(window)
    frame.pack()
    window.wm_overrideredirect(True)
    window.after(10, lambda: set_appwindow(window))

    window.mainloop()
