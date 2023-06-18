import string
import random


def structDataSampling(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

#主函数
print('示例数据：生成5个int型且范围0~10的随机数')
a = {'int': {"datarange": (0, 10)}}
b = structDataSampling(5, **a)
print(b)

type = input("请输入目标随机数的数据类型： ")
num = int(input("请输入目标个数："))

if type == "int" or type == "float":
    irange = int(input("请输入下边界："))
    arange = int(input("请输入上边界："))
    a = {type: {"datarange": (irange, arange)}}
if type == "str":
    mrange = int(input("请输入字符串的长度： "))
    a = {type: {"datarange": string.ascii_letters, "len": mrange}}

b = structDataSampling(num, **a)
print(b)
