
import requests
from collections.abc import Iterable, Iterator
class WeatherIterable(Iterable):
    def __init__(self, city_list):
        self.city_list = city_list

    def __iter__(self):
        iterator = WeatherIterator(self.city_list)
        iterator.fetch_weather_data()
        return iterator

class WeatherIterator(Iterator):
    def __init__(self, city_list):
        self.city_list = city_list
        self.index = 0
        self.weather_data = []

    def fetch_weather_data(self):
        url = "http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("获取天气数据失败")
        self.weather_data = response.json()['data']

    def search_weather(self, city):
        for key in self.weather_data:
            if key[0] == city:
                return key
        return None

    def get_weather_info(self, city):
        weather = self.search_weather(city)
        if weather is None:
            return '抱歉，未找到%s的天气信息' % city
        return '%s的天气信息：最高温度为%s ；最低温度为%s' % (city, weather[8], weather[13])

    def __next__(self):
        if self.index >= len(self.city_list):
            raise StopIteration
        city = self.city_list[self.index]
        self.index += 1
        return self.get_weather_info(city)


