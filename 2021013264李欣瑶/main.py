from test1 import dataSimpling
from test2 import decorator
from test3 import weather



if __name__ == "__main__":
    while(True):
        test_id = input("输入作业编号(输入1，2，3，输入out退出)：")
        if test_id == 'out':
            break
        elif test_id == "1":
            para = {
                "num": 10,
                "struct": (
                    {
                        'datatype': "int",
                        'datarange': [1, 220]
                    },
                    {
                        'datatype': "int",
                        'datarange': [220, 300]
                    },
                    {
                        'datatype': "float",
                        'datarange': [1.0, 100.0]
                    },
                    {
                        'datatype': "str",
                        'datarange': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        'len': 8
                    }
                )
            }
            dataSimpling.dataSimpling(para)
        elif test_id == "2":
            para = {
                "num": 10,
                "struct": (
                    {
                        'datatype': "int",
                        'datarange': [1, 300]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 300]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 300]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 300]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 300]
                    },
                    {
                        'datatype': "int",
                        'datarange': [1, 300]
                    }
                )
            }
            decorator.decorator(para)
        elif test_id == "3":1
            weather.weather()
        else:
            print("错误，请重新输入")
        print()
