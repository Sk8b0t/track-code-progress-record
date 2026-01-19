
s=input()
m=int(input())
pre=[0]*(len(s)+1)
cnt=0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cnt+=1
    pre[i+1]+=cnt


while m:
    l,r=map(int,input().split())
    print(pre[r]-pre[l])

    



    m-=1