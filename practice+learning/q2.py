# class Student:
#     def __init__(self,roll):
#         self.roll=roll
#     @property
#     def roll_no(self):
#         return self.roll
# s=Student(12)
# print(s.roll_no)

class User:
    def __init__(self,n):
        self.username=n

    @property
    def username(self):
        return self._name
    
    @username.setter
    def username(self,s):
        self._name=s.strip().lower()

if __name__ == '__main__':
    u=User("  SayanBISWAS ")
    print(u.username)
    
    
