import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar
import cv2
import os
import torch
from PIL import Image, ImageTk

# ================================================================================================================
# plant information. Couldn't figure out how to put this in a seperate file, so for now
# it'll be in the same file as the plant class.


plants = {
    "Mint": {
        "description": "Mint, a member of the Lamiaceae family, is a popular aromatic herb known for its refreshing scent and flavorful leaves. There are several species within the Mentha genus, with peppermint (Mentha piperita) and spearmint (Mentha spicata) being the most common. Mint plants have square stems, opposite leaves, and small, tubular flowers in shades of white, pink, or purple. They are well-known for their culinary and medicinal uses. Mint leaves are not only safe to eat but also widely used in culinary applications. They add a fresh and aromatic flavor to various dishes, desserts, beverages, and sauces. Mint is often used to make teas, salads, and garnishes. However, it's important to harvest mint from clean, pesticide-free environments. Mint leaves are a good source of vitamins A and C, as well as several minerals, including calcium and potassium. Menthol, the compound responsible for mint's characteristic cooling sensation, has various medicinal uses. Mint tea is often consumed to aid digestion and soothe upset stomachs. While mint is generally safe for consumption, it can sometimes be invasive in garden settings, spreading rapidly. It's advisable to plant mint in containers to control its growth. Mint is a versatile herb widely used in both culinary and medicinal applications. In addition to adding flavor to food and beverages, mint is known for its calming properties and is used in aromatherapy. It is also employed to relieve headaches and congestion. In summary, mint is a safe and versatile herb with a pleasant aroma and a wide range of uses. It is valued for its culinary, medicinal, and aromatic properties, making it a popular choice in gardens and kitchens around the world. When foraging or growing mint, it's important to do so responsibly, ensuring that the plant is sourced from clean environments and used in various delightful and beneficial ways.",
        "scientific_name": "Mentha spp. (various species, commonly Mentha piperita - Peppermint, and Mentha spicata - Spearmint)",
        "family": "Lamiaceae (Mint family)",
        "size": "Mint plants vary in size but generally grow low to the ground, reaching a height of about 1 to 3 feet (0.3 to 0.9 meters) depending on the specific species and growing conditions.",
        "safe_to_touch": "It is entirely safe to touch mint plants. They do not have any thorns or spines and are harmless to handle.",
        "safe_to_eat": "Mint leaves are not only safe to eat but also widely used in culinary applications. They add a fresh and aromatic flavor to various dishes, desserts, beverages, and sauces. Mint is often used to make teas, salads, and garnishes. However, it's important to harvest mint from clean, pesticide-free environments.",
        "nutritional_benefits": "Mint leaves are a good source of vitamins A and C, as well as several minerals, including calcium and potassium. Menthol, the compound responsible for mint's characteristic cooling sensation, has various medicinal uses. Mint tea is often consumed to aid digestion and soothe upset stomachs.",
        "caution": "While mint is generally safe for consumption, it can sometimes be invasive in garden settings, spreading rapidly. It's advisable to plant mint in containers to control its growth.",
    },
    "mint": {
        "description": "Mint, a member of the Lamiaceae family, is a popular aromatic herb known for its refreshing scent and flavorful leaves. There are several species within the Mentha genus, with peppermint (Mentha piperita) and spearmint (Mentha spicata) being the most common. Mint plants have square stems, opposite leaves, and small, tubular flowers in shades of white, pink, or purple. They are well-known for their culinary and medicinal uses. Mint leaves are not only safe to eat but also widely used in culinary applications. They add a fresh and aromatic flavor to various dishes, desserts, beverages, and sauces. Mint is often used to make teas, salads, and garnishes. However, it's important to harvest mint from clean, pesticide-free environments. Mint leaves are a good source of vitamins A and C, as well as several minerals, including calcium and potassium. Menthol, the compound responsible for mint's characteristic cooling sensation, has various medicinal uses. Mint tea is often consumed to aid digestion and soothe upset stomachs. While mint is generally safe for consumption, it can sometimes be invasive in garden settings, spreading rapidly. It's advisable to plant mint in containers to control its growth. Mint is a versatile herb widely used in both culinary and medicinal applications. In addition to adding flavor to food and beverages, mint is known for its calming properties and is used in aromatherapy. It is also employed to relieve headaches and congestion. In summary, mint is a safe and versatile herb with a pleasant aroma and a wide range of uses. It is valued for its culinary, medicinal, and aromatic properties, making it a popular choice in gardens and kitchens around the world. When foraging or growing mint, it's important to do so responsibly, ensuring that the plant is sourced from clean environments and used in various delightful and beneficial ways.",
        "scientific_name": "Mentha spp. (various species, commonly Mentha piperita - Peppermint, and Mentha spicata - Spearmint)",
        "family": "Lamiaceae (Mint family)",
        "size": "Mint plants vary in size but generally grow low to the ground, reaching a height of about 1 to 3 feet (0.3 to 0.9 meters) depending on the specific species and growing conditions.",
        "safe_to_touch": "It is entirely safe to touch mint plants. They do not have any thorns or spines and are harmless to handle.",
        "safe_to_eat": "Mint leaves are not only safe to eat but also widely used in culinary applications. They add a fresh and aromatic flavor to various dishes, desserts, beverages, and sauces. Mint is often used to make teas, salads, and garnishes. However, it's important to harvest mint from clean, pesticide-free environments.",
        "nutritional_benefits": "Mint leaves are a good source of vitamins A and C, as well as several minerals, including calcium and potassium. Menthol, the compound responsible for mint's characteristic cooling sensation, has various medicinal uses. Mint tea is often consumed to aid digestion and soothe upset stomachs.",
        "caution": "While mint is generally safe for consumption, it can sometimes be invasive in garden settings, spreading rapidly. It's advisable to plant mint in containers to control its growth.",
    },
    "Amanita": {
        "description": "Amanita species, belonging to the Amanitaceae family, are among the most perilous mushrooms in the world, responsible for 90 percent of mushroom-related fatalities. Recognizing them is crucial due to their deadly nature. Amanitas start as egg-shaped buttons, similar to small puffballs, which break open as they mature. Fully grown amanitas have gilled mushrooms with parasol-shaped caps in various colors such as white, yellow, red, or brown. They possess distinctive features:\n\nA saclike cup surrounds the stem base, often buried just beneath the soil surface and may not be easily noticeable.\nA ring encircles the stem.\nWhite gills.\nA white spore print.\n\nBoth the ring and the cup can be destroyed by rain or other disturbances. Therefore, novice mushroom hunters should avoid all parasol-shaped mushrooms with white gills.\nThis group includes numerous species, making them challenging to differentiate. Some notable names among amanitas include the destroying angel, fly agaric, yellow patches, blusher, grisette, ringless panther, death cap, and fool's mushroom.",
        "scientific_name": "Amanita spp. (about 600 species, worldwide)",
        "family": "Amanitaceae",
        "size": "The size of Amanita mushrooms varies significantly, contingent on the species and growing conditions.",
        "safe_to_touch": "It is generally safe to touch Amanita mushrooms with your hands, but it is essential to wash your hands thoroughly afterward. Some people might be sensitive or allergic to certain fungi, so it's a good practice to avoid unnecessary contact, especially if you are not familiar with specific species.",
        "safe_to_eat": "Eating Amanita mushrooms, especially without expert knowledge, is extremely dangerous and potentially deadly. As mentioned earlier, some Amanita species, such as the Death Cap mushroom (Amanita phalloides), are highly toxic and can cause severe liver and kidney damage, leading to death if ingested. Even experienced foragers can sometimes mistake deadly Amanita species for edible mushrooms, making it critical to have proper expertise before considering any wild mushroom for consumption.",
        "side_effects": {
            "digesting": "Ingesting Amanita mushrooms, particularly the poisonous species, can lead to a range of severe side effects, including nausea, vomiting, diarrhea, abdominal pain, and in severe cases, organ failure. The toxins present in these mushrooms can cause rapid and severe damage to internal organs, leading to a life-threatening situation.",
            "touching": "While touching Amanita mushrooms with your hands is generally safe, if you have an allergy or sensitivity to fungi, you might experience mild skin irritation or rash. It's advisable to wash your hands thoroughly after handling any wild mushrooms to remove any spores or residues that might cause irritation.",
        },
        "nutritional_benefits": "None",
        "caution": "In summary, Amanita mushrooms are a diverse group, and while some species are edible, many are highly toxic and potentially lethal if ingested. Extreme caution must be exercised, and it is recommended to consult with an expert mycologist or a knowledgeable forager before attempting to identify or consume any wild mushrooms, including those from the Amanita genus.",
    },
    "Basil": {
        "description": "Basil, scientifically known as Ocimum basilicum, is a fragrant herb belonging to the Mint family. It is widely cultivated around the world for its culinary and medicinal uses. Basil plants are recognized for their tender, green leaves that come in various sizes and shapes, depending on the variety. The leaves are often used fresh or dried in cooking due to their distinctive aroma and flavor, which is a combination of sweet, spicy, and slightly peppery notes.",
        "scientific_name": "Ocimum basilicum",
        "family": "Lamiaceae (Mint family)",
        "size": "Basil plants vary in size, ranging from small bushy varieties to larger, more robust plants, depending on the specific cultivar and growing conditions.",
        "safe_to_touch": "It is absolutely safe to touch basil plants. In fact, many people enjoy the tactile experience of rubbing the leaves to release their aromatic oils. Touching basil leaves is a common practice when harvesting the herb for culinary purposes.",
        "safe_to_eat": "Basil is not only safe to eat but also widely used in various cuisines around the world. Its leaves are edible and commonly used fresh in salads, sauces, pesto, and other dishes. Basil adds a delightful flavor and aroma to a wide range of recipes.",
        "nutritional_benefits": "Basil is not just a flavor-enhancing herb; it is surprisingly good for your health. It is an excellent source of vitamins K, A, and C, providing essential nutrients for overall well-being. Additionally, basil contains significant amounts of manganese, iron, calcium, and magnesium, essential minerals for various bodily functions. Furthermore, it contains omega-3 fatty acids, contributing to heart health and overall vitality. Given its nutritional richness, incorporating basil into your diet can provide numerous health benefits.",
        "caution": "There are generally no adverse side effects associated with consuming basil in moderate amounts as part of a balanced diet. However, individuals with basil allergies may experience allergic reactions. If you have a known allergy to plants in the Lamiaceae family, such as mint or oregano, it's advisable to avoid basil. Note: While basil itself is safe and nutritious, always be cautious about the sources of basil products you consume, especially if you have allergies, as cross-contamination or additives in processed foods could potentially cause adverse reactions. In summary, basil is not only a versatile and flavorful herb but also a nutritional powerhouse. It is safe to touch, eat, and enjoy in various dishes, providing essential vitamins, minerals, and other nutrients that contribute to your overall health and well-being.",
    },
    "Boletus": {
        "description": "Boletus, specifically the Bay Bolete variety, is a mushroom belonging to the Boletaceae family. This mushroom sports a fairly traditional appearance, making it easily confused with other species. The stem of the Bay Bolete is often a pale brown or yellow color and can be quite thick. The bulbous caps are dark rusty brown in color, while the flesh is an off-white hue.",
        "scientific_name": "Boletus spp. (including Bay Bolete species)",
        "family": "Boletaceae",
        "size": "Bay Bolete mushrooms come in various sizes, with caps ranging from small to large, and their height depends on the specific species and growing conditions.",
        "safe_to_touch": "It is generally safe to touch Bay Bolete mushrooms with your hands. However, even though they are a culinary delight, as with all wild mushrooms, it is essential to wash your hands thoroughly after handling them to remove any dirt or spores.",
        "safe_to_eat": "The Bay Bolete is one of the edible Boletus species and is considered a delicious delicacy. It is often used in cooking due to its excellent flavor and texture. However, because Bay Bolete mushrooms can be confused with other, potentially toxic species, it is crucial to be certain of the identification before consumption. Bay Bolete mushrooms are great for roasting as a side dish or addition to classic recipes. They can also be dried and enjoyed as a snack for later use.",
        "nutritional_benefits": "Contains very high fiber content. Hence, they can help keep your gut healthy and prevent constipation",
        "caution": "When properly identified, Bay Bolete mushrooms are generally safe to eat and are prized for their culinary uses. However, consuming misidentified mushrooms, especially those in the wild, can lead to adverse reactions. If you mistakenly consume a toxic species, symptoms can include nausea, vomiting, abdominal pain, and, in severe cases, organ failure. Therefore, it is essential to be absolutely certain of the mushroom's identity before consumption. In summary, the Bay Bolete is a delightful addition to culinary creations. Its traditional appearance and excellent flavor make it a sought-after ingredient in various dishes. However, proper identification is crucial, as confusing Bay Bolete with toxic species can have serious consequences. Foraging for wild mushrooms, including Bay Bolete, should only be done by those with expert knowledge or under the guidance of experienced mycologists to ensure safety and enjoyment.",
    },
    "Dandelion": {
        "description": "Dandelions, scientifically known as Taraxacum officinale, are common flowering plants in the Asteraceae family. They are recognizable for their bright yellow flowers and fluffy seed heads. Dandelion leaves are deeply toothed and form a rosette at the base of the plant. The plant is known for its hollow stems, milky latex, and taproot. Despite often being considered a weed, dandelions have a long history of culinary and medicinal use.",
        "scientific_name": "Taraxacum officinale",
        "family": "Asteraceae (Daisy family)",
        "size": "Dandelion plants vary in size but typically grow low to the ground in a rosette pattern. The height can range from a few inches to a foot or more, depending on the specific conditions.",
        "safe_to_touch": "It is completely safe to touch dandelion plants. They do not have any thorns or spines and are entirely harmless to handle.",
        "safe_to_eat": "Dandelions are not only safe to eat but also highly nutritious. Both the leaves and flowers of dandelion plants are edible and have culinary uses. Dandelion leaves are often used in salads, sandwiches, and cooked dishes. The flowers can be used to make dandelion wine or used as a garnish. Dandelion greens are rich in vitamins A, C, and K, as well as several minerals. However, it's crucial to harvest dandelions from areas free of pesticides and other contaminants.",
        "nutritional_benefits": "Dandelions are surprisingly nutritious. They are a good source of vitamins A and C, providing essential antioxidants that support overall health. Dandelion greens are also rich in vitamin K, which is vital for blood clotting and bone health. Additionally, they contain minerals such as calcium, iron, and potassium. Dandelion greens are often considered a valuable addition to a balanced diet.",
        "caution": "When consumed in moderate amounts, dandelions are generally safe for most people. However, some individuals might be allergic to dandelion pollen and could experience mild allergic reactions. As with any wild edible plant, it's important to ensure you are not allergic to dandelions before consuming them in larger quantities. Also, be cautious about harvesting dandelions from areas where herbicides or pesticides have been used. In summary, dandelions are safe to touch and eat, and they offer a range of nutritional benefits. They are a versatile wild edible plant that has been used for centuries in various culinary and medicinal applications. When foraging for dandelions, it's essential to do so responsibly and from clean, pesticide-free environments to ensure their safety and enjoy their health benefits.",
    },
    "Exidia": {
        "description": "Exidia glandulosa, commonly known as Black Jelly Roll, is a species within the Exidia genus, belonging to the Basidiomycota phylum. Its scientific name, Exidia glandulosa, is derived from 'glandul-' meaning 'gland' and '-osa' meaning 'an abundance of,' referring to the glands on the surface of the basidiocarp. This fungus forms irregular masses on decaying deciduous wood and is saprobic, meaning it feeds on dead organic matter. The individual fruit bodies are brainlike to irregularly contorted, gelatinous, and fuse together to form large masses. They are blackish-brown to olive-brown or black in color, with a shiny surface adorned with numerous small black-brown glandular dots.",
        "scientific_name": "Exidia glandulosa (Bull.) Fr.",
        "family": "Exidiaceae",
        "size": "None",
        "safe_to_touch": "It is generally safe to touch Exidia fungi. They are soft and gelatinous, posing no harm to humans upon contact. However, always wash your hands thoroughly after handling any wild fungi to remove spores and dirt.",
        "nutritional_benefits": "None",
        "safe_to_eat": "Exidia glandulosa is inedible and not recommended for consumption. Like many fungi, it should not be ingested due to the lack of widespread culinary use and the potential for confusion with toxic species.",
        "caution": "Consuming Exidia species is not recommended due to their inedible nature. Ingesting unidentified wild mushrooms, including Exidia fungi, can lead to gastrointestinal distress, nausea, vomiting, or other adverse reactions. Therefore, it is advisable to avoid consuming Exidia fungi or any wild mushrooms unless you are an experienced mycologist or under the guidance of an expert forager.",
    },
    "Fireweed": {
        "description": "Fireweed, scientifically known as Chamaenerion angustifolium, is a perennial herbaceous plant belonging to the Onagraceae family. It stands tall with slender stems, lance-shaped leaves, and striking pink to purple blossoms that adorn its frame during the summer months. Notably, fireweed earned its name for its tendency to emerge in areas after fires, its seeds carried widely by the wind.",
        "scientific_name": "Chamaenerion angustifolium",
        "family": "Onagraceae",
        "size": "Fireweed plants can vary in height, typically ranging from 3 to 7 feet (1 to 2 meters), depending on environmental conditions.",
        "Safe_to_touch": "Yes, Fireweed is safe to touch and handle.",
        "Safe_to_eat": "Fireweed is not only safe to touch but also edible and nutritious. Its leaves, stems, flowers, and roots are all edible, finding use in salads, teas, or as garnishes.",
        "nutritional_benefits": "Rich in vitamins and minerals such as A, C, calcium, iron, and magnesium, fireweed offers both culinary and potential health benefits.",
        "caution": "Fireweed should be harvested from clean environments, avoiding areas treated with pesticides or herbicides, to ensure its safety for consumption.",
    },
    "Lactarius": {
        "description": "Lactarius, commonly known as Milkcaps, is a genus of mushrooms within the Russulaceae family. These fungi are characterized by their distinctive feature: the exudation of a milky substance from their gills when touched or damaged. Lactarius species exhibit a wide range of colors, including white, yellow, orange, red, or purple. The cap shape, size, and texture also vary significantly, necessitating accurate identification for safe foraging.",
        "scientific_name": "Lactarius spp. (various species)",
        "family": "Russulaceae",
        "size": "Lactarius mushrooms come in various sizes, with caps ranging from small to large. The height depends on the species and growing conditions.",
        "safe_to_touch": "It is generally safe to touch Lactarius mushrooms. However, always wash your hands thoroughly after handling them to remove any latex residue.",
        "safe_to_eat": "Most Milkcaps exude a milky substance from their gills when touched or damaged. This latex can be acrid and hot, akin to the heat found in raw hot chilies. As a result, tasting Milkcaps directly is not advisable unless you are certain of the specific species and its edibility. Since many Milkcaps are toxic, it is crucial to refrain from consuming any fungi that release latex from the gills unless you are skilled in recognizing individual members of this family. Consuming toxic Milkcaps can lead to various symptoms, including nausea, vomiting, stomach cramps, and, in severe cases, organ failure. It is crucial to be absolutely certain of the mushroom's identity before considering consumption.",
        "nutritional_benefits": "None",
        "caution": "Identifying edible Milkcaps can be challenging, as the latex exudation diminishes as the mushrooms age. Younger mushrooms usually need to be found to aid accurate identification. Due to the potential toxicity of many Milkcaps, it is essential to avoid these mushrooms unless you are experienced in distinguishing between different species.",
    },
    # Add more plants as needed
}


