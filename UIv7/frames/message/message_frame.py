import tkinter as tk
from tkinter import Canvas, Button, PhotoImage
from PIL import Image, ImageTk
import threading
import pandas as pd


class Message(tk.Frame):
    def __init__(self, master, Lora):
        super().__init__(master)

        self.thread = None

        self.Lora = Lora

        self.canvas1 = tk.Canvas(
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

        self.original_image = Image.open(
            "frames/message/assets/Hiker_Texting_Resized.png"
        )
        self.resized_image = self.original_image.resize((1200, 800))
        self.tk_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas1.create_image(0, 0, image=self.tk_image, anchor="nw")

        # ====================================================================================================================
        # Canvas for Banner1 (Communication Services)
        #
        self.canvas2 = Canvas(
            self,
            bg="#006400",
            height=50,
            width=1000,
            bd=1,  # Set border width to 1 (or adjust to your preference)
            highlightbackground="Black",  # Set the border color
            highlightthickness=5,
            relief="ridge",
        )

        self.canvas2.place(x=0, y=30)

        self.tempText = self.canvas2.create_text(
            130.0,
            15,
            anchor="nw",
            text="Communication Services",
            fill="#FFFFFF",
            font=("Inter Bold", 20, "bold"),
        )

        # ==========================================================================================================================
        # Canvas for Banner2, with Delta Logo
        #
        self.canvas3 = Canvas(
            self,
            bg="#006400",
            height=62,
            width=178,
            relief="ridge",
            highlightthickness=0,  # Set highlightthickness to 0 to remove the border highlight
        )

        self.canvas3.place(x=1015, y=30)

        self.original_image4 = Image.open("frames/message/assets/delta_logo.png")
        self.resized_image = self.original_image4.resize((60, 60))
        self.tk_image4 = ImageTk.PhotoImage(self.resized_image)
        self.canvas3.create_image(105, 0.5, image=self.tk_image4, anchor="nw")

        self.tempText = self.canvas3.create_text(
            10.0,
            8.0,
            anchor="nw",
            text="TextNav\nServices",
            fill="#FFFFFF",
            font=("Inter Bold", 15, "bold"),
        )

        # ====================================================================================================================
        # Message Canvas

        self.messageString = ""

        # messagecanvas
        self.messagesCanvas = tk.Canvas(
            self,
            bg="#006400",
            height=300,
            width=450,
            bd=1,  # Set border width to 1 (or adjust to your preference)
            highlightbackground="Black",  # Set the border color
            highlightthickness=3,
            relief="ridge",
        )
        self.messagesCanvas.place(x=50, y=150)
        # self.messagesCanvas.place(x=self.findCenterx(self.messagesCanvas), y=50)

        self.messages = self.messagesCanvas.create_text(
            0,
            300,  # Adjust the coordinates for the bottom-left corner
            text=self.messageString,
            justify="left",
            anchor="sw",  # Set anchor to "sw" for bottom-left alignment
        )

        # ============================================================================================================================
        # Buttons with predefined messages on them
        # Keep this as self reference: self.helloButton.place(x=self.findCenterx(self.helloButton), y=400)

        # Hello
        self.helloButton = tk.Button(
            self,
            text="Hello",
            command=lambda: self.addMessage("client: Hello"),
            width=20,
            height=3,
        )
        self.helloButton.place(x=25, y=500)

        # Hi there
        self.hi_there_Button = tk.Button(
            self,
            text="Hi there!!!",
            command=lambda: self.addMessage("client: Hi There!!!"),
            width=20,
            height=3,
        )
        self.hi_there_Button.place(x=25, y=600)

        # Goodbye
        self.Goodbye_Button = tk.Button(
            self,
            text="Goodbye",
            command=lambda: self.addMessage("client: Goodbye"),
            width=20,
            height=3,
        )
        self.Goodbye_Button.place(x=25, y=700)

        # Yes
        self.yes_Button = tk.Button(
            self,
            text="Yes",
            command=lambda: self.addMessage("client: Yes"),
            width=20,
            height=3,
        )
        self.yes_Button.place(x=225, y=500)

        # No
        self.no_Button = tk.Button(
            self,
            text="No",
            command=lambda: self.addMessage("client: No"),
            width=20,
            height=3,
        )
        self.no_Button.place(x=225, y=600)

        # Maybe
        self.maybe_Button = tk.Button(
            self,
            text="Maybe",
            command=lambda: self.addMessage("client: Maybe"),
            width=20,
            height=3,
        )
        self.maybe_Button.place(x=225, y=700)

        # Are you ok?
        self.are_you_ok_Button = tk.Button(
            self,
            text="Are you ok?",
            command=lambda: self.addMessage("client: Are you ok?"),
            width=20,
            height=3,
        )
        self.are_you_ok_Button.place(x=425, y=500)

        # Where are you?
        self.where_are_you_Button = tk.Button(
            self,
            text="Where are you?",
            command=lambda: self.addMessage("client: Where are you?"),
            width=20,
            height=3,
        )
        self.where_are_you_Button.place(x=425, y=600)

        # Quick check-in!
        self.check_in_Button = tk.Button(
            self,
            text="Quick check-in!",
            command=lambda: self.addMessage("client: Quick check-in!"),
            width=20,
            height=3,
        )
        self.check_in_Button.place(x=425, y=700)

        # Location update, please!
        self.location_please_Button = tk.Button(
            self,
            text="Location update, please! ",
            command=lambda: self.addMessage("client: Location update, please! "),
            width=20,
            height=3,
        )
        self.location_please_Button.place(x=625, y=500)

        # Send GPS coordinates
        self.GPS_Coordinates_Button = tk.Button(
            self,
            text="[Send GPS Coordinates]",
            command=lambda: self.addMessage("client: [Insert GPS coordinates here]"),
            width=20,
            height=3,
        )
        self.GPS_Coordinates_Button.place(x=625, y=600)

        # Water that's blessed by the gods themselves
        self.water_Button = tk.Button(
            self,
            text="Found safe drinking water",
            command=lambda: self.addMessage(
                "client: Hey, I found safe drinking water!"
            ),
            width=20,
            height=3,
        )
        self.water_Button.place(x=625, y=700)

        # Wanna meet up?
        self.wanna_meet_up_Button = tk.Button(
            self,
            text="Wanna meet up?",
            command=lambda: self.addMessage("client: Wanna meet up?"),
            width=20,
            height=3,
        )
        self.wanna_meet_up_Button.place(x=825, y=500)

        # How's your hike going?
        self.hike_going_Button = tk.Button(
            self,
            text="How's your hike going?",
            command=lambda: self.addMessage("client: Hey! How's your hike going?"),
            width=20,
            height=3,
        )
        self.hike_going_Button.place(x=825, y=600)

        # Are you close?
        self.are_you_close_Button = tk.Button(
            self,
            text="Are you close?",
            command=lambda: self.addMessage("client: Are you close?"),
            width=20,
            height=3,
        )
        self.are_you_close_Button.place(x=825, y=700)

        # Trail conditions?
        self.trail_Button = tk.Button(
            self,
            text="Trail conditions?",
            command=lambda: self.addMessage("client: Trail conditions?"),
            width=20,
            height=3,
        )
        self.trail_Button.place(x=1025, y=500)

        # Safe
        self.safe_Button = tk.Button(
            self,
            text="safe",
            command=lambda: self.addMessage("client: safe"),
            width=20,
            height=3,
        )
        self.safe_Button.place(x=1025, y=600)

        # unsafe
        self.unsafe_Button = tk.Button(
            self,
            text="unsafe",
            command=lambda: self.addMessage("client: unsafe"),
            width=20,
            height=3,
        )
        self.unsafe_Button.place(x=1025, y=700)

        # Danger! Stay away!
        self.danger_Button = tk.Button(
            self,
            text="Danger! Stay away!",
            command=lambda: self.addMessage("client: Danger! Stay away!"),
            width=20,
            height=3,
        )
        self.danger_Button.place(x=825, y=260)

        # Add a new button to clear the canvas
        self.clearButton = tk.Button(
            self,
            text="[Update Messages]",
            command=self.clearMessages,
            width=20,
            height=3,
        )
        self.clearButton.place(x=1025, y=260)

    # ============================================================================================================================

    # Function to clear messages
    def updateMessageLora(self):
        self.Lora.add_to_queue(self.Lora.active_listen)
        self.updateMessageBorad()

    # update message window of the id loops every 5 sec
    def updateMessageBoard(self):
        if self.Lora.messageDone == True:
            self.Lora.messageDone = False

            id = "1111111111111111"

            df = pd.read_csv("data/messages.csv")
            clean = df.dropna(subset=[id])[id]
            self.messageString = ""
            for x in clean:
                self.messageString = self.messageString + "\n" + x

            self.messagesCanvas.itemconfig(self.messages, text=self.messageString)
        else:
            self.after(1000, self.updateMessageBoard)

    def clearMessages(self):
        self.messageString = ""
        self.messagesCanvas.itemconfig(self.messages, text=self.messageString)

    def addMessage(self, s):
        self.messageString = self.messageString + "\n" + s
        self.messagesCanvas.itemconfig(self.messages, text=self.messageString)

        # self.threadMessage(s)

        self.Lora.add_to_queue(self.Lora.send_text, "1111111111111111", f"{s}")

        # self.Lora.send_text("b69b9d14e5e5b0c0", f"{s}")

    def threadMessage(self, s):
        if self.thread and self.thread.is_alive():
            print("Threaded function is already running.")
        else:
            # Create and start a new thread
            self.thread = threading.Thread(
                target=self.Lora.send_text, args=("b69b9d14e5e5b0c0", f"{s}")
            )
            self.thread.start()
            print("Threaded function started.")

    def findCenterx(self, object):
        self.object = object
        self.width = 1200
        self.objectWidth = object.winfo_reqwidth()

        self.x = (self.width - self.objectWidth) // 2

        return self.x


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")

    frame = Message(root)
    frame.config(width=1200, height=800)
    frame.pack()

    root.mainloop()
