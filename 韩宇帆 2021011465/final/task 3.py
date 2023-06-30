import random
import string

class CityWeatherIterator:
    def __init__(self, city_weather):
        self.city_weather = city_weather
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.city_weather):
            raise StopIteration
        result = self.city_weather[self.index]
        self.index += 1
        return result

class CityWeather:
    def __init__(self, *cities):
        self.cities = cities

    def __iter__(self):
        return CityWeatherIterator(self.cities)

    def get_weather(self, city):

        return f"The weather of {city} is sunny"


city_weather = CityWeather('Beijing', 'Shanghai', 'Guangzhou')


for weather in city_weather:
    print(weather)

