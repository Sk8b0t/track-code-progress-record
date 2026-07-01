# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     print(" " * (rows - i), end="")
#     print("* " * i)
for i in range(1, 5):
    for j in range(4, i, -1):
        print(" ", end="")
    print("* " * i)
