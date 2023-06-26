import json
from typing import Iterator, Iterable

import requests as r


def get_data():
    with open('weather/城市编码.json', 'r', encoding='UTF-8') as f:
        return json.loads(f.read()).get('城市代码')


# 打开文件
p_dict = get_data()


# 找到城市对应的编码
def getcode(city):
    for x in p_dict:
        for y in x.get('市'):
            if y.get('市名') == city:
                return y.get('编码')
    print("输入城市名有误")
    return "0"


class WeatherIterator(Iterator):

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(selfs, city):
        code = getcode(city)
        if code == '0':
            return '无数据'
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


def func(struct):
    try:
        for x in WeatherIterable(struct):
            print(x)
    except Exception as result:
        print('异常的基本信息是：', result)
        print('短时间访问链接过于频繁，远程主机强迫关闭了连接，请稍后再试')
        return


def city_input():
    cities = list()
    while True:
        city = input("请输入你想要查询的城市：(输入end结束查询)").strip()
        if city == 'end':
            break
        else:
            cities.append(city)
    print("你的输入是：", cities)
    return cities
