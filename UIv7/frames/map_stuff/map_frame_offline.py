import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import tkintermapview
import pandas as pd
from PIL import Image, ImageTk
import os


####################### map frame #######################


class OfflineMapFrame(tk.Frame):
    def __init__(self, master, Gps):
        super().__init__(master)

        self.Gps = Gps

        # ====================================================================================================================
        # Changes Tariq Made/Added

        # Load in the background Image:
        # Load the image
        image_path = "frames/map_stuff/assets/world.png"  # Replace this with the actual file path of your image
        self.background_image = Image.open(image_path)

        # Resize the image to your desired dimensions (width, height) with LANCZOS filter
        new_width = 1200  # Replace this with your desired width
        new_height = 800  # Replace this with your desired height
        self.background_image = self.background_image.resize(
            (new_width, new_height), Image.LANCZOS
        )

        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # background image label
        self.background_image_label = tk.Label(
            self,
            image=self.background_photo,
            borderwidth=0,  # Set borderwidth to 0 to remove the border
            highlightthickness=0,  # Set highlightthickness to 0 to remove the border
            bd=0,
        )
        self.background_image_label.place(x=0, y=0)  # Adjust the coordinates as needed

        # ====================================================================================================================

        # self.image_image_1 = PhotoImage(file="assets/map/asset/image_1.png")
        # self.image_1 = self.canvas.create_image(600.0, 303.0, image=self.image_image_1)

        # script_directory = os.path.dirname(os.path.abspath(__file__))
        # database_path = os.path.join(script_directory, "data/offline_tiles.db")

        self.map_widget = tkintermapview.TkinterMapView(
            self,
            width=1000,
            height=600,
            corner_radius=20,
            use_database_only=True,
            max_zoom=18,
            database_path="data/offline_tiles.db",
        )
        self.map_widget.config(bg="black")

        # self.map_widget.place(x=50, y=25)

        # self.map_widget.pack(side="top", pady=18)

        self.map_widget.place(x=self.findCenterx(self.map_widget), y=25)

        self.map_widget.set_marker(33.93800600852982, -84.52126795783944)
        self.map_widget.set_position(33.93800600852982, -84.52126795783944)
        self.map_widget.set_zoom(15)

        # Create seperate Canvas for Text like Latitude and Longitude
        # Tariq Added
        self.canvas = Canvas(
            self,
            bg="#1E90FF",
            height=100,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=400, y=650)

        # Draw a black border around the canvas
        # Tariq Added
        border_width = 7  # You can adjust the border width as needed
        self.canvas.create_rectangle(
            border_width,
            border_width,
            400 - border_width,
            100 - border_width,
            outline="black",  # Set the border color to black
            width=border_width,  # Set the border width
        )

        # Text for Latitude and Longitude
        self.latText = self.canvas.create_text(
            25,
            10,
            anchor="nw",
            text="Latitude: 33.9380060",
            fill="#000000",
            font=("Inter", 32 * -1),
        )

        self.longText = self.canvas.create_text(
            25,
            55,
            anchor="nw",
            text="Longitude: -84.5212679",
            fill="#000000",
            font=("Inter", 32 * -1),
        )

        self.updateLocation()

    def findCenterx(self, object):
        self.object = object
        self.width = 1200
        self.objectWidth = object.winfo_reqwidth()

        self.x = (self.width - self.objectWidth) // 2

        return self.x

    def updateLocation(self):
        cords = self.Gps.getCords()  # [latitude, longitude, 1]
        lat = cords[0]
        long = cords[1]
        self.canvas.itemconfig(self.latText, text=f"Latitude: {lat:.7f}")
        self.canvas.itemconfig(self.longText, text=f"Longitude: {long:.7f}")
        self.map_widget.delete_all_marker()
        self.map_widget.set_marker(lat, long)
        self.map_widget.set_position(lat, long)
        self.after(5000, self.updateLocation)

    # def update_location(self):
    #     self.df = pd.read_csv("data/gps_data.csv")
    #     self.lat = self.df.iloc[0, 1]
    #     self.long = self.df.iloc[0, 2]
    #     self.map_widget.delete_all_marker()
    #     self.map_widget.set_marker(self.lat, self.long)
    #     self.map_widget.set_position(self.lat, self.long)
    #     self.canvas.itemconfig(self.latText, text=f"Latitude: {self.lat:.7f}")
    #     self.canvas.itemconfig(self.longText, text=f"Longitude: {self.long:.7f}")
    #     self.after(5000, self.update_location)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x800")

    # Instantiate Plant class
    frame = OfflineMapFrame(root)

    frame.config(width=1200, height=800)

    # Pack the Plant frame
    frame.pack()
    root.mainloop()
