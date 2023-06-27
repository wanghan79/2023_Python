# 导入requests库和Iterable、Iterator类
import requests
from collections.abc import Iterable, Iterator


# 自定义天气信息迭代器
class WeatherIterator(Iterator):
    def __init__(self, cities):
        # 保存要获取天气信息的城市列表
        self.cities = cities
        # 初始化迭代器的游标
        self.index = 0

    # 获取指定城市的天气信息
    def getWeather(self, city):
        # 发送GET请求，获取城市天气信息
        r = requests.get(
            u'https://restapi.amap.com/v3/weather/weatherInfo?key=da8fa78adb6d1fc873b1e20e83c321fe&city=' + city + '&extensions=base')
        # 解析返回结果，获取天气信息
        data = r.json()['lives'][0]
        # 格式化天气信息并返回
        return '城市:{}; 天气:{}; 温度:{}; 风向:{}风;'.format(data['city'], data['weather'], data['temperature'], data['winddirection'])

    # 实现Iterator类中的抽象方法，返回下一个数据元素
    def __next__(self):
        # 判断游标是否到达迭代器末尾，如果是则停止迭代
        if self.index == len(self.cities):
            raise StopIteration
        # 获取当前城市
        city = self.cities[self.index]
        # 增加游标
        self.index += 1
        # 返回当前城市的天气信息
        return self.getWeather(city)

# 自定义天气信息可迭代对象
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)


def main():
    for x in WeatherIterable([u'天津', u'辽宁', u'上海', u'长春']):
        print(x)


if __name__ == "__main__":
    main()