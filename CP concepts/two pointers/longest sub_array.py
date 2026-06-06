arr=[1,2,3,5,6,3,5,2]
# optimal sol.
# k=14
# max_len=0
# r=l=0
# sum=0
# while(r<len(arr)):
#     sum+=arr[r]
#     if sum<=k:
#         max_len=max(max_len,r-l+1)
#     else:
#         sum-=arr[l]
#         l+=1
#     r+=1
# print(max_len)


k=14
l=r=ml=0
sum=0
while(r<len(arr)):
    sum+=arr[r]
    while(sum>k):
        sum-=arr[l]
        l+=1
    if sum<=k:
        ml=max(ml,r-l+1)
    r+=1
    
print(ml)
    



