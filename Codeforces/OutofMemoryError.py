t=int(input())
while t:
    n,m,h=map(int,input().split())
    a=list(map(int,input().split()))
    a1=a[:]
    modified_index=[]
    for _ in range(m):
        b,c=map(int,input().split())
        idx=b-1
        a1[idx]+=c
        modified_index.append(idx)
        if a1[idx]>h:
            for index in modified_index:
                a1[index]=a[index]
            modified_index=[]
    print(*a1)







    t-=1