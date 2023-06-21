import requests
from collections.abc import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
        self.api_key = 'd31d61e7322f9b76fe4e4f0a384b58cf'

    def getCoordinates(self, city):
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={self.api_key}'
        r = requests.get(url)
        data = r.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            return None, None

    def getWeather(self, lat, lon):
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={self.api_key}&lang=zh_cn&units=metric'
        r = requests.get(url)
        data = r.json()
        weather_info = data['list'][0]['weather'][0]
        temp = data['list'][0]['main']['temp']
        return f"{weather_info['description']}，温度{temp}°C"

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        lat, lon = self.getCoordinates(city)
        self.index += 1
        if lat is not None:
            return f"{city}: {self.getWeather(lat, lon)}"
        else:
            return f"{city}: 无法获取天气信息"


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

def working(city):
    for x in WeatherIterable(city):
        print(x)


if __name__=="__main__":
    city = input("输入：").split()
    working(city)