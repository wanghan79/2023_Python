import requests
from collections.abc import Iterable, Iterator

class WeatherIterator(Iterator):
    url = "http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671"
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    def getweather(self, city):
        response = requests.get(self.url)
        data = response.json()['data']
        for item in data:
            if item[0] == city:
                return f"{city}: high【{item[8]}】 ,low【{item[13]}】"
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getweather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterator(["北京","广州","长春"]):
   print(x)