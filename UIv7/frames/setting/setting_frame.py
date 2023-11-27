import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class SettingFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = Canvas(
            self,
            bg="white",
            height=800,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            460.0,
            63.0,
            anchor="nw",
            text="Settings page",
            fill="#000000",
            font=("Inter Bold", 40 * -1),
        )

        # self.canvas.create_text(
        #     50.0,
        #     173.0,
        #     anchor="nw",
        #     text="Degrees: ",
        #     fill="#000000",
        #     font=("Inter Bold", 36 * -1),
        # )

        # self.canvas.create_text(
        #     222.0,
        #     177.0,
        #     anchor="nw",
        #     text="C",
        #     fill="#000000",
        #     font=("Inter Bold", 36 * -1),
        # )

        # self.canvas.create_rectangle(
        #     250.0, 173.0, 313.0, 224.0, fill="#FFFFFF", outline=""
        # )

    #     self.buttonfull = tk.Button(text="fullscreen", command=self.fullscreen)
    #     self.buttonfull.place(x=400, y=400)

    #     self.buttonExitFull = tk.Button(
    #         text="exit fullscreen", command=self.exitFullscreen
    #     )
    #     self.buttonExitFull.place(x=500, y=400)

    # def fullscreen(self):
    #     self.master.attributes("-fullscreen", True)

    # def exitFullscreen(self):
    #     self.master.attributes("-fullscreen", False)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x800")

    # Instantiate Emg class
    frame = SettingFrame(root)
    frame.config(width=1200, height=800)

    # Pack the Emg frame
    frame.grid(row=0, column=0)
    root.mainloop()
