from work1 import dataSampling
from work2 import decorator
from work3 import run

if __name__ == "__main__":
    while(True):
        id = input("输入作业编号：")
        if id == 'exit':
            break
        elif id == "1":
            para = {
                "num": 5,
                "struct": (
                    {
                        'datatype': "int",
                        'datarange': [1, 10]
                    },
                    {
                        'datatype': "float",
                        'datarange': [1.0, 10.0]
                    },
                    {
                        'datatype': "str",
                        'datarange': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        'len': 5
                    }
                )
            }
            dataSampling.dataSampling(para)
        elif id == "2":
            para = {
                "num": 5,
                "struct": (
                    {
                        'datatype': "int",
                        'datarange': [1, 10]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 10]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 10]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 10]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 10]
                    }
                )
            }
            decorator.decorator(para)
        elif id == "3":
            run.weather()
        else:
            print("输入错误，请重新输入")
        print()