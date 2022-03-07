import tkinter as tk
from source.app.OnConnexion.connexion import ConnectionFrame
from Sys import select_image, set_color, center, set_appwindow
from InscriptionPage.inscription import InscriptionFrame
from BasePage.baseframe import BaseFrame
from BasePage.creditframe import CreditFrame
from BasePage.homeframe import HomeFrame
from source.app.BasePage.debitframe import DebitFrame


class Shadow(tk.Tk):
    '''
    Add shadow to a widget

    This class adds a squared shadow to a widget. The size, the position, and
    the color of the shadow can be customized at wills. Different shadow
    behaviors can also be specified when hovering or clicking on the widget,
    with binding autonomously performed when initializing the shadow. If the
    widget has a 'command' function, it will be preserved when updating the
    shadow appearance.
    Note that enough space around the widget is required for the shadow to
    correctly appear. Moreover, other widgets nearer than shadow's size will be
    covered by the shadow.
    '''

    def __init__(self, widget, color='#212121', size=5, offset_x=0, offset_y=0,
                 onhover={}, onclick={}):
        '''
        Bind shadow to a widget.

        Parameters
        ----------
        widget : tkinter widget
            Widgets to which shadow should be binded.
        color : str, optional
            Shadow color in hex notation. The default is '#212121'.
        size : int or float, optional
            Size of the shadow. If int type, it is the size of the shadow out
            from the widget bounding box. If float type, it is a multiplier of
            the widget bounding box (e.g. if size=2. then shadow is double in
            size with respect to widget). The default is 5.
        offset_x : int, optional
            Offset by which shadow will be moved in the horizontal axis. If
            positive, shadow moves toward right direction. The default is 0.
        offset_y : int, optional
            Offset by which shadow will be moved in the vertical axis. If
            positive, shadow moves toward down direction. The default is 0.
        onhover : dict, optional
            Specify the behavior of the shadow when widget is hovered. Keys may
            be: 'size', 'color', 'offset_x', 'offset_y'. If a key-value pair is
            not provided, normal behavior is maintained for that key. The
            default is {}.
        onclick : dict, optional
            Specify the behavior of the shadow when widget is clicked. Keys may
            be: 'size', 'color', 'offset_x', 'offset_y'. If a key-value pair is
            not provided, normal behavior is maintained for that key. The
            default is {}.

        Returns
        -------
        None.

        '''
        # Save parameters
        self.widget = widget
        self.normal_size = size
        self.normal_color = color
        self.normal_x = int(offset_x)
        self.normal_y = int(offset_y)
        self.onhover_size = onhover.get('size', size)
        self.onhover_color = onhover.get('color', color)
        self.onhover_x = onhover.get('offset_x', offset_x)
        self.onhover_y = onhover.get('offset_y', offset_y)
        self.onclick_size = onclick.get('size', size)
        self.onclick_color = onclick.get('color', color)
        self.onclick_x = onclick.get('offset_x', offset_x)
        self.onclick_y = onclick.get('offset_y', offset_y)

        # Get master and master's background
        self.master = widget.master
        self.to_rgb = tuple([el // 257 for el in self.master.winfo_rgb(self.master.cget('bg'))])

        # Start with normal view
        self.__lines = []
        self.__normal()

        # Bind events to widget
        self.widget.bind("<Enter>", self.__onhover, add='+')
        self.widget.bind("<Leave>", self.__normal, add='+')
        self.widget.bind("<ButtonPress-1>", self.__onclick, add='+')
        self.widget.bind("<ButtonRelease-1>", self.__normal, add='+')

    def __normal(self, event=None):
        ''' Update shadow to normal state '''
        self.shadow_size = self.normal_size
        self.shadow_color = self.normal_color
        self.shadow_x = self.normal_x
        self.shadow_y = self.normal_y
        self.display()

    def __onhover(self, event=None):
        ''' Update shadow to hovering state '''
        self.shadow_size = self.onhover_size
        self.shadow_color = self.onhover_color
        self.shadow_x = self.onhover_x
        self.shadow_y = self.onhover_y
        self.display()

    def __onclick(self, event=None):
        ''' Update shadow to clicked state '''
        self.shadow_size = self.onclick_size
        self.shadow_color = self.onclick_color
        self.shadow_x = self.onclick_x
        self.shadow_y = self.onclick_y
        self.display()

    def __destroy_lines(self):
        ''' Destroy previous shadow lines '''
        for ll in self.__lines:
            ll.destroy()
        self.__lines = []

    def display(self):
        ''' Destroy shadow according to selected configuration '''

        def _rgb2hex(rgb):
            """
            Translates an rgb tuple of int to hex color
            """
            return "#%02x%02x%02x" % rgb

        def _hex2rgb(h):
            """
            Translates an hex color to rgb tuple of int
            """
            h = h.strip('#')
            return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

        # Destroy old lines
        self.__destroy_lines()

        # Get widget position and size
        self.master.update_idletasks()
        x0, y0, w, h = self.widget.winfo_x(), self.widget.winfo_y(), self.widget.winfo_width(), self.widget.winfo_height()
        x1 = x0 + w - 1
        y1 = y0 + h - 1

        # Get shadow size from borders
        if type(self.shadow_size) is int:
            wh_shadow_size = self.shadow_size
        else:
            wh_shadow_size = min([int(dim * (self.shadow_size - 1)) for dim in (w, h)])
        uldr_shadow_size = wh_shadow_size - self.shadow_y, wh_shadow_size - self.shadow_x, \
                           wh_shadow_size + self.shadow_y, wh_shadow_size + self.shadow_x
        uldr_shadow_size = {k: v for k, v in zip('uldr', uldr_shadow_size)}
        self.uldr_shadow_size = uldr_shadow_size

        # Prepare shadow color
        shadow_color = self.shadow_color
        if not shadow_color.startswith('#'):
            shadow_color = _rgb2hex(tuple([min(max(self.to_rgb) + 30, 255)] * 3))
        self.from_rgb = _hex2rgb(shadow_color)

        # Draw shadow lines
        max_size = max(uldr_shadow_size.values())
        diff_size = {k: max_size - ss for k, ss in uldr_shadow_size.items()}
        rs = np.linspace(self.from_rgb[0], self.to_rgb[0], max_size, dtype=int)
        gs = np.linspace(self.from_rgb[2], self.to_rgb[2], max_size, dtype=int)
        bs = np.linspace(self.from_rgb[1], self.to_rgb[1], max_size, dtype=int)
        rgbs = [_rgb2hex((r, g, b)) for r, g, b in zip(rs, gs, bs)]
        for direction, size in uldr_shadow_size.items():
            for ii, rgb in enumerate(rgbs):
                ff = tk.Frame(self.master, bg=rgb)
                self.__lines.append(ff)
                if direction == 'u' or direction == 'd':
                    diff_1 = diff_size['l']
                    diff_2 = diff_size['r']
                    yy = y0 - ii + 1 + diff_size[direction] if direction == 'u' else y1 + ii - diff_size[direction]
                    if diff_1 <= ii < diff_size[direction]:
                        ff1 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff1)
                        ff1.configure(width=ii + 1 - diff_1, height=1)
                        ff1.place(x=x0 - ii + 1 + diff_size['l'], y=yy)
                    if diff_2 <= ii < diff_size[direction]:
                        ff2 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff2)
                        ff2.configure(width=ii + 1 - diff_2, height=1)
                        ff2.place(x=x1, y=yy)
                    if ii >= diff_size[direction]:
                        ff.configure(width=x1 - x0 + ii * 2 - diff_size['l'] - diff_size['r'], height=1)
                        ff.place(x=x0 - ii + 1 + diff_size['l'], y=yy)
                elif direction == 'l' or direction == 'r':
                    diff_1 = diff_size['u']
                    diff_2 = diff_size['d']
                    xx = x0 - ii + 1 + diff_size[direction] if direction == 'l' else x1 + ii - diff_size[direction]
                    if diff_1 <= ii < diff_size[direction]:
                        ff1 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff1)
                        ff1.configure(width=1, height=ii + 1 - diff_1)
                        ff1.place(x=xx, y=y0 - ii + 1 + diff_size['u'])
                    if diff_2 <= ii < diff_size[direction]:
                        ff2 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff2)
                        ff2.configure(width=1, height=ii + 1 - diff_2)
                        ff2.place(x=xx, y=y1)
                    if ii >= diff_size[direction]:
                        ff.configure(width=1, height=y1 - y0 + ii * 2 - diff_size['u'] - diff_size['d'])
                        ff.place(x=xx, y=y0 - ii + 1 + diff_size['u'])


