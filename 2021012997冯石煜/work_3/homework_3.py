#Feng shiyu
import requests
import json
from collections.abc import Iterable,Iterator
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        with open('城市编码表.json', mode='r', encoding='UTF-8') as f:
            dic = json.load(f)
            list = dic['城市编码']
            for index in list:
                cities1 = index['市']
                for c in cities1:
                    if c['市名'] == city:
                        cityNumber = c['编码']
        r = requests.get(u'http://t.weather.sojson.com/api/weather/city/'+cityNumber)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])
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

if __name__ == '__main__':
    for x in WeatherIterable(['北京', '长春', '广州', '上海']):
        print(x)