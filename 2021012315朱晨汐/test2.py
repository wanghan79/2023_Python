import random
import string


def struct_data_sampling(**kwargs):
    result = list()
    for index in range(kwargs['num']):
        element = list()
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


def calculation(*dec_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            mean = 0
            total = 0
            for r in result:
                for e in r:
                    if isinstance(e, (int, float)):
                        total += e
                        mean += 1
            mean = total / mean
            if 'SUM' in dec_args:
                print(f'The sum of the numbers is {total:.3f}')
            if 'AVG' in dec_args:
                print(f'The mean of the numbers is {mean:.3f}')
            return result
        return wrapper
    return decorator


@calculation()
def res1(**kwargs):
    return struct_data_sampling(**kwargs)


@calculation('SUM')
def res2(**kwargs):
    return struct_data_sampling(**kwargs)


@calculation('AVG')
def res3(**kwargs):
    return struct_data_sampling(**kwargs)


@calculation('SUM', 'AVG')
def res4(**kwargs):
    return struct_data_sampling(**kwargs)


parameters = {'num': 5,
              'struct': {int: {'datarange': [1, 10]},
                         float: {'datarange': [1.0, 10.0]},
                         str: {'datarange': string.ascii_letters, 'len': 20}
                         }}

print('Decorator with 0 arguments, no operations implemented:')
print(str(res1(**parameters)) + '\n')

print('Decorator with 1 argument (SUM operation):')
print(str(res2(**parameters)) + '\n')

print('Decorator with 1 argument (AVG operation):')
print(str(res3(**parameters)) + '\n')

print('Decorator with 2 arguments (SUM and AVG operations):')
print(str(res4(**parameters)) + '\n')