class Main(tk.Tk):
    def __init__(self, window):
        tk.Tk.__init__(self, window)
        self.window = window

        self.geometry("679x406")
        self.config(background=set_color("lightblue"))
        self.title('GestMoney')
        self.iconbitmap(select_image('icon.ico'))
        center(self)
        self.wm_overrideredirect(True)
        self.x, self.y = None, None
        self.title_frame = None
        self.user_email = None
        self.user_id = None
        self.main_frame = tk.Frame()
        self.active_frame = None

        # Titlebar
        self.widget_title_bar()

        # Permet de voir l'icon dans notre barre des taches
        self.after(10, lambda: set_appwindow(self))

        # Permet d'afficher notre première fenêtre ( Base Page )

        self.active_frame = ConnectionFrame(self)
        self.active_frame.pack()

    def switch_frame(self, frame_name, boolean: bool = None):

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
            if boolean:
                self.title_frame.destroy(), self.active_frame.destroy(), self.main_frame.destroy()
            else:
                self.active_frame.destroy()
            self.geometry("679x406")
            self.widget_title_bar()
            self.active_frame = ConnectionFrame(self)
            self.active_frame.pack()
            center(self)

        elif frame_name == 'DebitFrame':
            self.active_frame.destroy()
            self.active_frame = DebitFrame(self)
            self.active_frame.place(x=0, y=80)

    def widget_title_bar(self):
        self.title_frame = tk.Frame(self)
        title_bar = tk.Canvas(self.title_frame, width=679, height=47, bg=set_color('entrycolor'), highlightthickness=0)
        title_bar.create_text(135, 22, text="GestMoney", font=('Roboto', 20, 'bold'), fill=set_color("white"))
        title_bar.pack()

        imgs = tk.PhotoImage(file=select_image("icon.png")).subsample(11)
        icon = tk.Label(self.title_frame, image=imgs, background=set_color("entrycolor"), bd=0,
                        foreground=set_color("lightblue"))
        icon.photo = imgs
        icon.place(x=5, y=0)

        quit_button = tk.Button(self.title_frame, text="X", background=set_color("entrycolor"), cursor='hand2',
                                relief='groove', foreground=set_color("pink"),
                                activebackground=set_color("lightblue"), activeforeground=set_color("pink"),
                                font=('Roboto', 14, 'bold'), command=exit)
        quit_button.place(x=620, y=3, width=40, height=40)
        self.title_frame.pack()

        self.apply_drag([title_bar, icon])

    def mouse_down(self, event):
        self.x, self.y = event.x, event.y

    def mouse_up(self, event):
        self.x, self.y = None, None

    def mouse_drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x0 = self.winfo_x() + deltax
        y0 = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x0, y0))

    def apply_drag(self, elements):
        for element in elements:
            element.bind('<ButtonPress-1>', self.mouse_down)
            element.bind('<B1-Motion>', self.mouse_drag)
            element.bind('<ButtonRelease-1>', self.mouse_up)


if __name__ == "__main__":
    app = Main(None)
    app.mainloop()
