import requests

from collections.abc import Iterable, Iterator

class WeatherIterator(Iterator):
    """
    迭代器，用于获取指定城市的天气信息
    """
    url = "http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671"

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        """
        获取指定城市的天气信息
        """
        response = requests.get(self.url)
        data = response.json()['data']
        for item in data:
            if item[0] == city:
                return f"{city}: 最高温【{item[8]}】 ,最低温【{item[13]}】"

    def __next__(self):
        """
        获取下一个城市的天气信息
        """
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

class WeatherIterable(Iterable):
    """
    可迭代对象，用于获取多个城市的天气信息
    """
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

if __name__ == "__main__":
    cities = ["北京", "长春", "广州", "天津"]
    for weather in WeatherIterable(cities):
        print(weather)