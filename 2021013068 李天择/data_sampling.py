import random

def dataSampling(**kwargs):
    result = []
    for data_type, data_size in kwargs.items():
        if data_type == 'int':
            result.append([random.randint(0, 100) for _ in range(data_size)])
        elif data_type == 'float':
            result.append([random.uniform(0, 100) for _ in range(data_size)])
        elif data_type == 'str':
            result.append([''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)) for _ in range(data_size)])
    return result

# # 调用示例
# random_data = dataSampling(int=5, float=3, str=4)
# print(random_data)
