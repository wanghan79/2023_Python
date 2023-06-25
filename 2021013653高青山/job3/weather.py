from collections.abc import Iterator, Iterable
import requests as r
import json
with open("../FinalJob/input/城市编码表.json", 'r', encoding='UTF-8') as f:
    data = json.loads(f.read())
    data = data.get('城市代码')

# 找到城市对应的编码
def getcode(city):
    for x in data:
        for y in x.get('市'):
            if y.get('市名') == city:
                return y.get('编码')
    print("输入城市名有误，默认返回北京天气")
    return "101010100"



class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0
    def getWeather(selfs,city):
        url = ''
        req = ''
        code = getcode(city)
        if code == '101010100':
            city = '北京'
        try:
            url = r'http://t.weather.sojson.com/api/weather/city/'+code
        except (TypeError) as res:
            print("异常的基本信息是："+res)
        try:
            req = r.get(url)
        except ConnectionError as result:
            print('异常的基本信息是：'+result)
            print('短时间访问链接过于频繁，远程主机强迫关闭了连接')
        data = req.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city,data['low'],data['high'])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)

struct = list()
def option():
    print('请依次输入所有想要查询的城市，再次输入回车确认输入完成')
    while(1):
        str = input()
        if str == '':
            break
        else:
            struct.append(str)
    print('您输入的信息是：')
    print(struct)
    func(struct)

def func(struct):
    for x in WeatherIterable(struct):
        print(x)
    print('******************************************************************************************************************')

option()