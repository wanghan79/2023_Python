import json
import requests
from collections.abc import Iterable,Iterator


def getData():
    with open('cityData.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get('http://t.weather.sojson.com/api/weather/city/'+str(getData()[city]))
        data = r.json()
        return '%s: %s,%s' % (city,data["data"]["forecast"][0]["high"], data["data"]["forecast"][0]["low"])

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


class show:
    def __init__(self):
        self.name = 'weather'
    def show(self,a):
        for x in WeatherIterable(a):
            print(x)

if __name__ == '__main__':
    hw03 = show()
    a = ['北京', '长春']
    hw03.show(a)
