import requests
from collections.abc import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        cityCode = city_Dict.get(city)
        r = requests.get(u'http://t.weather.sojson.com/api/weather/city/' + cityCode)
        data = r.json()['data']['forecast'][0]
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


city_Dict = {
    "长春": "101060101",
    "成都": "101270101",
    "自贡": "101270301",
    "绵阳": "101270401",
    "南充": "101270501",
    "达州": "101270601"
}

for x in WeatherIterable(["成都"]):
    print(x)
