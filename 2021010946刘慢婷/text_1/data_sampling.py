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