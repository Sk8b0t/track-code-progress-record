n = "PAPER"
lst = []
for i in n:
    lst.append(i)
try:
    for i in range(len(lst) // 2):
        lst[i], lst[i + 3] = lst[i + 3], lst[i]
    for i in lst:
        print(i, end="")

except Exception as e:
    print("Enter a code of length greater than 4")
