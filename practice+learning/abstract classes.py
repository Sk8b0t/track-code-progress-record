from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, len, br):
        self.len = len
        self.br = br

    def area(self):
        return f"The area of rectangle is {self.len * self.br}"


if __name__ == '__main__':
    r = Rectangle(6, 7)
    print(r.area())
