#Feng shiyu
import random
def dataprocess(*addAction):
    def decorater(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            sum = 0.0
            actionContainer = addAction
            for listt in data:
                for index in listt:
                    sum += index
                listLength = len(listt)
            num = listLength*len(data)
            if actionContainer == ():
                print("You didn't input 'sum' or 'average' ! ")
                print("所以原数据结构为:")
                print(data)
            for action in actionContainer:
                if action == 'average':
                    ave = sum/num
                    print(f"平均数average为: {ave}")
                elif action == 'sum':
                    print(f"数的和sum为: {sum}")
        return wrapper
    return decorater


@dataprocess('sum', 'average')   # 'sum','average',可以都有，也可以有其一，或为空
def structDataSampling(**kwargs):
    result = list()
    for index in range(kwargs['num']):
        element = list()
        for key, value in  kwargs.items():
            if key == 'num':
                continue
            for key, value in value.items():
                if key == 'int':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == 'float':
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == 'str':
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                element.append(tmp)
        result.append(element)
    return result


if __name__ == '__main__':
    structDataSampling(int1={'int': {'datarange': (1, 100)}}, int2={'int': {'datarange': (22, 66)}},float1={'float': {'datarange': (1.167, 6.24)}}, num=5)


