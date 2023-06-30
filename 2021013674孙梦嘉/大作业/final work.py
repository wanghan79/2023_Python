print("全部展示：")

import work1
import work2
import work3

print("输入数字查看详细情况:")

def showending():
    while True:
        x = int(input())
        if x == 1:
            print("输出作业生成的随机数:")
            work1.showrandom()
        elif x == 2:
            print("输出作业计算生成的随机数和与平均值:")
            work2.showsumavg()
        elif x == 3:
            print("输出作业输出的天气:")
            work3.showweater()
        else:
            continue

showending()