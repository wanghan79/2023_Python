#chengly
"""
作业3要求：
使用迭代器实现城市天气数据的自动获取，以及相应的调用示例，主要考察点是自定义可迭代对象与相应迭代器的开发：
"""

"""
作业3代码部分展示：
"""
import requests
from collections.abc import Iterable, Iterator
url = "http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671"

def seach(city, list):
    for key in list:
        if key[0] == city:
            return key

class WeatherIterator(Iterator):
    def __init__(self,city):
        self.cities = city
        self.index = 0

    def getWeather(self, city):
        r = requests.get(url)
        data = r.json()['data']
        weather = seach(city, data)
        if weather == 0:
            return '请检查您输入的城市，区县名字是否正确或该城市，区县不在数据库'
        return '%s: 最高温【%s】 ,最低温【%s】 ' %(city, weather[8], weather[13])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index +=1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

"""
作业3结果部分展示：
"""
def show3():
    try:
        city = [u'西安',u'青岛',u'北京',u'长春']
        for weather in WeatherIterable(city):
            print(weather)
    except requests.exceptions.RequestException as e:
        print("程序发生异常：", e)
    else:
        print('程序执行成功!')

if __name__ == "__main__":
    show3()