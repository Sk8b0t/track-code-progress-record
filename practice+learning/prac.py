class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        if self._age<0:
            return 0
        return self._age
    @age.setter
    def age(self,s):
        self._age=s


if __name__ == '__main__':
    p = Person(-5)
    print(p.age)
    p.age=20
    print(p.age)
