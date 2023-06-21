import random
from DataSampling import DataSampling
from decorator import structDataSampling
from weather import working
import ast

print('测试生成随机数请输入 1\n'
      '测试修饰器请输入 2 \n'
      '测试天气查看请输入 3 (如果报错可能是代理的原因,关闭代理应该就可以了)\n'
      '输入你想测试的功能\n')
s = input()
if s == '1':
    # 输入示例: {"int1": {"type": "float", "datarange": (44, 77)}, "int2": {"type": "int", "datarange": (3, 6)}, "int3": {"type": "int", "datarange": (7, 100)}, "num": 5}
    input_string = input("请输入参数(例如: {\"int1\": {\"type\": \"float\", \"datarange\": (44, 77)}, \"int2\": {\"type\": \"int\", \"datarange\": (3, 6)}, \"int3\": {\"type\": \"int\", \"datarange\": (7, 100)}, \"num\": 5}):\n")
    s = DataSampling(**ast.literal_eval(input_string))
    print(s)
elif s == '2':
    # 输入示例: {"int1": {"type": "float", "datarange": (44, 77)}, "int2": {"type": "int", "datarange": (3, 6)}, "int3": {"type": "int", "datarange": (7, 100)}, "num": 5}
    input_string = input(
        "请输入参数(例如: {\"int1\": {\"type\": \"float\", \"datarange\": (44, 77)}, \"int2\": {\"type\": \"int\", \"datarange\": (3, 6)}, \"int3\": {\"type\": \"int\", \"datarange\": (7, 100)}, \"num\": 5}):\n")
    s = structDataSampling(**ast.literal_eval(input_string))
    print(s)


elif s == '3':
    print('输入样例:'
          '长春 上海 广州')
    print('输入你想查看的城市')
    city = input().split()
    working(city)

else:
    print('请确保输入符合要求')
