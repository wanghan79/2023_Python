import urllib.request
from collections.abc import Iterable, Iterator
import json


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        city_code = cityDictionary.get(city)
        if city_code:
            r = urllib.request.urlopen('http://t.weather.sojson.com/api/weather/city/' + city_code)
            data = r.read().decode('utf-8')
            data = json.loads(data)['data']['forecast'][0]
            return '%s:%s,%s' % (city, data['low'], data['high'])
        else:
            return '%s: City code not found' % city

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


cityDictionary = {
    "长春": "101060101",
    "成都": "101270101",
    "厦门": "101230201",
    "广州": "101280101",
    "上海": "101020100",
    "石家庄": "101090101",
    "郑州": "101180101",
    "杭州": "101210101"
}

for x in WeatherIterable(["长春"]):
    print(x)
