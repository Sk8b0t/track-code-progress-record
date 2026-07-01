# GCD of two numbers without functions
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    t = b
    b = a % b
    a = t
print("GCD is:", a)
