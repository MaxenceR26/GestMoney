import tkinter as tk
from datetime import datetime


from data.data import select_image_user, return_money
from source.app.BasePage.parameter import ParametreWindow
from source.app.Sys import set_color, select_image


def create_buttons(frame, valid_function):
    valid_button = tk.Button(frame, text="Valider", background=set_color("lightblue"), cursor='hand2',
                             foreground=set_color("pink"), font=('Roboto', 18, 'bold'), relief="groove",
                             activebackground=set_color("lightblue"), activeforeground=set_color("pink"),
                             command=valid_function)
    valid_button.place(x=100, y=440, width=211, height=84)

    annuler_button = tk.Button(frame, command=lambda: frame.window.switch_frame('HomePage'), activeforeground='red',
                               font=('Roboto', 18, 'bold'), foreground='red', activebackground=set_color('lightblue'),
                               background=set_color('lightblue'), relief='groove', cursor='hand2', text='Annuler')
    annuler_button.place(x=550, y=440, width=211, height=84)


def date_valid(date):
    try:
        datetime.strptime(date, '%d/%m/%y')
        return True

    except ValueError:
        return False


class BaseFrame(tk.Frame):

    def __init__(self, window):
        super().__init__(window, bg=set_color('basic', 'lightblue'))
        self.window = window

        # Affichage de la titlebar
        self.title_bar()

        self.right_widgets()

    def right_widgets(self):
        canvas = tk.Canvas(self, width=257, height=645, bg=set_color('basic', "entrycolor"), highlightthickness=0)
        canvas.create_line(1000, 0, -10, 0, fill="black")
        canvas.create_line(210, 120, 40, 120, fill=set_color('basic', "buttonactive"), width=2)

        canvas.create_text(128.5, 50, text="Argent", font=('Roboto', 20, 'bold'), fill='white')
        canvas.create_text(128.5, 90, text=f"{return_money(self.window.user_id)}€", font=('Roboto', 14), fill='white')
        canvas.pack(side=tk.RIGHT)

        accueil_button = tk.Button(self, text="Accueil", font=('Roboto', 14), fg='white', bd=0,
                                  activeforeground='white', activebackground=set_color('basic', "onactivebutton"), cursor='hand2',
                                  bg=set_color('basic', "buttonactive"), command=lambda: self.window.switch_frame('basic', 'HomePage'))
        accueil_button.place(x=1048, y=220, width=201, height=33)

        credit_button = tk.Button(self, text="Créditer l'argent", font=('Roboto', 14), fg='white', bd=0,
                                  activeforeground='white', activebackground=set_color('basic', "onactivebutton"), cursor='hand2',
                                  bg=set_color('basic', "buttonactive"), command=lambda: self.window.switch_frame('CreditPage'))
        credit_button.place(x=1048, y=270, width=201, height=33)

        debit_button = tk.Button(self, text="Débiter de l'argent", font=('Roboto', 14), fg='white', cursor='hand2',
                                 bg=set_color('basic', "buttonactive"), bd=0, activebackground=set_color('basic', "onactivebutton"),
                                 activeforeground='white', command=lambda: self.window.switch_frame('DebitFrame'))
        debit_button.place(x=1048, y=320, width=201, height=33)

        deco_button = tk.Button(self, text="Déconnexion", font=('Roboto', 14), fg='white', activeforeground='white',
                                bg=set_color('basic', "buttonactive"), bd=0, activebackground=set_color('basic', "onactivebutton"),
                                command=lambda: self.window.switch_frame('basic', 'ConnexionPage', True), cursor='hand2')
        deco_button.place(x=1048, y=635, width=206, height=49)



    def title_bar(self):
        title_bar = tk.Canvas(self, width=1700, height=80, bg=set_color('basic', 'entrycolor'), highlightthickness=0)
        title_bar.create_text(200, 40, text="GestMoney", font=('Roboto', 30, 'bold'), fill=set_color('basic', "white"))
        title_bar.pack()

        imgs = tk.PhotoImage(file=select_image("icon.png")).subsample(7)
        icon = tk.Label(self, image=imgs, background=set_color('basic', "entrycolor"), bd=0,
                        foreground=set_color('basic', "lightblue"))
        icon.photo = imgs
        icon.place(x=5, y=5)


        image = tk.PhotoImage(file=select_image('exit_button.png')).subsample(5)
        quit_button = tk.Button(self, image=image, background=set_color('basic', "entrycolor"), cursor='hand2',
                                bd=0, foreground=set_color('basic', "pink"),
                                activebackground=set_color('basic', "entrycolor"), activeforeground=set_color('basic', "pink"),
                                font=('Roboto', 20, 'bold'), command=exit)
        quit_button.photo = image
        quit_button.place(x=1190, y=10, width=60, height=60)

        profile_img = tk.PhotoImage(file=select_image_user(self.window.user_id)).subsample(9)
        profile_btn = tk.Button(self, image=profile_img, background=set_color('basic', 'entrycolor'), cursor='hand2', bd=0,
                                activebackground=set_color('basic', 'entrycolor'), command=lambda: ParametreWindow(self.window).update())
        profile_btn.photo = profile_img
        profile_btn.place(x=1110, y=10)

        self.window.apply_drag([title_bar, icon])