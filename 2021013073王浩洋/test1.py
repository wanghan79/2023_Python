import random
import string


def generate_random_data(**kwargs):
    result = []
    for _ in range(kwargs['num']):
        element = []
        for data_type, data_info in kwargs['data_structure'].items():
            if data_type == int:
                data_range = iter(data_info['range'])
                value = random.randint(next(data_range), next(data_range))
            elif data_type == float:
                data_range = iter(data_info['range'])
                value = random.uniform(next(data_range), next(data_range))
            elif data_type == str:
                value = ''.join(random.SystemRandom().choice(data_info['range']) for _ in range(data_info['length']))
            else:
                break
            element.append(value)
        result.append(element)
    return result


test_data = {
    'num': 3,
    'data_structure': {
        int: {'range': [1, 10]},
        float: {'range': [1.0, 10.0]},
        str: {'range': string.ascii_letters, 'length': 10}
    }
}

result = generate_random_data(**test_data)
print(result)
