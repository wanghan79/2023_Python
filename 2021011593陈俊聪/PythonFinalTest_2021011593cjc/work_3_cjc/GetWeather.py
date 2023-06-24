# 迭代器 第三次作业
# 获取天气数据
# import requests
# from collections import Iterable,Iterator
# class WeatherIterator(Iterator):
#     def __init__(self,cities):
#         self.cities = cities
#         self.index  = 0
#     def getWeather(self,city):
#         r = requests.get(u'https://www.tianqi.com/'+city+'/')
#         data = r.json()['data']['forecast'][0]
#         return '%s: %s, %s ' % (city,data['low'],data['high'])
#
#     def __next__(self):
#         if self.index == len(self.cities):
#             raise StopIteration
#         city = self.cities[self.index]
#         self.index += 1
#         return self.getWeather(city)
#
# class WeatherIterable(Iterable):
#     def __init__(self,cities):
#         self.cities = cities
#
#     def __iter__(self):
#         return WeatherIterator(self.cities)
#
# for x in WeatherIterable([u'beijing',u'shanghai',u'guangzhou',u'changchun']):
#     print(x)

from collections.abc import Iterator, Iterable
import requests as r
import json

with open("城市编码表.json", 'r', encoding='UTF-8') as f:
    data = json.loads(f.read())
    data = data.get('城市代码')


def getcode(city):
    for x in data:
        for y in x.get('市'):
            if y.get('市名') == city:
                return y.get('编码')


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        url = r'http://t.weather.sojson.com/api/weather/city/' + getcode(city)
        req = r.get(url)
        data = req.json()['data']['forecast'][0]
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

def example(city):
    for data in WeatherIterable([city]):
        print(data)


# # 北京 上海 广州 长春
# for x in WeatherIterable(['北京', '上海', '广州', '长春']):
#     print(x)
