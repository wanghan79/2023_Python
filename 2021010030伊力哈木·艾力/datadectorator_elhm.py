import random
import string


def calSumAndAvg(*args):
    def decorator(func):
        def wrapper(*w_args, **kwargs):
            result = func(*w_args, **kwargs)
            if "SUM" in args:
                total_sum = 0
                for resort in result:
                    for k, v in resort.items():
                        if isinstance(v, list):
                            for item in v:
                                if isinstance(item, (int, float)):
                                    total_sum += item
                print("Total sum:", total_sum)
            if "AVG" in args:
                total_sum = 0
                total_count = 0
                for resort in result:
                    for k, v in resort.items():
                        if isinstance(v, list):
                            for item in v:
                                if isinstance(item, (int, float)):
                                    total_sum += item
                            total_count += len(v)
                print("Average:", total_sum / total_count)
            return result
        return wrapper
    return decorator



@calSumAndAvg('SUM', 'AVG')  #在此可以指定需要进行的计算
def dataSampling(**kwargs):
    result = []
    for i in range(kwargs["n"]):
        res = {}
        for k, v in kwargs.items():
            if k == "n":
                continue
            if k == "int":
                datarange = v["datarange"]
                num = v["num"]
                res[k] = [random.randint(*datarange) for _ in range(num)]
            elif k == "float":
                datarange = v["datarange"]
                num = v["num"]
                res[k] = [random.uniform(*datarange) for _ in range(num)]
            elif k == "str":
                num = v["num"]
                strlen = v["strlen"]
                res[k] = [''.join(random.choices(string.ascii_letters + string.digits, k=strlen)) for _ in range(num)]
            else:
                raise ValueError("Unrecognized data type: {}".format(k))
        result.append(res)
    return result


print(dataSampling(n=3, int={"datarange": (0, 100), "num": 3}, float={"datarange": (0, 100), "num": 2}, str={"num": 2, "strlen": 6}))