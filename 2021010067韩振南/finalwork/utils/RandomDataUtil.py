import random


def dataSampling(dataType, datarange, num, strlen=8):
    """
    :Description: 获取相应类型的随机数
    :param dataType: 需要获取的随机数的类型
    :param dataange: 随机数范围
    :param num: 生成随机数的个数
    :param strlen: 字符随机数的长度
    :return:
    """
    result = set()
    for index in range(0, num):
        if dataType is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
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
    """
   :Description: 获取相应结构体的随机数
   :param num: 获取随机数的数量
   :param struct: 目标结构体
   :return:
    """
    result = list()
    for index in range(0, num):
        element = list()
        for key, values in struct.items():
            for value in values["datarange"]:
                if key is int:
                    it = iter(value)
                    tmp = random.randint(next(it), next(it))
                elif key is float:
                    it = iter(value)
                    tmp = random.uniform(next(it), next(it))
                elif key is str:
                    tmp = ''.join(random.SystemRandom().choice(value[0]) for _ in range(value[1]))
                else:
                    break
                element.append(tmp)
        result.append(element)
    return result
