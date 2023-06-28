from collections.abc import Iterator, Iterable
import requests as r

dict = {'北京':'101010100','上海':'101020100','广州':'101280101','长春':'101060101'}

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0
    def getWeather(selfs,city):
        url = r'http://t.weather.sojson.com/api/weather/city/'+dict[city]
        req = r.get(url)
        data = req.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city,data['low'],data['high'])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)

def weather_test():
    for x in WeatherIterable([u'北京',u'上海',u'广州',u'长春']):
        print(x)