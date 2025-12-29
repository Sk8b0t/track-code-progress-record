t = int(input())
n = []
x = []
for i in range(t):
   x.append(int(input("Enter the value of x")))
   n.append(int(input("Enter the value of n")))
for i in range(t):
    if x[i] >= 1 and n[i] <= 10:
        if n[i] % 2 == 0:
            print(0)
        else:
            print(x[i])
