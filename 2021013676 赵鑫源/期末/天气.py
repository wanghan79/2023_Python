import requests

import json

from collections import Iterable,Iterator


def getData():
    with open('城市编码表.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    element = {}
    for i in data['城市代码']:
        for j in i['市']:
            element[j['市名']] = j['编码']
    return element


class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getWeather(self,city):
        r = requests.get('http://t.weather.sojson.com/api/weather/city/'+getData()[city])
        data = r.json()['data']['forecast'][0]
        return '%s : %s,%s' % (city,data['low'],data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)



if __name__ == '__main__':
    for x in WeatherIterable([u'北京', u'上海', u'广州', u'长春', u'漯河', u'郑州']):
        print(x)


