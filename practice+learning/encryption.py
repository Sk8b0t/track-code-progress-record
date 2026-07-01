def decrypt(n):
    lst = []
    r = ""
    for i in n:
        lst.append(i)
    try:
        for i in range(len(lst) // 2):
            lst[i], lst[i + 3] = lst[i + 3], lst[i]

        for i in lst:
            r += i
        return r
    except Exception as e:
        print("Enter a code of length greater than 4")


n = input("Enter a sentence: ")
for i in n.split():
    print(decrypt(i), end=" ")
