t = int(input())

while t:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans=[]
    for i in range(n):
        r=a[i]%k
        if r==0:
            r=k
        ans.append((-r,i+1))
    ans.sort()
    for _,index in ans:
        print(index,end=" ")
    print()
        

    t -= 1