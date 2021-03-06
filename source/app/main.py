import tkinter as tk
from datetime import datetime

from dateutil.relativedelta import relativedelta

from data.data import get_transactions, add_transaction, change_money, get_regu_transacs
from source.app.BasePage.regudebit import ReguDebit
from source.app.BasePage.regucredit import ReguCredit
from source.app.OnConnexion.connexion import ConnectionFrame
from source.app.Sys import select_image, set_color, center, set_appwindow
from source.app.InscriptionPage.inscription import InscriptionFrame
from source.app.BasePage.baseframe import BaseFrame
from source.app.BasePage.creditframe import CreditFrame
from source.app.BasePage.homeframe import HomeFrame
from source.app.BasePage.debitframe import DebitFrame


class Main(tk.Tk):
    def __init__(self, window):
        tk.Tk.__init__(self, window)
        self.window = window

        self.geometry("679x406")
        self.color_theme = 'basic'
        self.config(background=self.set_color('bg'))
        self.title('GestMoney')
        self.iconbitmap(select_image('icon.ico'))
        center(self)
        self.wm_overrideredirect(True)
        self.x, self.y = None, None
        self.title_frame = None
        self.user_email = None
        self.user_id = None
        self.main_frame = tk.Frame()

        # Titlebar
        self.widget_title_bar()

        # Permet de voir l'icon dans notre barre des taches
        self.after(10, lambda: set_appwindow(self))

        # Permet d'afficher notre première fenêtre (Base Page)

        self.active_frame = ConnectionFrame(self)
        self.active_frame.pack()

    def switch_frame(self, frame_name):

        if frame_name == 'InscriptionFrame':
            self.title_frame.destroy(), self.active_frame.destroy()
            self.geometry('431x473')
            self.active_frame = InscriptionFrame(self)
            self.active_frame.pack()
            center(self)

        elif frame_name == 'BasePage':
            self.title_frame.destroy(), self.active_frame.destroy(), self.main_frame.destroy()
            self.geometry('1280x720')
            self.main_frame = BaseFrame(self)
            self.main_frame.pack()
            self.switch_frame('HomePage')
            center(self)

        elif frame_name == 'HomePage':
            self.active_frame.destroy()
            self.active_frame = HomeFrame(self)
            self.active_frame.place(x=0, y=80)

        elif frame_name == 'DebitPage':
            self.active_frame.destroy()
            self.active_frame = DebitFrame(self)
            self.active_frame.place(x=0, y=80)

        elif frame_name == 'CreditPage':
            self.active_frame.destroy()
            self.active_frame = CreditFrame(self)
            self.active_frame.place(x=0, y=80)

        elif frame_name == 'ConnexionPage':
            self.title_frame.destroy(), self.active_frame.destroy(), self.main_frame.destroy()
            self.geometry("679x406")
            self.widget_title_bar()
            self.active_frame = ConnectionFrame(self)
            self.active_frame.pack()
            center(self)

        elif frame_name == 'DebitFrame':
            self.active_frame.destroy()
            self.active_frame = DebitFrame(self)
            self.active_frame.place(x=0, y=80)

        elif frame_name == 'ReguDebit':
            self.active_frame.destroy()
            self.active_frame = ReguDebit(self)
            self.active_frame.place(x=0, y=80)

        elif frame_name == 'ReguCredit':
            self.active_frame.destroy()
            self.active_frame = ReguCredit(self)
            self.active_frame.place(x=0, y=80)

    def widget_title_bar(self):
        self.title_frame = tk.Frame(self)
        title_bar = tk.Canvas(self.title_frame, width=679, height=47,
                              bg=self.set_color('darkbg'), highlightthickness=0)
        title_bar.create_text(135, 22, text="GestMoney", font=('Roboto', 20, 'bold'), fill=self.set_color('text'))
        title_bar.pack()

        imgs = tk.PhotoImage(file=select_image("icon.png")).subsample(11)
        icon = tk.Label(self.title_frame, image=imgs, background=self.set_color('darkbg'), bd=0,
                        foreground=self.set_color('bg'))
        icon.photo = imgs
        icon.place(x=5, y=0)

        image = tk.PhotoImage(file=select_image('exit_button.png')).subsample(6)
        quit_button = tk.Button(self, image=image, background=self.set_color('darkbg'), cursor='hand2',
                                bd=0, foreground=self.set_color('text'),
                                activebackground=self.set_color('darkbg'),
                                activeforeground=self.set_color('text'),
                                font=('Roboto', 20, 'bold'), command=exit)
        quit_button.photo = image
        quit_button.place(x=620, y=-1, width=50, height=50)
        self.title_frame.pack()

        self.apply_drag([title_bar, icon])

    def regu_transacs(self):
        for transac in get_regu_transacs(self.user_id):

            if transac['type'] == 'debit':
                transac['method'] = 'Paiement régulier'

            elif transac['type'] == 'credit':
                transac['method'] = 'Crédit régulier'

            old_transac = transac.copy()

            for i in range(12):
                transac = old_transac.copy()
                today = datetime.now()
                today = today.replace(hour=0, minute=0, second=0, microsecond=0)

                transac_date = today.replace(day=transac['date'], hour=0, minute=0, second=0, microsecond=0)
                transac_date -= relativedelta(months=i)

                if datetime.strptime(transac['creation_date'], '%d/%m/%y') <= transac_date <= today:
                    transac['date'] = datetime.strftime(transac_date, '%d/%m/%y')
                    transac['type'] = f"regu_{transac['type']}"
                    del transac['creation_date']

                    if transac not in get_transactions(self.user_id):
                        add_transaction(self.user_id, transac)

                        change_money(self.user_id, transac['amount'])

    def mouse_down(self, event):
        self.x, self.y = event.x, event.y

    def mouse_up(self, event):
        self.x, self.y = None, None

    def mouse_drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x0 = self.winfo_x() + deltax
        y0 = self.winfo_y() + deltay
        self.geometry(f"+{x0}+{y0}")

    def apply_drag(self, elements):
        for element in elements:
            element.bind('<ButtonPress-1>', self.mouse_down)
            element.bind('<B1-Motion>', self.mouse_drag)
            element.bind('<ButtonRelease-1>', self.mouse_up)

    def set_color(self, color):
        return set_color(self.color_theme, color)


if __name__ == "__main__":
    app = Main(None)
    app.mainloop()