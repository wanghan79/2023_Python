import work_1, work_2, work_3

while(True):
    number = input("请输入需展示的作业号(1,2或3): ")
    if number == '1':
        s = work_1.structDataSampling(int1={'int':{'datarange': (44,77)}}, float1={'float':{'datarange': (3.14,5.15)}}, float2={'float':{'datarange': (6.17,10.0)}}, str = {'str': {'datarange': 'adbcdefghijklmnopq', 'len':8}},  num = 5)
        print(s)
    elif number == '2':
        work_2.structDataSampling(int1={'int': {'datarange': (1, 100)}}, int2={'int': {'datarange': (22, 66)}},float1={'float': {'datarange': (1.167, 6.24)}}, num=5)
    elif number == '3':
        for x in work_3.WeatherIterable(['北京', '长春', '广州', '上海']):
            print(x)