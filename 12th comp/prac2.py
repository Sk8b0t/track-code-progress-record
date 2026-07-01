def push(stk, value):
    stk.append(value)


def pop(stk):
    if len(stk) == 0:
        print("underflow")
    else:
        print("deleted element=",stk[len(stk)-1])
        stk.pop()


def display(stk):
    print(stk[::-1])


stack = []
print("press 1 for push")
print("press 2 for pop")
print("press 3 for display")
print("press 4 for exit")
while True:
    ch = int(input("Enter your choice: "))
    if ch == 1:
        push(stack, int(input("Enter the value to be stored in the stack:")))
    elif ch == 2:
        pop(stack)
    elif ch == 3:
        display(stack)
    else:
        break
