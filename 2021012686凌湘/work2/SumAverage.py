import sys
sys.path.append("../work1/")
sys.path.append("work1/")
from DataSampling import structDataSampling as fun_StructRandom
def dataProcess(*decorator_args):
    def decorator(func):
        def wrapper(*args):
            temp = func(*args)
            result= [item for sublist in temp for item in sublist]
            for item in result:
                if isinstance(item, int) or isinstance(item, float):
                    continue
                else:
                    raise TypeError("数据格式错误！")
            total = sum(result)
            average = total / len(result)
            for dec_arg in decorator_args:
                if dec_arg == "avg":
                    print("随机列表为：\n", temp)
                    print("avg；\n", average)
                    return average
                if dec_arg == "sum":
                    print("随机列表为：\n", temp)
                    print("sum：\n", total)
                    return total
                elif dec_arg == "all":
                    print("随机列表为：\n", temp)
                    print("求和 sum：\n", total)
                    print("求均值 avg：\n", average)
                    obj = {
                        "result": temp,
                        "total": total,
                        "average": average,
                    }
                    return obj
                else:
                    raise ValueError("Invalid args")
        return wrapper
    return decorator
def run():
    struct = {
        int: {'datarange': ([1, 100], [1, 100])},
        float: {'datarange': ((0.0, 10.0),)},
    }
    #输入 avg 对随机数求均值
    #输入 sum 对随机数求和
    #输入 all 显示随机数组以及求和与均值的结果
    choose_type = input("请输入： ")
    @dataProcess(choose_type)
    def structDataSampling(num, struct):
        return fun_StructRandom(num, struct)
    structDataSampling(3, struct)
if __name__ == '__main__':
    run()

