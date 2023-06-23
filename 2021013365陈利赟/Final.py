"""
结课作业要求：
建立完整项目工程，将三次平时作业集成在一个工程中，实现控制台交互，提示用户输入要求展示的作业号（1、2或3），自动运行相应作业示例，并将结果输出到控制台。
"""

import homework1
import homework2
import homework3

def showFinal():
    print("请输入数字1,2,3来选择查看作业1,2,3，输入数字0退出程序")
    while True:
        x = int(input())
        if x == 1:
            homework1.show1()
        elif x == 2:
            homework2.show2()
        elif x == 3:
            homework3.show3()
        elif x == 0:
            print('谢谢使用，生活愉快')
            break
        else:
            print('输入数字为1,2,3,请检查输入！')

if __name__ == '__main__':
    showFinal()
