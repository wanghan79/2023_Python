import urllib.request
from collections.abc import Iterable, Iterator
import json


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        # 使用 urllib.request.urlopen 打开一个 URL 并返回一个文件对象
        cityCode = cityDictionary.get(city)
        if cityCode:
            r = urllib.request.urlopen('http://t.weather.sojson.com/api/weather/city/' + cityCode)
            # 使用 read 方法读取文件对象的内容，并使用 decode 方法将字节转换为字符串
            data = r.read().decode('utf-8')
            # 使用 json.loads 方法将字符串转换为 JSON 对象，并从中提取所需的数据
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
    "北京": "101010100",
    "上海": "101020100",
    "广州": "101280101",
    "深圳": "101280601",
    "长春": "101060101",
}

# 北京，上海，广州，深圳，长春
for x in WeatherIterable(['北京', '上海', '广州', '深圳', '长春']):
    print(x)
