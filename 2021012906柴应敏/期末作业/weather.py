import requests
from collections.abc import Iterable, Iterator


cities = {
    '北京': u'110000',
    '上海': u'310000',
    '广州': u'440100',
    '长春': u'220100',
}


class WeatherIterator(Iterator):

    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'https://restapi.amap.com/v3/weather/weatherInfo?key=3e2fb91961b3881c29c2448f487e99b5'
                         u'&city=' + city + '&extensions=base')
        data = r.json()['lives'][0]
        return '%s, %s, 气温：%s摄氏度' % \
               (data['city'], data['weather'], data['temperature_float'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        try:
            city = cities[self.cities[self.index]]
        except:
            pass
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

def weather_test1():
    for x in WeatherIterable(['北京','广州','上海','长春']):
        print(x)

if __name__ == '__main__':
    weather_test1()
