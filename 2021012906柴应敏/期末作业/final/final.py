import string

from Random import DataSampling
from weather import weather_test1
from decorate import structDataSampling

while True:
    print('Please enter a number,1 is Random,2 is decorate,3 is weather and other numbers is exit：')
    x=input()
    if x == '1':
        print("Random:")
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
        print(DataSampling(**hw1))
    elif x == '2':
        print("decorate:")
        hw2={
            "num": 5,
            "struct": (
                {'datatype': "float", 'datarange': [1, 100]},
                {'datatype': "float", 'datarange': [100, 250]},
                {'datatype': "int", 'datarange': [100, 250]},
                {'datatype': "int", 'datarange': [100, 250]},
                {'datatype': "int", 'datarange': [100, 250]},
                {'datatype': "float", 'datarange': [100, 250]}
            )
        }
        print(structDataSampling(**hw2))
    elif x == '3':
        weather_test1()
    else:
        break
