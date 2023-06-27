import random
import string
'''
:param num 代表生成随机列表项的个数
:param struct 代表传入的参数是个字典类型 
    例如：{int: {'datarange': ([1, 100], [1, 100])}}
    每一项的key是数据类型，包括[int,float,str]
    每一项的value是个字典类型，字典的key是"datarange",value是可迭代对象， 包括 [],()
'''
def structDataSampling(num, struct):
    result = list()
    for _ in range(num):
        element = list()
        for key, value in struct.items():
            for item in value['datarange']:
                if key is int:
                    it = iter(item)
                    tmp = random.randint(next(it), next(it))
                elif key is float:
                    it = iter(item)
                    tmp = random.uniform(next(it), next(it))
                elif key is str:
                    tmp = ''.join(random.SystemRandom().choice(
                        item[0]) for _ in range(item[1]))
                else:
                    raise TypeError("文本类型错误！！！")
                element.append(tmp)
        result.append(element)
    return result
def run():
    struct = {
        int: {'datarange': ([1, 100], [1, 100])},
        float: {'datarange': ((0.0, 10.0),)},
        str: {'datarange': ((string.ascii_letters, 3), ("sdsdhfjl", 5))}
    }
    data = structDataSampling(3, struct)
    print("产生随机列表的结果为：\n", data)
if __name__ == '__main__':
    run()


