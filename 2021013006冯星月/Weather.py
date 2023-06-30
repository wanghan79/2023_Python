import requests
import json
from collections import Iterable,Iterator

with open('city.json', 'r', encoding='utf8') as f:
    data1 = json.load(f)
class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get('http://t.weather.sojson.com/api/weather/city/'+str(data1[city]))
        data = r.json()
        return '%s: %s,%s' % (city,data["data"]["forecast"][0]["high"], data["data"]["forecast"][0]["low"])

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



if __name__ == '__main__':
    for x in WeatherIterable(['北京', '长春']):
        print(x)