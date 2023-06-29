import requests
from collections.abc import Iterable, Iterator

def getWeather(city):
    r = requests.get(u'http://t.weather.sojson.com/api/weather/city/' + city)
    data = r.json()['data']['forecast'][0]
    city_name = r.json()['cityInfo']['city']
    return '%s : %s , %s' % (city_name,  data['low'], data['high'])

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

def test_weather():
    for x in WeatherIterable([u'101010100', u'101020100', u'101280101', u'101060101']):
        print(x)
