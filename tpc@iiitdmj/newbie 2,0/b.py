n=int(input())
per=2*(n+1)

for i in range(1,int(n**0.5)+1):
    if n%i==0:
        p=2*(i+(n//i))
        if per>p:
            per=p 
print(per)
