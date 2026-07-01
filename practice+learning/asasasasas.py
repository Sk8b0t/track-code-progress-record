# dsict = {"key1": 7, "DUP_test": 2, "dup_key": 4}
lst = [("key1", 5), ("key1", 2), ("DUP_key", 1), ("dup_test", 7)]
result = {}
for item in lst:
    if item[0] in result:
        result[item[0]] += item[1]
    else:
        result[item[0]] = item[1]

for key in result:
    if key[0:3].lower() == "dup":
        result[key] = result[key] * 2

print(result)
