t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    newa=[]
    while(len(newa)!=n):
        ind=a.index(max(a))
        a[ind]-=k
        if a[ind]<=0:
            newa.append(ind+1)
    print(*newa)



    t-=1