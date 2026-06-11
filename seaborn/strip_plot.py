import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset('Penguins')
# sns.stripplot()
print(df)
sns.stripplot(data=df,x='species',y='body_mass_g',hue='sex')
plt.show()