import tkinter as tk

from data.data import add_user_in_activity_recent, get_all_users, dump_users
from source.app.Sys import set_color, select_image


class InscriptionFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=431, height=473)

        self.ROBOTO_14 = ('Roboto', 14, 'bold')

        self.window = window

        # Config Window
        self.config(background=set_color("lightblue"))

        self.x, self.y = None, None

        # Design

        self.title_bar()

        # Les entrées et leurs noms
        self.inputs_canvas = tk.Canvas(self, height=421, width=431, background=set_color("lightblue"),
                                       highlightthickness=0)
        self.inputs_name()
        self.inputs_entry()

        # Affichage erreurs
        self.error_canvas = tk.Canvas(self, height=40, width=431, background=set_color("lightblue"),
                                      highlightthickness=0)

        # Bouton valider
        validate = tk.Button(self.inputs_canvas, text='Inscription', bg=set_color('entrycolor'), fg=set_color('white'),
                             activebackground=set_color('entrycolor'), activeforeground=set_color('white'),
                             font=('Roboto', 12), relief='flat', cursor='hand2', bd=0, command=self.create_account)
        validate.place(x=142, y=345, width=150, height=40)

        self.inputs_canvas.place(x=0, y=52)

        # Copyright
        copyright_text = tk.Label(self, text="© 2022 GestMoney", background=set_color("lightblue"),
                                  foreground=set_color("white"), font=('Roboto', 10))
        copyright_text.place(x=155, y=450)

    def inputs_name(self):
        names = ['Identifiant', 'E-mail', 'Mot de passe', 'Confirmation mot de passe', 'Montant actuel']

        for i in range(5):
            self.inputs_canvas.create_text(114, (i * 59) + 50, text=names[i], font=('Roboto', 13),
                                           fill=set_color("pink"), anchor='w')

    def inputs_entry(self):
        self.user_id = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                                font=('Roboto', 12, 'bold'), fg='white')
        self.user_id.place(x=114, y=60, height=29, width=204)

        self.email = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                              font=('Roboto', 12, 'bold'), fg='white')
        self.email.place(x=114, y=119, height=29, width=204)

        self.mdp = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                            font=('Roboto', 12, 'bold'), fg='white', show='*')
        self.mdp.place(x=114, y=178, height=29, width=204)

        self.mdp_confirm = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                                    font=('Roboto', 12, 'bold'), fg='white', show='*')
        self.mdp_confirm.place(x=114, y=237, height=29, width=204)

        self.money = tk.Entry(self.inputs_canvas, bd=0, bg=set_color('entrycolor'),
                              font=('Roboto', 12, 'bold'), fg='white')
        self.money.place(x=114, y=296, height=29, width=204)

    def title_bar(self):
        title_bar = tk.Canvas(self, height=52, width=431, background=set_color("entrycolor"),
                              highlightthickness=0)
        title_bar.create_text(205, 25, text="GestMoney", font=('Roboto', 20, 'bold'), fill=set_color("white"))
        title_bar.place(x=0, y=0)

        logo = tk.PhotoImage(file=select_image("icon.png")).subsample(11)
        icon = tk.Label(title_bar, image=logo, background=set_color("entrycolor"), bd=0,
                        foreground=set_color("lightblue"))
        icon.photo = logo
        icon.place(x=5, y=5)

        quit_button = tk.Button(title_bar, text="X", background=set_color("entrycolor"), cursor='hand2',
                                relief='groove', foreground=set_color("pink"),
                                activebackground=set_color("lightblue"), activeforeground=set_color("pink"),
                                font=self.ROBOTO_14, command=self.window.destroy)
        quit_button.place(x=385, y=5, height=40, width=40)

        self.window.apply_drag([title_bar, icon])

    def show_error(self, text):
        self.error_canvas.destroy()
        self.error_canvas = tk.Canvas(self, height=40, width=431, background=set_color("lightblue"),
                                      highlightthickness=0)
        self.error_canvas.create_text(215, 20, text=text, font=('Roboto', 12), fill='red')

        self.error_canvas.place(x=0, y=52)

    def create_account(self):
        identifiant = self.user_id.get()
        email = self.email.get()
        mdp = self.mdp.get()
        mdp_confirm = self.mdp_confirm.get()
        money = self.money.get()
        image = "ressource\\img\\profile-base.png"

        user = {
            'id': identifiant,
            'email': email,
            'mdp': mdp,
            'money': money,
            'image': image
        }

        users = get_all_users()

        if '' in user.values():
            self.show_error('Veuillez remplir toutes les cases')

        elif not identifiant.isalpha():
            self.show_error("L'identifiant ne doit contenir que des lettres")

        elif identifiant in users:
            self.show_error('Cet identifiant est déjà utilisé')

        elif '@' not in email and '.' not in email:
            self.show_error('E-mail invalide')

        elif not 6 <= len(mdp) <= 20:
            self.show_error('Le mot de passe doit faire entre 6 et 20 aractères')

        elif mdp != mdp_confirm:
            self.show_error('Confirmation du mot de passe invalide')

        elif not money.isdigit():
            self.show_error('Montant actuel invalide')

        else:
            user['money'] = int(user['money'])
            users[identifiant] = user
            dump_users(users)

            self.window.user_email = user['email']
            add_user_in_activity_recent(user['id'])
            self.window.switch_frame('ConnexionPage', False)