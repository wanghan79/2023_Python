import requests
from collections.abc import Iterable, Iterator


class WeatherIterator(Iterator):
    url = "http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671"

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(self.url)
        data = r.json()['data']
        for item in data:
            if item[0] == city:
                return f"{city}: high【{item[8]}】 ,low【{item[13]}】"

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




def out_3():
    for x in WeatherIterable([u'北京', u'河南', u'广州', u'长春', u'杭州']):
        print(x)

if __name__ == '__main__':
    out_3()