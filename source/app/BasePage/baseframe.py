import tkinter as tk

from source.app.BasePage.parameter import ParamettreWindow
from source.app.Sys import set_color, select_image

def launchwindowParamettre():
    ParamettreWindow().update()


class BaseFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.window = window

        # Affichage de la titlebar
        self.title_bar()

        self.widgets()

    def widgets(self):
        canvas = tk.Canvas(self, width=257, height=585, bg=set_color("entrycolor"), highlightthickness=0)
        canvas.create_line(1000, 0, -10, 0, fill=set_color("lightgreen"))
        canvas.create_line(1000, 150, -10, 150, fill=set_color("lightgreen"))
        canvas.create_line(1000, 300, -10, 300, fill=set_color("lightgreen"))
        canvas.create_line(1000, 450, -10, 450, fill=set_color("lightgreen"))
        canvas.create_text(128.5, 50, text="Argent", font=('Roboto', 20, 'bold'), fill='white')
        canvas.create_text(128.5, 90, text="105400", font=('Roboto', 14), fill='white')
        canvas.pack(side=tk.RIGHT)

        credit_button = tk.Button(self, text="Créditer l'argent", font=('Roboto', 14), fg='white',
                                  bg=set_color("buttontext"), bd=0,
                                  activeforeground='white', activebackground=set_color("buttontext"))
        credit_button.place(x=880, y=290, width=201, height=33)

        debit_button = tk.Button(self, text="Débiter effectuer", font=('Roboto', 14), fg='white',
                                  bg=set_color("buttontext"), bd=0,
                                 activeforeground='white', activebackground=set_color("buttontext"))
        debit_button.place(x=880, y=440, width=201, height=33)

        deco_button = tk.Button(self, text="Débiter effectuer", font=('Roboto', 14), fg='white',
                                 bg=set_color("buttontext"), bd=0,
                                activeforeground='white', activebackground=set_color("buttontext"))
        deco_button.place(x=880, y=575, width=206, height=49)

    def title_bar(self):
        title_bar = tk.Canvas(self, width=1110, height=80, bg=set_color('entrycolor'), highlightthickness=0)
        title_bar.create_text(200, 40, text="GestMoney", font=('Roboto', 30, 'bold'), fill=set_color("gray"))
        title_bar.pack()

        imgs = tk.PhotoImage(file=select_image("icon.png")).subsample(7)
        icon = tk.Label(self, image=imgs, background=set_color("entrycolor"), bd=0,
                        foreground=set_color("lightgreen"))
        icon.photo = imgs
        icon.place(x=10, y=0)

        quit_button = tk.Button(self, text="X", background=set_color("entrycolor"), cursor='hand2',
                                relief='groove', foreground=set_color("buttontext"),
                                activebackground=set_color("lightgreen"), activeforeground=set_color("buttontext"),
                                font=('Roboto', 20, 'bold'), command=exit)
        quit_button.place(x=1040, y=10, width=60, height=60)

        profile_img = tk.PhotoImage(file=select_image("profile-base.png")).subsample(14)
        profile_btn = tk.Button(self, image=profile_img, background=set_color('entrycolor'), cursor='hand2', activebackground=set_color('entrycolor'), bd=0, command=launchwindowParamettre)
        profile_btn.photo = profile_img
        profile_btn.place(x=955, y=10)

        self.window.apply_drag([title_bar, icon])