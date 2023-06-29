import homework1
import homework2
import homework3

print("请输入'1'或'2'或'3'来展示三次作业，输入'q'退出")
while (1):
    m = input()
    if m == '1':
        structDataSampling = {
            "struct": ({"datatype": int,
                        "datarange": [0, 100]
                        },
                       {"datatype": float,
                        "datarange": [0.0, 100.0]
                        },
                       {"datatype": str,
                        "datarange": ['0', '1', '2', '3', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                        "len": 10
                        })
        }
        homework1.dataSampling(**structDataSampling)
    elif m == '2':
        param = {
            "struct": [{"type": int, "range": (0, 100)}] * 10
        }
        result = homework2.data(**param, num=50)
        print(result)
    elif m == '3':
        for x in homework3.WeatherIterable([u'北京', u'长春', u'广州', '天津']):
            print(x)
    elif m == 'q':
        break
    else:
        print("输入异常，请重新输入。")