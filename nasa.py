import requests
from datetime import date, timedelta


class NasaAPI:
    def __init__(self, api_key: str):
        self.key = api_key

    def get_pictures(self, from_when: date, thumbs: bool, download_image: bool):
        request_url = f"https://api.nasa.gov/planetary/apod"
        request_url += f"?api_key={self.key}"
        request_url += f"&thumbs={thumbs}"
        request_url += f"&date={from_when.strftime('%Y-%m-%d')}"

        try:
            response = requests.get(request_url)
            response.raise_for_status()
            json = response.json()

            if download_image:
                src = json["url"]
                if json["media_type"] == "video":
                    src = json["thumbnail_url"]

                image = requests.get(src)
                with open("/tmp/image.png", "wb") as f:
                    f.write(image.content)

            return json
        except Exception as e:
            print(f"Something went wrong while fetching data from NASA's API! Error: {e}")
