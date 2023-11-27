import cv2
import os
import torch
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class PlantRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plant Recognition App")

        self.camera = cv2.VideoCapture(0)
        self.image_saved = False
        self.model_path = "/home/deltalabs/Desktop/PlantRecog/best.pt"
        self.model = torch.hub.load(
            "/home/deltalabs/Desktop/yolov5",
            "custom",
            path=self.model_path,
            source="local",
        )

        self.root.configure(bg="blue")  # Set the background color of the main window

        self.camera_label = ttk.Label(self.root)
        self.camera_label.pack()

        self.capture_button = ttk.Button(
            self.root, text="Capture", command=self.capture_image
        )
        self.capture_button.pack(pady=10)
        self.capture_button.configure(width=20)

        self.quit_button = ttk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)
        self.quit_button.configure(width=20)

        self.result_label = ttk.Label(
            self.root, text="", font=("Helvetica", 12), foreground="black"
        )  # Set text color to black
        self.result_label.pack()

        self.update_camera()

    def capture_image(self):
        if not self.image_saved:
            output_path = "captured_image.jpg"
            ret, frame = self.camera.read()
            if ret:
                cv2.imwrite(output_path, frame)
                self.image_saved = True

                result = self.recognize_plant(output_path)

                if result is not None:
                    result_text = result.replace(
                        "Speed, inference, and NMS per image: ", ""
                    )
                    self.result_label.config(
                        text="Plant recognition result:\n" + result_text
                    )

                os.remove(output_path)

                # Reset the image_saved flag to allow capturing another image
                self.image_saved = False

    def recognize_plant(self, image_path):
        try:
            result = self.model(image_path)
            return str(result)
        except Exception as e:
            return "Plant recognition failed: " + str(e)

    def update_camera(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            frame = cv2.resize(frame, (640, 480))
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)
            self.camera_label.config(image=photo)
            self.camera_label.photo = photo
        self.root.after(10, self.update_camera)


if __name__ == "__main__":
    root = tk.Tk()
    app = PlantRecognitionApp(root)
    root.mainloop()
