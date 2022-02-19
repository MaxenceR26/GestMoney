import tkinter as tk
from source.app.Sys import set_color, select_image


class BaseFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.window = window

        self.title_bar()

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
        self.window.apply_drag([title_bar, icon])