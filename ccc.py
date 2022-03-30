import os
from ctypes import windll
from tkinter import *
from tkinter import filedialog


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
    win.geometry(f'{width}x{height}+{x}+{y}')
    win.deiconify()


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


class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        main = self
        main.title("Note pad")
        main.geometry("720x480")
        main.minsize(720, 480)
        frame = Frame0(main)
        frame.pack()
        main.config(background='#959595')
        center(main)
        # self.wm_overrideredirect(True)
        # set_appwindow(self)
        self.mainloop()

class Frame0(Frame):
    def __init__(self, window):
        Frame.__init__(self, bg='#959595', width=720, height=480)
        self.haut = self.winfo_reqheight()
        self.large = self.winfo_reqwidth()
        self.file = []
        text = Text(self, height=self.haut, width=self.large, bg='#959595')
        text.pack()
        filemenu = Menu(self, tearoff=0)
        filemenu.add_command(label="Exit", command=lambda: exit())
        filemenu.add_command(label="Save", command=lambda: self.savemyfile(text))
        filemenu.add_command(label="Import", command=lambda: self.importmyfile(text))

        filemenu.config()
        window.config(menu=filemenu)

    def savemyfile(self, text):
        if not self.file:
            print("Tu n'as rien importer !")
        else:
            with open(self.file[0], "w+") as file:
                text_get = text.get(1.0, "end-1c")
                file.write("\n" + f"{text_get}")
            file.close()

    def importmyfile(self, text):
        if file := filedialog.askopenfile(
            mode='r', filetypes=[('Text Files', '*.txt')]
        ):
            filepath = os.path.abspath(file.name)
            self.file.append(filepath)
            with open(filepath, 'r') as file:
                data = file.read()
                text.insert(END, data)




Main()