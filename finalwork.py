import string

from dataSampling import dataSampling
from weather import show
from wrapper import structDataSampling

while True:
    print('Please enter a number,1 is dataSampling,2 is wrapper,3 is weather and other numbers is exit：')
    x=input()
    if x == '1':
        print("DataSampling:")
        hw1={"num":5,
            "struct":{
            "data1":
                {"datatype":'int',
                "datarange":{0,100}},
            "data2":
                {"datatype":'int',
                 "datarange":{0,100}},
            "data3":
                {"datatype":'str',
                 "datarange":string.ascii_uppercase,
                 "len":50}}
      }
        print(dataSampling(**hw1))
    elif x == '2':
        print("Wrapper:")
        hw2={
            "num": 50,
            "struct": (
                {
                    'datatype': "float",
                    'datarange': [1, 100]
                },
                {
                    'datatype': "float",
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
                    'datatype': "float",
                    'datarange': [100, 250]
                }
            )
        }
        print(structDataSampling(**hw2))
    elif x == '3':
        print("Weather:")
        hw3= show()
        cities = ['北京','长春','长沙','上海']
        hw3.show(cities)
    else:
        break


