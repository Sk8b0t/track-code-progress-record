t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    M=0
    cnt=ans=wtf=0
    for item in a :
        if item%2==0:
            cnt+=1
        if item%k==0:
            ans=0
            break
        if item%k>M:
             M=item%k
        ans=k-M
    
    if k==4:
        if cnt>=2:
            ans=min(ans,0)
        elif cnt==1:
            ans=min(ans,1)
        else:
            ans=min(ans,2)
    print(ans)
    t-=1


# import sys

# input = sys.stdin.read

# data = input().split()

# index = 0

# t = int(data[index]) # Read the number of test cases
# index += 1

# results = []

# for _ in range(t):
# 	n = int(data[index]) # Read the size of the array
# 	k = int(data[index + 1]) # Read the divisor k
# 	index += 2

# 	a = list(map(int, data[index:index + n])) # Read the array elements
# 	index += n

# 	ans = float('inf') # Initialize the minimum operations to a large value
# 	even_count = 0 # Count of even numbers in the array

# 	for num in a:
# 		if num % 2 == 0:
# 			even_count += 1 # Increment even_count if the element is even
# 		if num % k == 0:
# 			ans = 0 # If any element is divisible by k, no operations are needed
# 		ans = min(ans, (k - num % k)) # Calculate the minimum operations needed

# 	# Special handling for k = 4
# 	if k == 4:
# 		if even_count >= 2:
# 			ans = min(ans, 0) # If there are at least two even numbers, no operations are needed
# 		elif even_count == 1:
# 			ans = min(ans, 1) # If there is one even number, one operation is needed
# 		elif even_count == 0:
# 			ans = min(ans, 2) # If there are no even numbers, two operations are needed

# 	results.append(ans)

# for result in results:
# 	print(result) # Output the minimum number of operations