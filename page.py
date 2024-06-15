import tkinter
from tkinter import ttk
from typing import Any
import config


class Page:
    frame: tkinter.Frame = None

    def __init__(self):
        self.frame["height"] = config.HEIGHT
        self.frame["width"] = config.WIDTH


    def init_tree_table(self, frame, columns: list[str],
                        columns_settings: dict[str, Any]):
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree["height"] = 5
        tree.grid(row=1, column=0)

