"""
  陈俊聪
  Python结课作业
  2023/6/20
"""

from PythonClass.final_work_cjc import UserInput


def startProject():
    UserInput.mainMenuInput()


def enterMainMenu():
    print("-------------------------------------------------")
    print("Welcome to the Python Final Test Menu")
    print("Here are my works")
    print("1、Random_dataSampling")
    print("2、Advanced_random_dataSampling_Calculation")
    print("3、Get_Weather")
    print("4、Exit")



def randomDataSampling():
    print("-------------------------------------------------")
    print("Python Test 1: Random_dataSampling")
    print("实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：\n"
          "1.采用关键字参数作为随机数据结构及数量的输入。 \n"
          "2.在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成。  \n"
          "3.其中随机数涵盖int，float和str三种类型。")
    print("示例如下: ")



def advancedRandomDataSamplingCalculation():
    print("-------------------------------------------------")
    print("Python Test 2: Advanced_random_dataSampling_calculation")
    print("采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的求和（SUM），求均值（AVG）操作，以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：\n"
          "1.	修饰器类型不限，可以是函数修饰器或类修饰器；\n"
          "2.	只能实现一个修饰器，通过修饰器参数（*args）实现SUM和AVG操作的任意组合，即修饰器在接收0、1、2个参数的情况下都可以正常运行；")
    print("Please select a operation you want to perform: ")
    print("1、Input sample number")
    print("2、return to the main menu")


def getWeatherViewing():
    print("-------------------------------------------------")
    print("Python Test 3: Get_Weather")
    print("使用迭代器实现城市天气数据的自动获取，以及相应的调用示例，主要考察点是自定义可迭代对象与相应迭代器的开发")
    print("Please select a operation you want to perform: ")
    print("1、Get weather")
    print("2、return to the main menu")




