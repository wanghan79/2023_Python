import random
import string
import requests
from collections.abc import Iterable, Iterator
from functools import wraps


# 作业1
def dataSampling(**kwargs):
    result = []
    structure = kwargs.get('struct')
    num = kwargs.get('num')
    for _ in range(num):
        element = {}
        for key, value in structure.items():
            data_type = value['datatype']
            if data_type == int:
                data_range = value['range']
                element[key] = random.randint(data_range[0], data_range[1])
            elif data_type == float:
                data_range = value['range']
                element[key] = random.uniform(data_range[0], data_range[1])
            elif data_type == str:
                data_range = value['range']
                length = value['len']
                element[key] = ''.join(random.choices(data_range, k=length))
        result.append(element)
    return result


# 作业2
def sum_avg(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if 'SUM' in args:
            return sum(res)
        if 'AVG' in args:
            return sum(res) / len(res)
        return res

    return wrapper


@sum_avg
def dataSampling_decorated(*types, num=1, length=10, start=0, end=100, repeat=False):
    result = []
    for i in range(num):
        if 'int' in types:
            result.append(random.randint(start, end))
        if 'float' in types:
            result.append(random.uniform(start, end))
        if 'str' in types:
            result.append(''.join(random.sample('abcdefghijklmnopqrstuvwxyz', length)))
    if not repeat:
        result = list(set(result))
    return result


# 作业3
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
               (data['city'], data['weather'], data['temperature_float'], data['wind-direction'], data['humidity'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


def main():
    job_number = input("请输入要展示的作业号（1、2或3）：")

    if job_number == '1':
        x = dataSampling(num=2, struct={
            'a': {
                'datatype': int,
                'range': [1, 10]
            },
            'b': {
                'datatype': float,
                'range': [1, 10]
            },
            'c': {
                'datatype': str,
                'range': string.ascii_lowercase,
                'len': 10
            },
            '123': {
                'datatype': int,
                'range': [1, 10]
            },
            '111': {
                'datatype': int,
                'range': [1, 10]
            },
        })
        print(x)
    elif job_number == '2':
        # 调用作业2的示例代码并输出结果
        print(dataSampling_decorated('int', num=5))
        print(dataSampling_decorated('float', num=5))
        print(dataSampling_decorated('str', num=5))
        print(dataSampling_decorated('int', 'float', num=5))
        print(dataSampling_decorated('int', 'float', 'str', num=5))
    elif job_number == '3':
        # 调用作业3的示例代码并输出结果
        city_weather = CityWeather(['北京', '上海', '广州', '长春'])
        for item in city_weather:
            print(item)
    else:
        print("无效的作业号！")


# 运行主程序
if __name__ == '__main__':
    main()
