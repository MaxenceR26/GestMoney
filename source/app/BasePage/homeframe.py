from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk

from data.data import get_transactions
from source.app.BasePage.baseframe import create_copyright
from source.app.Sys import set_color, select_image

"""
12 = Nombre de pages 

"""


class HomeFrame(tk.Frame):

    def __init__(self, window):
        self.cb_check = None
        self.cheq_check = None
        self.esp_check = None
        self.vir_check = None
        self.listing_of_checkbutton = None
        self.window = window
        super().__init__(window, width=1023, height=640, bg=self.set_color('fourthbg'))

        self.user_transacs = get_transactions(self.window.user_id)
        self.user_transacs = sorted(self.user_transacs,
                                    key=lambda x: datetime.strptime(x['date'], "%d/%m/%y").strftime("%y-%m-%d"))[::-1]

        self.treeview_transacs = self.user_transacs.copy()

        self.tab_page = 1
        self.page_var = tk.StringVar()
        self.page_var.set('1')
        self.tab_lines = []

        self.treeview_canvas = tk.Canvas(self, height=640, width=766, bg=self.set_color('fourthbg'),
                                         highlightthickness=0, bd=0)
        self.treeview_canvas.create_text(self.treeview_canvas.winfo_reqwidth() / 2, 40,
                                         text="Historique des transactions",
                                         font=('Roboto', 20, 'bold'), fill=self.set_color('text2'))

        self.title_treeview = tk.Canvas(self, width=690, height=20, bg=self.set_color("bg"), highlightthickness=0, bd=0)
        self.title_treeview.create_text(87, 10, text="Montant",
                                        font=('Roboto', 13, 'bold'), fill=self.set_color('text2'))

        self.title_treeview.create_text(170, 8, text=" | ",
                                        font=('Roboto', 13), fill=self.set_color('text2'))

        self.title_treeview.create_text(260, 10, text="Objet",
                                        font=('Roboto', 13, 'bold'), fill=self.set_color('text2'))

        self.title_treeview.create_text(353, 8, text=" | ",
                                        font=('Roboto', 13), fill=self.set_color('text2'))

        self.title_treeview.create_text(435, 10, text="Moyen de paiement",
                                        font=('Roboto', 13, 'bold'), fill=self.set_color('text2'))

        self.title_treeview.create_text(518, 8, text=" | ",
                                        font=('Roboto', 13), fill=self.set_color('text2'))

        self.title_treeview.create_text(608, 10, text="Date",
                                        font=('Roboto', 13, 'bold'), fill=self.set_color('text2'))

        self.title_treeview.place(x=292, y=75)

        # Création du style
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('Treeview',
                        background=self.set_color('tertiarybg'),
                        foreground=self.set_color('text2'),
                        highlightthickness=0, bd=0,
                        font=('Roboto', 9, 'bold'),
                        rowheight=40)

        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.map('Treeview', background=[('selected', '#172F6E')],
                  foreground=[('selected', self.set_color('text'))])

        self.treeview = ttk.Treeview(self.treeview_canvas, columns=('amount', 'object', 'method', 'date'))

        self.treeview.column("#1", width=174, anchor=tk.CENTER, stretch=tk.NO)
        self.treeview.column("#2", width=174, anchor=tk.CENTER, stretch=tk.NO)
        self.treeview.column("#3", width=174, anchor=tk.CENTER, stretch=tk.NO)
        self.treeview.column("#4", width=174, anchor=tk.CENTER, stretch=tk.NO)

        self.treeview['show'] = 'headings'

        self.set_page(self.tab_page)

        self.treeview.place(x=35, y=75, width=690, height=500)

        top = tk.Canvas(self, width=690, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
        top.place(x=292, y=74)

        bottom = tk.Canvas(self, width=690, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
        bottom.place(x=292, y=574)

        left = tk.Canvas(self, width=2, height=500, bg=self.set_color('darkbg'), highlightthickness=0)
        left.place(x=292, y=74)

        right = tk.Canvas(self, width=2, height=500, bg=self.set_color('darkbg'), highlightthickness=0)
        right.place(x=982, y=74)

        create_copyright(self, self.treeview_canvas)

        self.left_widgets()
        self.page_buttons()
        self.treeview_canvas.place(x=257, y=0)

    def left_widgets(self):
        canvas = tk.Canvas(self, width=257, height=645, bg=self.set_color("darkbg"), highlightthickness=0)
        canvas.create_line(1000, 0, -10, 0, fill="black")
        canvas.create_text(128.5, 30, text='Rechercher', font=('Roboto', 17), fill=self.set_color('text2'))
        canvas.create_text(20, 100, text='Date', font=('Roboto', 17), fill=self.set_color('text'), anchor='w')
        canvas.create_text(20, 175, text='Objet', font=('Roboto', 17), fill=self.set_color('text'), anchor='w')

        self.date_entry = tk.Entry(self, background=self.set_color('bg'), bd=0, font=('Roboto', 15, 'bold'),
                                   fg='#FFFFFF', insertbackground=self.set_color('entrytext'))
        self.date_entry.place(x=20, y=120, width=200, height=32)

        self.magasin_entry = tk.Entry(self, background=self.set_color('bg'), bd=0, font=('Roboto', 15, 'bold'),
                                      fg='#FFFFFF', insertbackground=self.set_color('entrytext'))
        self.magasin_entry.place(x=20, y=195, width=200, height=32)

        self.vir_check = tk.IntVar()
        self.esp_check = tk.IntVar()
        self.cheq_check = tk.IntVar()
        self.cb_check = tk.IntVar()

        self.vir_checkbutton = tk.Checkbutton(self, text='Virement', background=self.set_color('darkbg'),
                                              foreground=self.set_color('text'), font=('Roboto', 16),
                                              variable=self.vir_check, activeforeground=self.set_color('text'),
                                              highlightthickness=0, bd=0, activebackground=self.set_color('darkbg'),
                                              command=lambda: self.uncheck_buttons(0))
        self.vir_checkbutton.place(x=70, y=250)

        self.espece_checkbutton = tk.Checkbutton(self, text='Espèces', background=self.set_color('darkbg'),
                                                 foreground=self.set_color('text'), font=('Roboto', 16),
                                                 variable=self.esp_check, activeforeground=self.set_color('text'),
                                                 highlightthickness=0, bd=0, activebackground=self.set_color('darkbg'),
                                                 command=lambda: self.uncheck_buttons(1))
        self.espece_checkbutton.place(x=70, y=300)

        self.cheque_checkbutton = tk.Checkbutton(self, text='Chèques', background=self.set_color('darkbg'),
                                                 foreground=self.set_color('text'), font=('Roboto', 16),
                                                 variable=self.cheq_check, activeforeground=self.set_color('text'),
                                                 highlightthickness=0, bd=0, activebackground=self.set_color('darkbg'),
                                                 command=lambda: self.uncheck_buttons(2))
        self.cheque_checkbutton.place(x=70, y=350)

        self.cb_checkbutton = tk.Checkbutton(self, text='CB', background=self.set_color('darkbg'),
                                             foreground=self.set_color('text'), font=('Roboto', 16),
                                             variable=self.cb_check, activeforeground=self.set_color('text'),
                                             highlightthickness=0, bd=0, activebackground=self.set_color('darkbg'),
                                             command=lambda: self.uncheck_buttons(3))
        self.cb_checkbutton.place(x=70, y=400)

        self.listing_of_checkbutton = [self.vir_checkbutton, self.espece_checkbutton,
                                       self.cheque_checkbutton, self.cb_checkbutton]

        valid_button = tk.Button(self, text="Valider", foreground=self.set_color('text2'), font=('Roboto', 14),
                                 background=self.set_color('bg'), bd=0, activebackground=self.set_color('bg'),
                                 activeforeground=self.set_color('text2'),
                                 command=self.search)
        valid_button.place(x=50, y=450, width=150, height=32)

        reset_button = tk.Button(self, text="Réinitialiser", foreground=self.set_color('text2'), font=('Roboto', 14),
                                 background=self.set_color('bg'), bd=0, activebackground=self.set_color('bg'),
                                 activeforeground=self.set_color('text2'), command=lambda: self.reset())

        reset_button.place(x=50, y=500, width=150, height=32)

        canvas.place(x=0, y=0)

    def search(self):
        date = self.date_entry.get()
        objet = self.magasin_entry.get().lower()

        self.treeview_transacs = []

        pay_methods = []

        if self.vir_check.get() == 1:
            pay_methods.append('Virement')

        if self.esp_check.get() == 1:
            pay_methods.append('Espèces')

        if self.cheq_check.get() == 1:
            pay_methods.append('Chèque')

        if self.cb_check.get() == 1:
            pay_methods.append('Carte Bancaire')

        if not date and not objet and not pay_methods:
            error = tk.Label(self, text="Veuillez entrer un critère !\nOu choisir un mode de paiement",
                             bg=self.set_color('darkbg'), fg='red', font=('Roboto', 13), justify='center')
            error.place(x=40, y=45)

        elif date:
            self.treeview_transacs = [transac for transac in self.user_transacs if transac['date'] == date]

            if pay_methods:
                self.treeview_transacs = [transac for transac in self.treeview_transacs
                                          if transac['method'] in pay_methods]

            if objet:
                self.treeview_transacs = [transac for transac in self.treeview_transacs
                                          if objet in [transac['objet'].lower(), transac.get('market')]]

        elif objet:
            self.treeview_transacs = [transac for transac in self.user_transacs
                                      if objet in [transac['objet'].lower(), transac.get('market')]]

            if pay_methods:
                self.treeview_transacs = [transac for transac in self.treeview_transacs
                                          if transac['method'] in pay_methods]

        self.set_page(1)
        print(len(self.treeview_transacs))

    def uncheck_buttons(self, exception):
        for button in self.listing_of_checkbutton:
            if button != self.listing_of_checkbutton[exception]:
                button.deselect()

    def reset(self):
        self.treeview_transacs = self.user_transacs.copy()

        self.set_page(1)

    def set_color(self, color):
        return set_color(self.window.color_theme, color)

    def set_page(self, page):
        if not 0 < page < len(self.treeview_transacs) / 12 + 1:
            return

        self.tab_page = page
        self.page_var.set(str(page))

        page -= 1

        self.treeview.delete(*self.treeview.get_children())

        for line in self.tab_lines:
            line.destroy()

        for index in range(page*12, min((page + 1) * 12, len(self.treeview_transacs))):

            transac = self.treeview_transacs[index]

            if transac['type'] in ['credit', 'regu_credit', 'regu_debit']:
                self.treeview.insert(parent='', index='end', iid=index, text='Market',
                                     values=(f"{transac['amount']}€", transac['objet'],
                                             transac['method'], transac['date']))

            elif transac['type'] == 'debit':
                self.treeview.insert(parent='', index='end', iid=index, text='Market',
                                     values=(f"{transac['amount']}€", f"{transac['market']} / {transac['objet']}",
                                             transac['method'], transac['date']))

        self.tab_lines = []

        for i in range(min(len(self.treeview_transacs[page*12:]), 12)):
            line = tk.Canvas(self, width=690, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
            line.place(x=292, y=i * 40 + 94)
            self.tab_lines.append(line)

    def page_buttons(self):
        previous_image = tk.PhotoImage(file=select_image('page_précédente.png')).subsample(5)
        previous_button = tk.Button(self.treeview_canvas, image=previous_image, background=self.set_color("darkbg"),
                                    bd=0, cursor='hand2', activebackground=self.set_color("fourthbg"), relief='groove',
                                    command=lambda: self.set_page(self.tab_page - 1))
        previous_button.photo = previous_image
        previous_button.place(x=self.treeview_canvas.winfo_reqwidth() / 2 - 320, y=self.winfo_reqheight() - 55,
                              width=225, height=38)

        next_image = tk.PhotoImage(file=select_image('page_suivante.png')).subsample(5)
        next_button = tk.Button(self.treeview_canvas, image=next_image, background=self.set_color("darkbg"),
                                bd=0, cursor='hand2', activebackground=self.set_color("fourthbg"), relief='groove',
                                command=lambda: self.set_page(self.tab_page + 1))
        next_button.photo = next_image
        next_button.place(x=self.treeview_canvas.winfo_reqwidth() / 2 + 115, y=self.winfo_reqheight() - 55,
                          width=197, height=38)

        page_number = tk.Label(self.treeview_canvas, bg=self.set_color('fourthbg'), fg=self.set_color('text'),
                               textvariable=self.page_var, font=('Roboto', 16, 'bold'))

        page_number.place(x=self.treeview_canvas.winfo_reqwidth() / 2 - 20, y=self.winfo_reqheight() - 60,
                          width=40, height=40)