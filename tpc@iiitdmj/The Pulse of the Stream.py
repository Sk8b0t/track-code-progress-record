t=int(input())
while t:
    freq={}
    cnt=0
    n=int(input())
    a=list(map(int,input().split()))
    for idx,val in enumerate(a):
        pos=idx+1
        r=pos-val
        if r in freq:
            cnt+=freq[r]
        l=val+pos
        if l in freq:
            freq[l]+=1
        else:
            freq[l]=1
    print(cnt)
    t-=1

