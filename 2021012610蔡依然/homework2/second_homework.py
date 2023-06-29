import random

data_struct = [
    {"data_type": int, "data_range": (1, 10)},
    {"data_type": int, "data_range": (1, 10)},
    {"data_type": float, "data_range": (1, 10)},
    {"data_type": float, "data_range": (1, 10)},
    {"data_type": int, "data_range": (1, 10)},
    {"data_type": str, "data_range": ['a', 'b', 'c', 'd', 'e', 'f', 'g'], "data_len": 10}
]

def random_data_summary(func):
    def wrapper(num, *args):
        random_data = func(num)
        operations = set(args)

        # 求和操作
        if 'SUM' in operations:
            total_sum = 0
            for element in random_data:
                for item in element:
                    if isinstance(item, (int, float)):
                        total_sum += item
            print(f"随机数据总和: {total_sum}")

        # 均值操作
        if 'AVG' in operations:
            total_sum = 0
            total_count = 0
            for element in random_data:
                for item in element:
                    if isinstance(item, (int, float)):
                        total_sum += item
                        total_count += 1
            if total_count > 0:
                avg = total_sum / total_count
                print(f"随机数据均值: {avg}")

        return random_data
    return wrapper

@random_data_summary
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


def print_random_data(num, *args):
    print(f"生成随机数为：")
    random_data = generate_random_data(num, *args)
    for element in random_data:
        print(element)
print("___________________________________________")
print("简易版")
print("默认生成50组6维的随机数")
operations = input("请输入操作，用空格分隔（可选：SUM、AVG、SUM AVG，或者不选）：").split()
print_random_data(50, *operations)
print("___________________________________________")
print("升级版")
print("自主选择数据结构和数量范围等")
import random

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

def random_data_summary(func):
    def wrapper(num, *args):
        random_data = func(num)
        operations = set(args)
        total_sum = 0
        total_count = 0

        for element in random_data:
            for item in element:
                if isinstance(item, (int, float)):
                    total_sum += item
                    total_count += 1
        if 'SUM' in operations:
            print(f"随机数据总和: {total_sum}")
        if 'AVG' in operations and total_count > 0:
            avg = total_sum / total_count
            print(f"随机数据均值: {avg}")
        return random_data
    return wrapper


@random_data_summary
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

def print_random_data(num, *args):
    print(f"生成随机数为：")
    random_data = generate_random_data(num, *args)
    for element in random_data:
        print(element)

add_data_structure()
num = int(input("请输入要生成的随机数据的数量："))
operations = input("请输入操作，用空格分隔（可选：SUM、AVG、SUM AVG，或者不选）：").split()
print_random_data(num, *operations)
print("___________________________________________")