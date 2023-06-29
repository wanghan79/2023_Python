

import random
data_struct = [
    {"data_type": int, "data_range": (1, 10)},
    {"data_type": float, "data_range": (1, 10)},
    {"data_type": str, "data_range": ['a', 'b', 'c', 'd','e','f','g'], "data_len": 10}
]
def generate_random_data(num):
    result = []
    for _ in range(num):
        element = []
        for item in data_struct:
            data_type = item['data_type']
            data_range = item['data_range']

            if data_type is int:
                element.append(random.randint(*data_range))
            elif data_type is float:
                element.append(random.uniform(*data_range))
            elif data_type is str:
                element.append(''.join(random.choice(data_range) for _ in range(item['data_len'])))
        result.append(element)
    return result

def print_random_data(num):
    print(f"生成随机数为：")
    random_data = generate_random_data(num)
    for element in random_data:
        print(element)
print("___________________________________________")
print("简易版，数据结构固定")
num = int(input("请输入要生成的随机数据的数量："))
print_random_data(num)

print("___________________________________________")
import random
print("升级版，数据结构自主选择")
data_struct = []

def add_data_structure():
    print("请添加数据结构：")
    while True:
        data_type_str = input("请输入数据类型（int、float、str），或输入 q 退出：")
        if data_type_str == 'q':
            break

        data_type = None
        if data_type_str == 'int':
            data_type = int
        elif data_type_str == 'float':
            data_type = float
        elif data_type_str == 'str':
            data_type = str
        else:
            print("无效的数据类型，请重新输入！")
            continue

        if data_type is str:
            data_range_str = input("请输入数据范围（用逗号分隔，如 'a,b,c,d'）：")
            data_range = data_range_str.split(',')
        else:
            data_range_min = int(input("请输入数据范围的最小值："))
            data_range_max = int(input("请输入数据范围的最大值："))
            data_range = (data_range_min, data_range_max)

        data_struct.append({"data_type": data_type, "data_range": data_range})

def generate_random_data(num):
    result = []
    for _ in range(num):
        element = []
        for item in data_struct:
            data_type = item['data_type']
            data_range = item['data_range']

            if data_type is int:
                element.append(random.randint(*data_range))
            elif data_type is float:
                element.append(random.uniform(*data_range))
            elif data_type is str:
                element.append(''.join(random.choice(data_range) for _ in range(item.get('data_len', 1))))
        result.append(element)
    return result

def print_random_data(num):
    print(f"生成随机数为：")
    random_data = generate_random_data(num)
    for element in random_data:
        print(element)

add_data_structure()
num = int(input("请输入要生成的随机数据的数量："))
print_random_data(num)
print("___________________________________________")