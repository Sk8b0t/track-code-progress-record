#COSNTANT WINDOW
arr=[-1,2,3,5,6,-3,5,2]
k=4
l=0
r=k-1
sum=0
max_sum=0
for i in range(k):
    sum+=arr[i]

while(r<len(arr)-1):
    sum-=arr[l]
    l+=1
    r+=1
    sum+=arr[r]
    max_sum=max(max_sum,sum)
print(max_sum)