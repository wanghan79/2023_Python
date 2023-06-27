
import test1
import test2
import test3

def main():
    print(u"请输入数字1~3来选择查看作业1~3，输入数字0退出程序")
    while True:
        try:
            x = int(input())
            if x == 1:
                test1.main()
            elif x == 2:
                test2.show()
            elif x == 3:
                test3.main()
            elif x == 0:
                break
            else:
                print(u'input error')
        except ValueError:
            print(u'retype please')


if __name__ == '__main__':
    main()