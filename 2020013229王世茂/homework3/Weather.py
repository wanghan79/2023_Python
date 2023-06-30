import requests
import sys
from collections.abc import Iterable, Iterator

key = 'bd5e378503939ddaee76f12ad7a97608'
class WeatherIterator(Iterator):
        def __init__(self, cities, key):
                self.cities = cities
                self.index = 0
                self.key = key

        def get_city_Weather(self, city):
                get_info_url = "http://api.openweathermap.org/geo/1.0/direct"
                base_url = "https://api.openweathermap.org/data/2.5/forecast"
                params = {
                "q": city,
                "appid": self.key,
                }
#               print(params)
                info = requests.get(get_info_url, params).json()
#               print(info)
                lat, lon = info[0]['lat'], info[0]['lon']
#               print(lat, lon)
                params = {
                        'lat': lat,
                        'lon': lon,
                        'appid': self.key,
                        'exclude': 'current',
                        'units': "metric",
                }
                response = requests.get(base_url, params)
                weather_data = response.json()
#               print(weather_data["list"])
#               print(response)
#               for x in weather_data["list"]:
#                       print(x)
                if weather_data["cod"] != 404:
                        temperature = weather_data["list"][0]["main"]["temp"]
                        return temperature
                else:
                        raise Exception("City not found")

        def __next__(self):
                if self.index >= len(self.cities):
                        raise StopIteration
                city = self.cities[self.index]
                self.index += 1
                print("%s当前气温为" % (city), end = " ")
                return self.get_city_Weather(city)


class WeatherIterable(Iterable):
        def __init__(self, cities, key):
                self.cities = cities
                self.key = key

        def __iter__(self):
                return WeatherIterator(self.cities, self.key)

cities = ["长春市", "北京市", "上海市", "南京市", "杭州市", "天津市", "New York"]

for tp in WeatherIterable(cities, key):
        print("%.2f 摄氏度。" % (tp))
'''
导入所需的模块：requests用于进行HTTP请求，sys用于特定于系统的功能。还从collections.abc模块中导入Iterable和Iterator类。

将访问OpenWeatherMap API所需的API密钥存储在key变量中。

WeatherIterator类被定义为Iterator的子类。它接受城市列表和API密钥作为参数。__init__方法初始化迭代器并设置索引为0。get_city_Weather方法通过向OpenWeatherMap API发出API请求来检索给定城市的天气数据。它使用API端点获取城市的纬度和经度，然后使用获得的坐标进行天气预报请求。它返回该城市的当前温度。

WeatherIterator类中的__next__方法定义了迭代器的行为。它检查是否还有更多的城市可迭代，如果没有更多城市，则引发StopIteration异常。它从列表中获取下一个城市，增加索引，并调用get_city_Weather方法获取该城市的温度。它还打印城市名称和温度。

WeatherIterable类被定义为Iterable的子类。它接受城市列表和API密钥作为参数。__iter__方法返回WeatherIterator类的实例，传递城市和API密钥。

城市列表被定义在cities变量中。

使用for循环迭代WeatherIterable对象，该对象在内部使用WeatherIterator。对于每次迭代，它获取一个城市的温度并将其与城市名称一起打印。

该代码通过进行API请求检索每个城市的天气数据，并打印每个城市的当前温度。
'''
