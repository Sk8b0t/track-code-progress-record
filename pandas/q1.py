import pandas as pd
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Math": [78, 90, 67, 88, 95, 70],
    "Physics": [80, 85, 70, 92, 96, 65],
    "Chemistry": [75, 89, 72, 90, 98, 60]
})
df.loc[:,["Average"]]=(df.loc[:,"Math"]+df.loc[:,"Physics"]+df.loc[:,"Chemistry"])/3
print(df)
print("Topper marks:",df["Average"].max())
print(df.sort_values(by="Average",ascending=False))
abv=df[(df['Math']>85) & (df["Physics"]>85) & (df["Chemistry"]>85)]
print("students above 85 marks in all subjects are:\n")
print(abv)
# df["Result"]="Pass" if df["Average"]>=75 else "Fail"
df.loc[:,"Result"]="Fail"
df.loc[df["Average"]>=75,"Result"]="Pass"
print(df)




