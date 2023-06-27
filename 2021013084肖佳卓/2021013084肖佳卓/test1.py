import random
import string


def generate_data(**kwargs):
    result = []
    for index in range(kwargs['num']):
        element = []
        for key, value in kwargs['struct'].items():
            if key == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


test_dict = {
    "num": 3,
    "struct": {
        int: {"datarange": [1, 10]},
        float: {"datarange": [1.0, 10.0]},
        str: {"datarange": string.ascii_letters, "len": 10}
    }
}

result = generate_data(**test_dict)
print(result)
