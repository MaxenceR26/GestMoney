import tkinter as tk
from datetime import datetime

from data.data import select_image_user, return_money

from source.app.Paramettre.main_parametre import ParametreWindow
from source.app.Sys import set_color, select_image


def create_buttons(frame, valid_function, x_1=150, x_2=600, width=256):
    valid_button = tk.Button(frame, text="Valider", background=frame.set_color('bg'), cursor='hand2',
                             foreground=frame.set_color('green'), font=('Roboto', 18), relief="groove",
                             activebackground=frame.set_color('bg'), activeforeground=frame.set_color('green'),
                             command=valid_function, bd=0)
    valid_button.place(x=x_1, y=530, width=width, height=48)

    annuler_button = tk.Button(frame, command=lambda: [
        frame.window.switch_frame('HomePage'),
        frame.window.main_frame.change_color_button(frame.window.main_frame.accueil_button)],
                               bd=0, font=('Roboto', 18, 'bold'), foreground=frame.set_color('error'),
                               activeforeground=frame.set_color('error'), activebackground=frame.set_color('bg'),
                               background=frame.set_color('bg'), relief='groove', cursor='hand2', text='Annuler')
    annuler_button.place(x=x_2, y=530, width=width, height=48)


def show_error(frame, text, width=None, y=95):
    width = frame.winfo_width() if width is None else width

    frame.error_canvas.destroy()
    frame.error_canvas = tk.Canvas(frame, height=26, width=width,
                                   background=frame.set_color('fourthbg'), highlightthickness=0)
    frame.error_canvas.create_text(frame.error_canvas.winfo_reqwidth()/2, 0, text=text,
                                   font=('Roboto', 14), fill=frame.set_color('error'), anchor='n')

    frame.error_canvas.place(x=0, y=y)


def create_copyright(frame, canvas):
    # Copyright
    canvas.create_text(canvas.winfo_reqwidth() / 2, canvas.winfo_reqheight() - 12,
                       text="© 2022 GestMoney", fill=frame.set_color('text2'), font=('Roboto', 10))


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

        self.accueil_button = tk.Button(self, text="Accueil", font=('Roboto', 14), fg=self.set_color('text2'), bd=0,
                                        activeforeground=self.set_color('text2'),
                                        activebackground=self.set_color("onactivebutton"), cursor='hand2',
                                        bg=self.set_color("buttonactive"),
                                        command=lambda: [self.window.switch_frame('HomePage'),
                                                         self.change_color_button(self.accueil_button)])
        self.accueil_button.place(x=1048, y=220, width=201, height=33)

        self.credit_button = tk.Button(self, text="Créditer de l'argent", font=('Roboto', 14), cursor='hand2', bd=0,
                                       activeforeground=self.set_color('text2'), bg=self.set_color("buttonactive"),
                                       activebackground=self.set_color("onactivebutton"), fg=self.set_color('text2'),
                                       command=lambda: [self.window.switch_frame('CreditPage'),
                                                        self.change_color_button(self.credit_button)])
        self.credit_button.place(x=1048, y=270, width=201, height=33)

        self.debit_button = tk.Button(self, text="Débiter de l'argent", font=('Roboto', 14), fg=self.set_color('text2'),
                                      bg=self.set_color("buttonactive"), activebackground=self.set_color("onactivebutton"),
                                      bd=0, cursor='hand2', activeforeground=self.set_color('text2'),
                                      command=lambda: [self.window.switch_frame('DebitFrame'),
                                                       self.change_color_button(self.debit_button)])
        self.debit_button.place(x=1048, y=320, width=201, height=33)

        self.debit_regulier = tk.Button(self, text="Dépense régulière", font=('Roboto', 14), fg=self.set_color('text2'),
                                        bg=self.set_color("buttonactive"),
                                        activebackground=self.set_color("onactivebutton"),
                                        bd=0, cursor='hand2', activeforeground=self.set_color('text2'),
                                        command=lambda: [self.window.switch_frame('ReguFrame'),
                                                         self.change_color_button(self.debit_regulier)])
        self.debit_regulier.place(x=1048, y=370, width=201, height=33)

        deco_button = tk.Button(self, text="Déconnexion", font=('Roboto', 14), fg=self.set_color('text2'),
                                bg=self.set_color("buttonactive"), bd=0, activeforeground=self.set_color('text2'),
                                activebackground=self.set_color("onactivebutton"), cursor='hand2',
                                command=lambda: self.window.switch_frame('ConnexionPage'))
        deco_button.place(x=1048, y=635, width=206, height=49)

        self.change_color_button(self.accueil_button)

    def title_bar(self):
        title_bar = tk.Canvas(self, width=1700, height=80, bg=self.set_color('darkbg'), highlightthickness=0)
        title_bar.create_text(200, 40, text="GestMoney", font=('Roboto', 30, 'bold'), fill=self.set_color('text'))
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
                                command=lambda: ParametreWindow(self.window.user_id, self.window.user_email).update())
        profile_btn.photo = profile_img
        profile_btn.place(x=1110, y=10)

        self.window.apply_drag([title_bar, icon])

    def set_color(self, color):
        return set_color(self.window.color_theme, color)

    def change_color_button(self, active_button):
        active_button.config(bg=self.set_color('fourthbg'))

        for button in [self.credit_button, self.accueil_button, self.debit_button, self.debit_regulier]:
            if button != active_button:
                button.config(bg=self.set_color('bg'))