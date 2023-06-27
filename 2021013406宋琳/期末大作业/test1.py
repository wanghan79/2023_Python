#songlin_test_1_随机数生成
import random
import string

def DataSampling(**kwargs):
    """
    :param kwargs:
    :return:
    """
    result = list()
    for index in range(0,kwargs["num"]):
        element = list()
        for key in kwargs.get("struct"):
            if key["datatype"] == "int":
                it = iter(key["datarange"])
                tmp = random.randint(next(it),next(it))
            elif key["datatype"] == "float":
                it = iter(key["datarange"])
                tmp = random.uniform(next(it), next(it))
            elif key["datatype"] =="str":
                tmp = ''.join(random.SystemRandom().choice(key["datarange"]) for _ in range(key["len"]))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

def result_1():
    s = DataSampling(
            num=3,
            struct=(
                {
                    'datatype': "int",
                    'datarange': (0, 100)
                },
                {
                    'datatype': "float",
                    'datarange': (0, 100)
                },
                {
                    'datatype': "str",
                    'datarange': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    'len': 5
                }
            )
        )
    print("生成的随机数如下：")
    print(s)


if __name__ == '__main__':
    result()

