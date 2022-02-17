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


class InscriptionWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.COLOR = {
            'lightgreen': '#EAFCEC',
            'entrycolor': '#89DA92',
            'buttontext': '#45794A',
            'gray': '#666666'
        }

        # Config Window

        window_width, window_height = 431, 473

        self.geometry("431x473+100+100")
        self.config(background=self.COLOR["lightgreen"])
        self.wm_overrideredirect(True)

        self.x, self.y = None, None

        # Design

        title_bar = tk.Canvas(self, height=52, width=window_width, background=self.COLOR["entrycolor"],
                              highlightthickness=0)
        title_bar.create_text(205, 25, text="GestMoney", font=('Roboto', 20, 'bold'), fill=self.COLOR["gray"])
        title_bar.place(x=0, y=0)

        logo = tk.PhotoImage(file=r'../../ressource/img/icon.png').subsample(11)
        icon = tk.Label(self, image=logo, background=self.COLOR["entrycolor"], bd=0, foreground=self.COLOR["lightgreen"])
        icon.photo = logo
        icon.place(x=10, y=5)

        quit_button = tk.Button(self, text="X", bd=2, background=self.COLOR["entrycolor"],
                                foreground=self.COLOR["buttontext"], activebackground=self.COLOR["lightgreen"],
                                activeforeground=self.COLOR["buttontext"], font=('Roboto', 14, 'bold'),
                                command=self.destroy)
        quit_button.place(x=385, y=5, height=40, width=40)

        # Permet de voir l'icon dans notre barre des taches
        self.after(10, lambda: set_appwindow(self))

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
        x0 = self.winfo_x() + deltax
        y0 = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x0, y0))

    def apply_drag(self, elements):
        for element in elements:
            element.bind('<ButtonPress-1>', self.mouse_down)
            element.bind('<B1-Motion>', self.mouse_drag)
            element.bind('<ButtonRelease-1>', self.mouse_up)

    def update(self):
        self.mainloop()


if __name__ == "__main__":
    InscriptionWindow().update()