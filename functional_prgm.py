'''
numbers=[65,40,32,4,6]

n=list(map(lambda num:num%2==0,numbers))
print(n)

'''
'''
numbers=[65,40,32,4,6]

n=list(filter(lambda num:num%2==0,numbers))
print(n)

'''
numbers=[65,40,32,4,6]

n=list(filter(lambda num:num%2==0,numbers))
print(n)

from functools import reduce

total=reduce(lambda a,b:a*b,range(1,6))
print(total)