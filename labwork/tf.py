# sol.1
# import numpy as np
# arr=np.arrange(1,21)
# print("Mean:",np.mean(arr))
# print("Median:",np.median(arr))
# print("Standard Deviaton:",np.std(arr))
#
#
# import numpy as np
# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6], [7, 8, 9]])
# print("Transpose:\n", matrix.T)
# print("Sum of all the elements:", np.sum(matrix))
#
#
# sol.4
# import numpy as np
# from matplotlib import pyplot as plt
# x=np.arange(-10,11)
# y=x**2
# plt.plot(x,y,color='green',marker='o')
# plt.title("Parabola: y=x^2")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.grid(True)
# plt.show()
#
# sol 6
# from matplotlib import pyplot as plt
# classes = ['A', 'B', 'C', 'D']
# students = [20, 25, 30, 22]
# plt.bar(classes, students,color='black')
# plt.title("students per class")
# plt.xlabel("class")
# plt.ylabel("number of students")
# plt.show()
#
# sol.6
# import time
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#
#     def start(self):
#         print("Loading",end="")
#         for i in range(5):
#             time.sleep(1)
#             print("..",end="")
#         print("\n")
#         print(f"{self.color} {self.brand} has started")
#
#
#     def stop(self):
#         print(f"{self.color} {self.brand} has stopped")
#
#
# if __name__ == '__main__':
#     myCar = Car("Lamborghini", "Black")
#     myCar.start()
#     myCar.stop()
#
#
# sol 7
# class Student:
#     def __init__(self,n,m):
#         self.name=n
#         self.marks=m
#
# s1=Student("Sayan",10)
# s2=Student("Nayas",30)
# print(s1.__dict__)
# print(s2.__dict__)
#
# sol 8
# class BankAccount:
#
#     def __init__(self, b=0):
#         self.balance = b
#
#     def deposit(self, amt):
#         self.balance += amt
#         print(f"deposited amount={amt}")
#
#     def nikalo(self, amt):
#         if amt < self.balance:
#             self.balance -= amt
#         else:
#             print("Insufficient balance")
#
#     def displayBalance(self):
#         print(self.__dict__)
#
# acc = BankAccount(1000)
# acc.deposit(500)
# acc.nikalo(300)
# acc.displayBalance()
#
# sol 9
# class Parent:
#     def dekhoParent(self):
#         print("This is the parent class")
# class Child(Parent):
#     def dekhoChild(self):
#         print("This is the child class, inherited from parent")
# obj=Child()
# obj.dekhoParent()
# obj.dekhoChild()
#
