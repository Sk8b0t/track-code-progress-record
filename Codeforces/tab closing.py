t=int(input())
for _ in range(t):
    a,b,n=map(int,input().split())
    m,cnt,prev,tlen=n,0,0,0
    while(m!=0):
        tlen=min(b,a//m)
        if prev!=tlen:
         cnt+=1
        prev=tlen      
        m-=1
    print(cnt)

