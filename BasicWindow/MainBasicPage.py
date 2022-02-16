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
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)

    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())


def Color(set_color: str):
    color = {'lightgreen': '#EAFCEC',
             'entrycolor': '#89DA92',
             'buttontext': '#45794A',
             }
    return color[set_color]


class Main:
    def __init__(self):
        super(Main).__init__()
        self.root = tk.Tk()

        self.root.geometry("851x512")
        self.root.config(background=Color("lightgreen"))
        self.root.wm_overrideredirect(True)

        self.x, self.y = None, None

        self.root.after(10, lambda: set_appwindow(self.root))  # Permet de voir l'icon dans notre barre des taches
        self.root.bind('<ButtonPress-1>', self.mouse_down)
        self.root.bind('<B1-Motion>', self.mouse_drag)
        self.root.bind('<ButtonRelease-1>', self.mouse_up)

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
