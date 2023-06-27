# 姓名：徐腾飞
# 时间：2023/6/12 17:59
import random

def dataSampling(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value == 'int':
            result[key] = random.randint(0, 100)
        elif value == 'float':
            result[key] = random.uniform(0, 100)
        elif value == 'str':
            result[key] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    return result

# 调用示例
print(dataSampling(a='int', b='float', c='str'))