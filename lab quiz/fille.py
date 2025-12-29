d1 = {"Sayan": 1, "Nayas": 2, "Likitha": 1, "NeymarJr": 2, "NJR": 69}
d2 = {}
# for key in d1:
#     if d1[key] in d2:
#         d2[d1[key]].append(key)
#     else:
#         d2[d1[key]] = []
#         d2[d1[key]].append(key)
for key in d1:
    if d1[key] not in d2:
        d2[d1[key]] = []
    d2[d1[key]].append(key)
lst = []
# for key in d2:
#     if len(d2[key]) > 1:
#         for item in d2[key]:
#             lst.append(item)

for val, names in d2.items():
    if len(names) > 1:
        lst.extend(names)
print(tuple(lst))
