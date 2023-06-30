import requests
from collections.abc import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(
            u'https://restapi.amap.com/v3/weather/weatherInfo?key=da8fa78adb6d1fc873b1e20e83c321fe&city=' + city + '&extensions=base')
        data = r.json()['lives'][0]
        return '城市:{}; 天气:{}; 温度:{};'.format(data['city'], data['weather'], data['temperature'],
                                                             )

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


def weather_test():
    for x in WeatherIterable([u'北京',u'上海',u'广州',u'长春']):
        print(x)

if __name__ == "__main__":
    weather_test()