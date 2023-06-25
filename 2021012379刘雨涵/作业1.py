import random
import string

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


print(dataSampling(n=3, int={"datarange": (1, 10), "num": 3}, float={"datarange": (1, 100), "num": 2}, str={"num": 2, "strlen": 5}))

