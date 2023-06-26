# 随机数生成
import random
import string


def dataSampling(dataType, datarange, num, strlen = 8):
    """
    :Description: 获取相应类型的随机数
    :param dataType: 需要获取的随机数的类型
    :param datarange: 随机数范围
    :param num: 生成随机数的个数
    :param strlen: 字符随机数的长度
    :return:
    """
    result = set()
    for index in range(0, num):
        if dataType is int:
            it = iter(datarange)
            item = random.randint(next(it),next(it))
            result.add(item)
            continue
        elif dataType is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.add(item)
            continue
        elif dataType is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)
            continue
        else:
            continue
    return result

def structDataSampling(num, struct):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in struct.items():
            tmp=dataSampling(key,value['datarange'],1)
            element.append(tmp)
        result.append(element)
    return result

print(structDataSampling(10, {int:{'datarange':(0,10)},str:{'datarange':string.ascii_letters.format("&*_"),'len':10},float:{'datarange':(0,1.0)}}))
print(dataSampling(int,(0,100), 3))
print(dataSampling(float, (0.0, 1.0), 10))
print(dataSampling(str, string.ascii_letters.format("&*_"), 10))