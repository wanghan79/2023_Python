from job1 import varystrctDataSampling, inputStruct
from job2 import decorateStrctDataSampling, decorateInputStruct
from job3 import WeatherIterable

print("请轮流输入数字1,2,3来查看三个不同作业的演示,\n(如果想停止执行，请输入数字-1)\n")
for i in range(0,3):
    task = input("输入数字 ：")
    if task == '1' : print(varystrctDataSampling(**inputStruct))
    elif task == '2' : decorateStrctDataSampling(**decorateInputStruct)
    elif task == '3' :
        for x, y in zip(WeatherIterable(['101010100', '101280101', '101060101']),['北京', '广州', '长春']):  # 查询城市名可根据需求增添或更改,括号内的数值是城市编码，可以根据需求从city.json文件查询
            print(y, "今天的天气:", x)
    elif task == '-1': break
    else: print("The project has no this job!")