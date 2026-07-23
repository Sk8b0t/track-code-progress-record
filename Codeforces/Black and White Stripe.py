t=int(input())
while t:
    n,k=map(int,input().split())
    s=input()
    pre=[0]*(n+1)
    cnt=0
    for i in range(n):
        if s[i]=="W":
            cnt+=1
        pre[i+1]=cnt
    m=n
    for i in range(n-k+1):
        m=min(m,pre[i+k]-pre[i])
    print(m)

    t-=1