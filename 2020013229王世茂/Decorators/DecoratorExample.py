import logging


def foo():
    print("%s is running!" % foo.__name__)

'''
def bar(func):
    func()

bar(foo)


def addLogging(func):
    logging.warning("%s is running" % func.__name__)
    func()

addLogging(foo)
'''

def addLogging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()
    return wrapper

print(id(foo))
foo = addLogging(foo)
print(id(foo))
foo()

print()

# the first decorator in python
@addLogging
def foo():
    print("this is a decorated foo")

foo()

print()

# the decorator with parameters
def addLogging(decPara):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@addLogging("A Level")
def foo(name="mike"):
    print("the name in foo is %s" % name)

foo()
print()

@addLogging("A Level")
def doo(paraA, paraB, *args):
    print(paraA, paraB, *args)

foo('aaa')
print()
foo()
print()

doo('paraA', 'paraB', ('argsA', 'argsb'))
print()

# class decorator
class AddLogging:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        logging.warning("%s is running" % self.func.__name__)
        return self.func(*args, **kwargs)

@AddLogging
def foo():
    print("This is th foo function")

foo()

