class A:
    clsvar1 = "I am a variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.clsvar1 = "Instance variable of class A"
        self.spd = "I am red ranger in A"
-0-=

class B(A):
    clsvar1 = "I am in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.clsvar1 = "Instance variable of class B"


if __name__ == '__main__':
    a = A()
    b = B()
    print(a.clsvar1)
    print(b.clsvar1)
    print(b.spd)
