import json
import requests
from collections.abc import Iterable, Iterator
import os
import json

def get_city_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '城市编码表.json')
    with open(file_path, 'r', encoding='utf8') as f:
        data = json.load(f)
    element = {}
    for i in data['城市代码']:
        for j in i['市']:
            element[j['市名']] = j['编码']
    return element



class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        try:
            r = requests.get(u'http://t.weather.sojson.com/api/weather/city/' + get_city_data()[city])
            data = r.json()['data']['forecast'][0]
            return f"{city}, {data['low']}, {data['high']}"
        except (requests.RequestException, json.JSONDecodeError, KeyError):
            return f"Failed to get weather data for {city}"

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__ == "__main__":
    for weather_data in WeatherIterable([u'北京', u'上海', u'广州', u'长春', u'鄂尔多斯']):
        print(weather_data)
