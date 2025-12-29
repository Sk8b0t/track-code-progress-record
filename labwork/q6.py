# write a python program to to check whether a no. is divisible by both  3 and 5
n1 = int(input("Enter a number:"))

if n1 % 3 == 0 and n1 % 5 == 0:
    print("divisible")
else:
    print("not divisible")
