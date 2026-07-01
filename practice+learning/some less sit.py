# import math
#
# ls = []
# for i in range( 50):
#     if i % 3 == 0:
#         ls.append(i)
#     if (100 - i) % 3 == 0:
#         ls.append(100 - i)
# ls.sort()
# print(*ls)
print(*[i for i in range(100) if i%3==0])
d={i:f"item {i}" for i in range(1,10) if i%3==0}
print(d)
d={val:key for key,val in d.items()}
print(d)
s={i for i in [j for j in range(5)]}
print(s)
