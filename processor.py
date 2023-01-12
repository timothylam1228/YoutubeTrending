from PIL import Image, ImageDraw, ImageFont
import numpy as np
import json
import urllib.request
from data import Data
import pathlib

# path to temp folder


THUMBNAIL_TEMP_PATH = "./temp"


class Processor:
    def __init__(self, data):
        self.data = data
        self.backgroundImage = "assets/background.png"
        self.font = ImageFont.truetype(
            "assets/SofiaSans-VariableFont_wght.ttf", size=20
        )
        self.image = Image.open(self.backgroundImage)
        self.drawImage = ImageDraw.Draw(self.image)
        self.thumbnail = None

    def generate_image(self):
        img = Image.open(self.backgroundImage)
        I1 = ImageDraw.Draw(img)
        I1.text((28, 36), "Daily Trending YouTube Video", fill=(255, 0, 0))
        I1.text((28, 50), self.data.get_video_data(0)["title"], "blue", font=self.font)
        img.save("car2.png")

    def add_header(self):
        self.drawImage.text((28, 36), "Daily Trending YouTube Video", fill=(255, 0, 0))
        self.image.save("result/temp.png")

    def add_thumbnail(self):
        self.thumbnail = self.data["thumbnail"]
        resource = urllib.request.urlretrieve(self.thumbnail, "temp/test.png")
        thumbnail = Image.open("temp/test.png")
        self.image.paste(thumbnail, (20, 20))
        self.image.save("car2.png")
