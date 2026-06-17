''''
character count from string

s=input("enter your string : ")
d={}
for k in s:
    if k in d:
        d[k]=d[k]+1
    else:
        d[k]=1
for n in d:
    print(f"{n}={d[n]}")

''''''
list sorting
numbers=[19,2,1,23,8]
count
n=len(numbers)
for k in range(n-1):
    for v in range(n-k-1):
        if numbers[v]>numbers[v+1]:
            numbers[v],numbers[v+1]=numbers[v+1],numbers[v]
print(numbers)  
'''

count=int(input("how many numbers you wish to enter : "))
numbers=[]
for k in range(1, count+1):
    num=int(input(f"{k}.enter the number : "))
    numbers=numbers+[num]
n=len(numbers)
for k in range(n-1):
    for v in range(n-k-1):
        if numbers[v]>numbers[v+1]:
            numbers[v],numbers[v+1]=numbers[v+1],numbers[v]
print(numbers)             

