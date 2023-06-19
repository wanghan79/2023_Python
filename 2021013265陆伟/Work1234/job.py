import RandomTest
import DecorationRandom
import Weather


if __name__ == '__main__':
    print("1:作业一 2:作业二 3:作业三 -1:退出")
    while True:
        operation = int(input("请输入"))
        if operation == 1:
            result = RandomTest.structDataSampling(num=5, struct={'one':{'datatype':'int',"datarange": (0,100)}, 'two': {'datatype': 'float', 'datarange': [1, 100]}})
            print(result)

        elif operation == 2:
            result = DecorationRandom.structDataSampling(num=5, struct={'one':{'datatype':'int',"datarange": (0,100)}, 'two': {'datatype': 'float', 'datarange': [1, 100]}})
            print(result)
        elif operation ==3:
            for x in Weather.WeatherIterable(['重庆', '上海', '广州', '长春']):
                print(x)
        else :
            print("Thanks")
            break


