import SJHhomework1
import SJHhomework2
import SJHhomework3

def show():
    print(u"请输入数字1~3来选择查看作业1~3，输入数字0退出程序")
    while True:
        try:
            x = int(input())
            if x == 1:
                SJHhomework1()
            elif x == 2:
                SJHhomework2()
            elif x == 3:
                SJHhomework3()
            elif x == 0:
                break
            else:
                print(u'数字的范围是1~3')
        except ValueError:
            print(u'请输入一个数字')


if __name__ == '__main__':
    show()