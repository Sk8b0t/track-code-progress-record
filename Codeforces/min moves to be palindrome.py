#calculates no. of minimum moves to be a palindrome provided that the input can be palindromed
s=input("Enter a word:")
n=list(s)
mov=0
while n:
    i=n.index(n[-1])
    if i==len(n)-1:
        mov+=len(n)//2
    else:
        mov+=i
        n.pop(i)
    n.pop()

print(mov)
