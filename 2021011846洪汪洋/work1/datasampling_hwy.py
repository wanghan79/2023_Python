import random


def dataSampling(**kwargs):
    result = list()
    num = int(kwargs.get("num", 0))
    len = int(kwargs.get("len", 1))
    if num < 0:
        raise ValueError("num cannot be negative")
    if len <= 0:
        raise ValueError("len cannot be less than 1")
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(len))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def show():
    print(f"""案例展示
    {dataSampling(num=50, len=3,
                 int={
                     'datarange': [1, 100]
                 },
                 float={
                     'datarange': [0.1, 10.0]
                 },
                 str={
                     'datarange': ['a', 'b', 'c']
                 }
                 )}
                 """)

if __name__ == '__main__':
    show()
    print("————————————以下为用户输入内容——————————")
    element = {}
    type_num = int(input("请输入随机数种类的个数"))
    while type_num > 0:
        type = input("请输入数据类型: 1.int, 2.float 3.str")
        if type == "1":
            irange = input("请输入随机数最小值：")
            arange = input("请输入随机数最大值：")
            try:
                irange = int(irange)
                arange = int(arange)
                if irange - arange > 0:
                    print("最大值要大于等于最小值")
                    continue
            except:
                print("类型错误,重新输入")
            tmp = {"int":{"datarange": (irange, arange)}}
            element.update(tmp)
            type_num = type_num - 1
            continue
        elif type == "2":
            irange = input("请输入随机数最小值：")
            arange = input("请输入随机数最大值：")
            try:
                irange = float(irange)
                arange = float(arange)
                if irange - arange > 0:
                    print("最大值要大于等于最小值")
                    continue
            except:
                print("类型错误,重新输入")
            tmp = {"float": {"datarange": (irange, arange)}}
            element.update(tmp)
            type_num = type_num - 1
            continue
        elif type == "3":
            str_range = list()
            str_range = input("请输入随机数范围")
            str_range_list = [char for char in str_range]
            Len = int(input("请输入字符长度"))
            tmp = {"str": {"datarange": str_range_list}}
            element.update(tmp)
            element.update(len = Len)
            type_num = type_num - 1
            continue
        else:
            print("请输入数字1、2、3！")
    Num = input("请输入生成随机数个数")
    element.update(num = Num)

    print(dataSampling(**element))