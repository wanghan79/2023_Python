import random
def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if isinstance(value, dict): 
            for k, v in value.items():
                if k == 'type' and v in ['int', 'float', 'str']:
                    dataType = v
                elif k == 'size':
                    size = v
                elif k == 'range':
                    dataRange = v
        else:
            raise ValueError(f"Invalid input: {key}={value}")

    if dataType == 'int':
        result = [random.randint(*dataRange) for _ in range(size)]
    elif dataType == 'float':
        result = [random.uniform(*dataRange) for _ in range(size)]
    elif dataType == 'str':
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = [random.choice(chars) for _ in range(size)]
    return result
def sum_avg_decorator(*args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)

            if 'SUM' in args and 'AVG' in args:
                return sum(data), sum(data) / len(data)
            elif 'SUM' in args:
                return sum(data)
            elif 'AVG' in args:
                return sum(data) / len(data)
            else:
                return data
        return wrapper
    return decorator
@sum_avg_decorator()
def generate_random_data_1(**kwargs):
    return dataSampling(**kwargs)

@sum_avg_decorator('SUM', 'AVG') 
def generate_random_data_2(**kwargs):
    return dataSampling(**kwargs)

@sum_avg_decorator('SUM') 
def generate_random_data_3(**kwargs):
    return dataSampling(**kwargs)

@sum_avg_decorator('AVG') 
def generate_random_data_4(**kwargs):
    return dataSampling(**kwargs)


