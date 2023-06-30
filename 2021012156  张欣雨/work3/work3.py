import requests
from collections.abc import Iterable,Iterator
def seach(city, list):
    for key in list:
        if key[0] == city:
            return key
    return 0
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
    def run():
    city = [u'北京',u'上海',u'广州',u'深圳']
    for weather in WeatherIterable(city):
        print(weather)
if __name__ == '__main__':
    show()
