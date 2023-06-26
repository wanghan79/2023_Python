import random
example = {
    "num":2,
     "struct":{
         "a":{
             "datatype": "int",
             "datarange": (0, 100)
         },
         "b":{
                "datatype": "float",
                "datarange":(-199,200)
         },
         "d":{
                "datatype":"str",
                 "datarange" : "qjjdiehaincbcuieudhdh",
                "strlen": 8
         }
     }
}


def addLogging(*args):
    def decorator(func):
        param = args
        # print(param)
        def wrapper(*args,**kwargs):
            randomNumber = func(*args, **kwargs)
            print("产生的随机数是：")
            print(randomNumber)
            if len(param) == 0:
                    print("未给任何参数，直接返回随机数")
                    return randomNumber
            for x in param:
                if x == "SUM":
                    print("下面开始计算SUM·······")
                    a = 0
                    for x in randomNumber:
                        sum = x[0]+x[1]
                        a+=sum
                    print("sum 的值是：")
                    print(a)
                elif x == "AVG":
                    print("下面开始计算AUG·····")
                    a = 0
                    for x in randomNumber:
                        sum = x[0] + x[1]
                        a = a + sum
                    # print(a)
                    b = kwargs['num']
                    avg = 0.0
                    avg = a/b
                    print("avg的值是:")
                    print(avg)

                else:
                    raise ValueError("给出的参数错误")
            return "计算结束"
        return wrapper
    return decorator




@addLogging('SUM')
def structDatasampling(**kwargs):
    result = list()
    for index in range(0,kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                temp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                temp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
               continue
            else:
                break
            element.append(temp)
        result.append(element)
    return result


print(structDatasampling(**example))




