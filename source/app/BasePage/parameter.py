import tkinter as tk

from source.app.Sys import set_color, select_image, set_appwindow, center


class ParamettreWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("238x290")
        self.config(bg=set_color("lightgreen"))
        self.wm_overrideredirect(True)
        self.title_bar()
        center(self)
        # Permet de voir l'icon dans notre barre des taches
        self.after(10, lambda: set_appwindow(self))

    def title_bar(self):
        title_bar = tk.Canvas(self, width=238, height=48, bg=set_color('entrycolor'), highlightthickness=0)
        title_bar.create_text(120, 25, text="GestMoney", font=('Roboto', 15, 'bold'), fill=set_color("gray"))
        title_bar.pack()

        imgs = tk.PhotoImage(file=select_image("parametre.png")).subsample(12)
        icon = tk.Label(self, image=imgs, background=set_color("entrycolor"), bd=0,
                        foreground=set_color("lightgreen"))
        icon.photo = imgs
        icon.place(x=10, y=2)

        quit_button = tk.Button(self, text="X", background=set_color("entrycolor"), cursor='hand2',
                                relief='groove', foreground=set_color("buttontext"),
                                activebackground=set_color("lightgreen"), activeforeground=set_color("buttontext"),
                                font=('Roboto', 15, 'bold'), command=exit)
        quit_button.place(x=190, y=4, width=40, height=40)

        profile_img = tk.PhotoImage(file=select_image("profile-base.png")).subsample(14)
        profile_btn = tk.Button(self, image=profile_img, background=set_color('entrycolor'), cursor='hand2',
                                activebackground=set_color('entrycolor'), bd=0)
        profile_btn.photo = profile_img
        profile_btn.place(x=955, y=10)

        self.apply_drag([title_bar, icon])

    def update(self):
        self.mainloop()

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


if __name__ == '__main__':
    ParamettreWindow().mainloop()
