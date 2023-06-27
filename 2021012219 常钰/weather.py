import urllib.request
from collections.abc import Iterable, Iterator
import json


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        # 打开一个URL并返回一个文件对象
        r = urllib.request.urlopen('http://t.weather.sojson.com/api/weather/city/' + urllib.parse.quote(city.encode('utf-8')))
        # 使用read方法读取文件内容，并使用decode方法将字节转换为字符串
        data = r.read().decode('utf-8')
        data = json.loads(data)['data']['forecast'][0]
        return '%s: %s ,%s ' % (city, data['low'], data['high'])

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


for x in WeatherIterable([u'101060101']):
    print(x)
