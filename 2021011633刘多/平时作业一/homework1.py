import random
import string


def dataSampling(**kwargs):
    num = kwargs.get('num')
    datatype = kwargs.get('datatype')
    datarange = kwargs.get('datarange')

    # 参数校验
    if num is None or not isinstance(num, int) or num <= 0:
        raise ValueError("参数 num 必须是一个大于0的整数")
    if datatype is None or not isinstance(datatype, list) or len(datatype) == 0:
        raise ValueError("参数 datatype 必须是一个非空列表")
    if datarange is None or not isinstance(datarange, list) or len(datarange) != 2:
        raise ValueError("参数 datarange 必须是一个长度为2的列表")

    result = []
    for _ in range(num):
        element = []
        for dt in datatype:
            if dt == 'int':
                element.append(random.randint(datarange[0], datarange[1]))
            elif dt == 'float':
                element.append(random.uniform(datarange[0], datarange[1]))
            elif dt == 'str':
                length = random.randint(datarange[0], datarange[1])
                element.append(''.join(random.choices(string.ascii_letters + string.digits, k=length)))
        result.append(element)

    return result


if __name__ == '__main__':
    # 调用示例
    struct = {
        'num': 10,
        'datatype': ['int', 'float', 'str'],
        'datarange': [0, 100]
    }
    generated_data = dataSampling(**struct)
    print("生成的随机数据结构如下：")
    for x in generated_data:
        print(x)
