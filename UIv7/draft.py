import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pandas as pd

# import frames
from frames.toolbar.toolbar import ToolBar
from frames.emergency.emg_frame import Emg
from frames.map_stuff.map_frame import MapFrame
from frames.map_stuff.map_frame_offline import OfflineMapFrame
from frames.plant_stuff.plant_frame import Plant
from frames.env.env_frame import Env
from frames.setting.setting_frame import SettingFrame
from frames.message.message_frame import Message

# import sensor modules
from sensorLibs.Lora import Lora
from sensorLibs.Bme import Bme
from sensorLibs.Gps import Gps


class MainApplication:
    def __init__(self, master):
        # master is root, root represents the main application window

        self.frames = [MapFrame, Plant, Env, Message, SettingFrame, Emg]

        self.master = master

        self.master.geometry("1280x800")  # set window size

        # ToolBar frame, the right side with buttons

        self.toolBar = ToolBar(master, self.switch_frame, self.frames)
        self.toolBar.pack(side="left")
        self.toolBar.config(width=80, height=800)

        # main frame
        # the frame that will hold the other frames, the left side
        # make after tool bar so take the first left side, main frame left of tool bar

        self.mainFrame = tk.Frame(master, width=1200, height=800)
        self.mainFrame.pack(side="left")

        # make intances of each frame and store them in frames with width=1200, height=800
        # ask cody question for more information

        # make class instances
        self.Bme = Bme()
        self.Lora = Lora()
        self.Gps = Gps()

        # storing the frame into the frames list

        # Mapframe
        # self.frames[0] = MapFrame(self.mainFrame, self.Gps)
        # offline map
        self.frames[0] = OfflineMapFrame(self.mainFrame, self.Gps)

        # Plant
        self.frames[1] = Plant(self.mainFrame)

        # env
        self.frames[2] = Env(self.mainFrame, self.Bme)

        # message
        self.frames[3] = Message(self.mainFrame, self.Lora)

        # settingFrame
        self.frames[4] = SettingFrame(self.mainFrame)

        # emg
        self.frames[5] = Emg(self.mainFrame, self.Gps, self.Lora)

        # place all of the frames in the same spot
        for x in range(6):
            self.frames[x].grid(row=0, column=0, sticky="wnse")
            self.frames[x].config(width=1200, height=800)

        self.switch_frame(0)  # defualt page map frame

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)

    root.attributes("-fullscreen", True)
    root.bind("<q>", lambda event: root.attributes("-fullscreen", False))

    root.mainloop()
