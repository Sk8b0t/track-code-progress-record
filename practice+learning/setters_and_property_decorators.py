class Employee():
    def __init__(self, f, l):
        self.fname = f
        self.lname = l

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return "email is not set"
        return f"{self.fname}.{self.lname}@iiitdmj.ac.in"

    @email.setter
    def email(self, s):
        self.fname, self.lname = map(str, s.split("@")[0].split("."))

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    def AllMethods(self):
        with open("sayannnn.txt","w") as f:
            for item in dir(Employee):
                f.write(item+"\n")



if __name__ == '__main__':
    njr = Employee("Neymar", "Jr")
    m10 = Employee("Lionel", "Messi")
    njr.fname = "sayan"
    print(njr.email)
    njr.email = "tmkc.fk@iiitdmj.ac.in"
    print(njr.email)
    del njr.email
    print(njr.email)
    skillf=Employee("Skill","F")
    print(skillf.email)
    o="pookie"
    print(dir(o))
    print(dir(skillf))
    skillf.AllMethods()
    import inspect
    print(inspect.getmembers(skillf))
    