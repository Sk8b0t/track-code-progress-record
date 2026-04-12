n=int(input("Enter a number"))
import math
prime=[1]*(n+1)

for i in range(2,int(n**0.5)):
    for j in range(i*i,n,i):
        prime[j]=0
for i in range(2,n):
    print(i) if prime[i]==1 else None