# ================================================================================================================


class Plant(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.CameraUpdate = True  # Corrected variable name

        self.canvas = Canvas(
            self,
            bg="#0000FF",
            height=800,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)

        self.camera = cv2.VideoCapture(0)
        self.image_saved = False
        self.model_path = "frames/plant_stuff/best.pt"
        self.model = torch.hub.load(
            "frames/plant_stuff/yolov5", "custom", path=self.model_path, source="local"
        )

        # ====================================================================================================================
        # Changes Tariq Made/Added

        # Load in the Left Image of the panel:
        # Load the image
        image_path = "frames/plant_stuff/Left_Image.png"  # Replace this with the actual file path of your image
        self.left_image = Image.open(image_path)

        # Resize the image to your desired dimensions (width, height) with LANCZOS filter
        new_width = 280  # Replace this with your desired width
        new_height = 760  # Replace this with your desired height
        self.left_image = self.left_image.resize((new_width, new_height), Image.LANCZOS)

        self.left_photo = ImageTk.PhotoImage(self.left_image)

        # Left image label
        self.left_image_label = tk.Label(
            self,
            image=self.left_photo,
            borderwidth=0,  # Set borderwidth to 0 to remove the border
            highlightthickness=0,  # Set highlightthickness to 0 to remove the border
        )
        self.left_image_label.place(x=0, y=0)  # Adjust the coordinates as needed
        # ====================================================================================================================
        # Changes Tariq Made/Added

        # Load in the Right Image of the panel:
        # Load the image
        image_path = "frames/plant_stuff/Right_Image.png"  # Replace this with the actual file path of your image
        self.right_image = Image.open(image_path)

        # Resize the image to your desired dimensions (width, height) with LANCZOS filter
        new_width = 280  # Replace this with your desired width
        new_height = 760  # Replace this with your desired height
        self.right_image = self.right_image.resize(
            (new_width, new_height), Image.LANCZOS
        )

        self.right_photo = ImageTk.PhotoImage(self.right_image)

        # Right image label
        self.right_image_label = tk.Label(
            self,
            image=self.right_photo,
            borderwidth=0,  # Set borderwidth to 0 to remove the border
            highlightthickness=0,  # Set highlightthickness to 0 to remove the border
        )
        self.right_image_label.place(x=920, y=0)  # Adjust the coordinates as needed
        # ====================================================================================================================
        self.welcome_user = Text(
            self,
            wrap=tk.WORD,
            width=74,
            height=14,
            bg="#00FFFF",
            fg="#000000",
        )
        self.welcome_user.insert(
            tk.END,
            "\nWelcome to the Plant/Fungi Recognition Camera!\n\nPlease keep in mind that the accuracy of this model is close to Seventy-Five percent for all classes.\n\nSo make sure to be in a well-lit area before taking your picture. \n\nOtherwise, happy identifying and enjoy the outdoors!",
        )  # Insert initial text
        self.welcome_user.place(x=280, y=480, width=640, height=240)

        # Configure a tag for bold and center-aligned text
        self.welcome_user.tag_configure("bold", font=("Helvetica", 14, "bold"))
        self.welcome_user.tag_configure("center", justify="center")  # Center-align tag

        # Apply the bold and center-aligned tags to the entire text
        self.welcome_user.tag_add("bold", "1.0", "end")
        self.welcome_user.tag_add("center", "1.0", "end")

        self.welcome_user.config(state=tk.DISABLED)
        # ====================================================================================================================

        # capture button

        self.capture_button = tk.Button(
            self,
            text="Capture",
            command=self.capture_image,
            anchor="center",
        )
        self.capture_button.place(x=self.findCenterx(self.capture_button), y=730)

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

        self.image = Image.open("frames/plant_stuff/default_img.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.camera_image = self.camera_canvas.create_image(
            0, 0, anchor="nw", image=self.photo
        )

        # result_label

        # self.result_label = tk.Label(
        #     self, text="", font=("Helvetica", 12), foreground="black", bg="#AFAFAF"
        # )
        # self.result_label.place(x=self.findCenterx(self.result_label), y=500)

        # update camera

        self.update_camera()

        # self.result_label = tk.Label(
        #     self, text="", font=("Helvetica", 12, "bold"), foreground="black", bg="#AFAFAF"
        # )
        # self.result_label.place(x=self.findCenterx(self.result_label), y=500)

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
            self.capture_button.config(text="Take Another Picture?")
            self.capture_button.place(x=self.findCenterx(self.capture_button), y=730)

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

                        if predictions.numel() == 0:
                            raise Exception(
                                "\nPlease make sure to take image to where the background is bright enough.\n\nPlease try again."
                            )
                            print("test1")
                            self.plant_info_textbox.detroy()
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
                        self.plant_detected = f"{class_name}"
                    except Exception as e:
                        print("test2")
                        None

                    if self.result is not None:
                        print(self.plant_detected)  # for testing purposes

                        self.scrollbar = Scrollbar(self)
                        self.scrollbar.place(x=890, y=480, width=30, height=280)

                        # Create a Text widget
                        self.plant_info_textbox = Text(
                            self,
                            wrap=tk.WORD,  # Wrap text at word boundaries
                            yscrollcommand=self.scrollbar.set,  # Connect Text widget to the scrollbar
                        )
                        self.plant_info_textbox.place(
                            x=280, y=480, width=610, height=240
                        )

                        # Configure the scrollbar to work with the Text widget
                        self.scrollbar.config(command=self.plant_info_textbox.yview)

                        # Update the plant_info_textbox with the detected plant information
                        plant_name = (
                            self.plant_detected
                        )  # Assuming self.result contains the plant name
                        plant_info = plants.get(plant_name, {})

                        # Format plant information for display
                        formatted_info = f"Description: {plant_info.get('description', 'No information available.')}\n\n"
                        formatted_info += f"Scientific Name: {plant_info.get('scientific_name', 'N/A')}\n\n"
                        formatted_info += (
                            f"Family: {plant_info.get('family', 'N/A')}\n\n"
                        )
                        formatted_info += f"Size: {plant_info.get('size', 'N/A')}\n\n"
                        formatted_info += f"Safe to Touch: {plant_info.get('safe_to_touch', 'N/A')}\n\n"
                        formatted_info += (
                            f"Safe to Eat: {plant_info.get('safe_to_eat', 'N/A')}\n\n"
                        )
                        formatted_info += f"Nutritional Benefits: {plant_info.get('nutritional_benefits', 'N/A')}\n\n"
                        formatted_info += f"Caution: {plant_info.get('caution', 'N/A')}"

                        # Update the plant_info_textbox with the formatted plant information
                        self.plant_info_textbox.config(
                            state=tk.NORMAL
                        )  # Set the Text widget to normal state to allow editing
                        self.plant_info_textbox.delete(
                            1.0, tk.END
                        )  # Clear previous content
                        self.plant_info_textbox.insert(
                            tk.END, formatted_info
                        )  # Insert the new plant information
                        self.plant_info_textbox.config(
                            state=tk.DISABLED
                        )  # Set the Text widget to read-only state
                    else:
                        print("try again")
                    # Reset the image_saved flag to allow capturing another image
                    self.image_saved = False
        else:
            self.CameraUpdate = True

            self.capture_button.config(text="Capture")
            self.capture_button.place(x=self.findCenterx(self.capture_button), y=730)

            # self.result_label.config(text="")
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
