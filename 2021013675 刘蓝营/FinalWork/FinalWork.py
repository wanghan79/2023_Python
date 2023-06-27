print("三次作业完整运行结果:")

import work1
import work2
import work3

print("输入“1”查看第一次作业，输入“2”查看第二次作业，输入“3”查看第三次作业，输入“0”结束")


while (True):
    i = input()
    if i == '1':
        work1.out_1()
    elif i == '2':
        work2.out_2()
    elif i == '3':
       work3.out_3()
    elif i == '0':
        break
    else:
        print("ERROR")