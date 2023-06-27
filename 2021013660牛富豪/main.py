import random
import string
from functools import wraps


class WeatherData:
    def __init__(self):
        self.city_temp = {"Beijing": 23, "Shanghai": 25, "Guangzhou": 29, "Shenzhen": 28, "Hangzhou": 22}

    def __iter__(self):
        self.cities = iter(self.city_temp.keys())
        return self

    def __next__(self):
        city = next(self.cities)
        temp = self.city_temp[city]
        return f"{city} temperature: {temp} degree Celsius"


def sum_avg_decorator(*args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            samples = func(*args, **kwargs)
            sum_value = sum(samples)
            avg_value = round(sum_value / len(samples), 2)
            if "SUM" in args:
                return sum_value
            elif "AVG" in args:
                return avg_value
            else:
                return samples

        return wrapper

    return decorator


@sum_avg_decorator("SUM")
def dataSampling(**kwargs):
    samples = []
    for key, value in kwargs.items():
        if key == "int":
            for i in range(value):
                num = random.randint(-100, 100)
                samples.append(num)
        elif key == "float":
            for i in range(value):
                num = round(random.uniform(-100.0, 100.0), 2)
                samples.append(num)
        elif key == "str":
            for i in range(value):
                num = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                samples.append(num)
    return samples


def main():
    while True:
        print("请输入要求展示的作业号：1、2或3（输入q退出）")
        choice = input().strip()
        if choice == "1":
            samples = dataSampling(int=3, float=2, str=1)
            print(samples)
        elif choice == "2":
            sum_value = dataSampling(int=3, float=2, str=1, "SUM")
            print(sum_value)
            avg_value = dataSampling(int=3, float=2, str=1, "AVG")
            print(avg_value)
        elif choice == "3":
            weather_data = WeatherData()
            for data in weather_data:
                print(data)
        elif choice == "q":
            break
        else:
            print("输入有误，请重新输入！")


if __name__ == "__main__":
    main()