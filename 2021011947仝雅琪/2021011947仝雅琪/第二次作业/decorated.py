import random
import string

def my_decorator(*seq):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result1={}
            print(result)
            sum=0
            num=len(result)
            for i in result:
                sum+=i
            for index in seq:
                if index=="SUM":
                    result1['SUM'] = sum
                elif index=="AVG":
                    result1['AVG'] = sum / num
            return result1
        return inner_wrapper
    return wrapper

@my_decorator('SUM','AVG')
def dataSampling1(**kwargs):
    result = []
    num = kwargs.get('num')
    for i in range(num):
        for index in kwargs["struct"]:
            if index["type"] == int:
                it = iter(index["range"])
                tmp = random.randint(next(it),next(it))
                result.append(tmp)
            elif index["type"] == float:
                it = iter(index["range"])
                tmp = random.uniform(next(it),next(it))
                result.append(tmp)
            elif index["type"] == str:
                result.append(''.join(random.SystemRandom().choice(index["range"]) for _ in range(index["len"])))
    return result

if __name__ == '__main__':
    demo = {"num":3,"struct":({"type":int,"range":[0,100]},
                        {"type":float,"range":[0,100]})
            }
    print(dataSampling1(**demo))
