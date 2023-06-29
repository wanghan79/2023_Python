import requests
from collections.abc import Iterable, Iterator

url = "http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671"

def seach(city, list):
    for item in list:
        if item[0] == city:
            return item

class WeatherIterator(Iterator):
    def __init__(self,city):
        self.cities = city
        self.index = 0

    def getWeather(self, city):
        r = requests.get(url)
        data = r.json()['data']
        weather = seach(city, data)
        if weather == 0:
            return '输入错误'
        return '%s: 最高温: %s ,最低温: %s, 风象: %s ' %(city, weather[8], weather[13], weather[10])

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

def showeater():
    try:
        city = [u'东莞', u'廊坊', u'北京', u'长春']
        for weather in WeatherIterable(city):
            print(weather)
    except requests.exceptions.RequestException as e:
        print("程序发生异常：", e)
    else:
        print('天气预报成功')

showeater()
