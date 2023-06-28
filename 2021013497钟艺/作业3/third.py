#import requests
from collections import Iterable,Iterator
class WeatherIterator(Iterator):
    def _init_(self,cities):
        self.cities = cities
        self.index = 0
    def getWeather(self,city):
        r = request.get(u'http://wthrcdn.etouch.cn/weather_min?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s,%s '%(city,data['low'],data['high'])
    def _next_(self):
        if self.index == len(self.cities):
            raise stopIteration
        city = self.cities[self.index]
        self.index +=1
        return self.getWeather(city)
class WeatherIterable(Iterable):
    def _init_(self,cities):
        self.cities = cities
    def _iter_(self):
        return WeatherIterator(self.city)
for x in WeatherIterable([u'北京',u'上海',u'广州',u'长春']):
    print(x)