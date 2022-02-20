import tkinter as tk
from source.app.OnConnexion.connexion import ConnectionFrame
from Sys import select_image, set_color, center, set_appwindow
from InscriptionPage.inscription import InscriptionFrame
from BasePage.baseframe import BaseFrame
from BasePage.creditframe import CreditFrame
from BasePage.homeframe import HomeFrame
from source.app.BasePage.debitframe import DebitFrame


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
        self.title_frame = None
        self.main_frame = None
        self.active_frame = None

        # Titlebar
        self.widget_title_bar()

        # Permet de voir l'icon dans notre barre des taches
        self.after(10, lambda: set_appwindow(self))

        # Permet d'afficher notre première fenêtre ( Base Page )

        self.active_frame = ConnectionFrame(self)
        self.active_frame.pack()

    def switch_frame(self, frame_name):

        if frame_name == 'InscriptionFrame':
            self.title_frame.destroy(), self.active_frame.destroy()
            self.geometry('431x473')
            self.active_frame = InscriptionFrame(self)
            self.active_frame.pack()
            center(self)

        elif frame_name == 'BasePage':
            self.title_frame.destroy(), self.active_frame.destroy()
            self.geometry('1110x664')
            self.main_frame = BaseFrame(self)
            self.main_frame.pack()
            self.switch_frame('HomePage')
            center(self)

        elif frame_name == 'HomePage':
            self.active_frame.destroy()
            self.active_frame = HomeFrame(self)
            self.active_frame.place(x=0, y=80)

        elif frame_name == 'DebitPage':
            self.active_frame.destroy()
            self.active_frame = DebitFrame(self)
            self.active_frame.place(x=0, y=80)

        elif frame_name == 'CreditPage':
            self.active_frame.destroy()
            self.active_frame = CreditFrame(self)
            self.active_frame.place(x=0, y=80)

        elif frame_name == 'ConnexionPage':
            self.title_frame.destroy(), self.active_frame.destroy(), self.main_frame.destroy()
            self.geometry("679x406")
            self.widget_title_bar()
            self.active_frame = ConnectionFrame(self)
            self.active_frame.pack()
            center(self)

    def widget_title_bar(self):
        self.title_frame = tk.Frame(self)
        title_bar = tk.Canvas(self.title_frame, width=679, height=47, bg=set_color('entrycolor'), highlightthickness=0)
        title_bar.create_text(135, 22, text="GestMoney", font=('Roboto', 20, 'bold'), fill=set_color("gray"))
        title_bar.pack()

        imgs = tk.PhotoImage(file=select_image("icon.png")).subsample(11)
        icon = tk.Label(self.title_frame, image=imgs, background=set_color("entrycolor"), bd=0,
                        foreground=set_color("lightgreen"))
        icon.photo = imgs
        icon.place(x=5, y=0)

        quit_button = tk.Button(self.title_frame, text="X", background=set_color("entrycolor"), cursor='hand2',
                                relief='groove', foreground=set_color("darkgreen"),
                                activebackground=set_color("lightgreen"), activeforeground=set_color("darkgreen"),
                                font=('Roboto', 14, 'bold'), command=exit)
        quit_button.place(x=620, y=3, width=40, height=40)
        self.title_frame.pack()

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
