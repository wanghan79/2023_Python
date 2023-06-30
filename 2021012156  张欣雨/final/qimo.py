import work1
import work2
import work3

def show():
    print(u"请输入数字0~3，其中0为退出，数字1~3分别为查看程序1~3")
    while True:
        try:
            x = int(input())
            if x == 0:
                break
            elif x == 1:
                work1.show()
            elif x == 2:
                work2.show()
            elif x == 3:
                work3.show()
            else:
                print(u'输入错误')

if __name__ == '__main__':
    show()
