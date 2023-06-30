import random
import string


def structDataSampling(**kwargs):
    results = list()
    for item in range(0, kwargs['num']):
        result = list()
        for key, value in kwargs['struct'].items():
            if key is int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key is float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key is str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            result.append(tmp)
        results.append(result)
    return results


def run():
    print("随机生成结构体")
    print(structDataSampling(num=5, struct={int: {'datarange': (0, 10)},
                                            str: {'datarange': string.ascii_letters.format("&*_"), 'len': 10},
                                            float: {'datarange': (0, 1.0)}}))
    print("job1_yzy ^_^")


if __name__ == '__main__':
    run()
