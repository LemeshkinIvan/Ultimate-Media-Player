from tkinter import *
import config


class MainWindow(Tk):
    HEIGHT = str(config.HEIGHT)
    WIDTH = str(config.WIDTH)

    upper_frame = None
    center_frame = None
    lower_frame = None

    def __init__(self):
        super().__init__()
        self.title("Ultimate Media Player")
        self.iconbitmap(default=config.icon)
        self.geometry(self.WIDTH + 'x' + self.HEIGHT)
        self.resizable(False, False)

        # frames
        self.main_frame = Frame(height=self.HEIGHT, width=self.WIDTH)
        self.main_frame.pack()

        self.init_frames()
        self.color_frames()
        self.init_login_button()

    def init_frames(self):
        # 14 - still magic number
        frame_height = (int(self.HEIGHT) / 14)
        frame_width = (int(self.WIDTH))
        center_frame_height = int(self.HEIGHT) - frame_height * 2

        self.upper_frame = Frame(relief=SOLID, borderwidth=1,
                                 height=frame_height,
                                 width=frame_width,
                                 master=self.main_frame)
        self.upper_frame.pack(side="top", fill="x")
        self.upper_frame.pack_propagate(False)

        self.center_frame = Frame(relief=SOLID, borderwidth=1,
                                  height=center_frame_height - 100,
                                  width=frame_width,
                                  master=self.main_frame)
        self.center_frame.pack(side="top", fill="x")
        self.center_frame.pack_propagate(False)

        self.lower_frame = Frame(relief=SOLID, borderwidth=1,
                                 height=frame_height + 100,
                                 width=frame_width,
                                 master=self.main_frame)
        self.lower_frame.pack(side="bottom", fill="x")
        self.lower_frame.pack_propagate(False)

    def color_frames(self):
        for key, value in self.main_frame.children.items():
            if type(value) is Frame:
                value.configure(bg="#26272a")

    def init_login_button(self):
        frame_for_button = Frame(self.upper_frame, height=self.upper_frame.winfo_height(),
                                 width=self.WIDTH, relief=SOLID, borderwidth=1)
        frame_for_button.pack(side="right", fill="y")

        button = Button(master=frame_for_button, text="Войти")
        button.pack(side="right", padx=(int(self.WIDTH) / 20))
