import requests
import json
from collections.abc import Iterable,Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
        self.cityCode = open("城市编码表(1).json", encoding="utf-8")
        self.file = json.load(self.cityCode)

    def getWeather(self, city):
        code = 0
        for i in self.file['城市代码']:
            for j in i['市']:
                if j['市名'] == city:
                    code = j['编码']
        r = requests.get("http://t.weather.sojson.com/api/weather/city/" + code)
        data = r.json()['data']['forecast'][0]
        return '%s: %s ,%s ' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index +=1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)
def showWeather():
    for x in WeatherIterable([u'北京',u'上海',u'广州',u'长春']):
        print(x)

showWeather()
