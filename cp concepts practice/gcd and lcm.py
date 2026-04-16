import math
def gcd(b,a):
    return b if a==0 else gcd(a,b%a)

print(gcd(24,210))

# print(gcd(12,18))
# print((12*18)//gcd(12,18))
# print(math.gcd(18,12))
# print(math.lcm(12,18))