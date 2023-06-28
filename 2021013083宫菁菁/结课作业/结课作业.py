def task1():
    import random
    import string
    def structDataSampling(**kwargs):
        result = list()
        for index in range(0, 10):
            element = list()
            for key, value in kwargs.items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == "str":
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    break
                element.append(tmp)
            result.append(element)
        return result

    a = {"int": {"datarange": (0, 100)}}
    b = {"float": {"datarange": (0, 10000)}}
    c = {"str": {"datarange": string.ascii_letters, "len": 5}}
    d = structDataSampling(**a)
    e = structDataSampling(**b)
    f = structDataSampling(**c)
    print("int型")
    print(d)
    print("float型")
    print(e)
    print("str型")
    print(f)

def task2():
    import random
    import logging

    def sum(a):
        result = list()
        for i in range(0, 5):
            sum = 0;
            for j in range(0, 49):
                sum += a[j][i]
            result.append(sum)
        return result

    def avg(a):
        result = sum(a)
        for i in range(0, 5):
            result[i] = result[i] / 50
        return result

    def addlogging(*order):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                sum_result = sum(result)
                avg_result = avg(result)
                output = {'result': result, 'sum': sum_result, 'avg': avg_result}
                for item in order:
                    if item == "sum":
                        output['sum'] == sum_result
                    if item == "avg":
                        output['avg'] == avg_result
                return output

            return wrapper

        return decorator

    @addlogging("sum", "avg")
    def structDataSamping(num, struct):
        result = []
        for i in range(50):
            element = []
            for j in range(5):
                it = iter(struct['datarange'])
                tmp = random.uniform(next(it), next(it))
                element.append(tmp)
            result.append(element)
        return result

    struct = {"datarange": (0, 50)}
    a = structDataSamping(3, struct)
    print(a['result'])
    print(a['sum'])
    print(a['avg'])

def task3():
    import requests
    from collections.abc import Iterable, Iterator

    def seach(city, list):
        for key in list:
            if key[0] == city:
                return key
        return 0

    class WeatherIterator(Iterator):
        def __init__(self, city):
            self.cities = city
            self.index = 0

        def getWeather(self, city):
            r = requests.get("http://www.nmc.cn/dataservice/weather/map/ALL/day2.json?t=1685701082502&_=1685701063671")
            data = r.json()['data']
            weather = seach(city, data)
            return '%s: 最高温【%s】 ,最低温【%s】 ' % (city, weather[8], weather[13])

        def __next__(self):
            if self.index == len(self.cities):
                raise StopIteration
            city = self.cities[self.index]
            self.index += 1
            return self.getWeather(city)

    class WeatherIterable(Iterable):
        def __init__(self, cities):
            self.cities = cities

        def __iter__(self):
            return WeatherIterator(self.cities)

    if __name__ == '__main__':
        city = [u'北京', u'长春']
        for weather in WeatherIterable(city):
            print(weather)

def main():
    while True:
        num = input("请输入1, 2, 3: ")

        if num == '1':
            task1()
        elif num == '2':
            task2()
        elif num == '3':
            task3()
        else:
            break


if __name__ == "__main__":
    main()