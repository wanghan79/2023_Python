import random


def structDataSampling(**kwargs):
    """
     :param kwargs:
    :return: 
    """
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

def dataSimpling(para):
    print("随机数生成：")
    print(structDataSampling(**para))

if __name__=='__main__':
       para = {
          "num": 10,
          "struct": (
          {
            'datatype':"int",
            'datarange' : [1,220]
          },
          {
              'datatype': "int",
              'datarange': [220, 300]
          },
          {
             'datatype':"float",
            'datarange': [1.0, 100.0]
          },
          {
           'datatype':"str",
            'datarange': "ABCDEFGHIJKLM",
            'len': 10
          }

          )
       }
       dataSimpling(para)
