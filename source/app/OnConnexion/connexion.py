import json
import tkinter as tk

from data.data import add_user_in_activity_recent, get_recent_user, select_image_user
from source.app.Sys import set_color


class ConnectionFrame(tk.Frame):
    def __init__(self, window):
        self.window = window
        tk.Frame.__init__(self, window, width=700, height=500, bg=self.set_color("lightblue"))
        self._frame = None

        # Design de la page de base quand on lance l'application

        welcometext = tk.Label(self, text="""

Bienvenue sur GestMoney

Tu cherches à gérer tes comptes
mais tu n’y arrive pas ?

Alors GestMoney est la 
pour t’aider !

        """, background=self.set_color("lightblue"), foreground=self.set_color("white"), font=('Roboto', 16))
        welcometext.place(x=30, y=10)

        # Gestion de demande identifiants et mot de passe

        identifiant_text = tk.Label(self, text="Identifiant", background=self.set_color("lightblue"),
                                    foreground=self.set_color("pink"), font=('Roboto', 14))
        identifiant_text.place(x=432, y=60)

        self.identifiant_entry = tk.Entry(self, background=self.set_color("entrycolor"), fg=self.set_color('entrytext'),
                                          insertbackground=self.set_color('insert'), font=('Roboto', 12, 'bold'), bd=0)
        self.identifiant_entry.place(x=435, y=90, width=204, height=29)

        motdepasse_text = tk.Label(self, text="Mot de passe", background=self.set_color("lightblue"),
                                   foreground=self.set_color("pink"), font=('Roboto', 14))
        motdepasse_text.place(x=432, y=130)

        self.motdepasse_entry = tk.Entry(self, background=self.set_color("entrycolor"), font=('Roboto', 12, 'bold'),
                                         fg=self.set_color('entrytext'), bd=0, show='*',
                                         insertbackground=self.set_color('insert'))
        self.motdepasse_entry.place(x=435, y=160, width=204, height=29)

        # Bouton de connexion / Création de compte

        connexion_button = tk.Button(self, text="Connexion", background=self.set_color('entrycolor'),
                                     foreground=self.set_color('entrytext'), activebackground=self.set_color('entrycolor'),
                                     cursor='hand2', font=('Roboto', 13), bd=0, command=self.connect)
        connexion_button.place(x=472, y=210, width=126, height=30)

        inscription_button = tk.Button(self, text="Créez mon compte", background=self.set_color("lightblue"),
                                       foreground=self.set_color("pink"), activebackground=self.set_color("lightblue"),
                                       activeforeground=self.set_color("buttonactive"), font=('Roboto', 10, 'bold'), bd=0,
                                       command=lambda: self.window.switch_frame('InscriptionFrame'), cursor='hand2')
        inscription_button.place(x=474, y=245, width=122, height=30)

        # Rapid connection

        rapid_connect_text = tk.Label(self, text="Reconnecte-toi rapidement...", background=self.set_color("lightblue"),
                                      foreground=self.set_color("pink"), font=('Roboto', 11, 'bold'))
        rapid_connect_text.place(x=20, y=245)

        # One
        profile_img_one = tk.PhotoImage(file=select_image_user(get_recent_user(0))).subsample(11)
        profile_one = tk.Button(self, image=profile_img_one, background=self.set_color('lightblue'), cursor='hand2', bd=0,
                                activebackground=self.set_color('lightblue'), command=lambda: self.fill_entry(0))
        profile_one.photo = profile_img_one
        profile_one.place(x=21, y=280)

        profile_one_text = tk.Label(self, text=get_recent_user(0), background=self.set_color("lightblue"),
                                    foreground=self.set_color('white'), font=('Roboto', 9))

        if len(get_recent_user(0)) == 3:
            profile_one_text.place(x=30, y=330)
        elif 3 < len(get_recent_user(0)) < 5:
            profile_one_text.place(x=27, y=330)
        elif 5 <= len(get_recent_user(0)) < 6:
            profile_one_text.place(x=27, y=330)
        elif 6 <= len(get_recent_user(0)) < 7:
            profile_one_text.place(x=26, y=330)
        elif len(get_recent_user(0)) == 7:
            profile_one_text.place(x=23, y=330)

        # Two
        profile_img_two = tk.PhotoImage(file=select_image_user(get_recent_user(1))).subsample(11)
        profile_two = tk.Button(self, image=profile_img_two, background=self.set_color('lightblue'), cursor='hand2', bd=0,
                                activebackground=self.set_color('lightblue'), command=lambda: self.fill_entry(1))
        profile_two.photo = profile_img_two
        profile_two.place(x=106, y=280)

        profile_two_text = tk.Label(self, text=get_recent_user(1), background=self.set_color("lightblue"),
                                    foreground=self.set_color('white'), font=('Roboto', 9))

        if len(get_recent_user(1)) == 3:
            profile_two_text.place(x=117, y=330)
        elif 3 < len(get_recent_user(1)) < 5:
            profile_two_text.place(x=115, y=330)
        elif 5 <= len(get_recent_user(1)) < 6:
            profile_two_text.place(x=113, y=330)
        elif 6 <= len(get_recent_user(1)) < 7:
            profile_two_text.place(x=110, y=330)
        elif len(get_recent_user(1)) == 7:
            profile_two_text.place(x=108, y=330)

        # Three
        profile_img_three = tk.PhotoImage(file=select_image_user(get_recent_user(2))).subsample(11)
        profile_three = tk.Button(self, image=profile_img_three, background=self.set_color('lightblue'), cursor='hand2',
                                  activebackground=self.set_color('lightblue'), command=lambda: self.fill_entry(2), bd=0)
        profile_three.photo = profile_img_three
        profile_three.place(x=191, y=280)

        profile_three_text = tk.Label(self, text=get_recent_user(2), background=self.set_color('lightblue'),
                                      foreground=self.set_color('white'), font=('Roboto', 9))

        if len(get_recent_user(2)) == 3:
            profile_three_text.place(x=203, y=330)
        elif len(get_recent_user(2)) < 5:
            profile_three_text.place(x=200, y=330)
        elif len(get_recent_user(2)) < 6:
            profile_three_text.place(x=198, y=330)
        elif len(get_recent_user(2)) < 7:
            profile_three_text.place(x=196, y=330)
        elif len(get_recent_user(2)) == 7:
            profile_three_text.place(x=193, y=330)

        # Copyright

        copyright_text = tk.Label(self, text="© 2022 GestMoney", background=self.set_color('lightblue'),
                                  foreground=self.set_color("white"), font=('Roboto', 10))
        copyright_text.place(x=275, y=335)

        # Affichage erreurs
        self.error_canvas = tk.Canvas(self, height=40, width=431, background=self.set_color('lightblue'),
                                      highlightthickness=0)

    def show_error(self, text):
        self.error_canvas.destroy()
        self.error_canvas = tk.Canvas(self, height=60, width=300, background=self.set_color("lightblue"),
                                      highlightthickness=0)
        self.error_canvas.create_text(130, 40, text=text, font=('Roboto', 11), fill='red')

        self.error_canvas.place(x=400, y=0)

    def connect(self):
        entry_id = self.identifiant_entry.get()
        mdp = self.motdepasse_entry.get()

        with open(r'..\..\data\users.json', 'r') as f:
            users = json.load(f)

        for user in users.values():
            if user['id'] == entry_id and user['mdp'] == mdp:
                self.window.user_email = user['email']
                self.window.user_id = user['id']
                add_user_in_activity_recent(user['id'])
                self.window.switch_frame('BasePage')
                return

        if entry_id not in [user['id'] for user in users.values()]:
            self.show_error("Identifiant incorrect")

        else:
            self.show_error("Mot de passe incorrect")

    def fill_entry(self, index):
        self.identifiant_entry.delete(0, 10000000)
        self.identifiant_entry.insert(0, get_recent_user(index))
        self.motdepasse_entry.focus_set()

    def set_color(self, color):
        return set_color(self.window.color_theme, color)