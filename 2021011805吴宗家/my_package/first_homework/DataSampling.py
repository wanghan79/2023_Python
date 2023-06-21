import random
import ast

def DataSampling(**kwargs):
    result = []
    for index in range(kwargs['num']):
        element = []
        for key, value in kwargs.items():
            if key == 'num':
                continue
            elif value.get('type') == 'int':
                datarange = value['datarange']
                element.append(random.randint(datarange[0], datarange[1]))
            elif value.get('type') == 'float':
                datarange = value['datarange']
                element.append(random.uniform(datarange[0], datarange[1]))
            elif value.get('type') == 'str':
                datarange = value.get('datarange', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
                n = value.get('len', 8)
                element.append(''.join(random.choice(datarange) for _ in range(n)))
        result.append(element)
    return result

if __name__ == "__main__":
    # 输入示例: {"int1": {"type": "float", "datarange": (44, 77)}, "int2": {"type": "int", "datarange": (3, 6)}, "int3": {"type": "int", "datarange": (7, 100)}, "num": 5}
    input_string = input("请输入参数(例如: {\"int1\": {\"type\": \"float\", \"datarange\": (44, 77)}, \"int2\": {\"type\": \"int\", \"datarange\": (3, 6)}, \"int3\": {\"type\": \"int\", \"datarange\": (7, 100)}, \"num\": 5}):\n")
    s = DataSampling(**ast.literal_eval(input_string))
    print(s)
