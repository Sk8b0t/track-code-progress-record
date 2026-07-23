t=int(input())
while t:
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
            if a[i]<b[i]:
                a[i]=b[i]

    for i in range(n-1,0,-1):
            if a[i-1]<a[i]:
                a[i-1]=a[i]

    pre=[0]*(n+1)
    for i in range(n):
        pre[i+1]=pre[i]+a[i]
       
   
    while q:
        l,r=map(int,input().split())
        print(pre[r]-pre[l-1],end=" ")

        q-=1
    print()
    t-=1