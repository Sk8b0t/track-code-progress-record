t=int(input())
for _ in range(t):
    n,k=map(int , input().split())
    s=input()
    sleep=0
    i=0
    while(i<n):
        if s[i]=='1':
            i+=(k+1)
        else:
            sleep+=1
            i+=1
    print(sleep)

