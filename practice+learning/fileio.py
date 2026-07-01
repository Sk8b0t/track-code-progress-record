# wrd = ""
# d = {}
# with open("Mary Kom.txt", "r+") as f:
#     for item in f.readlines():
#         item+=" "
#         for i in item:
#             if i != " " and i != "\n":
#                 wrd += i
#             else:
#                 if wrd!="":
#                     wrd=wrd.lower()
#                     if wrd not in d:
#                         d[wrd] = 1
#                     else:
#                         d[wrd] += 1
#                     wrd = ""
#
# print(d)
d={}
itemlst=[]
wrd=""
with open("Mary Kom.txt","r+") as f:
    for item in f.readlines():
        for p in [",", ".", "!", "?", ";", ":"]:
            item=item.replace(p,"")
        itemlst=item.lower().split()
        for item in itemlst:
            if item not in d:
                d[item]=1
            else:
                d[item]+=1
for key in d:
    print(f"{key}={d[key]}")


