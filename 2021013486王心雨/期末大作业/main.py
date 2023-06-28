"""
@Content: python大作业
            建立完整项目工程，将三次平时作业集成在一个工程中，实现控制台交互，提示用户输入要求展示的作业号（1、2或3），
            自动运行相应作业示例，并将结果输出到控制台。
"""
import hm1
import hm2
import hm3


print("\n" + "-" * 100)
print("\n")
print(" " * 40 + "欢迎！！！")
print(" " * 40 + "输入1：展示作业一")
print(" " * 40 + "输入2：展示作业二")
print(" " * 40 + "输入3：展示作业三")
print(" " * 40 + "输入0：退出")
print("\n")
print("-" * 100)

def solve():
    while(True):
        try:
            num = int(input("\n请输入:"))
            if num == 1:
                hm1.show()
            elif num == 2:
                hm2.show()
            elif num == 3:
                hm3.show()
            elif num == 0:
                print('さようなら！')
                break
            else:
                print("Invalid num!, Please confirm again and enter")
        except KeyboardInterrupt:
            pass


try:
    solve()
except Exception:
    pass


