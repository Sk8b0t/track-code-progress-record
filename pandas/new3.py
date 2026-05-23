import pandas as pd
import numpy as np

# print(pd.Series(np.random.rand(10)))
ser=pd.Series(np.random.rand(10))
print(ser)
print(type(ser))
df=pd.DataFrame(np.random.rand(10,5)*10,index=np.arange(1,11),columns=list("ABCDE"))
df.to_csv("random.csv")
print(type(df))
print(df)
print(df.dtypes)
print(df.index)
print(df.sort_index(axis=1,ascending=False))
print(df['E'].describe())
print(type(df["E"]))
# df.columns=list("ABCDE")
print(df)
df.loc[2,0]="Sayan"
df.loc[1,"E"]=69
print(df)
df=df.drop(0,axis=1).copy()
print(df)
print(df.loc[[7,8],['A','C']])
print(df.drop(['A','E'],axis=1))