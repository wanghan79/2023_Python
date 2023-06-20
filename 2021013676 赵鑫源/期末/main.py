from DataSampling import structDataSampling3
from 天气 import WeatherIterable
from 装饰器 import structDataSampling2

print('请输入，0为退出，1，2，3分别为第1，2.3次作业')
while True:
    i = input()
    if i == '0':
        break
    elif i == '1':
        print(structDataSampling3(num=10, struct=(
            {
                'dataType': 'int',
                'dataRange': (0, 5),
                'num': 2
            },
            {
                'dataType': 'int',
                'dataRange': (10, 15),
                'num': 3
            },
            {
                'dataType': 'int',
                'dataRange': (100, 150),
                'num': 4
            },
            {
                'dataType': 'float',
                'dataRange': (1.3, 4.9),
                'num': 5
            },
            {
                'dataType': 'float',
                'dataRange': (2.6, 7.8),
                'num': 1
            },
            {
                'dataType': 'str',
                'dataRange': ('w', 'm', 's', 'f', 'a'),
                'len': 6,
                'num': 1
            },
            {
                'dataType': 'str',
                'dataRange': ('hello', 'world', 'you', 'me', 'hi', ' '),
                'len': 3,
                'num': 1
            }
        )))
    elif i == '2':
        # 共60行，每行5个元素，2个int，3个float
        result = structDataSampling2(num=60, struct=(
            {
                'dataType': 'int',
                'dataRange': (1, 50),
                'num': 1
            },
            {
                'dataType': 'int',
                'dataRange': (500, 700),
                'num': 1
            },
            {
                'dataType': 'float',
                'dataRange': (3.6, 7.8),
                'num': 3
            }
        ))
        print(result)
    elif i == '3':
        for x in WeatherIterable([u'北京', u'上海', u'广州', u'长春', u'漯河', u'郑州']):
            print(x)
    else:
        print("输入的数字不对")