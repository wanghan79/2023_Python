import SJwork1
import SJwork2
import SJwork3

print ("功能以及其编号： ")
print ("1.生成随机数")
print ("2.通过修饰器生成随机数，并求其和以及平均数")
print ("3.天气预报")
print ("4.结束进程")
while(True):
    a = input("输入所需功能编码: ")
    a = int(a)
    if a == 1:
        SJwork1.SJwork_1()
    if a == 2:
        SJwork2.SJwork_2()
    if a == 3:
        SJwork3.SJwork_3()
    if a == 4:
        print("感谢使用")
        break
