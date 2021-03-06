import requests
import json
from time import sleep

class vid:
    def __init__(self, channelId, key):
        self.url = "https://www.googleapis.com/youtube/v3/search"
        self.params = dict(part="snippet", channelId=channelId, key=key, maxResults=1, order="date")

    def getvid(self):
        data = requests.get(self.url, self.params)
        return data.json()
    
    def parsevid(self):
        data = self.getvid()
        if data.get("items", "error") == "error":
            with open("log.json", "a") as f:
                f.write(json.dumps(data) + "\n")
                return ["Error please check logs", "Error please check logs", "Error please check logs"]
        else:
            with open("log.json", "a") as f:
                f.write(json.dumps(data) + "\n")
        id: str = data["items"][0]["id"]["videoId"]
        title: str = data["items"][0]["snippet"]["title"]
        ptime: str = data["items"][0]["snippet"]["publishedAt"]
        return [id, title, ptime]

if __name__ == "__main__":
    with open("data.json", "r") as f:
        data = json.loads(f.read())
    getvideo = vid(data["id"], data["key"])
    print(getvideo.parsevid())