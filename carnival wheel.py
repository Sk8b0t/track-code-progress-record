t=int(input())
for _ in range(t):
    l,a,b=map(int,input().split())
    amod,max=a,a
    lst=[]
    while amod not in lst:
        lst.append(amod)
        if amod>max:
            max=amod
        amod=(amod+b)%l
print(max)
