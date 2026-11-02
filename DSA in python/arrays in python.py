import array
# from array import *
val=array.array('d',[1,2,3,4,5,6])
# print(val)

# for i in range(0,len(val)):
#     print(val[i],end=" ")
# print("\n")

# for i in val:
#     print(i,end=" ")
# print("\n")

# print(val.typecode)
# print(val.append(300))
# val.insert(3,69)
# val.reverse()
# print(val)
cpy=array.array(val.typecode,[x**2 for x in val])
cpy.pop(3)
print(cpy.index(9))
print(cpy)

