from weather_dongzq import Weather_dongzq
from datasampling_dongzq import DataSampling_dongzq
from foo_dongzq import Sum_Avg_dongzq

def show():
    print(u"请输入数字x,y,z来选择查看作业1~3，输入字母e退出程序")
    while True:
        try:
            x = str(input())
            if x == 'x':
                DataSampling_dongzq.show()
            elif x == 'y':
                Sum_Avg_dongzq.show()
            elif x == 'z':
                Weather_dongzq.show()
            elif x == 'e':
                break
            else:
                print(u'字母的范围是x,y,z')
        except ValueError:
            print(u'请输入一个字母')


if __name__ == '__main__':
    show()