t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    freq={}
    for item in a:
        if item not in freq:
            freq[item]=1
        else:
            freq[item]+=1
    i,miss=0,0
    while(i<k):
        if i not in freq:
            miss+=1
        i+=1
    kcnt=0
    if k in freq:
        kcnt=freq[k]
    print(miss if miss>kcnt else kcnt)