import string
import random
def struct_data_sampling(num, struct):
    result = []
    for _ in range(num):
        item = []
        for key, value in struct.items():
            if key == int:
                item.append(random.randint(value['datarange'][0], value['datarange'][1]))
            elif key == float:
                item.append(random.uniform(value['datarange'][0], value['datarange'][1]))
            elif key == str:
                item.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            else:
                break
        result.append(item)
    return result

def show():
    print(struct_data_sampling(
        5, {
            int: {'datarange': (0,10)},
            str: {'datarange': string.ascii_letters.format("&*_"), 'len': 10},
            float: {'datarange': (0, 1.0)}
        }))