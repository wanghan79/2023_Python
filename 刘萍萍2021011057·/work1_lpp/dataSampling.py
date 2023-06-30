import random
import string


def dataSampling(**kwargs):
    result = []
    structure = kwargs.get('struct')
    num = kwargs.get('num')
    for _ in range(num):
        element = {}
        for key, value in structure.items():
            data_type = value['datatype']
            if data_type == int:
                data_range = value['range']
                element[key] = random.randint(data_range[0], data_range[1])
            elif data_type == float:
                data_range = value['range']
                element[key] = random.uniform(data_range[0], data_range[1])
            elif data_type == str:
                data_range = value['range']
                length = value['len']
                element[key] = ''.join(random.choices(data_range, k=length))
        result.append(element)
    return result


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
            'range': string.ascii_lowercase,
            'len': 10
        },
        '123': {
            'datatype': int,
            'range': [1, 10]
        },
        '111': {  # 异常处理
            'datatype': int,
            'range': [1, 10]
        },
    })
    print(x)
