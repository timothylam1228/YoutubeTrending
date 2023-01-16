import os
import numpy as np
import json
import urllib.request
from data import Data
from processor import Processor

SAVE_FOLDER = "result"


def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    f = open("data.json", encoding="utf-8")
    json_data = json.load(f)
    data = Data(json_data)
    for i in range(0, 1):
        final_result = Processor(data.get_video_data(i), i + 1)
        final_result.generate_image()


main()
