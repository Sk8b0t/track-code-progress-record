t=int(input())
for _ in range(t):
    n,m,x=map(int,input().split())
    if n>m:
        print(n%m *x)
    else:
        print((m-n)*x)