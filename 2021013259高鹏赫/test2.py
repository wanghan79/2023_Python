# 导入random和string库
import random
import string

# 定义装饰器函数
def datasampling(*args):
    def decorator(func):
        # 定义子函数wrapper
        def wrapper(*w_args, **kwargs):
            # 调用原始函数并获取结果
            result = func(*w_args, **kwargs)
            # 遍历参数列表args，分别执行不同的操作
            if "SUM" in args:
                # 计算结果中所有int和float元素的总和
                total_sum = 0
                for res in result:
                    for key,value in res.items():
                        if isinstance(value, list):
                            for item in value:
                                if isinstance(item, (int, float)):
                                    total_sum += item
                print("总和为:", total_sum)
            if "AVG" in args:
                # 计算结果中所有int和float元素的平均值
                total_sum = 0
                total_count = 0
                for res in result:
                    for key, value in res.items():
                        if isinstance(value, list):
                            for item in value:
                                if isinstance(item, (int, float)):
                                    total_sum += item
                            total_count += len(value)
                print("平均值为:", total_sum / total_count)
            # 返回原始函数的结果
            return result
        # 返回子函数wrapper
        return wrapper
    # 返回装饰器函数decorator
    return decorator

# 装饰的原始函数
@datasampling('SUM', 'AVG')
def getrandomdata(**kwargs):
    # 定义一个列表，存放生成的数据样本
    result = []
    # 重复生成n个数据样本
    for i in range(kwargs["n"]):
        # 定义一个字典，存放一个数据样本
        res = {}
        # 遍历所传递的关键字参数
        for key, value in kwargs.items():
            # 如果关键字参数是n，则跳过不做处理
            if key == "n":
                continue
            # 如果关键字参数是int，则生成指定数量和范围的随机整数
            if key == "int":
                datarange = value["datarange"]
                num = value["num"]
                res[key] = [random.randint(*datarange) for _ in range(num)]
            # 如果关键字参数是float，则生成指定数量和范围的随机浮点数
            elif key== "float":
                datarange = value["datarange"]
                num = value["num"]
                res[key] = [random.uniform(*datarange) for _ in range(num)]
            # 如果关键字参数是str，则生成指定数量和长度的随机字符串
            elif key== "str":
                num = value["num"]
                strlen = value["strlen"]
                res[key] = [''.join(random.choices(string.ascii_letters + string.digits, k=strlen)) for _ in range(num)]
            else:
                # 抛出异常，表示无法识别的数据类型
                raise ValueError("Unrecognized data type: {}".format(k))
        # 将生成的一个数据样本加入到结果列表中
        result.append(res)
    # 返回结果列表
    return result

# 定义展示函数
def show():
    # 调用装饰后的原始函数，生成数据样本，并传递给该函数的关键字参数
    print(getrandomdata(n=3, int={"datarange": (1, 5), "num": 3}, float={"datarange": (1, 50), "num": 2}, str={"num": 2, "strlen": 10}))
show()