class Employee:
  def __init__(self,sal):
    self.salary=sal
  @property
  def salary(self):
        return self.sal
        
  @salary.setter
  def salary(self,s):
    if s>=10000 and s<=100000:
         self.sal=s
    else:
     self.sal=10000

e = Employee(5000)
print(e.salary)     # 10000
e.salary = 90000
print(e.salary)     # 90000
