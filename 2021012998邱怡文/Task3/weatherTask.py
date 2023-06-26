import requests
from collections.abc import Iterable,Iterator
class WeatherIterator(Iterator ):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getWeather(self,city):
        r = requests.get(u'http://t.weather.sojson.com/api/weather/city/'+ city)
        # print(r.url)
        # print(r.text)
        data = r.json()['data']['forecast'][0]
        cityInfo = r.json()['cityInfo']
        # print(data)
        return '%s  %s: %s: %s: ' % (cityInfo["city"],cityInfo['citykey'],data['high'], data['low'])

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

for x in WeatherIterable([u'101270101','101270301','101120901','101060101']):
    print(x)

