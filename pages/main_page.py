from tkinter import *
import config


class MainPage:
    HEIGHT = config.HEIGHT
    WIDTH = config.WIDTH

    upper_frame = None
    center_frame = None
    lower_frame = None

    def __init__(self):
        # frames
        self.main_frame = Frame(height=self.HEIGHT, width=self.WIDTH)
        self.main_frame.pack()

        self.init_frames()
        self.color_frames()
        self.init_login_button()
        self.init_menu_buttons()

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
                value.configure(bg=config.FRAME_COLOR)

    def init_login_button(self):
        frame_for_button = Frame(self.upper_frame, height=60,
                                 width=self.WIDTH, relief=SOLID, borderwidth=1)
        frame_for_button.pack(side="right", fill="y")

        img = PhotoImage(file=config.ICON_LOGIN)

        button = Button(master=frame_for_button, text="Войти", compound="left")
        button.pack(side="right", padx=(int(self.WIDTH) / 20))

    def init_menu_buttons(self):
        for item in list(["Открыть файл", "Плейлисты", "Настройки"]):
            Button(master=self.lower_frame, text=item).pack(side="left", padx=150)
