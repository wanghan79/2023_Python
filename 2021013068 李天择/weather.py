import requests


class CityWeatherIterator:
    def __init__(self, cities):
        self.cities = cities
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.cities):
            raise StopIteration
        else:
            city = self.cities[self.current]
            weather_data = self.get_weather_data(city)
            self.current += 1
            return (city, weather_data)

    def get_weather_data(self, city):
        url = f'https://api.seniverse.com/v3/weather/daily.json?key=SeCutN4lsWHp7bFZL&location={city}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = data['results'][0]['daily'][0]['text_day']
            return weather_data
        else:
            return 'N/A'


class CityWeatherIterable:
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return CityWeatherIterator(self.cities)


# 调用示例
# cities = ['Beijing', 'Shanghai']
# city_weather = CityWeatherIterable(cities)
#
# for city, weather in city_weather:
#     print(f"The weather in {city} is {weather}")
