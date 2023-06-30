import random

def sum_result(x):
    result = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            result += x[i][j]
    return result

def avg_result(x):
    total = 0
    count = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            total += x[i][j]
            count += 1
    return total / count if count > 0 else 0

def add_logging(*order):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("生成的随机数如下：", result)
            data = {}
            for item in order:
                if item == "sum":
                    data['sum'] = sum_result(result)
                elif item == "avg":
                    data['avg'] = avg_result(result)
            return data
        return wrapper
    return decorator

def dataSampling(**kwargs):
    result_set = list()
    for _ in range(kwargs.get("num", 1)):
        single_struct_result = list()
        for idxNum in kwargs.get("struct", []):
            if idxNum["type"] is int:
                it = iter(idxNum["range"])
                tmp = random.randint(next(it), next(it))
                single_struct_result.append(tmp)
            elif idxNum["type"] is float:
                it = iter(idxNum["range"])
                tmp = random.uniform(next(it), next(it))
                single_struct_result.append(tmp)
            else:
                break
        result_set.append(single_struct_result)
    return result_set

def run_operation(order):
    structure = {"struct": [{"type": int, "range": [0, 100]}, {"type": float, "range": [0, 100]}], "num": 10}
    @add_logging(*order)
    def operation():
        return dataSampling(**structure)
    results = operation()
    print("结果如下：", results)

def main():
    print("请输入一个操作码，1代表求和，2代表求平均数，3代表两者都求, 0退出该程序")
    while True:
        x = input()
        if x == '1':
            run_operation(["sum"])
        elif x == '2':
            run_operation(["avg"])
        elif x == '3':
            run_operation(["sum", "avg"])
        elif x == '0':
            break
        else:
            print("操作码无效，请重新输入!")

if __name__ == '__main__':
    main()
