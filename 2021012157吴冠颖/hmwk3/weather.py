import urllib.request
from collections.abc import Iterable, Iterator
import json


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = urllib.request.urlopen(
            'http://t.weather.sojson.com/api/weather/city/' + urllib.parse.quote(city.encode('utf-8')))
        data = r.read().decode('utf-8')
        data = json.loads(data)['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])

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


def putWeather():
    for x in WeatherIterable([u'101010100', u'101020100', u'101280101', u'101280601', u'101060101']):
        print(x)
if __name__ == '__main__':
    putWeather()

