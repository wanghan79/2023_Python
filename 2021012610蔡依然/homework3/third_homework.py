print("___________________________________________")
print("有城市名字但是英文，用的群里第二个网址,有点慢，耐心等待喔")
import requests
class WeatherIterator:
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_coordinates(self, city):
        api_key = "6d66149a4f969dd84936cbd53788d8fd"
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            return None, None

    def get_weather(self, lat, lon):
        api_key = "6d66149a4f969dd84936cbd53788d8fd"
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        if data and 'list' in data:
            weather_data = data['list'][0]
            temp_min = weather_data['main']['temp_min'] - 273.15  # 转换为摄氏度
            temp_max = weather_data['main']['temp_max'] - 273.15  # 转换为摄氏度
            return f"Temperature: Min {temp_min:.2f}°C, Max {temp_max:.2f}°C"
        else:
            return "Weather data not available"

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration

        city = self.cities[self.index]
        self.index += 1

        lat, lon = self.get_coordinates(city)
        if lat and lon:
            weather = self.get_weather(lat, lon)
            return f"{city}: {weather}"
        else:
            return f"{city}: Coordinates not found"


cities = ['Beijing', 'Shanghai', 'Guangzhou', 'Changchun']
weather_info = WeatherIterator(cities)
for info in weather_info:
    print(info)

print("___________________________________________")

print("是中文，但是只有城市编码，是群里发的第一个方法")
import requests
import json
from collections.abc import Iterable, Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(f'http://t.weather.sojson.com/api/weather/city/{city}')
        data = r.json()['data']['forecast'][0]
        return '%s: %s ,%s ' % (city, data['low'], data['high'])

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

for x in WeatherIterable(['101010100', '101020100', '101280101', '101060101']):
        print(x)
print("___________________________________________")