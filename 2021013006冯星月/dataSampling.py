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
        'int': {
            'datatype': int,
            'range': [1, 10]
        },
        'float': {
            'datatype': float,
            'range': [1, 10]
        },
        'str': {
            'datatype': str,
            'range': "abcde",
            'len': 10
        },
        'int1': {
            'datatype': int,
            'range': [1, 10]
        },
        'int2': {
            'datatype': int,
            'range': [1, 10]
        },
    })
    print(x)