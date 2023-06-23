
def foo():
    print("foo")

def bar(func):
    print("1")
    func()

# traditional use
def logging(func):
    def wrapper():
        print('hh')
        return func()
    return wrapper

foo = logging(foo)
foo()

# normal use
@logging
def foo():
    print('foov1')

foo()

def logging(func):
    def wrapper(*args, **kwargs):
        print('update')
        return func(*args, **kwargs)
    return wrapper

@logging
def foo(name = 'wsm'):
    print(name)

foo()
