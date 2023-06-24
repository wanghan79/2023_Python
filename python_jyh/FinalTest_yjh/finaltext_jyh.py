import text1_jyh
import text2_jyh
import text3_jyh

def show():
    print(u"请输入数字1~3来选择查看作业1~3，输入数字0退出程序")
    while True:
        try:
            x = int(input())
            if x == 1:
                text1_jyh.show()
            elif x == 2:
                text2_jyh.show()
            elif x == 3:
               text3_jyh.show()
            elif x == 0:
                break
            else:
                print(u'数字的范围是1~3')
        except ValueError:
            print(u'请输入一个数字')


if __name__ == '__main__':
    show()