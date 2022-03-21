import json
import tkinter as tk
import cv2

from data.data import select_image_user, get_user, set_user, get_all_users, update_user_id
from source.app.Sys import set_color, select_image, set_appwindow, center

from tkinter import filedialog as fd, messagebox


class ChangePassFrame(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window, width=348, height=440, bg='red')

        self.window = window

        self.tttt = tk.Label(self, text="ddddddd")
        self.tttt.pack()

        # Affichage erreurs
        self.error_canvas = tk.Canvas(self)

