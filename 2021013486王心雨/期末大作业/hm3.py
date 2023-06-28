"""
@Content: python大作业
            使用迭代器实现城市天气数据的自动获取，以及相应的调用示例，主要考察点是自定义可迭代对象与相应迭代器的开发，，
"""
import json
import requests
from collections.abc import Iterable, Iterator
# from collections.abc import interable


class WeatherIterator(Iterator):
    # 继承可迭代的对象
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
        # 读取城市编码表文件
        self.f = open("城市编码表.json", encoding="utf-8")
        self.cityCode = json.load(self.f)


    def getWeather(self, city):
        code = ""
        for i in self.cityCode['城市代码']:
            for name in i['市']:
                if name['市名'] == city:
                    code = name['编码']
                    break
        if code == "":
            return "The city " + city + " was not found..."
        r = requests.get("http://t.weather.sojson.com/api/weather/city/" + code)
        data = r.json()['data']['forecast'][0]
        return '{0}: {1}, {2}'.format(city, data['low'], data['high'])

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


def show():
    cities = ['北京', '长春', '重庆']
    for x in WeatherIterable(*cities):
        print(x)



try:
    show()
except Exception:
    pass
