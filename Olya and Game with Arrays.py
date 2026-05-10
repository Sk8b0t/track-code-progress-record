t=int(input())
while t:
    a=[]
    sum=0
    n=int(input())

    for i in range(n):
        m=int(input())
        x=sorted(list(map(int,input().split())))
        a.append(x)

    lowa=a[0][0]
    lowb=a[0][1]
    
    for i in range(n):
        sum+=a[i][1]
        if a[i][0]<lowa:
            lowa=a[i][0]
        if a[i][1]<lowb:
            lowb=a[i][1]          
    print(sum-lowb+lowa)

    t-=1