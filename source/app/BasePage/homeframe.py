from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk

from data.data import get_transactions
from source.app.BasePage.baseframe import create_copyright
from source.app.Sys import set_color

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
        self.tab_page = 0
        self.tab_lines = []

        self.history_canvas = tk.Canvas(self, height=640, width=766, bg=self.set_color('fourthbg'),
                                        highlightthickness=0, bd=0)
        self.history_canvas.create_text(self.history_canvas.winfo_reqwidth() / 2, 40,
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

        self.tableau = ttk.Treeview(self.history_canvas, columns=('amount', 'object', 'method', 'date'))

        self.tableau.column("#1", width=174, anchor=tk.CENTER, stretch=tk.NO)
        self.tableau.column("#2", width=174, anchor=tk.CENTER, stretch=tk.NO)
        self.tableau.column("#3", width=174, anchor=tk.CENTER, stretch=tk.NO)
        self.tableau.column("#4", width=174, anchor=tk.CENTER, stretch=tk.NO)

        self.tableau.heading('amount', text='Montant')
        self.tableau.heading('object', text='Objet')
        self.tableau.heading('method', text='Moyen de paiement')
        self.tableau.heading('date', text='Date')
        self.tableau['show'] = 'headings'

        self.set_page(self.tab_page)

        self.tableau.place(x=35, y=75, width=690, height=500)

        top = tk.Canvas(self, width=690, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
        top.place(x=292, y=74)

        bottom = tk.Canvas(self, width=690, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
        bottom.place(x=292, y=574)

        left = tk.Canvas(self, width=2, height=500, bg=self.set_color('darkbg'), highlightthickness=0)
        left.place(x=292, y=74)

        right = tk.Canvas(self, width=2, height=500, bg=self.set_color('darkbg'), highlightthickness=0)
        right.place(x=982, y=74)

        create_copyright(self, self.history_canvas)

        self.left_widgets()
        self.history_canvas.place(x=257, y=0)

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
                                              variable=self.vir_check,
                                              highlightthickness=0, bd=0, activebackground=self.set_color('darkbg'),
                                              activeforeground=self.set_color('text'))
        self.vir_checkbutton.place(x=70, y=250)

        self.espece_checkbutton = tk.Checkbutton(self, text='Espèces', background=self.set_color('darkbg'),
                                                 foreground=self.set_color('text'), font=('Roboto', 16),
                                                 variable=self.esp_check,
                                                 highlightthickness=0, bd=0, activebackground=self.set_color('darkbg'),
                                                 activeforeground=self.set_color('text'))
        self.espece_checkbutton.place(x=70, y=300)

        self.cheque_checkbutton = tk.Checkbutton(self, text='Chèques', background=self.set_color('darkbg'),
                                                 foreground=self.set_color('text'), font=('Roboto', 16),
                                                 variable=self.cheq_check,
                                                 highlightthickness=0, bd=0, activebackground=self.set_color('darkbg'),
                                                 activeforeground=self.set_color('text'))
        self.cheque_checkbutton.place(x=70, y=350)

        self.cb_checkbutton = tk.Checkbutton(self, text='CB', background=self.set_color('darkbg'),
                                             foreground=self.set_color('text'), font=('Roboto', 16),
                                             variable=self.cb_check,
                                             highlightthickness=0, bd=0, activebackground=self.set_color('darkbg'),
                                             activeforeground=self.set_color('text'))
        self.cb_checkbutton.place(x=70, y=400)

        self.listing_of_checkbutton = [self.vir_checkbutton, self.cb_checkbutton, self.espece_checkbutton,
                                       self.cheque_checkbutton]

        valid_button = tk.Button(self, text="Valider", foreground=self.set_color('text2'), font=('Roboto', 14),
                                 background=self.set_color('bg'), bd=0, activebackground=self.set_color('bg'),
                                 activeforeground=self.set_color('text2'),
                                 command=self.search)
        valid_button.place(x=50, y=450, width=150, height=32)

        reset_button = tk.Button(self, text="Réinitialiser", foreground=self.set_color('text2'), font=('Roboto', 14),
                                 background=self.set_color('bg'), bd=0, activebackground=self.set_color('bg'),
                                 activeforeground=self.set_color('text2'), command=lambda: self.set_page(2))

        reset_button.place(x=50, y=500, width=150, height=32)

        canvas.place(x=0, y=0)

    def search(self):
        query = self.date_entry.get()
        objet = self.magasin_entry.get()
        selections = []

        if self.vir_check.get() == 1:
            selections.extend(
                child[-1]
                for child in self.tableau.get_children()
                if self.vir_checkbutton in self.tableau.item(child)['values']
            )

        elif not query and not objet:
            print("Entre un texte")

        elif query and objet:
            selections.extend(
                child[-1]
                for child in self.tableau.get_children()
                if objet.lower()
                and query.lower() in self.tableau.item(child)['values']
            )
        elif query:
            selections.extend(
                child[-1]
                for child in self.tableau.get_children()
                if query.lower() in self.tableau.item(child)['values']
            )

        else:
            for child in self.tableau.get_children():
                if objet in self.tableau.item(child)['values']:
                    selections.append(child[-1])
                else:
                    print("no")

            print(selections)

        # child_id = self.tableau.get_children()[-1]
        # print(child_id[-1])
        # print(selections)
        # self.tableau.focus_get()
        self.tableau.selection_set(selections)

    def set_color(self, color):
        return set_color(self.window.color_theme, color)

    def set_page(self, page):
        page -= 1

        self.tableau.delete(*self.tableau.get_children())

        for line in self.tab_lines:
            line.destroy()

        for index in range(page*12, min((page + 1) * 12, len(self.user_transacs))):

            transac = self.user_transacs[index]

            if transac['type'] in ['credit', 'regu_credit']:
                self.tableau.insert(parent='', index='end', iid=index, text='Market',
                                    values=(f"{transac['amount']}€", transac['origin'],
                                            transac['method'], transac['date']))

            elif transac['type'] == 'debit':
                self.tableau.insert(parent='', index='end', iid=index, text='Market',
                                    values=(f"{transac['amount']}€", f"{transac['market']} / {transac['buy_type']}",
                                            transac['method'], transac['date']))

            elif transac['type'] == 'regu_debit':
                self.tableau.insert(parent='', index='end', iid=index, text='Market',
                                    values=(f"{transac['amount']}€", transac['buy_type'],
                                            transac['method'], transac['date']))

        self.tab_lines = []

        for i in range(min(len(self.user_transacs[page*12:]), 12)):
            line = tk.Canvas(self, width=690, height=2, bg=self.set_color('darkbg'), highlightthickness=0)
            line.place(x=292, y=i * 40 + 94)
            self.tab_lines.append(line)