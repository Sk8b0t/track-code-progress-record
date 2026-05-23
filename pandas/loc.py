import numpy as np
import pandas as pd
df=pd.read_csv("random.csv")
print(df.loc[[1,2],['A','B']])
print(df.loc[:,['E','A']])
print(df.loc[:,:])
print(df.loc[(df['A']>4) & (df['C']<3)])
print(df.iloc[9,5])
df.drop([1,4,7],axis=0,inplace=True)
print(df)
print(df.reset_index(drop=True))
print(df.shape)
print(df.info())