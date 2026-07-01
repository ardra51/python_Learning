'''
try:
    a,b=12,0
    print(a/b)
except:
    print("you cannot divide by zero")
print("program executed")

'''
'''
try:
    a,b=12
    print(a/b)
except ZeroDivisionError:
    print("you cannot divide by zero")
except TypeError:
    print("you can divide only by integer")
except NameError:
    print("provide values for a and b")
except Exception as e:
    print("error occured,e")

'''