t=int(input())
while t:
    n=int(input())
    print(*[i for i in range(1,n+1)][::-1])
    t-=1