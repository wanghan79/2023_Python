import requests

from collections.abc import Iterable,Iterator

url="http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671"

def seach(city, list):
    for key in list:
        if key[0] == city:
            return key
    return 0

class WeatherIterator(Iterator):
    def __init__(self,city):
        self.cities = city
        self.index = 0

    
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
def show():
    city = [u'哈尔滨',u'长春',u'沈阳',u'深圳']
    for weather in WeatherIterable(city):
        print(weather)