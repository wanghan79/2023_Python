import random

def dataProcess(*args):
    # use data_args variable to store args
    data_args = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            result = []
            if 'AVG' in data_args:
                s = sum(sum(_) for _ in data)
                result.append(s / (len(data) * len(data[0])))
            if 'SUM' in data_args:
                s = sum(sum(_) for _ in data)
                result.append(s)
            return result
        return wrapper
    return decorator

@dataProcess('SUM', 'AVG')
def datasampling(*args, **kwargs):
    result = []
    n = kwargs.get('num', -1)
    if n == -1:
        raise Exception('Missing Parameter num!')
    Item = kwargs.get('struct', None)
    if Item is None:
        raise Exception('Missing Parameter struct!')
    for _ in range(n):
        element = []
        for key, value in Item.items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)

    return result

structure = {
    '1': {'datatype': 'float', 'datarange': (18, 65), 'len': None},
    '2': {'datatype': 'float', 'datarange': (18, 65), 'len': None},
    '3': {'datatype': 'float', 'datarange': (18, 65), 'len': None},
    '4': {'datatype': 'float', 'datarange': (18, 65), 'len': None},
    '5': {'datatype': 'float', 'datarange': (18, 65), 'len': None},
    '6': {'datatype': 'float', 'datarange': (18, 65), 'len': None},
}

f = datasampling(num=50, struct = structure)
print(f)

'''
    dataProcess 函数是一个装饰器，接受可变参数 (*args)。在 dataProcess 函数内部，参数被存储在 data_args 变量中。

    decorator 函数定义在 dataProcess 内部，它接受一个函数 func 作为参数。

    wrapper 函数定义在 decorator 内部，它接受任意数量的位置参数和关键字参数 (*args 和 **kwargs)。

    在 wrapper 函数中，装饰的函数 (func) 使用提供的参数 (*args 和 **kwargs) 进行调用，并将结果存储在 data 变量中。

    result 列表被初始化以存储处理结果。

    如果字符串 'AVG' 出现在 data_args 中（也就是传递给 dataProcess 装饰器的参数），代码将使用嵌套的列表推导计算 data 列表中所有元素的平均值。然后将平均值添加到 result 列表中。

    如果字符串 'SUM' 出现在 data_args 中，代码将使用嵌套的列表推导计算 data 列表中所有元素的和。然后将和添加到 result 列表中。

    wrapper 函数返回 result 列表。

    wrapper 函数被 decorator 函数返回。

    decorator 函数被 dataProcess 函数返回。

    datasampling 函数使用 @dataProcess('SUM', 'AVG') 进行装饰，这意味着 datasampling 函数将被处理以计算总和和平均值。

    datasampling 函数根据提供的结构和指定的样本数量 (num) 生成随机样本。它创建一个包含多个列表的列表 (result)，其中每个列表表示一个样本。

    生成的样本基于 structure 字典，该字典定义了每个属性的数据类型和数据范围。datatype 可以是 'int'、'float' 或 'str'。样本根据给定的数据范围生成。

    最后，使用 print(f) 打印生成的样本。
'''
