import random
import string


def structDataSampling(**kwargs):
    results = list()      # 总序列
    for index in range(kwargs['num']):
        result = list()    # 单个随机元素的生成
        for key, value in kwargs['struct'].items():
            if key == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            result.append(tmp)
        results.append(result)
    return results


def dataProcess(*decargs):
    def decorator(func):    # 定义包装函数
        def wrapper(*args, **kwargs):      # 调用原始函数
            print("%s is running" % func.__name__)
            result = func(*args, **kwargs)
            avg = 0     #初始化平均值
            variable = 0      # 初始化变量
            count = 0      # 初始化计数变量
            for row in result:      # 循环遍历结果中的每一行
                for element in row:     # 遍历每行中元素
                    if isinstance(element, (int, float)):
                        variable = variable + element
                        count += 1
            avg = variable / count
            if "SUM" in decargs:
                print(f"The sum of these numbers is {variable:.3f}")
            if "AVG" in decargs:
                print(f"The average of these numbers is {avg:.1f}")
            return result

        return wrapper

    return decorator



@dataProcess("SUM")
def structDataSamplingResSUM(**kwargs):
    return structDataSampling(**kwargs)


@dataProcess("AVG")
def structDataSamplingResAVG(**kwargs):
    return structDataSampling(**kwargs)




para = {"num": 5,
        "struct": {
            int: {"datarange": [1, 100]},
            float: {"datarange": [1.0, 100.0]},
            str: {"datarange": string.ascii_letters, "len": 20}
        }
        }


print("SUM修饰器呈现的结果是：")
resultSUM = structDataSamplingResSUM(**para)
print("当前随机生成的序列是" + str(resultSUM) + '\n')

print("AVG修饰器呈现的结果是：")
resultAVG = structDataSamplingResAVG(**para)
print("当前随机生成的序列是" + str(resultAVG) + '\n')
