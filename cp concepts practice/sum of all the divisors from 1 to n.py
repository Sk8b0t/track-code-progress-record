sum=0
n=int(input("Enter a number :"))
for i in range(1,n):
    sum+=(n//i)*i
print("Sum of all divisors=",sum)
       
