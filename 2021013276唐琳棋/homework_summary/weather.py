# -*- coding: utf-8 -*-
"""
# @Time        : 2023/6/30 16:55
# @Author      : tanliqiu
# @FileName    : weather.py
# @Software    : PyCharm
# @ProjectName : python_homework
# @Description : null
"""
import json
import requests
# from collections import Iterable,Iterator
from collections.abc import Iterable,Iterator

def GetData():
    with open('city.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getWeather(self,city):
        r = requests.get('http://t.weather.sojson.com/api/weather/city/'+str(GetData()[city]))
        data = r.json()['data']['forecast'][0]
        # return '%s:%s,%s' % (city, data[0], data[1])
        return '%s:%s,%s' % (city,data['low'],data['high'])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index+=1
        return  self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)




class show:
    def __init__(self):
        self.name = 'weather'
    def show(self,a):
        for x in WeatherIterable(a):
            print(x)

if __name__ == '__main__':
    test3 = show()
    a = ['北京', '长春','上海','重庆']
    test3.show(a)