class Data:
    def __init__(self, data):
        self.data = data
        self.thumbnail_size = "medium"

    def get_data(self):
        return self.data

    def get_video_data(self, number):

        response = {
            "title": self.data[number]["snippet"]["title"],
            "thumbnail": self.data[number]["snippet"]["thumbnails"][
                self.thumbnail_size
            ]["url"],
            "channelTitle": self.data[number]["snippet"]["channelTitle"],
            "viewCount": self.data[number]["statistics"]["viewCount"],
            "likeCount": self.data[number]["statistics"]["likeCount"],
            "thumbnail_size": (320, 180),
        }
        return response
