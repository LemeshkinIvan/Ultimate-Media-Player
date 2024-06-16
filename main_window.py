from tkinter import *
from tkinter import ttk

import config
from main_page import MainPage


class MainWindow(Tk):
    HEIGHT = str(config.HEIGHT)
    WIDTH = str(config.WIDTH)

    def __init__(self):
        super().__init__()
        self.title("Ultimate Media Player")
        self.iconbitmap(default=config.ICON_APP)
        self.geometry(self.WIDTH + 'x' + self.HEIGHT)
        self.resizable(False, False)

        MainPage()
