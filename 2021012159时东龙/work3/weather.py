import requests
from collections.abc import Iterable,Iterator
#使用了高德地图的天气API和地理编码API
API_KEY = 'f4b6fb8977c1221b77b65e771bec0599'

def get_adcode(city):
    url = 'https://restapi.amap.com/v3/geocode/geo?key={}&address={}'.format(API_KEY,city)
    response = requests.get(url)
    data = response.json()
    return data['geocodes'][0]['adcode']

def get_weather(adcode):
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?key={}&city={}'.format(API_KEY,adcode)
    response = requests.get(url)
    data = response.json()
    return data['lives'][0]

class WeatherIterator(Iterator):
    def get_weather_by_name(self,city):
        #格式化输出温度、天气、风力
        data = get_weather(get_adcode(city))
        return '{}: {} {}摄氏度 风力等级{}'.format(city,data['weather'],data['temperature'],data['windpower'])

    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather_by_name(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

def weather_test1():
    for x in WeatherIterable(['北京','吉林省','吉林市','长春']):
        print(x)


if __name__ == '__main__':
    weather_test1()