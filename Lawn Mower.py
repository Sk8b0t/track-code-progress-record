t=int(input())
while t:
    n,w=map(int,input().split())
    cnt=0
    bst=0
    for i in range(n):
        if cnt<w-1:
            cnt+=1
        else:
            bst+=cnt
            cnt=0
    bst+=cnt
    print(bst)

    t-=1