l=r=0
ml=0
nums=[1,1,1,0,0,1,1,1,1,1,1]
while(r<len(nums)):
    if nums[r]==1:
        ml=max(ml,r-l+1)
    else:
        l=r+1
    r+=1
print(ml)