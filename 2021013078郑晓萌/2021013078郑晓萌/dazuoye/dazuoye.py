print("三次作业完整运行结果:")

import work1
import work2
import work3

print("输入“1”查看第一次作业，输入“2”查看第二次作业，输入“3”查看第三次作业，输入“0”结束")


while (True):
    i = input()
    if i == '1':
        x = work1.DataSampling(num=5, struct={
            'x1': {'type': 'int', 'datarange': [0, 10]},
            'x2': {'type': 'float', 'datarange': [0, 1]},
            'x3': {'type': 'str', 'datarange': ['a', 'b', 'c', 'd'], 'len': 3}
        })
        print(x)
    elif i == '2':
        x = work2.DataSampling(num=5, struct={'x1': {'type': 'int', 'datarange': [0, 10]},
                                        'x2': {'type': 'int', 'datarange': [0, 10]}, })
        print(x)
    elif i == '3':
        for x in work3.WeatherIterator(["北京", "广州", "长春"]):
            print(x)
    elif i == '0':
        break
    else:
        print("ERROR")
