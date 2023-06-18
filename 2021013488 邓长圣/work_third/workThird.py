# deng chang sheng

"""
生成器，
"""
import json

import requests
from collections.abc import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

        # 读取城市编码表文件
        self.f = open("work_third/城市编码表.json", encoding="utf-8")
        self.cityCode = json.load(self.f)


    def getWeather(self, city):
        code = ""
        for province in self.cityCode['城市代码']:
            for muni in province['市']:
                if muni['市名'] == city:
                    code = muni['编码']
                    break

        if code == "":
            return "The city " + city + " was not found..."
        r = requests.get("http://t.weather.sojson.com/api/weather/city/" + code)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' %(city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, *cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


"""
作业三展示
"""
def show():
    print("作业三：使用迭代器实现城市天气数据的自动获取，以及相应的调用示例，主要考察点市自定义可迭代对象与相应迭代器的开发")
    print("示例：查看以下城市的天气：北京， 上海， 广州， 长春")
    cities = [u'北京', u'上海', u'广州', u'长春']
    for x in WeatherIterable(*cities):
        print(x)


if __name__ == "__main__":
    # for x in WeatherIterable(u'北京', u'上海', u'广州', u'长春'):
    #     print(x)
    show()