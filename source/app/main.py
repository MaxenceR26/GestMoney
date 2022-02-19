import tkinter as tk
from source.app.OnConnexion.connexion import ConnectionFrame
from Sys import select_image, set_color, center, set_appwindow
from InscriptionPage.inscription import InscriptionFrame
from BasePage.baseframe import BaseFrame


class Main(tk.Tk):
    def __init__(self, window):
        tk.Tk.__init__(self, window)
        self.window = window

        self.geometry("679x406")
        self.config(background=set_color("lightgreen"))
        self.title('GestMoney')
        self.iconbitmap(select_image('icon.ico'))
        center(self)
        self.wm_overrideredirect(True)
        self.x, self.y = None, None
        self.JFrame = None
        self._frame = None

        # Titlebar
        self.widget_title_bar()

        # Permet de voir l'icon dans notre barre des taches
        self.after(10, lambda: set_appwindow(self))

        # Permet d'afficher notre première fenêtre ( Base Page )

        self._frame = ConnectionFrame(self)
        self._frame.pack()

    def switch_frame(self, frame_name):

        if frame_name == 'InscriptionFrame':
            self.JFrame.destroy(), self._frame.destroy()
            self.geometry('431x473')
            self._frame = InscriptionFrame(self)
            self._frame.pack()
            center(self)

        elif frame_name == 'BasePage':
            self.JFrame.destroy(), self._frame.destroy()
            self.geometry('1110x664')
            self._frame = BaseFrame(self)
            self._frame.pack()
            center(self)

        else:
            self.JFrame.destroy(), self._frame.destroy()
            self.widget_title_bar()
            self._frame = ConnectionFrame(self)
            self._frame.pack()

    def widget_title_bar(self):
        self.JFrame = tk.Frame(self)
        title_bar = tk.Canvas(self.JFrame, width=679, height=47, bg=set_color('entrycolor'), highlightthickness=0)
        title_bar.create_text(135, 22, text="GestMoney", font=('Roboto', 20, 'bold'), fill=set_color("gray"))
        title_bar.pack()

        imgs = tk.PhotoImage(file=select_image("icon.png")).subsample(11)
        icon = tk.Label(self.JFrame, image=imgs, background=set_color("entrycolor"), bd=0,
                        foreground=set_color("lightgreen"))
        icon.photo = imgs
        icon.place(x=10, y=0)

        quit_button = tk.Button(self.JFrame, text="X", background=set_color("entrycolor"), cursor='hand2',
                                relief='groove', foreground=set_color("buttontext"),
                                activebackground=set_color("lightgreen"), activeforeground=set_color("buttontext"),
                                font=('Roboto', 14, 'bold'), command=exit)
        quit_button.place(x=620, y=3, width=40, height=40)
        self.JFrame.pack()

        self.apply_drag([title_bar, icon])

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


if __name__ == "__main__":
    app = Main(None)
    app.mainloop()
