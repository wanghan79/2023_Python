import requests
from collections.abc import Iterable, Iterator
import pandas as pd

def search(city_name):
    city_code = '-1'

    df = pd.read_json('SJ3.json')
    for row in df.values:
        row_data = row[0]
        city_data = row_data['市']
        for cd in city_data:
            if (city_name == cd['市名'] or cd['市名'] in city_name):city_code = cd['编码']
            break

    return city_code

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, citycode):
        url = f'http://t.weather.sojson.com/api/weather/city/{citycode}'
        r = requests.get(url)
        weather_data = r.json().get('data', {})
        forecast = weather_data.get('forecast', [])
        low, high = forecast[0].get('low'), forecast[0].get('high')
        return f' {low}~{high}'

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

def SJwork_3():
    print(("练习3："))
    print(("练习测试（案例：北京)："))
    for x in WeatherIterable(['101010100']):
        print(("北京")+x)
    print("随机测试：")
    name = input("输入你想查询的城市： ")
    name = str(name)
    for x in WeatherIterable([search(name)]):
        print(name+x)

SJwork_3()
