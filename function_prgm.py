'''
def add(*args):
    total=0
    for i in args:
        total+=1
    print(total)

add(34,12)
add(9,12,46)

'''  
'''
def greet(**kwargs):
    print(f"hello {kwargs["name"]} you are {kwargs["age"]} years old")

greet(name="aswin", age=24,place="kottayam")    

'''
'''
def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
    
print("factorial of 5 is : ",fact(5))    
    
'''
'''
def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
print("factiorial of 4 is : ",fact(4))    

'''

add=lambda a,b:a+b
print(add(31,12))

is_even=lambda num: num%2==0
print(is_even(4))
