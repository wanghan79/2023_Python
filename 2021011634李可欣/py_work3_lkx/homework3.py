import requests
from collections.abc import Iterable,Iterator

def find(city, list):
    for key in list:
        if key[0] == city:
            return key
    return 0

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        r = requests.get("http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671")
        data = r.json()['data']
        weather = find(city, data)
        return '%s: 低温:%s℃ ,高温:%s℃ ' %(city, weather[13], weather[8])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index +=1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable([u'北京',u'长春',u'广州','天津']):
    print(x)