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


def calculate_statistics(*decargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            mean = 0
            total = 0
            for row in result:
                for element in row:
                    if isinstance(element, (int, float)):
                        total += element
                        mean += 1
            mean = total / mean
            if 'SUM' in decargs:
                print(f"The sum of the numbers is {total:.3f}")
            if 'AVG' in decargs:
                print(f"The mean of the numbers is {mean:.3f}")
            return result

        return wrapper

    return decorator


@calculate_statistics()
def generate_data_res1(**kwargs):
    return generate_data(**kwargs)


@calculate_statistics('SUM')
def generate_data_res2(**kwargs):
    return generate_data(**kwargs)


@calculate_statistics('AVG')
def generate_data_res3(**kwargs):
    return generate_data(**kwargs)


@calculate_statistics('SUM', 'AVG')
def generate_data_res4(**kwargs):
    return generate_data(**kwargs)


parameters = {
    "num": 3,
    "struct": {
        int: {"datarange": [1, 10]},
        float: {"datarange": [1.0, 10.0]},
        str: {"datarange": string.ascii_letters, "len": 10}
    }
}

print("Decorator with 0 arguments, no operations implemented:")
result1 = generate_data_res1(**parameters)
print(str(result1) + "\n")

print("Decorator with 1 argument, performing SUM operation:")
result2 = generate_data_res2(**parameters)
print(str(result2) + "\n")

print("Decorator with 1 argument, performing AVG operation:")
result3 = generate_data_res3(**parameters)
print(str(result3) + "\n")

print("Decorator with 2 arguments, performing both SUM and AVG operations:")
result4 = generate_data_res4(**parameters)
print(str(result4) + "\n")
