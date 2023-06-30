import random
def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if isinstance(value, dict):  # 处理字典类型的参数
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


