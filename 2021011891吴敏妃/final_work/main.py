import random
import string
import requests
from collections.abc import Iterable, Iterator


def structDataSampling(**kwargs):
    result = []
    for _ in range(kwargs["num"]):
        element = {}
        for key, value in kwargs['struct'].items():
            if value['datatype'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element[key] = tmp
        result.append(element)
    return result


def dataSamplingDecorator(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        sums = 0
        count = 0
        for row in data:
            for element in row:
                if isinstance(element, (int, float)):
                    sums += element
                    count += 1
        avg = sums / count if count > 0 else 0
        return sums, avg

    return wrapper


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

    def getWeather(self, city):
        api_key = "Sq1lM8msLFRwgRGKj"  # 替换为你的心知天气API密钥
        url = f"https://api.seniverse.com/v3/weather/now.json?key={api_key}&location={city}&language=zh-Hans&unit=c"
        response = requests.get(url)
        data = response.json()
        weather = data["results"][0]["now"]["text"]

        temperature = data["results"][0]["now"]["temperature"]
        return f"{city}: {weather}，温度：{temperature}°C"


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def run_homework_1():
    struct = {
        'int': {'datatype': int, 'datarange': (1, 100)},
        'float': {'datatype': float, 'datarange': (1.0, 100.0)},
        'str': {'datatype': str, 'datarange': string.ascii_letters, 'len': 5}
    }

    data = structDataSampling(num=5, struct=struct)
    print(data)


@dataSamplingDecorator
def run_homework_2(**kwargs):
    struct = {
        'int': {'datatype': int, 'datarange': (1, 100)},
        'float': {'datatype': float, 'datarange': (1.0, 100.0)},
        'str': {'datatype': str, 'datarange': string.ascii_letters, 'len': 5}
    }

    data = structDataSampling(num=5, struct=struct)
    return data


def run_homework_3():
    cities = ['北京', '上海', '广州', '深圳']
    weather_data = WeatherIterable(cities)

    for data in weather_data:
        print(data)


def main():
    print("欢迎使用作业示例展示程序！")
    print("请输入要展示的作业号（1、2或3），输入其他内容将退出程序。")

    while True:
        choice = input("请输入作业号：")

        if choice == "1":
            print("运行作业一示例：")
            run_homework_1()
        elif choice == "2":
            print("运行作业二示例：")
            result = run_homework_2(num=5, struct={})
            print("Sum:", result[0])
            print("Avg:", result[1])
        elif choice == "3":
            print("运行作业三示例：")
            run_homework_3()
        else:
            print("退出程序。")
            break


if __name__ == "__main__":
    main()

