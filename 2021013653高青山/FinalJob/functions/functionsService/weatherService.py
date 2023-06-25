import sys
sys.path.append("./functions")
sys.path.append("../")
from weather import WeatherIterable

struct = list()
def optionthr(choice = 0):
    print('请依次输入所有想要查询的城市，再次输入回车确认输入完成')
    while(1):
        str = input()
        if str == '':
            break
        else:
            struct.append(str)
    print('您输入的信息是：')
    print(struct)
    func(struct)

def func(struct):
    for x in WeatherIterable(struct):
        print(x)
    print('******************************************************************************************************************')