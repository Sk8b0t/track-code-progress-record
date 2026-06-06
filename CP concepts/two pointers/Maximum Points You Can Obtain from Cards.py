arr=[1,7,4,5,6,3,5,2]
k=4
rs=ls=0

for i in range(k):
    ls+=arr[i]

ms=ls
rind=len(arr)-1

for i in range(k-1,-1,-1):
    ls-=arr[i]
    rs+=arr[rind]
    rind-=1
    ms=max(ms,ls+rs)
print(ms)