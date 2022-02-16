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
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())


def Color(set_color: str):
    color = {'lightgreen': '#EAFCEC',
             'entrycolor': '#89DA92',
             'buttontext': '#45794A',
             'gray': '#666666'
             }
    return color[set_color]


class Main:
    def __init__(self):
        super(Main).__init__()

        # Config Window

        self.root = tk.Tk()

        self.root.geometry("851x512")
        self.root.config(background=Color("lightgreen"))
        self.root.wm_overrideredirect(True)

        self.x, self.y = None, None


        self.root.bind('<ButtonPress-1>', self.mouse_down)
        self.root.bind('<B1-Motion>', self.mouse_drag)
        self.root.bind('<ButtonRelease-1>', self.mouse_up)

        # Design
        imgs = tk.PhotoImage(file=r'../ressource/img/icon.png').subsample(20)
        icons = tk.Label(self.root, image=imgs, background=Color("lightgreen"), bd=0, foreground=Color("lightgreen"))
        icons.photo = imgs
        icons.place(x=10, y=10)

        title = tk.Label(self.root, text="GestMoney", background=Color("lightgreen"), foreground=Color("gray"), font=('Roboto', 24, 'bold'))
        title.place(x=80, y=10)

        quit_button = tk.Button(self.root, text="X", bd=2, background=Color("lightgreen"),
                                foreground=Color("buttontext"), activebackground=Color("lightgreen"),
                                activeforeground=Color("buttontext"), font=('Roboto', 14, 'bold'),
                                command= lambda: self.root.destroy())
        quit_button.place(x=800, y=10)

        # Permet de voir l'icon dans notre barre des taches
        self.root.after(10, lambda: set_appwindow(self.root))

    # Fonction
    def mouse_down(self, event):
        self.x, self.y = event.x, event.y

    def mouse_up(self, event):
        self.x, self.y = None, None

    def mouse_drag(self, event):
        try:
            deltax = event.x - self.x
            deltay = event.y - self.y
            x0 = self.root.winfo_x() + deltax
            y0 = self.root.winfo_y() + deltay
            self.root.geometry("+%s+%s" % (x0, y0))
        except:
            pass

    def update(self):
        self.root.mainloop()


if __name__ == "__main__":
    Main().update()
