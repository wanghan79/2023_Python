import requests
import json
from collections.abc import Iterable,Iterator
class WeatherIterator(Iterator) :
    def __init__(self,cities) :
        self.index = 0
        self.cities = cities
        self.City = open("城市编码表.json",encoding = "utf-8")
        self.doc = json.load(self.City)

    def getWeather(self,city) :
        cityname = 0
        for i in self.doc['城市代码']:
            for j in i['市']:
                if j['市名'] == city:
                    cityname = j['编码']
        r = requests.get("http://t.weather.sojson.com/api/weather/city/"+ cityname)
        data = r.json()['data']['forecast'][0]
        return '%s： %s , %s ' % (city, data['low'], data['high'])

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
def weather():
    for x in WeatherIterable([u'北京',u'长春',u'上海',u'广州']):
        print(x)
if __name__ == '__main__':
    weather()