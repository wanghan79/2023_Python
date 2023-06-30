
from test1 import dataSampling
from test2 import generate_random_data_1, generate_random_data_2, generate_random_data_3, generate_random_data_4
from test3 import WeatherIterable
def main():
    while True:
        print("请输入选项：")
        print("1. 运行程序1")
        print("2. 运行程序2")
        print("3. 运行程序3")
        print("4. 退出程序")

        option = input("选项: ")

        if option == '1':
            data1 = dataSampling(numbers={'type': 'int', 'size': 10, 'range': (1, 100)})
            print(data1)
            data2 = dataSampling(points={'type': 'float', 'size': 5, 'range': (0.0, 1.0)})
            print(data2)
            data3 = dataSampling(words={'type': 'str', 'size': 6})
            print(data3)
        elif option == '2':
            data1 = generate_random_data_1(numbers={'type': 'int', 'size': 10, 'range': (1, 100)})
            print(data1)
            data2 = avg2 = generate_random_data_2(points={'type': 'float', 'size': 5, 'range': (0.0, 1.0)})
            print(data2)
            print(avg2)
        elif option == '3':
            if __name__ == '__main__':
                cities = ['北京', '上海', '广州', '深圳']
                for weather in WeatherIterable(cities):
                    print(weather)
        elif option == '4':
            print("退出程序")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == '__main__':
    main()