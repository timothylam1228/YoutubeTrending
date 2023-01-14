from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
import json
import urllib.request
from data import Data
import pathlib
import math
import uuid
import textwrap

# path to temp folder


THUMBNAIL_TEMP_PATH = "./temp"


class Processor:
    def __init__(self, data, number):
        self.data = data
        self.backgroundImage = "assets/background.png"
        self.rank_font = ImageFont.truetype(
            "assets/Roboto-Bold.ttf",
            size=25,
        )
        self.font = ImageFont.truetype("assets/Roboto-Bold.ttf", size=15)
        self.channel_font = ImageFont.truetype("assets/Roboto-Bold.ttf", size=18)
        self.image = Image.open(self.backgroundImage)
        self.drawImage = ImageDraw.Draw(self.image)
        self.thumbnail = None
        self.thumbnail_size = None
        self.number = number
        self.width, self.height = 512, 512

    def generate_image(self):
        self.add_header()
        self.add_thumbnail()
        self.add_like()
        self.add_view_count()
        self.add_channel_title()
        self.image.save(
            ("result/{number} - {i}.png").format(number=self.number, i=uuid.uuid4())
        )

    def add_header(self):
        title_start_position = 115
        self.data["title"] = "Top" + str(self.number) + ". " + self.data["title"]
        new_header = textwrap.wrap(self.data["title"], width=45)
        if len(new_header) >= 3:
            new_header = new_header[:2]
            new_header[1] = new_header[1] + "..."

        if len(new_header) == 1:
            title_start_position = 125

        line_heigh = 0
        self.drawImage.text(
            (50, 60),
            ("#" + str(self.number)),
            fill=(230, 210, 225),
            font=self.rank_font,
            align="center",
        )
        for i in new_header:
            self.drawImage.text(
                (85, title_start_position + (line_heigh * 20)),
                (i),
                fill=(0, 0, 0),
                font=self.font,
                align="center",
            )
            line_heigh = line_heigh + 1

    def add_thumbnail(self):
        self.thumbnail = self.data["thumbnail"]
        urllib.request.urlretrieve(self.thumbnail, "temp/test.png")
        thumbnail = Image.open("temp/test.png")
        thumbnail_width, thumbnail_height = thumbnail.size
        # Resize image and keep aspect ration
        thumbnail = thumbnail.resize(
            (math.floor(thumbnail_width * 1), math.floor(thumbnail_height * 1)),
            Image.ANTIALIAS,
        )
        thumbnail = ImageOps.expand(thumbnail, border=2, fill=(230, 210, 225))

        self.thumbnail_size = thumbnail.size
        self.image.paste(
            thumbnail,
            (
                int((512 - self.thumbnail_size[0]) / 2),
                int(512 / 1.4 - self.thumbnail_size[1]),
            ),
        )
        pathlib.Path("temp/test.png").unlink()

    def add_like(self):
        self.drawImage.text(
            (280, 380),
            ("Likes: " + self.decminal_to_string(self.data["likeCount"])),
            (180, 115, 180),
            font=self.channel_font,
            align="center",
        )

    def add_view_count(self):
        self.drawImage.text(
            (280, 420),
            ("Views: " + self.decminal_to_string(self.data["viewCount"])),
            (180, 115, 180),
            font=self.channel_font,
            align="center",
        )

    def add_channel_title(self):
        # CHECK TEXT WIDTH
        new_title = textwrap.wrap(self.data["channelTitle"], width=15)
        if len(new_title) >= 2:
            self.channel_font = ImageFont.truetype("assets/Roboto-Bold.ttf", size=15)
        line_height = 0
        for i in new_title:
            self.drawImage.text(
                (
                    int((512 - self.thumbnail_size[0]) / 2),
                    int(512 - self.thumbnail_size[1] / 1.5 + line_height * 20),
                ),
                i,
                (180, 115, 180),
                font=self.channel_font,
            )
            line_height = line_height + 1

    def decminal_to_string(self, number):
        return "{:,}".format(int(number))
