from tkinter import Tk, filedialog
import config

"""
    Window - оболочка, физ.контейнер, содержащий конфиг.
    Page - контейнер виджетов.
"""


class MainWindow(Tk):
    HEIGHT = str(config.HEIGHT)
    WIDTH = str(config.WIDTH)

    def __init__(self):
        super().__init__()
        self.geometry(self.HEIGHT + 'x' + self.WIDTH)
        self.title("Ultimate Media Player")
        self.resizable(False, False)

