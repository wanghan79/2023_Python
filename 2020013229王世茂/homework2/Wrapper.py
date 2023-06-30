import random

def dataProcess(*args):
    # use data_args variable to store args
    data_args = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            result = {}
            result['origin_data'] = data
            for opt in data_args:
                if opt == 'AVG':
                    s = sum(sum(_) for _ in data)
                    result['AVG'] = s / (len(data) * len(data[0]))
                if opt == 'SUM':
                    s = sum(sum(_) for _ in data)
                    result['SUM'] = s
            return result
        return wrapper
    return decorator

@dataProcess('SUM', 'AVG')
def datasampling(**kwargs):
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
    '1': {'datatype': 'float', 'datarange': [18, 65]},
    '2': {'datatype': 'float', 'datarange': [18, 65]},
}

f = datasampling(num=2, struct = structure)
print(f)
'''
装饰器函数decorator接受一个函数func作为参数，并定义了一个内部函数wrapper。在wrapper函数中，首先调用被装饰函数func，并将返回的数据存储在变量data中。

接下来，创建一个空字典result，并将原始数据存储在键为'origin_data'的项中。

然后，遍历装饰器函数的参数data_args，对于每个选项，如果选项为'AVG'，则计算数据的平均值，并将结果存储在键为'AVG'的项中。如果选项为'SUM'，则计算数据的总和，并将结果存储在键为'SUM'的项中。

最后，返回结果字典result。

在datasampling函数中，根据传入的参数生成样本数据。样本数据的数量由num参数确定，数据结构由struct参数指定。根据每个字段的数据类型和范围，使用随机函数生成对应类型的数据，并将数据存储在result列表中。
'''
