import Homework.FunctionHomework
import Homework.DecoratorHomework
import Homework.IteratorHomework


while True:
    # 菜单
    print("---------Python大作业运行示例---------",
          "            1: Function            ",
          "            2: Decorator           ",
          "            3: Iterator            ",
          sep="\n")
    # 输入作业编号
    job = int(input("选择作业序号："))
    # 判断
    if job == 1:
        s = {'dataType1': [int, {'datarange': (0, 100)}], 'dataType2': [float, {'datarange': (0, 100)}],
             'dataType3': [str, {'datarange': ('z', 'y', 'c'), 'len': 3}]}
        result = Homework.FunctionHomework.kwargsDataSapling(n=5, struct=s)
        print("测试样例：")
        print("n = 5, struct = ", s)
        print("输出结果：")
        print(result)
    elif job == 2:
        s = {'dataType1': [float, {'datarange': (0, 100)}], 'dataType2': [float, {'datarange': (0, 100)}],
             'dataType3': [float, {'datarange': (0, 100)}], 'dataType4': [float, {'datarange': (0, 100)}],
             'dataType5': [float, {'datarange': (0, 100)}], 'dataType6': [float, {'datarange': (0, 100)}]}
        result = Homework.DecoratorHomework.kwargsDataSapling(num=50, struct=s)
        print("测试样例：")
        print("num = 50, struct = ", s)
        print("输出结果：")
        print(result)
    elif job == 3:
        s = ["北京", "上海"]
        print("测试样例：")
        print("s = ", s)
        print("输出结果：")
        for x in Homework.IteratorHomework.WeatherIterable(s):
            print("----" * 9)
    else:
        print("输入错误！")
        continue
    print("--------------Welcome--------------")