import sys
sys.path.append("../../functions")
import structDataSampling

def option(choice):
    # print("请选择执行的函数，dataSampling,structDataSamplingSimple,structDataSamplingComplicated")
    try:
        if choice == 'dataSampling':
            print("执行：print(dataSampling(int, [1, 9], 4, 2))")
            print(dataSampling(int, [1, 9], 4, 2))
            print("执行：print(dataSampling(float, [1, 10], 4, 2))")
            print(dataSampling(float, [1, 10], 4, 2))
            print("执行：print(dataSampling(str, ['a','b'], 10, 2))")
            print(dataSampling(str, ['a','b'], 10, 2))
            print("执行：print(dataSampling(str, ['a','b','c','d'], 10))")
            print(dataSampling(str, ['a', 'b', 'c', 'd'], 10))
            print('******************************************************************************************************************')
        elif choice == 'structDataSamplingSimple':
            # 正常数据
            struct1 = {int: {'datarange': [1, 9], 'len': 10}}
            # 异常数据
            struct2 = {int: {'datarange': [1.3, 9], 'len': 10}}
            print("执行：print(structDataSamplingSimple(4, struct1))")
            print(structDataSamplingSimple(4, struct1))
            print('******************************************************************************************************************')
        elif choice == 'structDataSamplingComplicated':
            # 这个函数的参数我放在input目录下的structDataSamplingComplicated.json文件里面了
            # func()函数返回的是structDataSamplingComplicated.json文件里面的数据
            print("执行：print(structDataSamplingComplicated(**func()))")
            print(structDataSamplingComplicated(**func()))
            print('******************************************************************************************************************')
        else:
            print("请输入正确的函数名")
            print('******************************************************************************************************************')
    except (TypeError, ValueError) as res:
        print("异常的基本信息是：", res)
        print("random.*参数不匹配，请检查输入的类型与数据是否一致")
        print()