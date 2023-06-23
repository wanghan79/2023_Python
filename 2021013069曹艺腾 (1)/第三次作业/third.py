import json

import requests
from collections.abc import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
        self.f = open("城市编码表.json", encoding="utf-8")
        self.cityCode = json.load(self.f)


    def getWeather(self, city):
        code = ""
        for province in self.cityCode['城市代码']:
            for muni in province['市']:
                if muni['市名'] == city:
                    code = muni['编码']
                    break

        if code == "":
            return "The city " + city + " was not found..."
        r = requests.get("http://t.weather.sojson.com/api/weather/city/" + code)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' %(city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, *cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def test():
    for x in WeatherIterable(u'北京', u'上海', u'广州', u'长春'):
        print(x)


if __name__ == "__main__":
    for x in WeatherIterable(u'北京', u'上海', u'广州', u'长春'):
        print(x)
