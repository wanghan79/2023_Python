import random
import string

def structDataSampling(**kwargs):
    result = list()
    for item in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value["datarange"]) for _ in range(value["len"]))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result



if __name__ == "__main__":
    result1 = structDataSampling(num=5, struct={'one':{'datatype':'int',"datarange": (0,100)}, 'two': {'datatype': 'float', 'datarange': [1, 100]}})
    print(result1)
    print("\n******************************************************************************************")

    # num = 5, struct = {{'datatype': }}