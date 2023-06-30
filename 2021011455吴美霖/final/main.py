from homework1 import dataSampling
from homework2 import decorated
from homework3 import weather

if __name__ == "__main__":
    while(True):
        work_id = input("输入作业编号(输入1，2，3，输入exit退出)：")
        if work_id == 'exit':
            break
        elif work_id == "1":
            para = {
                "num": 10,
                "struct": (
                    {
                        'datatype': "int",
                        'datarange': [1, 100]
                    },
                    {
                        'datatype': "int",
                        'datarange': [100, 250]
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
            dataSampling.dataSimpling(para)
        elif work_id == "2":
            para = {
                "num": 10,
                "struct": (
                    {
                        'datatype': "int",
                        'datarange': [1, 100]
                    },
                    {
                        'datatype': "int",
                        'datarange': [100, 250]
                    },
                    {
                        'datatype': "int",
                        'datarange': [100, 250]
                    },
                    {
                        'datatype': "int",
                        'datarange': [100, 250]
                    },
                    {
                        'datatype': "int",
                        'datarange': [100, 250]
                    },
                    {
                        'datatype': "int",
                        'datarange': [100, 250]
                    }
                )
            }
            decorated.decorator(para)
        elif work_id == "3":
            weather.weather()
        else:
            print("输入错误，请重新输入")
        print()