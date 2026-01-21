# to print all prime numbers upto n using sieve of eratothenes
import math

n = int(input())
pre = [True] * (n + 1)
pre[0] = False
pre[1] = False
for i in range(2, int(math.sqrt(n) + 1)):
    if pre[i] == True:
        for j in range(i * i, n + 1, i):
            pre[j] = False
for index, val in enumerate(pre):
    if val == True:
        print(index, end=" ")
