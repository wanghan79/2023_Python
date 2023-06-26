from finalwork.utils.Math import average, sum


def aop(func):
    def decorator(function):
        def wrapper(*args, **kwargs):  # 实际做事的部分，集成了修饰功能和老函数的功能
            # 修饰的内容
            temp = function(*args, **kwargs)
            print(type(temp))
            if func == 1:
                sum(temp)
            elif func == 2:
                average(temp)
            elif func == 3:
                sum(temp)
                print("------------------------")
                average(temp)
            else:
                print("修饰器未工作")
            return temp

        return wrapper  # 返回整体的wrapper，

    return decorator


def aop2():
    def decorator(function):
        def wrapper(*args, **kwargs):  # 实际做事的部分，集成了修饰功能和老函数的功能
            choose = args[0]
            # 修饰的内容
            temp = function(*args, **kwargs)
            if choose == 1:
                sum(temp)
            elif choose == 2:
                average(temp)
            elif choose == 3:
                sum(temp)
                print("------------------------")
                average(temp)
            else:
                print("修饰器未工作")
            return temp

        return wrapper  # 返回整体的wrapper，

    return decorator
