from PIL import Image, ImageDraw, ImageFont
import numpy as np
import json
import urllib.request
from data import Data
from processor import Processor


def main():
    f = open("data.json", encoding="utf-8")
    json_data = json.load(f)
    data = Data(json_data)
    for i in range(0, 9):
        final_result = Processor(data.get_video_data(i), i + 1)
        final_result.generate_image()


main()
