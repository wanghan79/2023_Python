import random
import string

# 定义结构形式的数据抽样函数
def structDataSampling(num, struct):
    # 初始化结果列表
    result = list()
    # 根据设定的数量，执行指定次数的抽样
    for _ in range(num):
        # 每次抽样得到一个元素，即一个字典
        element = list()
        # 遍历传入的结构化数据
        for key, value in struct.items():
            # 针对每种数据类型的数据范围进行抽样
            for item in value['datarange']:
                # 根据数据类型，使用不同的生成随机数的方法
                if key is int:
                    # 对于整数类型，使用区间范围内的整数进行随机抽样
                    it = iter(item)
                    # 为了保证左闭右闭，需要使用 range 的下一个函数 next() 来生成范围内的整数
                    tmp = random.randint(next(it), next(it))
                elif key is float:
                    # 对于浮点数类型，使用区间范围内的浮点数进行随机抽样
                    it = iter(item)
                    # 为了保证左闭右开，需要使用 range 的下一个函数 next() 来生成范围内的随机数
                    tmp = random.uniform(next(it), next(it))
                elif key is str:
                    # 对于字符串类型，从指定的字符集合中随机选择指定长度的字符组成字符串
                    tmp = ''.join(random.SystemRandom().choice(
                        item[0]) for _ in range(item[1]))
                else:
                    # 如果类型不在指定的 int、float、str 中，则抛出异常并提示传入的数据类型有误。
                    raise TypeError("txt error")
                # 将生成的随机数加入到当前元素的列表中
                element.append(tmp)
        # 将当前元素（即字典）加入到结果列表中
        result.append(element)
    # 返回处理后的结果列表
    return result

# 调用函数生成数据
def main():
    # 定义结构化数据：包含三种基本类型的数据范围，以及相应的取值情况
    struct = {
        int: {'datarange': ([1, 100], [1, 100])},
        float: {'datarange': ((0.0, 100.0),)},
        str: {'datarange': ((string.ascii_letters, 3), ("sderghjiy", 5))}
    }
    # 使用 structDataSampling 函数生成数据
    data = structDataSampling(4, struct)
    # 输出生成的数据
    print("产生的随机列表为：\n", data)

if __name__ == '__main__':
    main()