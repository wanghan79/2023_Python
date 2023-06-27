# 姓名：徐腾飞
# 时间：2023/6/13 16:24
import random



def dataStatistics(func):
    def wrapper(*args, **kwargs):
        data = func(**kwargs)
        sum_result = 0
        count = 0
        for key, value in data.items():
            if isinstance(value, (int, float)):
                sum_result += value
                count += 1
        avg_result = sum_result / count if count > 0 else 0
        if 'SUM' in args:
            print(f"SUM: {sum_result}")
        if 'AVG' in args:
            print(f"AVG: {avg_result}")
        return data
    return wrapper


@dataStatistics
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

#dataSampling = dataStatistics(dataSampling)

# 调用示例
dataSampling('SUM', a='int', b='float', c='str')