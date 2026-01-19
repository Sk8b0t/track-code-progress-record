n=int(input())
x=list(map(int,input().split()))
q=int(input())
x.sort()
while q:
    m=int(input())
    right=n-1
    left=mid=0
    while(left<=right):
        mid=(left+right)//2
        if x[mid]<=m:
            left=mid+1
        else:
            right=mid-1
    print(left)

    q-=1