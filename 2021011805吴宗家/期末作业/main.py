import ast

from first_work.DataSampling import DataSampling
from second_work.decorator import structDataSampling
from third_work.weather import working

while True:
    print('测试生成随机数请输入 1\n'
          '测试修饰器请输入 2 \n'
          '测试天气查看请输入 3 (如果报错可能是代理的原因,关闭代理应该就可以了)\n'
          '输入你想测试的功能，退出请输入 0\n')
    s = input()

    if s == '0':
        break

    if s == '1':
        input_string = input(
            "请输入参数(例如: {\"int1\": {\"type\": \"float\", \"datarange\": (44, 77)}, \"int2\": {\"type\": \"int\", \"datarange\": (3, 6)}, \"int3\": {\"type\": \"int\", \"datarange\": (7, 100)}, \"num\": 5}):\n")
        s = DataSampling(**ast.literal_eval(input_string))
        print(s)

    elif s == '2':
        input_string = input(
            "请输入参数(例如: {\"int1\": {\"type\": \"float\", \"datarange\": (44, 77)}, \"int2\": {\"type\": \"int\", \"datarange\": (3, 6)}, \"int3\": {\"type\": \"int\", \"datarange\": (7, 100)}, \"num\": 5}):\n")
        s = structDataSampling(**ast.literal_eval(input_string))
        print(s)

    elif s == '3':
        print('输入样例: 长春 上海 广州')
        print('输入你想查看的城市，空格分隔多个城市')
        city = input().split()
        working(city)

    else:
        print('请确保输入符合要求')
