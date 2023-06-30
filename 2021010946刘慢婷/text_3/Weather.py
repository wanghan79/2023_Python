import requests
from collections.abc import Iterable,Iterator

def research(**kwargs):
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
        weather = research(city=city, data=data)
        return '%s: 最高温： %s°C ,最低温： %s°C,天气状况：%s' %(city,weather[8],weather[13],weather[6])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index = self.index + 1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

def weather_3():
    print("Python第三次作业：使用迭代器实现城市天气数据的自动获取，以及相应的调用示例。")
    print("*******************获取结果如下：***********************")


    for x in WeatherIterable([u'宁波',u'杭州',u'广州',u'长春',u'北京']):
          print(x)

if __name__ == '__main__':
    weather_3()