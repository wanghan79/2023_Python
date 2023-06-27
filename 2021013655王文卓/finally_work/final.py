import dataSampling
import decorator
import weather

def out():

    while(True):
        try:
            print(u"请输入数字1~3来选择查看作业1~3，输入数字0退出程序:")
            x = int(input())
            if x == 1:
                dataSampling.out()
            elif x == 2:
                decorator.out()
            elif x == 3:
                weather.out()
            elif x == 0:
                break
            else:
                print(u'数字的范围是1~3')
        except ValueError:
            print(u'请输入一个数字')


if __name__ == '__main__':
    out()