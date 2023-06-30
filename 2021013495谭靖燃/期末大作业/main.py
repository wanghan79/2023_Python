import Random
import Decorator
import WeatherIterator
def main_test():
    while True:
        print("输入1演示作业1，输入2演示作业2，输入3演示作业3，输入其他退出程序")
        a = input("请输入：")
        if a == '1':
            Random.work1()
        elif a == '2':
            Decorator.work2()
        elif a == '3':
            WeatherIterator.work3()
        else:
            break

if __name__ == '__main__':
    main_test()