import work1
import work2
import work3

print("请输入“1”来运行第一次作业代码，输入“2”来运行第二次作业代码，输入“3”来运行第三次作业代码，输入“0”退出")
while (True):
    i = input()
    if i == '1':
        print("接下来是第一次作业运行结果")
        param = {
            "struct": ({"type": int,
                        "range": [0, 100]
                        },
                       {"type": float,
                        "range": [0, 100]
                        },
                       {"type": str,
                        "range": ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                        "len": 10
                        })
        }
        work1.dataSampling(**param)
    elif i == '2':
        print("接下来是第二次作业运行结果")
        params = {
            "struct": [{"type": int, "range": (0, 1000)}] * 6
        }
        calc_result = work2.sample_structured_data(**params, num=50)
        print("计算结果如下")
        print(calc_result)
    elif i == '3':
        print("接下来是第三次作业运行结果")
        for x in work3.WeatherIterable(["长春", "郑州", "成都", "广州"]):
            print(x)
    elif i == '0':
        print("程序就要退出咯~")
        break
    else:
        print("输入异常，请检查输入")
