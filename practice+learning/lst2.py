lst = ["hello", "world", "aeiou"]
lst2 = []
a = ""
cnt = 0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] != 'a' and lst[i][j] != 'e' and lst[i][j] != 'i' and lst[i][j] != 'o' and lst[i][j] != 'u':
            a += lst[i][j]
            cnt += 1
    if cnt > 0:
        lst2.append(a[::-1])
        a = ""
        cnt = 0
    else:
        lst2.append("NO_Vowel")
print(lst2)
