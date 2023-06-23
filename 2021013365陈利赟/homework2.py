#chengly
"""
作业2要求：
采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的求和（SUM），求均值（AVG）操作，以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：
1.	修饰器类型不限，可以是函数修饰器或类修饰器；
2.	只能实现一个修饰器，通过修饰器参数（*args）实现SUM和AVG操作的任意组合，即修饰器在接收0、1、2个参数的情况下都可以正常运行；
"""

"""
作业2代码部分展示：
"""
import random
import logging

def sum(a):
    result = list()
    sum = 0
    for i in range(0,len(a[0])):
        for j in range(0,len(a)):
            sum += a[j][i]
    return sum


def avg(a):
    result=sum(a)
    return result/len(a[0])


def addlogging(*oder):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a = list()
            result = func(*args, **kwargs)
            for item in oder:
                if item == "sum":
                    a.append(sum(result))
                if item == "avg":
                    a.append(avg(result))
            return a
        return wrapper
    return decorator


@addlogging("sum", "avg")
def structDataSampling(struct):
    result = list()
    for i in range(0, struct['num']):
        element = list()
        for key in struct["datatype"]:
            if key == "int":
                it = iter(struct['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "float":
                it = iter(struct['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(struct['datarange'] )for _ in range(struct['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

"""
作业2结果部分展示：
"""
def show2():
    print("示例：生成50组随机数，每组4个loat数据,1个int数据,并对生成的随机数求和,求均值")
    print("第一个数为和，第二个数为均值")
    print("展示如下：")
    try:
        result = structDataSampling({"num": 50,
                                    "datatype":["float", "float", "float", "int", "float"], "datarange": [0, 50]
                                    })
        print(result)
    except(TypeError,KeyError):
        print("参数格式错误，请输入正确的格式！")
    else:
        print('程序执行成功!')

if __name__ == "__main__":
    show2()