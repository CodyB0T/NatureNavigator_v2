import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import cv2
import os
import torch
from PIL import Image, ImageTk


class Plant(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.CameraUpdate = True  # Corrected variable name

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

        # midline

        # self.midline = Canvas(
        #     self,
        #     bg="black",
        #     height=800,
        #     width=5,
        #     bd=0,
        #     highlightthickness=0,
        #     relief="ridge",
        # )

        # self.midline.place(x=600, y=0)

        self.camera = cv2.VideoCapture(0)
        self.image_saved = False
        self.model_path = "frames/plant_stuff/best.pt"
        self.model = torch.hub.load(
            "frames/plant_stuff/yolov5", "custom", path=self.model_path, source="local"
        )

        # capture button

        self.capture_button = tk.Button(
            self,
            text="Capture",
            command=self.capture_image,
            anchor="center",
        )
        self.capture_button.place(x=self.findCenterx(self.capture_button), y=600)

        # camera_canvas

        self.camera_canvas = tk.Canvas(
            self,
            width=640,
            height=480,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.camera_canvas.place(x=self.findCenterx(self.camera_canvas), y=0)

        # inital image

        self.image = Image.open("frames/plant_stuff/image.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.camera_image = self.camera_canvas.create_image(
            0, 0, anchor="nw", image=self.photo
        )

        # result_label

        self.result_label = tk.Label(
            self, text="", font=("Helvetica", 12), foreground="black", bg="#AFAFAF"
        )
        self.result_label.place(x=self.findCenterx(self.result_label), y=500)

        # update camera

        self.update_camera()

    def update_camera(self):
        if self.CameraUpdate:  # Corrected variable name
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
                frame = cv2.resize(frame, (640, 480))
                self.image = Image.fromarray(frame)
                self.photo = ImageTk.PhotoImage(self.image)

                self.camera_canvas.itemconfig(self.camera_image, image=self.photo)

                # Remember to keep a reference to the new image, or it might be garbage collected
                # self.camera_canvas = photo

            self.after(10, self.update_camera)

    def capture_image(self):
        if self.CameraUpdate:
            self.CameraUpdate = False
            self.capture_button.config(text="take another picture")
            self.capture_button.place(x=self.findCenterx(self.capture_button), y=600)

            if not self.image_saved:
                output_path = "frames/plant_stuff/captured_image.jpg"
                ret, frame = self.camera.read()

                if ret:
                    cv2.imwrite(output_path, frame)
                    self.image_saved = True

                    try:
                        self.result = self.model(output_path)
                        predictions = self.result.pred[
                            0
                        ]  # Get predictions for the first image (assuming batch size is 1)
                        most_confident_prediction = predictions[
                            torch.argmax(predictions[:, 4])
                        ]  # Get the most confident prediction
                        class_id = int(most_confident_prediction[5])
                        class_name = self.model.names[
                            class_id
                        ]  # Get class name from the model's class list
                        confidence = float(
                            most_confident_prediction[4]
                        )  # Get confidence score

                        # Return the formatted recognition result
                        self.result = f"Detected: {class_name}"
                    except Exception as e:
                        self.result = "Plant recognition failed: " + str(e)

                    if self.result is not None:
                        print("testing")

                        self.result_label.config(
                            text=f"Plant recognition result:\n {self.result}"
                        )
                        self.result_label.place(
                            x=self.findCenterx(self.result_label), y=500
                        )

                    # Reset the image_saved flag to allow capturing another image
                    self.image_saved = False
        else:
            self.CameraUpdate = True

            self.capture_button.config(text="Capture")
            self.capture_button.place(x=self.findCenterx(self.capture_button), y=600)

            self.result_label.config(text="")
            self.update_camera()

    def findCenterx(self, object):
        self.object = object
        self.width = 600
        self.objectWidth = object.winfo_reqwidth()

        self.x = self.width - self.objectWidth // 2

        return self.x


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x800")

    # Instantiate Plant class
    frame = Plant(root)
    frame.config(width=1200, height=800)

    # Pack the Plant frame
    frame.grid(row=0, column=0)
    root.mainloop()
