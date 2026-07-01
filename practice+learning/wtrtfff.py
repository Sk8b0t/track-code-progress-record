n=input("Enter a sentence: ")
lst = []
n += " "
d = {}
wrd = ""
for i in range(len(n)):
    if n[i] != " ":
        wrd += n[i]
    else:
        lst.append(wrd)
        wrd = ""
cnt = 0
for word in lst:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

for i in d:
    print(f"{i} : {d[i]}")
