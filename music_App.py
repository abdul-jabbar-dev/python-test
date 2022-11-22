import requests
from functools import cache


class Music:
    def __init__(self, url, api_key):
        self.__secret_key = api_key
        self.url = url

    def search(self):
        search = input('Enter your search: ')
        self.get_data(search)

    @cache
    def get_data(self, value):
        url = f"{self.url}/search?q={value}"
        header = {
            "apikey": self.__secret_key
        }
        res = requests.get(url, headers=header)
        res = res.json()
        for i, data in enumerate(res['albums']['items']):
            song_name = data['data']['name']
            artist_name = data['data']['artists']['items'][0]['profile']['name']
            song_uri = data['data']['uri']
            print(song_name)


spotify = Music("https://api.apilayer.com/spotify",
                "US56cyVX0QwlYwWYI1hfTa2QK5EKAAaI")
spotify.search()
