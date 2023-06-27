import random
import string

class StatisticAnalysis:
    """

    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        data = self.func(*args, **kwargs)
        if len(args) == 0:
            return data
        elif len(args) == 1 and args[0] == 'SUM':
            return sum(data)
        elif len(args) == 1 and args[0] == 'AVG':
            return sum(data) / len(data)
        elif len(args) == 2 and args[0] == 'SUM' and args[1] == 'AVG':
            return sum(data), sum(data) / len(data)
        else:
            raise ValueError('Invalid argument')

@StatisticAnalysis
def dataSampling(**kwargs):
    """
        用于生成随机数据的函数
        :param kwargs: 在调用该函数时传入的关键字参数
        :return: 生成好的随机数据结构
    """
    result = []
    choices = string.ascii_letters + string.digits

    for key, value in kwargs.items():
        if type(value) is int:
            result.extend(random.sample(range(1, 101), value))  # 随机生成1~100之间的整数
        elif type(value) is float:
            result.extend([random.uniform(0, 1) for _ in range(value)])  # 随机生成0~1之间的浮点数
        elif type(value) is str:
            result.extend([''.join(random.sample(choices, 6)) for _ in range(value)]) # 随机生成6位的字符串
    return result

data = dataSampling(int=20, float=10, str=5)
print(data)

sum_avg_data = dataSampling('SUM', 'AVG', int=20)
print(sum_avg_data)

invalid_data = dataSampling('MAX', int=20)
print(invalid_data)