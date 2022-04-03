import tkinter as tk

from data.data import add_user_in_activity_recent, get_all_users, dump_users, create_user
from source.app.Sys import set_color, select_image


class InscriptionFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, width=431, height=473)

        self.ROBOTO_14 = ('Roboto', 14, 'bold')

        self.window = window

        # Config Window
        self.config(background=self.set_color('bg'))

        self.x, self.y = None, None

        # Design

        self.title_bar()

        # Les entrées et leurs noms
        self.inputs_canvas = tk.Canvas(self, height=421, width=431, background=self.set_color('fourthbg'),
                                       highlightthickness=0)
        self.inputs_name()
        self.inputs_entry()

        # Affichage erreurs
        self.error_canvas = tk.Canvas(self, height=40, width=431, background=self.set_color('fourthbg'),
                                      highlightthickness=0)

        # Bouton valider
        validate = tk.Button(self.inputs_canvas, text='Inscription', bg=self.set_color('bg'), fg=self.set_color('text2'),
                             activebackground=self.set_color('bg'), activeforeground=self.set_color('text2'),
                             font=('Roboto', 12), relief='flat', cursor='hand2', bd=0, command=self.create_account)
        validate.place(x=142, y=345, width=150, height=40)

        self.inputs_canvas.place(x=0, y=52)

        # Copyright
        copyright_text = tk.Label(self, text="© 2022 GestMoney", background=self.set_color('fourthbg'),
                                  foreground=self.set_color("text2"), font=('Roboto', 10))
        copyright_text.place(x=155, y=450)

    def inputs_name(self):
        names = ['Identifiant', 'E-mail', 'Mot de passe', 'Confirmation mot de passe', 'Montant actuel']

        for i in range(5):
            self.inputs_canvas.create_text(114, (i * 59) + 50, text=names[i], font=('Roboto', 13),
                                           fill=self.set_color('text'), anchor='w')

    def inputs_entry(self):
        self.user_id = tk.Entry(self.inputs_canvas, bd=0, bg=self.set_color('bg'), font=('Roboto', 12, 'bold'),
                                fg=self.set_color('text2'), insertbackground=self.set_color('entrytext'))
        self.user_id.place(x=114, y=60, height=29, width=204)

        self.email = tk.Entry(self.inputs_canvas, bd=0, bg=self.set_color('bg'), font=('Roboto', 12, 'bold'),
                              fg=self.set_color('text2'), insertbackground=self.set_color('entrytext'))
        self.email.place(x=114, y=119, height=29, width=204)

        self.mdp = tk.Entry(self.inputs_canvas, bd=0, bg=self.set_color('bg'), fg=self.set_color('text2'),
                            font=('Roboto', 12, 'bold'), show='*', insertbackground=self.set_color('entrytext'))
        self.mdp.place(x=114, y=178, height=29, width=204)

        self.mdp_confirm = tk.Entry(self.inputs_canvas, bd=0, bg=self.set_color('bg'),
                                    fg=self.set_color('text2'), font=('Roboto', 12, 'bold'), show='*',
                                    insertbackground=self.set_color('entrytext'))
        self.mdp_confirm.place(x=114, y=237, height=29, width=204)

        self.money = tk.Entry(self.inputs_canvas, bd=0, bg=self.set_color('bg'), font=('Roboto', 12, 'bold'),
                              fg=self.set_color('text2'), insertbackground=self.set_color('entrytext'))
        self.money.place(x=114, y=296, height=29, width=204)

    def title_bar(self):
        title_bar = tk.Canvas(self, height=52, width=431, background=self.set_color("darkbg"),
                              highlightthickness=0)
        title_bar.create_text(205, 25, text="GestMoney", font=('Roboto', 20, 'bold'), fill=self.set_color("text"))
        title_bar.place(x=0, y=0)

        logo = tk.PhotoImage(file=select_image("icon.png")).subsample(11)
        icon = tk.Label(title_bar, image=logo, background=self.set_color("darkbg"), bd=0,
                        foreground=self.set_color('bg'))
        icon.photo = logo
        icon.place(x=5, y=5)

        image = tk.PhotoImage(file=select_image('exit_button.png')).subsample(6)
        quit_button = tk.Button(self, image=image, background=self.set_color('darkbg'), cursor='hand2',
                                bd=0, foreground=self.set_color('text'),
                                activebackground=self.set_color('darkbg'),
                                activeforeground=self.set_color('text'),
                                font=('Roboto', 20, 'bold'), command=exit)
        quit_button.photo = image
        quit_button.place(x=375, y=1, width=50, height=50)

        self.window.apply_drag([title_bar, icon])

    def show_error(self, text):
        self.error_canvas.destroy()
        self.error_canvas = tk.Canvas(self, height=40, width=431, background=self.set_color('bg'),
                                      highlightthickness=0)
        self.error_canvas.create_text(215, 20, text=text, font=('Roboto', 12), fill=self.set_color('error'))

        self.error_canvas.place(x=0, y=52)

    def create_account(self):
        identifiant = self.user_id.get()
        email = self.email.get()
        mdp = self.mdp.get()
        mdp_confirm = self.mdp_confirm.get()
        money = self.money.get()
        image = "source\\app\\ressource\\img\\profile-base.png"

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
            create_user(user['id'])

            self.window.user_email = user['email']
            add_user_in_activity_recent(user['id'])
            self.window.switch_frame('ConnexionPage')

    def set_color(self, color):
        return set_color(self.window.color_theme, color)