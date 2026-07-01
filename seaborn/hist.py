import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset('Penguins')
# sns.stripplot()
print(df)
sns.set_context('paper')
sns.set_style('whitegrid')
# sns.histplot(data=df,x='species',hue='sex',multiple="stack")
sns.regplot(data=df,x='flipper_length_mm',y='body_mass_g',color='red')
plt.show()
