import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import datetime


class ToolBar(tk.Frame):
    def __init__(self, master, switch_frame, frames):
        super().__init__(master)

        # frames = [MapFrame, Plant, Env, Message, SettingFrame, Emg]
        self.frames = frames

        self.switch_frame = switch_frame

        self.canvas = Canvas(
            self,
            bg="#000000",
            height=800,
            width=80,
            # bd is border width defualt to 2 pixels
            # same for highlightthickness
            bd=0,
            highlightthickness=0,
        )
        self.canvas.place(x=0, y=0)

        # Time

        self.clock = self.canvas.create_text(
            40.0,
            17.0,
            anchor="center",
            text="12:00",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1),
        )

        # updates the time every 3 sec
        self.updateTime()

        # map button

        self.button_image_1 = PhotoImage(file="frames/toolbar/assets/map.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_frame(0),
            relief="flat",
            bg="black",
            activebackground="black",
        )
        self.button_1.place(x=12.0, y=365.0, width=56.0, height=56.0)

        # camera button

        self.button_image_5 = PhotoImage(file="frames/toolbar/assets/camera.png")
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_frame(1),
            relief="flat",
            bg="black",
            activebackground="black",
        )
        self.button_5.place(x=12.0, y=447.0, width=56.0, height=56.0)

        # env data button

        self.button_image_2 = PhotoImage(file="frames/toolbar/assets/env.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_frame(2),
            relief="flat",
            bg="black",
            activebackground="black",
        )
        self.button_2.place(x=12.0, y=529.0, width=56.0, height=56.0)

        # message button

        self.button_image_3 = PhotoImage(file="frames/toolbar/assets/message.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_frame(3),
            relief="flat",
            bg="black",
            activebackground="black",
        )
        self.button_3.place(x=12.0, y=611.0, width=56.0, height=56.0)

        # setting button

        self.button_image_4 = PhotoImage(file="frames/toolbar/assets/setting.png")
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_frame(4),
            relief="flat",
            bg="black",
            activebackground="black",
        )
        self.button_4.place(x=12.0, y=693.0, width=56.0, height=56.0)

        # emg button

        self.button_image_6 = PhotoImage(file="frames/toolbar/assets/emg.png")
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.switch_frame(5),
            relief="flat",
            bg="black",
            activebackground="black",
        )
        self.button_6.place(x=12.0, y=173.0, width=56.0, height=56.0)

    def updateTime(self):
        # Get the current time
        self.current_time = datetime.datetime.now().time()

        # Format the time
        self.formatted_time = self.current_time.strftime("%I:%M %p")

        self.canvas.itemconfig(self.clock, text=f"{self.formatted_time}")

        self.after(3000, self.updateTime)
