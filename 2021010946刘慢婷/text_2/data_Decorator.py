import random
def Struct_DataSampling(**kwargs):
    result = list()
    for index in range(kwargs["num"]):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def structdataSampling_1():
    print("Python第一次作业：实现随机数据结构生成封装函数dataSampling(**kwargs）。")
    print("*******************获取结果如下：***********************")
    a = Struct_DataSampling(num=5,
                            struct={int: {'datarange': (0, 100)},
                                    float: {'datarange': (0.0, 100.0)},
                                    str: {'datarange':"abcdefghsyc", 'len': 5}
                                   }
                           )
    for i in a:
        print(i)

if __name__ == '__main__':
    structdataSampling_1()


def struct_sum(data):
    sum = 0
    for i in range(len(data[0])):
        for j in range(len(data)):
            sum = sum + data[j][i]
    return sum


def dataProcess(*arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = list()
            data = func(*args, **kwargs)
            for a in arg:
                if a == "sum":
                    x.append(struct_sum(data))
                elif a == "avg":
                    x.append(struct_sum(data) / len(data) / len(data[0]))
            return x, data

        return wrapper

    return decorator


@dataProcess("sum", "avg")
def data_decorator(**kwargs):
    result =Struct_DataSampling(**kwargs)
    return result


def data_decorator_2():
    print(
        "Python第二次作业：采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的求和（SUM），求均值（AVG）操作。")
    print("*******************获取结果如下：***********************")

    a = data_decorator(
        num=5,
        struct={
            int: {'datarange': (1, 100)},
            float: {'datarange': (1.0, 100.0)}
        }
    )
    print(a)


if __name__ == '__main__':
    data_decorator_2()
