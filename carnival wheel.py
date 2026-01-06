t=int(input())
for i in range(t):
    l,a,b=map(int,input().split())
    lst=[]
    pos,max=a,a
    while pos not in lst:
        lst.append(pos)
        if pos>max:
            max=pos
        pos=(pos+b)%l
print(max)

