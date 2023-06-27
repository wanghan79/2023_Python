import random
import string


def structDataSampling(**kwargs):
    results = list()      # 总序列
    for item in range(kwargs['num']):
        result = list()    # 单个随机元素的生成
        for key, value in kwargs['struct'].items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            result.append(tmp)
        results.append(result)
    return results


para = {"num": 5, "struct": {"int": {'datarange': (1, 10)},
                             "str": {'datarange': string.ascii_letters.format("&*_"), 'len': 10},
                             "float": {'datarange': (1.0, 10)}}}
print(structDataSampling(**para))
# **会在函数调用的时候，把相应的字典打包成键值对，然后把解包后数据传回去
