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

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.COLOR = {
            'lightgreen': '#EAFCEC',
            'entrycolor': '#89DA92',
            'buttontext': '#45794A',
            'gray': '#666666'
        }

        # Config Window

        self.geometry("679x406")
        self.config(background=self.COLOR["lightgreen"])
        self.wm_overrideredirect(True)

        self.x, self.y = None, None

        # Design

        Title_bar = tk.Canvas(width=679, height=47, bg=self.COLOR['entrycolor'], highlightthickness=0)
        Title_bar.pack()

        Title_bar.bind('<ButtonPress-1>', self.mouse_down)
        Title_bar.bind('<B1-Motion>', self.mouse_drag)
        Title_bar.bind('<ButtonRelease-1>', self.mouse_up)


        imgs = tk.PhotoImage(file=r'../ressource/img/icon.png').subsample(11)
        icons = tk.Label(self, image=imgs, background=self.COLOR["entrycolor"], bd=0,
                         foreground=self.COLOR["lightgreen"])
        icons.photo = imgs
        icons.place(x=10, y=0)

        icons.bind('<ButtonPress-1>', self.mouse_down)
        icons.bind('<B1-Motion>', self.mouse_drag)
        icons.bind('<ButtonRelease-1>', self.mouse_up)

        title = tk.Label(self, text="GestMoney", background=self.COLOR["entrycolor"], foreground=self.COLOR["gray"],
                         font=('Roboto', 20, 'bold'))
        title.place(x=60, y=2)

        title.bind('<ButtonPress-1>', self.mouse_down)
        title.bind('<B1-Motion>', self.mouse_drag)
        title.bind('<ButtonRelease-1>', self.mouse_up)

        quit_button = tk.Button(self, text="X", bd=2, background=self.COLOR["entrycolor"],
                                foreground=self.COLOR["buttontext"], activebackground=self.COLOR["entrycolor"],
                                activeforeground=self.COLOR["buttontext"], font=('Roboto', 14, 'bold'),
                                command=self.destroy)
        quit_button.place(x=620, y=3, width=45, height=40)

        # Centrer la fenêtre au milieu de l'écran
        center(self)

        # Permet de voir l'icon dans notre barre des taches
        self.after(10, lambda: set_appwindow(self))

    # Fonction
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

    def update(self):
        self.mainloop()


if __name__ == "__main__":
    MainWindow().update()
