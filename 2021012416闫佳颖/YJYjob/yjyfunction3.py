import requests
import pandas as pd
from collections.abc import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        url = f'http://t.weather.sojson.com/api/weather/city/{city}'
        r = requests.get(url)
        weather_data = r.json().get('data', {})
        if not weather_data:
            return f'{city} 天气数据获取失败'
        forecast = weather_data.get('forecast', [])
        if not forecast:
            return f'{city} 天气数据获取失败'
        low, high = forecast[0].get('low'), forecast[0].get('high')
        return f'{city}:{low}~{high}'

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


def search_city_code(city_name):
    city_code = '-1'

    df = pd.read_json('yjy_city_list.json')
    for row in df.values:
        row_data = row[0]
        city_data = row_data['市']
        for cd in city_data:
            if (city_name == cd['市名'] or cd['市名'] in city_name):
                city_code = cd['编码']
                break
    return city_code


def yfunction3():
    city_name_in = input("请输入城市名称：")
    for x in WeatherIterable([search_city_code(city_name_in)]):
        print(x)