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
   #IT GIVES TLE 
# t=int(input())
# while t:
#     n,k=map(int,input().split())
#     a=list(map(int,input().split()))
#     newa=[]
#     while(len(newa)!=n):
#         ind=a.index(max(a))
#         a[ind]-=k
#         if a[ind]<=0:
#             newa.append(ind+1)
#     print(*newa)



#     t-=1