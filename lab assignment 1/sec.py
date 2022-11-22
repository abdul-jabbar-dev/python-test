import requests
import math
import time
url = "https://api.openweathermap.org/data/2.5/weather?appid=a6a8b8f7e4078905cd73727c1b86e3b1&q=dhaka"

res = requests.get(url)
res = res.json()


def getResponse():
    res = requests.get(url)
    res = res.json()
    return res


def weather_data():
    response = getResponse()
    temp = (math.ceil(response['main']['temp']-273.15))
    loca = f"{response['name']}, {response['sys']['country']}"
    weat_data = response['weather'][0]['main']
    print(f"Temperature in Celsius = {temp}")
    print(f"Location = {loca}")
    print(f"Weather atmospheric = {weat_data}")
    print()


while True:
    weather_data()
    time.sleep(1800)
