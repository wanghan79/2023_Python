# 姓名：徐腾飞
# 时间：2023/6/14 17:42
import requests

class WeatherIterator:
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        url = f'http://wttr.in/{city}'
        weather = requests.get(url).text
        return city, weather

class WeatherIterable:
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

# 调用示例
for city, weather in WeatherIterable(['Henan', 'Hebei', 'Hubei']):
    print(f"{city}: {weather}")