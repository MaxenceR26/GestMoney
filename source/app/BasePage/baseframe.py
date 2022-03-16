import tkinter as tk
from datetime import datetime

from data.data import select_image_user, return_money
from source.app.BasePage.parameter import ParametreWindow
from source.app.Sys import set_color, select_image


def create_buttons(frame, valid_function):
    valid_button = tk.Button(frame, text="Valider", background=frame.set_color('bg'), cursor='hand2',
                             foreground=frame.set_color('text'), font=('Roboto', 18, 'bold'), relief="groove",
                             activebackground=frame.set_color('bg'), activeforeground=frame.set_color('text'),
                             command=valid_function)
    valid_button.place(x=100, y=440, width=211, height=84)

    annuler_button = tk.Button(frame, command=lambda: frame.window.switch_frame('HomePage'),
                               font=('Roboto', 18, 'bold'), foreground=frame.set_color('error'),
                               activeforeground=frame.set_color('error'), activebackground=frame.set_color('bg'),
                               background=frame.set_color('bg'), relief='groove', cursor='hand2', text='Annuler')
    annuler_button.place(x=550, y=440, width=211, height=84)


def show_error(frame, text):
    frame.error_canvas.destroy()
    frame.error_canvas = tk.Canvas(frame, height=50, width=frame.window.winfo_width(),
                                   background=frame.set_color('bg'), highlightthickness=0)
    frame.error_canvas.create_text(frame.winfo_width() / 2, 25, text=text,
                                   font=('Roboto', 14), fill=frame.set_color('error'))

    frame.error_canvas.place(x=0, y=80)


def date_valid(date):
    try:
        datetime.strptime(date, '%d/%m/%y')
        return True

    except ValueError:
        return False


class BaseFrame(tk.Frame):

    def __init__(self, window):
        self.window = window
        super().__init__(window, bg=self.set_color('fourthbg'))

        # Affichage de la titlebar
        self.title_bar()

        self.right_widgets()

    def right_widgets(self):
        canvas = tk.Canvas(self, width=257, height=645, bg=self.set_color("darkbg"), highlightthickness=0)
        canvas.create_line(1000, 0, -10, 0, fill="black")
        canvas.create_line(210, 120, 40, 120, fill=self.set_color("buttonactive"), width=2)

        canvas.create_text(128.5, 50, text="Argent", font=('Roboto', 20, 'bold'), fill=self.set_color('text2'))
        canvas.create_text(128.5, 90, text=f"{return_money(self.window.user_id)}€",
                           font=('Roboto', 14), fill=self.set_color('text2'))
        canvas.pack(side=tk.RIGHT)

        accueil_button = tk.Button(self, text="Accueil", font=('Roboto', 14), fg=self.set_color('text2'), bd=0,
                                   activeforeground=self.set_color('text2'),
                                   activebackground=self.set_color("onactivebutton"), cursor='hand2',
                                   bg=self.set_color("buttonactive"),
                                   command=lambda: self.window.switch_frame('HomePage'))
        accueil_button.place(x=1048, y=220, width=201, height=33)

        credit_button = tk.Button(self, text="Créditer l'argent", font=('Roboto', 14), fg=self.set_color('text2'), bd=0,
                                  activeforeground=self.set_color('text2'), bg=self.set_color("buttonactive"),
                                  activebackground=self.set_color("onactivebutton"), cursor='hand2',
                                  command=lambda: self.window.switch_frame('CreditPage'))
        credit_button.place(x=1048, y=270, width=201, height=33)

        debit_button = tk.Button(self, text="Débiter de l'argent", font=('Roboto', 14), fg=self.set_color('text2'),
                                 bg=self.set_color("buttonactive"), activebackground=self.set_color("onactivebutton"),
                                 bd=0, cursor='hand2', activeforeground=self.set_color('text2'),
                                 command=lambda: self.window.switch_frame('DebitFrame'))
        debit_button.place(x=1048, y=320, width=201, height=33)

        deco_button = tk.Button(self, text="Déconnexion", font=('Roboto', 14), fg=self.set_color('text2'),
                                bg=self.set_color("buttonactive"), bd=0, activeforeground=self.set_color('text2'),
                                activebackground=self.set_color("onactivebutton"), cursor='hand2',
                                command=lambda: self.window.switch_frame('ConnexionPage', True))
        deco_button.place(x=1048, y=635, width=206, height=49)

    def title_bar(self):
        title_bar = tk.Canvas(self, width=1700, height=80, bg=self.set_color('darkbg'), highlightthickness=0)
        title_bar.create_text(200, 40, text="GestMoney", font=('Roboto', 30, 'bold'), fill=self.set_color('text2'))
        title_bar.pack()

        imgs = tk.PhotoImage(file=select_image("icon.png")).subsample(7)
        icon = tk.Label(self, image=imgs, background=self.set_color("darkbg"), bd=0,
                        foreground=self.set_color('bg'))
        icon.photo = imgs
        icon.place(x=5, y=5)

        image = tk.PhotoImage(file=select_image('exit_button.png')).subsample(5)
        quit_button = tk.Button(self, image=image, background=self.set_color("darkbg"), cursor='hand2',
                                bd=0, foreground=self.set_color('text'),
                                activebackground=self.set_color("darkbg"), activeforeground=self.set_color('text'),
                                font=('Roboto', 20, 'bold'), command=exit)
        quit_button.photo = image
        quit_button.place(x=1190, y=10, width=60, height=60)

        profile_img = tk.PhotoImage(file=select_image_user(self.window.user_id)).subsample(9)
        profile_btn = tk.Button(self, image=profile_img, background=self.set_color('darkbg'), cursor='hand2', bd=0,
                                activebackground=self.set_color('darkbg'),
                                command=lambda: ParametreWindow(self.window).update())
        profile_btn.photo = profile_img
        profile_btn.place(x=1110, y=10)

        self.window.apply_drag([title_bar, icon])

    def set_color(self, color):
        return set_color(self.window.color_theme, color)
