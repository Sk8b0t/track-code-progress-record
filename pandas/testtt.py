import numpy as np
import pandas as pd 

data = {
    'Name': ['Aparna', 'Pankaj', 'Ram', 'Ramesh', 'Naveen', 'Krrishnav', 'Bhawna'],
    'Degree': ['MBA', 'BCA', 'M.Tech', 'MBA', np.nan, 'BCA', 'MBA'],
    'Score': [90.0, np.nan, 80.0, 98.0, 97.0, 78.0, 89.0]
}
df=pd.DataFrame(data)
print(df)
print(df.groupby("Degree")["Score"].max())