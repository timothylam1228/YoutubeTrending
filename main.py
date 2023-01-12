from PIL import Image, ImageDraw, ImageFont
import numpy as np
import json
import urllib.request
from data import Data
from processor import Processor

# img = Image.open('background.png')


# font = ImageFont.truetype("SofiaSans-VariableFont_wght.ttf", size=20)

# # Call draw Method to add 2D graphics in an image
# I1 = ImageDraw.Draw(img)

# # Add Text to an image
# f = open('data.json',encoding="utf-8")
# data = json.load(f)
# print(data[0])
# I1.text((28, 36), "Daily Trending YouTube Video" ,fill=(255, 0, 0))
# I1.text((28,50),data[0]['snippet']['title'],'blue',font=font)
# # I1.text((28,50),data[0]['snippet']['thumbnails']['default'],'blue',font=font)
# thumbnail = data[0]['snippet']['thumbnails']['default']['url']
# # resource = urllib.request.urlretrieve(thumbnail,"test.png")

# # Display edited image
# # img.show()

# # Save the edited image
# img.save("car2.png")


def get_thumbnail_to_temp_folder(number):
    f = open("data.json", encoding="utf-8")
    data = json.load(f)
    # for i in data:
    thumbnail = data[0]["snippet"]["thumbnails"]["default"]["url"]
    resource = urllib.request.urlretrieve(thumbnail, ("test{i}.png").format(0))


def main():
    f = open("data.json", encoding="utf-8")
    json_data = json.load(f)
    data = Data(json_data)
    final_result = Processor(data.get_video_data(0))
    final_result.add_header()
    final_result.add_thumbnail()


main()
