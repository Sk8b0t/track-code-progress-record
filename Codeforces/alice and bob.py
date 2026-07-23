t=int(input())
for _ in range(t):
    l,r=0,0
    n,a=map(int,input().split())
    v=list(map(int,input().split()))
    for i in range(n):
        if a>v[i]:
            l+=1
    r=n-l
    if r>l:
        b=a+1
    else:
        b=a-1
    print(b)

