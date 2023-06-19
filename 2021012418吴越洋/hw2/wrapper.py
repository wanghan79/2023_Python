import random
from dataSampling import *


def funDecorator(*args):
    modes = args

    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            num = 0
            s = 0
            for li in res:
                for _, v in li.items():
                    if type(v) == int or type(v) == float:
                        s += v
                        num += 1
            ans = []
            for mode in modes:
                if mode == 'mean':
                    ans.append(s / num)
                elif mode == 'sum':
                    ans.append(s)
            return ans, res

        return wrapper

    return decorator


@funDecorator("sum", 'mean')
def foo(**kwargs):
    res = dataSampling(**kwargs)
    return res


if __name__ == '__main__':
    data, x = foo(num=2, struct={
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
    print(data)
