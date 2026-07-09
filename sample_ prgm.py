'''
num=1
for k in range(1,6):
    for c in range(k):
        print(num,end=" ")
        num+=1
    print()
'''
'''
for k in range(1,6):
    for c in range(k,0,-1):
        print(c,end=" ")
        
    print()'''



 #for i in range(1,5):
 #  print(" *"*i)


'''for i in range(4,1,-1):
    print(" *" *i)'''

'''for r in range(1,6):
    for sp in range(5-r):
        print(" ",end="")
    print("*"*r)'''  

for r in range(1,6):
    print(" "*int(5-r),"*"*r)