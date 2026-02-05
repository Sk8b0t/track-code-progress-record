t=int(input())
while t:
    n=int(input())
    a=input().split()
    s=a[0]
    for i in range(1,n):
        if s+a[i]< a[i]+s:
            s=s+a[i]
        else:
            s=a[i]+s
        
    print(s)

        
            
        



    t-=1