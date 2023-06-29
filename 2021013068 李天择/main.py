from data_sampling import dataSampling
from decorator import data_avg, data_sum
from weather import CityWeatherIterable


def main(op):
    if op == 1:
        random_data = dataSampling(int=5, float=3, str=4)
        print(random_data)
    elif op == 2:
        data_sum(int=5, float=3)
        data_avg(int=5, float=3)
    elif op == 3:
        cities = ['Beijing', 'Shanghai']
        city_weather = CityWeatherIterable(cities)

        for city, weather in city_weather:
            print(f"The weather in {city} is {weather}")


if __name__ == '__main__':
    input_op = int(input("请选择要展示的作业号（1、2或3）: "))
    main(input_op)
