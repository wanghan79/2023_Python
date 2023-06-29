
print("全部展示：")

import yrandom
import yandomsumavg
import weather

print("输入数字查看详细情况:")

def showending():
    while True:
        x = int(input())
        if x == 1:
            print("输出作业生成随机数的展示:")
            yrandom.showrandom()
        elif x == 2:
            print("输出作业计算生成随机数和与平均值的展示:")
            yandomsumavg.showsumavg()
        elif x == 3:
            print("输出作业输出天气的展示:")
            weather.showeater()
        else:
            continue

showending()