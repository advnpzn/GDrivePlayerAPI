import requests
from GDrivePlayer.exceptions import StatusCodeError


class GDrivePlayer:

    url_anime = "https://api.gdriveplayer.us/v1/animes/"
    url_movie = "https://api.gdriveplayer.us/v1/movie/"
    url_drama = "https://api.gdriveplayer.us/v1/drama/"
    url_series = "https://api.gdriveplayer.us/v2/series/"

    def request(self, url: str):
        try:
            res = requests.get(url)
            if res.status_code != 200:
                raise StatusCodeError
            else:
                return res.text
        except Exception as e:
            print(e)
            exit
        

