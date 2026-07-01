import pandas as pd
employees = pd.DataFrame({
    "EmpID": [101,102,103,104,105],
    "Name": ["Alice","Bob","Charlie","David","Eva"],
    "DeptID": [1,2,1,3,2],
    "Salary": [50000,60000,55000,70000,65000]
})

departments = pd.DataFrame({
    "DeptID": [1,2,3],
    "Department": ["IT","HR","Finance"]
})

df=pd.merge(employees,departments,on="DeptID")
print(df)
print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
df1=df.set_index(["Department","Name"])
print(df.sort_values(by=["Department","Salary"],ascending=[True,False]))
a=df.groupby("Department")["Salary"].mean()
print(a[a>58000])

