class Employee:
    no_of_leaves = 8

    def __init__(self, name, sal, role):
        self.name = name
        self.salary = sal
        self.role = role

    def printdetails(self):
        print(f"{self.name} earns {self.salary} as a {self.role}")

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod
    def dashInp(cls, data_as_string):
        # lst=data_as_string.split("-")
        # return cls(lst[0],lst[1],lst[2])
        return cls(*data_as_string.split("-"))

    @staticmethod
    def printEmp():
        print("this is a method of the Employee class")


class Programmer(Employee):
    def __init__(self, name, sal, lang):
        self.name = name
        self.salary = sal
        self.languages = lang

    def printInfo(self):
        print(f"{self.name} earns {self.salary} as a programmer and knows {self.languages}")

class Player:
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printGame(self):
        print(f"{self.name} plays {self.game} ")

class coolProgrammer(Player,Employee):
    lang = "TypeScript"
    def printLanguages(self):
        lang="TypeScript"
        print(f"{self.name} knows {self.lang}")






if __name__ == '__main__':
    e1 = Employee("Sayan", "30000000000", "CEO")
    e2 = Employee("Nayas", "900000000", "COO")
    e3 = Employee.dashInp("Likhitha-9000000-SDE")

    e4 = Programmer("Sayan", "30000000000", ["python", "C", "Java", "HTML"])
    e5 = Programmer("Sayan", "30000000000", "Python")

    e6=coolProgrammer("Sayan","Football")

    e1.printdetails()
    e2.printdetails()
    e1.no_of_leaves = 9
    e1.changeLeaves(12)
    print(e3.__dict__)
    e1.printEmp()
    Employee.printEmp()

    e4.printInfo()
    e6.printLanguages()
    e6.printGame()

