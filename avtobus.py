t=int(input())
while t:
    n=int(input())
    if n%2==0 and n>=4:
        print((n+5)//6,n//4)
    else:
        print(-1)

    
    t-=1
