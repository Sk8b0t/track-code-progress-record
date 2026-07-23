t=int(input())
for i in range(t):
    R,X,D,n=map(int,input().split())
    div=input().strip()
    print(div)
    # divisions=input()
    # div=[]
    # for i in range(len(divisions)):
    #     div.append(int(divisions[i]))
    
    r=R
    cnt=0
    for j in range(n):
        if div[j]=='1':
            r-=D
            cnt+=1
        else:
            if r<X:
                r-=D
                cnt+=1
    print(cnt)

