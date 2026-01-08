t=int(input())
for _ in range(t):
    cnt=0
    n=int(input())
    lst=list(map(int,input().split()))
    maxNow=lst[0]
    for i in range(n):
        if maxNow>lst[i]:
            cnt+=1
        else:
            maxNow=lst[i]
        
    print(cnt)
