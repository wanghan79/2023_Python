import requests
from collections.abc import Iterable, Iterator

cityDictionary = {
    "长春": "101060101",
    "成都": "101270101",
    "厦门": "101230201",
    "广州": "101280101",
    "上海":"101020100",
    "石家庄":"101090101",
    "郑州":"101180101",
    "杭州":"101210101"
}


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getweather(city)

    def getweather(self, city):
        cityCode = cityDictionary[city]
        r = requests.get(u'http://t.weather.sojson.com/api/weather/city/' + cityCode)
        data = r.json()['data']['forecast'][0]
        return ' %s %s %s市天气%s %s %s %s ' \
            % (data['ymd'],data['week'],city,data['type'],data['low'],data['high'],data['notice'])
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

if __name__ == '__main__':
    for x in WeatherIterable(["长春", "上海", "成都", "广州"]):
        print(x)
