import os
from ctypes import windll


def select_image(name):
    scriptpath = os.path.abspath(__file__)
    scriptdir = os.path.dirname(scriptpath)
    return os.path.join(scriptdir, f"ressource\\img\\{name}")


def set_color(theme, color):
    themes = {
        'basic': {
            'bg': '#001242',
            'green': '#77AB7D',
            'darkbg': '#000022',
            'text2': 'white',
            'text': '#DC2A58',
            'buttonactive': '#001242',
            'onactivebutton': '#050B1C',
            'fourthbg': '#050B1C',
            'entrytext': 'white',
            'error': 'red',
            'tertiarybg': '#2D4481',
            'copyright': '#C6CACB'
                  }
    }
    return themes[theme][color]


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry(f'{width}x{height}+{x}+{y}')
    win.deiconify()


def set_appwindow(mainWindow):  # Pour afficher l'icon dans la barre des taches

    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)

    mainWindow.wm_withdraw()
    mainWindow.after(10, mainWindow.wm_deiconify)
