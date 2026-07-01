''''def my_dec(fun):
    def wrapper():
        print("hello from my dec")
        fun()
    return wrapper

def greet():
    print("hello from greet")

f=my_dec(greet)
f()
------------------

def my_dec(fun):
    def wrapper():
        print("hello from my dec")
        fun()
    return wrapper
@my_dec
def greet():
    print("hello from greet")

greet()'''

def my_dec(fun):
    def wrapper(a,b):
        if a>b:
            fun(a,b)
        else:
            print("a must be greater than be b")
    return wrapper

@my_dec
def divide(a,b):
    print(a/b)

divide(4,7)
        