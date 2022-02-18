import tkinter as tk
from Sys import set_color


class MainWindow(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window, width=700, height=500, bg=set_color("lightgreen"))
        self.window = window
        self._frame = None

        # Design de la page de base quand on lance l'application

        welcometext = tk.Label(self, text="""
        
Bienvenue sur GestMoney

Tu cherches à gérer tes comptes
mais tu n’y arrive pas ?

Alors GestMoney est la 
pour t’aider !
        
        """, background=set_color("lightgreen"), foreground=set_color("gray"), font=('Roboto', 16))
        welcometext.place(x=30, y=10)

        # Gestion de demande identifiants et mot de passe

        identifiant_text = tk.Label(self, text="Identifiant", background=set_color("lightgreen"),
                                    foreground=set_color("buttontext"), font=('Roboto', 14))
        identifiant_text.place(x=450, y=60)

        identifiant_entry = tk.Entry(self, background=set_color("entrycolor"), foreground='#000000', bd=0)
        identifiant_entry.place(x=435, y=90, width=204, height=29)

        motdepasse_text = tk.Label(self, text="Mot de passe", background=set_color("lightgreen"),
                                   foreground=set_color("buttontext"), font=('Roboto', 14))
        motdepasse_text.place(x=450, y=130)

        motdepasse_entry = tk.Entry(self, background=set_color("entrycolor"), foreground='#000000', bd=0)
        motdepasse_entry.place(x=435, y=160, width=204, height=29)

        # Bouton de connexion / Création de compte

        connexion_button = tk.Button(self, text="Connexion", background=set_color("darkgreen"), foreground="#fff",
                                     activebackground=set_color("buttonactive"),activeforeground="#fff", font=('Roboto', 13), bd=0)
        connexion_button.place(x=472, y=210, width=126, height=30)

        inscription_button = tk.Button(self, text="Créez mon compte", background=set_color("lightgreen"), foreground=set_color("buttontext"),
                                     activebackground=set_color("lightgreen"), activeforeground=set_color("buttonactive"),
                                     font=('Roboto', 10, 'bold'), bd=0)
        inscription_button.place(x=474, y=245, width=122, height=30)

        # Copyright

        copyright_text = tk.Label(self, text="© 2022 GestMoney", background=set_color("lightgreen"),
                                    foreground=set_color("gray"), font=('Roboto', 13))
        copyright_text.place(x=250, y=325)
