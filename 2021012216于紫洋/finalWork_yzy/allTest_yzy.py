import structDataSampling
import weather
import wrapper
class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def OverError():
    raise MyException("操作码无效")


def run():
    while True:
        print("请按需求输入下面数字：（不要输入多余回车）")
        print('输入1：执行平时作业1：实现随机数据结构生成封装函数dataSampling(**kwargs)')
        print(
            '输入2：执行平时作业2：采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的求和（SUM），求均值（AVG）操作，以及相应的调用示例')
        print('输入3：执行平时作业3：执行使用迭代器实现城市天气数据的自动获取，以及相应的调用示例')
        print('输入0：退出程序')
        try:
            x = int(input())
            if x == 1:
                structDataSampling.run()
            elif x == 2:
                wrapper.run()
            elif x == 3:
                weather.run()
            elif x == 0:
                print("bye~")
                break
            else:
                print('数字的范围是0~3')
                OverError()
        except  OverError:
            print('请输入一个数字')

run()
