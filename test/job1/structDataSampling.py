import random
import re

# 随机数函数采样，如何合理动态参数调用
def dataSampling(datatype, datarange, num, strlen=8):
    result = set()
    for index in range(0, num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            result.add(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.add(item)
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)
            continue
        else:
            continue
    return result

def structDataSamplingSimple(num, struct):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in struct.items():
            if key is int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key is float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key is str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def structDataSamplingComplicated(**kwargs):
    result = list()
    num = kwargs.get("num", -1)
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "data":
                for data in value:
                    type = data.get('datatype')
                    tmp = 0
                    if type == "int":
                        it = iter(data['datarange'])
                        tmp = random.randint(next(it), next(it))
                    elif type == "float":
                        it = iter(data['datarange'])
                        tmp = random.uniform(next(it), next(it))
                    elif type == "str":
                        tmp = ''.join(random.SystemRandom().choice(data['datarange']) for _ in range(data['len']))
                    element.append({type: tmp})
            elif key == "num":
                continue
            else:
                break
            result.append(element)
    return result

# json数据传入处理
import json
data = dict()
def func():
    print("请将需要传输的关键字参数以json文件形式传入，并且把文件放在input文件夹下")
    print("请输入文件名(可以不加后缀)，可以使用structDataSamplingComplicated.json")
    filename = input()
    # 匹配输入是否有json
    if re.match("^[\s\S]*\.(json)$", filename):
        filename = filename
    else:
        filename = filename + ".json"
    try:
        with open("../gqsJob/input/" + filename, 'r', encoding='UTF-8') as f:
            data = json.loads(f.read())
        return data
    except (FileNotFoundError,UnboundLocalError) as res:
        print("异常的基本信息是：", res)
        print("请查看文件名是否输入有误")
        print()

# 第一个
print("执行：print(dataSampling(int, [1, 9], 4, 2))")
print(dataSampling(int, [1, 9], 4, 2))
print("执行：print(dataSampling(float, [1, 10], 4, 2))")
print(dataSampling(float, [1, 10], 4, 2))
print("执行：print(dataSampling(str, ['a','b'], 10, 2))")
print(dataSampling(str, ['a', 'b'], 10, 2))
print("执行：print(dataSampling(str, ['a','b','c','d'], 10))")
print(dataSampling(str, ['a', 'b', 'c', 'd'], 10))
print('******************************************************************************************************************')

# 第二个
# 正常数据
struct1 = {int: {'datarange': [1, 9], 'len': 10}}
# 异常数据
struct2 = {int: {'datarange': [1.3, 9], 'len': 10}}
print("执行：print(structDataSamplingSimple(4, struct1))")
print(structDataSamplingSimple(4, struct1))
print('******************************************************************************************************************')

# 第三个
print(structDataSamplingComplicated(**func()))