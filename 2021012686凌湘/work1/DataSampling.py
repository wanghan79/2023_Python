import random
import string
def structDataSampling(num, struct):
    result = list()
    for _ in range(num):
        element = list()
        for key, value in struct.items():
            for item in value['datarange']:
                if key is int:
                    it = iter(item)
                    tmp = random.randint(next(it), next(it))
                elif key is float:
                    it = iter(item)
                    tmp = random.uniform(next(it), next(it))
                elif key is str:
                    tmp = ''.join(random.SystemRandom().choice(
                        item[0]) for _ in range(item[1]))
                else:
                    raise TypeError("文本错误！！！")
                element.append(tmp)
        result.append(element)
    return result
def run():
    struct = {
        int: {'datarange': ([1, 100], [1, 100])},
        float: {'datarange': ((0.0, 10.0),)},
        str: {'datarange': ((string.ascii_letters, 3), ("sdsdhfjl", 5))}
    }
    data = structDataSampling(3, struct)
    print("产生的结果为：\n", data)
if __name__ == '__main__':
    run()


