"""
    Author:Haizhu.Wu
    Title:Assignment
"""
from assignment1 import randomgenerate
from assignment2 import randomdecorator
from assignment3 import iter
import json
with open("城市编码表.json", 'r', encoding='UTF-8') as file:
    data = json.loads(file.read())
    data = data.get('城市代码')

def main():
    while True:
        print('请选择要运行的作业：')
        print('1.Assignment1 ')
        print('2.Assignment2')
        print('3.Assignment3')
        print('0. exit')
        choice = input('请输入作业号：')

        if choice == '1':
            randomgenerate.show()

        elif choice == '2':
            randomdecorator.show()

        elif choice == '3':
            iter.show()

        elif choice == '0':
            break

        else:
            print('无效的作业号，请重新输入')


if __name__ == '__main__':
    main()