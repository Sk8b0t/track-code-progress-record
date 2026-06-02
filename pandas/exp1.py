import pandas as pd
d= pd.DataFrame({
    "Name": ["A", "B", None, "D", "E"],
    "Age": [20, None, 20, 21, None],
    "Salary": [25000, 30000, None, 40000, 35000],
    "Department": ["IT", "HR", "IT", None, "Finance"]
})
df=pd.DataFrame(d)
print(df)
print(df.count())
print(df.value_counts(dropna=False,ascending=False))
print(df.value_counts("Department",ascending=True))