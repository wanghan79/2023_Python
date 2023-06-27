import requests
from collections.abc import Iterable, Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

    def getWeather(self, city):
        # 使用心知天气API获取城市天气数据
        api_key = "Sq1lM8msLFRwgRGKj"
        url = f"https://api.seniverse.com/v3/weather/now.json?key={api_key}&location={city}&language=zh-Hans&unit=c"
        response = requests.get(url)
        data = response.json()
        weather = data["results"][0]["now"]["text"]
        temperature = data["results"][0]["now"]["temperature"]
        return f"{city}: {weather}，温度：{temperature}°C"

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

# 调用示例
cities = ['北京', '上海', '广州', '深圳']
weather_data = WeatherIterable(cities)

for data in weather_data:
    print(data)