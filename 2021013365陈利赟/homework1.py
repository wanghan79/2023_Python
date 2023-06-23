#chengly
"""
作业1要求：
实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
1.	采用关键字参数作为随机数据结构及数量的输入；
2.	在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
3.	其中随机数涵盖int，float和str三种类型。
"""

"""
作业1代码部分展示：
"""
import random
import string
def struct_data_sampling(num, struct):
    result = []
    for _ in range(num):
        item = []
        for key, value in struct.items():
            if key == int:
                item.append(random.randint(value['datarange'][0], value['datarange'][1]))
            elif key == float:
                item.append(random.uniform(value['datarange'][0], value['datarange'][1]))
            elif key == str:
                item.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            else:
                break
        result.append(item)
    return result

"""
作业1结果部分展示：
"""
def show1():
    print("示例：生成5组随机数，每组随机数含有1个int型数据，1个float型数据和一个字符串")
    print("展示如下：")
    try:
        result = (struct_data_sampling #参数部分
                (5,{
                    #int：
                    int: {'datarange': (0,10)},
                    #str：
                    str: {'datarange': string.ascii_letters.format("&*_"), 'len': 10},
                    #float：
                    float: {'datarange': (0, 1.0)}
                })
            )
        print(result)
    except(TypeError,KeyError):
        print("参数格式错误，请输入正确的参数:格式为: 整数,{int or float or str : {'datarange':(0,100)}}")
    else:
        print('程序执行成功!')

if __name__ == "__main__":
    show1()