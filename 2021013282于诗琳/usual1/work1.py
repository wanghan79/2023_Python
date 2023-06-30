import string
import random
def structDataSampling(num,**kwargs):
    result = list()
    for index in range(0,num):
        element = list()
        for key,value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it),next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

def SJwork_1():
    print("练习1: ")
    print("案例测试（生成3种，共5个随机数）：")
    num = 5
    c = {"int":{"datarange":(0,100)},"float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_letters,"len":50}}
    d = structDataSampling(num,**c)
    print(d)
    print("随机测试：")
    type = input("请输入数据类型: ")
    type = str(type)
    num = input("请输入生成数的个数： ")
    num = int(num)
    if type == "int" or type == "float":
        irange = input("请输入生成数最小边界： ")
        arange = input("请输入生成数最大边界：")
        irange = int(irange)
        arange = int(arange)
    if type == "str":
        mrange = input("请输入生成数据的范围： ")
        mrange = int (mrange)
    if type == "float":
        a = {"float":{"datarange":(irange,arange)}}
    if type == "int":
        a = {"int":{"datarange":(irange,arange)}}
    if type == "str":
        a = {"str":{"datarange":string.ascii_letters,"len":mrange}}
    b=structDataSampling(num,**a)
    print(b)


SJwork_1()
