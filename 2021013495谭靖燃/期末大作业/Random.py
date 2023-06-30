import  random
def structData(**kwargs):
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                tmp = random.randint(next(it),next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                tmp = random.uniform(next(it),next(it))
            elif e['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(e['datarange'])for _ in range(e['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

para = {
    "num" :10,
    "struct":(
        {"datatype":"int",'datarange':(1,100)},
        {"datatype": "int", 'datarange': (100, 190)},
       {"datatype":"float",'datarange' : (1.0,100.0)},
        {"datatype":"str",'datarange':"ASDFTVTRRTTTH", 'len':8 }
    )
}
def work1():
    print(structData(**para))
if __name__ == '__main__':
    work1()