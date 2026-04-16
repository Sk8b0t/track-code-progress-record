import math
n = int(input())
a = list(map(int, input().split()))
    
common_gcd = a[0]
for i in range(1, n):
        common_gcd = math.gcd(common_gcd, a[i])
    
for x in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]: 
     if common_gcd % x != 0:
            print(x)
            break
# x = 2
# while True:
#         if common_gcd % x != 0:
#             print(x)
#             break
#         x += 1