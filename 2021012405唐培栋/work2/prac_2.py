
import random


def dataProcess(*args1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result1 = list()
            data=func(*args, **kwargs)
            data1 = adddata(data)
            data2 = AVGdata(data)
            for i in args1:
                if(i=="AVG"):
                    result1.append(data2)
                if(i=="SUM"):
                    result1.append(data1)
            return result1
        return wrapper
    return decorator


def adddata(data):
    sum = 0
    for j in range(50):
        for i in range(6):
            sum = sum + data[j][i]
    return sum

def AVGdata(data):
    sum = 0
    for j in range(50):
        for i in range(6):
            sum = sum + data[j][i]
    return sum/300

@dataProcess("AVG","SUM")
def structDateSampling(**kwargs):
    result = list()
    for index in range(kwargs['num']):
        element = list()
        for dj in range(kwargs['dage']):
            for key, value in kwargs['struct'].items():
                if key is int:
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it),next(it))
                elif key is float:
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key is str:
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    break
                element.append(tmp)
        result.append(element)
    return result


para2 = {"num":50,"dage":6, "struct":{float:{"datarange":(10.0,100.0)}}}

a=structDateSampling(**para2)



def show():
    print("Python 第二次作业：采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的求和（SUM），求均值（AVG）操作")
    print("******调用示例：******")
    print("输入样例：  ",para2)
    print("输出结果：  ",a)


