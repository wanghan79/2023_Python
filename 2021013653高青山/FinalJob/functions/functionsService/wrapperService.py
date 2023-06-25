import sys
sys.path.append("./functions")
sys.path.append("../")
from wrapper import func

class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
def isError(number):
    if number <= 0:
        raise MyError("num 不能为负数")

def optionsec(choice = 0):
    try:
        print("请输入num，表示生成num维数据")
        num = int(input())
        isError(num)
        func(num)
    except (TypeError, ValueError) as res:
        print("异常的基本信息是：", res)
        print("请输入int型数据")
        print()
    except MyError as res:
        print("异常的基本信息是：", res)
        print()

