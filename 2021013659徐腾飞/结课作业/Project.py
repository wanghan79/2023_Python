# 姓名：徐腾飞
# 时间：2023/6/27 19:24
import random
import requests

def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value == 'int':
            result[key] = random.randint(0, 100)
        elif value == 'float':
            result[key] = random.uniform(0, 100)
        elif value == 'str':
            result[key] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    return result

def dataStatistics(func):
    def wrapper(*args, **kwargs):
        data = func(**kwargs)
        sum_result = 0
        count = 0
        for key, value in data.items():
            if isinstance(value, (int, float)):
                sum_result += value
                count += 1
        avg_result = sum_result / count if count > 0 else 0
        if 'SUM' in args:
            print(f"SUM: {sum_result}")
        if 'AVG' in args:
            print(f"AVG: {avg_result}")
        return data
    return wrapper

dataSampling = dataStatistics(dataSampling)

class WeatherIterator:
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        url = f'http://wttr.in/{city}'
        weather = requests.get(url).text
        return city, weather

class WeatherIterable:
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

def run_homework1():
    print("Running homework 1...")
    print(dataSampling(a='int', b='float', c='str'))

def run_homework2():
    print("Running homework 2...")
    dataSampling('SUM', a='int', b='float', c='str')

def run_homework3():
    print("Running homework 3...")
    for city, weather in WeatherIterable(['Henan', 'Hebei', 'Hubei']):
        print(f"{city}: {weather}")

def main():
    while True:
        homework_number = input("Enter homework number (1, 2 or 3) or 'q' to quit: ")
        if homework_number == 'q':
            break
        elif homework_number == '1':
            run_homework1()
        elif homework_number == '2':
            run_homework2()
        elif homework_number == '3':
            run_homework3()
        else:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()