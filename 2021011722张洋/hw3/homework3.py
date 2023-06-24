

import requests
from collections.abc import Iterable,Iterator

def search(**kwargs):
    for value in kwargs['data']:
        if value[0] == kwargs['city']:
            return value

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index=0

    def getWeather(self, city):
        r = requests.get(u'http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1686895900253&_=1686895783945'+city)
        data = r.json()['data']
        weather = search(city=city, data=data)
        return '%s: 最高温度： %s ,最低温度： %s' %(city,weather[8],weather[13])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index+=1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


#for x in WeatherIterable([u'连云港', u'北京' ,u'广州',u'长春']):
#   print(x)


def show():
    print("*********************Python 第三次作业***************************")
    print("使用迭代器实现城市天气数据的自动获取，主要考察点是自定义可迭代对象与相应迭代器的开发:")
    print("*********调用示例：")
    print("*********输入：[u'连云港', u'北京' ,u'广州',u'长春']")
    print("*********输出结果：")
    for x in WeatherIterable([u'连云港', u'北京', u'广州', u'长春']):
        print(x)

