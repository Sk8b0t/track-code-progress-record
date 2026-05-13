t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    fa={}
    fb={}
    cnt=0
    ele=a[0]
    a.append(-1)
    for i in range(n+1):
        if a[i]==ele:
            cnt+=1
        else:
            if a[i-1] not in fa:
                fa[a[i-1]]=0
            fa[a[i-1]]=max(fa[a[i-1]],cnt)
            ele=a[i]
            cnt=1
    cnt=0
    ele=b[0]
    b.append(-1)
    for i in range(n+1):
        if b[i]==ele:
            cnt+=1
        else:
            if b[i-1] not in fb:
                fb[b[i-1]]=0
            fb[b[i-1]]=max(fb[b[i-1]],cnt)
            ele=b[i]
            cnt=1
    m=m1=0

    for key in fa:
        if key not in fb:
            fb[key]=0
        m=max(m,fa[key]+fb[key])
    
    for key in fb:
        if key not in fa:
            fa[key]=0
        m1=max(m1,fa[key]+fb[key])
    print(max(m,m1))
    
    t-=1