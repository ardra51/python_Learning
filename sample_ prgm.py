'''
num=1
for k in range(1,6):
    for c in range(k):
        print(num,end=" ")
        num+=1
    print()
'''

for k in range(1,6):
    for c in range(k,0,-1):
        print(c,end=" ")
        
    print()