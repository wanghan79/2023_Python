import requests
from collections.abc import Iterable, Iterator


class CityWeather(Iterable):

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


class WeatherIterator(Iterator):

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def get_weather(self, city):
        r = requests.get(u'https://restapi.amap.com/v3/weather/weatherInfo?key=3e2fb91961b3881c29c2448f487e99b5'
                         u'&city=' + city + '&extensions=base')
        data = r.json()['lives'][0]
        return '%s, %s, 气温：%s摄氏度, %s风, 湿度:%s%%' % \
            (data['city'], data['weather'], data['temperature_float'], data['winddirection'], data['humidity'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


# 调用示例
city_weather = CityWeather(['北京', '上海', '广州', '长春'])
for item in city_weather:
    print(item)