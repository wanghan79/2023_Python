
import random
import string

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


para2 = {"num":50,"dage":2, "struct":{float:{"datarange":(10.0,100.0)},int:{"datarange":(10,100)},str:{"datarange":"Python","len":10}}}

a=structDateSampling(**para2)



def show():
    print("-----------实现随机数据结构生成封装函数------------")
    print("-----------------调用示例-----------------")
    print("输入样例：")
    print(para2)
    print("输出结果：")
    print(a)

