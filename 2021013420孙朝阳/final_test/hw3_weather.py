from collections.abc import Iterator, Iterable
import requests as r
import os
import json


def get_city_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '../城市编码表.json')
    with open(file_path, 'r', encoding='utf8') as f:
        data = json.load(f)
    dict = {}
    for i in data['城市代码']:
        for j in i['市']:
            dict[j['市名']] = j['编码']
    return dict


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        try:
            url = r'http://t.weather.sojson.com/api/weather/city/' + get_city_data()[city]
            req = r.get(url)
            data = req.json()['data']['forecast'][0]
            return '%s:%s,%s' % (city, data['low'], data['high'])
        except (r.RequestException, json.JSONDecodeError, KeyError):
            return f"Failed to get weather data for {city}"

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
    for x in WeatherIterable([u'北京', u'深圳', u'济南', u'长春']):
        print(x)
