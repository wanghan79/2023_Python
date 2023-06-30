import random
import string

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

def run1():

    try:
        result = (struct_data_sampling
                (4,{
                    #int：
                    int: {'datarange': (0,10)},
                    #str：
                    str: {'datarange': string.ascii_letters.format("&*_"), 'len': 10},
                    #float：
                    float: {'datarange': (0, 1.0)}
                })
            )
        print(result)
    except(TypeError,KeyError):
        print("参数格式错误")
    else:
        print('程序执行成功')

if __name__ == "__main__":
    run1()