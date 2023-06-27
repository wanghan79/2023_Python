class WeatherIterator:
    """

    """
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.weather_data):
            raise StopIteration
        info = self.weather_data[self.index]
        self.index += 1
        return info

class Weather:
    """

    """
    def __init__(self):
        self.city_weather = {}  # 存放城市天气数据的字典

    def addCity(self, city, temp):
        """

        """
        self.city_weather[city] = temp

    def __iter__(self):
        return WeatherIterator(list(self.city_weather.items()))

w = Weather()
w.addCity('Beijing', 32)
w.addCity('Shanghai', 30)
w.addCity('Guangzhou', 28)

for city, temp in w:
    print(f'{city}: {temp}')