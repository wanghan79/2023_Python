import requests,json
from collections.abc import Iterable,Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        url = 'http://t.weather.sojson.com/api/weather/city/' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        return '%s,%s  ' % (data['low'], data['high'])

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

if __name__ == "__main__":
    for x, y in zip(WeatherIterable(['101010100', '101280101', '101060101']),
                    ['北京', '广州', '长春']):  # 查询城市名可根据需求增添或更改,括号内的数值是城市编码，可以根据需求从city.json文件查询
        print(y, "今天的天气:", x)



