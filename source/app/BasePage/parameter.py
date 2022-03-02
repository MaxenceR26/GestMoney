import json
import os
import tkinter as tk
import cv2

from data.data import select_image_user
from source.app.Sys import set_color, select_image, set_appwindow, center

from tkinter import filedialog as fd, messagebox


class ParametreWindow(tk.Tk):
    def __init__(self, user, email):
        tk.Tk.__init__(self)

        self.email = email
        self.user = user
        self.geometry("238x290")
        self.config(bg=set_color("entrycolor"))
        self.wm_overrideredirect(True)
        self.iconbitmap(select_image('parametre.ico'))
        self.title_bar()
        self.title("GestMoney | Paramètre")

        self.profile_img = tk.PhotoImage(master=self, file=select_image_user(self.user)).subsample(9)

        self.profile = tk.Label(self, image=self.profile_img, background=set_color('entrycolor'), bd=0)
        self.profile.photo = self.profile_img
        self.profile.pack(ipady=10)

        self.widgets()
        center(self)
        # Permet de voir l'icon dans notre barre des taches
        self.after(10, lambda: set_appwindow(self))

    def select_files(self):
        filetypes = (
            ('Type', '*.png'),
        )

        filenames = fd.askopenfilenames(
            title='GestMoney | Open files',
            initialdir='/',
            filetypes=filetypes)

        img = cv2.imread(filenames[0], cv2.IMREAD_UNCHANGED)

        width = img.shape[1]
        height = img.shape[0]

        if width and height == 500:
            self.profile_img = tk.PhotoImage(master=self, file=filenames).subsample(9)
            self.profile.photo = self.profile_img
            self.profile.configure(image=self.profile_img)

            image_show = tk.Label(self, text="/!\ Attention l'image s'actualisera \nau redémarrage de l'application !",
                                  background=set_color("entrycolor"),
                                  foreground="red", font=('Roboto', 8, 'bold'))
            image_show.place(x=25, y=138)

            with open(r'..\..\data\users.json', 'r+') as file:
                data = json.load(file)

                data[self.user]["image"] = filenames

            with open(r'..\..\data\users.json', 'w') as file:
                json.dump(data, file, indent=4)
        else:
            messagebox.showerror("GestMoney | Erreur","S'il vous plait veuillez mettre une image de taille : 500x500")

    def widgets(self):

        open_button = tk.Button(self, text="Modifier la photo", background=set_color("entrycolor"),
                                foreground=set_color("darkgreen"), bd=0, activebackground=set_color("entrycolor"),
                                activeforeground=set_color("darkgreen"), cursor='hand2', command=self.select_files)
        open_button.place(x=72, y=115)

        identifiant_text = tk.Label(self, text="Identifiant", background=set_color("entrycolor"),
                                    foreground=set_color("darkgreen"), font=('Roboto', 12))
        identifiant_text.place(x=40, y=150)

        self.id_entry = tk.Entry(self, background=set_color("darkgreen"), bd=0,
                                 font=('Roboto', 12), fg='#FFFFFF')
        self.id_entry.insert(0, self.user)
        self.id_entry.configure(justify='center')
        self.id_entry.place(x=16, y=175, width=204, height=25)

        email_text = tk.Label(self, text="Email", background=set_color("entrycolor"),
                              foreground=set_color("darkgreen"), font=('Roboto', 12))
        email_text.place(x=40, y=210)

        self.email_entry = tk.Entry(self, background=set_color("darkgreen"), bd=0,
                                    font=('Roboto', 12), fg='#FFFFFF')
        self.email_entry.insert(0, self.email)
        self.email_entry.place(x=16, y=235, width=204, height=25)

        # Copyright
        copyright_text = tk.Label(self, text="© 2022 GestMoney", background=set_color("entrycolor"),
                                  foreground=set_color("gray"), font=('Roboto', 10))
        copyright_text.place(x=55, y=266)

    def title_bar(self):
        title_bar = tk.Canvas(self, width=238, height=48, bg=set_color('darkgreen'), highlightthickness=0)
        title_bar.create_text(120, 25, text="GestMoney", font=('Roboto', 15, 'bold'), fill="white")
        title_bar.pack()

        imgs = tk.PhotoImage(master=self, file=select_image("parametre.png")).subsample(12)
        icon = tk.Label(self, image=imgs, background=set_color("darkgreen"), bd=0,
                        foreground=set_color("entrycolor"))
        icon.photo = imgs
        icon.place(x=5, y=2)

        quit_button = tk.Button(self, text="X", background=set_color("darkgreen"), cursor='hand2',
                                relief='groove', foreground=set_color("lightgreen"),
                                activebackground=set_color("darkgreen"), activeforeground=set_color("lightgreen"),
                                font=('Roboto', 15, 'bold'), command=self.destroy)
        quit_button.place(x=190, y=4, width=40, height=40)

        profile_img = tk.PhotoImage(master=self, file=select_image("profile-base.png")).subsample(14)
        profile_btn = tk.Button(self, image=profile_img, background=set_color('darkgreen'), cursor='hand2',
                                activebackground=set_color('darkgreen'), bd=0)
        profile_btn.photo = profile_img
        profile_btn.place(x=955, y=10)

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