t=int(input())
while t:
    n,r,b=map(int,input().split())
    rlen=r//(b+1)
    rem=r-(rlen *(b+1))
    s=[]
    bcnt=0
    irem=rem
    for i in range(1,b+2):
        s.extend(["R"]*rlen)
        if rem>0:
            s.append("R")
            rem-=1
        if bcnt!=b:
            s.append("B")
            bcnt+=1
       
    for i in s:
        print(i,end="")
    print()

    t-=1