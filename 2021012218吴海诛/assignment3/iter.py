"""
    Author:Haizhu.Wu
    Title:Assignment3
"""
import requests
import json
with open("城市编码表.json", 'r', encoding='UTF-8') as file:
    data = json.loads(file.read())
    data = data.get('城市代码')
from collections.abc import Iterator, Iterable
# 找到城市对应的编码
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
        r = requests.get(u'http://t.weather.sojson.com/api/weather/city/'+getcode(city))
        data = r.json()['data']['forecast'][0]
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

def show():
    for x in WeatherIterable(['北京','上海','广州','长春','郑州']):
        print(x)

if __name__ == "__main__":
    show()