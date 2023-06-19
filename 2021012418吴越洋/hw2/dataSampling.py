import random


def dataSampling(**kwargs):
    res = list()
    structure = kwargs.get('struct')
    structure = structure.items()
    for i in range(kwargs.get('num')):
        element = dict()
        for k, v in structure:
            try:
                if v['datatype'] == int or v['datatype'] == 'int':
                    it = iter(v['range'])
                    tmp = random.randint(next(it), next(it))
                elif v['datatype'] == float or v['datatype'] == 'float':
                    it = iter(v['range'])
                    tmp = random.uniform(next(it), next(it))
                elif v['datatype'] == str or v['datatype'] == 'str':
                    tmp = ''.join(random.SystemRandom().choice(v['range']) for _ in range(v['len']))
                else:
                    break
                element[k] = tmp
            except:
                pass
        res.append(element)
    return res


if __name__ == '__main__':
    x = dataSampling(num=2, struct={
        'a': {
            'datatype': int,
            'range': [1, 10]
        },
        'b': {
            'datatype': float,
            'range': [1, 10]
        },
        'c': {
            'datatype': str,
            'range': "abcde",
            'len': 10
        },
        '123': {
            'datatype': int,
            'range': [1, 10]
        },
        '111': {  # 异常处理
            'datatype': int,
            'ran2ge': [1, 10]
        },
    })
    print(x)
