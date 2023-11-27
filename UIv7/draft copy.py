import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pandas as pd

from frames.toolbar.toolbar import ToolBar
from frames.emergency.emg_frame import Emg
from frames.map_stuff.map_frame import MapFrame
from frames.plant_stuff.plant_frame import Plant
from frames.env.env_frame import Env
from frames.setting.setting_frame import SettingFrame
from frames.message.message_frame import Message


class MainApplication:
    def __init__(self, master):
        # master is root, root represents the main application window

        self.theframes = [MapFrame, Plant, Env, Message, SettingFrame, Emg]

        self.master = master

        self.master.geometry("1280x800")  # set window size

        # ToolBar frame, the right side with buttons

        self.toolBar = ToolBar(master, self.switch_frame, self.theframes)
        self.toolBar.pack(side="left")
        self.toolBar.config(width=80, height=800)

        # main frame
        # the frame that will hold the other frames, the left side
        # make after tool bar so take the first left side, main frame left of tool bar

        self.mainFrame = tk.Frame(master, width=1200, height=800)
        self.mainFrame.pack(side="left")

        # make intances of each frame and store them in frames with width=1200, height=800
        # ask cody question for more information

        self.frames = {}  # Store frame instances
        for FrameClass in self.theframes:
            frame = FrameClass(self.mainFrame)
            frame.grid(row=0, column=0, sticky="wnse")
            frame.config(width=1200, height=800)
            self.frames[FrameClass] = frame

        self.switch_frame(MapFrame)  # defualt page

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
