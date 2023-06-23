from gqsJob.functions.wrapper import func


def option(choice = 0):
    try:
        print("请输入num，表示生成num维数据")
        num = int(input())
        func(num)
    except (TypeError, ValueError) as res:
        print("异常的基本信息是：", res)
        print("请输入int型数据")
        print()