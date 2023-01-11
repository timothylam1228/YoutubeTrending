class Data:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def get_video_data(self, number):
        response = {
            "title": self.data[number]['snippet']['title'],
            "thumbnail" : self.data[number]['snippet']['thumbnails']['default']['url'],
            "channelTitle": self.data[number]['snippet']['channelTitle'],
            "viewCount": self.data[number]['statistics']['viewCount'],
            "likeCount": self.data[number]['statistics']['likeCount'],
        }
        return response

   