"""
    Author:Haizhu.Wu
    Title:Assignment2
"""
import random
import string

def dataprocess(*operations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = dict()
            data = func(*args, **kwargs)
            for operation in operations:
                if operation == 'AVG':  # 求平均数
                    result[operation] = sum(sum(element) for element in data) / (len(data) * len(data[0]))
                elif operation == 'SUM':  # 求和
                    result[operation] = sum(sum(element) for element in data)
                else:
                    raise Exception('wrong operation')
            return result
        return wrapper
    return decorator


@dataprocess('AVG', 'SUM')
def dataSampling(**kwargs):
    result = []
    for index in range(0, kwargs['num']):
        element = []
        for value in kwargs['struct']:
            if value['datatype'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['length']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

"""
作业二展示
"""
def show():
    kwargs = {
        "num": 5,
        "struct": [
             {"datatype": int, "datarange": (0, 1000)},
             {"datatype": int, "datarange": (0, 1000)},
             {"datatype": int, "datarange": (0, 1000)},
        ]
    }
    result = dataSampling(**kwargs)

    print(result)

if __name__ == "__main__":
    show()