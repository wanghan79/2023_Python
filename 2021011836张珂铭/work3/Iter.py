import requests
from collections.abc import Iterable,Iterator
class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities=cities
        self.index=0
    def getWeather(self,city):
        r=requests.get(u'http://t.weather.sojson.com/api/weather/city/'+city)
        data=r.json()['data']['forecast'][0]
        city_name=r.json()['cityInfo']['city']
        return f"{city_name}:{data['low']},{data['high']}"
    def __next__(self):
        if self.index==len(self.cities):
            raise StopIteration
        city=self.cities[self.index]
        self.index+=1
        return self.getWeather(city)
class Weatherable(Iterable):
    def __init__(self,cities):
        self.cities=cities
    def __iter__(self):
        return WeatherIterator(self.cities)
def PrintWeather():
    print(f"获取北京、上海、广州、长春的气温")
    for x in Weatherable([u'101010100',u'101020100',u'101280101',u'101060101']):
        print(x)
    print('')
if __name__ == '__main__':
    PrintWeather()
# u'北京',101010100
# u'上海',101020100
# u'广州',101280101
# u'长春',101060101
