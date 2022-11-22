import ctypes
import requests
import json
from pathlib import Path
api_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'


response = requests.get(api_url)
content = response.content.decode('UTF-8')
parse = json.loads(content)
url = parse['url']

res = requests.get(url)
with open('image.png', 'wb') as image:
    image.write(res.content)


# set as wallpaper

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, f'{Path().absolute()}\image.png' , 0)