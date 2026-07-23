t=int(input())
for _m in range(t):
    n=int(input())
    if n<=3:
        print(n)
    else:
        n1=n//2
        n2=n-n1
        print(n2-n1)