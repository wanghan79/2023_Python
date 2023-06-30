import random

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

# 测试数据
struct1 = {
    'fieldname1': {
        'datatype': 'int',
        'datarange': [1, 100]
    },
    'fieldname2': {
        'datatype': 'str',
        'datarange': 'abcdefghijklmnopqrstuvwxyz',
        'len': 5
    },
    'fieldname3': {
        'datatype': 'float',
        'datarange': [0, 1]
    }
 }

samples1 = datasampling(num=10, struct=struct1)
print(samples1)

'''
 函数使用关键字参数**kwargs来接收输入。

 函数从关键字参数中获取一个名为num的参数，用于指定要生成的样本数量（默认为-1）。

 如果未提供num参数，函数将引发异常并显示"Missing Parameter num!"。

 函数从关键字参数中获取一个名为struct的参数，用于指定样本的结构（数据类型和范围）。

 如果未提供struct参数，函数将引发异常并显示"Missing Parameter struct!"。

 函数生成指定数量的样本，每个样本的结构由struct参数定义。

 每个样本的元素根据其对应的数据类型和范围生成随机值。

 生成的样本以列表的形式返回。

 示例中的测试数据struct1包含了三个字段的定义，分别是一个整数字段、一个字符串字段和一个浮点数字段。每个字段具有相应的数据类型和范围。
'''
