import sytest1
import sytest2
import sytest3

def show():
    print(u"请输入数字1~3来选择查看作业1~3，输入数字0退出程序")
    while True:
        try:
            x = int(input())
            if x == 1:
                demo = sytest1.structDataSampling(num=3, struct={
                    'data1': {'datatype': 'int', 'datarange': [0, 100]},
                    'data2': {'datatype': 'int', 'datarange': [0, 100]},
                    'data3': {'datatype': 'str', 'datarange': ['a', 'b', 'c'], 'len': 5}
                })
                sytest1.show(demo)
            elif x == 2:
                sytest2.show()
            elif x == 3:
               sytest3.show()
            elif x == 0:
                break
            else:
                print(u'数字的范围是1~3')
        except ValueError:
            print(u'请输入一个数字')


if __name__ == '__main__':
    show()