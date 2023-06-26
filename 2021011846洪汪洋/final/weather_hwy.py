import requests
from collections.abc import Iterable, Iterator

key = "70ad64ad36af58951fba3a45a93b6ddc"
def get_adcode(city):
    url = f'https://restapi.amap.com/v3/geocode/geo?key={key}&address={city}'
    response = requests.get(url)
    data = response.json()
    return data['geocodes'][0]['adcode']

def get_weather(adcode):
    url = f'https://restapi.amap.com/v3/weather/weatherInfo?key={key}&city={adcode}'
    response = requests.get(url)
    data = response.json()
    return data['lives'][0]


class weatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getweather(self, city):
        adcode = get_adcode(city)
        res = get_weather(adcode)
        return f"{city}：温度为{res['temperature']}°c， 天气为{res['weather']}"


    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getweather(city)


class weatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return weatherIterator(self.cities)

def show():
    for x in weatherIterable([u"北京", u"上海", u"广州", u"长春"]):
        print(x)