t=int(input())
while t:
    x=[]
    n=int(input())
    for k in range(1,19):
        if n%((10**k)+1)==0:
            x.append(n//((10**k)+1))
    x.sort()
    print(len(x))
    if len(x)!=0:
        print(*x)
    t-=1
