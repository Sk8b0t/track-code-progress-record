t=int(input())
while t:
    n,x1,x2,k=map(int,input().split())
    x=abs(x1-x2)
    ans=min(x,n-x)
    print(1) if n==2 or n==3 else print(ans+k)
    
    t-=1