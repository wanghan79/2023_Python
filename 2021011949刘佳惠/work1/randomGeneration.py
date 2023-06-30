import string
import random


def structDataSampling(**kwargs):
    """
    :param num:
    :param kwargs:
    :return:
    """
    result = list()
    for item in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


para={"num":5,"struct":{"int":{"datarange":(0,10)},"float":{"datarange":(0,1000)},"str":{"datarange":string.ascii_letters,"len":10}}}

def main1():
    print(structDataSampling(**para))


if __name__ == '__main__':

    main1()
