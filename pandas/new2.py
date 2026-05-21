import pandas as pd
padho=pd.read_csv("Team.csv")
print(padho)
padho.index=[i for i in range(1,6)]
print(padho)
padho.to_csv("Team.csv")