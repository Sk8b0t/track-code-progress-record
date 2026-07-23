t=int(input())
while t:
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]<=q:
            a[i]=1
        else:
            a[i]=0
    
    ways=cnt=0
    a.append(0)
    for i in range(len(a)):
        if a[i]==1:
            cnt+=1
        else:
            if cnt>=k:
                N=cnt-k+1
                ways+=(N*(N+1))//2
            cnt=0
    print(ways)
        
    t-=1