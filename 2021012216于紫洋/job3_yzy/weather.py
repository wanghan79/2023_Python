import json
from typing import Iterator, Iterable

import requests as r

with open('../城市编码.json', 'r', encoding='UTF-8') as f:
    res = json.load(f)


class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# 未用到
def findError():
    raise MyException("未找到关于该城市的信息，请重新输入")


def getCode(city):
    list = res['城市代码']
    for index in list:
        cityLead = index['市']
        for c in cityLead:
            if c['市名'] == city:
                cityNumber = c['编码']
                return cityNumber
    print("没有此城市的信息，请重新输入一个,若一直错误想退出可以输入exit")
    return 0


class WeatherIterator(Iterator):

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(selfs, city):
        code = getCode(city)
        while code == 0:
            city = input()
            if code == "exit":
                break
            code = getCode(city)
        url = r'http://t.weather.sojson.com/api/weather/city/' + code
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


def run():
    ask = list()
    print("请输入你想要查询的城市：(输入0结束查询，按回车输入下一个城市)")
    while True:
        city = input().strip()
        if city == '0':
            break
        else:
            ask.append(city)
    print("正在查询......")
    try:
        for x in WeatherIterable(ask):
            print(x)
    except Exception:
        print("请求过于频繁，请稍后重试")


if __name__ == '__main__':
    run()
