# 在上次作业的基础上，生成50个六维向量，修饰器进行求和或者求均值（根据参数决定）
import random
from gqsJob.utils.math import average, getsum


def structDataSampling(num, struct):
    result = list()
    for index in range(0, num):
        element = list()
        for key, values in struct.items():
            for value in values["datarange"]:
                tmp = ''
                try:
                    if key is int:
                        it = iter(value)
                        tmp = random.randint(next(it), next(it))
                    elif key is float:
                        it = iter(value)
                        tmp = random.uniform(next(it), next(it))
                    elif key is str:
                        tmp = ''.join(random.SystemRandom().choice(values['datarange']) for _ in range(value['len']))
                    else:
                        break
                except (TypeError, ValueError) as res:
                    print("异常的基本信息是：", res)
                    print("random.*参数不匹配，请检查输入的类型与数据是否一致")
                    print()
                element.append(tmp)
        result.append(element)
    return result

# 参数改成*args
def aop():
    def decorator(function):  # 重点是为了传函数接口
        def wrapper(*args, **kwargs):  # 实际做事的部分，集成了修饰功能和老函数的功能
            # 老代码做的事
            temp = function(*args, **kwargs)
            # 新增加的功能
            print("求和输入1，求均值输入2，求和求均值输入3，其余无额外操作")
            choice = input()
            if choice == '1':
                print("修饰器求和")
                getsum(temp)
            elif choice == '2':
                print("修饰器求平均值")
                average(temp)
            elif choice == '3':
                print("修饰器求和以及平均值")
                getsum(temp)
                print("------------------------")
                average(temp)
            else:
                print("修饰器未工作")
            print('生成的数据是')
            print(temp)
            print('******************************************************************************************************************')
            return temp

        return wrapper  # 返回整体的wrapper，

    return decorator

@aop()
def func(num):
    return structDataSampling(num,
                              {int: {'datarange': ((1, 100), (0, 100), (0, 100))},
                               float: {"datarange": ((0, 1.0), (0, 5.0), (0, 6.0))}})

print("请输入num，表示生成num维数据")
num = int(input())
func(num)


