import requests
import json

class WeatherIterator:
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        # api地址
        url = 'http://t.weather.sojson.com/api/weather/city/'

        # 读取json文件
        f = open('city.json', 'rb')

        # 使用json模块的load方法加载json数据，返回一个字典
        cities = json.load(f)

        # 通过城市的中文获取城市代码
        city = cities.get(city)

        # 网络请求，传入请求api+城市代码
        response = requests.get(url + city)

        # 将数据以json形式返回，这个d就是返回的json数据
        d = response.json()

        # 当返回状态码为200，输出天气状况
        if (d['status'] == 200):
            print("城市：", d["cityInfo"]["parent"], d["cityInfo"]["city"])
            print("时间：", d["time"], d["data"]["forecast"][0]["week"])
            print("温度：", d["data"]["forecast"][0]["high"], d["data"]["forecast"][0]["low"])
            print("天气：", d["data"]["forecast"][0]["type"])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable():
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


# for x in WeatherIterable(["北京", "上海"]):
#     print("----" * 10)