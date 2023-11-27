import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import pandas as pd
import time
from PIL import Image, ImageTk


class Env(tk.Frame):
    def __init__(self, master, Bme):
        super().__init__(master)

        self.Bme = Bme

        # ====================================================================================================================
        self.canvas = Canvas(
            self,
            bg="#AFAFAF",
            height=800,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        # ====================================================================================================================
        # Background Image of Clouds

        self.original_image = Image.open("frames/env/assets/cloud.png")
        self.resized_image = self.original_image.resize((1200, 800))
        self.tk_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")

        # Background Rectangle for Text
        # (first set coordinates for top left corner, second set coordinates for bottom right corner)
        # (x1, y1, x2, y2)
        # self.canvas.create_rectangle(35,150,400,600,outline ="white",fill ="black",width = 2) #Dont delete please
        # Default for center: 200,150,1000,600
        self.canvas.create_rectangle(
            400, 150, 800, 615, outline="black", fill="DeepSkyBlue2", width=2
        )

        # Image of the Sun
        self.original_image2 = Image.open("frames/env/assets/praise_the_sun.png")
        self.resized_image = self.original_image2.resize((250, 250))
        self.tk_image2 = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(480, 225, image=self.tk_image2, anchor="nw")

        # ====================================================================================================================
        # Canvas for Banner1
        # Tariq
        #
        self.canvas2 = Canvas(
            self,
            bg="#B2EEEE",
            height=50,
            width=1000,
            bd=1,  # Set border width to 1 (or adjust to your preference)
            highlightbackground="DeepSkyBlue2",  # Set the border color
            highlightthickness=5,
            relief="ridge",
        )

        self.canvas2.place(x=0, y=30)

        self.tempText = self.canvas2.create_text(
            70.0,
            15,
            anchor="nw",
            text="Environmental Metrics: Temperature, Humidity, and Pressure Analysis",
            fill="#00BFFF",
            font=("Inter Bold", 20, "bold"),
        )

        # ====================================================================================================================
        # Canvas for Banner2
        # Tariq
        #
        self.canvas3 = Canvas(
            self,
            bg="#00BFFF",
            height=62,
            width=178,
            relief="ridge",
            highlightthickness=0,  # Set highlightthickness to 0 to remove the border highlight
        )

        self.canvas3.place(x=1015, y=30)

        self.original_image3 = Image.open("frames/env/assets/delta_logo.png")
        self.resized_image = self.original_image3.resize((60, 60))
        self.tk_image3 = ImageTk.PhotoImage(self.resized_image)
        self.canvas3.create_image(115, 0.5, image=self.tk_image3, anchor="nw")

        self.tempText = self.canvas3.create_text(
            5.0,
            0.0,
            anchor="nw",
            text="NatureNav\nNews",
            fill="#FFFFFF",
            font=("Inter Bold", 18, "bold"),
        )

        # ====================================================================================================================

        self.rigntnow = self.canvas.create_text(
            515.0,
            180.0,
            anchor="nw",
            text="Right Now:",
            fill="#FFFFFF",
            font=("Inter Bold", 25, "bold"),
        )

        self.tempText = self.canvas.create_text(
            480.0,
            480.0,
            anchor="nw",
            text="Temperature: 21°C ",
            fill="#FFFFFF",
            font=("Inter Bold", 20, "bold"),
        )

        self.humdText = self.canvas.create_text(
            480.0,
            515.0,
            anchor="nw",
            text="Humidity: 50 % ",
            fill="#FFFFFF",
            font=("Inter Bold", 20, "bold"),
        )

        self.pressText = self.canvas.create_text(
            480.0,
            550.0,
            anchor="nw",
            text="Pressure: 1000 hPa ",
            fill="#FFFFFF",
            font=("Inter Bold", 20, "bold"),
        )

        self.custom_font = ("Helvetica", 16, "bold")  # setting the font
        # frame to display all the forcast data
        self.forcastFrame = tk.Frame(
            self,
            bg="DeepSkyBlue2",
            bd=1,
            highlightthickness=2,
            highlightbackground="Black",
        )
        self.forcastFrame.place(x=self.findCenterx(self.forcastFrame), y=600)

        # to make all the labels and display the data in forcastFrame
        self.forcast()

        self.update_data()

    def update_data(self):
        self.canvas.itemconfig(
            self.tempText, text=f"Temperature: {self.Bme.getTemp():.2f}"
        )
        self.canvas.itemconfig(
            self.humdText, text=f"Humidity: {self.Bme.getHumidity():.2f}"
        )
        self.canvas.itemconfig(
            self.pressText, text=f"Altitude: {self.Bme.getAltitude():.2f}"
        )

        self.after(3000, self.update_data)

    def to_Fahrenheit(self, celsius):
        fahrenheit = (float(celsius) * 9 / 5) + 32
        return fahrenheit

    def forcast(self):
        self.df = pd.read_csv("data/weather_data.csv")
        self.df = self.df.T

        # add High-low label
        self.per = tk.Label(
            self.forcastFrame,
            bg="DeepSkyBlue2",
            fg="white",
            text="High-Low",
            font=self.custom_font,
        )
        self.per.grid(row=1, column=0)

        # add Precipitation label
        self.day = tk.Label(
            self.forcastFrame,
            text="Precipitation",
            bg="DeepSkyBlue2",
            fg="white",
            font=self.custom_font,
        )
        self.day.grid(row=2, column=0)

        # will generate the day, hilo temp, and precipitation for df
        for col in range(5):
            # makes all the days display
            dayLabel = tk.Label(
                self.forcastFrame,
                text=self.df.iloc[0, col],
                font=self.custom_font,
                fg="white",
                bg="DeepSkyBlue2",
            )
            dayLabel.grid(row=0, column=col + 1)

            # makes all the HiLo temps display
            HiLo = tk.Label(
                self.forcastFrame,
                text=f"{self.to_Fahrenheit(self.df.iloc[1,col]):.0f} - {self.to_Fahrenheit(self.df.iloc[2,col]):.0f}",
                font=self.custom_font,
                bg="DeepSkyBlue2",
                fg="white",
            )
            HiLo.grid(row=1, column=col + 1)

            # makes all the preChance display
            preChance = tk.Label(
                self.forcastFrame,
                text=self.df.iloc[3, col],
                font=self.custom_font,
                bg="DeepSkyBlue2",
                fg="white",
            )
            preChance.grid(row=2, column=col + 1)

        self.update()  # THIS IS IMPORTANT, this will update the geometry of the forcastFrame, so I can center the frame

        # places the forcastFrame in the center after place all the other labels
        self.forcastFrame.place(x=self.findCenterx(self.forcastFrame), y=650)

    def findCenterx(self, object):
        self.object = object
        self.width = 1200
        self.objectWidth = object.winfo_width()

        self.x = (self.width // 2) - (self.objectWidth // 2)

        return self.x


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x800")

    # Instantiate Plant class
    frame = Env(root)
    frame.config(width=1200, height=800)

    # Pack the Plant frame
    frame.pack()
    root.mainloop()
