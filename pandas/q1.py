import numpy as np
import pandas as pd
df=pd.DataFrame(np.random.rand(3,2)*10,index=[f"row{i}" for i in range(3)],columns=[f"column-{i}" for i in range(2)])
print(df)
print(df.describe())
print(df.mean())
print(df.corr())
print(df.std())
print("min:",df.min())
