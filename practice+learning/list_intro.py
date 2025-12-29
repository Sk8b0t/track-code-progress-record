lst = ["hello", "world", "aeiou"]
a = ""
lst2 = []
cnt = 0
for item in lst:
    for wrd in item:
        if wrd not in "aeiou":
            a += wrd
            cnt += 1
    if cnt > 0:
        lst2.append(a[::-1])
        a = ""
        cnt = 0
    else:
        lst2.append("No_Vowel")

print(lst2)
