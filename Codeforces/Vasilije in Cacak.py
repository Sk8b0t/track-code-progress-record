t=int(input())
while t:
    n,k,x=map(int,input().split())
    print("YES") if ((k*(k+1))//2)<=x<=(n*k - (k*(k-1))//2) else print("NO")
    t-=1