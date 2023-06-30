import hw1_dataSampling
import hw3_weather
from hw2_wrapper import run_operation


class InvalidChoiceException(Exception):
    pass


def main():
    while True:
        print("请选择要展示的作业号：")
        print("1. 作业一:实现随机数据结构生成封装函数dataSampling(**kwargs)")
        print("2. 作业二:采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的求和（SUM），求均值（AVG）操作")
        print("3. 作业三:执行使用迭代器实现城市天气数据的自动获取")
        print("0. 退出程序")
        choice = input("请输入选择的作业号：")

        try:
            if choice == "1":
                struct = {"struct": ({"type": int, "range": [0, 100]}, {"type": float, "range": [0, 100]},
                                     {"type": str, "range": ['a', 'b', 'c', 'd', 'e', 'f', 'g'], "len": 10})}
                num_structs = 10  # 指定生成10个结构体
                generated_data = hw1_dataSampling.genStructs(num_structs, struct)
                print("生成的随机数据结构如下：")
                for data in generated_data:
                    print(data)


            elif choice == "2":
                print("请输入一个操作码，1代表求和，2代表求平均数，3代表两者都求, 0返回主菜单")
                while True:
                    x = input()
                    if x == '1':
                        run_operation(["sum"])
                        break
                    elif x == '2':
                        run_operation(["avg"])
                        break
                    elif x == '3':
                        run_operation(["sum", "avg"])
                        break
                    elif x == '0':
                        break
                    else:
                        print("操作码无效，请重新输入!")


            elif choice == "3":
                cities = [u'北京', u'深圳', u'济南', u'长春']
                print("获取城市天气数据如下：")
                for weather_data in hw3_weather.WeatherIterable(cities):
                    print(weather_data)

            elif choice == "0":
                break

            else:
                raise InvalidChoiceException("无效的选择，请重新输入。")
        except InvalidChoiceException as e:
            print(e)
        finally:
            print("=================")


if __name__ == "__main__":
    main()
