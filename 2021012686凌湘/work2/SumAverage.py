import sys
sys.path.append("../work1/")
sys.path.append("work1/")
from DataSampling import structDataSampling as fun_StructRandom
def dataProcess(*decorator_args):
    # 传入被修饰的函数
    def decorator(func):
        def wrapper(*args):
            temp = func(*args)
            result= [item for sublist in temp for item in sublist]
            for item in result:
                if isinstance(item, int) or isinstance(item, float):
                    continue
                else:
                    raise TypeError("数据格式是非数值，不能参与运算！！请修改结构体传参格式！")
            total = sum(result)
            average = total / len(result)
            for dec_arg in decorator_args:
                if dec_arg == "avg":
                    print("生成的随机列表为：\n", temp)
                    print("avg；\n", average)
                    return average
                if dec_arg == "sum":
                    print("生成的随机列表为：\n", temp)
                    print("sum：\n", total)
                    return total
                elif dec_arg == "all":
                    print("生成的随机列表为：\n", temp)
                    print("列表数据求和 sum：\n", total)
                    print("列表数据均值 avg：\n", average)
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
        # str: {'datarange':(("hahaha",3),)}
        # 此处传入字符串目的是验证是否抛出异常
    }
    print("选择修饰器实现的功能：")
    print("输入 avg 代表对随机数进行求平均值")
    print("输入 sum 代表对随机数进行求和")
    print("输入 all 代表呈现随机数组并显示求和与平均值的结果")
    choose_type = input("输入你的选择： ")
    @dataProcess(choose_type)
    def structDataSampling(num, struct):
        return fun_StructRandom(num, struct)
    structDataSampling(3, struct)
if __name__ == '__main__':
    run()

