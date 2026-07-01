from setters_and_property_decorators import Employee
import inspect
e=Employee("Sayan","Biswas")
with open("sayan1.txt","w") as f:
    for item in inspect.getmembers(e):
        for tup1 in item:
            f.write(str(tup1)+" ")
        f.write("\n")
#EITHER import inspect or use dir(write here) to know all the methods and attrivutes associated with it 
