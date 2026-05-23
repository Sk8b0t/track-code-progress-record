import pandas as pd
d= pd.DataFrame({
    "Name": ["A", "B", None, "D", "E"],
    "Age": [20, None, 22, 21, None],
    "Salary": [25000, 30000, None, 40000, 35000],
    "Department": ["IT", "HR", "IT", None, "Finance"]
})
df=pd.DataFrame(d)
print(df)
print(df.isna().sum())
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].median())
df.dropna(subset=["Department"],inplace=True)
df["Name"]=df["Name"].fillna("Unknown")
df["Department"]=df["Department"].str.upper()
print(df.groupby("Department")["Salary"].mean())

print(df)

