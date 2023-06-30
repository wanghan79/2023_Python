import random


class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def OverError():
    raise MyException("操作码无效")


def structDataSampling(**kwargs):
    results = list()
    for item in range(0, kwargs['num']):
        result = list()
        for key, value in kwargs['struct'].items():
            if key is int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key is float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key is str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            result.append(tmp)
        results.append(result)
    print(f"生成的{kwargs['num']}组数据为{results}")
    return results


def addSum(arr):
    all = 0
    result = list()
    for i in range(0, len(arr)):
        tmp = 0
        for j in range(0, len(arr[i])):
            tmp += arr[i][j]
        result.append(tmp)
        all += tmp
        print(f"第{i + 1}组数据的总和为{tmp}")
    result.append(all)
    print(f"数据的总和为{all}")
    return result

def avg(arr):
    tmp = addSum(arr)
    all = 0
    for i in range(0, len(tmp) - 1):
        all += tmp[i]
        n = tmp[i] / len(arr[0])
        print(f"第{i + 1}组数据的平均值为{n}")
    ans = all / len(arr) / len(arr[0])
    print(f"总的平均值为{ans}")
    return ans


def dataProcess(*choice):
    def decorator(func):
        def wrapper(**kwargs):
            data = func(**kwargs)
            result = dict()
            result["data"] = data
            for item in choice:
                if item == "sum":
                    tmp = addSum(data)
                    result["sum"] = tmp[len(tmp) - 1]
                if item == "avg":
                    result["avg"] = avg(data)
            return result

        return wrapper

    return decorator


def run():
    print(f"请输入一个操作码，1代表求和，2代表求平均数，3代表两者都求,0退出该程序")
    while True:
        x = input()
        if x == '1':
            func1()
        elif x == '2':
            func2()
        elif x == '3':
            func3()
        elif x == '0':
            break
        else:
            try:
                OverError()
            except MyException as e:
                print('Error!', e)
                print("请重新输入一个数")


@dataProcess("sum")
def func1():
    return structDataSampling(num=5, struct={int: {'datarange': (0, 10)},
                                             float: {'datarange': (0, 1.0)}})


@dataProcess("avg")
def func2():
    return structDataSampling(num=5, struct={int: {'datarange': (0, 10)},
                                             float: {'datarange': (0, 1.0)}})


@dataProcess("sum", "avg")
def func3():
    return structDataSampling(num=5, struct={int: {'datarange': (0, 10)},
                                             float: {'datarange': (0, 1.0)}})


if __name__ == '__main__':
    run()
