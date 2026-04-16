t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    M=0
    cnt=0
    for item in a:
        if item%2==0:
            cnt+=1
        if item%k==0:
            ans=0
            break
        if item%k>M:
            M=item%k
        ans=k-M
    if k==4:
        if cnt>=2:
            ans=min(ans,0)
        elif cnt==1:
            ans=min(ans,1)
        else:
            ans=min(ans,2)
    print(ans)
    t-=1