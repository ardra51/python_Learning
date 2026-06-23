s=input("enter you string : ")
d={}

for k in s:
    if k in d:
        d[k]=d[k]+1
    else:
        d[k]=1

for n in d:
    print(f"{n} = {d[n]}")