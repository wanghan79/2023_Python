from functions.functionsService.structDataSamplingService import optionfir
from functions.functionsService.wrapperService import optionsec
from functions.functionsService.weatherService import optionthr

def func():
    while(1):
        print("欢迎检查gqs的期末大作业")
        print("请选择想要运行的函数")
        print('输入1：执行第一次小作业')
        print('输入2：执行第二次小作业')
        print('输入3：执行第三次小作业')
        print('输入4：完成作业检查')
        num = int(input())
        if num == 1:
            print('执行第一次小作业')
            print("请选择执行的函数，dataSampling,structDataSamplingSimple,structDataSamplingComplicated")
            optionfir(input())
        elif num == 2:
            print('执行第二次小作业')
            optionsec()
        elif num == 3:
            print('执行第三次小作业')
            optionthr()
        elif num == 4:
            print("拜拜！！！")
            break
        else:
            print('没有该选项')
        continue
if __name__ == '__main__':
    func()