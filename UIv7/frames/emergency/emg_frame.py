import tkinter as tk
from tkinter import Canvas, Button, PhotoImage
from PIL import Image, ImageTk


class Emg(tk.Frame):
    def __init__(self, master, Gps, Lora):
        super().__init__(master)

        self.Gps = Gps
        self.Lora = Lora

        self.canvas1 = Canvas(
            self,
            bg="#AFAFAF",
            height=800,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas1.place(x=0, y=0)

        # ====================================================================================================================
        # Background Image of Hiker Lost

        self.original_image = Image.open("frames/emergency/assets/EMG_Services.png")
        self.resized_image = self.original_image.resize((1200, 800))
        self.tk_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas1.create_image(0, 0, image=self.tk_image, anchor="nw")

        # ====================================================================================================================

        # flashing image Code
        self.original_image2 = Image.open("frames/emergency/assets/flashing.png")
        self.resized_image = self.original_image2.resize((600, 600))
        self.tk_image2 = ImageTk.PhotoImage(self.resized_image)
        self.canvas1.create_image(550, 50, image=self.tk_image2, anchor="nw")

        # ====================================================================================================================
        # Canvas for Banner1 (I Need help services with short explanation)
        # Tariq
        #
        self.canvas2 = Canvas(
            self,
            bg="#EE0000",
            height=50,
            width=1000,
            bd=1,  # Set border width to 1 (or adjust to your preference)
            highlightbackground="Black",  # Set the border color
            highlightthickness=5,
            relief="ridge",
        )

        self.canvas2.place(x=0, y=30)

        self.tempText = self.canvas2.create_text(
            70.0,
            15,
            anchor="nw",
            text="Emergency Services! Please Press Red Button for Help if Lost or Hurt!",
            fill="#FFFFFF",
            font=("Inter Bold", 20, "bold"),
        )

        # ==========================================================================================================================
        # Canvas for Banner2
        # Tariq
        #
        self.canvas3 = Canvas(
            self,
            bg="#EE0000",
            height=62,
            width=178,
            relief="ridge",
            highlightthickness=0,  # Set highlightthickness to 0 to remove the border highlight
        )

        self.canvas3.place(x=1015, y=30)

        self.original_image4 = Image.open("frames/emergency/assets/logo2.png")
        self.resized_image = self.original_image4.resize((60, 60))
        self.tk_image4 = ImageTk.PhotoImage(self.resized_image)
        self.canvas3.create_image(105, 0.5, image=self.tk_image4, anchor="nw")

        self.tempText = self.canvas3.create_text(
            10.0,
            8.0,
            anchor="nw",
            text="EmgNav\nServices",
            fill="#FFFFFF",
            font=("Inter Bold", 15, "bold"),
        )

        # ====================================================================================================================

        # Emergency Button Code
        self.original_image3 = Image.open("frames/emergency/assets/button_1.png")
        self.resized_image3 = self.original_image3.resize((500, 150))
        self.tk_image3 = ImageTk.PhotoImage(self.resized_image3)
        self.button = self.canvas1.create_image(
            600, 550, image=self.tk_image3, anchor="nw"
        )

        # Bind the button press event to the function
        self.canvas1.tag_bind(self.button, "<Button-1>", self.button_pressed)

        # Text over button
        self.helptext = self.canvas1.create_text(
            750.0,
            608.0,
            anchor="nw",
            text="I NEED HELP",
            fill="#FFFFFF",
            font=("Inter Bold", 25, "bold"),
        )

        # Bind the button press event to the "i need help part"
        self.canvas1.tag_bind(self.helptext, "<Button-1>", self.button_pressed)

    # If user presses button, do something here
    def button_pressed(self, event):
        cords = self.Gps.getCords()  # [latitude, longitude, 1]
        lat = cords[0]
        long = cords[1]
        self.Lora.send_text("b69b9d14e5e5b0c0", f"{lat},{long}")


# ====================================================================================================================

# if __name__ == "__main__":


#     root = tk.Tk()
#     root.geometry("1280x800")

#     # Instantiate Emg class
#     frame = Emg(root, Gps, Lora)
#     frame.config(width=1200, height=800)

#     # Pack the Emg frame
#     frame.grid(row=0, column=0)
#     # frame.pack()
#     root.mainloop()
