import numpy as np
import pandas as pd

d1={
    "name": ["Sayan","Neymar Jr","Raphinha","Casemiro","Endrick"],
    "jersey no.": [95,10,11,5,20],
    "Country":["India","Brasil","Brasil","Brasil","Brazil"]

}

df=pd.DataFrame(d1)

print(df)
# df.to_csv("Team.csv")
df.to_csv("Team.csv",index=False)

print(df.head(2)) #shows 1st two rows of the csv
print(df.tail(2)) #shows bottom 2 elements of the csv
print(df.describe()) #shows the statistics of the columns which contain numbes 