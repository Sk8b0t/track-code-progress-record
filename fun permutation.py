t=int(input())
for _ in range(t):
    n=int(input())
    q=[]
    p=list(map(int,input().split()))
    for i in range(n):
        q.append(n+1-p[i])
    print(*q)
