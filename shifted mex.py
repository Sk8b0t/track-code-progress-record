t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    new_a=sorted(list(set(a)))
    best=curr=0
    for i in range(len(new_a)):
        if i==0 or new_a[i]==new_a[i-1]+1:
            curr+=1
        else:
            curr=1
        if best<curr:
            best=curr
    print(best)
        
    t-=1